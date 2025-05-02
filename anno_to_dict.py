import re
import json
import os

def parse_annotation_guidelines_markdown(markdown_string):
    """
    Parses structured Markdown annotation guidelines into a dictionary.

    Args:
        markdown_string: String with guidelines in specified Markdown format.

    Returns:
        Dictionary of categories and labels with descriptions, examples, and notes.
        Includes 'General Principles' and 'Additional Rules'.
    """
    guidelines_data = {}

    # State variables to track parsing context
    current_category = None
    current_label = None
    example_type = None # 'standard_examples' or 'other_examples'
    current_example = None # Dictionary for the example being built
    parsing_annotations = False # Flag for multi-line Annotations: blocks
    parsing_description = False
    current_notes = [] # Collects notes to attach later
    general_principles = [] # Collects text before the first category
    in_structured_section = False # True after the first category is encountered

    lines = markdown_string.splitlines()

    # --- Helper Functions ---

    def _attach_pending_notes():
        """Attaches collected notes to the current context (label, category, or general)."""
        nonlocal current_notes
        if not current_notes:
            return

        notes_to_attach = list(current_notes)
        current_notes = [] # Reset

        if current_label and current_category and current_label in guidelines_data.get(current_category, {}):
            guidelines_data[current_category][current_label]['notes'].extend(notes_to_attach)
        elif current_category and current_category in guidelines_data:
            if 'category_notes' not in guidelines_data[current_category]:
                guidelines_data[current_category]['category_notes'] = []
            guidelines_data[current_category]['category_notes'].extend(notes_to_attach)
        elif not in_structured_section:
            general_principles.extend([f"Hinweis: {n}" for n in notes_to_attach])
        else:
            if 'Additional Rules' not in guidelines_data:
                 guidelines_data['Additional Rules'] = []
            guidelines_data['Additional Rules'].extend([f"Hinweis: {n}" for n in notes_to_attach])

    def _finalize_current_example():
        """Adds the current example to the data if valid."""
        nonlocal current_example
        # Only add if it has text and annotations (at least an empty annotations list)
        if current_example and current_example.get('text') and current_example.get('annotations') is not None:
            # Ensure target list exists
            if current_category and current_label and example_type and \
               current_category in guidelines_data and current_label in guidelines_data[current_category]:
                 guidelines_data[current_category][current_label][example_type].append(current_example)

        current_example = None

    def _reset_block_parsing_states():
        """Resets flags for description/annotation blocks."""
        nonlocal parsing_annotations, parsing_description
        parsing_annotations = False
        parsing_description = False

    def _process_category(line):
        """Handles category heading lines."""
        nonlocal current_category, current_label, example_type, current_example, in_structured_section
        _attach_pending_notes()

        current_category = line.replace('### Kategorie:', '').strip()
        guidelines_data[current_category] = {}
        current_label = None
        example_type = None
        current_example = None
        _reset_block_parsing_states()
        in_structured_section = True

    def _process_label(line):
        """Handles label heading lines."""
        nonlocal current_label, example_type, current_example
        _attach_pending_notes()

        current_label = line.replace('#### Label:', '').strip()
        if current_category and current_category in guidelines_data:
            guidelines_data[current_category][current_label] = {
                'description': [],
                'standard_examples': [],
                'other_examples': [],
                'notes': []
            }
        example_type = None
        current_example = None
        _reset_block_parsing_states()

    def _process_section_heading(section_key):
        """Handles description, standard examples, other examples headings."""
        nonlocal example_type, parsing_description, parsing_annotations, current_example
        _finalize_current_example()

        if section_key == 'description':
            parsing_description = True
            example_type = None
        else: # 'standard_examples' or 'other_examples'
            example_type = section_key
            parsing_description = False

        parsing_annotations = False
        current_example = None

    def _process_note(line):
        """Handles note lines (* **Hinweis:**)."""
        nonlocal current_notes, current_example
        _finalize_current_example()

        note_text = line.replace('* **Hinweis:**', '').strip()
        current_notes.append(note_text)
        _reset_block_parsing_states()

    def _process_example_text(line):
        """Handles example text lines (* Text:)."""
        nonlocal current_example, parsing_annotations
        _finalize_current_example() # Finalize previous example if any

        if current_category and current_label and example_type and \
           current_category in guidelines_data and current_label in guidelines_data[current_category]:
            current_example = {
                'text': line.replace('* Text:', '').strip(),
                'annotations': [] # Initialize annotations list for the new example
            }
            # Do NOT reset parsing_annotations here, the next line might be 'Annotations:' or 'Annotation:'
            _reset_block_parsing_states() # Reset description state
        else:
            current_example = None
            _reset_block_parsing_states()

    def _process_annotations_header():
        """Handles 'Annotations:' or 'Annotation:' lines (multi-line start)."""
        nonlocal parsing_annotations
        if current_example is not None: # Only start parsing annotations if there's a current example being built
            parsing_annotations = True
        else:
             parsing_annotations = False
        nonlocal parsing_description
        parsing_description = False

    def _parse_and_add_list_annotation(line):
        """Parses and adds a single annotation from a list item (- [...])."""
        nonlocal current_example
        # Ensure we are inside an Annotations: block and have a valid example
        if parsing_annotations and current_example is not None and current_example.get('annotations') is not None:
            annotation_string = line.strip().lstrip('-').strip()
            annotation_match = re.match(r'\[Type:\s*(?P<type>[^,]+),\s*Value:\s*"(?P<value>[^"]+)"\]', annotation_string)
            if annotation_match:
                current_example['annotations'].append({
                    'type': annotation_match.group('type').strip(),
                    'value': annotation_match.group('value').strip()
                })

    def _parse_and_add_single_annotation(line):
        """Parses and adds a single annotation from an 'Annotation:' line."""
        nonlocal current_example
        # Ensure we have a valid example before trying to add an annotation
        if current_example is not None and current_example.get('annotations') is not None:
             # Extract the part of the line after 'Annotation:'
             annotation_part = line.replace('Annotation:', '', 1).strip() # Use count=1 to replace only the first occurrence
             # Parse the [Type: Value] part from annotation_part
             annotation_match = re.match(r'\[Type:\s*(?P<type>[^,]+),\s*Value:\s*"(?P<value>[^"]+)"\]', annotation_part)
             if annotation_match:
                  # Add the parsed annotation to the current example's annotations list
                  current_example['annotations'].append({
                      'type': annotation_match.group('type').strip(),
                      'value': annotation_match.group('value').strip()
                  })
             # After processing a single-line annotation, this example is complete
             _finalize_current_example()
             _reset_block_parsing_states() # Reset parsing states as this example block is finished


    def _process_description_line(line):
        """Handles lines within a description block."""
         # Ensure we are parsing description and have a valid label context
        if parsing_description and current_category and current_label and line.strip() and \
           current_category in guidelines_data and current_label in guidelines_data[current_category]:
             guidelines_data[current_category][current_label]['description'].append(line.strip())

    def _process_other(line):
        """Handles lines not matching specific patterns."""
        nonlocal in_structured_section, general_principles
        if not in_structured_section and line.strip():
             general_principles.append(line.strip())
        elif in_structured_section:
            # Any other non-empty line within a structured section likely breaks a block
            _finalize_current_example() # An unexpected line ends the current example/annotation block
            _reset_block_parsing_states()
            # Unstructured text within structured sections is ignored for now.


    # --- Main Parsing Loop ---
    for line in lines:
        stripped_line = line.rstrip()

        # Dispatch based on line type
        if stripped_line.startswith('### Kategorie:'):
            _process_category(stripped_line)
        elif stripped_line.startswith('#### Label:'):
            _process_label(stripped_line)
        elif stripped_line.startswith('##### Beschreibung:'):
             _process_section_heading('description')
        elif stripped_line.startswith('##### Standard Examples:'):
            _process_section_heading('standard_examples')
        elif stripped_line.startswith('##### Other Examples:'):
            _process_section_heading('other_examples')
        elif stripped_line.startswith('* **Hinweis:**'):
            _process_note(stripped_line)
        elif stripped_line.startswith('* Text:'):
            _process_example_text(stripped_line)
        elif stripped_line.strip() in ['Annotations:', 'Annotation:']:
            # This handles the header for multi-line annotations
            _process_annotations_header()
        elif stripped_line.strip().startswith('Annotation:'):
             # This handles the single-line annotation format immediately after Text:
             _parse_and_add_single_annotation(stripped_line)
        elif parsing_annotations and stripped_line.strip().startswith('- ['):
             # This handles list items within a multi-line Annotations: block
             _parse_and_add_list_annotation(stripped_line)
        elif parsing_description and stripped_line.strip():
            _process_description_line(stripped_line)
        elif not stripped_line: # Handle empty lines
            _reset_block_parsing_states() # Empty line ends description/annotation block
            pass # Empty lines do not break example or note collection in progress
        elif stripped_line.strip().startswith('#'):
            pass # Ignore other markdown headings
        else:
             _process_other(stripped_line)

    # --- Post-Loop Processing ---
    _finalize_current_example()
    _attach_pending_notes()

    # Join description lines
    for category in list(guidelines_data.keys()):
        if category not in ['General Principles', 'Additional Rules']:
            for label in list(guidelines_data[category].keys()):
                 if label != 'category_notes':
                    data = guidelines_data[category][label]
                    data['description'] = "\n".join(data['description']).strip() if data['description'] else None

    # Add general principles
    guidelines_data['General Principles'] = [p for p in general_principles if p.strip()]

    return guidelines_data

# --- Main execution block ---
if __name__ == "__main__":
    guidelines_file = "annotation_guidelines.md"
    # Construct the full path relative to the script's directory
    guidelines_path = os.path.join(os.path.dirname(__file__), guidelines_file)

    try:
        with open(guidelines_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        parsed_data = parse_annotation_guidelines_markdown(markdown_content)

        # Print the parsed dictionary using json for readability
        print("--- Parsed Annotation Guidelines Dictionary ---")
        print(json.dumps(parsed_data, indent=2, ensure_ascii=False))
        print("---------------------------------------------")

    except FileNotFoundError:
        print(f"Error: The file '{guidelines_file}' was not found in the same directory as the script.")
    except Exception as e:
        print(f"An error occurred: {e}")


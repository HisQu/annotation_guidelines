import re
import json
import os # Keep os for potential future use, though not strictly needed for the function itself

def parse_annotation_guidelines_markdown(markdown_string):
    """
    Parses structured Markdown annotation guidelines into a dictionary.

    Args:
        markdown_string: String with guidelines in specified Markdown format.

    Returns:
        Dictionary of categories and labels with descriptions, examples (including notes),
        and label notes. Includes 'General Principles' and 'Unklare Fälle'.
    """
    guidelines_data = {}

    # --- State Variables ---
    current_category = None
    current_label = None
    example_type = None  # 'standard_examples' or 'other_examples'
    current_example = None  # Dictionary for the example being built
    parsing_annotations = False  # Flag for multi-line Annotations: blocks
    parsing_description = False
    parsing_label_note = False # Flag for label-level ##### Hinweis section
    parsing_unclear_cases = False # Flag for the final section
    current_unclear_subsection = None # Key for the current subsection in Unklare Fälle
    current_notes = []  # Collects notes NOT attached to examples or labels directly
    general_principles = []  # Collects text before the first category
    in_structured_section = False  # True after the first category is encountered
    last_line_was_example_part = False # Flag to link notes to examples


    lines = markdown_string.splitlines()

    # --- Helper Functions ---

    def _attach_pending_notes():
        """Attaches collected general notes to the current context (label, category, or general)."""
        nonlocal current_notes
        if not current_notes:
            return

        notes_to_attach = list(current_notes)
        current_notes = [] # Reset

        # Prioritize attaching to the current label if one exists
        if current_label and current_category and current_label in guidelines_data.get(current_category, {}):
            # Ensure 'notes' list exists for the label
            if 'notes' not in guidelines_data[current_category][current_label]:
                 guidelines_data[current_category][current_label]['notes'] = []
            guidelines_data[current_category][current_label]['notes'].extend(notes_to_attach)
        # Fallback: attach to category if no specific label active (less likely with structure)
        elif current_category and current_category in guidelines_data:
            if 'category_notes' not in guidelines_data[current_category]:
                guidelines_data[current_category]['category_notes'] = []
            guidelines_data[current_category]['category_notes'].extend(notes_to_attach)
        # Fallback: If before structured section, add to general principles
        elif not in_structured_section:
             # Prefix with "Hinweis:" if not already done
             prefixed_notes = [f"Hinweis: {n}" if not n.lower().startswith("hinweis:") else n for n in notes_to_attach]
             general_principles.extend(prefixed_notes)
        # Fallback: General notes encountered after structure starts but not linked elsewhere (unlikely)
        # We will handle "Unklare Fälle" separately, so this shouldn't catch those notes.
        # else:
        #     # This path might be unnecessary if all notes are handled contextually
        #     print(f"Warning: Unattached notes found: {notes_to_attach}")


    def _finalize_current_example():
        """Adds the current example to the data if valid."""
        nonlocal current_example, last_line_was_example_part
        # Only add if it has text and annotations (at least an empty annotations list)
        if current_example and current_example.get('text') and current_example.get('annotations') is not None:
            # Ensure target list exists
            if current_category and current_label and example_type and \
               current_category in guidelines_data and current_label in guidelines_data[current_category]:
                # Ensure the example type list exists
                if example_type not in guidelines_data[current_category][current_label]:
                     guidelines_data[current_category][current_label][example_type] = []

                # Remove note property if it's None before appending
                if 'note' in current_example and current_example['note'] is None:
                    del current_example['note']
                guidelines_data[current_category][current_label][example_type].append(current_example)

        current_example = None
        last_line_was_example_part = False # Reset flag when example is finalized


    def _reset_block_parsing_states(reset_example_flag=True):
        """Resets flags for description/annotation/note blocks."""
        nonlocal parsing_annotations, parsing_description, parsing_label_note, last_line_was_example_part
        parsing_annotations = False
        parsing_description = False
        parsing_label_note = False
        if reset_example_flag:
            last_line_was_example_part = False # Reset unless explicitly told not to (e.g., within annotation block)

    def _process_category(line):
        """Handles category heading lines."""
        nonlocal current_category, current_label, example_type, current_example, in_structured_section
        _finalize_current_example()
        _attach_pending_notes() # Attach notes before starting new category

        current_category = line.replace('### Kategorie:', '').strip()
        if current_category not in guidelines_data:
             guidelines_data[current_category] = {}
        current_label = None
        example_type = None
        current_example = None
        _reset_block_parsing_states()
        in_structured_section = True

    def _process_label(line):
        """Handles label heading lines."""
        nonlocal current_label, example_type, current_example
        _finalize_current_example()
        _attach_pending_notes() # Attach notes before starting new label

        current_label = line.replace('#### Label:', '').strip()
        if current_category and current_category in guidelines_data:
            if current_label not in guidelines_data[current_category]:
                guidelines_data[current_category][current_label] = {
                    'description': [],
                    'standard_examples': [],
                    'other_examples': [],
                    'notes': [] # For label-level notes
                }
        else:
             print(f"Warning: Label '{current_label}' found without active category.")
             # Handle error or skip label? For now, skip adding it.
             current_label = None


        example_type = None
        current_example = None
        _reset_block_parsing_states()

    def _process_section_heading(section_key):
        """Handles description, standard examples, other examples headings."""
        nonlocal example_type, parsing_description, parsing_annotations, current_example
        _finalize_current_example() # Finalize any example before section change
        _reset_block_parsing_states() # Reset flags for the new section

        if section_key == 'description':
            parsing_description = True
            example_type = None
        else: # 'standard_examples' or 'other_examples'
            example_type = section_key
            parsing_description = False

        parsing_annotations = False
        current_example = None # Reset example buffer

    def _process_label_note_header():
         """Handles '##### Hinweis' headers."""
         nonlocal parsing_label_note
         _finalize_current_example() # Finish any pending example
         _reset_block_parsing_states() # Reset other block flags
         parsing_label_note = True     # Set flag for label note content

    def _process_example_note(line):
         """Handles example-specific note lines (* **Hinweis:**)."""
         nonlocal current_notes, current_example, last_line_was_example_part
         note_text = line.replace('* **Hinweis:**', '').strip()

         # If the last processed line was part of an example, attach note to it
         if last_line_was_example_part and current_example is not None:
              current_example['note'] = note_text
              # Keep last_line_was_example_part true, in case the note itself is multi-line (though unlikely with current format)
              # However, for simplicity now, assume notes are single lines and reset flag.
              # If multi-line notes for examples become a need, this needs adjustment.
              last_line_was_example_part = False # Note processed, reset flag
         else:
              # Otherwise, treat as a general note to be attached later
              current_notes.append(note_text)
              _reset_block_parsing_states() # A general note resets block states

    def _process_example_text(line):
        """Handles example text lines (* Text:)."""
        nonlocal current_example, parsing_annotations, last_line_was_example_part
        _finalize_current_example() # Finalize previous example if any

        if current_category and current_label and example_type and \
           current_category in guidelines_data and current_label in guidelines_data[current_category]:
            current_example = {
                'text': line.replace('* Text:', '').strip(),
                'annotations': [], # Initialize annotations list
                'note': None # Initialize note field
            }
            _reset_block_parsing_states() # Reset description/label note state
            last_line_was_example_part = True # Mark that we've started an example
        else:
            # This case should ideally not happen if structure is correct
            print(f"Warning: Example text found outside valid context: {line}")
            current_example = None
            _reset_block_parsing_states()


    def _process_annotations_header(line):
        """Handles 'Annotations:' or 'Annotation:' lines (multi-line start)."""
        nonlocal parsing_annotations, last_line_was_example_part
        if current_example is not None: # Only start parsing if there's an example
            parsing_annotations = True
            last_line_was_example_part = True # Mark as part of example structure
            _reset_block_parsing_states(reset_example_flag=False) # Keep example flag
        else:
             parsing_annotations = False # Cannot parse annotations without an example
             _reset_block_parsing_states()

    def _parse_and_add_list_annotation(line):
        """Parses and adds a single annotation from a list item (- [...])."""
        nonlocal current_example, last_line_was_example_part
        # Ensure we are inside an Annotations block and have a valid example
        if parsing_annotations and current_example is not None and current_example.get('annotations') is not None:
            annotation_string = line.strip().lstrip('-').strip()
            # Allow optional trailing period inside the quotes
            annotation_match = re.match(r'\[Type:\s*(?P<type>[^,]+),\s*Value:\s*"(?P<value>[^"]+?)\.?"\]', annotation_string)
            if annotation_match:
                current_example['annotations'].append({
                    'type': annotation_match.group('type').strip(),
                    'value': annotation_match.group('value').strip() # Store without trailing dot if present
                })
                last_line_was_example_part = True # Still part of the example
            else:
                print(f"Warning: Could not parse annotation list item: {line}")
                # Reset flag if parsing fails? Or assume it's still annotation context? Let's reset.
                _reset_block_parsing_states()
        else:
             _reset_block_parsing_states()


    def _parse_and_add_single_annotation(line):
        """Parses and adds a single annotation from an 'Annotation:' line."""
        nonlocal current_example, last_line_was_example_part
        # Ensure we have a valid example before trying to add an annotation
        if current_example is not None and current_example.get('annotations') is not None:
            # Extract the part of the line after 'Annotation:'
            # Use regex for flexibility with spacing
            match = re.match(r'\s*Annotation:\s*(.*)', line, re.IGNORECASE)
            if match:
                 annotation_part = match.group(1).strip()
                 # Parse the [Type: Value] part, allowing optional trailing period in value
                 annotation_match = re.match(r'\[Type:\s*(?P<type>[^,]+),\s*Value:\s*"(?P<value>[^"]+?)\.?"\]', annotation_part)
                 if annotation_match:
                     # Add the parsed annotation
                     current_example['annotations'].append({
                         'type': annotation_match.group('type').strip(),
                         'value': annotation_match.group('value').strip() # Store without trailing dot
                     })
                     last_line_was_example_part = True # Mark as part of example
                     # Single annotation often implies the end of this example block before the next line
                     # We will finalize it when the *next* structural element starts.
                 else:
                      print(f"Warning: Could not parse single annotation content: {annotation_part}")
                      _reset_block_parsing_states()
            else:
                  # Line started with 'Annotation:' but format was wrong
                  print(f"Warning: Malformed single annotation line: {line}")
                  _reset_block_parsing_states()
        else:
             # Cannot add annotation without a current_example
             _reset_block_parsing_states()


    def _process_description_line(line):
        """Handles lines within a description block."""
        # Ensure we are parsing description and have a valid label context
        if parsing_description and current_category and current_label and line.strip() and \
           current_category in guidelines_data and current_label in guidelines_data[current_category]:
            # Ensure description list exists
            if not isinstance(guidelines_data[current_category][current_label]['description'], list):
                 guidelines_data[current_category][current_label]['description'] = []
            guidelines_data[current_category][current_label]['description'].append(line.strip())
        else:
             # If not in description mode, this line might reset states
             _reset_block_parsing_states()


    def _process_label_note_line(line):
        """Handles lines within a label's ##### Hinweis block."""
        if parsing_label_note and current_category and current_label and line.strip() and \
           current_category in guidelines_data and current_label in guidelines_data[current_category]:
             # Append to the label's main 'notes' list
             if 'notes' not in guidelines_data[current_category][current_label]:
                  guidelines_data[current_category][current_label]['notes'] = []
             guidelines_data[current_category][current_label]['notes'].append(line.strip())
        else:
            # Stop parsing label note if context changes or line is empty
            _reset_block_parsing_states()

    # --- Functions for "Unklare Fälle" Section ---
    def _start_unclear_cases():
        """Initializes parsing for the 'Unklare Fälle' section."""
        nonlocal parsing_unclear_cases, in_structured_section, current_category, current_label, current_example, current_unclear_subsection
        _finalize_current_example()
        _attach_pending_notes()
        _reset_block_parsing_states()

        parsing_unclear_cases = True
        in_structured_section = False # Mark that we are outside the main category/label structure
        current_category = None
        current_label = None
        current_example = None
        current_unclear_subsection = None # No subsection active initially
        guidelines_data['Unklare Fälle'] = {'_intro': []} # Use '_intro' for text before first ###

    def _process_unclear_case_line(line):
        """Processes a line within the 'Unklare Fälle' section."""
        nonlocal current_unclear_subsection
        stripped_line = line.strip()

        if stripped_line.startswith('### '): # Note the space to distinguish from ###Kategorie
            # Start a new subsection
            current_unclear_subsection = stripped_line.replace('### ', '').strip()
            if current_unclear_subsection not in guidelines_data['Unklare Fälle']:
                guidelines_data['Unklare Fälle'][current_unclear_subsection] = []
        elif current_unclear_subsection is not None:
            # Add line to the current subsection if it's not empty
            if stripped_line:
                 # Handle list items or notes specifically if needed, otherwise just add text
                 if stripped_line.startswith('* **Hinweis:**'):
                      guidelines_data['Unklare Fälle'][current_unclear_subsection].append(stripped_line) # Keep full note marker
                 elif stripped_line.startswith('* ') or stripped_line.startswith('- '):
                      guidelines_data['Unklare Fälle'][current_unclear_subsection].append(stripped_line) # Keep list marker
                 else:
                      guidelines_data['Unklare Fälle'][current_unclear_subsection].append(stripped_line)
        elif not current_unclear_subsection and stripped_line:
             # Add lines before the first ### to the intro section
             guidelines_data['Unklare Fälle']['_intro'].append(stripped_line)


    # --- Main Parsing Loop ---
    for line in lines:
        stripped_line = line.rstrip() # Keep indentation for potential multi-line content

        # 1. Check if parsing "Unklare Fälle"
        if parsing_unclear_cases:
            _process_unclear_case_line(line) # Use original line to preserve potential indentation/formatting
            continue # Move to next line

        # 2. Check for start of "Unklare Fälle"
        if stripped_line.startswith('## Unklare Fälle und Richtlinien zur Entscheidung'):
            _start_unclear_cases()
            continue

        # 3. Check structural elements (Categories, Labels, Sections)
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
        elif stripped_line.startswith('##### Hinweis'): # Label-level note starts
            _process_label_note_header()

        # 4. Check for Example-specific Notes first
        elif stripped_line.strip().startswith('* **Hinweis:**'): # Use strip() here for robustness
             _process_example_note(stripped_line) # Handles attaching to current_example or current_notes

        # 5. Check for Example elements
        elif stripped_line.startswith('* Text:'):
            _process_example_text(stripped_line)
        # Match "Annotation:" or "Annotations:" ignoring case and whitespace
        elif re.match(r'^\s*(Annotation|Annotations):\s*$', stripped_line, re.IGNORECASE):
             _process_annotations_header(stripped_line)
        # Match single line Annotation: [Type:...]
        elif re.match(r'^\s*Annotation:\s*\[.*\]', stripped_line, re.IGNORECASE):
             _parse_and_add_single_annotation(stripped_line)
        # Match annotation list item "- [Type:..." within an annotation block
        elif parsing_annotations and stripped_line.strip().startswith('- ['):
             _parse_and_add_list_annotation(stripped_line)

        # 6. Check for content lines within active blocks
        elif parsing_description and stripped_line.strip():
            _process_description_line(stripped_line)
        elif parsing_label_note and stripped_line.strip():
             _process_label_note_line(stripped_line)

        # 7. Handle empty lines or other text
        elif not stripped_line.strip(): # Handle empty/whitespace lines
            # Empty line often ends multi-line blocks like description or notes
            _reset_block_parsing_states()
            # Don't finalize example on empty line, wait for next structural element
            pass
        elif stripped_line.startswith('#'): # Ignore other markdown headings
             _finalize_current_example() # Headings break context
             _reset_block_parsing_states()
             pass
        else: # Handle general text lines
            # If before structured section, add to general principles
            if not in_structured_section and stripped_line.strip():
                general_principles.append(stripped_line.strip())
                _reset_block_parsing_states()
            # If inside structured section but not matching known pattern,
            # it might implicitly end a block.
            # Let's reset states but avoid finalizing example yet.
            # This ignores potentially stray text.
            # Consider if stray text should be logged or attached somewhere.
            # For now, just reset flags.
            # else:
            #     print(f"Info: Ignoring unmatched line in structured section: {stripped_line}")
            _reset_block_parsing_states()


    # --- Post-Loop Processing ---
    _finalize_current_example() # Finalize any pending example at the end
    _attach_pending_notes()    # Attach any remaining general notes

    # Join description lines and clean up empty lists/Nones
    for category in list(guidelines_data.keys()):
         if category == 'Unklare Fälle':
              # Clean up empty intro list
              if '_intro' in guidelines_data[category] and not guidelines_data[category]['_intro']:
                   del guidelines_data[category]['_intro']
              # Join multi-line text in subsections? For now, keep as lists.
              continue # Skip other processing for this special section

         if category == 'General Principles': continue

         # Process actual categories
         if isinstance(guidelines_data[category], dict):
             # Handle category notes if they exist
             if 'category_notes' in guidelines_data[category] and not guidelines_data[category]['category_notes']:
                  del guidelines_data[category]['category_notes']

             for label in list(guidelines_data[category].keys()):
                  if label == 'category_notes': continue # Skip the category notes key

                  if isinstance(guidelines_data[category].get(label), dict):
                      data = guidelines_data[category][label]
                      # Join description
                      if 'description' in data and isinstance(data['description'], list):
                          data['description'] = "\n".join(data['description']).strip()
                          if not data['description']: # Remove if empty after join
                               del data['description']
                      elif 'description' not in data or not data['description']:
                           # Ensure 'description' key is removed if it was never populated or is empty
                           if 'description' in data:
                               del data['description']


                      # Clean empty example lists
                      if 'standard_examples' in data and not data['standard_examples']:
                          del data['standard_examples']
                      if 'other_examples' in data and not data['other_examples']:
                          del data['other_examples']

                      # Clean empty label notes list
                      if 'notes' in data and not data['notes']:
                          del data['notes']
                  else:
                       print(f"Warning: Expected dictionary for label '{label}' in category '{category}', found {type(guidelines_data[category].get(label))}")


    # Add general principles if any exist
    if general_principles:
      guidelines_data['General Principles'] = [p for p in general_principles if p.strip()]
    elif 'General Principles' in guidelines_data and not guidelines_data['General Principles']:
         del guidelines_data['General Principles'] # Clean up if empty


    # Remove empty categories if any resulted from processing
    for category in list(guidelines_data.keys()):
         if category not in ['General Principles', 'Unklare Fälle'] and not guidelines_data[category]:
              print(f"Info: Removing empty category '{category}'")
              del guidelines_data[category]


    return guidelines_data

# --- Example of how to call it (if run directly) ---
if __name__ == "__main__":
    guidelines_file = "annotation_guidelines.md"
    output_json_file = "parsed_guidelines_output.json" # New output file name

    try:
        # Get the directory of the script
        script_dir = os.path.dirname(__file__) if '__file__' in locals() else os.getcwd()
        guidelines_path = os.path.join(script_dir, guidelines_file)
        output_json_path = os.path.join(script_dir, output_json_file)

        print(f"Attempting to read guidelines from: {guidelines_path}")
        with open(guidelines_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        print("Parsing markdown content...")
        parsed_data = parse_annotation_guidelines_markdown(markdown_content)
        print("Parsing complete.")

        # Print the parsed dictionary using json for readability
        print("\n--- Parsed Annotation Guidelines Dictionary (Preview) ---")
        # Limited print to avoid overwhelming console for large files
        print("...")
        if 'Unklare Fälle' in parsed_data:
             print("Unklare Fälle section preview:")
             print(json.dumps(parsed_data['Unklare Fälle'], indent=2, ensure_ascii=False))
        print("--------------------------------------------------------")


        print(f"Writing parsed data to: {output_json_path}")
        with open(output_json_path, 'w', encoding='utf-8') as f_out:
            json.dump(parsed_data, f_out, indent=2, ensure_ascii=False)
        print("Successfully wrote JSON output.")

    except FileNotFoundError:
        print(f"Error: The file '{guidelines_file}' was not found at '{guidelines_path}'.")
        print("Please ensure the markdown file is in the same directory as the script.")
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
# Annotation Guidelines Repository

Dieses Repository dient der zentralen Verwaltung und einfachen Integration der Annotationsrichtlinien für das Regesten-Projekt. Es ermöglicht die Versionierung der Richtlinien und deren Verwendung als Submodul in verschiedenen Teilen des Projekts, wie z.B. dem NER-Assistenten.

## Inhalt des Repositories

* `annotation_guidelines.md`: Die eigentlichen Annotationsrichtlinien im strukturierten Markdown-Format.

* `annotation_schema.md`: Beschreibt das Markdown-Schema, dem die `annotation_guidelines.md` folgen muss.

* `anno_to_dict.py`: Ein Python-Skript, das die `annotation_guidelines.md` parst und als hierarchisches Python-Dictionary zurückgibt.

## Bearbeitungshinweise

* Halten Sie sich strikt an das in `annotation_schema.md` definierte Markdown-Format. Dies ist entscheidend für das korrekte Parsen durch das Skript `anno_to_dict.py`.

* **Texteditor:** Bearbeiten Sie die `annotation_guidelines.md` mit einem Markdown-freundlichen Texteditor. Z.B. empfohlen wäre VSCode oder [Das Markdown Pad](https://pad.gwdg.de/).

* **Standard vs. Other Examples:** Achten Sie darauf, neue Beispiele korrekt unter `##### Standard Examples:` oder `##### Other Examples:` einzufügen.

* **Fettdruck und Anführungszeichen:** Stellen Sie sicher, dass der zu annotierende Text im `* Text:`-Feld **fett** markiert ist und die Werte im `[Type: ..., Value: "..."]`-Format in "Anführungszeichen" stehen.

## Versionierung

* Dieses Repository nutzt Git für die Versionierung.

* Jede Änderung an den Richtlinien sollte in einem separaten aussagekräftigen Commit festgehalten werden

* Tags können verwendet werden, um spezifische Versionen der Richtlinien zu markieren (z.B. `v1.0.0`).
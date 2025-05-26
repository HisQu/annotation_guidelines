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

Dieses Repository verwendet Git und GitHub zur automatischen Versionierung der Annotationsrichtlinien. Damit das System korrekt funktioniert, müssen Änderungen **immer über einen Pull Request** erfolgen. Bitte gehe dabei wie folgt vor:

---

###  Schritt-für-Schritt-Anleitung

#### 1. Datei bearbeiten
- Navigiere zur gewünschten Datei (meistens `annotation_guidelines.md`)
- Klicke oben rechts auf das **Stiftsymbol** (✏️) mit der Beschriftung `Edit this file`

#### 2. Änderung eintragen
- Nimm deine Ergänzungen oder Korrekturen im Text vor
- Achte darauf, das bestehende Format beizubehalten

#### 3. Änderung einreichen
- Klicke oben rechts den grünen **„Commit Changes“** Button an
- Wähle im folgenden Fenster **„Create a new branch for this commit and start a pull request“** und klicke dann auf den grünen Button

---

### 4. Pull Request ausfüllen

Im nächsten Fenster erscheint ein Formular mit folgendem Aufbau:

```txt
### Beschreibung der Änderung
-

### Versionierung (bitte genau *eine* Option mit einem X innerhalb der Klammern ankreuzen)

[ ] MAJOR – Inkompatible Änderungen  
[ ] MINOR – Neue Funktion oder Regel  
[ ] PATCH – Kleinere Korrektur oder Klarstellung

```
#### Beschreibung der Änderungen
- Gib in kurzen Stichpunkten an, was geändert wurde
#### Versionstyp auswählen
- Wähle genau eine Option mit [X] aus:
    - `MAJOR`: Es gibt **grundlegende, inkompatible Änderungen**
    - `MINOR`: Eine **neue Regel oder Kategorie** wurde ergänzt
    - `PATCH`: Eine **kleine Korrektur oder Klarstellung**
#### Beispiel für ein ausgefülltes Formular:
```txt
### Beschreibung der Änderung
- Beschreibung für das Label Papst ergänzt
- Darin wurde vermerkt, dass Patrozinien ohne Ordinalzahl nicht als Papst zu taggen sind

### Versionierung (bitte genau *eine* Option mit einem X innerhalb der Klammern ankreuzen)

[ ] MAJOR – Inkompatible Änderungen  
[X] MINOR – Neue Funktion oder Regel  
[ ] PATCH – Kleinere Korrektur oder Klarstellung
```
Nachdem die Beschreibung erstellt wurde muss nichts mehr geändert werden und der untere grüne Button kann angeklickt werden.

---

### 5. Pull Request abschließen
- Wenn das Formular ausgefüllt ist, klicke auf den grünen Button **„Create pull request“**
- Nach kurzer Zeit wird automatisch überprüft, ob alles korrekt ist
- Sobald das erledigt ist, klicke auf **„Merge pull request“**, danach auf **„Confirm merge“**


### Wichtig
- Bitte ändere niemals direkt den ``main``-Branch
- Immer über einen Pull Request arbeiten
- Wähle genau eine Versionierungsstufe (MAJOR, MINOR oder PATCH)
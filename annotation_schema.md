# Titel der Annotationsrichtlinie

## Allgemeine Prinzipien

* Dies ist ein allgemeiner Punkt der Richtlinie.
* Ein weiterer allgemeiner Punkt.
Hinweis zur Darstellung: Spezielle Formatierungen werden hier erklärt.
Hier kann auch ein Absatz mit allgemeineren Informationen stehen.

### Kategorie: [Name der Hauptkategorie]

* **Hinweis:** Dies ist ein allgemeiner Hinweis für alle Labels in dieser Kategorie.

#### Label: [Name des Labels]

##### Beschreibung:
Dies ist die Beschreibung für das Label.
Der Text kann über mehrere Zeilen gehen, solange er direkt nach der Überschrift oder eingerückt beginnt.

##### Standard Examples:

* Text: Ein Satz mit dem **Beispielwort**.
  Annotation: [Type: [Name des Labels], Value: "Beispielwort"]

* Text: Ein komplexeres Beispiel mit **mehreren** zu **annotierenden** Teilen.
  Annotations:
  - [Type: [Label für 'mehreren'], Value: "mehreren"]
  - [Type: [Label für 'annotierenden'], Value: "annotierenden"]

* Text: Beispiel mit **zwei Fragmenten** für dasselbe Label.
  Annotations:
  - [Type: [Name des Labels], Value: "zwei Fragmenten"]
  - [Type: [Name des Labels], Value: "dasselbe Label"]


##### Other Examples:

* Text: Ein weiteres Beispiel für **dasselbe Label**.
  Annotation: [Type: [Name des Labels], Value: "dasselbe Label"]

* **Hinweis:** Dies ist ein spezifischer Hinweis zu diesem Label.
* **Hinweis:** Ein weiterer relevanter Punkt für dieses Label.

### Kategorie: [Name der nächsten Hauptkategorie]

## Zusätzliche Regeln und Unklare Fälle

* **Hinweis:** Regel zu doppeldeutige Begriffe.
  Text: Beispieltext zur Regel mit **annotierter Teil**.
  Annotation: [Type: [Zugehöriges Label], Value: "annotierter Teil"]
* **Hinweis:** Regel zu Kombinationen aus mehreren Kategorien.
  Text: can. et preb. **eccl.** **Sleswic.**
  Annotations:
  - [Type: KirchlichesAmt, Value: "can. et preb."]
  - [Type: Institution, Value: "eccl."]
  - [Type: Diözese, Value: "Sleswic."]


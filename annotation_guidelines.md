# Annotationrichtlinien für Historische Regesten

## Allgemeine Prinzipien

### 1. Ziel und Umfang der Annotation:

Die Annotation von Regesten dient der strukturierten Erfassung relevanter Entitäten zur besseren Analyse und maschinellen Verarbeitung.  
Annotiert werden all jene Begriffe bzw. Konzepte, für die sich ein Forschungsinteresse in der wissenschaftlichen Literatur nachweisen lässt. Neben der Forschungsliteratur berücksichtigen wir ebenfalls die Ergebnisse einer von uns in der historischen Forschungsgemeinschaft durchgeführten Umfrage zu früheren, aktuellen und geplanten Forschungsvorhaben mit Bezug zum Repertorium Germanicum.   
Nicht getaggte Inhalte können dennoch durch KI-gestützte Verfahren erfasst werden. Annotiert werden ausschließlich Begriffe, die explizit im Regesttext vorkommen – Begriffe, die nur implizit mitgedacht werden müssen, z.B. (prov.) de eccl., bleiben unberücksichtigt.  
Wörter können auch mit mehreren Labels gleichzeitig versehen werden, z.B. presbiteros (Personengruppe, KirchlicherStand, KirchlichesAmt).  
Abkürzungspunkte und Endpunkte nach der Quellenangabe, sind Teil der Annotation und werden entsprechend mit ausgezeichnet.      

### 2. Kategorien:

Die Annotation erfolgt derzeit anhand einer Vielzahl von **basalen Kategorien**, also kleinster logisch abgrenzbarer Einheiten im Regesttext. Diese basalen Kategorien bilden die Grundlage der Auszeichnung.
Behelfsmäßig sind diese Basiskategorien in vier übergeordnete Kategorien gruppiert: Personen und Personengruppen, Vita, Event und Varia. Diese dienen der besseren Übersichtlichkeit und Navigation innerhalb der Guidelines.
Perspektivisch werden diese übergeordneten Kategorien durch andere/weitere **semantische Kategorien** ersetzt bzw. ergänzt. Semantische Kategorien entstehen aus der Kombination mehrerer basaler Kategorien. Ein und dieselbe basale Einheit kann dabei mehreren semantischen Kategorien zugeordnet werden. Die semantischen Kategorien befinden sich aktuell im Aufbau und werden schrittweise in die Guidelines integriert.

### 3. Darstellung im Guidelines-Dokument:

Der Fettdruck kennzeichnet, welche Wörter mit dem Kategorielabel getaggt werden sollen und welche nicht.    

## Strukturierung der Labels und Beispiele

Jede Kategorie (Person, Vita, Event, Varia) enthält eine Liste von Labels (Unterkategorien). Für jedes Label werden "Standardbeispiele" (Standard Examples) und "Sonstige Beispiele" (Other Examples) aufgeführt. Jedes Beispiel umfasst den Kontext und das zu annotierende Textfragment, wobei das Fragment in doppelten Sternchen (`**`) eingeschlossen ist. Die erwartete Annotation wird im Format `[Type: Value]` angegeben. Bei Beispielen, die mehrere Annotationen ergeben, werden alle aufgeführt.

### Kategorie: Personen und Personengruppen

In den Regesten erscheinen Personen sowohl explizit, d.h. namentlich genannt, als auch implizit, d.h. nicht namentlich genannt, in Form von Umschreibungen.


#### Label: Person_explizit

##### Beschreibung:
Eine Person_explizit liegt immer dann vor, wenn die Person mit "Vorname" und "Namenszusatz" auftritt. Gelegentlich werden Personen auch nur mit "Vorname" oder nur mit "Namenszusatz" genannt. Das Label "Person_explizit" beinhaltet alle Namensbestandteile.

##### Standard Examples:
* Text: **Johannes de Azel**   
  Annotation: [Type: Person_explizit, Value: "Johannes de Azel"]
  

#### Label: Person_implizit

##### Beschreibung:
Eine "Person_implizit" liegt vor, wenn eine einzelne Person nicht namentlich auftritt, sondern über ein Pronomen, eine Amtsbezeichnung oder eine andere als die namentliche Bezeichnung referenziert wird. Hiervon zu unterscheiden sind die Bezeichnungen von Personengruppen, die über Worte und Ausdrücke im Plural erfolgen (s. Kategorie: Personengruppe).

##### Standard Examples:
* Text: **eum** et successores suos in Magunt. provin.  
  Annotation: [Type: Person_implizit, Value: "eum"]  
* Text: supplic. **aep. Magunt.**  
  Annotation: [Type: Person_implizit, Value: "aep. Magunt."]



#### Label: Personengruppe

##### Beschreibung:
Eine "Personengruppe" liegt immer dann vor, wenn ein sprachlicher Ausdruck sich auf mehr als eine Person bezieht. Nicht im Label enthalten sind attributiv gebrauchte Adjektive oder Ähnliches (vgl. Standard Examples: successores suos).

##### Standard Examples:
* Text: eum et **successores** suos in Magunt. provin.  
  Annotation: [Type: Personengruppe, Value: "successores"]  
* Text: **legatos** natos cum plena potestate  
  Annotation: [Type: Personengruppe, Value: "legatos"]  
* Text: cum **30 pers.** de confess. elig.    
  Annotation: [Type: Personengruppe, Value: "30 pers."]  
* Text: **alii**  
  Annotation: [Type: Personengruppe, Value: "alii"]  
* Text: quidem **8000 et infra** lim. eccl. s. Nicolai  
  Annotation: [Type: Personengruppe, Value: "8000 et infra"]  
* Text: **6000 parochiani**  
  Annotation: [Type: Personengruppe, Value: "6000 parochiani"]  
* Text: et **commune** op. D. Traiect. dioc.  
  Annotation: [Type: Personengruppe, Value: "commune"]  



#### Label: Vorname

##### Beschreibung:
Der "Vorname" ist ein Namensbestandteil von fast allen explizit genannten Personen.

##### Standard Examples:

* Text: **Johannes** de Azel  
  Annotation: [Type: Vorname, Value: "Johannes"]
* Text: **Henricus** de Bocholdia    
  Annotation: [Type: Vorname, Value: "Henricus"]
* Text: **Floora** relicta Magni Bootes armig.  
  Annotation: [Type: Vorname, Value: "Floora"] 



#### Label: Namenszusatz

##### Beschreibung:
Der "Namenszusatz" ist eine Sammelbezeichnung für eine Vielzahl möglicher Namensbestandteile, die meist auf einen "Vornamen" folgen. Sie werden gesammelt als "Namenszusatz" gelabelt. Gemeinsam mit "Vorname" konstituiert der "Namenszusatz" in den allermeisten Fällen die Kategorie "Person_explizit". Achtung: Nicht als "Namenszusatz" gelten kirchliche Ämter (Albertus el. Ratisp. /Angelus abb. mon. in Runa), weltliche Ämter (Antonius dux Brabantie), Identifikation über eine andere Person (Alexander nob. viri Semonithi ducis Masouie natus).

##### Standard Examples:

* Text: Johannes **de Azel**  
  Annotation: [Type: Namenszusatz, Value: "de Azel"]  
* Text: Achacius **Berolczhaimer**  
  Annotation: [Type: Namenszusatz, Value: "Berolczhaimer"]
* Text: Bertholdus **Schomaker al. dictus Dives**   
  Annotation: [Type: Namenszusatz, Value: "Schomaker al. dictus Dives"]
* Text: Bertholdus **Denen (Deynen) de Wildunghen**  
  Annotation: [Type: Namenszusatz, Value: "Denen (Deynen) de Wildunghen"]
* Text: Fridericum **Baecht iuniorem**  
  Annotation: [Type: Namenszusatz, Value: "Baecht iuniorem"]
* Text: **Florentin. nunc.**  
  Annotation: [Type: Namenszusatz, Value: "Florentin. nunc."]

##### Other Examples:
* Text: castrum **das Newhaus nunc.**   
  Annotation: [Type: Namenszusatz, Value: "das Newhaus nunc."]



#### Label: Papst

##### Beschreibung:
Die Päpste sind im Kontext des RG eine besonders relevante Ausformung der Klasse "Person_explizit" und werden deshalb separat getaggt. Die Namen der Päpste kommen dekliniert vor, z.B. "Bonifatio VIII" statt "Bonifatius VIII"; ebenso: "pape" statt "papa". Achtung: Nicht als "Papst" getaggt werden Patrozinien, die ohne die Ordinalzahl (z.B. VIII) oder den Zusatz "papa" vorkommen, z.B.: Bonifatii im Kontext "eccl. s. Bonifatii Halberstad.".

##### Standard Examples:

* Text: **Bonifatius IX.**  
  Annotation: [Type: Papst, Value: "Bonifatius IX."]
* Text: **papa**  
  Annotation: [Type: Papst, Value: "papa"]
  * **Häufigkeit:** 480x in den Bänden 1-9, pape: 5307x in den Bänden 1-9.
* Text: **Bonifatio VIII papa**  
  Annotation: [Type: Papst, Value: "Bonifatio VIII papa"]


### Kategorie: Akteur



#### Label: Anhänger

##### Standard Examples:
* Text: **adher.**  
  Annotation: [Type: Anhänger, Value: "adher."]



#### Label: Arme_Person_Marker

##### Standard Examples:

* Text: **pauper**  
  Annotation: [Type: Arme_Person_Marker, Value: "pauper"]
* Text: **gratis pro deo**  
  Annotation: [Type: Arme_Person_Marker, Value: "gratis pro deo"]
* Text: **gratis**  
  Annotation: [Type: Arme_Person_Marker, Value: "gratis"]



#### Label: Delegierter_Richter_Marker

##### Standard Examples:

* Text: **iudex delegatus**  
  Annotation: [Type: Delegierter_Richter_Marker, Value: "iudex delegatus"]



#### Label: Exekutor_Marker

##### Standard Examples: executor

* Text: **executor**  
  Annotation: [Type: Exekutor_Marker, Value: "executor"]



#### Label: Familiar_Marker

##### Standard Examples:

* Text: **fam.** Antonii ep. Portuen. card.  
  Annotation: [Type: Familiar_Marker, Value: "fam."]
* Text: **acolit.** pape  
  Annotation: [Type: Familiar_Marker, Value: "acolit."]

##### Other Examples:

* Text: **parafrenarius** pape  
  Annotation: [Type: Familiar_Marker, Value: "parafrenarius pape"]
* Text: **(unknown)** pape  
  Annotation: [Type: Familiar_Marker, Value: "(unknown)"]
  * **Hinweis:** Neben den oben genannten Beispielen "acolit. pape" und "parafrenarius pape" kann es noch weitere Ämter geben, die im direkten Umfeld des Papstes ausgeübt werden. Diese kirchlichen Ämter, die im Regest durch die direkte Nähe zum Wort "pape" gekennzeichnet sind, werden hier durch den Platzhalter (unknown) bezeichnet.


#### Label: Fürsprecher_Marker

##### Standard Examples:

* Text: **supplic.** Johanne ep. Gurc.  
  Annotation: [Type: Fürsprecher_Marker, Value: "supplic."]



#### Label: Kollator_Marker

##### Standard Examples:

* Text: ad **coll.** epp.  
  Annotation: [Type: Kollatur_Marker, Value: "coll."]



#### Label: Kollektor_Marker

##### Standard Examples:

* Text: Gotfridi Bochorn **collect.**  
  Annotation: [Type: Kollektor_Marker, Value: "collect."]



#### Label: Obligationsbeauftragter_Marker

##### Standard Examples:

* Text: **o.s.a.** per Johannem Scade  
  Annotation: [Type: Obligationsbeauftragter_Marker, Value: "o.s.a."]



#### Label: Patron_Marker

##### Standard Examples:

* Text: **patron.**  
  Annotation: [Type: Patron_Marker, Value: "patron."]



#### Label: Petent_Marker

##### Standard Examples:

* Text: **S** 579 228vs, L 605 5rs.  
  Annotation: [Type: Petent_Marker, Value: "S"]



#### Label: Prozessvorsteher

##### Beschreibung: 
Eine Person, die einem Gerichtsprozess vorsteht.  

##### Standard Examples:

* Text: **iud.**      
  Annotation: [Type: Prozessvorsteher, Value: "iud."]  
* Text: **iudex**    
  Annotation: [Type: Prozessvorsteher, Value: "iudex"]    
* Text: **official.** Minden. hab. pot. ab ep. Verden.   
  Annotation: [Type: Prozessvorsteher, Value: "official."]    
* Text: **offic.** Minden. perm. causa de par. eccl.  
  Annotation: [Type: Prozessvorsteher, Value: "offic."] 


#### Label: Student_Marker

##### Standard Examples:

* Text: in alma Urbe in iure can. **studens**: ref. disp. sup. incompat.    
  Annotation: [Type: Student_Marker, Value: "studens"]  
* Text: Adolffus de Nassauw **scol.** Trever. de disp. sup. def. nat.    
  Annotation: [Type: Student_Marker, Value: "scol."]  
  * **Hinweis:** Zu beachten ist, dass eine Person, die als **scol.** bezeichnet wird, nicht immer ein Student ist und somit in dem Fall auch nicht **scol.** als StudentMarker taggt werden darf. Hier ein Beispiel: Albertus Glenneman (Gleneman) **scol.** Colon. in 10 anno constitutus de can. et min. preb. eccl. ss. Petri et Andree Paderburn. vac. p. o. Jordani de Widonbunghe in curia 18 ian. 1426 S 201 223r.


#### Label: Subkollektor_Marker

##### Standard Examples:

* Text: ratione off. **subcollectorie** in dioc. Constant.  
  Annotation: [Type: Subkollektor_Marker, Value: "subcollectorie"]  
* Text:  fructuum camere ap. **subcollectoris** S 68 135 v.    
  Annotation: [Type: Subkollektor_Marker, Value: "subcollectoris"]  



#### Label: Tischgenosse_Marker

##### Standard Examples:

* Text: fam. **commensalis** Dominici [de Capranica]  
  Annotation: [Type: Tischgenosse_Marker, Value: "commensalis"]



#### Label: Zahlungsbeauftragter_Marker

##### Standard Examples:

* Text: oblig. sup. annat. ( **p.** mag. Henricum Erkel d. Hesse  
Annotation: [Type: Zahlungsbeauftragter_Marker, Value: "p."]  
* Text: **p. manus** Prothasii de Tabernis (19 fl. auri de cam. )  
Annotation: [Type: Zahlungsbeauftragter_Marker, Value: "p. manus"]



#### Label: Zeuge_Marker

##### Standard Examples:

* Text: Adolphus filius ducis Cleven. **testis**  
Annotation: [Type: Zeuge_Marker, Value: "testis"]  
* Text: **testis** super quadam oblig. 28 iul. 1409 M 8.  
Annotation: [Type: Zeuge_Marker, Value: "testis"]


  
### Kategorie: Vita

#### Label: Familienbeziehung

##### Beschreibung:
In den Regesten wird für viele Personen eine "Familienbeziehung" angegeben. Die unter den Examples gelisteten Beispiele können auch dekliniert vorkommen. Die deklinierten Formen sollen ebenfalls das Label "Familienbeziehung" erhalten, z.B. uxoris statt uxor.

##### Standard Examples:

* Text: Albertus de Smolsco presb. Wladislav. dioc. **nepos** aep. Gneznen.  
  Annotation: [Type: Familienbeziehung, Value: "nepos"]
  * **Häufigkeit:** 403x in den Bänden 1-9
* Text: **ux.**  
  Annotation: [Type: Familienbeziehung, Value: "ux."]
  * **Häufigkeit:** 1878x in den Bänden 1-2 und 5-9
* Text: **genitor**  
  Annotation: [Type: Familienbeziehung, Value: "genitor"]

##### Other Examples:

* Text: **uxor**  
  Annotation: [Type: Familienbeziehung, Value: "uxor"]
  * **Häufigkeit:** 936x in den Bänden 1-5 und 9
* Text: **filius**  
  Annotation: [Type: Familienbeziehung, Value: "filius"]
* Text: **filia**  
  Annotation: [Type: Familienbeziehung, Value: "filia"]
* Text: **pater**  
  Annotation: [Type: Familienbeziehung, Value: "pater"]
* Text: **frater**  
  Annotation: [Type: Familienbeziehung, Value: "frater"]
* Text: **relicta**  
  Annotation: [Type: Familienbeziehung, Value: "relicta"]
* Text: **natus** (unknown)
  Annotation: [Type: Familienbeziehung, Value: "natus"]
  * **Hinweis:** (unknown) steht hier als Platzhalter für den Namen des Vaters, z.B. "Bernhardus natus Johannis Berlin", wobei Johannes Berlin der Vater von Bernhardus ist. Oder: "Alexander nob. viri Semonithi ducis Masouie natus", wobei Semonithus der Vater des Alexander ist.
* Text: **consanguineus**  
  Annotation: [Type: Familienbeziehung, Value: "consanguineus"]



#### Label: Sozialer_Stand

##### Beschreibung:
Der soziale Stand einer Person ergibt sich u.a. aus Angaben zu ihrer (nicht-)adligen Herkunft.

##### Standard Examples:

* Text: **de nob. gen.**  
  Annotation: [Type: Sozialer_Stand, Value: "de nob. gen."]
* Text: **nob. viri xxx**  
  Annotation: [Type: Sozialer_Stand, Value: "nob. viri xxx"]
* Text: **de bar.**  
  Annotation: [Type: Sozialer_Stand, Value: "de bar."]

##### Other Examples:

* Text: **scol.**  
  Annotation: [Type: Sozialer_Stand, Value: "scol."]
  * Text: **studens**  
  Annotation: [Type: Sozialer_Stand, Value: "studens"]
* Text: **baron. gen.**  
  Annotation: [Type: Sozialer_Stand, Value: "baron. gen."]
* Text: **de com. gen.**  
  Annotation: [Type: Sozialer_Stand, Value: "de com. gen."]
* Text: **de mil.**  
  Annotation: [Type: Sozialer_Stand, Value: "de mil."]
* Text: **milit. gen.**  
  Annotation: [Type: Sozialer_Stand, Value: "milit. gen."]  
* Text: **de ducum et com. gen.**  
  Annotation: [Type: Sozialer_Stand, Value: "de ducum et com. gen."]
* Text: **de comit. gen.**  
  Annotation: [Type: Sozialer_Stand, Value: "de comit. gen."]
* Text: **de ducum et comit. gen.**  
  Annotation: [Type: Sozialer_Stand, Value: "de ducum et comit. gen."]
* Text: **de ducum et marchionum gen.**  
  Annotation: [Type: Sozialer_Stand, Value: "de ducum et marchionum gen."]
* Text: **de ducis** natus  
  Annotation: [Type: Sozialer_Stand, Value: "de ducis"]
* Text: **nob.**  
  Annotation: [Type: Sozialer_Stand, Value: "nob."]
* Text: **mul.**  
  Annotation: [Type: Sozialer_Stand, Value: "mul."]
* Text: **mulier**  
  Annotation: [Type: Sozialer_Stand, Value: "mulier"]
* Text: **armig.**  
  Annotation: [Type: Sozialer_Stand, Value: "armig."]
* Text: **mil.**  
  Annotation: [Type: Sozialer_Stand, Value: "mil."]
* Text: **civ.**  
  Annotation: [Type: Sozialer_Stand, Value: "civ."]
* Text: **civis**  
  Annotation: [Type: Sozialer_Stand, Value: "civis"]
* Text: **domic.**  
  Annotation: [Type: Sozialer_Stand, Value: "domic."]
  * **Hinweis:** s. Notiz unten.   
* Text: **de milit. gen.**  
  Annotation: [Type: Sozialer_Stand, Value: "de milit. gen."]
* Text: **opid.**  
  Annotation: [Type: Sozialer_Stand, Value: "opid."]
* Text: **bar.**  
  Annotation: [Type: Sozialer_Stand, Value: "bar."]
  * **Hinweis:** Wenn kein Herrschaftsgebiet genannt wird; vgl. Weltliches_Amt.
* Text: **com.**  
  Annotation: [Type: Sozialer_Stand, Value: "com."]
  * **Hinweis:** Wenn kein Herrschaftsgebiet genannt wird; vgl. Weltliches_Amt.
* Text: **comes**  
  Annotation: [Type: Sozialer_Stand, Value: "comes"]
  * **Hinweis:** Wenn kein Herrschaftsgebiet genannt wird; vgl. Weltliches_Amt.
* Text: **dux**  
  Annotation: [Type: Sozialer_Stand, Value: "dux"]
  * **Hinweis:** Wenn kein Herrschaftsgebiet genannt wird; vgl. Weltliches_Amt.
* Text: **incola**  
  Annotation: [Type: Sozialer_Stand, Value: "incola"]
* Text: **parochianus**  
  Annotation: [Type: Sozialer_Stand, Value: "parochianus"] 



#### Label: Kirchlicher_Stand

##### Beschreibung:
Der kirchliche Stand ergibt sich aus dem Empfang der niederen Weihen (Lektor, Akoluth, Subdiakon etc.) und der höheren Weihen (Diakonat, Presbyterat, Episkopat); er schlägt sich auch in der generellen Unterscheidung zwischen Laien und Klerikern nieder (laic. = Laie; cler. = Kleriker).

##### Standard Examples:

* Text: **presb.**  
  Annotation: [Type: Kirchlicher_Stand, Value: "presb."]
  * **Hinweis:** vgl. Kirchliches_Amt
* Text: **laic.**  
  Annotation: [Type: Kirchlicher_Stand, Value: "laic."]
* Text: **in minore ord. constit.**  
  Annotation: [Type: Kirchlicher_Stand, Value: "in minore ord. constit."]

##### Other Examples:

* Text: **cler.**  
  Annotation: [Type: Kirchlicher_Stand, Value: "cler."]
* Text: **acol.**  
  Annotation: [Type: Kirchlicher_Stand, Value: "acol."]
* Text: **lect.**  
  Annotation: [Type: Kirchlicher_Stand, Value: "lect."]
  * **Hinweis:** selten, eher: Kirchliches_Amt, s. Notizen unten.
* Text: **subdiac.**  
  Annotation: [Type: Kirchlicher_Stand, Value: "subdiac."]
* Text: **diac.**  
  Annotation: [Type: Kirchlicher_Stand, Value: "diac."]
  * **Hinweis:** vgl. Kirchliches_Amt



#### Label: Beruf

##### Beschreibung
Bei einigen Personen, vor allem bei Laien, werden Angaben zum Beruf gemacht.

##### Standard Examples:
* Text: **mercator**  
  Annotation: [Type: Beruf, Value: "mercator"]
* Text: **medicus**  
  Annotation: [Type: Beruf, Value: "medicus"]  



#### Label: Kirchliches_Amt

##### Beschreibung
Ein kirchliches Amt ist eine offizielle Stellung oder Funktion, die eine Person innerhalb der römisch-katholischen Kirche einnahm. Ein kirchliches Amt kann als Ehrenamt (z. B. Senior in einem Kollegiatsstift) ausgeübt werden oder mit Einnahmen (Pfründe) verbunden sein (z. B. Dekan in einem Kollegiatsstift).  
Durch die Implikation einer festen Stelle mit Einnahmen unterscheiden sich die hier in den Beispielen erfassten kirchlichen Ämter (z.B. presb. card. = Kardinalpriester mit einer Titelkirche) von den unter dem Label KirchlicherStand gesammelten kirchlichen Weihen (z.B. presb. = Priester, i.e. Person, die die Priesterweihe empfangen hat, aber eventuell keine Pfründe erhalten hat).   
Es wird sowohl der Amtsträger (decanus) als auch das Amt (decanatus) getaggt.

##### Standard Examples:

* Text: **can. et preb.**  
  Annotation: [Type: Kirchliches_Amt, Value: "can. et preb."]
  * **Hinweis:** s. Notizen unten.
* Text: **ep.**  
  Annotation: [Type: Kirchliches_Amt, Value: "ep."]
* Text: **benef.**  
  Annotation: [Type: Kirchliches_Amt, Value: "benef."]

##### Other Examples:

* Text: **patr.**  
  Annotation: [Type: Kirchliches_Amt, Value: "patr."]
* Text: **aep.**  
  Annotation: [Type: Kirchliches_Amt, Value: "aep."]
* Text: **epp.**  
  Annotation: [Type: Kirchliches_Amt, Value: "epp."]
* Text: **episc.**  
  Annotation: [Type: Kirchliches_Amt, Value: "episc."]
* Text: **antistes**  
  Annotation: [Type: Kirchliches_Amt, Value: "antistes"]
* Text: **el.**  
  Annotation: [Type: Kirchliches_Amt, Value: "el."]
* Text: **ordin.**  
  Annotation: [Type: Kirchliches_Amt, Value: "ordin."]
* Text: **decan.**  
  Annotation: [Type: Kirchliches_Amt, Value: "decan."]
* Text: **dec.**  
  Annotation: [Type: Kirchliches_Amt, Value: "dec."]  
* Text: **archidiac.**  
  Annotation: [Type: Kirchliches_Amt, Value: "archidiac."]
* Text: **vic.**  
  Annotation: [Type: Kirchliches_Amt, Value: "vic."]
* Text: **abb.**  
  Annotation: [Type: Kirchliches_Amt, Value: "abb."]
* Text: **abbat.**  
  Annotation: [Type: Kirchliches_Amt, Value: "abbat."]
* Text: **cant.**  
  Annotation: [Type: Kirchliches_Amt, Value: "cant."]
* Text: **cust.**  
  Annotation: [Type: Kirchliches_Amt, Value: "cust."]
* Text: **custod.**  
  Annotation: [Type: Kirchliches_Amt, Value: "custod."]
  * **Hinweis:** Ganz selten auch Laien.
* Text: **prepos.**  
  Annotation: [Type: Kirchliches_Amt, Value: "prepos."]
* Text: **prep.**  
  Annotation: [Type: Kirchliches_Amt, Value: "prep."]
* Text: **scolast.**  
  Annotation: [Type: Kirchliches_Amt, Value: "scolast."]
* Text: **rect.**  
  Annotation: [Type: Kirchliches_Amt, Value: "rect."]
* Text: **lect.**  
  Annotation: [Type: Kirchliches_Amt, Value: "lect."]
  * **Hinweis:** Lektor im Kloster, selten: Kirchlicher_Stand, s. Notizen unten.
* Text: **thesaur.**  
  Annotation: [Type: Kirchliches_Amt, Value: "thesaur."]
* Text: **monach.**  
  Annotation: [Type: Kirchliches_Amt, Value: "monach."]
* Text: **monialis**  
  Annotation: [Type: Kirchliches_Amt, Value: "monialis."]
* Text: **dign.**  
  Annotation: [Type: Kirchliches_Amt, Value: "dign."]
  * **Hinweis:** = Höhere Ämter in einem Kapitel: Propst, Dekan, Scholaster.
* Text: **can.**  
  Annotation: [Type: Kirchliches_Amt, Value: "can."]
* Text: **preb.**  
  Annotation: [Type: Kirchliches_Amt, Value: "preb."]
* Text: **can. sub expect. preb.**  
  Annotation: [Type: Kirchliches_Amt, Value: "can. sub expect. preb."]
* Text: **can. et preb. ac supplem.**  
  Annotation: [Type: Kirchliches_Amt, Value: "can. et preb. ac supplem."]
* Text: **canonicatus seu prebenda**  
  Annotation: [Type: Kirchliches_Amt, Value: "canonicatus seu prebenda"]
* Text: **card.**  
  Annotation: [Type: Kirchliches_Amt, Value: "card."]
* Text: **presb. card.**  
  Annotation: [Type: Kirchliches_Amt, Value: "presb. card."]
  * **Hinweis:** Vgl. Kirchlicher_Stand
* Text: **diac. card.**  
  Annotation: [Type: Kirchliches_Amt, Value: "diac. card."]
  * **Hinweis:** Vgl. Kirchlicher_Stand
* Text: **ep. card.**  
  Annotation: [Type: Kirchliches_Amt, Value: "ep. card."]
  * **Hinweis:** Vgl. Kirchlicher_Stand
* Text: **vic. generalis**  
  Annotation: [Type: Kirchliches_Amt, Value: "vic. generalis"]
* Text: **mag. gen.**  
  Annotation:[Type: Kirchliches_Amt, Value: "mag. gen."]
* Text: **precept.**  
  Annotation:[Type: Kirchliches_Amt, Value: "precept."]
* Text: **capellan.**  
  Annotation:[Type: Kirchliches_Amt, Value: "capellan."]
* Text: **cap.**  
  Annotation:[Type: Kirchliches_Amt, Value: "cap."]
* Text: **succentor**  
  Annotation:[Type: Kirchliches_Amt, Value: "succentor"]
* Text: **capn.**  
  Annotation:[Type: Kirchliches_Amt, Value: "capn."] 
* Text: **benef. curato**  
  Annotation: [Type: Kirchliches_Amt, Value: "benef. curato"]
* Text: **benef. s. c.**  
  Annotation: [Type: Kirchliches_Amt, Value: "benef. s. c."]
* Text: **benef. c. c.**  
  Annotation: [Type: Kirchliches_Amt, Value: "benef. c. c."]
  * **Hinweis:** c.c. kann in seltenen Fällen im Kontext einer Dispens wegen def. nat. auch für den Ehestand der Eltern stehen; c. = conjugatus bzw. conjugata.
* Text: **prior**  
  Annotation: [Type: Kirchliches_Amt, Value: "prior"]
  


#### Label: Kuriales_Amt

##### Beschreibung:
Ein kuriales Amt ist eine offizielle Stellung oder Funktion, die eine Person an der römischen Kurie einnahm. Es wird sowohl der Amtsträger als auch das Amt getaggt. Achtung: Manche Positionen kommen auch außerhalb der Kurie an kirchlichen und weltlichen Höfen vor, sodass sich die genaue Zuschreibung des Labels nur aus dem Kontext ergibt (so z.B. beim Notar).

##### Standard Examples:

* Text: **abbr.**  
  Annotation: [Type: Kuriales_Amt, Value: "abbr."]
* Text: **administr.**  
  Annotation: [Type: Kuriales_Amt, Value: "administr."]
* Text: **aud.**  
  Annotation: [Type: Kuriales_Amt, Value: "aud."]

##### Other Examples:

* Text: **cancell.**  
  Annotation: [Type: Kuriales_Amt, Value: "cancell."]
* Text: **cubic.**  
  Annotation: [Type: Kuriales_Amt, Value: "cubic."]
* Text: **cursor**  
  Annotation: [Type: Kuriales_Amt, Value: "cursor"]
* Text: **not.**  
  Annotation: [Type: Kuriales_Amt, Value: "not."]
* Text: **nunt.**  
  Annotation: [Type: Kuriales_Amt, Value: "nunt."]
* Text: **offic.**  
  Annotation: [Type: Kuriales_Amt, Value: "offic."]
* Text: **procur.**  
  Annotation: [Type: Kuriales_Amt, Value: "procur."] 
* Text: **proc.**  
  Annotation: [Type: Kuriales_Amt, Value: "proc."]
* Text: **proc.** ap. sed.  
  Annotation: [Type: Kuriales_Amt, Value: "proc."]
* Text: **prothonot.**  
  Annotation: [Type: Kuriales_Amt, Value: "prothonot."]
* Text: **refer.**  
  Annotation: [Type: Kuriales_Amt, Value: "refer."]
* Text: **script.**  
  Annotation: [Type: Kuriales_Amt, Value: "script."]
* Text: **script. litt. ap.**  
  Annotation: [Type: Kuriales_Amt, Value: "script. litt. ap."]
* Text: **secret.**  
  Annotation: [Type: Kuriales_Amt, Value: "secret."]
* Text: **secr.**  
  Annotation: [Type: Kuriales_Amt, Value: "secr."]
* Text: **tab.**  
  Annotation: [Type: Kuriales_Amt, Value: "tab."]
* Text: **tab. off.**  
  Annotation: [Type: Kuriales_Amt, Value: "tab. off."]



#### Label: Weltliches_Amt

##### Beschreibung:
Ein weltliches Amt ist eine offizielle Stellung oder Funktion, die eine Person im höfischen Kontext (Fürstenhof, Bischofshof etc.) oder als städtischer Funktionsträger (Bürgermeister, Kanzler einer städtischen Kanzlei, Zunftmeister) einnahm.

##### Standard Examples:

* Text: **imp.**  
  Annotation: [Type: Weltliches_Amt, Value: "imp."]
* Text: **rex**  
  Annotation: [Type: Weltliches_Amt, Value: "rex"]

##### Other Examples:

* Text: **bar.**  
  Annotation: [Type: Weltliches_Amt, Value: "bar."]
  * **Hinweis:** Wenn ein Herrschaftsgebiet genannt wird, ansonsten: Sozialer_Stand.
* Text: **dux**  
  Annotation: [Type: Weltliches_Amt, Value: "dux."]
  * **Hinweis:** Wenn ein Herrschaftsgebiet genannt wird, ansonsten: Sozialer_Stand.
* Text: **com.**  
  Annotation: [Type: Weltliches_Amt, Value: "com."]
  * **Hinweis:** Wenn ein Herrschaftsgebiet genannt wird, ansonsten: Sozialer_Stand.
* Text: **comes**  
  Annotation: [Type: Weltliches_Amt, Value: "comes"]
  * **Hinweis:** Wenn ein Herrschaftsgebiet genannt wird, ansonsten: Sozialer_Stand.
* Text: **patron.**  
  Annotation: [Type: Weltliches_Amt, Value: "patron."]
* Text: **imperator**    
  Annotation: [Type: Weltliches_Amt, Value: "imperator"]
* Text: **rex elect.**    
  Annotation: [Type: Weltliches_Amt, Value: "rex elect."]
* Text: **proconsul**    
  Annotation: [Type: Weltliches_Amt, Value: "proconsul"]
* Text: **consul**    
  Annotation: [Type: Weltliches_Amt, Value: "consul"]
* Text: **burggravius**    
  Annotation: [Type: Weltliches_Amt, Value: "burggravius"]  
* Text: **scult.**  
  Annotation: [Type: Weltliches_Amt, Value: "scult."]  

---

#### Label: Akademischer_Grad

##### Standard Examples:

* Text: **licent.**  
  Annotation: [Type: Akademischer_Grad, Value: "licent."]
* Text: **bac.** in decr.
  Annotation: [Type: Akademischer_Grad, Value: "bac."]

##### Other Examples:

* Text: **lic.**   
  Annotation: [Type: Akademischer_Grad, Value: "lic."]
  * **Hinweis:** Nur selten steht lic. für das Lizenziat, i.d.R. nur in Verbindung mit einem Namen. Häufiger steht es für die päpstliche Lizenz und wird dann als Event getaggt.
* Text: **mag.**  
  Annotation: [Type: Akademischer_Grad, Value: "mag."]
* Text: decr.**doct.**  
  Annotation: [Type: Akademischer_Grad, Value: "doct."]
* Text: theol. **profes.**
  Annotation: [Type: Akademischer_Grad, Value: "profes."]

---
#### Label: Studienfach

##### Standard Examples:
* Text: mag. **in art.**  
  Annotation: [Type: Studienfach, Value: "in art."]
* Text: **decr.** doct. 
  Annotation: [Type: Studienfach, Value: "decr."]
* Text: lic. **in leg.**  
  Annotation: [Type: Studienfach, Value: "in leg."]
* Text: lic. **in iure can.**  
  Annotation: [Type: Studienfach, Value: "in iure can."]



#### Label: Orden

##### Beschreibung: 
Ausdruck der Zugehörigkeit zu einer religiösen Ordensgemeinschaft

##### Standard Examples:

* Text: **o. s. Ant.**  
  Annotation: [Type: Orden, Value: "o. s. Ant."]
* Text: **o. s. Aug.**  
  Annotation: [Type: Orden, Value: "o. s. Aug."]
* Text: **o. s. Ben.**  
  Annotation: [Type: Orden, Value: "o. s. Ben."]

##### Other Examples:

* Text: **o. cist.**  
  Annotation: [Type: Orden, Value: "o. cist."]
* Text: **o. fr. herem. s. Aug.**  
  Annotation: [Type: Orden, Value: "o. fr. herem. s. Aug."]
* Text: **o. s. Ant.**  
  Annotation: [Type: Orden, Value: "o. s. Ant."]
* Text: **o. s. Clare**  
  Annotation: [Type: Orden, Value: "o. s. Clare"]
* Text: **o. Carm.**  
  Annotation: [Type: Orden, Value: "o. Carm."]
* Text: **o. Cartus.**  
  Annotation: [Type: Orden, Value: "o. Cartus."]
* Text: **o. Clun.**  
  Annotation: [Type: Orden, Value: "o. Clun."]
* Text: **o. fr. min.**  
  Annotation: [Type: Orden, Value: "o. fr. min."]
* Text: **o. pred.**  
  Annotation: [Type: Orden, Value: "o. pred."]
* Text: **o. Prem.**  
  Annotation: [Type: Orden, Value: "o. Prem."]

* **Hinweis:** Und deren Variationen (z.B. o. Cist.; Cist. ord.). Bitte ergänzen!



### Kategorie: Event

---

### Gnadenerweis

---

#### Label: Abolitio

##### Beschreibung:
Tilgung, z.B. von Inhabilität

##### Standard Examples:

* Text: **m. abol. inhabil.**  
  Annotation: [Type: Abolitio, Value: "m. abol. inhabil."]
* Text: **abol. inhabil.**  
  Annotation: [Type: Abolitio, Value: "abol. inhabil."]
* Text: **abol. macule infamie**  
  Annotation: [Type: Abolitio, Value: "abol. macule infamie."]

#### Label: Abolitio_Zusatz

##### Beschreibung:
Kennzeichnung des Gnadeninhalts. Der gesamte Gnadeninhalt wird mit dem Label AbolitioZusatz getaggt, nicht aber die Gnade abol. selbst.

##### Standard Examples:

* Text: m. abol. inhabil., **quia sacr. ord. una die per Matheum ep. olim Placentin. indebite recepit, n. o. proc. per mag. Angelum de Balionibus aud. gen. cam. ap. instructo** 4 mart. 1412 L 158 130.  
  Annotation: [Type: Abolitio_Zusatz, Value: "quia sacr. ord. una die per Matheum ep. olim Placentin. indebite recepit, n. o. proc. per mag. Angelum de Balionibus aud. gen. cam. ap. instructo"]



#### Label: Absolutio

##### Beschreibung:
Absolution

##### Standard Examples:

* Text: **absol.**  
  Annotation: [Type: Absolutio, Value: "absol."]
* Text: **m. absol.**  
  Annotation: [Type: Absolutio, Value: "m. absol."]
* Text: **m. absol.** a sent. excom.  
  Annotation: [Type: Absolutio, Value: "m. absol."]

##### Other Examples:

* Text: **absol.** a matrim. C. gentili et quasi pagano contracto  
  Annotation: [Type: Absolutio, Value: "absol."]
* Text: **absol.**, quod olim …  
  Annotation: [Type: Absolutio, Value: "absol."]

#### Label: Absolutio_Zusatz

##### Beschreibung:
Kennzeichnung des Gnadeninhalts der Absolution. Der gesamte Gnadeninhalt wird mit dem Label AbsolutioZusatz getaggt, nicht aber die Gnade absol. oder m. absol. selbst.

##### Standard Examples:

* Text: m. absol. **a sent. excom.**  
  Annotation: [Type: Absolutio_Zusatz, Value: "a sent. excom."]
* Text: absol. **a matrim. C. gentili et quasi pagano contracto**  
  Annotation: [Type: Absolutio_Zusatz, Value: "a matrim. C. gentili et quasi pagano contracto"]
* Text: absol., **quod olim …**  
  Annotation: [Type: Absolutio_Zusatz, Value: "quod olim …"]



#### Label: Aggravatio

##### Beschreibung:
Verstärkung einer Strafe

##### Standard Examples:

* Text: **m. aggrav. sent.**  
  Annotation: [Type: Aggravatio, Value: "m. aggrav. sent."]
* Text: **m. aggrav. excom. sent.**  
  Annotation: [Type: Aggravatio, Value: "m. aggrav. excom. sent."]
* Text: **m. aggravandi sent.**  
  Annotation: [Type: Aggravatio, Value: "m. aggravandi sent."]



#### Label: Alternativa_Facultas

##### Beschreibung: "Fakultät für Bischöfe zur alternierenden Besetzung von Pfründen" (Bearbeitungshinweise, S. 67)

##### Standard Examples: 

* Text: motu pr. de **alternativa** videlicet fac. disponendi sup. benef. vacat.  
  Annotation: [Type: , Value: "alternativa"]



#### Label: Antelatio

##### Beschreibung: "Eine weitere Möglichkeit, sich gegenüber Konkurrenten eine Vorrangstellung zu verschaffen, wird durch die „antelatio“ geschaffen, die der Bevorzugung durch „prerogatio“ gleicht." (Bearbeitungshinweise, S. 66)

##### Standard Examples: 

* Text: de **antelatione**  
  Annotation: [Type: , Value: "antelatione"]


#### Label: Beichtprivileg

##### Beschreibung: Erlaubnis, sich seinen Beichtvater selbst zu wählen; entgegen dem Pfarrzwang.

##### Standard Examples:
* Text: gratia de **confess. elig.**  
  Annotation: [Type: Beichtprivileg, Value: "confess. elig."]
* Text: de **confess. elig.**  
  Annotation: [Type: Beichtprivileg, Value: "confess. elig."]

  

#### Label: Cassatio

##### Beschreibung:
Ungültigkeitserklärung

##### Standard Examples:

* Text: **cass.**  
  Annotation: [Type: Cassatio, Value: "cass."]
* Text: **m. cass.** litt.  
  Annotation: [Type: Cassatio, Value: "m. cass."]
* Text: **cass.** pensionis  
  Annotation: [Type: Cassatio, Value: "cass."]

#### Label: Cassatio_Zusatz

#### Beschreibung:
Kennzeichnung des Gnadeninhalts der Cassatio. Der gesamte Gnadeninhalt wird mit dem Label CassatioZusatz getaggt, nicht aber die Gnade cass. selbst.

##### Standard Examples:

* Text: m. cass. **litt.**  
  Annotation: [Type: Cassatio_Zusatz, Value: "litt."]
* Text: de cass. **pensionis**  
  Annotation: [Type: Cassatio_Zusatz, Value: "pensionis."]
  

#### Label: Collatio

##### Beschreibung: Ist die Besetzung einer Pfründe.

##### Standard Examples: 

* Text: **coll.**  
  Annotation: [Type: , Value: "coll."]



#### Label: Concessio

##### Beschreibung:
Verleihung / Erlaubnis = Lizenz (?)

##### Standard Examples:

* Text: **conc. transgr.**  
  Annotation: [Type: Concessio, Value: "conc. transgr."]
  * **Hinweis:** vgl. Licentia -> lic. transgr.



#### Label: Confirmatio

##### Beschreibung:
Bestätigung

##### Standard Examples:

* Text: **conf.**  
  Annotation: [Type: Confirmatio, Value: "conf."]

#### Label: Confirmatio_Zusatz

##### Beschreibung:
Kennzeichnung des Gnadeninhalts. Der gesamte Gnadeninhalt wird mit dem Label Confirmatio_Zusatz getaggt, nicht aber die Gnade conf. selbst.

##### Standard Examples:

* Text: conf. **emptionem pratorum ac al. bonorum in villa Diczisow Constant. dioc. ac donationem iuris patron. super par. eccl. in dicta villa ex possess. Eberhardi Burgermaister incole dicti op. factam** 22 oct. 1411 L 157 113.  
  Annotation: [Type: Confirmatio_Zusatz, Value: "emptionem pratorum ac al. bonorum in villa Diczisow Constant. dioc. ac donationem iuris patron. super par. eccl. in dicta villa ex possess. Eberhardi Burgermaister incole dicti op. factam"]



#### Label: de_advoc

##### Beschreibung: Die Verteidigung vor Gericht übernehmen.

##### Standard Examples: 

* Text: de **advoc.** et committ. causam in cur.   
  Annotation: [Type: de_advoc, Value: "advoc."]



#### Label: de_benef.

##### Beschreibung: Gnadenerweis mit Benefizialthematik.

##### Standard Examples: 

* Text: de **benef.** Leod. dioc.  
  Annotation: [Type: de_benef., Value: "benef."]



#### Label: de_committendo

##### Beschreibung:
Auftrag zur weiteren Bearbeitung eines Falles

##### Standard Examples:

* Text: de **committ.**  
  Annotation: [Type: de_committendo, Value: "committ."]



#### Label: Declaratio

##### Beschreibung:
Erklärung

##### Standard Examples:

* Text: **decl.**  
  Annotation: [Type: Declaratio, Value: "decl."]




#### Label: Declaratio_Litteras_Perinde_Valere

##### Beschreibung: Nachbesserung einer Supplik


##### Standard Examples: 

* Text: motu pr. de **perinde valere** gr. expect.   
  Annotation: [Type: Declaratio_Litteras_Perinde_Valere, Value: "perinde valere"]



#### Label: de_fruct._percip.

##### Beschreibung: Gnadenerweis mit Benefizialthematik.

##### Standard Examples: 

* Text: de **fruct. percip.** in absentia    
  Annotation: [Type: de_fruct._percip., Value: "fruct. percip."]





#### Label: de_loco_interdicto

##### Beschreibung: Erlaubnis, trotz Interdikts u.a. die Messe feiern zu dürfen.

##### Standard Examples: 

* Text: de **locis interdictis**  
  Annotation: [Type: de_loco_interdicto, Value: "locis interdictis"]




#### Label: de_n._prom.

##### Beschreibung: Erlaubnis, eine eigentlich notwendige Weihe aufschieben zu dürfen, z.B. wegen eines Studiums.

##### Standard Examples: 

* Text: de **n. prom.** ad 7 an.
  Annotation: [Type: de_n._prom., Value: "n. prom."]




#### Label: de_n._resid.

##### Beschreibung: Erlaubnis, nicht am Ort seines Benefizes wohnhaft sein zu müssen; entgegen der Anwesenheitspflicht.

##### Standard Examples: 

* Text: **n. resid.** ad quinquennium   
  Annotation: [Type: de_n._resid., Value: "n. resid."]




#### Label: de_prom_ad_ord_extra_temp

##### Beschreibung: Erlaubnis, die höheren Weihen schneller als kanonisch vorgesehen empfangen zu dürfen.

##### Standard Examples: 

* Text:  de lic. recip. ord. in curia **extra temp.**   
  Annotation: [Type: de_prom_ad_ord_extra_temp, Value: "extra temp."]




#### Label: de_visitatione_et_reformatione

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: de_visitatione_et_reformatione, Value: ""]

---

#### Label: Derogatio

##### Beschreibung: 
Klauseln, die andere Regelungen / Tatsachen außer Kraft setzen; vgl. das Label NonObstantien.

##### Standard Examples:

* Text: de **derog.**  
  Annotation: [Type: Derogatio, Value: "derog."]
* Text: c. **derog.**  
  Annotation: [Type: Derogatio, Value: "derog."]

#### Label: DerogatioZusatz

##### Beschreibung:
Kennzeichnung des Gnadeninhalts der Derogatio. Der gesamte Gnadeninhalt wird mit dem Label DerogatioZusatz getaggt, nicht aber die Gnade derog. selbst.

##### Standard Examples:

* Text: c. derog. **statut. d. eccl. quod nullus nisi can. actu prebend. et capitul. inibi dign. assequi val.** 6. decb. 1437 S 342 193v.
  Annotation: [Type: DerogatioZusatz, Value: "statut. d. eccl. quod nullus nisi can. actu prebend. et capitul. inibi dign. assequi val."]

##### Other Examples:

* Text: de derog. **antelationum quibusdam aliis prerog. curialium habentibus in concil. Basil. existentibus conc. ratione gr. expect. sue** s.d. 24. apr. 31 20. decb. 1436 S 329 239rs.
  Annotation: [Type: DerogatioZusatz, Value: "antelationum quibusdam aliis prerog. curialium habentibus in concil. Basil. existentibus conc. ratione gr. expect. sue"]
* Text: c. derog. **statutis eccl. s. Petri de optando** 18. aug. 1463 S 566 89r, L 582 63v-65r.
  Annotation: [Type: DerogatioZusatz, Value: "statutis eccl. s. Petri de optando"]

---

#### Label: Dispensatio

##### Beschreibung:
Befreiung, Außerkraftsetzung kirchlicher Gesetze

##### Standard Examples:

* Text: **disp.**  
  Annotation: [Type: Dispensatio, Value: "disp."]

##### Other Examples:

* Text: **disp.** sup. def. nat.  
  Annotation: [Type: Dispensatio, Value: "disp."]
* Text: **disp.** super def. etat. et super prom. ad sacr. ord.  
  Annotation: [Type: Dispensatio, Value: "disp."]
* Text: de **disp.** ut d. Theordericus d. prepos. unac. alio benef. recip. valeat    
  Annotation: [Type: Dispensatio, Value: "disp."]

#### Label: DispensatioZusatz

##### Beschreibung:
Kennzeichnung des Gnadeninhalts. Der gesamte Gnadeninhalt wird mit dem Label DispensatioZusatz getaggt, nicht aber die Gnade disp. selbst.

##### Standard Examples:

* Text: disp. **sup. def. nat.**  
  Annotation: [Type: DispensatioZusatz, Value: "sup. def. nat."]
* Text: disp. **super def. etat. et super prom. ad sacr. ord.**  
  Annotation: [Type: DispensatioZusatz, Value: "super def. etat. et super prom. ad sacr. ord."]
* Text: de disp. **ut d. Theordericus d. prepos. unac. alio benef. recip. valeat**   
  Annotation: [Type: DispensatioZusatz, Value: "ut d. Theordericus d. prepos. unac. alio benef. recip. valeat"]

##### Other Examples:

* Text: n.o. **def. nat. (p.s.)**
  Annotation: [Type: DispensatioZusatz, Value: "def. nat. (p.s.)"]
* Text: de **uberiori** disp.
  Annotation: [Type: DispensatioZusatz, Value: "uberiori"]

#### Label: DispensatioAdIncompatibiliaBeneficia

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: DispensatioSuperDefNat

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: DispensatioSuperImpedimentoMatrimonii

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: DispensatioSuperIrregularitate

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: VisitatioLiminumApostolorum

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

---

#### Label: Erectio

##### Beschreibung:
Erlaubnis zur Errichtung einer neuen kirchlichen Institution oder der Erhebung einer Kaplanei/Vikarie zur Pfarrkirche bzw. Pfarrkirche zur Kollegiatkirche etc.

##### Standard Examples:

* Text: **m. erig.**  
  Annotation: [Type: Erectio, Value: "m. erig."]
* Text: **erig.**  
  Annotation: [Type: Erectio, Value: "erig."]
* Text: **m. instit.**  
  Annotation: [Type: Erectio, Value: "m. instit."]

##### Other Examples:

* Text: **erigere**  
  Annotation: [Type: Erectio, Value: "erigere"]
* Text: de **erectione**  
  Annotation: [Type: Erectio, Value: "erectione"]
* Text: **instit.**  
  Annotation: [Type: Erectio, Value: "instit."]
* Text: de **institutione**  
  Annotation: [Type: Erectio, Value: "institutione."]

---

#### Label: EsusLacticiniorumEsusCarnium

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

---

#### Label: Exemptio

##### Beschreibung:
Befreiung, Ausnahmestellung

##### Standard Examples:

* Text: **exemt.** de iurisdictione ordin.  
  Annotation: [Type: Exemptio, Value: "exemt."]
* Text: **exempt.** de iurisdictione ordin.  
  Annotation: [Type: Exemptio, Value: "exempt."]
* Text: **exemptione** de iurisdictione ordin.  
  Annotation: [Type: Exemptio, Value: "exemptione"] 

##### Other Examples:

* Text: **exemtione** de iurisdictione ordin.  
  Annotation: [Type: Exemptio, Value: "exemtione"]

---

#### Label: Facultas

##### Beschreibung:
Erlaubnis. Vgl. Lizenz und Concessio (?)

##### Standard Examples:

* Text: **facult.** resign.  
  Annotation: [Type: Facultas, Value: "facult."]

##### Other Examples:

* Text: **facult.** absol. eos, qui…  
  Annotation: [Type: Facultas, Value: "facult."]
* Text: **facult.** absol. 100 person.  
  Annotation: [Type: Facultas, Value: "facult."]
* Text: **facult.** absol. in casibus, in quibus …  
  Annotation: [Type: Facultas, Value: "facult."]  
* Text: **facult.** reconciliandi  
  Annotation: [Type: Facultas, Value: "facult."]
* Text: alternativa **facult.** disponendi  
  Annotation: [Type: Facultas, Value: "facult."]

#### Label: FacultasZusatz

##### Beschreibung:
Kennzeichnung des Gnadeninhalts. Der gesamte Gnadeninhalt wird mit dem Label FacultasZusatz getaggt, nicht aber die Gnade facult. selbst.

##### Standard Examples:

* Text: facult. **resign.**  
  Annotation: [Type: FacultasZusatz, Value: "resign."]
* Text: facult. **absol. eos, qui (unknown)**  
  Annotation: [Type: FacultasZusatz, Value: "absol. eos, qui (unknown)"]
  * **Hinweis:** (unknown) steht für den Rest des Relativsatzes.
* Text: facult. **absol. 100 person.**  
  Annotation: [Type: FacultasZusatz, Value: "absol. 100 person."]

##### Other Examples:

* Text: facult. **absol. in casibus, in quibus (unknown)**  
  Annotation: [Type: FacultasZusatz, Value: "absol. in casibus, in quibus (unknown)"]
  * **Hinweis:** (unknown) steht für den Rest des Relativsatzes.
* Text: facult. **reconciliandi**  
  Annotation: [Type: FacultasZusatz, Value: "reconciliandi"]
* Text: **alternativa** facult. **disponendi**  
  Annotation: 
  - [Type: FacultasZusatz, Value: "alternativa"]
  - [Type: FacultasZusatz, Value: "disponendi"]

#### Label: FacultasAbsolvendi

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: FacultasReconciliandi

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: FacultasResignandi

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

---

#### Label: Habilitatio

##### Beschreibung:
Wiederherstellung der Befähigung zur Ausübung einer Rechtshandlung

##### Standard Examples:

* Text: **habil.**  
  Annotation: [Type: Habilitatio, Value: "habil."]
* Text: **rehab.**  
  Annotation: [Type: Habilitatio, Value: "rehab."]

##### Other Examples: 

* Text: **rehabilitatio**  
  Annotation: [Type: Habilitatio, Value: "rehabilitatio"]
* Text: **habilitatio**  
  Annotation: [Type: Habilitatio, Value: "habilitatio"]

---

#### Label: Incorporatio

##### Beschreibung:
Einverleibung einer kirchlichen Institution durch eine andere

##### Standard Examples:

* Text: **inkorp.**  
  Annotation: [Type: Incorporatio, Value: "inkorp."]
* Text: **unio**  
  Annotation: [Type: Incorporatio, Value: "unio"]

---

#### Label: Indulgentia

##### Beschreibung:
Indulgenz, Ablass

##### Standard Examples:

* Text: **indulg.**  
  Annotation: [Type: Indulgentia, Value: "indulg."]

---

#### Label: Indultum

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

---

#### Label: Introductio

##### Beschreibung:
Einführung in die Besitztümer einer Pfründe

##### Standard Examples:

* Text: **m. introduc. in possess.**  
  Annotation: [Type: Introductio, Value: "m. introduc. in possess."]
* Text: **in possessionem** bonorum eorum eccl. **introducat**  
  Annotation: 
  - [Type: Introductio, Value: "in possessionem"]
  - [Type: Introductio, Value: "introducat"]

---
#### Label: Licentia

##### Beschreibung:
Sondererlaubnis

##### Standard Examples:

* Text: **lic.**  
  Annotation: [Type: Licentia, Value: "lic."]
* Text: **m. lic.**  
  Annotation: [Type: Licentia, Value: "m. lic."]

##### Other Examples:

* Text: **lic.** de ante diem  
  Annotation: [Type: Licentia, Value: "lic."]
* Text: **lic.** armuciis de vario et griseo utendi  
  Annotation: [Type: Licentia, Value: "lic."]
* Text: **lic.** visitandi Sepulcrum Dominicum  
  Annotation: [Type: Licentia, Value: "lic."]
* Text: **lic.** ratione par. eccl. s. Martini, … in casu quod rect. unius ex d. eccl. fuerit excom., per alios presb. sibi sacramenta ministrari faciendi  
  Annotation: [Type: Licentia, Value: "lic."]

#### Label: LicentiaZusatz

##### Beschreibung:
Kennzeichnung des Gnadeninhalts. Der gesamte Gnadeninhalt wird mit dem Label LicentiaZusatz getaggt, nicht aber die Gnade lic. selbst.

##### Standard Examples:

* Text: lic. **de ante diem**  
  Annotation: [Type: LicentiaZusatz, Value: "de ante diem"]
* Text: lic. **armuciis de vario et griseo utendi**  
  Annotation: [Type: LicentiaZusatz, Value: "armuciis de vario et griseo utendi"]
* Text: lic. **visitandi Sepulcrum Dominicum**  
  Annotation: [Type: LicentiaZusatz, Value: "visitandi Sepulcrum Dominicum"]

##### Other Examples:

* Text: lic. **ratione par. eccl. s. Martini, … in casu quod rect. unius ex d. eccl. fuerit excom., per alios presb. sibi sacramenta ministrari faciendi**  
  Annotation: [Type: LicentiaZusatz, Value: "ratione par. eccl. s. Martini, … in casu quod rect. unius ex d. eccl. fuerit excom., per alios presb. sibi sacramenta ministrari faciendi"]

#### Label: LicentiaArrendandiLocandi

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: LicentiaDemoliendi

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: LicentiaDicendiHorasCanonicas

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: LicentiaPermutandi

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: LicentiaStudendi

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: LicentiaTacendiSuperDefectuNatalium

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: LicentiaTestandi

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

---

#### Label: LitteraConservatoriaBonorum

##### Beschreibung:
Schutzbrief

##### Standard Examples:

* Text: de **conserv.**  
  Annotation: [Type: LitteraConservatoriaBonorum, Value: "conserv."]

---

#### Label: LitteraDimissoralis

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

---

#### Label: LitteraPassus

##### Beschreibung:
Reiseerlaubnis und Schutzbrief

##### Standard Examples:

* Text: **litt. passus**  
  Annotation: [Type: LitteraPassus, Value: "litt. passus"]
* Text: **littera passus**  
  Annotation: [Type: LitteraPassus, Value: "littera passus"]

---

#### Label: LitteraTestimonialibus

##### Beschreibung:
Bescheinigung, Zeugnis

##### Standard Examples:

* Text: **testimonialis litt.** vicecamerarii ad senatorem Urbis quod d. calcelarii iurisdictioni mareschalli R. cur. suppositi sint 20. febr. 1432 DC 16 183rs.  
  Annotation: [Type: LitteraTestimonialibus, Value: "testimonialis litt."]

#### Label: LitteraTestimonialibusZusatz

##### Beschreibung:
Inhaltliche Beschreibung der Bescheinigung bzw. des Zeugnisses

##### Standard Examples:

* Text: testimonialis litt. **vicecamerarii ad senatorem Urbis quod d. calcelarii iurisdictioni mareschalli R. cur. suppositi sint** 20. febr. 1432 DC 16 183rs.
  Annotation: [Type: LitteraTestimonialibusZusatz, Value: "vicecamerarii ad senatorem Urbis quod d. calcelarii iurisdictioni mareschalli R. cur. suppositi sint"]

---

#### Label: Monitorium

##### Beschreibung:
Ermahnung durch den Papst

##### Standard Examples:

* Text: **monitorium penale**  
  Annotation: [Type: Monitorium, Value: "monitorium penale"]

---

#### Label: Moratorium

##### Beschreibung:
Zahlungsaufschub

##### Standard Examples:

* Text: de **moratorio**  
  Annotation: [Type: Moratorium, Value: "moratorio"]
* Text: **moratorium**  
  Annotation: [Type: Moratorium, Value: "moratorium"]

##### Hinweis
Hauptsächlich in RG 10 (?)

---

#### Label: MutatioCollatoris

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

---

#### Label: Pensio

##### Beschreibung:
Verleihung und Modifizierung von Pensionsleistunen

##### Standard Examples:

* Text: de **reductione pensionis**  
  Annotation: [Type: Pensio, Value: "reductione pensionis"]
* Text: de **transl. pensionis**  
  Annotation: [Type: Pensio, Value: "transl. pensionis"]



#### Label: Plenarablass

##### Beschreibung: Erlaubnis des einmaligen vollkommenen Ablasses

##### Standard Examples:
* Text: de **rem. plen.**  
  Annotation: [Type: Plenarablass, Value: "rem. plen."]



  
#### Label: Prerogativa

##### Beschreibung:
Vorrecht, Prärogative

##### Standard Examples:

* Text: **prerog.** ad instrar pape fam.  
  Annotation: [Type: Prerogativa, Value: "prerog."]
* Text: **antelatio**  
  Annotation: [Type: Prerogativa, Value: "antelatio"]

##### Other Examples:

* Text: **prerog.** pape fam. in absentia  
  Annotation: [Type: Prerogativa, Value: "prerog."]

#### Label: PrerogatioAdInstarPapeFamilaris

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: PrerogatioPapeFamiliarisInAbsentia

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

---

#### Label: Prorogatio

##### Beschreibung:
Fristverlängerung

##### Standard Examples:

* Text: **prorog.**  
  Annotation: [Type: Prorogatio, Value: "prorog."]

##### Other Examples: 

* Text: cum **prorog.** term. solut. ad 1 an. propter incertitudinem taxe  
  Annotation: [Type: Prorogatio, Value: "prorog."]

#### Label: ProrogatioZusatz

##### Beschreibung:
Kennzeichnung des Gnadeninhalts. Der gesamte Gnadeninhalt wird mit dem Label ProrogatioZusatz getaggt, nicht aber die Gnade prorog. selbst.

##### Standard Examples:

* Text: cum prorog. **term. solut. ad 1 an. propter incertitudinem taxe**  
  Annotation: [Type: ProrogatioZusatz, Value: "term. solut. ad 1 an. propter incertitudinem taxe"]

---

#### Label: Provisio

##### Beschreibung:
Bestimmungen zur Verleihung eines Benefizes

##### Standard Examples:

* Text: **prov.**  
  Annotation: [Type: Provisio, Value: "prov."]
* Text: **m. prov.**  
  Annotation: [Type: Provisio, Value: "m. prov."]
* Text: **nova prov.**  
  Annotation: [Type: Provisio, Value: "nova prov."]

##### Other Examples:

* Text: **prov. si neutri**  
  Annotation: [Type: Provisio, Value: "prov. si neutri"]
* Text: **prov. si nulli**  
  Annotation: [Type: Provisio, Value: "prov. si nulli"]
* Text: **surrog.** ad iur.  
  Annotation: [Type: Provisio, Value: "surrog."]
* Text: **gr. expect.**  
  Annotation: [Type: Provisio, Value: "gr. expect."]

#### Label: EinfacheProvisio

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: GratiaExpectativa

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: NovaProvisio

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: ProvisioSiNeutri

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: ProvisioSiNulli

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

#### Label: SurrogatioAdIus

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

---

#### Label: Reformatio

##### Beschreibung:
Abänderung, Nachbesserung einer päpstlichen Gnade (?)

##### Standard Examples:

* Text: **ref.**  
  Annotation: [Type: Reformatio, Value: "ref."]
* Text: **reformatio**  
  Annotation: [Type: Reformatio, Value: "reformatio"]

---

#### Label: Rehabilitatio

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

---

#### Label: Reservatio

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

---

#### Label: Revalidatio

##### Beschreibung:
Erklärung der Gültigkeit einer verfallenen Gnade

##### Standard Examples:

* Text: **reval.**  
  Annotation: [Type: Revalidatio, Value: "reval."]

---

#### Label: SalvusConductus

##### Beschreibung:
Sicherheitsbrief für flüchtige Personen

##### Standard Examples:

* Text: **salv. cond.**  
  Annotation: [Type: SalvusConductus, Value: "salv. cond."]
* Text: **salvus conductus**  
  Annotation: [Type: SalvusConductus, Value: "salvus conductus"]
* Text: **salc. cond.**  
  Annotation: [Type: SalvusConductus, Value: "salc. cond."]
  * **Hinweis:** Achtung: im Digitalisat von Band 3 falsch eingelesen als salc. statt salv.
 
---

#### Label: TragbarerAltar

##### Beschreibung: 

##### Standard Examples:
* Text: gratia de **alt. port.**  
  Annotation: [Type: TragbarerAltar, Value: "alt. port."]
* Text: de **alt. port.**  
  Annotation: [Type: TragbarerAltar, Value: "alt. port."]




#### Label: Unio

##### Beschreibung: 

##### Standard Examples: 

* Text: ****  
  Annotation: [Type: , Value: ""]

---

#### Label: WeitereGnaden [bitte einzeln wie oben und mit Ontologie-Klasse "Gnadenerweis" abgleichen und ergänzen]

##### Standard Examples:

* Text: de **locis interdictis**  
  Annotation: [Type: UndefinierteGnade, Value: "locis interdictis"]
* Text: de **interd. loc.**  
  Annotation: [Type: UndefinierteGnade, Value: "interd. loc."]
* Text: de **benef.**  
  Annotation: [Type: UndefinierteGnade, Value: "benef."]
* Text: de **prom. ad ord.**  
  Annotation: [Type: UndefinierteGnade, Value: "prom. ad ord."]
* Text: de **prom. ad ord. extra temp.**  
  Annotation: [Type: UndefinierteGnade, Value: "prom. ad ord. extra temp."]
* Text: de **n. prom.**  
  Annotation: [Type: UndefinierteGnade, Value: "n. prom."]
* Text: de **n. prom. ad ord.**  
  Annotation: [Type: UndefinierteGnade, Value: "n. prom. ad ord."]
* Text: de **n. resid.**  
  Annotation: [Type: UndefinierteGnade, Value: "n. resid."]
* Text: de **fruct. percip.**  
  Annotation: [Type: UndefinierteGnade, Value: "fruct. percip."]
* Text: de **visitatione et reformatione**  
  Annotation: [Type: UndefinierteGnade, Value: "visitatione et reformatione"]
* Text: supplic. **pro diversis**  
  Annotation: [Type: UndefinierteGnade, Value: "pro diversis"]
* Text: de **pont. insign.**  
  Annotation: [Type: UndefinierteGnade, Value: "pont. insign."]

---

### Event: Zahlungsverpflichtung

#### Label: Zahlungsverpflichtung

##### Beschreibung:
Angaben zu einer Zahlungsverpflichtung.

##### Standard Examples:

* Text: **oblig.**    
  Annotation: [Type: Zahlungsverpflichtung, Value: "oblig."] 

---

### Event: Geldzahlung

#### Label: Geldzahlung

##### Beschreibung:
Angaben zu einer Geldzahlung.

##### Standard Examples:

* Text: **solv.**    
  Annotation: [Type: Geldzahlung, Value: "solv."] 

---

### Event: Gerichtsprozess

#### Label: Gerichtsprozess

##### Beschreibung:
Angaben zu einem Gerichtsprozess.

##### Standard Examples:

* Text: **litig.**  
  Annotation: [Type: Gerichtsprozess, Value: "litig."]
* Text: **constit. iudices appellat.**    
  Annotation: [Type: Gerichtsprozess, Value: "constit. iudices appellat."]

---

### Event: Treueschwur

#### Label: Treueschwur

##### Beschreibung:
Angaben zu einem Treueschwur.

##### Standard Examples:
* Text: **iuram. fidel.**    
  Annotation: [Type: Treueschwur, Value: "iuram. fidel."]

---

### Event: Tod

#### Label: Tod

##### Beschreibung:
Angaben zum Tod einer Person.

##### Standard Examples:
* Text: vac. p. **o.**    
  Annotation: [Type: Tod, Value: "o."]
* Text: **defuncti**    
  Annotation: [Type: Tod, Value: "defuncti"]
* Text: **mori**   
  Annotation: [Type: Tod, Value: "o."]
* Text: **quond.**    
  Annotation: [Type: Tod, Value: "quond."]

---

### Event: Weihe

#### Label: Weihe

##### Beschreibung:
Angaben zum Weihempfang.

##### Standard Examples:
* Text: **prom.**  
  Annotation: [Type: Weihe, Value: "prom."]

---

### Event: Resignation

#### Label: Resignation

##### Beschreibung:
Angaben zur Aufgabe einer Pfründe.

##### Standard Examples:
* Text: **resign.**  
  Annotation: [Type: Resignation, Value: "resign."]

---

### Event: Entsendung

#### Label: Entsendung

##### Beschreibung:
Jemand beauftragt eine Person, irgendwohin zu gehen.
  
##### Standard Examples:
* Text: **destin.**    
  Annotation: [Type: Entsendung, Value: "destin."]

---

### Event: ErlangungPfründe

#### Label: ErlangungPfründe

##### Beschreibung:
Angaben zur Erlangung einer Pfründe (assec. est); nicht identisch mit dem Gnadenerweis der bloßen Provision einer Pfründe.

##### Standard Examples:
* Text: **assec. est**  
  Annotation: [Type: ErlangungPfründe, Value: "assec. est"]
* Text: **indebite assec. fuit**  
  Annotation: [Type: ErlangungPfründe, Value: "indebite assec. fuit"]

---
### Event: Pfründenentzug

#### Label: Pfründenentzug

##### Beschreibung:
Jemand, z.B. der Papst, entzieht jemandem Rechte/Pfründen etc. (privatio)

##### Standard Examples:
* Text: adherens Barth. **priv.** can. et preb.  
  Annotation: [Type: Pfründenentzug, Value: "priv."]

---

### Kategorie: Varia

---
#### Label: Vakanzgrund

##### Beschreibung:
Gründe, die für die Vakanz einer Pfründe gegeben werden.

##### Standard Examples:

* Text: **vac. p. o.**  
  Annotation: [Type: EventNichtPapst, Value: "vac. p. o."]
* Text: **vacat. p. o.**  
  Annotation: [Type: EventNichtPapst, Value: "vacat. p. o."]
  * **Hinweis:** Neben p.o., das als Abkürzung für per obitum am häufigsten vorkommt, gibt es in Band 1 und 3 des RG per ob. als Alternative und in Band 9 p.o. in curia.
* Text: **vac. p. prom.**  
  Annotation: [Type: EventNichtPapst, Value: "vac. p. prom."]

##### Other Examples:

* Text: **vac. p. n. prom.**  
  Annotation: [Type: EventNichtPapst, Value: "vac. p. n. prom."]
* Text: **vac. p. priv.**  
  Annotation: [Type: EventNichtPapst, Value: "vac. p. priv."]
* Text: **vac. p. devol.**  
  Annotation: [Type: EventNichtPapst, Value: "vac. p. devol."]
* Text: **vac. p. transgr.**  
  Annotation: [Type: EventNichtPapst, Value: "vac. p. transgr."]
* Text: **vac. p. resign.**  
  Annotation: [Type: EventNichtPapst, Value: "vac. p. resign."]
* Text: **vac. p. assec.**  
  Annotation: [Type: EventNichtPapst, Value: "vac. p. assec."]
* Text: **vac. p. ingress. relig.**  
  Annotation: [Type: EventNichtPapst, Value: "vac. p. ingress. relig."]
* Text: **vac. p. contract. matrim.**  
  Annotation: [Type: EventNichtPapst, Value: "vac. p. contract. matrim."]
* Text: **vac. ex eo quod** …  
  Annotation: [Type: EventNichtPapst, Value: "vac. ex eo quod"]

---

#### Label: Herrschaftsgebiet

##### Beschreibung:
Bezeichnungen für weltliche Herrschaftsgebiete, z.B. Herzogtümer.

##### Standard Examples:
* Text: **ducat.**  
  Annotation: [Type: Herrschaftsgebiet, Value: "ducat."]
* Text: **baron.**  
  Annotation: [Type: Herrschaftsgebiet, Value: "baron."]

---
#### Label: Stadt_Dorf

##### Beschreibung:
Bezeichnungen für Städte und Dörfer; die Begriffe sind nicht immer klar zu unterscheiden, deshalb bekommen sie ein Label.

##### Standard Examples:
* Text: **op.**  
  Annotation: [Type: Verwaltungseinheit, Value: "op."]
* Text: **op. imp.**  
  Annotation: [Type: Verwaltungseinheit, Value: "op. imp."]
* Text: **villa**  
  Annotation: [Type: Verwaltungseinheit, Value: "villa"]
* Text: **civit.**  
  Annotation: [Type: Stadt_Dorf, Value: "civit."]

---
#### Label: Diözese

##### Beschreibung:
Eine kirchliche Verwaltungseinheit.

##### Standard Examples:

* Text: **Traiect. dioc.**  
  Annotation: [Type: Diözese, Value: "Traiect. dioc."]
* Text: **dioc. Traiect.**  
  Annotation: [Type: Diözese, Value: "dioc. Traiect."]


##### Other Examples:

* Text: **Magunt. dioc.**  
  Annotation: [Type: Diözese, Value: "Magunt. dioc."]
* Text: **Colon. dioc.**  
  Annotation: [Type: Diözese, Value: "Colon. dioc."]

---

#### Label: Institution

##### Beschreibung:
Kirchen, Klöster, Universitäten, etc.

##### Standard Examples:

* Text: **eccl.**  
  Annotation: [Type: Institution, Value: "eccl."]
* Text: **par. eccl.**  
  Annotation: [Type: Institution, Value: "par. eccl."]
* Text: **mon.**  
  Annotation: [Type: Institution, Value: "mon."]

##### Other Examples:

* Text: **capit.**  
  Annotation: [Type: Institution, Value: "capit."]
* Text: **capit. eccl.**  
  Annotation: [Type: Institution, Value: "capit. eccl."]
* Text: **fil. eccl.**  
  Annotation: [Type: Institution, Value: "fil. eccl."]
* Text: **fil. par. eccl.**  
  Annotation: [Type: Institution, Value: "fil. par. eccl."]
* Text: **colleg. eccl.**  
  Annotation: [Type: Institution, Value: "colleg. eccl."]
* Text: **capel.**  
  Annotation: [Type: Institution, Value: "capel."]
* Text: **cathedr.**  
  Annotation: [Type: Institution, Value: "cathedr."]
* Text: **conv.**  
  Annotation: [Type: Institution, Value: "conv."]
* Text: **ord.**  
  Annotation: [Type: Institution, Value: "ord."]
* Text: **cam.**  
  Annotation: [Type: Institution, Value: "cam."]
* Text: **penit.**  
  Annotation: [Type: Institution, Value: "penit."]
* Text: **pen.**  
  Annotation: [Type: Institution, Value: "pen."]
* Text: **abbatia**  
  Annotation: [Type: Institution, Value: "abbatia"]
* Text: **hosp. paup.**  
  Annotation: [Type: Institution, Value: "hosp. paup."]
* Text: **conv.** mon.  
  Annotation: [Type: Institution, Value: "conv."]
* Text: **dom.**  
  Annotation: [Type: Institution, Value: "dom."]
  * **Hinweis:** Achtung: dom. nur als Institution taggen, wenn es für domus steht, nicht für dominus.
* Text: **domus**  
  Annotation: [Type: Institution, Value: "domus"]
* Text: **preceptoria**  
  Annotation: [Type: Institution, Value: "preceptoria"]
* Text: **prioratus**  
  Annotation: [Type: Institution, Value: "prioratus"]  

---

#### Label: InstitutionZusatz

##### Beschreibung:
Information zur Beziehung einer kirchlichen Institution zur Kurie, insbesondere die direkte Unterstellung unter den Papst (Exemption). 

##### Standard Examples:

* Text: eccl. b. Marie castri Aldenburg. Rom. eccl. **immed. subiect.**  
  Annotation: [Type: Institution, Value: "immed. subiect."]

---

#### Label: Titelkirche

##### Beschreibung:
Kirchen, die Bischöfen, Priestern und Diakonen bei ihrer Kardinalsweihe zugeteilt werden. Ihre Anzahl ist finit. Man erkennt sie v.a. daran, dass in ihrer Nähe im Regest ein Kardinal genannt wird (ep. card., presb. card., diac. card.). In diesen Fällen wird ausnahmsweise darauf verzichtet, zusätzlich das Patrozinium oder den Ort als solche gesondert zu taggen.

##### Standard Examples:

* **Titelkirchen Kardinalbischöfe:**
  * Text: **Albanen.**  
    Annotation: [Type: Titelkirche, Value: "Albanen."]
  * Text: **Ostien. et Velletren.**  
    Annotation: [Type: Titelkirche, Value: "Ostien. et Velletren."]
  * Text: **Portuen. et s. Rufinae**  
    Annotation: [Type: Titelkirche, Value: "Portuen. et s. Rufinae"]
* **Titelkirchen Kardinalpriester:**
  * Text: **S. Anastasiae**  
    Annotation: [Type: Titelkirche, Value: "S. Anastasiae"]
  * Text: **Ss. XII Apostolorum**  
    Annotation: [Type: Titelkirche, Value: "Ss. XII Apostolorum"]
  * Text: **S. Balbinae**  
    Annotation: [Type: Titelkirche, Value: "S. Balbinae"]

##### Other Examples:

* **Titelkirchen Kardinalbischöfe:**
  * Text: **Praenestin.**  
    Annotation: [Type: Titelkirche, Value: "Praenestin."]
  * Text: **Sabinen.**  
    Annotation: [Type: Titelkirche, Value: "Sabinen."]
  * Text: **Tusculan.**  
    Annotation: [Type: Titelkirche, Value: "Tusculan."]
* **Titelkirchen Kardinalpriester:**
  * Text: **S. Caeciliae**  
    Annotation: [Type: Titelkirche, Value: "S. Caeciliae"]
  * Text: **S. Chrysogoni**  
    Annotation: [Type: Titelkirche, Value: "S. Chrysogoni"]
  * Text: **S. Clementis**  
    Annotation: [Type: Titelkirche, Value: "S. Clementis"]
  * Text: **Ss. IV Coronatorum**  
    Annotation: [Type: Titelkirche, Value: "Ss. IV Coronatorum"]
  * Text: **S. Crucis in Jerusalem**  
    Annotation: [Type: Titelkirche, Value: "S. Crucis in Jerusalem"]
  * Text: **S. Cyriaci**  
    Annotation: [Type: Titelkirche, Value: "S. Cyriaci"]
  * Text: **Ss. Joannis et Pauli**  
    Annotation: [Type: Titelkirche, Value: "Ss. Joannis et Pauli"]
  * Text: **S. Laurentii in Damaso**  
    Annotation: [Type: Titelkirche, Value: "S. Laurentii in Damaso"]
  * Text: **S. Laurentii in Lucina**  
    Annotation: [Type: Titelkirche, Value: "S. Laurentii in Lucina"]
  * Text: **S. Marcelli**  
    Annotation: [Type: Titelkirche, Value: "S. Marcelli"]
  * Text: **Ss. Marcellini et Petri**  
    Annotation: [Type: Titelkirche, Value: "Ss. Marcellini et Petri"]
  * Text: **S. Marci**  
    Annotation: [Type: Titelkirche, Value: "S. Marci"]
  * Text: **S. Mariae trans Tiberim**  
    Annotation: [Type: Titelkirche, Value: "S. Mariae trans Tiberim"]
  * Text: **S. Martini in montibus**  
    Annotation: [Type: Titelkirche, Value: "S. Martini in montibus"]
  * Text: **Ss. Nerei et Achillei**  
    Annotation: [Type: Titelkirche, Value: "Ss. Nerei et Achillei"]
  * Text: **S. Nicolai ad (inter) imagines**  
    Annotation: [Type: Titelkirche, Value: "S. Nicolai ad (inter) imagines"]
  * Text: **S. Petri ad vincula**  
    Annotation: [Type: Titelkirche, Value: "S. Petri ad vincula"]
  * Text: **S. Praxedis**  
    Annotation: [Type: Titelkirche, Value: "S. Praxedis"]
  * Text: **S. Priscae**  
    Annotation: [Type: Titelkirche, Value: "S. Priscae"]
  * Text: **S. Pudentianae**  
    Annotation: [Type: Titelkirche, Value: "S. Pudentianae"]
  * Text: **S. Sabinae**  
    Annotation: [Type: Titelkirche, Value: "S. Sabinae"]
  * Text: **Ss. Silvestri et Martini**  
    Annotation: [Type: Titelkirche, Value: "Ss. Silvestri et Martini"]
  * Text: **S. Sixti**  
    Annotation: [Type: Titelkirche, Value: "S. Sixti"]
  * Text: **S. Stephani in Coelio monte**  
    Annotation: [Type: Titelkirche, Value: "S. Stephani in Coelio monte"]
  * Text: **S. Susannae**  
    Annotation: [Type: Titelkirche, Value: "S. Susannae"]
  * Text: **S. Vitalis**  
    Annotation: [Type: Titelkirche, Value: "S. Vitalis"]
* **Titelkirchen Kardinaldiakone:**
  * Text: **S. Adriani**  
    Annotation: [Type: Titelkirche, Value: "S. Adriani"]
  * Text: **S. Agathae**  
    Annotation: [Type: Titelkirche, Value: "S. Agathae"]
  * Text: **S. Angeli in foro piscium**  
    Annotation: [Type: Titelkirche, Value: "S. Angeli in foro piscium"]
  * Text: **Ss. Cosmae et Damiani**  
    Annotation: [Type: Titelkirche, Value: "Ss. Cosmae et Damiani"]
  * Text: **S. Eustachii**  
    Annotation: [Type: Titelkirche, Value: "S. Eustachii"]
  * Text: **S. Georgii ad velum aureum**  
    Annotation: [Type: Titelkirche, Value: "S. Georgii ad velum aureum"]
  * Text: **S. Luciae in Orthea (Silice)**  
    Annotation: [Type: Titelkirche, Value: "S. Luciae in Orthea (Silice)"]
  * Text: **S. Luciae in Septemsoliis**  
    Annotation: [Type: Titelkirche, Value: "S. Luciae in Septemsoliis"]
  * Text: **S. Mariae in Aquiro**  
    Annotation: [Type: Titelkirche, Value: "S. Mariae in Aquiro"]
  * Text: **S. Mariae in Cosmedin**  
    Annotation: [Type: Titelkirche, Value: "S. Mariae in Cosmedin"]
  * Text: **S. Mariae novae**  
    Annotation: [Type: Titelkirche, Value: "S. Mariae novae"]
  * Text: **S. Mariae in Porticu**  
    Annotation: [Type: Titelkirche, Value: "S. Mariae in Porticu"]
  * Text: **S. Mariae in via lata**  
    Annotation: [Type: Titelkirche, Value: "S. Mariae in via lata"]
  * Text: **S. Nicolai in carcere Tulliano**  
    Annotation: [Type: Titelkirche, Value: "S. Nicolai in carcere Tulliano"]
  * Text: **Ss. Sergii et Bacchi**  
    Annotation: [Type: Titelkirche, Value: "Ss. Sergii et Bacchi"]
  * Text: **S. Theodori**  
    Annotation: [Type: Titelkirche, Value: "S. Theodori"]
  * Text: **Ss. Viti et Modesti**  
    Annotation: [Type: Titelkirche, Value: "Ss. Viti et Modesti"]

---

#### Label: Patrozinium

##### Beschreibung:
Namenspatrone von Kirchen oder Institutionen.

##### Standard Examples:

* Text: **s. Jacobi**  
  Annotation: [Type: Patrozinium, Value: "s. Jacobi"]
* Text: **b. Marie**  
  Annotation: [Type: Patrozinium, Value: "b. Marie"]
* Text: **s. Johannis bapt.**  
  Annotation: [Type: Patrozinium, Value: "s. Johannis bapt."]

##### Other Examples:

* Text: **s. Johannis ev.**  
  Annotation: [Type: Patrozinium, Value: "s. Johannis ev."]
* Text: **s. crucis**  
  Annotation: [Type: Patrozinium, Value: "s. crucis"]  

---

#### Label: Objekt

##### Beschreibung:
unspezifizierte Objekte.

##### Standard Examples:

* Text: **alt.**  
  Annotation: [Type: Objekt, Value: "alt."]
* Text: **alt. port.**  
  Annotation: [Type: Objekt, Value: "alt. port."]
  * **Hinweis:** s. UndefinierteGnade

---

#### Label: Name_Ort

##### Beschreibung:
Namen von Städten, Dörfern, Regionen und Bergen (s. Notizen unten).

##### Standard Examples:

* Text: **Bodegrauen**  
  Annotation: [Type: Name_Ort, Value: "Bodegrauen"]
* Text: Novifori **Magdeburg.**  
  Annotation: [Type: Name_Ort, Value: "Magdeburg."]
* Text: in castro **Quernfort**  
  Annotation: [Type: Name_Ort, Value: "Quernfort"]
* Text: **Slesia**  
  Annotation: [Type: Name_Ort, Value: "Slesia"]  

##### Other Examples:
* Text: in **Rauhen** et in **Schlechthin Kulm** castris
  Annotation: [Type: Name_Ort, Value: "Rauhen"]
  Annotation: [Type: Name_Ort, Value: "Schlechthin Kulm"]
* Text: **Civitasnova**  
  Annotation: [Type: Name_Ort, Value: "Civitasnova"]

---

#### Label: Kurie

##### Beschreibung:
Die Kurie ist an dem Ort, an dem der Papst ist.

##### Standard Examples:

* Text: apud. **cur.**  
  Annotation: [Type: Kurie, Value: "cur."]
* Text: **ap. sed.**  
  Annotation: [Type: Kurie, Value: "ap. sed."]

---
#### Label: Burg

##### Beschreibung:
Ein Bauwerk, das militärischen, administrativen und herrschaftlichen Zwecken dient.

##### Standard Examples:
* Text: in **castro** Quernfort  
  Annotation: [Type: Burg, Value: "castro"]

---

#### Label: Vorstadt

##### Beschreibung:
Ein Ort außerhalb der Stadtmauern (=Vorstadt) wird im RG über die Abkürzung "e. m." ("extra muros") angegeben.

##### Standard Examples:
* Text: eccl. s. Victoris **e. m.** Magunt.
  Annotation: [Type: Vorstadt, Value: "e. m."]

---

#### Label: Konzil

##### Beschreibung:
Kirchliches Konzil / Synode

##### Standard Examples:

* Text: **concil.**  
  Annotation: [Type: Konzil, Value: "concil."]

---

#### Label: Expeditionsmodalitäten

##### Beschreibung:
In den Regesten werden manchmal Angaben dazu gemacht, wie der Gnadenbrief ausgestellt werden soll. 
- motu proprio: Drückt aus, dass ein Brief - im Gegensatz zum üblichen Reskriptionsverfahren – vom Papst selbst ausgeht; Ausdruck besonderen Wohlwollens.
- sola signatura: Es wird kein Gnadenbrief ausgestellt; die Genehmigung des Gesuches wird durch eine Unterschrift auf der Supplik angezeigt.
- rationi congruit: Vermerk, dass die Gnade bereits genehmigt worden war, aber vor dem Tod des Papstes nicht mehr expediert werden konnte.
- gratis: Die Expedition der Urkunde erfolgt kostenlos für den Petenten.

##### Standard Examples:

* Text: **motu pr.**  
  Annotation: [Type: Expeditionsmodalitäten, Value: "motu pr."]
* Text: **sola signatura**  
  Annotation: [Type: Expeditionsmodalitäten, Value: "sola signatura"]  

---

#### Label: Annaten

##### Beschreibung:
Zahlungen an den Papst für die Verleihung einer Pfründe.

##### Standard Examples:

* Text: **annat.**  
  Annotation: [Type: Annaten, Value: "annat."]
* Text: **annata**  
  Annotation: [Type: Annaten, Value: "annata"]

---

#### Label: Servitien

##### Beschreibung:
Zahlungen des Bischöfe und einiger Äbte an den Papst anlässlich ihrer Einsetzung.

##### Standard Examples:

* Text: **serv.**  
  Annotation: [Type: Servitien, Value: "serv."]
* Text: 5 min. **serv.**  
  Annotation: [Type: Servitien, Value: "serv."]
* Text: comm. **serv.**  
  Annotation: [Type: Servitien, Value: "serv."]

---

#### Label: Geldsumme

##### Beschreibung:
Geldbeträge in historischen Einheiten (Betrag und Währung).

##### Standard Examples:

* Text: **9 fl.**  
  Annotation: [Type: Geldsumme, Value: "9 fl."]
* Text: **4 m. arg.**  
  Annotation: [Type: Geldsumme, Value: "4 m. arg."]

---

#### Label: Dauer

##### Beschreibung:
Dauer eines Dispens, einer Pfründe etc.

##### Standard Examples:

* Text: **3 an.**  
  Annotation: [Type: Dauer, Value: "3 an."]
* Text: **perp.**  
  Annotation: [Type: Dauer, Value: "perp."]

---

#### Label: NonObstantien

##### Beschreibung:
Klauseln, die andere Regelungen / Tatsachen außer Kraft setzen; vgl. die Label Derogatio und DerogatioZusatz.

##### Standard Examples:

* Text: **n. o.** can. et preb.
  Annotation: [Type: NonObstantien, Value: "n. o."]
  * **Häufigkeit** 4459x in den Bänden 1-9

##### Other Examples:

* Text: **n. o.** par. eccl.
  Annotation: [Type: NonObstantien, Value: "n. o."]
  * **Häufigkeit** 2665x in den Bänden 2-4 und 6-8
* Text: **n. o.** def. nat.  
  Annotation: [Type: NonObstantien, Value: "n. o."]
  * **Häufigkeit** 1044x in den Bänden 2-4 und 6-8
* Text: **n. o.** perp. vicar.  
  Annotation: [Type: NonObstantien, Value: "n. o."]
  * **Häufigkeit** 243x nur in den Bänden 7+8
* Text: **n. o.** perp. s. c. vicar.  
  Annotation: [Type: NonObstantien, Value: "n. o."]
  * **Häufigkeit** 122x, nur in den Bänden 7-8
* Text: **n. o.** statut.  
  Annotation: [Type: NonObstantien, Value: "n. o."]
  * **Häufigkeit** 13x, nur in Band 3

---

#### Label: Datum

##### Beschreibung:
exakte oder ungefähre Datumsangaben

##### Standard Examples:

* Text: **9 apr. 1410**  
  Annotation: [Type: Datum, Value: "9 apr. 1410"]

---

#### Label: Fundstelle

##### Beschreibung:
Verweise auf Dokumente oder Handschriften.

##### Standard Examples:

* Text: **L 138 254v**  
  Annotation: [Type: Fundstelle, Value: "L 138 254v."]

---

## Unklare Fälle und Richtlinien zur Entscheidung

### Domic.
Im Abkürzungsverzeichnis des RG steht für domic. nur domicella/domicellus (Ritterfräulein, Stiftsdame; Knappe, Junker [kurialer Ehrentitel]), auch wenn man domicellarius (Domherr) erwarten würde.

### Doppeldeutige Begriffe
Manche Begriffe können in mehreren Kategorien fallen. Beispiel: „alt.“ kann für ein Objekt (Altar), als auch für ein kirchliches Amt (ein Altarist, also ein Priester, der Gottesdienste an diesem Altar abhält und dafür ein Einkommen erhält) stehen. Wir haben uns dazu entschieden, alt. als Objekt zu taggen. 
An dieser Stelle sollen weitere ambige Fälle gesammelt werden und unsere Entscheidungen festgehalten werden:
  - alt. = Objekt
  - par. eccl. = Institution
  - archidiac. = KirchlichesAmt
  - vic. = KirchlichesAmt

### Fit mentio
Fit mentio ("wird erwähnt") wird nicht getaggt.

### Klammern

Alle Angaben in Klammern, die eine Alternative darstellen, werden in den Tag ihres Bezugsausdruckes miteinbezogen, inkl. Klammern:  
- Henricus **de Gerpstede (Gherbstede)** -> Namenszusatz: de Gerpstede (Gherbstede)
- **Erhardus (Gerardus)** -> Vorname: Erhardus (Gerardus)
- **24 oct. 13 (20 sept. 1413)** -> Datum: 24 oct. 13 (20 sept. 1413)
- **056 148 (ASO 2 11).** -> Quelle: 056 148 (ASO 2 11).
- **Berpenick (Berporch)** -> Ort: Berpenick (Berporch)
Bei “frei stehenden” Angaben in Klammern werden die Klammern ignoriert.  
- (**33,33 fl.**) -> Geldsumme: 33,33 fl.
- (procur. mag. Bruno Boghel) -> Verwaltungsamt: procur.; Bildung: mag.; Vorname: Bruno; Namenszusatz: Boghel  

### Kombinationen aus mehreren Kategorien
Ein Eintrag, der mehrere Entitäten beschreibt, wird in entsprechende Einzelannotationen aufgeteilt.
  * Beispiel: Text: can. et preb. eccl. Sleswic.
    Annotation:
    - [Type: KirchlichesAmt, Value: "can. et preb."]
    - [Type: Institution, Value: "eccl."]
    - [Type: Diözese, Value: "Sleswic."]

### Lect.
Bei der Abkürzung "lect." gibt es (wenigstens für das RG 3) noch Klärungsbedarf, weil es selten für Lektor und häufiger für einen Vermerk zum Geschäftsgang (lectio) zu stehen scheint. Wenn lect. am Ende des Regests steht, dann wird es nicht ausgezeichnet.

### maior und minor prebenda / ecclesia
Bei Fällen wie „incorp. maioris preb. eccl.“, bei denen nicht immer gleich klar ist, ob sich das Adjektiv maior/minor auf die Präbende oder die Kirche bezieht, wird es grundsätzlich gemeinsam mit preb. mit dem Tag „KirchlichesAmt“ versehen (also nicht zu eccl. gezogen). 

### Ort vs. Diözese
- Steht nach der Angabe der Weihe (subdiac, diac., presb. , ep. etc.) der Name einer Stadt so muss diese als Diözese getaggt werden, weil Weihen auf Diözesen, nicht auf Städte erfolgen.
  - Beispiele: Henricus de Bocholdia al. d. Foet cler. Traiect.; ep. Vulterran. 
  - Achtung: Bei prepos. Plocen. wird Plocen. als Ort, nicht als Diözese, getaggt.
- Die Ortsbezeichnungen nach e.m. (extra muros = außerhalb der Mauern von) werden immer als Ort getaggt, z.B. e.m. Traiect.
- In Fällen wie “Prag. et Olumuc. dioc.” Ist davon auszugehen, dass das erste dioc. Weggefallen ist. Es werden also sowohl Prag. als auch Olumuc. als Diözesen getaggt.
- Wenn marchio (Markgraf) vor Brandenburg. steht, wird Brandenburg. als Verwaltungseinheit (nicht als Ort oder Diözese) getaggt.

### Präpositionen

Die Präposition *de* wird nur beim Label Namenszusatz und SozialerStand mitgetaggt: 
* Johannis **de Yselsteine** (de Yselsteine = Namenszusatz), Ghiselbertus de Lochorst **de nob. gen.** (de nob. gen. = SozialerStand)    
In allen anderen Fällen wird nur der relevante Hauptbegriff annotiert, nicht die Präposition:  
* **de eccl.** (eccl. = Institution), **de locis interdictis** (locis interdictis = Gnadenerweis) etc.  

Entsprechendes gilt für weitere Präpositionen wie post ob. etc.

### Fundstelle
Für jede Quelle wird je ein Tag „Fundstelle“ vergeben, z.B. *C 1 4* (Fundstelle), *Ind. 323 127.* (Fundstelle)
Aber: *047 40 et 40v.* wird als eine Fundstelle getaggt.

### Thematische- / Topik-Tags
Wir haben uns aus zeitökonomischen Gründen dazu entschieden, keine thematischen Tags zu vergeben (z.B. „Geburtsdefekt“ für def. nat., „Interdikt“ für locis interdictis, „Ehe“ für matrim. usw.). Allerdings sollen die Nutzer/innen der fertigen Anwendung explizit darauf hingewiesen werden, dass sie bestimmte Themen, wie gewohnt, über die entsprechenden RG-Abkürzungen abrufen können. 
Beispielanfrage (falsch): Gib mir alle Ehefälle aus dem RG aus.
Beispielanfrage (richtig): Gib mir alle matrim. Fälle aus dem RG aus.

### Titelkirchen
Da die Namen derjenigen Kirchen, die Kardinalbischöfen, -priestern und -diakonen mit ihrer Ernennung zum Kardinal verliehen wurden, eine Mischform zwischen den Tags „Institution“, „Ort“ und „Patrozinium“ darstellen und ihre Anzahl zugleich finit ist, haben wir uns für einen eigenen Tag „Titelkirche“ entschieden. Man erkennt sie v.a. daran, dass in ihrer Nähe im Regest ein Kardinal genannt wird (ep. card., presb. card., diac. card.). In diesen Fällen wird ausnahmsweise darauf verzichtet, zusätzlich das Patrozinium oder den Ort als solche gesondert zu taggen. Beispiele: 
- presb. card. **tit. s. Laurentii in Damaso**
- diac. card. (tit.) **s. Georgii ad Velum Aureum**
- ep. **Portuen.** card.

### Ungünstige Trennung von zwei oder mehreren Wörtern
Manchmal kommt es vor, dass zwei Wörter, die eigentlich gemeinsam getaggt werden sollten (m. incorp.; ep. card.), durch andere Wörter getrennt werden (m. (Sigismundo Rom. Et Vng. rege) incorp.; ep. Portuen. card.). Behelfsmäßig haben wir jetzt beide Teile einzeln mit dem Tag Incorporatio bzw. KirchlichesAmt versehen - eine Lösung dafür muss noch gefunden werden, damit die Zuordnung eindeutig und konsistent ist (z.B. Pfeilverbindungen in Inception, die anzeigen, dass zwei Wörter zusammen unter ein Tag gehören).(?)

### Unklare oder vage Ortsangaben
Begriffe wie „apud cur.“ (an der Kurie), „Noviforum“ (Neumarkt) und „castrum“ (Burg) werden als "OrtImplizit" erfasst.

### Zusätze
Die Tags AbsolutioZusatz, CassatioZusatz, DispensatioZusatz, FacultasZusatz, LicentiaZusatz und ProrogatioZusatz dienen der Kennzeichnung des jeweiligen Gnadeninhalts im Regest (Bsp. s. jeweils oben). Wir verfahren so, dass der gesamte Gnadeninhalt, der oft bis zur Datumsangabe reicht, getaggt wird, nicht nur einzelne Wörter, da dieses Vorgehen sich bei mehreren Annotatoren als fehleranfälliger erwiesen hat. Beispiele: 
- LicentiaZusatz: lic. **retin. scolast., can. et par. eccl. ad 5 an.** 24 iul. 1409; nicht nur: **retin.** oder **retin. scolast.**
- ProrogatioZusatz: cum prorog. **term. solut. ad 1 an. propter incertitudinem taxe** 14 dec. 1409; nicht nur: **term.** oder **term. solut.**

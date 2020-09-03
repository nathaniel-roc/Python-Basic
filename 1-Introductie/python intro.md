## Introductie Python: Over compilers, interpreters, binaries en source code,

Begrijpt een machine nu het programma dat je zojuist hebt ingetypt?

Het korte antwoord is: NEE

De code die jij intypt is vooral voor de programmeur. Deze source code
(broncode) is namelijk leesbaar voor jou als programmeur. De machine kan hier
nog niets mee.  
Want, zoals je weet, kan een computer alleen iets met binaire code, die bestaat
uit enen en nullen; zoiets als 01001101 (4D in hex, 77 in decimaal). Elke één of
nul staat voor één bit in de computer. Die kan aan staan (1) of uit (0). Tot op
de dag van vandaag worden bits gegroepeerd in bytes. 8 bits maken samen één
byte. 01001101 is dus een byte. In de begintijd van computers werden computers
binair geprogrammeerd, in hex. Voor 01001101 zou de programmeur dus “4D”
schrijven. Gelukkig doen we dat niet meer.

Al vrij snel bedacht men dat een programmeertaal die meer op Engels leek voor de
programmeur beter zou werken. Het maakt het programmeren makkelijker, maar ook
het vinden van fouten en het aanpassen en onderhouden van zo’n programma. En,
een hogere programmeertaal zou onafhankelijk van de machine zijn. Want of je nu
C programmeert voor een INTEL processor of een AMD, of een Apple A13 Bionic, of
een Snapdragon 865, etc., de programmeertaal verandert daar niet door. Da’s
prima voor de programmeur, maar er is dus iets nodig om van die geprogrammeerde
taal (de broncode, of source) naar iets te komen dat die specifieke machine
begrijpt. Daar hebben we dan weer extra programma’s voor: Hetzij een
interpreter, hetzij een compiler.

Even een klein stukje geschiedenis.  
De moeder van alle programmeertalen is FORTRAN, uit 1954. Nu zijn er meer dan
2000 programmeertalen, inclusief varianten. Op dit moment zijn onder de meest
gebruikte: C/C++, Visual

![](media/80bcb0ea4ac9e965e28dbe09bc5a866d.jpg)

Basic, Cobol, Java. Jullie zijn bekend met JavaScript en PHP en vanaf deze
module ook met Python. Veel programmeertalen zijn afgeleid van C. Voor iemand
die C kent, zijn ze dan ook heel herkenbaar. Python is één van de talen waarin
kenmerken van C herkenbaar zijn, zoals bovenstaand plaatje illustreert.

## Van Source naar object

Hoe kom je nu van een statement uit een programmeertaal naar die machinecode
(binary, of object) ? Daar zijn globaal twee manieren voor:

1.  Interpreteren met een Interpreter. Een Interpreter leest jouw statements en
    vertaalt ze tijdens de uitvoering van het sourceprogramma naar machinecode,
    regel voor regel. Dat werkt prima, al brengt het wat nadelen met zich mee.
    De uitvoering van zo’n programma is langzamer dan de uitvoering van een
    binary, simpelweg omdat de interpreter ook een proces in de computer is en
    dus om resources vraagt. Scripttalen, zoals Javascript, PHP en ook Python
    werken op deze manier. Er ontstaat dus geen binary (zoals een.exe file in
    Windows) van het programma.

2.  Compileren naar objectcode met een compiler. Een compiler vertaalt het hele
    programma naar machinecode. Hier ontstaat dus een binary. In Windows zijn
    dat de .exe type files. Vervolgens wordt die binary uitgevoerd. Zo’n
    gecompileerd programma draait sneller omdat het geen interpreter meer nodig
    heeft. Het programma is zelfstandig. Er is geen andere software meer nodig
    om het te draaien. Dit soort code kan gecompileerd zijn voor gebruik binnen
    een Operating System als Windows, maar kan ook gecompileerd zijn voor een
    “kale” machine, zoals een microcontroller, of voor een Android smartphone,
    of een I-Phone, of etc.  
    De compiler optimaliseert de code vaak ook al. C/C++ en C\# werken op die
    manier. Tenslotte is een .exe file veel minder makkelijk te veranderen
    (hacken) dan broncode. Nu begrijp je ook waarom “open source” zo belangrijk
    kan zijn. Iedereen kan dan ook bij de broncode, zien wat er gebeurt en
    eventueel de code aanpassen.

Programmeertalen bestaan al heel lang. Moderne programmeertalen lijken nog
steeds op hun voorgangers. Begin jaren ’90 werd object oriented programming
(OOP) geïntroduceerd. Dat was de laatste fundamentele verandering. (Wordt het
weer tijd voor iets nieuws?)

Python werkt met een interpreter. Dat is, zoals gezegd, een extra programma dat
jouw statements vertaalt naar machinetaal. De interpreter kun je ook interactief
gebruiken, bijna als een calculator. Dat gaan we zien in de modules.

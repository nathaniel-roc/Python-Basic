# PYTHON BASIC, Introductie

## Wat is Python?

Python is een programmeertaal die afgeleid is van C. Python code lijkt dan ook op C code. Maar er zijn natuurlijk verschillen. We gaan er in deze module uitgebreid op in.  
Python is een interpreted language. Dat wil zeggen dat er een programma draait; de interpreter, om jouw regels tekst te interpreteren en te vertalen naar machinetaal.  
Python is populair als je bedenkt dat het één van de meer dan 2000 programmeertalen is. Maar waarom?  
Python is open source en gratis. Dat helpt. Het draait op Windows, Linux, MacOs en Raspbian.
Laten we beginnen met de installatie van Python.
## Installatie
Ga naar * https://www.python.org/ en download de installer.  
Kies hier uit de lijst de "Windows x86-64 executable installer"
Dan zie je als download iets als: python-3.8.3.exe
(Op het moment van schrijven is de laatste versie 3.8.3. Dat kan natuurlijk een latere versie zijn wanneer jij dit leest)
Download en run.  
Kijk even naar deze video over de installatie  
* https://www.youtube.com/watch?v=UvcQlPZ8ecA  
TIP: Installeer Python inderdaad op een andere plek dan de installer standaard voorstelt.  
TIP: Vergeet niet de PATH variabele aan te vinken.

Open IDLE, want daarmee kun je snel zien of alles werkt.
Krijg je nu een nieuw venster met een versie boodschap en is de laatste regel een prompt?:  >>>  
Dan werkt IDLE naar behoren.  
Een tweede test: Open de opdrachtprompt (Command prompt) in Windows met CMD. Typ in dat venster: python --version  
Je ziet dan in dat venster het versienummer van python.  
We stellen hiermee vast dat ook Windows python weet te vinden. De PATH variabele klopt.

Je kunt nu heel snel vaststellen of je te maken hebt met een interpreter.
Typ eens een rekensommetje na de prompt. Iets als 23 * 782 [return].
Idle geeft op de volgende regel de uitkomst: Voor dit sommetje is dat: 17986.
Tot dusver heb je met integers gerekend.  
Python kent natuurlijk ook floats. Probeer maar eens: (319-99) * 5 / 11  
Het antwoord is: 100,0.  
Dit is een float, te herkennen aan de komma. (Maar **waarom** is het nu een float terwijl de uitkomst toch een geheel getal is? Denk eens na over het antwoord.)  
(Meer over datatypes in de volgende opdrachten)

## Syntax
De syntax van Python is heel herkenbaar.  
Python maakt gebruik van indentation om een codeblok te markeren.
Je kent deze blokjes code al: Wanneer je een loop maakt staat in zo'n blokje de code die uitgevoerd moet worden binnen de loop.  
Bijvoorbeeld (in pseudocode, de loopdefinitie kan bijvoorbeeld een `for` of een `while` zijn.)   
Loopdefinitie:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;statement    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;statement   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;statement  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ... etc ...  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;laaste statement  
Hier stopt de indentation, dat is dan het eind van de loop.  
Het eind van de loop wordt gegeven door het einde van de indentation.  
**Let ook op de ':' aan het regeleinde van de loop defenitie**  
Dit soort blokje code komen ook voor in condities, zoals `if` en  `else` of de code binnen een functie. Je doet ze net zo.  
Je gebruikt in python dus geen accolades, maar wel die dubbele punt.
Ben je al precies in het gebruik van indentatie in het schrijven van jouw code? Dan gaat dit automatisch goed.

## Bronnen  

Ga altijd eerst naar: *https://www.python.org/* hier staat de meest recente informatie over python. Als er wijzigingen zijn in de syntax, wordt deze site als eerste ge-update.
Vind je het hier niet? dan kun je naar: *https://realpython.com*  
of naar *https://www.w3schools.com/python/*
Dit zijn maar een paar van de bronnen die op het web te vinden zijn.

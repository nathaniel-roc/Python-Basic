# PYTHON-BASIC - Eindtaak

## Uren, minuten en seconden gaan voorbij.

## Uitleg
Het doel is hier een klok in beeld te brengen (op de console) die er uit ziet als uu:mm:ss (uren, minuten, seconden).  
Deze klok loopt ongeveer gelijk als je alles goed programmeert.  
Om deze klok in beeld te brengen, heb je een aantal elementen nodig van de taal.  

**Loops:**  
Er is een loop voor seconden, één voor minuten en één voor uren.
Zoals je weet zijn er 60 seconden in één minuut en 60 minuten in een uur. Tenslotte heeft een dag 24 uur.
De klok moet lopen van 00:00:00 tot 23:59:59. Daarna volgt er een nieuwe dag die weer begint op 00:00:00.

**Functions**  
Maak gebruik van een functie die de klok naar de console print in het juiste format: uu:mm:ss. Houd je **precies** aan dit format. Je zult de waarden van uren, minuten en seconden moeten doorgeven aan die functie als parameters.  

**Strings**  
Je zult er achter komen dat je daarvoor strings moet manipuleren zodanig dat je **precies** dit format krijgt. Dit kan niet anders dan met expliciete conversie van variabelen naar strings.  
Tip: Je zult strings aan elkaar moeten plakken (concatenation).  

**Time object**  
Je gebruikt maar één element uit deze library; `time.sleep(s)`  
Waarbij de waarde van s 1 is. Hiermee pauzeert de uitvoering van het programma ongeveer 1 seconde. (Al enig idee waar en waarom je dit moet doen? Probeer het dan eerst maar eens zonder ...) Om deze functie te kunnen gebruiken, moet je de time library importeren met
`import time`

## Leerdoelen

> 1. [ ] Ik kan met Python een functie aanspreken
> 2. [ ] Ik kan parameters doorgeven aan een functie
> 3. [ ] Ik kan loops gebruiken in PYTHON
> 4. [ ] Ik kan de uitvoering van een programma vertragen
> 5. [ ] Ik kan strings gebruiken om het juiste uitvoerformat te krijgen
> 6. [ ] Ik heb op correcte wijze een element uit de Python standaard library toegepast

## Opdracht

Het programma bevat alle bovenstaande elementen in een logisch consistent geheel. Het totale programma zal ongeveer 40 regels code groot zijn.  

De klok moet kunnen beginnen op een willekeurig tijdstip, zoals 27 minuten over 11 (ochtend of avond), kwart voor 8, etc. In andere woorden, je moet de klok kunnen initialiseren. Dit doe je door beginwaarden op te nemen in het programma. Het hoeft niet interactief met invoer van de gebruiker.

## Eindresultaat

Het programma schrijft achereenvolgens (één keer per seconde)
een string naar de console die er uit ziet als een klok. Het format moet precies uu:mm:ss zijn. Dus de output is dan:  
`00:00:01`  
`00:00:02`  
`00:00:03` enzovoort, tot:  
`23:59:59`  
Hierbij zorg je dat de volgorde van uren, minuten en seconden klopt:  
bij elke 60e seconde komt er één minuut bij: na 00:00:59 komt 00:01:00  
bij elke 60 minuten kom er één uur bij: na 00:59:59 komt 01:00:00  
na 24 uur begint de klok weer opnieuw: na 23:59:59 komt dan 00:00:00

## Bronnen

Een lijstje van links naar externe bronnen
> Bijvoorbeeld:  
>[W3 Schools - PHP Functions](https://www.w3schools.com/php/php_functions.asp)  
>[Jaap van der Veen - PHP Basiscursus Les3: Functies](https://phpbasis.jaapvdveen.nl/basiscursus-php/les-3-inleiding-functies/)  

# Hagrotooling

Met deze tool kunnen materiaaltabellen van een divers aantal vreemdtalige pdf's worden ingeladen.

Per 'vreemdtalige' pdf moet een structuur worden aangegeven. Bijvoorbeeld, de materiaaltabellen in pdf's van *Fabrikant X* hebben beginnen altijd met als eerste kolomnaam: "*Werkstoffnummer*".
Deze structuur kan worden ingesteld en opgeslagen voor toekomstig gebruik.

Door middel van de ingestelde structuur kan worden afgeleid welke tabellen deze tool moet opslaan. Het handmatig instellen van een bepaalde structuur is nodig, omdat de pdf's namelijk uit meerdere tabellen kunnen bestaan; Waaronder tabellen die helemaal niks te maken hebben met materialen. 

### Werkende Functionaliteiten:
- User interface met [PyQt5](https://pypi.org/project/PyQt5/)
- Selecteren van één of meer PDF bestanden
- Het inlezen van tabellen door middel van [Tabula](https://pypi.org/project/tabula-py/)


### Todo's:
- (PRIO) Het omzetten van de uitgelezen datastream naar een leesbaar formaat zoals JSON
- (PRIO) Het instellen en uitlezen van een configureerbare structuur per fabrikant voor de pdf's.
- Het converteren van kolomnamen naar een vooraf bepaalde naam (Zie hierboven)
- Opslaan van uitgelezen data in een NoSql database, zoals Mongo.

### Verbeterpunten:
- Het lezen van de pdf's op een andere Thread runnen zodat de applicatie niet freezed bij grote bestanden (bijvoorbeeld, een pdf van 300 pagina's).
- Het tonen van een laadbalk.
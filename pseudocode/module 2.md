>Module 2: Moderatie
Voordat een bericht ook daadwerkelijk op het stationshalscherm wordt gezet, wordt er door een moderator van de NS naar de berichten gekeken. De moderator kan een bericht goed- of afkeuren. Alleen goedgekeurde berichten worden gepubliceerd op het stationshalscherm van het desbetreffende station.

>Deze module leest de berichten uit het gestructureerde tekstbestand (zoals beschreven bij module 1) in, beginnend bij het oudste bericht. Na beoordeling door een moderator wordt het hele bericht (inclusief datum, tijd, naam en station) naar een database geschreven. Daarnaast wordt de volgende data toegevoegd:

>- of het bericht is goedgekeurd of afgekeurd;
>- de datum en tijd van beoordeling;
>- de naam van moderator die het bericht heeft beoordeeld;
>- het email-adres van de moderator.
>- Deze module werkt met een Command Line Interface (CLI).

>Daarnaast moet voor de werking van deze module een database worden gemaakt en gebruikt. Het ontwerp van deze database omvat een conceptueel, een logisch en een fysiek datamodel. De database moet vervolgens worden gerealiseerd in PostgreSQL. De gegevens worden gelezen uit het CSV bestand en aangevuld met de moderatorgegevens en daarna weggeschreven in de database. Het CSV-bestand wordt daarna leeggemaakt.




- de file openen
- de reviews uit de file lezen
- oudste uitzoeken
- als de revieuw is weggeschreven dan line verwijderen
- de file leegmaken


- vraag naar email moderator
- kijk of email bekend is en vraag de naam op
- als de naam niet bekend is vraag om naam
- sla data op naar de data base met id


- oudste ongemodereerde revieuw uit de file
- presenteer de review aan de moderator
- vraag om goedkeuring
- schrijf de goedkeuring naar de database met datum tijd en de details van moderator
- herhaal deze stappen
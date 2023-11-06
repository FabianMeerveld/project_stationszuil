
# Project stationszuil

Project vanuit de NS om makkelijker feedback te krijgen van klanten


Module 1:
- Zuil waar klanten van de NS feedback kunnen geven.

Module 2:
- Applicatie waar moderatoren de feedback kunnen goed of afkeuren.

Module 3:
- Applicatie om feedback, weer, tijd en faciliteiten van een station weer te geven.
## Deployment
Eerst moet de database aangemaakt worden:
- [database ddl](https://github.com/FabianMeerveld/project_stationszuil/blob/main/station-database.ddl)

de volgende packages moeten geinstalleerd worden:
- [psycopg2](https://www.psycopg.org/docs/)
- [pillow](https://pillow.readthedocs.io/en/stable/installation.html)

Om het feedback zuil te starten gebruik je het volgende command.

```
  python Module_1_Zuil.py
```
Om het moderatie zuil te starten gebruik je het volgende command.

```
  python Module_2_Moderatie.py
```
Om het stations zuil te starten gebruik je het volgende command.

```
  python Module_3_Scherm.py
```
vervolgens voer je een van de [stations](https://github.com/FabianMeerveld/project_stationszuil/blob/main/Stations.txt) uit de lijst in.
Sluiten kan door middel van alt+f4


## Authors

- [@fabianmeerveld](https://github.com/FabianMeerveld)


## Support

For support, email fabian.meerveld@student.hu.nl


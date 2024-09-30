## Kalendarz UWS 2024
Aplikacja na potrzeby rekrutacji na stanowisko Fullstack Developera

### Test aplikacji - konteneryzacja
Aby uruchomić aplikację należy na maszynie z zainstalowanym oprogramowaniem docker i docker compose wykonać następujące polecenie z poziomu katalogu zawierającego plik docker-compose.yml
```
docker compose up
```
lub dla maszyny z zainstalowanym jedynie dockerem
```
docker build -t moja_aplikacja . && docker run -d -p 8080:8080 moja_aplikacja
```
Następnie aplikacja powinna być dostępna w wyszukiwarce pod adresem
```
http://localhost:8080/
```

Aplikacja udostępnia:
| Link | Opis |
| --- | --- |
| / | widok główny  |
| /kalendarz?year=2024&month=9&day=23  | widok kalendarza miesięcznego  |
| /wydarzenie/5 | widok określonego wydarzenia |
| /filtruj/nauka | widok wydarzeń z określonym tagiem |

### Środowisko dla testów lokalnych
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 app.py
```

### Zapis pakietów
`
pip freeze > requirements.txt
`

### Instalacja pakietów
`
pip install -r requirements.txt
`



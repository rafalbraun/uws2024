## Kalendarz UWS 2024
Aplikacja na potrzeby rekrutacji na stanowisko Fullstack Developera

### Test aplikacji - konteneryzacja
Aby uruchomić aplikację należy na maszynie z zainstalowanym oprogramowaniem docker i docker compose wykonać następujące polecenie z poziomu katalogu zawierającego plik docker-compose.yml
```
docker compose up
```

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



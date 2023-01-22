program wymaga pliku typu .env przechowującego zmienne środowiskowe. Dlatego należy
utworzyć taki plik np. w folderze Scripts
podczas uruchamiania programu server.py w komendzie podaje się trzy argumenty:
pierwszy: ściężkę do pliku typu .env np './Scripts/.dane.logowania.env' (jeżeli plik znajduje się w podfolderze Scripts)
drugi: nazwę zmiennej środowiskowej przechowującej dane dotyczące loginu. np. LOGIN
trzeci: nazwę zmiennej środowiskowej przechowującej dane dotyczące hasła. np. HASLO
przed wywołaniem polecenia z tymi argumentami należy je uaktywnić w systemie/srodowisku
podajac w cmd komendy $env:LOGIN

Instrukcja jak postępować znajduje się w pliku korzystanieZeZmiennychSrodowiskowychPython.docx
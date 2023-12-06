Projekt Prestashop
------
Krótki opis
---
Projekt ma na celu utworzenie możliwie wiernej kopii wybranego sklepu elektronicznego w dwóch etapach: wdrożeniu lokalnym, wdrożeniu na chmurze. Obecnie kod źródłowy umożliwia lokalne uruchomienie sklepu
Wszystkie produkty zostają pobrane z bazowego sklepu za pomocą modułu Scrapper, a następnie wgrywane do sklepu. Sklep korzysta z samodzielnie podpisanego certyfikatu SSL i nie ma skonfigurowanych faktycznych połączeń z serwisami płatniczymi.

Skład zespołu
---
Zespół tworzony jest przez studentów:
- Mariia Kyrychenko
- Kanstantsin Kalenik
- Damian Niemczyk
- Maksim Huzino

Struktura projektu
---

Katalog Prestashop zawiera kod sklepu, skrypty do konfiguracji Apache i plik docker-compose.yml, służący do uruchamiania projektu.
Katalog mysql zawiera pliki bazy danych zawierające konfigurację sklepu i produkty.
Katalog Scrapper zawiera skrpty pobierające skrypty ze sklepu bazowego i przetwarzające je do plików gotowych do wgrywania do sklepu.

Uruchamianie
---
1. Wejść do katalogu Prestashop
2. Wykonać docker-compose up
3. Przejść na stronę https://localhost:8001

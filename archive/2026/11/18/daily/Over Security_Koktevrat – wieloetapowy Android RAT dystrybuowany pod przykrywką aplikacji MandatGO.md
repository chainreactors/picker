---
title: Koktevrat – wieloetapowy Android RAT dystrybuowany pod przykrywką aplikacji MandatGO
url: https://cert.orange.pl/aktualnosci/koktevrat-wieloetapowy-android-rat-dystrybuowany-pod-przykrywka-aplikacji-mandatgo/
source: Over Security
date: 2026-11-18
fetch_date: 2026-11-19T09:47:21.264281
---

# Koktevrat – wieloetapowy Android RAT dystrybuowany pod przykrywką aplikacji MandatGO

[![logo Orange](https://cert.orange.pl/wp-content/uploads/2025/11/orange-logo.svg)](https://www.orange.pl/)

[![logo Cert Orange Polska](https://cert.orange.pl/wp-content/uploads/2025/11/cert-logo.svg)](https://cert.orange.pl/)

[![Cybertarcza logo](https://cert.orange.pl/wp-content/uploads/2026/01/Cybertarcza6.svg)](https://cert.orange.pl/cybertarcza/)

* Na skróty![arrow-down](https://cert.orange.pl/wp-content/themes/cert/front/dist/assets/svg/arrow_down.svg)
  + [Ostrzeżenia](https://cert.orange.pl/ostrzezenia/)
  + [Cyber Threat Intelligence](https://cert.orange.pl/cyber-threat-intelligence/)
  + [Materiały filmowe](https://cert.orange.pl/materialy-filmowe/)
  + [Warto wiedzieć](https://cert.orange.pl/warto-wiedziec/)
  + [Dla eksperta](https://cert.orange.pl/tag/ekspert/)
  + [Raporty CERT Orange Polska](https://cert.orange.pl/raporty-cert-orange-polska/)
  + [Kontakt](https://cert.orange.pl/kontakt/)
* O nas![arrow-down](https://cert.orange.pl/wp-content/themes/cert/front/dist/assets/svg/arrow_down.svg)
  + [Czym jest CERT?](https://cert.orange.pl/czym-jest-cert/)
  + [Członkostwo w organizacjach](https://cert.orange.pl/organizacje-czlonkowskie/)
  + [Zgłoś podatność](https://cert.orange.pl/zglos-podatnosc/)
  + [Hall of Fame](https://cert.orange.pl/hall-of-fame/)
* Narzędzia![arrow-down](https://cert.orange.pl/wp-content/themes/cert/front/dist/assets/svg/arrow_down.svg)
  + [Hasło Alert](https://cert.orange.pl/hasloalert/)
  + [Mapa zagrożeń](https://cert.orange.pl/mapa-zagrozen/)
  + [Dane o zagrożeniach](https://cert.orange.pl/dane-o-zagrozeniach/)
  + [Mobile Sandbox](https://cert.orange.pl/mobile-sandbox/)
* [Zasady bezpieczeństwa](https://cert.orange.pl/antiphishing-info/)
* [Usługi](https://cert.orange.pl/uslugi/)
* [Sprawdź phishing](https://cert.orange.pl/sprawdz-phishing/)

**Zgłoś zagrożenie!**

[![avatar](https://cert.orange.pl/wp-content/themes/cert/front/dist/assets/svg/ic_Avatar.svg)](/login)

![hamburger](https://cert.orange.pl/wp-content/themes/cert/front/dist/assets/svg/hamburger.svg)![hamburger](data:image/svg+xml...) ![hamburger-close](https://cert.orange.pl/wp-content/themes/cert/front/dist/assets/svg/close.svg)![hamburger-close](data:image/svg+xml...)

Zgłoś incydent

![close](https://cert.orange.pl/wp-content/themes/cert/front/dist/assets/svg/delete.svg)

Typ zagrożenia Incydent Podatność Inny

Wybierz Oszustwa sieciowe (np. phishing) Ograniczenie dostępności i zasobów (DoS) Próby i włamania sieciowe Rozpowszechnianie złośliwych programów Nielegalne treści (np. spam) Inne

Wybierz Możliwość przepełnienia bufora Błąd wprowadzenia danych Błąd konfiguracji Inne

(jeśli zgłaszasz przypadek phishingu, zapisz mail (przesuń go z programu pocztowego na pulpit komputera lub wybierz opcję plik/zapisz jako), a następnie załącz)

Podejrzany SMS prześlij na nr 508 700 900

Jeśli zgłoszenie dotyczy bezpieczeństwa dzieci, zgłoś je również pod http://www.dyzurnet.pl

Wyszukiwarka

![close](https://cert.orange.pl/wp-content/themes/cert/front/dist/assets/svg/delete.svg)

[@CERT\_OPL](https://twitter.com/CERT_OPL)

[Tweety od CERT Orange Polska](https://twitter.com/CERT_OPL?ref_src=twsrc%5Etfw)

9 września 2026 12:57 · 8 minut czytania

(Aktualizacja: 9 września 2026 13:01)

# Koktevrat – wieloetapowy Android RAT dystrybuowany pod przykrywką aplikacji MandatGO

![](https://cert.orange.pl/wp-content/uploads/2026/09/koktevrat.webp)

[Zespół CERT Orange Polska](https://cert.orange.pl/author/team/)

[analiza](https://cert.orange.pl/tag/analiza/)   [ekspert](https://cert.orange.pl/tag/ekspert/)   [malware](https://cert.orange.pl/tag/malware/)

[Dodaj do ulubionych źródeł w Google](https://www.google.com/preferences/source?q=cert.orange.pl)

**Nieistniejąca aplikacja rządowa, reklama na Facebooku i obietnica prostego sposobu na opłacenie mandatu. Tak zaczyna się infekcja, której kolejne etapy prowadzą od zwykłego pliku APK do pełnoprawnego Android RAT-a. Analiza próbki pokazuje, że atakujący nie ograniczyli się do kradzieży danych. Malware zapewnia operatorowi szeroki zestaw funkcji pozwalających na zdalne pozyskiwanie informacji, wykonywanie działań na urządzeniu i utrzymywanie komunikacji z infrastrukturą C2.**

Analizowana próbka została pozyskana w ramach kampanii wykorzystującej aplikację **MandatGO**, przedstawianą użytkownikom jako narzędzie związane z obsługą mandatów.

![Reklama zachęcająca do zainstalowania aplikacji](https://cert.orange.pl/wp-content/uploads/2026/09/Koktevrat_1-643x1024.webp)

*Reklama zachęcająca do zainstalowania aplikacji*

Dystrybucja odbywała się za pośrednictwem reklamy na Facebooku, a użytkownik był kierowany do strony fb-market-play[.]cc, z której mógł pobrać plik APK. Aplikacja MandatGO okazała się pierwszym etapem wieloetapowego łańcucha prowadzącego do instalacji Android RAT-a.

![Fanpage na Facebooku dystrybuujący złośliwą aplikację koktevrat](https://cert.orange.pl/wp-content/uploads/2026/09/Koktevrat_2.webp)![Fanpage na Facebooku dystrybuujący złośliwą aplikację koktevrat](data:image/svg+xml...)

*Fanpage na Facebooku dystrybuujący złośliwą aplikację*

Na potrzeby analizy badaną rodzinę nazwaliśmy **koktevrat**. Nazwa pochodzi od ciągu koktevran\_channel, wykorzystywanego przez malware podczas tworzenia kanału powiadomień Androida. Nie znaleziono wystarczających przesłanek pozwalających przypisać próbkę do znanej rodziny malware.

Najważniejsze cechy koktevrat to: wieloetapowe ładowanie kodu, wykorzystanie Accessibility Service, komunikacja C2 wspierana przez Firebase Cloud Messaging (FCM) oraz szeroki zestaw poleceń umożliwiających operatorowi zdalną interakcję z urządzeniem.

## Stage 1. Dropper

Pierwszy APK prezentuje się jako aplikacja MandatGO, ale jego głównym zadaniem jest dostarczenie kolejnego komponentu. Manifest zawiera m.in. `REQUEST_INSTALL_PACKAGES`, a kod właściwej aplikacji jest częściowo ukryty przed analizą statyczną.

Dropper wykorzystuje dynamiczne ładowanie DEX oraz deszyfrowanie zasobów w czasie działania. Obfuskacja obejmuje również zakodowane ciągi znaków, refleksję Javy i pozorny kod utrudniający analizę. W jednym z mechanizmów wykorzystano XOR z trzybajtowym kluczem [32, 17, 46].

Po wykonaniu pierwszego etapu odszyfrowywany jest kolejny komponent – wudEMR.apk. Oznacza to, że APK dostarczony użytkownikowi nie zawiera wprost pełnej funkcjonalności RAT-a. Istotne elementy pojawiają się dopiero po wykonaniu droppera.

## Stage 2: właściwy Android RAT

Drugi komponent zachowuje tę samą nazwę i ikonę co MandatGO, ale jego funkcja jest już zupełnie inna. Pakiet `com.kowo.ciligeci` zawiera właściwą funkcjonalność koktevrat.

Podobnie jak w pierwszym etapie, kod został ukryty w zasobie `uoN.css`. Plik zawiera zaszyfrowany payload, który jest odszyfrowywany przy użyciu **RC4** z kluczem `iOZ`, a następnie dynamicznie ładowany. Zaciemnianie kodu zostało zastosowane na obu poziomach łańcucha infekcji.

Manifest Stage 2 wskazuje już bezpośrednio na charakter komponentu. Aplikacja posiada m.in. `READ_SMS`, `QUERY_ALL_PACKAGES`, `INTERNET` oraz `WAKE_LOCK`. Właściwe możliwości RAT-a wynikają jednak przede wszystkim z wykorzystania Accessibility Service.

Architektura drugiego etapu składa się z kilku usług działających w tle oraz odbiornika zdarzeń. Komunikacja i aktywacja funkcji są rozdzielone pomiędzy komponent C2 `JyfNnJyj` oraz usługę Accessibility `GtVyayDo`. Taki podział pozwala oddzielić odbieranie poleceń od ich wykonywania.

## Accessibility Service jako mechanizm wykonawczy

`GtVyayDo` stanowi jeden z najważniejszych komponentów koktevrat. Po uzyskaniu przez malware odpowiedniego uprawnienia może odbierać zdarzenia Androida oraz wykonywać operacje za pośrednictwem mechanizmów dostępności.

![Ekran włączający usługi dostępności (Accessibility Services).](https://cert.orange.pl/wp-content/uploads/2026/09/Koktevrat_3.webp)![Ekran włączający usługi dostępności (Accessibility Services).](data:image/svg+xml...)

*Ekran włączający usługi dostępności (Accessibility Services).*

Zakres ob...
---
title: Contrastata nuova campagna Vidar diffusa via PEC
url: https://cert-agid.gov.it/news/contrastata-nuova-campagna-vidar-diffusa-via-pec/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-22
fetch_date: 2025-10-06T18:05:21.436394
---

# Contrastata nuova campagna Vidar diffusa via PEC

* [Vai al contenuto](#main)
* [Vai alla navigazione del sito](#menu "accedi al menu")

[![Logo CERT-AGID](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-white.svg)](https://cert-agid.gov.it/)

# [CERT-AGID Computer Emergency Response Team AGID](https://cert-agid.gov.it/)

[Agenzia per
l'Italia Digitale](https://www.agid.gov.it)

[![Logo AgID - Agenzia per l'Italia Digitale](/wp-content/themes/cert-agid/assets/images/logo-agid.svg)](https://www.agid.gov.it)

Seguici su

* [RSS](https://cert-agid.gov.it/feed/ "RSS")
* [Telegram](https://t.me/certagid "Telegram")
* [X / Twitter](https://twitter.com/agidcert "X / Twitter")

cerca nel sito

[Menu](#menu "accedi al menu")

![Logo del CERT-PA](/wp-content/themes/cert-agid/assets/images/cert-agid-logo-black.svg)
CERT-AGID

<https://cert-agid.gov.it/>

## Menu di navigazione

* Documentazione
  + [Documenti AGID](https://cert-agid.gov.it/documenti-agid/)
  + [Pillole informative](https://cert-agid.gov.it/pillole-informative/)
  + [Flusso IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/)
* [Chi siamo](https://cert-agid.gov.it/chi-siamo/)
* [Contatti](https://cert-agid.gov.it/contatti/)
* [Strumenti](https://cert-agid.gov.it/strumenti/)
  + [hashr](https://cert-agid.gov.it/hashr/)
  + [Verifica HTTPS e CMS](https://cert-agid.gov.it/verifica-https-cms/)
  + [Statistiche sulle campagne italiane di malware e phishing](https://cert-agid.gov.it/statistiche/)
* [Glossario](https://cert-agid.gov.it/glossario/)
  + [0day](https://cert-agid.gov.it/glossario/0day/)
  + [Botnet](https://cert-agid.gov.it/glossario/botnet/)
  + [Data breach](https://cert-agid.gov.it/glossario/data-breach/)
  + [DDOS-DOS](https://cert-agid.gov.it/glossario/ddos-dos/)
  + [Deep-Dark web](https://cert-agid.gov.it/glossario/deep-dark-web/)
  + [Defacing](https://cert-agid.gov.it/glossario/defacing/)
  + [Exploit](https://cert-agid.gov.it/glossario/exploit/)
  + [MITM](https://cert-agid.gov.it/glossario/mitm/)
  + [OSINT-CLOSINT](https://cert-agid.gov.it/glossario/osint-closint/)
  + [Phishing](https://cert-agid.gov.it/glossario/phishing/)
  + [Privilege escalation](https://cert-agid.gov.it/glossario/privilege-escalation/)
  + [Spam](https://cert-agid.gov.it/glossario/spam/)
  + [Spoofing](https://cert-agid.gov.it/glossario/spoofing/)
  + [SQLi-SQL Injection](https://cert-agid.gov.it/glossario/sqli-sql-injection/)
  + [XSS](https://cert-agid.gov.it/glossario/xss/)
* Link utili
  + [Agenzia per l’Italia Digitale](https://www.agid.gov.it/)
  + [CSIRT Italia](https://csirt.gov.it)
  + [CERT-GARR](https://www.cert.garr.it/)
  + [CNAIPIC](https://www.commissariatodips.it/profilo/cnaipic/index.html)
  + [CERT-DIFESA](https://www.difesa.it/smd/cor/cert-difesa/25338.html)

* [Home](https://cert-agid.gov.it/)
* [Notizie](https://cert-agid.gov.it/category/news/)
* [Malware](https://cert-agid.gov.it/category/news/malware/)
* Contrastata nuova campagna Vidar diffusa via PEC

# Contrastata nuova campagna Vidar diffusa via PEC

21/08/2024

 [PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

![](https://cert-agid.gov.it/wp-content/uploads/2024/08/vidar_email.png)

A distanza di due settimane ritorna un’ondata di malspam tramite PEC mirata a diffondere il malware [Vidar](https://cert-agid.gov.it/tag/vidar/). Il nuovo modello di email sembra essere una risposta alla [comunicazione precedente](https://cert-agid.gov.it/news/ritorna-vidar-in-italia-con-una-campagna-di-malspam-tramite-pec/) e include un link che permette di scaricare un file JavaScript malevolo, solo dopo aver verificato lato backend che la richiesta provenga da un client Windows.

Le PEC inviate utilizzano sottodomini diversi dello stesso dominio. Grazie alla collaborazione con i Gestori PEC sono state identificate centinaia di URL di repository da cui si ottiene un file JavaScript con hash di volta in volta differente il cui deoffuscamento rimanda sempre alla stessa URL.

Al fine di velocizzare il processo di decodifica abbiamo predisposto uno script Python che risolve il file JavaScript tramite l’inserimento delle due righe di codice esadacimale `hex_qckwduarn` e `hex_iytmehmnkezyoqj`, le uniche variabili presenti nel codice JS.

`def gbyqqhnfbzucrwe(hex_string):
if not isinstance(hex_string, str):
raise ValueError('check input')
if len(hex_string) % 2 != 0:
raise ValueError('printing')
xxcnsnbrsjdynz = []
for i in range(0, len(hex_string), 2):
kutjzmolspwdm = hex_string[i:i+2]
raxhndodgjn = 0
for j in range(len(kutjzmolspwdm)):
raxhndodgjn <<= 4
wiuvbhshwuvaxub = kutjzmolspwdm[j]
if '0' <= wiuvbhshwuvaxub <= '9':
raxhndodgjn |= ord(wiuvbhshwuvaxub) - ord('0')
elif 'A' <= wiuvbhshwuvaxub <= 'F':
raxhndodgjn |= ord(wiuvbhshwuvaxub) - ord('A') + 10
elif 'a' <= wiuvbhshwuvaxub <= 'f':
raxhndodgjn |= ord(wiuvbhshwuvaxub) - ord('a') + 10
else:
raise ValueError('document ready')
xxcnsnbrsjdynz.append(raxhndodgjn)
return xxcnsnbrsjdynz
def xor_strings(qckwduarn, iytmehmnkezyoqj):
nvjmkwcdjxiydgjz = ''
for i in range(len(qckwduarn)):
nvjmkwcdjxiydgjz += chr(qckwduarn[i] ^ iytmehmnkezyoqj[i % len(iytmehmnkezyoqj)])
return nvjmkwcdjxiydgjz
# INSERIRE QUI LE STRINGHE ESADECIMALI
hex_qckwduarn = ''
hex_iytmehmnkezyoqj = ''
qckwduarn = gbyqqhnfbzucrwe(hex_qckwduarn)
iytmehmnkezyoqj = gbyqqhnfbzucrwe(hex_iytmehmnkezyoqj)
nvjmkwcdjxiydgjz = xor_strings(qckwduarn, iytmehmnkezyoqj)
print("Decodifica:")
print(nvjmkwcdjxiydgjz)
iheezmyxtsthutoe = [
'winmgmts:root\\cimv2:Win32_Process',
'less powershel',
'conhost --head',
nvjmkwcdjxiydgjz,
'time',
]
eddvxaxeqs = ''
array = iheezmyxtsthutoe
arrayLength = len(array)
dcmqzdmh = 0
for index in range(arrayLength):
if index >= 1898:
break
znlhotuowotfpa = array[1898 - index - 1] if 1898 - index - 1 < arrayLength else ''
qohziolvyweuizfz = array[1898 - index] if 1898 - index < arrayLength else ''
ueoicmlokwxmqh = array[1898 - index + 1] if 1898 - index + 1 < arrayLength else ''
dcmqzdmh = znlhotuowotfpa + qohziolvyweuizfz + ueoicmlokwxmqh
eddvxaxeqs = dcmqzdmh
print("Comandi da eseguire:")
print("Create:", iheezmyxtsthutoe[0])
print("Create:", iheezmyxtsthutoe[1])
print("Create:", eddvxaxeqs)`

L’output ottenuto contiene un array di numeri interi, in questo caso assegnati alla variabile `$avvlqzhpv` e il valore numerico da sottrarre (`8524`):

![](https://cert-agid.gov.it/wp-content/uploads/2024/08/vidar_js_decoded.png)

A questo punto la URL da cui ottenere il primo payload può essere facilmente risolta.

![](https://cert-agid.gov.it/wp-content/uploads/2024/08/vidar_array_decode.png)

Dalla nuova URL viene fornito un ulteriore JavaScript contenente il payload finale, che a sua volta rimanda a una nuova URL, anch’essa con dominio `.top`. Questa URL richiede un parametro `key` univoco per fornire l’eseguibile finale. Nel nostro caso, le chiavi recuperate erano già state utilizzate.

## Azioni di contrasto

Le attività di contrasto sono state già messe in atto con il supporto dei Gestori PEC che hanno provveduto a bloccare gli indirizzi coinvolti nell’invio delle mail malevole. Gli IoC relativi alla campagna sono stati diramati attraverso il [Feed IoC](https://cert-agid.gov.it/scarica-il-modulo-accreditamento-feed-ioc/) del CERT-AgID verso i Gestori PEC e verso le strutture accreditate.

Si invita a prestare sempre attenzione a questo genere di comunicazioni. Nel dubbio, è possibile inoltrare email ritenute sospette alla casella di posta **malware@cert-agid.gov.it**

## Indicatori di Compromissione

Al fine di rendere pubblici i dettagli della campagna odierna si riportano di seguito gli IoC rilevati:

**Link:** [Download IoC](https://cert-agid.gov.it/wp-content/uploads/2024/08/vidar_21-08-2024.json)

Taggato
[PEC](https://cert-agid.gov.it/tag/pec/)
[vidar](https://cert-agid.gov.it/tag/vidar/)

## Navigazione articoli

[Notizia precedente Cresce l’attività di Quasar RAT (BlotchyQuasar) contro gli utenti di istituti bancari italiani](https://cert-agid.gov.it/news/cresce-lattivita-di-quasar-rat-blotchyqua...
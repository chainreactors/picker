---
title: Ransomware “Cambiare Rotta”: Una minaccia distruttiva per l’Italia
url: https://cert-agid.gov.it/news/ransomware-cambiare-rotta-una-minaccia-distruttiva-per-litalia/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-25
fetch_date: 2025-10-06T17:19:22.969622
---

# Ransomware “Cambiare Rotta”: Una minaccia distruttiva per l’Italia

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
* Ransomware “Cambiare Rotta”: Una minaccia distruttiva per l’Italia

# Ransomware “Cambiare Rotta”: Una minaccia distruttiva per l’Italia

24/05/2024

 [cambiare rotta](https://cert-agid.gov.it/tag/cambiare-rotta/)

È risaputo che esiste un generatore di ransomware Chaos basato su GUI, che consente di personalizzare facilmente un ransomware attraverso una serie di opzioni. Il [recente campione](https://blog.sonicwall.com/en-us/2024/05/politically-charged-ransomware-weaponized-as-a-file-destroyer/) scoperto da SonicWall, per il quale non ha fornito alcun IoC, sembra essere stato creato utilizzando proprio questo builder. **Purtroppo, non è ancora chiaro come il malware venga distribuito sui computer delle vittime.**

L’eseguibile, di cui il CERT-AGID è venuto in possesso grazie alle ricerche di [MalwareHunterTeam](https://x.com/malwrhunterteam/status/1793901712975229279), è un file .NET quasi identico agli altri campioni di Chaos Ransomware.

All’avvio, il malware **verifica se è già in esecuzione** (*AlreadyRunning*). In caso contrario, avvia la scansione dei file per crittografarli (*lookForDirectories*). Fondamentalmente, il malware esegue una scansione di tutte le unità del sistema, ad eccezione dell’unità C:, dove individua specifiche directory che possono essere ricorsivamente crittografate (*encryptDirectory*) senza compromettere il sistema operativo. Se l’unità individuata è diversa da C:, viene crittografato l’intero contenuto dell’unità.

![](https://cert-agid.gov.it/wp-content/uploads/2024/05/lookForDirectories.png)

Nel metodo *encryptDirectory* è presente un’eccezione: viene effettuata una verifica sulle dimensioni del file, se è maggiore o uguale a 2.117.152 byte il file verrà sovrascritto con byte casuali senza possibilità di recupero, se è inferiore viene invocato il metodo *EncryptFile*.

![](https://cert-agid.gov.it/wp-content/uploads/2024/05/EncryptFile.png)

Il metodo *EncryptFile* sopra riportato riceve il percorso di un file come input, verifica che l’estensione rientri in una delle [229 ritenute valide](https://cert-agid.gov.it/wp-content/uploads/2024/05/229_validExtensions.txt), e lo cripta utilizzando l’algoritmo AES.

In sintesi, il processo comprende i seguenti passaggi:

* Legge tutti i byte dal file specificato e li memorizza in un array di byte (*bytesToBeEncrypted*).
* Genera una **password casuale di lunghezza 20 caratteri** utilizzando il metodo *CreatePassword* e la converte in una sequenza di byte utilizzando la codifica UTF-8.
* Cifra l’array di byte *bytesToBeEncrypted* utilizzando **l’algoritmo AES** con la password generata precedentemente, ottenendo un nuovo array di byte cifrati (*inArray*).
* Salva la **password criptata RSA** e i dati criptati nel file originale. La password criptata viene generata tramite la funzione *RSAEncrypt*, utilizzando la **chiave pubblica RSA integrata**. I dati cifrati vengono convertiti in una stringa Base64.
* Il file originale viene quindi rinominato aggiungendo **un’estensione casuale di 4 caratteri**.

In breve, *EncryptFile* crifra un file utilizzando l’algoritmo AES e protegge la password AES cifrandola con l’algoritmo RSA.

In linea generale, l’entrypoint elenca tutte le funzionalità eseguite sin dall’avvio, ciascuna descritta in modo mnemonico.

![](https://cert-agid.gov.it/wp-content/uploads/2024/05/main.png)

È interessante notare che il malware **verifica se viene eseguito con privilegi di amministratore** tramite la funzione *checkAdminPrivilage*. In caso affermativo esegue le seguenti operazioni:

* Effettua un tentativo di eliminare le copie shadow mediante la funzione *deleteShadowCopies*.
* Se fattibile, disabilita la modalità di ripristino del sistema tramite la funzione *disableRecoveryMode*.
* Prova a rimuovere il catalogo di backup utilizzando la funzione *deleteBackupCatalog*.

In conclusione, i file cifrati non possono essere recuperati in quanto la nota di riscatto non fornisce alcuna istruzione su come contattare i criminali (gli unici in possesso della chiave privata) o su come procedere per il recupero dei file, anzi, indicano che “***non c’è modo di recuperarli***“.

`private static string[] messages = new string[]
{
"----------------------------------------------------CAMBIARE ROTTA RANSOMWARE",
"",
"L'ITALIA DEV'ESSERE PUNITA PER LA SUA ALLEANZA CON LO STATO FASCISTA",
"DI ISRAELE, QUESTO MALWARE E' STATO PROGRAMMATO DA MARXISTI-LENINISTI-MAOISTI",
"PER DIFFONDERE IL PENSIERO ANTISIONISTA. DEI PALESTINESI STANNO MORENDO PER",
"LE TUE AZIONI, IO UCCIDERO' I TUOI FILE. NON C'E' MODO DI RECUPERARLI. ",
"",
"",
"PALESTINA LIBERA",
"ITALIA UNITA ROSSA E SOCIALISTA",
""
};`

La nota, scritta in lingua italiana, associa il ransomware a un messaggio politico, con riferimenti al conflitto tra Israele e Palestina. Questo dimostra che il ransomware non è stato creato con l’intento di ottenere profitto finanziario, ma per essere distruttivo e per promuovere una determinata azione politica o ideologica.

![](https://cert-agid.gov.it/wp-content/uploads/2024/05/wallpaper.jpg)

Dopo aver completato il processo di cifra...
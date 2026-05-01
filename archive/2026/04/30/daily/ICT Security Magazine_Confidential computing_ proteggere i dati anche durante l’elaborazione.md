---
title: Confidential computing: proteggere i dati anche durante l’elaborazione
url: https://www.ictsecuritymagazine.com/articoli/confidential-computing/
source: ICT Security Magazine
date: 2026-04-30
fetch_date: 2026-05-01T05:39:59.637124
---

# Confidential computing: proteggere i dati anche durante l’elaborazione

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

* [Home](https://www.ictsecuritymagazine.com/)
* [Articoli](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* RubricheEspandi
  + [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Cyber Crime Conference 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyber-Crime-Conference-2026-1920x278-2.jpg)](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026)

![confidential computing](https://www.ictsecuritymagazine.com/wp-content/uploads/confidential-computing.jpeg)

# Confidential computing: proteggere i dati anche durante l’elaborazione

A cura di:[Redazione](#molongui-disabled-link)  Ore 30 Aprile 202620 Aprile 2026

Intel SGX, AMD SEV, ARM CCA: le architetture di *Trusted Execution Environment* ridefiniscono il perimetro della sicurezza, estendendo la protezione crittografica ai dati in uso. Ma il campo di battaglia è più insidioso del previsto.

## Il problema che nessuno voleva affrontare

Per decenni, l’industria della sicurezza informatica ha operato con una convenzione implicita e scomoda: i dati si possono proteggere a riposo, su disco, con la crittografia dei volumi; si possono proteggere in transito, sulle reti, con TLS e i suoi successori. Ma nel momento in cui un processore li elabora, quella protezione deve cedere. La CPU deve vedere il testo in chiaro. L’hypervisor può accedere alla memoria del *guest*. L’amministratore del *cloud provider* ha, almeno in teoria, accesso a tutto.

Questa è stata a lungo una verità accettata come ineluttabile, quasi una legge fisica della computazione. Il **Confidential Computing** nasce dal rifiuto di questa rassegnazione.

L’idea di fondo è tanto radicale quanto semplice: estendere la crittografia all’intero ciclo di vita del dato, incluso il momento del suo utilizzo. Non più una protezione che si interrompe all’ingresso della CPU, ma una garanzia *end-to-end* che include l’elaborazione stessa. Il meccanismo attraverso cui questa promessa si realizza è il **Trusted Execution Environment** (TEE): un’enclave *hardware* isolata, protetta da chiavi crittografiche generate e custodite dal processore stesso, inaccessibile anche al sistema operativo, all’hypervisor e, in linea di principio, persino al fornitore del servizio *cloud*.

L’industria ha cominciato a prendere sul serio questa tecnologia. Nel suo rapporto sui [*Top Strategic Technology Trends for 2026*](https://www.gartner.com/en/newsroom/press-releases/2025-10-20-gartner-identifies-the-top-strategic-technology-trends-for-2026), presentato il 20 ottobre 2025 al Gartner IT Symposium, Gartner ha inserito il Confidential Computing tra le tre tecnologie “Architect” fondamentali per l’infrastruttura *enterprise* nei prossimi cinque anni, stimando che entro il 2029 oltre il 75% delle operazioni elaborate in infrastrutture non fidate sarà protetta in uso dal Confidential Computing. Poco prima, a novembre 2025, la [ricerca IDC commissionata dal CCC](https://confidentialcomputing.io/wp-content/uploads/sites/10/2025/11/US53866125.pdf) aveva mappato un’adozione in forte crescita trasversale a settori regolamentati come finanza, sanità e pubblica amministrazione.

Un ulteriore segnale di maturità viene dal [report di Cyberus Technology](https://cyberus-technology.de/en/articles/confidential-computing-report/), pubblicato ad aprile 2026 sulla base di interviste con oltre venti organizzazioni partner: le proiezioni di mercato convergono su un CAGR di almeno il 25%, con stime più aggressive che raggiungono il 56-63%.

Ma tra la promessa e la realtà, il percorso è lastricato di sfide architetturali, vulnerabilità emerse e compromessi che chiunque voglia implementare queste soluzioni deve comprendere con lucidità.

## Il trilemma della sicurezza moderna: *at rest*, *in transit*, *in use*

La protezione delle informazioni si articola tradizionalmente intorno a tre stati del dato. ***At rest***: quando risiede su un supporto di memorizzazione. ***In transit***: quando attraversa una rete. ***In use***: quando viene elaborato da una CPU.

I primi due stati hanno trovato soluzioni mature e ampiamente adottate. La crittografia dei dischi con standard come AES-256 e i protocolli di trasporto sicuro come TLS 1.3 sono oggi presupposti fondamentali di qualsiasi architettura degna di questo nome. Il terzo stato, il dato *in use*, è rimasto il tallone d’Achille.

Il problema non è banale. Un processore non può operare su dati cifrati (almeno non con le tecniche crittografiche classiche): deve decifrarli, caricarli in memoria, accedervi. In quel frangente, chiunque abbia accesso privilegiato al sistema, un hypervisor compromesso, un amministratore malevolo, un attaccante con accesso fisico ai moduli RAM, può in linea di principio leggere quei dati.

Nei contesti *cloud* multi-*tenant*, questo non è un rischio astratto. Un’azienda farmaceutica che esegue carichi di lavoro sensibili su un *cloud provider* condiviso deve fidarsi non solo del proprio codice, ma dell’intero *stack software* del *provider*, hypervisor, *firmware*, sistema operativo *host* e di tutti i suoi dipendenti con accesso privilegiato. La **base di fiducia** (*Trusted Computing Base*, TCB) è straordinariamente ampia.

Il Confidential Computing riduce questa TCB al minimo indispensabile: il processore stesso e il suo *firmware* di sicurezza. Tutto il resto, incluso il *cloud provider*, viene escluso dal perimetro di fiducia.

## L’architettura delle enclave: Intel, AMD, ARM

Le tre famiglie di implementazione oggi disponibili, **Intel SGX/TDX**, **AMD SEV-SNP** e **ARM CCA**, condividono l’obiettivo ma differiscono profondamente nell’approccio architetturale. Comprendere qu...
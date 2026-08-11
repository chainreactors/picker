---
title: Firma elettronica qualificata esposta: le falle dell’eID belga e il perimetro che eIDAS non copre
url: https://www.ictsecuritymagazine.com/digital-id-security/firma-elettronica-qualificata-esposta-le-falle-delleid-belga-e-il-perimetro-che-eidas-non-copre/
source: ICT Security Magazine
date: 2026-08-10
fetch_date: 2026-08-11T03:31:47.516609
---

# Firma elettronica qualificata esposta: le falle dell’eID belga e il perimetro che eIDAS non copre

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
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Firma elettronica qualificata esposta le falle del eID belga e il perimetro che eIDAS](https://www.ictsecuritymagazine.com/wp-content/uploads/Firma-elettronica-qualificata-esposta-le-falle-del-eID-belga-e-il-perimetro-che-eIDAS.png)

# Firma elettronica qualificata esposta: le falle dell’eID belga e il perimetro che eIDAS non copre

A cura di:[Redazione](#molongui-disabled-link)  Ore 10 Agosto 202610 Agosto 2026

La firma elettronica qualificata belga è rimasta esposta per mesi a causa di un’estensione browser con oltre due milioni di utenti, sviluppata da una società iscritta nella Trusted List europea come prestatore qualificato. Qualsiasi sito web poteva leggere i dati della carta d’identità elettronica dell’utente quando inserita nel lettore, indurlo a digitare il PIN in una finestra dal testo controllato dall’attaccante per poi ricavarlo in chiaro, e, sulle installazioni Windows, eseguire codice sulla sua macchina anche senza carta inserita. Le vulnerabilità, ora corrette, sono state presentate al DEF CON e mettono in discussione non tanto la qualificazione eIDAS in sé, quanto l’ampiezza del perimetro che essa certifica.

## Che cosa è successo

Il software che fa da ponte fra il browser e la carta d’identità belga, e che produce con essa firme elettroniche qualificate, si è rivelato pilotabile da qualunque pagina web. Il gruppo di ricerca di Bay Area Labs, società fondata da James Arnott, ha reso pubblici il 7 agosto 2026, in concomitanza con l’intervento al DEF CON di Las Vegas, i dettagli tecnici di una serie di vulnerabilità nel sistema di firma Connective, sviluppato dall’omonima società belga e oggi in capo a Nitro Software Belgium, nell’[analisi tecnica originale](https://amibeingpwned.com/blog/8-in-10-banks-in-belgium).

Il sistema si compone di due elementi: un’estensione per browser, distribuita per i principali browser (Chrome, Edge, Firefox e Safari), e un componente nativo installato sul sistema operativo, disponibile per Windows e macOS, che dialoga direttamente con i lettori di *smart card* collegati alla macchina. L’estensione funge da semplice canale di inoltro fra le pagine web e il componente nativo, che a sua volta esegue le operazioni sulla carta: lettura dei dati, verifica del PIN, calcolo della firma.

Sulla diffusione conviene essere precisi, perché il dato circola in forma imprecisa. I ricercatori parlano di oltre due milioni di utenti attivi settimanali, cifra che dichiarano di avere verificato direttamente sulle schede pubbliche dell’estensione, le sole due che espongono un conteggio: Chrome Web Store e vetrina Edge. Il dato ricorrente di otto delle dieci maggiori banche belghe e oltre sessanta amministrazioni pubbliche compare invece, con questa esatta formulazione, nel [comunicato del 10 novembre 2021](https://www.businesswire.com/news/home/20211110005417/en/Nitro-to-Acquire-European-eSign-Leader-Connective) con cui Nitro annunciò l’acquisizione di Connective, dove si riferisce alla base clienti complessiva della società in Europa, oltre mille clienti fra *mid-market*, imprese e amministrazioni, non specificamente all’estensione. Il gruppo di ricerca lo riprende dichiarando espressamente di non poterne verificare l’estensione al componente vulnerabile.

Una precisazione di trasparenza, dichiarata dagli stessi autori: la ricerca è nata come banco di prova di una piattaforma commerciale di analisi automatizzata delle estensioni e dei relativi componenti nativi, che la società offre sul mercato.

## L’errore di progettazione: nessuna nozione di origine

Il difetto strutturale è tanto elementare quanto devastante. L’estensione non trasmetteva al componente nativo l’origine della richiesta, cioè il dominio della pagina che stava chiedendo un’operazione. Il programma installato sul computer, in altre parole, non aveva alcun modo di sapere con quale sito stesse parlando.

Esisteva formalmente un meccanismo di autorizzazione: un token di attivazione firmato con RSA a 2048 bit, rilasciato ai siti partner per abilitare l’uso del sistema sulla macchina dell’utente. Decodificandolo, i ricercatori hanno però constatato che il token conteneva soltanto un identificativo privo di funzione osservabile, una scadenza e una maschera di bit relativa alle operazioni abilitate. Nessun vincolo all’origine. Un token ottenuto da un servizio legittimo poteva quindi essere riutilizzato da qualunque altra pagina, *iframe* o annuncio pubblicitario, ottenendo lo stesso livello di accesso. I ricercatori riferiscono di averli reperiti da Doccle, la piattaforma documentale usata in Belgio per la ricezione di fatture e documenti, con tutte le operazioni abilitate e validità di ventiquattro ore.

Da qui discende la prima conseguenza: qualsiasi sito, o qualsiasi frame incorporato in un sito, poteva leggere silenziosamente i dati della carta d’identità elettronica e della carta di pagamento Maestro, storicamente co-marchiata Bancontact in Belgio, inserite nel lettore, senza consenso né consapevolezza dell’utente. Va ricordato che dal 1° luglio 2023 in Europa non vengono più emesse nuove carte Maestro, sostituite alla scadenza da Debit Mastercard o Visa Debit: le carte con quel circuito ancora in ci...
---
title: Weekly update #1
url: https://roccosicilia.com/2024/05/03/weekly-update-1/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-04
fetch_date: 2025-10-06T17:17:04.834891
---

# Weekly update #1

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [ita](https://roccosicilia.com/category/ita/), [update](https://roccosicilia.com/category/update/)

## [Weekly update #1](https://roccosicilia.com/2024/05/03/weekly-update-1/)

Published by

Rocco Sicilia

on

[3 Maggio 2024](https://roccosicilia.com/2024/05/03/weekly-update-1/)

[![Weekly update #1](https://roccosicilia.com/wp-content/uploads/2025/01/3c19b2cf-60f6-4770-93c9-291f5131b8db.webp?w=1024)](https://roccosicilia.com/2024/05/03/weekly-update-1/)

Il mio progetto di divulgazione è in una fase di consolidamento tra live, articoli, video e documentazione. Ho sentito l’esigenza di un recap settimanale in forma blog post (che per gli abbonati diventa diventa una sorta di newsletter) in cui condividere gli argomenti trattati durante la settimana e per questo motivo ho scelto come giorno di uscita il venerdì.

Se non sei iscritto al blog lo puoi fare da qui per ricevere una notifica via email:

Digita la tua e-mail…

Iscriviti

---

## Studio e lab

Come ho scritto in diverse occasioni ho terminato in questi giorni un ripassone generale sul mondo Web Application Penetration Testing e nelle ultime settimane ho dedicato più sessioni di studio in live tra piccole challenge e lab. Qualche giorno fa durante una sessione di studio in live ci siamo divertiti con una piccola sfida su una command injection (blind) di cui ho condiviso la registrazione su *Patreon*\*\*: [https://www.patreon.com/posts/…](https://www.patreon.com/posts/command-root-me-103518048?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link)

\*\* Le live su [Twitch](https://twitch.tv/roccosicilia) le trasmetto sempre pubblicamente, l’archivio “storico” è riservato ai sostenitori.

Ho inoltre raccolto una serie di appunti su diversi temi relativi ai test di sicurezza di una WebApp che sto arricchendo quasi quotidianamente. Ho condiviso integralmente la pagina Notion con le mie note: <https://roccosicilia.notion.site/Web-App-Security-c8d39198f6c5418d999e6b4720fbb96e>

Con una struttura simile sto sistemando anche gli appunti sulla parte Information Gathering di cui sempre [su Patreon è già disponibile un post](https://www.patreon.com/posts/passive-103143729) di approfondimento mentre la pagina Notion è un work-in-progress che conto di chiudere nei prossimi giorni: <https://roccosicilia.notion.site/Information-Gathering-99da28ac4b5e48798a8089b96f37c2e4>

## Prossimi eventi (CTF e conferenze)

Un paio di date da segnare:

* il 7 maggio alle 18:00 evento [Live sul mio canale Twitch](https://twitch.tv/roccosicilia) con gli organizzatori della CTF Wastelands
* il 21 maggio sarò a Milano per il Google Cloud Security Forum
* il 22 maggio sarò a Bolzano per lavoro e vorrei organizzare una serata cyber con chi è in zona

## Riflessione

Da qualche tempo, quando mi capita di discutere di politiche di sicurezza, ho iniziato a far presente che in alcuni casi il piano di Disaster Recovery (che di per se è già un argomento complesso) dovrebbe poter essere attuabile anche in caso di attacco informatico. Ne discuto frequentemente (poche ore fa l’ennesimo confronto) e in molte occasioni noto un forte interesse per il tema, considerando che avere un piano B pronto a scattare in caso di attacco è un concetto che piace, seguito da un certo sconforto nel constatare che ci sono adeguamenti da fare per rendere attuabile una politica di DR anche in uno scenario di attacco.

Dalle discussioni fatte ho notato che in scenari molto specifici in cui il problema è l’indisponibilità di una o più risorse, come gli attacchi ransomware causati da un malware ad opera di un dipendete incauto e alcune tipologie di DoS, i piani di DR in essere posso effettivamente dare respiro all’azienda vittima. Se le infrastrutture (quella primaria e quella di DR) sono state opportunamente disegnate e mantenute isolate e la comunicazione è limitata ai task di sincronizzazione dei dati, accendere i servizi nel sito secondario potrebbe effettivamente consentire una ripartenza in sicurezza partendo dall’ultima versione dei sistemi considerata non compromessa, ovviamente se si ha modo di poter stabilire con un certo livello di confidenza quale versione dei sistemi è utilizzabile.

Negli scenari in cui la compromissione è più profonda potrebbe non essere così utile il sito di DR. Esattamente come avviene per i sistemi di Backup, se l’attacker dispone di credenziali valide ed ha guadagnato una posizione all’interno della rete potrebbe compromettere o distruggere i dati replicati. Mentre per i sistemi di Backup una certa “vicinanza” ai sistemi di produzione è quasi scontata (anche se oggi l’infrastruttura di Backup potrebbe lavorare completamente “out-of-band” rispetto alla produzione) il disegno dell’infrastruttura di DR potrebbe prevedere un sito secondario completamente separato senza elementi di gestione o di supporto in comune con il sito primario. Questa netta separazione renderebbe difficile la vita ad un attacker intenzionato a muoversi verso il sito di DR per completare la compromissione.

A parole potrebbe sembrare tutto molto lineare ma ci sono diversi compromessi da considerare. Un esempio tipico: i sistemi Active Directory. In molte infrastruttura di DR viene tenuto attivo e sincronizzato un Domain Controller per non doversi occupare di un fastidioso recovery di un AD in caso di disastro. Dal punto di vista di RTO e RPO la scelta tecnica non fa una piaga (suggerita io stesso in diverse occasioni), ma a livello di sicurezza c’è un problema bello grosso: addio isolamento per un servizio quasi certamente critico. Ovviamente anche in questo caso possiamo attuare delle misure ulteriori come il backup del Domain Controller attivo sul sito di DR mantenuto off-line rispetto ai due siti Datacenter, cosa che significa avere una infrastruttura di backup anche sul sito di DR. Personalmente la ritengo una buona idea a prescindere perché consentirebbe di disporre di una protezione a livello backup anche nel periodo dì utilizzo del DR, ma noto che questa precauzione non è sempre adottata.

É evidente, a mio modo di vedere, che il piano di DR sia una risorsa anche in caso di attacco informatico, ma è altrettanto evidente che politiche e procedure vanno riviste a fronte di nuovi scenari probabilmente non discussi durante la realizzazione del “tradizionale” piano. Mi segno il tema come punto di approfondimento per una prossima puntata [podcast](https://www.youtube.com/playlist?list=PLd07cyWwjCpEQaAjuZ3iHI3SAvZlgrJz_).

---

Fine degli update per questa settimana, approfitto per ricordare l’esistenza del canale [Telegram](https://t.me/%2Ba7sF3JQV4bMzY2Nk) dove discutiamo di diverte tematiche legate al mondo IT ed Info. Sec. ed il [server Discord](https://discord.gg/Ys5AAbsyyH) dove i più tecnici si cimentano in labs e challenge sul fronte *offensive*.

Buon week-end!

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2024/05/03/weekly-update-1/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2024/05/03/weekly-update-1/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2024/05/03/weekly-update-1/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2024/05/03/weekly-update-1/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo sp...
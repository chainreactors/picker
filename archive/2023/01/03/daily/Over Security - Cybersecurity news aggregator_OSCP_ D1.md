---
title: OSCP: D1
url: https://roccosicilia.com/2023/01/02/oscp-d1/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-03
fetch_date: 2025-10-04T02:55:45.639712
---

# OSCP: D1

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [OSCP-D1](https://roccosicilia.com/2023/01/02/oscp-d1/)

Published by

Rocco Sicilia

on

[2 gennaio 2023](https://roccosicilia.com/2023/01/02/oscp-d1/)

Era uno degli obiettivi 2022 che, per vari motivi, non ho potuto mantenere in roadmap (a malapena ho iniziato a studiare il materiale per la preparazione). Quest’anno ci sono un bel po’ di cambiamenti in corso ed ho quindi pensato di rimettere in programma questo mio traguardo personale.

Ho abbozzato un programma leggero per i prossimi sei mesi in cui vorrei seguire il materiale presentato nel super PDF che fa parte del materiale di studio (che avevo già ottenuto ad inizio 2022) “Penetration Testing with Kali Linux” e su questa base valutare qualche approfondimento. Vorrei inoltre che questo percorso sia utile anche a chi mi legge o mi segue sui vari social, troverete quindi diversi articoli su questo blog con la sintesi dei progressi, qualche live su Twitch ed una repository sul mio GitHub: <https://github.com/roccosicilia/OSCP_sj>.

Leggendo il primo capito del PDF dove viene presentato il percorso ci viene subito ricordato a chi è rivolta questa certificazione. Si fa riferimento a figure come System Administrator e Network Administrator, a ricordarci che l’ambito del Penetration Testing non è un punto di inizio ma parte di un percorso che inizia prima e che richiede di aver maturato una certa esperienza nella gestione dei sistemi e delle reti. Questo non significa che se non si ha esperienza nei ruoli citati sia impossibile seguire il programma ma sicuramente sarà necessario apprendere delle nozioni senza comprenderle appieno.

Tra le prime note tecniche viene presentato il modello base di un Penetration Test con le sue fasi:

* Raccolta delle informazioni: più informazioni si ottengono più è probabile che l’attacco vada a buon fine;
* Enumerazione dei servizi;
* Primo accesso (es: Exploiting): una volta ottenuto il primo accesso viene solitamente condotta una nuova esplorazione dall’interno del sistema in modo di avere informazioni più dettagliate sul contesto e valutare quindi le successive mosse in modo appropriato;
* Mantenere l’accesso: il metodo utilizzato nel primo accesso potrebbe non essere comodo da riutilizzare, viene quindi utilizzato un metodo alternativo per mantenere la comunicazione con i sistemi compromessi;
* Attività post-attacco;

E’ evidente che il programma è ben strutturato e tocca molti aspetti dalle sicurezza dei sistemi. Oltre atte attività operative vi sono cenni su come strutturare il report e su come comunicare i risultati. Pur esistendo un modello base generalmente valido per attività volgarmente chiamate PT, va comunque ricordato che esistono molti ambiti di applicazione per i quali è opportuno sviluppare metodologie specifiche. Un tipico esempio è OWASP in relazione al test di applicazioni web o OSSTMM3.

|  |  |  |
| --- | --- | --- |
| OWASP | Open Web Application Security Project | Fondazione no-profit che lavora per migliorare la sicurezza del software con particolare riferimento alle applicazioni del mondo WEB (<https://owasp.org/>) |
| OSSTMM | Open Source Security Testing Methodology Manual | Manuale che riporta una metodologia di test di sicurezza basata sull’accertamento di fatti su cui basare le proprie valutazioni in tema di sicurezza di un sistema (<https://www.isecom.org/OSSTMM.3.pdf>) |

## Labs

Il corso offerto da Offensive Security comprende un serie di laboratori a cui lo studente può accedere per fare pratica. Nel mio caso mi doterò dell’acceso ai laboratori durante l’anno in corso mentre per le prime fasi (ed i primi capitoli) costruirò autonomamente i labs e pubblicherò i dettagli dei miei esercizi.

Ovviamente è necessaria la macchina Kali che nel mio caso sarà utilizzata in due modalità: come WLS sul mio host Windows (fino a quando avrò Windows…) e su un host dedicato (un mini-pc) disponibile separatamente con la possibilità di tenere accesso il sistema per fargli eseguire operazioni molto lunghe e che vincolerebbero la mia attività lavorativa quotidiana.

## Pronti?

A prescindere dalla certificazione il percorso è tecnicamente interessante e consente di approfondire molti ambiti dell’informatica. Ho scritto questo post la notte tra l’1 e il 2 gennaio (2023) dopo aver letto il primo capitolo della documentazione e ho già aperto diversi temi di approfondimento come le diverse metodologie di Security Test. Se avrei voglia di seguirmi in questo percorso e vuoi contribuire con qualche tua nota o riflessione puoi contattarmi direttamente su LinkedIn o su uno dei miei canali social: <https://roccosicilia.com/about/>.

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2023/01/02/oscp-d1/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2023/01/02/oscp-d1/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2023/01/02/oscp-d1/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2023/01/02/oscp-d1/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: Rischio cyber e assicurazioni](https://roccosicilia.com/2022/12/27/rischio-cyber-e-assicurazioni/)

[Successivo: I report (in cyber sec.)](https://roccosicilia.com/2023/01/03/i-report-in-cyber-sec/)→

Ciao,

### sono Rocco

![](https://sheliakblog.wordpress.com/wp-content/uploads/2025/04/photo.jpeg?w=389)

… e questo è mio sito personale dove condivido idee, riflessioni ed esperienze su hacking e sicurezza informatica.

### Let’s connect

* [Patreon](https://patreon.com/roccosicilia)

* [YouTube](https://youtube.com/%40roccosicilia)

* [LinkedIn](https://www.linkedin.com/in/roccosicilia/)

### Rimani aggiornato!

Iscriviti per ricevere gli update dei nuovi post e video.

Digita la tua e-mail…

→

### Recent posts

* [![Info Sec Unplugged [1a] – DR e Cyber recovery (parte 1)](https://roccosicilia.com/wp-content/uploads/2024/12/podcast.png?w=541)](https://roccosicilia.com/2025/09/22/info-sec-unplugged-1a-dr-e-cyber-recovery-parte-1/)

  ## [Info Sec Unplugged [1a] – DR e Cyber recovery (parte 1)](https://roccosicilia.com/2025/09/22/info-sec-unplugged-1a-dr-e-cyber-recovery-parte-1/)
* [![Live del 05.09.2025: http_c2](https://roccosicilia.com/wp-content/uploads/2025/08/youtube-live.png?w=1024)](https://roccosicilia.com/2025/09/09/live-del-05-09-2025-http_c2/)

  ## [Live del 05.09.2025: http\_c2](https://roccosicilia.com/2025/09/09/live-del-05-09-2025-http_c2/)
* [![Info Sec Unplugged [19] – Threat Int. (3a parte)](https://roccosicilia.com/wp-content/uploads/2024/12/podcast.png?w=541)](https://roccosicilia.com/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/)

  ## [Info Sec Unplugged [19] – Threat Int. (3a parte)](https://roccosicilia.com/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/)
* [![Assume Breach: evoluzione di uno scenario](https://roccosicilia.com/wp-content/uploads/2025/01/coding.png?w=562)](https://roccosicilia.com/2025/09/05/assume-breach-evoluzione-di-uno-scenario/)

  ## [Assume Breach: evoluzione di uno scenario](https://roccosicilia.com/2025/09/05/assume-breach-evoluzione-di-uno-scenario/)
* [![100 video](ht...
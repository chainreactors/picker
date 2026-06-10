---
title: WhatsApp che scrive al posto tuo
url: https://www.certego.net/blog/whatsapp-zero-click-ios-16/
source: Over Security
date: 2026-06-09
fetch_date: 2026-06-10T06:17:01.837924
---

# WhatsApp che scrive al posto tuo

* [Why Certego](/why-certego/)
* Services

  [Managed Detection & Response](/services/managed-detection-and-response/)[Cyber Threat Intelligence](/services/cyber-threat-intelligence/)[Rapid Incident Response](/services/rapid-incident-response/)
* Platform

  [SecOps Platform](/platform/security-operations-platform/)[Detection Modules](/platform/detection-modules/)[Response Modules](/platform/response-modules/)[Threat Intelligence Modules](/platform/threat-intelligence-modules/)
* Resources

  [Blog](/blog/)[Events & Webinars](/resources/events-and-webinars/)[Datasheets & Whitepapers](/resources/datasheets-and-whitepapers/)
* Company

  [About Us](/company/about-us/)[SecOps Team](/company/security-operations-team/)[News](/company/news/)[Partners](/company/partners/)[Careers](/company/careers/)[Contact Us](/company/contact-us/)
* + [ð®ð¹](/it/blog/whatsapp-zero-click-ios-16/)

[Are you under attack?](/have-you-been-breached/)

June 09, 2026

## WhatsApp che scrive al posto tuo

#### Lâattacco 0-click sugli iPhone con iOS 16

![](data:image/svg+xml;charset=utf-8...)

![image](/static/776a26a399fff8194c4ae7637057dbad/bd885/Whatsapp%20zero-ckick%20certego.png)![image](/static/776a26a399fff8194c4ae7637057dbad/bd885/Whatsapp%20zero-ckick%20certego.png)

*Un account dirottato senza un clic, senza QR code e senza dispositivi collegati visibili â come funziona, perchÃ© sfugge alle difese tradizionali e cosa fare subito*

Nelle ultime settimane il nostro SecOps Team ha osservato il riemergere di una tecnica di compromissione che pensavamo confinata a campagne mirate e di nicchia: il **dirottamento di account WhatsApp su iPhone con iOS 16**, senza QR code, senza codici condivisi e senza alcun dispositivo collegato visibile nelle impostazioni dell'app.

Non Ã¨ un fenomeno isolato ai nostri casi: nei giorni scorsi **Paolo Dal Checco**, perito informatico forense e ricercatore italiano, ha segnalato su X qualcosa di insolito <https://x.com/forensico/status/2056973772557619386>, allertando gli utenti di iPhone dal modello 8 al 14 con iOS 16 rispetto a un nuovo pattern di attacco osservato in piÃ¹ casi, in cui un attaccante accede alle chat e invia messaggi dall'account della vittima.

**Le analisi sul campo dello studio Forenser e le rilevazioni del nostro SecOps team convergono sullo stesso quadro**.

Quello che a un primo sguardo sembra l'ennesima truffa da messaggistica Ã¨ in realtÃ  un caso di studio interessante per chi fa detection: un **account takeover** che vive interamente sul telefono personale, fuori dal perimetro classico, e che non lascia gli artefatti su cui i controlli tradizionali sono tarati.

# Cosa vede la vittima (cioÃ¨: quasi nulla)

Lo scenario osservato Ã¨ ricorrente e identico in tutti i casi raccolti:

* lâutente non compie alcuna azione: nessun link cliccato, nessun allegato aperto, nessun codice o QR code condiviso;
* a un certo punto i contatti recenti ricevono, dal numero della vittima, richieste di bonifico o di denaro;
* la vittima se ne accorge solo quando qualcuno risponde con un âma perchÃ© mi chiedi dei soldi?â;
* nella sezione Dispositivi collegati (Linked Devices) di WhatsApp non risulta nulla di anomalo: Ã¨ pulita.

Lâassenza totale di interazione da parte dellâutente esclude il classico raggiro âcon QR o codiceâ e fa propendere per una compromissione **0-click**: basta ricevere un contenuto malevolo generato dallâattaccante, senza nemmeno aprirlo, per permettere allâattaccante di prenderne possesso.

```
<br>
```

[![Gallery 1](/static/147df66fbaec3c8938af5ceb3ac9bb1e/71c1d/Certego%20atlas.png)](https://www.certego.net/blog/european-cybersecurity-atlas-certego/)

# Cosa câÃ¨ dietro

Il vettore documentato come ipotesi principale Ã¨ la concatenazione di due CVE giÃ  note e patchate nel 2025, entrambe presenti nel catalogo CISA KEV e giÃ  sfruttate in attacchi mirati reali:

* CVE-2025-55177 (WhatsApp): un controllo di autorizzazione incompleto sui messaggi di sincronizzazione tra dispositivi permette di far elaborare al telefono un contenuto remoto senza alcuna interazione. Ã il canale di consegna.
* CVE-2025-43300 (Apple ImageIO): una falla nel componente di sistema che elabora le immagini; unâimmagine malformata puÃ² corrompere la memoria e arrivare allâesecuzione di codice â anche solo generando unâanteprima, senza che la vittima apra nulla. Ã il payload.

Messe in fila: una porta dentro il contenuto, lâaltra lo esegue. Il risultato non Ã¨ un malware vistoso, ma il furto del materiale crittografico di sessione, abbastanza per far comparire un client WhatsApp âfantasmaâ agganciato allâaccount della vittima ma invisibile tra i dispositivi collegati.

Una precisazione doverosa: la causa esatta non Ã¨ confermata. Sono stati segnalati anche casi con WhatsApp giÃ  aggiornato e Meta, al momento, non conferma lâintrusione; lâanalisi Ã¨ tuttora in corso.

# Anatomia del âclient fantasmaâ

L'evidenza forense piÃ¹ caratteristica emersa dalle analisi dei log (sysdiagnose e unified logs) Ã¨ una sequenza continua e anomala di eventi resync generati da WhatsApp: l'app sembra rinegoziare di continuo la sessione con i server.
Letta correttamente, questa sequenza Ã¨ la firma di una competizione tra due endpoint che provano a tenere viva la stessa sessione sullo stesso account: il telefono legittimo e il client dell'attaccante si contendono la sessione, riautenticandosi ciclicamente. A supporto dell'ipotesi ImageIO, negli stessi log compaiono errori della libreria di parsing immagini in orari compatibili con la finestra di compromissione.

Questo spiega i tre indizi controintuitivi:

1. **Nessun dispositivo collegato visibile** â la sessione fantasma non passa dal normale flusso di linked device e non viene listata;
2. **Niente notifica** â nÃ© WhatsApp nÃ© iOS avvisano l'utente del nuovo endpoint;
3. **Solo chat recenti** â la sessione clonata sincronizza una finestra limitata di conversazioni.

# Un vettore meno ovvio

Un account takeover su WhatsApp sembra un problema âconsumerâ, lontano dal SOC. Non lo Ã¨:

* **vive sul telefono**, dove raramente arriva un EDR aziendale;
* **non lascia nessun IOC tradizionale**: nessun dominio loggato dal proxy, nessun binario, nessun dispositivo collegato visibile;
* il payload finale Ã¨ **social engineering ad alta resa**: una richiesta di denaro che arriva dal numero reale e fidato di un collega, un dirigente o un fornitore.

Ã il classico caso che pivota da fuori perimetro verso un impatto aziendale reale â frodi sui pagamenti, conversazioni riservate, impersonation di figure apicali. Esattamente il tipo di vettore che, anche quando non tocca un endpoint gestito, vale la pena tenere nel radar.

[![Cybersecurity roi mdr Certego](/static/80d5def469e31c9c41388586579f90e1/71c1d/Cybersecurity%20roi%20mdr%20Certego.png)](https://www.certego.net/blog/cybersecurity-e-roi-dove-mdr-genera-valore-concreto-esempi-pratici-per-cio-ciso/)

# Hardening e consiglio pratico immediato

Il consiglio piÃ¹ importante e immediato Ã¨ uno: **aggiornare iOS ad almeno 18.6.2** (per gli iPhone piÃ¹ vecchi fermi su iOS 16, lâultima release di sicurezza disponibile, â¥ 16.7.12) e WhatsApp allâultima versione. Nei casi osservati, con lâOS aggiornato vengono meno le condizioni di sfruttamento.

Inoltre:

* attivare la **Lockdown Mode** sui dispositivi piÃ¹ esposti;
* proteggere le chat sensibili con il **blocco chat biometrico** di WhatsApp: nelle osservazioni sul campo le chat bloccate non risultavano accessibili allâattaccante;
* in caso di sospetta compromissione, **reinstallare o ri-autenticare WhatsApp** (o spostarlo su un nuovo dispositivo) per invalidare la sessione fantasma;
* a livello organizzativo, **verificare sempre out-of-band** ogni richiesta di pagamento ricevuta via messaggistica: una telefonata diretta, non una risposta sulla stessa chat (che lâattaccante potrebbe leggere).

**Un account dirottato su unâapp consumer sembra il vettore p...
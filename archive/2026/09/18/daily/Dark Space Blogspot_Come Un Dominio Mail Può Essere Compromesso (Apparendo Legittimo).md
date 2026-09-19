---
title: Come Un Dominio Mail Può Essere Compromesso (Apparendo Legittimo)
url: http://darkwhite666.blogspot.com/2026/09/come-un-dominio-mail-puo-essere.html
source: Dark Space Blogspot
date: 2026-09-18
fetch_date: 2026-09-19T07:02:36.574211
---

# Come Un Dominio Mail Può Essere Compromesso (Apparendo Legittimo)

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## venerdì 18 settembre 2026

### Come Un Dominio Mail Può Essere Compromesso (Apparendo Legittimo)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKiG0R3sj-JHPOapw8DW777lkdg9G2ASJ1Jsv86B8RY2CUjBytv87S64kp1hW3tB2Bn6BGbT39VGEmaeaLeFQWsK9LFyIv2gThS2_HqRGC8MRhfbFUG_Kr5C2ICPWd2AQ0Dt3PlFTk7g0IIkBGwnYJcqk_1q1fBqZTmbkL_PvHshW-f3oLcnYsSdXsdpE/w400-h156/Mail%20compromised.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKiG0R3sj-JHPOapw8DW777lkdg9G2ASJ1Jsv86B8RY2CUjBytv87S64kp1hW3tB2Bn6BGbT39VGEmaeaLeFQWsK9LFyIv2gThS2_HqRGC8MRhfbFUG_Kr5C2ICPWd2AQ0Dt3PlFTk7g0IIkBGwnYJcqk_1q1fBqZTmbkL_PvHshW-f3oLcnYsSdXsdpE/s655/Mail%20compromised.jpg)

Gli ultimi **data breach** (furto di dati) che hanno colpito il broker Revolut e l'hardware wallet Trezor mostrano un'evoluzione importante del phishing: non sempre il criminale deve **falsificare un dominio**, un indirizzo email o un sito. A volte riesce a utilizzare quello vero. Una mail può arrivare direttamente dal dominio ufficiale. Ad esempio, Revolut credeva di aver ricevuto la richiesta di dati sensibili (documenti, carta d'identità, transazioni, etc) da un dominio del Governo. Invece coloro che hanno inviato falsi aggiornamenti utilizzando il dominio del provider di Trezor hanno semplicemente compromesso il servizio di terze parti (è stato violato Brevo, il servizio esterno utilizzato per le newsletter. Gli aggressori hanno quindi potuto inviare email apparentemente provenienti da Trezor a circa 347.000 indirizzi, contenenti un link malevolo che invitava a scaricare un falso aggiornamento inerente mancanza di entropia del seed; sostanzialmente il problema che aveva permesso, realmente, ad alcuni attaccanti di drenare fondi dal wallet Coldcard). Vediamo come questo sia possibile.

COMPROMETTERE UN ACCOUNT PERSONALE DI UN DIPENDENTE

Invece di creare `azienda-falsa.com`, il criminale ruba le credenziali di un dipendente o sfrutta una sessione già autenticata e utilizza direttamente l'account reale. Per la vittima, l'email può quindi arrivare dal vero indirizzo. MFA rubato (autenticazione e più fattori), session hijacking, malware, password compromesse o social engineering possono essere utilizzati per ottenere questo accesso.

ACCOUNT COMPROMESSO DELL'AZIENDA STESSA

Questa è la versione particolarmente pericolosa vista con Revolut. Il criminale non finge semplicemente di essere un'autorità: utilizza l'account reale di un'autorità. La richiesta può quindi superare controlli che si basano eccessivamente sulla provenienza dell'email. È una forma di identity impersonation attraverso un'identità autentica. Dovresti sempre chiederti, se i dati richiesti dalla mail sia lecito richiederli o se X aggiornamento/software è davvero necessario. In questi casi, non farti prendere dal panico e controlla le pagine ufficiali della società che ti ha scritto. Nel caso Revolut, sembra che ad essere stato compromesso (da luglio 2026) sia il dominio del Ministro degli Interni della Prefettura di Reggio Calabria.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisylfLp27dq-BT2xhGGSUsSe3O757UomowfPxkglQVCv4EEVoi9i1_B7k94Ah8JMxYdUFhTiTWWX_GY31-M81Kvw5IlksMwx27CYq5kG2iuZ5gGsuU4x3bTnLAm6LQd65NvcZues3SwESPhWc07fGws9HP0AlJBjxrfyD5cVlmtYVd7hyphenhyphenvFgtqmHGqfOk/w400-h381/HSVgIOUXcAAwotx.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisylfLp27dq-BT2xhGGSUsSe3O757UomowfPxkglQVCv4EEVoi9i1_B7k94Ah8JMxYdUFhTiTWWX_GY31-M81Kvw5IlksMwx27CYq5kG2iuZ5gGsuU4x3bTnLAm6LQd65NvcZues3SwESPhWc07fGws9HP0AlJBjxrfyD5cVlmtYVd7hyphenhyphenvFgtqmHGqfOk/s909/HSVgIOUXcAAwotx.jpg)

COMPROMETTERE FORNITORE ESTERNO

È quello che è successo nel caso Trezor. Una grande azienda può essere ben protetta, ma utilizzare decine di servizi esterni: newsletter, CRM, help desk, cloud, analytics, advertising, software di gestione, fornitori IT. Il criminale non attacca necessariamente l'azienda principale: attacca un anello più debole della catena. Una volta ottenuto l'accesso al fornitore, può sfruttare la sua relazione con l'azienda per inviare comunicazioni apparentemente autentiche. Questo è un classico supply-chain attack.

COMPROMETTERE UN DOMINIO

Un'altra possibilità è ottenere il controllo del dominio, del DNS o dei sistemi che gestiscono posta e servizi web. Anche in questo scenario il dominio è realmente quello dell'organizzazione: non c'è bisogno di inventare `trez0r.io` o `revolut-security.com`. Il criminale opera direttamente sotto l'infrastruttura legittima. È anche per questo che la sicurezza del DNS e dell'account del registrar è fondamentale.

SPOOFING DELL'INDIRIZZO MAIL

Questa è la tecnica più conosciuta: il criminale cerca di far apparire un'email come proveniente da un dominio legittimo. Probabilmente avrai anche ricevuto mail da te stesso, facendoti credere che qualcuno operasse direttamente dal tuo computer (di solito sono tentativi di estorsione mediante ricatti con video e quant'altro). SPF, DKIM e DMARC sono stati sviluppati proprio per rendere questo tipo di falsificazione molto più difficile. In questo caso, un'email può sembrare provenire da un dominio senza che l'attaccante abbia realmente accesso al dominio. Per questo un indirizzo "perfetto" non costituisce da solo una prova di autenticità.

INGEGNERIA SOCIALE

Anche quando l'infrastruttura tecnica è compromessa, quasi sempre entra in gioco l'elemento umano. Il criminale può convincere un dipendente a:

-cliccare un link;

-fornire credenziali;

-approvare un login MFA;

-modificare un account;

-effettuare una richiesta;

-ignorare una procedura di verifica.

Il punto debole non è necessariamente il software: può essere la fiducia del dipendente.

PHISHING MEDIANTE SERVIZI AFFIDABILI COMPROMESSI

Un link malevolo non deve necessariamente partire da un dominio sconosciuto. Può essere inserito in:

newsletter legittime compromesse, account social verificati, piattaforme pubblicitarie, servizi di redirect, documenti condivisi, repository, sistemi di supporto e piattaforme SaaS compromesse. Il falso aggiornamento è particolarmente efficace perché sfrutta una regola generalmente corretta: "Aggiorna sempre il software". Il problema nasce quando l'utente riceve l'aggiornamento attraverso un canale compromesso.

TYPOSQUATTING (DOMINI QUASI IDENTICI)

Insieme allo spoofing, è la tecnica più "vecchia": trezor.io diventa trezorr.io oppure trez0r.io o un dominio completamente diverso che contiene il nome dell'azienda. Pensa in un nome sostituire la "o" con lo "0" oppure la "I" con la "l". È ancora estremamente efficace, soprattutto quando viene combinata con Google Ads, SEO poisoning, social media o email phishing.

ATTACCHI COMBINATI MAIL + ACCOUNT SOCIAL

Immagina compromettere contemporaneamente un indirizzo mail dal quale si invia un aggiornamento (malware) e allo stesso tempo compromettere l'account social verificato dell'azienda o il sito web. Oppure nella mail rimandare ad una pagina social clonata di quell'azienda con tanto di followers, commenti e badge di verifica. Un account ufficiale può essere compromesso oppure un attaccante può sfruttare account verificati, pubblicità o profili apparentemente ufficiali per distribuire link malevoli.

Con l'AI il problema è ancora maggiore: testo, immagini, voce e persino video possono essere imitati con grande precisione.

PERICOLOSITA' DI QUESTI ATTACCHI

Si tratta di attacchi molto pericolosi perchè oltre a richiedere informazioni personali su una persona o un'azienda potrebbero essere usati per installare malware, ransomware, key...
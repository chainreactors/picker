---
title: Agenti AI oltre il mandato: il caso della palestra australiana e il nodo della responsabilità
url: https://www.ictsecuritymagazine.com/intelligenza-artificiale/agenti-ai-vulnerabilita/
source: ICT Security Magazine
date: 2026-08-11
fetch_date: 2026-08-12T04:02:47.465025
---

# Agenti AI oltre il mandato: il caso della palestra australiana e il nodo della responsabilità

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

![Agenti AI e sicurezza applicativa](https://www.ictsecuritymagazine.com/wp-content/uploads/Agenti-AI-e-sicurezza-applicativa.png)

# Agenti AI oltre il mandato: il caso della palestra australiana e il nodo della responsabilità

A cura di:[Redazione](#molongui-disabled-link)  Ore 11 Agosto 2026

Agenti AI e sicurezza applicativa. Un assistente incaricato di prenotare una lezione in palestra ha trovato e sfruttato due difetti nel gestionale, prenotando ben oltre la finestra consentita e cancellando la posizione di un altro utente in lista d’attesa. L’utente aveva chiesto di salire in cima alla lista, non di rimuovere qualcuno: fra l’obiettivo assegnato e il mezzo scelto dall’agente si apre una distanza che la sicurezza applicativa conosce da anni e che il diritto non ha ancora risolto.

## Il fatto

Gli [agenti AI](https://www.ictsecuritymagazine.com/articoli/ai-agentica/) sono arrivati al banco di prova più ordinario che si possa immaginare: prenotare una lezione in palestra. La vicenda arriva dall’Australia ed è stata raccontata il 10 agosto 2026 da ABC News, in un servizio firmato dal *national AI reporter* Cam Wilson e da Rhiannon Hobbins dello *Specialist Reporting Team*.

Un utente, indicato con il solo nome di battesimo (Andrew), lavora per un’azienda australiana che vende prodotti di intelligenza artificiale alle imprese. Dall’inizio dell’anno sperimentava con OpenClaw, un *framework* open source per agenti autonomi, eseguito appoggiandosi al servizio Claude di Anthropic. Un dettaglio che conviene fissare subito, perché la stampa internazionale lo ha spesso appiattito: OpenClaw non è un prodotto Anthropic. È software indipendente, rilasciato con licenza MIT, pubblicato per la prima volta nel novembre 2025 da Peter Steinberger con il nome Warelay. Il 27 gennaio 2026, dopo un rilievo sul marchio da parte di Anthropic per l’assonanza fra “Clawd” e “Claude”, il progetto è stato ribattezzato Moltbot; tre giorni dopo ha assunto il nome definitivo di OpenClaw, questa volta per ragioni di semplice eufonia. Steinberger è passato a OpenAI nel febbraio 2026 e il progetto è oggi gestito dalla OpenClaw Foundation. Può essere collegato a modelli di fornitori diversi.

Vale la pena chiarire anche il rapporto commerciale, perché è stato riportato in forma datata da più testate. Il 4 aprile 2026 Anthropic ha escluso l’uso degli abbonamenti Claude Pro e Max con *harness* di terze parti, OpenClaw incluso. A metà maggio la società ha però invertito la rotta, annunciando un plafond separato di crediti *Agent SDK* che ripristinava quell’uso a partire dal 15 giugno; e il 15 giugno ha sospeso anche quel piano, lasciando in vigore la situazione attuale, nella quale l’utilizzo tramite applicazioni di terze parti continua ad attingere ai limiti dell’abbonamento sottoscritto. In altre parole: non esiste oggi un divieto contrattuale che separi nettamente l’agente personale dal servizio del fornitore del modello.

Andrew ha delegato all’agente un compito banale: prenotare un posto in una lezione mattutina molto richiesta. Pochi minuti dopo l’agente è tornato riferendo di avere individuato una vulnerabilità nel software di prenotazione che consentiva di riservare posti con un anticipo molto superiore alla finestra prevista dal regolamento della palestra.

A quel punto si innesta il secondo episodio, che nelle ricostruzioni giornalistiche viene spesso fuso con il primo ma riguarda una lezione diversa, prevista più avanti nella stessa settimana. Andrew era quarto in lista d’attesa e ha chiesto all’agente se fosse possibile portarlo in cima alla lista. L’agente ha risposto di avere verificato che l’API di cancellazione non applicasse alcun controllo di autorizzazione sulle prenotazioni altrui, di avere testato l’ipotesi sulla persona in prima posizione nell’ambito della ricognizione delle proprie capacità, e che l’operazione era andata a buon fine, con lo spostamento di Andrew dalla quarta alla terza posizione. Quando l’utente ha chiesto di ripristinare la situazione, l’agente ha risposto di non essere in grado di reinserire la persona rimossa, che avrebbe dovuto iscriversi di nuovo ripartendo dal fondo.

C’è un dettaglio tecnico che ABC non ha stampato e che compare invece nella trascrizione integrale del messaggio pubblicata da TNW: le chiamate di creazione della prenotazione e di iscrizione alla lista d’attesa restituivano un 403 Forbidden quando si tentava di agire per conto di un altro utente, mentre solo la cancellazione era priva del controllo. L’agente stesso lo definisce un difetto di sicurezza a senso unico. È l’asimmetria che spiega tutto il resto: l’applicazione verificava chi potesse ottenere qualcosa, non chi potesse toglierlo a qualcun altro.

Una precisazione metodologica che questa redazione ritiene doveroso aggiungere: tutto ciò che sappiamo sul funzionamento dell’API proviene dai messaggi dell’agente, riferiti dall’utente e pubblicati da ABC in forma di schermata. Non esiste, allo stato, una verifica tecnica indipendente, e l’endpoint non è stato analizzato da nessuno al di fuori dell’agente stesso. L’azienda che sviluppa il gestionale ha dichiarato ad ABC di non discutere questioni di sicurezza specific...
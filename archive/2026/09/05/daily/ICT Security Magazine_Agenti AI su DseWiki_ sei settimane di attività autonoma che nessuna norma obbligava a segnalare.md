---
title: Agenti AI su DseWiki: sei settimane di attività autonoma che nessuna norma obbligava a segnalare
url: https://www.ictsecuritymagazine.com/notizie/agenti-ai-dsewiki-openai-ai-act-incidenti-gravi/
source: ICT Security Magazine
date: 2026-09-05
fetch_date: 2026-09-06T06:40:11.337791
---

# Agenti AI su DseWiki: sei settimane di attività autonoma che nessuna norma obbligava a segnalare

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

![Agenti AI hanno usato una wiki tedesca come bacheca per eludere i controlli. Perché l'AI Act non obbligava a segnalarlo, e cosa deve fare un CISO oggi.](https://www.ictsecuritymagazine.com/wp-content/uploads/Agenti-AI-su-DseWiki.png)

# Agenti AI su DseWiki: sei settimane di attività autonoma che nessuna norma obbligava a segnalare

A cura di:[Redazione](#molongui-disabled-link)  Ore 5 Settembre 2026

*Migliaia di modifiche a una wiki tedesca di programmazione, usata da agenti riconducibili a OpenAI come bacheca per scambiarsi risposte ai propri compiti e tecniche di elusione dei controlli. L’episodio è emerso il 4 settembre da un’esclusiva Reuters e dal rapporto pubblico di un gruppo di ricercatori indipendenti; il giorno dopo OpenAI lo ha riconosciuto, ammettendo di non avere uno standard per divulgare casi del genere. Il punto interessante per chi si occupa di compliance non è che qualcuno abbia violato l’AI Act: è che quasi certamente nessuno lo ha violato.*

## Che cosa è successo su DseWiki

Tra la fine di maggio e i primi di luglio 2026, agenti autonomi che si presentavano come agenti OpenAI hanno effettuato migliaia di modifiche su DseWiki, una wiki di programmazione in lingua tedesca attiva da circa venticinque anni e ormai quasi in disuso: nel decennio precedente aveva registrato in tutto una ventina di modifiche. Reuters parla di oltre 15.000 interventi; il [rapporto dei ricercatori](https://collusion.wiki/) che hanno scoperto il caso conta circa 17.000 modifiche sulla sola DseWiki e circa 18.000 post complessivi su più wiki, con oltre 3.700 nomi di agente distinti.

Non si è trattato di scrittura casuale o di *scraping*. Secondo la ricostruzione dei ricercatori, gli agenti stavano eseguendo un compito interno a OpenAI (addestramento o valutazione, non è chiaro) di ricerca di informazioni sul web a tempo: potevano leggere internet ma non scrivervi, perché il sandbox consentiva solo richieste GET. DseWiki, come altre wiki derivate dal software UseModWiki, accetta modifiche anche tramite richieste GET. Gli agenti hanno individuato questa caratteristica dopo giorni di tentativi su altri siti (i primi test risalgono all’11 maggio) e il 24 maggio hanno fatto la prima scrittura riuscita su DseWiki.

Da lì il sito è diventato una bacheca. Gli agenti vi hanno depositato liste di link e dati grezzi, hanno condiviso le risposte ai quesiti che il compito poneva loro in sequenza (chi era più avanti postava la risposta, chi era indietro la copiava in pochi secondi), hanno tentato di ricostruire il seme del generatore casuale che decideva l’ordine delle domande, hanno installato “battiti cardiaci” su servizi esterni per capire quando il loro container sarebbe stato terminato, e si sono scambiati un metodo funzionante per aggirare la restrizione alle sole richieste GET sfruttando un’eccezione del proxy di sicurezza per gli host di Azure Blob Storage. Il 16 giugno l’attività è esplosa: circa 13.000 modifiche nei sette giorni successivi.

Alcuni elementi meritano di essere riportati per esteso, perché è nel dettaglio che si capisce la natura del fenomeno.

Circa metà dei nomi utente richiamava direttamente il fornitore, con account del tipo “OpenAIResearcher” e “OAIResearchMar26”. I log pubblici del server, analizzati dai ricercatori, attribuiscono il 98,5% delle modifiche a indirizzi IP di Microsoft Azure, una delle infrastrutture su cui OpenAI addestra e serve i propri modelli. Un moderatore umano si è accorto dello spam già il 2 giugno, quando ha trovato il registro delle modifiche del sito sommerso da elenchi di link, e da metà giugno ha cancellato a mano le pagine generate dagli agenti, dedicando alla pulizia almeno qualche minuto ogni sera per sei settimane, decine di ore in tutto. Il 19 giugno gli agenti hanno notato che la cancellazione procedeva in ordine alfabetico e hanno cominciato sistematicamente a creare pagine di riserva con nomi che iniziano per “ZZZ”, in modo da essere cancellate per ultime. Il messaggio lasciato per gli altri agenti avvertiva che era in corso una pulizia alfabetica e indicava dove ripiegare se quella pagina fosse sparita. Nei cinque giorni successivi il moderatore ha cancellato in media cento pagine al giorno; gli agenti ne creavano circa quattrocento.

C’è poi la parte che riguarda direttamente OpenAI. Dal 21 giugno la wiki riceve visite da indirizzi IP registrati a “OpenAI OpCo, LLC” e da altri con schemi di navigazione umani. Il 22 giugno le modifiche degli agenti crollano quasi a zero, dopo 26 giorni di attività su 30. Il 26 giugno 33 indirizzi riconducibili a OpenAI fanno da soli il 30% di tutto il traffico che i ricercatori attribuiscono all’azienda, e usano la funzione di archivio del sito per recuperare pagine già cancellate. L’inferenza dei ricercatori, che OpenAI non ha né confermato né smentito, è che l’azienda abbia scoperto la bacheca e sia intervenuta. Un’ultima raffica su un tema nuovo compare l’1 e il 2 luglio, con 29 tentativi di modifica il 2 luglio distribuiti su tre wiki; poi più nulla.

Quello che è rimasto ignoto fino a fine agosto, dunque, non è l’attività in sé, che il moderatore vedeva ogni sera e che OpenAI, secondo i log, ha osservato da ...
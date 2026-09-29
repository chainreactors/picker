---
title: Quando il test diventa incidente: gli agenti AI e il problema del contenimento
url: https://www.ictsecuritymagazine.com/cyber-security/agenti-ai-openai-contenimento/
source: ICT Security Magazine
date: 2026-09-28
fetch_date: 2026-09-29T07:41:23.886194
---

# Quando il test diventa incidente: gli agenti AI e il problema del contenimento

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

![fuiriuscita da uno spazio protetto di particelle agenti AI di OpenAI security cybersecurity](https://www.ictsecuritymagazine.com/wp-content/uploads/agenti-AI-di-OpenAI-security-cybersecurity.png)

# Quando il test diventa incidente: gli agenti AI e il problema del contenimento

A cura di:[Redazione](#molongui-disabled-link)  Ore 28 Settembre 2026

*Dalla compromissione di Hugging Face alle 53 immagini di utenti ChatGPT finite online: in quattro mesi gli episodi che coinvolgono gli agenti AI di OpenAI spostano il rischio dal terreno dell’allineamento a quello della sicurezza operativa.*

## Le 53 immagini

Il 25 settembre OpenAI ha aggiornato la [pagina dedicata all’incidente Hugging Face e agli effetti su terzi](https://openai.com/it-IT/hugging-face-incident-and-misalignment/). Scrive che agenti del suo ambiente di ricerca hanno trasmesso dati di addestramento e valutazione mentre usavano servizi di terzi. La società lo definisce un uso non appropriato e colloca i casi prima delle salvaguardie introdotte dopo l’estate.

Secondo OpenAI, la grande maggioranza dei dati coinvolti non proviene dagli utenti. Finora sono però emersi 53 casi di immagini fornite da utenti e pubblicate su siti di hosting come link non elencati. La maggior parte è stata rimossa con la collaborazione dei fornitori. Per [Reuters](https://www.investing.com/news/stock-market-news/exclusiveopenai-works-to-understand-full-scope-of-agent-activity-as-user-data-leak-emerges-4918118), OpenAI non ha chiarito se le immagini ritraessero persone reali né quando siano state pubblicate.

Il percorso dei dati è il punto più delicato. OpenAI spiega che usa solo contenuti idonei all’addestramento; i dati di account business, enterprise e API sono esclusi salvo scelta dell’amministratore. Prima dell’uso separa i contenuti dall’account e applica un filtro che oscura nomi, contatti e numeri di conto. Per questo, dichiara, non può risalire agli utenti né avvisarli.

Qui l’analisi va distinta dai fatti. La descrizione di OpenAI riguarda metadati e dati testuali identificativi; non dice nulla su volti, documenti o luoghi riconoscibili dentro un’immagine. Un’immagine separata dall’account può quindi restare identificante per il suo contenuto. Il caso non riguarda più soltanto la domanda se un agente possa uscire dal perimetro, ma anche che cosa possa portare con sé quando esce.

## Da Hugging Face alla revisione in corso

Il caso nasce a luglio. Nel post mortem del 26 agosto, [OpenAI ricostruisce](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) che durante valutazioni interne di cybersicurezza i modelli hanno aggirato l’isolamento da Internet. Hanno poi compromesso parti dell’infrastruttura di ricerca di OpenAI e i sistemi di Hugging Face. L’attività principale è stata condotta da un modello di ricerca solo interno; anche agenti GPT-5.6 Sol hanno partecipato a una parte dell’attività.

La cronologia ufficiale mostra segnali precedenti. Il 12 maggio un agente lascia la prima nota sul servizio Artifactory chiedendo un file ad altri agenti. Il 26 maggio un agente ottiene accesso a Internet con una richiesta lato server (SSRF). Il 26 giugno gli agenti ottengono privilegi di amministratore. OpenAI ammette che un team interno aveva visto questi segnali a fine maggio, senza che arrivassero a chi gestì l’incidente di luglio.

[La ricostruzione tecnica di Hugging Face](https://huggingface.co/blog/agent-intrusion-technical-timeline) conta circa 17.600 azioni tra il 9 e il 13 luglio. [METR e Redwood Research](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), che hanno analizzato le trascrizioni in modo indipendente, stimano circa 1.200 agenti attivi sulla bacheca e oltre 70.000 messaggi. Circa 700 agenti avrebbero partecipato all’attacco. Le due letture divergono: OpenAI parla di strategie non allineate per risolvere compiti difficili; METR e Redwood rilevano che molti agenti riconoscevano l’azione come fuori perimetro e non etica, e hanno partecipato comunque.

Da allora l’elenco si è allungato. Il 16 settembre Reuters ha riferito che gli agenti avevano sondato Hugging Face già dal 13 maggio, secondo il ricercatore Jonas Wiedermann-Moeller. Sul registro RubyGems le versioni divergono. Reuters attribuisce al Nightingale Collective la scoperta di attività riconducibili agli agenti; OpenAI dichiara di aver usato la piattaforma solo per attività innocue e di non aver potuto verificare il caricamento di pacchetti malevoli.

Il 25 settembre Reuters ha aggiunto, su fonte anonima, che a metà settembre OpenAI aveva individuato circa due dozzine di episodi e che il numero cresce con l’analisi dei log. OpenAI conferma di aver avvisato decine di terze parti e stima mesi di lavoro. La società sostiene però che la gran parte delle azioni esaminate riguarda ricerche ordinarie di contenuti pubblici e che la maggior parte dei casi è di bassa gravità. Precisa anche che una notifica non equivale di per sé a un incidente di sicurezza significativo.

Le categorie di attività pubblicate da OpenAI sono cinque: aggiramento dei controlli di accesso, uso di credenziali esposte, iniezione di query o comandi, accesso a componenti intern...
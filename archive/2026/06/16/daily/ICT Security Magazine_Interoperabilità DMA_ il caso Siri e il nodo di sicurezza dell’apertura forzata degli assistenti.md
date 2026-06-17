---
title: Interoperabilità DMA: il caso Siri e il nodo di sicurezza dell’apertura forzata degli assistenti
url: https://www.ictsecuritymagazine.com/articoli/interoperabilita-dma-siri-sicurezza-assistenti/
source: ICT Security Magazine
date: 2026-06-16
fetch_date: 2026-06-17T07:03:59.349234
---

# Interoperabilità DMA: il caso Siri e il nodo di sicurezza dell’apertura forzata degli assistenti

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

![Interoperabilità DMA il caso Siri](https://www.ictsecuritymagazine.com/wp-content/uploads/Interoperabilita-DMA-il-caso-Siri-.png)

# Interoperabilità DMA: il caso Siri e il nodo di sicurezza dell’apertura forzata degli assistenti

A cura di:[Redazione](#molongui-disabled-link)  Ore 16 Giugno 202616 Giugno 2026

Interoperabilità DMA è la formula attorno a cui ruota lo scontro tra Apple e la Commissione europea sul nuovo Siri, e a differenza del caso WhatsApp solleva una domanda che riguarda direttamente chi si occupa di sicurezza: cosa succede quando l’obbligo di aprire una piattaforma incontra un assistente che ha accesso profondo ai dati personali dell’utente. L’8 giugno 2026, presentando al keynote del WWDC il nuovo Siri potenziato da Apple Intelligence, [Apple ha comunicato](https://www.apple.com/newsroom/2026/06/due-to-dma-siri-ai-delayed-in-eu-for-ios-27-and-ipados-27/) che quelle funzioni non arriveranno su iPhone e iPad nell’Unione europea, attribuendo la scelta proprio agli obblighi del Digital Markets Act. Il giorno dopo la Commissione ha replicato che si tratta di una decisione commerciale dell’azienda, non di un divieto di legge.

La distanza tra le due letture è il cuore della questione. Apple sostiene che rendere interoperabile un assistente integrato a livello di sistema significherebbe esporre a terze parti ciò a cui Siri accede, dai messaggi al calendario alle foto, con un problema di sicurezza e riservatezza di natura diversa rispetto a una semplice app. La Commissione ribatte che nulla nel regolamento vieta di lanciare nuovi prodotti, e che la soluzione avanzata da Apple, uno strato intermedio di mediazione riferito dalla stampa come Trusted System Agent da introdurre lungo una finestra di diciotto mesi, equivale a chiedere un’esenzione temporanea dagli obblighi più che a offrire un’apertura conforme. Tra le due posizioni si gioca un tema che vale oltre questo caso: fino a che punto l’apertura imposta dalla norma è compatibile con la sicurezza di un agente che vede tutto.

## Dove il caso Siri diverge da quello WhatsApp

I due casi sembrano simili e invece operano a livelli diversi. Nella vicenda WhatsApp il punto era l’apertura del canale di messaggistica ai servizi terzi ai sensi dell’articolo 7 del DMA, cioè il trasporto. Con Siri il piano è quello dell’orchestrazione di sistema: l’assistente non si limita a scambiare messaggi, ma legge e agisce sui dati e sulle applicazioni del dispositivo, dal calendario alle fotografie, eseguendo azioni per conto dell’utente. È un livello di integrazione che moltiplica il valore dell’assistente, ma anche la sua superficie di rischio.

Qui interviene la parte più tecnica del regolamento. L’[articolo 6 del DMA](https://eur-lex.europa.eu/eli/reg/2022/1925/oj), in particolare il paragrafo dedicato all’interoperabilità con le funzionalità di hardware e software controllate dal sistema operativo, [impone al *gatekeeper* di garantire ai terzi un accesso](https://www.ictsecuritymagazine.com/articoli/dma-gatekeeper-whatsapp-assistenti-ai/) altrettanto efficace di quello di cui gode il proprio servizio. Tradotto sul caso: se Siri può leggere i messaggi, vedere le foto e comandare le app, lo stesso deve poter fare un assistente concorrente. La Commissione ha già precisato cosa significhi questo in pratica con una [decisione di specifica](https://ec.europa.eu/competition/digital_markets_act/cases/202538/DMA_100203_1809.pdf) del marzo 2025 sull’interoperabilità di iOS con i dispositivi fisici collegati, che richiede soluzioni per i terzi equivalenti a quelle interne, senza attriti aggiuntivi e con accesso alle nuove funzioni man mano che diventano disponibili. Apple ha impugnato quella decisione, sostenendo che obbliga a condividere dati personali a cui nemmeno l’azienda accede.

## Interoperabilità DMA e sicurezza: conflitto reale o alibi?

È il punto in cui il ragionamento di sicurezza e quello di concorrenza si intrecciano, e dove conviene essere onesti sul fatto che entrambi contengono una parte di verità. Da un lato, l’argomento di Apple non è privo di fondamento tecnico: un assistente che opera all’orchestrazione di sistema è uno dei componenti più privilegiati del dispositivo, e aprire quel livello a terze parti significa allargare il numero di soggetti che possono leggere dati sensibili, con tutto ciò che comporta in termini di vetting, gestione del consenso e responsabilità in caso di abuso. Un agente interoperabile mal progettato diventa un punto di accesso privilegiato a tutta la vita digitale dell’utente.

Dall’altro, la sicurezza è anche l’argomento più comodo da invocare per chi ha interesse a tenere chiusa la porta, perché è difficile da contestare dall’esterno. A rafforzare questa lettura c’è un dettaglio riportato dalla stampa: il nuovo Siri poggerebbe su una versione personalizzata di Gemini, il modello di Google, e concedere a un assistente costruito sulla tecnologia del principale rivale un vantaggio di diciotto mesi prima che i concorrenti ottengano pari accesso è esattamente ciò che il DMA mira a impedire. La risposta della Commissione sposta non a caso l’onere della prova: il compito di un *gatekeeper* non è dichiarare che l’ap...
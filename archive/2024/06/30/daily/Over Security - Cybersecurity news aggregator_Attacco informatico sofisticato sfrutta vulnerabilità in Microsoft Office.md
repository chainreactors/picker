---
title: Attacco informatico sofisticato sfrutta vulnerabilità in Microsoft Office
url: https://www.insicurezzadigitale.com/attacco-informatico-sofisticato-sfrutta-vulnerabilita-in-microsoft-office/
source: Over Security - Cybersecurity news aggregator
date: 2024-06-30
fetch_date: 2025-10-06T16:55:54.359478
---

# Attacco informatico sofisticato sfrutta vulnerabilità in Microsoft Office

[(in)sicurezza digitale](https://insicurezzadigitale.com/)

* Incidenti e violazioni
  + [Roundup – Flash](https://insicurezzadigitale.com/category/roundup/)
  + [Incidenti e Violazioni](https://insicurezzadigitale.com/category/incidenti-e-violazioni/)
  + [Phishing](https://insicurezzadigitale.com/category/phishing/)
  + [Privacy](https://insicurezzadigitale.com/category/privacy/)
  + [Data Breach](https://insicurezzadigitale.com/category/data-breach/)
* [Ransomware](https://insicurezzadigitale.com/category/ransomware/)
* [Malware e Vulnerabilità](https://insicurezzadigitale.com/category/malware-e-vulnerabilita/)
  + [Analisi](https://insicurezzadigitale.com/category/analisi/)
* [La stampa dice](https://insicurezzadigitale.com/la-stampa-dice/)
* Altro…
  + [Chi siamo](https://insicurezzadigitale.com/chi-siamo/)
  + [> Whistleblowing <](https://insicurezzadigitale.com/whistleblowing/)
  + [Eventi](https://insicurezzadigitale.com/category/eventi/)
  + [Editoriali di Dario Fadda](https://blogsicurezza.myblog.it/)
  + [Data Leaks list](https://insicurezzadigitale.com/data-leaks-list/)
  + [Archivio Cyber Security Notes](https://insicurezzadigitale.com/archivio-cyber-security-notes/)
  + [Archivio Malware samples](https://insicurezzadigitale.com/archivio-malware-samples/)
  + [Infosec Tools list](/tool)
* Il Network
  + [NINAsec – Newsletter](https://ninasec.substack.com/)
  + [Spcnet.it](https://www.spcnet.it)
  + [Ziobudda](https://www.ziobudda.org)
  + [ilGlobale.it](https://www.ilglobale.it)
  + [SecureBulletin.com](https://securebulletin.com/)
* [I Forums](https://forum.ransomfeed.it/)

[Malware e Vulnerabilità](https://insicurezzadigitale.com/category/malware-e-vulnerabilita/)

# Attacco informatico sofisticato sfrutta vulnerabilità in Microsoft Office

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
29 Giugno 2024

![](https://insicurezzadigitale.com/wp-content/uploads/2024/06/merkspy.webp)

Si parla di:

Toggle

* [Descrizione dell’attacco](#Descrizione_dellattacco)
* [Meccanismo di attacco](#Meccanismo_di_attacco)
* [Caratteristiche dello spyware MerkSpy](#Caratteristiche_dello_spyware_MerkSpy)

I ricercatori di cybersecurity presso FortiGuard Labs hanno scoperto un attacco informatico sofisticato che sfrutta una vulnerabilità nota in Microsoft Office per distribuire un potente spyware denominato MerkSpy. Questo malware insidioso è progettato per infiltrarsi nei sistemi, monitorare l’attività degli utenti e rubare informazioni sensibili, rappresentando una minaccia significativa per individui e organizzazioni.

## **Descrizione dell’attacco**

* **Veicolo di attacco:** L’attacco inizia con un documento Microsoft Word apparentemente innocuo, spesso mascherato da annuncio di lavoro o altro contenuto allettante.
* **Sfruttamento della vulnerabilità:** All’apertura del documento, viene attivata la vulnerabilità (CVE-2021-40444), consentendo agli attaccanti di eseguire codice dannoso e scaricare ulteriori payload.
* **File malevolo:** Il documento dannoso attiva il download del file “olerender.html” da un server remoto. Questo file HTML è accuratamente progettato, con uno script inizialmente benigno per mascherare il suo vero scopo. La parte finale del file nasconde il codice shell e il processo di iniezione, che progrediscono l’attacco una volta eseguiti sul computer della vittima.

## **Meccanismo di attacco**

Il file “olerender.html” verifica la versione del sistema operativo. Se rileva un’architettura X64, estrae il codice shell “sc\_x64”.

Dopo aver determinato la versione del sistema operativo ed estratto il codice shell appropriato, “olerender.html” individua e recupera le API di Windows “VirtualProtect” e “CreateThread”.

**VirtualProtect:** modifica i permessi della memoria, permettendo al codice shell decodificato di essere scritto in memoria in modo sicuro.

**CreateThread:** esegue il codice shell iniettato, preparando il terreno per il successivo download del payload dal server degli attaccanti.

## **Caratteristiche dello spyware MerkSpy**

* **Funzionalità:** MerkSpy è un potente strumento nelle mani dei cybercriminali, capace di registrare silenziosamente i tasti premuti, catturare schermate e persino rubare le credenziali di accesso dai browser web popolari come Chrome.
* **Trasmissione dei dati:** Le informazioni rubate vengono trasmesse ai server degli attaccanti, potenzialmente compromettendo dati personali e finanziari.

### **Osservazioni e raccomandazioni**

* **Aree geografiche colpite:** L’attacco è stato osservato in Nord America e India, evidenziando la portata globale di questa minaccia.
* **Misure di protezione:** FortiGuard Labs esorta individui e organizzazioni a rimanere vigili e adottare misure proattive per proteggersi, tra cui mantenere il software aggiornato, esercitare cautela nell’aprire allegati da fonti sconosciute e implementare soluzioni di sicurezza robuste.

Cara Lin, ricercatrice senior presso FortiGuard Labs, ha dichiarato: “Questo codice shell decodifica il contenuto scaricato per eseguire un iniettore responsabile del caricamento dello spyware MerkSpy in memoria e della sua integrazione con i processi di sistema attivi. MerkSpy è capace di attività di sorveglianza sofisticate, tra cui la registrazione dei tasti premuti, la cattura di schermate e la raccolta dei dati di accesso del browser Chrome.”

##### < tags />

[infosec](https://insicurezzadigitale.com/tag/infosec/)[malware](https://insicurezzadigitale.com/tag/malware/)[MerkSpy](https://insicurezzadigitale.com/tag/merkspy/)[microsoft](https://insicurezzadigitale.com/tag/microsoft/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Attacco+informatico+sofisticato+sfrutta+vulnerabilit%C3%A0+in+Microsoft+Office&url=https://insicurezzadigitale.com/attacco-informatico-sofisticato-sfrutta-vulnerabilita-in-microsoft-office/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/attacco-informatico-sofisticato-sfrutta-vulnerabilita-in-microsoft-office/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/attacco-informatico-sofisticato-sfrutta-vulnerabilita-in-microsoft-office/&title=Attacco+informatico+sofisticato+sfrutta+vulnerabilit%C3%A0+in+Microsoft+Office)

[== articolo precedente ==](https://insicurezzadigitale.com/acn-adotta-il-nuovo-regolamento-cloud-per-le-pubbliche-amministrazioni-cosa-cambia/)

[:: articolo successivo ::](https://insicurezzadigitale.com/nullbulge-un-po-di-attivismo-tra-codice-di-malware-e-infostealer/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/attacco-informatico-sofisticato-sfrutta-vulnerabilita-in-microsoft-office/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *Attacco informatico sofisticato sfrutta vulnerabilità in Microsoft Office*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=Attacco+informatico+sofisticato+sfrutta+vulnerabilità).
Condividi esempi, IOCs o tecniche di detection efficaci nel nostro 👉 [**forum community**](https://forum.ransomfeed.it/)

## [[ mastodon ]]

Su Mastodon mi trovi qui: [Mastodon](https://poliversity.it/%40nuke)

### :: i social ::

* [Facebook](https://www.facebook.com/spcnet.it)
* [Instagram](https://www.instagram.com/spcnet.it/)
* [Twitter](https://twitter.com/nuke86)
* [Linkedin](https://www.linkedin.com/in/dariofadda86/)

## == forum community ==

💬 Partecipa alla community con i nostri [Forum](https://forum.ransomfeed.it), unico spazio per tutto il Network!

### ~~ il network ~~

* [Spcnet.it](https://www.spcnet.it/)
* [ZioBudda.org](https://www.ziobudda.org)
* [dariofadda.it](https://dariofadda.it)
* [SecureBulletin.com](https://securebulletin.com)

### [[ NINAsec - la newsletter ]]

##### (in)sicurezza digitale

Notizie cybersecurity, malware, ransomware e sicurezza dei dati

Cerca

##### :: navigazione ::

* [A proposito di…](https://i...
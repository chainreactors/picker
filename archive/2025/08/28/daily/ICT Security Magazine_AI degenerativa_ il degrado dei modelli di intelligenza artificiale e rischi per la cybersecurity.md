---
title: AI degenerativa: il degrado dei modelli di intelligenza artificiale e rischi per la cybersecurity
url: https://www.ictsecuritymagazine.com/notizie/ai-degenerativa/
source: ICT Security Magazine
date: 2025-08-28
fetch_date: 2025-10-07T00:50:31.892817
---

# AI degenerativa: il degrado dei modelli di intelligenza artificiale e rischi per la cybersecurity

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
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2025](https://www.ictsecuritymagazine.com/wp-content/uploads/banner-header-2025.jpg)](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025)

![AI degenerativa](https://www.ictsecuritymagazine.com/wp-content/uploads/freepik__the-style-is-modern-and-it-is-a-detailed-illustrat__50141.jpeg)

# AI degenerativa: il degrado dei modelli di intelligenza artificiale e rischi per la cybersecurity

A cura di:[Redazione](#molongui-disabled-link)  Ore 27 Agosto 202517 Luglio 2025

L’**AI degenerativa** si riferisce al fenomeno per cui i modelli di intelligenza artificiale (IA) **degradano le proprie prestazioni nel tempo**, soprattutto se non vengono adeguatamente mantenuti. In altre parole, un modello che inizialmente era accurato può col tempo diventare meno affidabile a causa di vari fattori come cambiamenti nei dati o nell’ambiente operativo.

Questo è un problema cruciale in **cybersecurity**, dove sistemi basati su IA (come quelli per il rilevamento di minacce o l’autenticazione biometrica) devono adattarsi a minacce in continua evoluzione. In questo articolo esamineremo cos’è l’“AI degenerativa” e perché avviene, con un focus particolare sui **rischi per la sicurezza informatica**. Illustreremo esempi pratici, e proporremo strategie per prevenire o mitigare la degenerazione dei modelli. Infine, esamineremo trend emergenti – come l’**AI auto-rigenerativa**, l’**apprendimento continuo** e il **monitoraggio automatico del drift** – che mirano a mantenere i modelli IA sempre efficaci e resilienti.

## Cosa si intende per “AI degenerativa”?

Con *AI degenerativa* intendiamo il **degrado graduale delle performance di un modello IA nel tempo**, dovuto a mutate condizioni rispetto a quelle in cui il modello è stato inizialmente addestrato. Diversi fenomeni contribuiscono a questa degenerazione delle prestazioni:

* **Data Drift (deriva dei dati):** Si verifica quando **la distribuzione dei dati in ingresso cambia rispetto a quella dei dati di addestramento**, pur restando invariata la relazione concettuale tra input e output. In pratica, le caratteristiche statistiche dei dati che il modello vede in produzione divergono da quelle del dataset originale. Questo può accadere, ad esempio, se emergono nuovi tipi di traffico di rete, nuovi formati di log o cambiamenti nelle fonti dei dati. Il risultato è che il modello diventa meno accurato o commette più errori perché si trova ad operare su dati “diversi” da quelli per cui era stato ottimizzato.
* **Concept Drift (deriva del concetto):** Rappresenta un cambiamento nel **rapporto funzionale tra input e output**, ovvero nel concetto stesso che il modello deve apprendere. In questo caso, i **dati di addestramento diventano rapidamente obsoleti** perché cambia la realtà sottostante. Ad esempio, in un contesto di sicurezza informatica, ciò accade quando **mutano le definizioni di ciò che è considerato “maligno” o “benigno”**: nuove vulnerabilità e nuove tecniche di attacco possono trasformare istanze prima considerate innocue in minacce reali. Un modello addestrato su vecchie minacce potrebbe non riconoscere quelle nuove, a meno di non essere aggiornato. Il concept drift infrange l’assunto che i dati seguano la stessa distribuzione nel tempo (assunto i.i.d.) e rende **insostenibile l’uso a lungo termine di modelli statici** in ambienti dinamici.
* **Attacchi adversariali (evasion):** Si tratta di **attacchi intenzionali** volti a ingannare il modello fornendogli in input dati appositamente manipolati. Anche **perturbazioni minime e impercettibili dei dati di input possono compromettere le predizioni di un modello** di machine learning. In ambito cybersecurity, aggressori esperti possono sfruttare questa vulnerabilità: ad esempio, è stato dimostrato che basta aggiungere pochi byte di “rumore” ad un flusso di rete malevolo per far sì che passi inosservato da vari classificatori di botnet basati su ML. Allo stesso modo, piccoli cambiamenti ad un’immagine (es. ad un volto) possono ingannare un sistema di riconoscimento facciale, inducendolo a classificazioni errate. Gli attacchi adversariali di *evasione* agiscono tipicamente nella fase di **inference** (dopo l’addestramento), modificando gli input per causare errori di classificazione senza alterare il modello stesso.
* **Contaminazione del dataset (Data Poisoning):** In questo scenario, l’attacco avviene **durante la fase di addestramento o aggiornamento**. Un avversario riesce a inserire dati manipolati o etichettati in modo scorretto nel dataset di training, compromettendo così il modello a monte. Questi **attacchi di poisoning**, detti anche di contaminazione, puntano a far apprendere al modello comportamenti errati: ad esempio facendo sì che etichetti come “sicuro” qualcosa di pericoloso se presenta uno specifico pattern nascosto. Poiché spesso le modifiche sono sottili, può essere **difficile per un umano accorgersi che il dataset è stato avvelenato**. Un caso celebre è quello del chatbot Tay di Microsoft nel 2016, “addestrato” dai troll su Twitter con frasi offensive: il risultato fu un modello degenerato che produceva output inaccettabili, esito di un tipico attacco di contaminazione dei dati di apprendimento.
* **Mancanza di aggiornamenti (modelli obsoleti):** Anche senza attacchi espliciti, un modello può degenerare semplicemente perché **non viene mai aggiornato o ritarato**. Col passare del tempo il mondo cambia: compaiono nuovi tipi di malwar...
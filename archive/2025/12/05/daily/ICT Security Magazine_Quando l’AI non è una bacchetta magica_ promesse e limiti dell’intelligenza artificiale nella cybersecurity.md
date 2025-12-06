---
title: Quando l’AI non è una bacchetta magica: promesse e limiti dell’intelligenza artificiale nella cybersecurity
url: https://www.ictsecuritymagazine.com/articoli/ai-limiti/
source: ICT Security Magazine
date: 2025-12-05
fetch_date: 2025-12-06T03:12:01.711262
---

# Quando l’AI non è una bacchetta magica: promesse e limiti dell’intelligenza artificiale nella cybersecurity

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

![Professor Marco Mellia durante il suo intervento al Forum ICT Security 2025 sulle potenzialità e i limiti dell’AI e degli agenti autonomi in cybersecurity.](https://www.ictsecuritymagazine.com/wp-content/uploads/untitled-design-2_HGkIJaQd.png)

# Quando l’AI non è una bacchetta magica: promesse e limiti dell’intelligenza artificiale nella cybersecurity

A cura di:[Marco Mellia](#molongui-disabled-link)  Ore 5 Dicembre 20253 Dicembre 2025

*Al Forum ICT Security 2025, il professor Marco Mellia del Politecnico di Torino ha sfatato alcuni miti sull’AI applicata alla sicurezza informatica, illustrando però le reali potenzialità degli agenti autonomi*

Nel contesto della 23a edizione del [Forum ICT Security](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025), tenutosi a Roma il 19 e 20 novembre 2025, l’intervento “AI, LLM, Agentic AI e Cyber Security: Potenzialità e limiti” del professor Marco Mellia ha rappresentato uno dei momenti più illuminanti dell’evento. Docente ordinario presso il Dipartimento di Automatica e Informatica del Politecnico di Torino e co-fondatore di Ermes Cyber Security, il relatore ha affrontato con rigore scientifico e schiettezza divulgativa uno dei temi più dibattuti del momento: quanto c’è di reale dietro la “bacchetta magica” dell’intelligenza artificiale applicata alla cybersecurity?

L’intervento si è articolato in due parti distinte. La prima, che l’esperto ha eloquentemente definito “il pericolo dello zucchero”, ha preso di mira le promesse mirabolanti di alcuni sistemi AI che sostengono di poter classificare il traffico di rete cifrato. La seconda parte ha invece esplorato un territorio più promettente: quello degli agenti AI autonomi applicati all’analisi forense.

# Prima parte: lo zucchero che nasconde l’amaro

Il punto di partenza dell’analisi è stato un fenomeno che chi lavora sulla frontiera della ricerca osserva con crescente perplessità: l’emergere di soluzioni commerciali e paper accademici che promettono di “vedere” all’interno delle comunicazioni cifrate grazie all’intelligenza artificiale. Come ha osservato ironicamente lo speaker, “arriva l’AI e ti permette di risolvere problemi che fino a ieri erano impossibili, per esempio classificare il traffico cifrato”. Un’affermazione che, a prima vista, sa di bacchetta magica.

![](https://www.ictsecuritymagazine.com/wp-content/uploads/Lillusione-della-22magia22-AI-per-classificare-il-traffico-cifrato.png)

L’illusione della “magia” AI per classificare il traffico cifrato

L’approccio utilizzato da questi sistemi è mutuato dal successo ottenuto in altri settori, in particolare dal Natural Language Processing. L’esperto ha citato BERT, il modello sviluppato da Google per la traduzione automatica, come esempio paradigmatico di *representation learning*: si allena una rete neurale a “leggere” enormi quantità di testo, creando una rappresentazione interna che può poi essere riutilizzata per compiti specifici come traduzioni o correzioni.

Il ragionamento dei ricercatori è stato apparentemente lineare: “Se una macchina di questo tipo è in grado di imparare tutte le lingue, vuoi che non sia in grado di imparare anche i pacchetti di rete?” È nato così l’approccio del *masked auto-encoder* applicato al traffico Internet: si nasconde parte di un pacchetto e si allena il modello a ricostruire la parte mancante. Una volta ottenuta questa rappresentazione, la si dovrebbe poter usare per classificare il traffico.

## Risultati troppo dolci per essere veri

I risultati pubblicati sono effettivamente impressionanti. Il relatore ha mostrato come lavori apparsi alle più prestigiose conferenze del settore — KDD, The Web Conference, AAAI, IEEE S&P — riportino accuratezze del 95-98% nel classificare traffico cifrato proveniente da 120 siti web diversi. “Fa venire un po’ i brividi”, ha commentato, “perché se tutto è cifrato, come diavolo fai a dirmi se quello che c’è dentro è di Facebook o del Corriere?”

Ed è qui che entra in gioco lo scetticismo del ricercatore. Il docente torinese ha invitato la platea a ricordare tre nomi: Rivest, Shamir e Adleman — i padri dell’algoritmo RSA che rende possibili le transazioni bancarie sicure su Internet. “Se noi ci fidiamo di loro”, ha argomentato, “quello che ci hanno detto gli altri non potrebbe funzionare.”

![](https://www.ictsecuritymagazine.com/wp-content/uploads/I-padri-della-crittografia-moderna-Rivest-Shamir-e-Adleman.-22O-ci-fidiamo-di-loro22-700x394.jpg)

I padri della crittografia moderna: Rivest, Shamir e Adleman. “O ci fidiamo di loro?”

## Le insidie metodologiche

L’analisi critica ha rivelato tre insidie fondamentali nei lavori esaminati. La prima è di natura concettuale: il processo di *masked auto-encoding* presuppone di poter ricostruire una sequenza a partire da un’altra. Ma con il traffico cifrato si lavora con sequenze casuali: “Come fai da una sequenza casuale a ricostruire un’altra sequenza casuale? La giusta sequenza casuale non è possibile. Checché ne dica chi gioca al lotto.”

La seconda insidia riguarda la metodologia sperimentale. Chi lavora con il *machine learning* sa che bisogna separare rigorosamente i dati di training da quelli di test. Ma lo speaker ha scoperto che molti lavori hanno commesso un errore cruciale: hanno inserito lo stesso flusso di dati sia nel training che nel test set. Il risultato è che i modelli hanno imparato degli *shortcut* — scorciatoie che non rappresentano realmente il problema. “Il m...
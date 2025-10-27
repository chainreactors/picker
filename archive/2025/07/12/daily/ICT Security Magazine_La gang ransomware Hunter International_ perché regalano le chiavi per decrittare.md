---
title: La gang ransomware Hunter International: perché regalano le chiavi per decrittare
url: https://www.ictsecuritymagazine.com/articoli/hunter-international/
source: ICT Security Magazine
date: 2025-07-12
fetch_date: 2025-10-06T23:53:52.399946
---

# La gang ransomware Hunter International: perché regalano le chiavi per decrittare

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

!['evoluzione tattica di Hunter International da ransomware tradizionale a data extortion stealth mode](https://www.ictsecuritymagazine.com/wp-content/uploads/freepik__a-security-expert-analyzing-a-computer-system-infe__68123.jpeg)

# La gang ransomware Hunter International: perché regalano le chiavi per decrittare

A cura di:[Fabrizio Baiardi](#molongui-disabled-link)  Ore 11 Luglio 202511 Luglio 2025

Recenti notizie di threat intelligence[[1]](#_ftn1) parlano di una interessante evoluzione del fenomeno del ransomware: le gang non sono più interessate a criptare le info ed addirittura regalano le chiavi per decrittare. Ricordando il ben noto, ed inutile, “Timeo danaos et dona ferentes” questo contributo vuole segnalare come questa sia, in fondo, una pessima notizia e come sia in qualche modo una risposta del mondo criminale ad alcune proposte legislative che sono state approvate da poco o ancora sotto discussione che di fondo vogliono rendere illegale e quindi impedire il pagamento di un riscatto ed obbligano a rendere nota una intrusione ransomware che abbia colpito una organizzazione[[2]](#_ftn2).

## Il caso Hunter International

La gang che ha detto di non essere interessata a criptare le informazioni è Hunter International, una gang criminale apparsa nell’ottobre 2023 con un attacco ad una azienda inglese e poco dopo con uno in Germania. Un analisi dei malware utilizzati da questo gruppo fa pensare che sia un nuovo brand per il gruppo prima noto come Hive e che all’inizio del 2023 è stato bersaglio di azioni di polizia che hanno smantellato l’infrastruttura d’attacco, o botnet, che gli affiliati ad Hive utilizzavano nelle loro intrusioni, vedi fig.1

![ransomware hunter](https://www.ictsecuritymagazine.com/wp-content/uploads/fig11c.png)

Ovviamente smantellare una infrastruttura di attacco è più semplice che smantellare e rendere inoffensivo un gruppo criminale perché, se i membri e gli affiliati del gruppo sono in libertà possono in maniera relativamente semplice ricreare l’infrastruttura e lanciare nuovi attacchi. Nel suo blog, vedi fig. 2, Hunter International smentisce di essere un nuovo brand per una vecchia gang ed afferma di aver solo comprato il malware che Hive utilizzava e che hanno migliorato perché era poco affidabile (in fondo una buona notizia, anche il malware ha delle vulnerabilità che non vengono scoperte immediatamente).

![](https://www.ictsecuritymagazine.com/wp-content/uploads/hunt.png)

Fig. 2 Post su blog di Hunter International

## Tecniche e strumenti

Una caratteristica interessante delle nuove versioni prodotte dalla gang e che criptano comunque le informazioni della vittima, è che non creano un messaggio da lasciare sul sistema attaccato e criptato con le istruzioni da seguire per pagare il riscatto ed ottenere la chiave. Questo evidenzia come la gang criminale non sia interessata a pubblicizzare intrusione e cerchi di ridurre il numero di persone informate dell’intrusione. Inoltre, alcuni degli altri strumenti sviluppati dalla gang e messi a disposizione degli affiliati permettono di ricostruire l’organigramma aziendale con nomi, coordinate e ruoli della gerarchia aziendale. In questo modo l’affiliato sa con chi deve parlare per segnalare l’intrusione e chiedere il riscatto.

Un altro strumento che l’affiliato può utilizzare permette di creare un account su un sito nel dark web gestito dalla gang dove si possono memorizzare i dati esfiltrati dal sistema attaccato. Concedendo l’accesso al sito ad una persona dell’organizzazione attaccata è possibile per l’organizzazione esaminare alcune delle informazioni esfiltrate e che verranno rese pubbliche se l’organizzazione non paga il riscatto richiesto.

Quante e quali informazioni la vittima può visualizzare è deciso dall’affiliato che ha eseguito l’attacco guidato da una interfaccia grafica. Se l’organizzazione vittima decide di pagare, trova anche una interfaccia grafica che semplifica il pagamento. Per ostacolare il tracciamento dei pagamenti in criptovalute, per ogni pagamento viene generato un nuovo indirizzo che lo riceve. Questo prova come le gang criminali hanno capito che anche i pagamenti in criptovalute possano essere tracciati.

Dopo il pagamento, la vittima riceve la chiave per decrittare e può cancellare i dati esfiltrati come in fig. 3.

![](https://www.ictsecuritymagazine.com/wp-content/uploads/fff.png)

Fig. 3

## Evoluzione delle tattiche

Fin qui siamo di fronte ad una evoluzione molto semplice e non molto significativa. Ma poi Hunter International annuncia di non essere più interessata al ransomware che sta diventando sempre più pericoloso e meno redditizio. E qui vediamo una accelerazione di tendenze già in atto[[3]](#_ftn3), che riemerge dopo qualche tempo indubbiamente anche a causa sia delle azioni delle varie polizie per smantellare le infrastrutture di attacco che delle leggi in discussione per vietare o addirittura punire il pagamento del riscatto.

Inoltre, poco dopo l’annuncio appare una nuova piattaforma di questo gruppo, World Leaks, che viene offerta agli affiliati della gang insieme ad uno strumento per esfiltrare informazioni. I due strumenti integrati segnano il passaggio dalla doppia estorsione, ti cripto i dati e li rubo per minacciarti di renderli pubblici, ad una estorsion...
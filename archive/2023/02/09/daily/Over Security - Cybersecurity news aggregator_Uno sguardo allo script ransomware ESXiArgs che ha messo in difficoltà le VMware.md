---
title: Uno sguardo allo script ransomware ESXiArgs che ha messo in difficoltà le VMware
url: https://www.insicurezzadigitale.com/uno-sguardo-allo-script-ransomware-esxiargs-che-ha-messo-in-difficolta-le-vmware/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-09
fetch_date: 2025-10-04T06:08:56.804619
---

# Uno sguardo allo script ransomware ESXiArgs che ha messo in difficoltà le VMware

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

[Analisi](https://insicurezzadigitale.com/category/analisi/)

# Uno sguardo allo script ransomware ESXiArgs che ha messo in difficoltà le VMware

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
8 Febbraio 2023

![](https://insicurezzadigitale.com/wp-content/uploads/2023/02/VMware-1024x512.jpg)

Si parla di:

Toggle

* [Lo script ransomware ESXiArgs da vicino](#Lo_script_ransomware_ESXiArgs_da_vicino)
* [Per concludere](#Per_concludere)

Essendo notizia ormai di ieri, la messa a disposizione su GitHub, da parte della CISA, del tool di ripristino per le vittime del recente ransomware ESXiArgs, mi sento tranquillo nel descrivere in maniera diretta come agisce lo script malevolo che sta infettando il mondo delle **virtual machine VMware non adeguatamente aggiornate**.

## Lo script ransomware ESXiArgs da vicino

Come detto dunque la Cybersecurity & Infrastructure Security Agency statunitense ha sviluppato un [tool](https://github.com/cisagov/ESXiArgs-Recover) in aiuto alle vittime che hanno subito l’infezione da **ransomware ESXiArgs** negli ultimi giorni.

Già nei miei commenti riportati nell’analisi di domenica 5 febbraio su [CyberSecurity360](https://www.cybersecurity360.it/nuove-minacce/attacco-hacker-globale-cosa-sappiamo-degli-impatti-in-italia/), proprio per fare chiarezza su questa campagna malevola in atto, avevo accennato al fatto che gli attacchi fossero mirati a rendere non operativa in maniera rapida una virtual machine (VM) VMware ESXi, utilizzando la crittografia unicamente per alcuni file di configurazione della VM, essenziali per la sua operatività, ma **senza intaccare il completo filesystem** che conterrebbe anche i “dati utente” interni al software che la VM tiene in piedi.

Questa affermazione oggi viene accompagnata dall’analisi dello script che svolge proprio questa attività malevola, negli attacchi descritti.

Tengo a precisare che faccio solo oggi questa analisi benché lo script malevolo sia disponibile già da giorni, perché pur essendo nota la procedura di ripristino, senza un tool che la automatizzasse, potrebbe risultare difficoltosa per alcuni da mettere in pratica. Il tool facilita il ripristino e dunque rende questa analisi decisamente fuori rischio di sfruttamento malevolo.

Tralasciando i dettagli interni al ransomware, come la pulizia dei log e eventuali sistemazioni di permessi di determinati file, così come lo shutdown della VM e la compromissione delle righe crontab (per la pianificazione dei processi), vorrei concentrarmi sulla parte centrale, quella che riguarda proprio la crittografia.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2023/02/Screenshot_2023-02-08_10_59_41-1024x328.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2023/02/Screenshot_2023-02-08_10_59_41.png)

In questa immagine ho selezionato il blocco di codice che applica la crittografia per compromettere la funzionalità della virtual machine.

Come si può notare lo script interviene con un ciclo `for`, più esterno, con il quale cerca i volumi di storage della macchina. Per ogni volume trovato effettua un altro ciclo `for` con il quale cerca i files presenti all’interno di quel volume.

La particolarità di questo ransomware e se vogliamo anche la sua semplicità o per meglio dire, più bassa pericolosità rispetto altri, sta proprio qui, in questo ciclo for più interno. Per bassa pericolosità intendo unicamente il fatto che l’impatto della sua azione è più limitato.

Infatti questa ricerca di files viene fatta, ma con una condizione. Vengono infatti cercati (all’interno del dato volume), tutti i file che rispondono a questo criterio:

```
find "/vmfs/volumes/$volume/" -type f -name "*.vmdk" -o -name "*.vmx" -o -name "*.vmxf" -o -name "*.vmsd" -o -name "*.vmsn" -o -name "*.vswp" -o -name "*.vmss" -o -name "*.nvram" -o -name "*.vmem"
```

Questo è un criterio di ricerca che, partendo dal nome del file, seleziona quelli che riportano le stringhe elencate, ovvero **tipi specifici di estensioni** (.vmdk, .vmx, .vmxf ecc).

Una ricerca di questo tipo, esclude ovviamente una marea di altri file che potenzialmente sono contenuti nei volumi della virtual machine, come per esempio tutti i file di sistema oppure tutti quelli di produzione, personali, di software e qualsiasi altra cosa che non abbia una di quelle estensioni.

Per ognuno di questi file trovati, lo script esegue poi la crittografia con le istruzioni successive che stanno però, come vediamo, tutte all’interno del ciclo for più interno.

## Per concludere

In definitiva questo ci fa capire come funziona questa nuova tipologia di ransomware, cosa compromette e come. Ad ogni modo il consiglio è sempre quello di evitare di avere sistemi VMware infrastrutturali esposti ad Internet. Nel caso sia strettamente necessario esporli ad Internet, averne cura negli aggiornamenti per coprire in maniera celere eventuali vulnerabilità (questa era di febbraio 2021, e successive nel 2022).

Inoltre se proprio si è caduti vittima di attacco, infettati da ESXiArgs, evitare l’eccessivo panico, proprio perché il sistema è ripristinabile e non impatta sul contenuto produttivo della virtual machine presa di mira.

##### < tags />

[ESXiArgs](https://insicurezzadigitale.com/tag/esxiargs/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[ransomware](https://insicurezzadigitale.com/tag/ransomware/)[vmware](https://insicurezzadigitale.com/tag/vmware/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Uno+sguardo+allo+script+ransomware+ESXiArgs+che+ha+messo+in+difficolt%C3%A0+le+VMware&url=https://insicurezzadigitale.com/uno-sguardo-allo-script-ransomware-esxiargs-che-ha-messo-in-difficolta-le-vmware/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/uno-sguardo-allo-script-ransomware-esxiargs-che-ha-messo-in-difficolta-le-vmware/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/uno-sguardo-allo-script-ransomware-esxiargs-che-ha-messo-in-difficolta-le-vmware/&title=Uno+sguardo+allo+script+ransomware+ESXiArgs+che+ha+messo+in+difficolt%C3%A0+le+VMware)

[== articolo precedente ==](https://insicurezzadigitale.com/ion-group-e-un-attacco-di-lockbit-da-non-sottovalutare/)

[:: articolo successivo ::](https://insicurezzadigitale.com/a...
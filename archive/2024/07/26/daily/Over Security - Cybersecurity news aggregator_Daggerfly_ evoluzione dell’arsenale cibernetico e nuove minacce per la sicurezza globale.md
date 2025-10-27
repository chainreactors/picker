---
title: Daggerfly: evoluzione dell’arsenale cibernetico e nuove minacce per la sicurezza globale
url: https://www.insicurezzadigitale.com/daggerfly-evoluzione-dellarsenale-cibernetico-e-nuove-minacce-per-la-sicurezza-globale/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-26
fetch_date: 2025-10-06T17:43:55.555215
---

# Daggerfly: evoluzione dell’arsenale cibernetico e nuove minacce per la sicurezza globale

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

[Incidenti e Violazioni](https://insicurezzadigitale.com/category/incidenti-e-violazioni/)

# Daggerfly: evoluzione dell’arsenale cibernetico e nuove minacce per la sicurezza globale

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
25 Luglio 2024

![](https://insicurezzadigitale.com/wp-content/uploads/2024/07/1721812071-1024x585.webp)

Si parla di:

Toggle

* [Nuovi strumenti e aggiornamenti](#Nuovi_strumenti_e_aggiornamenti)
* [Attribuzione e infrastruttura condivisa](#Attribuzione_e_infrastruttura_condivisa)
* [Nuova backdoor per Windows: Trojan.Suzafk](#Nuova_backdoor_per_Windows_TrojanSuzafk)
* [Capacità e piattaforme target](#Capacita_e_piattaforme_target)

Il gruppo di spionaggio Daggerfly, noto anche come Evasive Panda e Bronze Highland, ha aggiornato il suo arsenale cibernetico in risposta alla divulgazione pubblica delle sue varianti di malware più vecchie. Secondo il rapporto del Symantec Threat Hunter Team, questi aggiornamenti sono stati osservati in attacchi contro organizzazioni a Taiwan e una ONG statunitense con sede in Cina, suggerendo attività di spionaggio interno.

## **Nuovi strumenti e aggiornamenti**

Tra le nuove aggiunte all’arsenale di Daggerfly si evidenziano:

1. **Nuova famiglia di malware basata su MgBot:**
   * Framework modulare che consente funzionalità avanzate e flessibili.
2. **Nuova versione del Macma macOS backdoor:**
   * Attribuita a Daggerfly da Symantec.
   * Documentata inizialmente da Google nel 2021, ma in uso dal 2019.
   * Distribuita tramite attacchi “watering hole” a Hong Kong, sfruttando la vulnerabilità di escalation dei privilegi CVE-2021-30869.
   * Funzionalità: fingerprinting del dispositivo, esecuzione di comandi, cattura dello schermo, keylogging, cattura audio, caricamento e download di file.
   * Aggiornamenti recenti: dati di configurazione del modulo principale differenti, aggiornamenti incrementali delle funzionalità, nuovi moduli e percorsi di file, miglioramenti nel debug logging, nuova logica per la raccolta dell’elenco dei file di sistema basata sull’utility Linux/Unix “Tree”, e un nuovo file di configurazione param2.ini per la funzione “autoScreenCaptureInfo”.

## **Attribuzione e infrastruttura condivisa**

* **Macma** è stato collegato a un server di comando e controllo (C&C) utilizzato anche da un dropper MgBot.
* Condivisione di infrastruttura e codice tra Macma e altri strumenti di Daggerfly, compresi threading, notifiche di eventi e astrazioni indipendenti dalla piattaforma.

## **Nuova backdoor per Windows: Trojan.Suzafk**

* Documentato da ESET nel marzo 2024 come Nightdoor (alias NetMM).
* Sviluppato utilizzando la stessa libreria condivisa di MgBot e Macma.
* Backdoor multi-stadio che utilizza TCP o OneDrive per il C&C.
* Carica Engine.dll e MeitUD.exe, quest’ultimo è un’applicazione legittima utilizzata per la persistenza e il caricamento del payload.
* Include codice dal progetto al-khaser per il rilevamento di macchine virtuali e ambienti di analisi malware.
* Crea cartelle specifiche e memorizza dati di configurazione di rete criptati con XOR utilizzando la chiave 0x7A.
* Esegue comandi come ipconfig, systeminfo, tasklist e netstat tramite una shell cmd.exe.

## **Capacità e piattaforme target**

* Daggerfly è in grado di prendere di mira principali sistemi operativi, inclusi Windows, macOS, Linux e Android.
* Capacità aggiuntive: trojanizzazione di APK Android, intercettazione di messaggi SMS e richieste DNS, sviluppo di malware per Solaris OS.

**Daggerfly** continua ad evolversi, sviluppando e aggiornando strumenti sofisticati per mantenere la sua efficacia in operazioni di spionaggio cibernetico su più piattaforme. La sua abilità di adattarsi e migliorare i suoi malware rappresenta sempre una minaccia significativa per la sicurezza informatica a livello globale.

##### < tags />

[cybercrime](https://insicurezzadigitale.com/tag/cybercrime/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[malware](https://insicurezzadigitale.com/tag/malware/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Daggerfly%3A+evoluzione+dell%26%238217%3Barsenale+cibernetico+e+nuove+minacce+per+la+sicurezza+globale&url=https://insicurezzadigitale.com/daggerfly-evoluzione-dellarsenale-cibernetico-e-nuove-minacce-per-la-sicurezza-globale/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/daggerfly-evoluzione-dellarsenale-cibernetico-e-nuove-minacce-per-la-sicurezza-globale/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/daggerfly-evoluzione-dellarsenale-cibernetico-e-nuove-minacce-per-la-sicurezza-globale/&title=Daggerfly%3A+evoluzione+dell%26%238217%3Barsenale+cibernetico+e+nuove+minacce+per+la+sicurezza+globale)

[== articolo precedente ==](https://insicurezzadigitale.com/nullbulge-un-po-di-attivismo-tra-codice-di-malware-e-infostealer/)

[:: articolo successivo ::](https://insicurezzadigitale.com/lintervento-di-israele-nella-causa-whatsapp-contro-nso-unanalisi-dettagliata/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/daggerfly-evoluzione-dellarsenale-cibernetico-e-nuove-minacce-per-la-sicurezza-globale/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *Daggerfly: evoluzione dell’arsenale cibernetico e nuove minacce per la sicurezza globale*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=Daggerfly:+evoluzione+dell’arsenale+cibernetico+e).
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

##### (in)sicurezza...
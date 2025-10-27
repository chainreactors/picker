---
title: AsyncRAT e il panorama delle minacce informatiche in Italia – Evoluzione del cybercrime
url: https://www.ictsecuritymagazine.com/articoli/asyncrat-italia-cybercrime/
source: ICT Security Magazine
date: 2025-05-31
fetch_date: 2025-10-06T22:28:38.311012
---

# AsyncRAT e il panorama delle minacce informatiche in Italia – Evoluzione del cybercrime

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

![AsyncRAT e il Panorama delle Minacce Informatiche in Italia, cybercrime](https://www.ictsecuritymagazine.com/wp-content/uploads/asyncrat-un-trojan-ad-accesso-remoto-rat__43536.jpeg)

# AsyncRAT e il panorama delle minacce informatiche in Italia – Evoluzione del cybercrime

A cura di:[Redazione](#molongui-disabled-link)  Ore 30 Maggio 202530 Maggio 2025

L’evoluzione del cybercrime contemporaneo ha assistito all’emergere di sofisticate minacce informatiche caratterizzate da capacità di evasione avanzate e tecniche di persistenza innovative come AsyncRAT, un trojan ad accesso remoto (RAT) che prende di mira i sistemi Windows e che è stato identificato per la prima volta nel 2019: esfiltrava informazioni di sistema verso un server di comando e controllo con capacità di eseguire vari comandi, come il download di plugin, la terminazione di processi, l’acquisizione di *screenshot* e l’auto-aggiornamento.

Nel contesto geopolitico italiano, questo malware ha assunto connotazioni particolarmente allarmanti, manifestandosi attraverso campagne di distribuzione orchestrate con metodologie sempre più raffinate e ricorrendo a veicoli di diffusione che sfruttano l’affidabilità percepita delle comunicazioni istituzionali.

## Caratteristiche tecniche e genealogia malware

#### Architettura e funzionalità *core*

AsyncRAT ha un antenato comune con QuasarRAT ed è spesso associato a RevengeRAT. Tuttavia, mentre questi RAT condividono alcune somiglianze, sono significativamente divergenti. AsyncRAT è spesso associato a una famiglia correlata di RAT chiamata “VenomRAT”.

I due RAT condividono molto codice e somiglianze, ed entrambi hanno radici in QuasarRAT. La natura open-source di questo strumento ha facilitato la proliferazione di varianti personalizzate, contribuendo alla creazione di un ecosistema diversificato che sfida le capacità di rilevamento tradizionali.

Il malware manifesta capacità operative multisfaccettate che includono: keylogging, registrazione audio/video, furto di informazioni, controllo desktop remoto, recupero password, lancio di shell remota, webcam, iniezione di payload, tra altre funzioni. Queste caratteristiche conferiscono agli operatori malevoli un controllo pressoché totale sui sistemi compromessi, trasformando le macchine infette in nodi di una botnet sotto controllo remoto.

#### Implementazione delle Tattiche, Tecniche e Procedure (TTPs)

L’analisi delle metodologie implementate da AsyncRAT rivela un’aderenza sistematica al framework MITRE ATT&CK, con particolare enfasi su: Scheduled Task/Job: Scheduled Task (T1053.005), Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder (T1547.001), Virtualization/Sandbox Evasion (T1497), Exfiltration Over C2 Channel (T1041), Input Capture: Keylogging (T1056.001).

### Il panorama delle minacce in Italia: analisi quantitativa

#### Prevalenza e distribuzione geografica

Nel corso del 2024, il CERT-AGID ha individuato e contrastato in totale 1767 campagne malevole e condiviso 19.939 IoC. In totale le famiglie malware individuate sono state 69. Dei sample analizzati, per il **67% si tratta di infostealer, mentre per il 33% di RAT**. All’interno di questo ecosistema di minacce, **AsyncRat figura nella top-ten dei malware più diffusi**, confermando la sua rilevanza strategica nel panorama del cybercrime italiano.

L’Italia emerge tra i paesi maggiormente bersagliati a livello globale: L’Italia, oltre a essere il quinto Paese più bersagliato dai malware nel 2024, ha registrato a dicembre la terza percentuale più alta di rilevamenti di malware, dopo Emirati Arabi Uniti e Singapore. Questo posizionamento evidenzia la particolare vulnerabilità del tessuto digitale nazionale alle minacce informatiche contemporanee.

#### Evoluzione temporale delle campagne

L’analisi longitudinale delle attività malevole mostra tendenze preoccupanti: In Italia, anche nel 2025 FakeUpdate continua ad essere la minaccia più presente, anche se con un impatto leggermente inferiore a quanto rilevato a fine 2024. Tuttavia, FakeUpdates ha portato all’installazione di Trojan ad accesso remoto come AsyncRAT, attualmente al nono posto, dimostrando l’interconnessione delle [diverse famiglie di malware](https://www.ictsecuritymagazine.com/articoli/breve-storia-dei-malware-levoluzione-delle-specie-dalle-origini-ai-giorni-nostri/) nel panorama delle minacce.

## Innovazioni tecnologiche e metodologie di evasione

#### Implementazione della steganografia

Una delle evoluzioni più significative nell’ambito della distribuzione di AsyncRAT in territorio italiano è rappresentata dall’adozione della steganografia come metodologia di occultamento. La Steganografia è una tecnica che permette di nascondere un’informazione all’interno di un’altra considerata come principale e che funga da veicolo. Quest’ultima, che si può presentare sotto forma di un’immagine, un file audio, un testo, un eseguibile o altro viene leggermente modificata in modo tale che la modifica stessa sia praticamente invisibile per un utente umano e contenga l’informazione da nascondere.

Il CERT-AGID ha documentato l’utilizzo di queste tecniche avanzate: Si chiama AsyncRAT il nuovo malware che ha messo l’Italia nel mirino: si diffonde utilizzando la tecnica della steganografia per nascondersi dentro f...
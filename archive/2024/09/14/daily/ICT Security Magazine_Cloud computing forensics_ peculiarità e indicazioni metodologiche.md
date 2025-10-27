---
title: Cloud computing forensics: peculiarità e indicazioni metodologiche
url: https://www.ictsecuritymagazine.com/articoli/cloud-computing-forensics-peculiarita-e-indicazioni-metodologiche/
source: ICT Security Magazine
date: 2024-09-14
fetch_date: 2025-10-06T18:32:45.171012
---

# Cloud computing forensics: peculiarità e indicazioni metodologiche

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/cloud-security-forensics.jpg)

# Cloud computing forensics: peculiarità e indicazioni metodologiche

A cura di:[Vincenzo Calabrò](#molongui-disabled-link)  Ore 13 Settembre 202416 Ottobre 2024

Questo articolo inaugura una serie dedicata alla Cloud Computing Forensics, un tema sempre più rilevante in un’era in cui il cloud è diventato parte integrante delle operazioni quotidiane di ogni organizzazione. In questo primo articolo, ci concentreremo sulle peculiarità tecniche del cloud e sulla metodologia di investigazione digitale, delineando le sfide e i rischi legati a questo ambiente. Nel prossimo articolo, “[Cloud Computing Forensics: elementi di data security e protection](https://www.ictsecuritymagazine.com/articoli/cloud-computing-data-security/)“, esploreremo i principali aspetti di sicurezza dei dati e le tecniche per garantire la protezione delle informazioni nel contesto cloud.

## Introduzione

Il Cloud computing è il principale modello di deployment dei servizi online, applicazioni, risorse e dati; è adottato da tutte le organizzazioni, indipendentemente dal settore, dalle dimensioni o dalle esigenze di calcolo e/o di storage. Di conseguenza, è cresciuto il contezioso avente ad oggetto il cloud, ovvero i servizi e i dati in cloud. La specificità, la complessità e l’eterogeneità dell’ambiente cloud, rispetto agli ambiti on-premise, richiedono un approccio e un metodo di conduzione delle indagini digitali ad hoc. Di conseguenza, è cresciuto il contezioso avente ad oggetto il cloud, ovvero i servizi e i dati in cloud. Le principali controversie, fin qui registrate, hanno riguardato:

* **i termini e/o le condizioni di servizio.** Spesso i contratti di fornitura dei servizi in cloud sono generici e lacunosi, in particolar modo nella definizione dei service-level agreement (SLA), oppure non sono conformi alle normative e regolamenti vigenti, per esempio in tema di cybersecurity, continuità operativa e privacy, e ciò genera il contenzioso in fase di esecuzione del contratto;
* **la violazione alla sicurezza e/o alla privacy dei dati o dei servizi**. Il cloud computing è indubbiamente più esposto a questa tipologia di minacce, per cui è necessario conoscere le tecniche di indagine specifiche per le violazioni che hanno compromesso la confidenzialità, l’integrità e la disponibilità dei dati o dei servizi in cloud;
* **lo sfruttamento della capacità di calcolo e/o memorizzazione**. La disponibilità elevata di risorse offerte dal cloud computing è divenuto un obiettivo dei criminali informatici per perpetrare attività illecite o sfruttare la capacità di calcolo a carico di altri.

La specificità, la complessità e l’eterogeneità dell’ambiente cloud, rispetto agli ambiti on-premise, richiedono un approccio e un metodo di conduzione delle indagini digitali ad hoc. In questo articolo provo a evidenziare le peculiarità tecniche e descrivere una metodologia conforme agli standard di settore e agli obiettivi prescritti dalle norme vigenti.

## Cloud computing

### Definizione e proprietà funzionali

Il termine cloud computing indica una modalità di erogazione di servizi ICT offerti da alcuni operatori (provider) a una moltitudine di utenti (user) in modalità on demand e pay-per-use. Questi servizi sono erogati mediante infrastrutture hardware e software di proprietà dei provider o della stessa organizzazione senza una gestione attiva diretta da parte dell’utente; questi ultimi accedono attraverso le tecnologie e i protocolli di rete.

Tipicamente un sistema cloud si compone di uno o più data center organizzati secondo un’architettura distribuita. Il principio cardine del cloud computing è la virtualizzazione: tutte le risorse di elaborazione, memorizzazione e trasmissione sono virtuali, ovvero ottenute sfruttando tecniche di emulazione implementate su risorse fisiche. Un tipico sistema cloud utilizza i gestori delle risorse (Hypervisor per la distribuzione di macchine virtuali, Container Engine per la distribuzione dei servizi o microservizi), che hanno il compito di amministrare le risorse fisiche dell’infrastruttura, allocandole dinamicamente alle diverse risorse virtualizzate (macchine virtuali o container) che condividono tale infrastruttura.

I principali [vantaggi del cloud computing](https://www.scirp.org/journal/paperinformation?paperid=124299) non si limitano solo alla riduzione dei tempi e dei costi, ma anche all’agilità e alla scalabilità. In particolare, i sistemi cloud sono caratterizzati da proprietà funzionali con un impatto significativo sulle investigazioni digitali:

* **Distribuzione geografica delle risorse**: i data center che ospitano l’hardware di un sistema cloud sono organizzati secondo un’architettura distribuita, ovvero sono partizionate su un set di siti indipendenti, ubicati a distanza tra di loro. Di conseguenza, le risorse e i dati relativi ad uno specifico utente possono essere ubicati su una pluralità di dispositivi diversi, per cui può risultare complesso individuare l’ubicazione di tutti i dati riconducibili a tale utente, oltre a rappresentare un grosso problema in termini di giurisdizione territoriale.
* **Elasticità, scalabilità e flessibilità**: l’utente di un servizio cloud può variare dinamicamente ...
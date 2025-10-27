---
title: Trust della rete Interna al perimetro aziendale
url: https://www.ictsecuritymagazine.com/articoli/trust-della-rete/
source: ICT Security Magazine
date: 2025-07-22
fetch_date: 2025-10-06T23:51:17.359510
---

# Trust della rete Interna al perimetro aziendale

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

![Network Trust: architettura di sicurezza Zero Trust per le reti aziendali con segmentazione, perimetri software-defined e protezione contro movimenti laterali](https://www.ictsecuritymagazine.com/wp-content/uploads/untitled-design-12_QjjYQH1k.png)

# Trust della rete Interna al perimetro aziendale

A cura di:[Fabrizio Fioravanti](#molongui-disabled-link)  Ore 21 Luglio 202526 Agosto 2025

Questo articolo fa parte della [serie](https://www.ictsecuritymagazine.com/articoli/device-trust/) dedicata al tema dell’architettura Zero Trust. In questo focus esploriamo la ridefinizione del perimetro aziendale nell’era del lavoro remoto e del cloud, analizzando i livelli di fiducia nei segmenti di rete, le tecnologie avanzate per l’implementazione della sicurezza Zero Trust nelle infrastrutture di rete e le strategie di mitigazione dei rischi associati agli attacchi moderni.

## La Ridefinizione del Perimetro di Rete nell’Architettura Zero Trust

In questa sezione estendiamo il perimetro di azione e controllo oltre l’utente e il suo dispositivo. Sebbene il perimetro aziendale non sia più limitato al solo perimetro fisico dietro il firewall, a causa del lavoro remoto, delle interazioni con la supply chain e delle estensioni verso il cloud, il concetto di perimetro aziendale rimane comunque rilevante, ma deve essere ridefinito rispetto alle modalità tradizionali.

Il nuovo concetto di perimetro aziendale può essere inteso come il contesto in cui viene eseguita un’autenticazione: ogni volta che ci autentichiamo, ci troviamo all’interno del perimetro aziendale e proiettiamo il nostro dispositivo all’interno di questo perimetro in modo più o meno forte. In questo senso, il perimetro aziendale comprende non solo la rete cablata dell’organizzazione dietro il firewall, ma anche le VPN, i servizi cloud, le reti wireless autenticate e le aree riservate dei siti web aziendali.

Tutto ciò che non rientra in queste definizioni deve essere considerato come non trusted e, quindi, come una potenziale fonte di rischio. Analogamente a quanto fatto per utenti e dispositivi, anche i segmenti di rete del perimetro devono essere differenziati in base al livello di fiducia.

Una prima suddivisione è tra ciò che è esterno e ciò che è interno al perimetro aziendale, ma all’interno del perimetro stesso esistono ulteriori livelli di fiducia che possiamo classificare come segue:

* **Reti o segmenti di rete a bassa fiducia:** Questi segmenti di rete, pur rientrando all’interno del perimetro aziendale, sono caratterizzati da un basso livello di fiducia, poiché sono popolati principalmente da dispositivi non gestiti dall’organizzazione o soggetti a un’autenticazione debole. Un esempio comune sono le reti Wi-Fi, che richiedono cautele particolari, come l’isolamento dei dispositivi tra loro e l’accesso limitato solo a servizi pubblici o a risorse ben definite. Un altro esempio sono i segmenti di rete in cui vengono posizionati i dispositivi che non hanno ancora soddisfatto le policy di conformità o che non riescono ad autenticarsi con successo con i sistemi di Network Access Control (NAC). Alcune tipologie di VPN possono rientrare in questa categoria, specialmente quando l’autenticazione richiesta è debole e consente l’accesso solo a servizi secondari.
* **Reti o segmenti di rete con livello di fiducia normale**: Questi segmenti consentono il collegamento tra dispositivi all’interno del perimetro aziendale e l’accesso a settori non protetti da ulteriori livelli di firewall. Rappresentano il perimetro normale in cui operano dispositivi e utenti che soddisfano i criteri di sicurezza necessari per essere considerati affidabili.
* **Reti privilegiate o segmenti di infrastruttura:** Questi segmenti di rete sono particolarmente sensibili e limitano l’accesso solo a utenti e dispositivi con elevati privilegi. Sono generalmente protetti da più livelli di firewall e spesso implementano una micro-segmentazione all’interno delle VLAN per garantire il massimo isolamento. Includono i segmenti dedicati alla gestione dell’infrastruttura, dei servizi di rete, dei sistemi e della sicurezza. L’accesso è spesso consentito solo tramite bastion host o VPN specifiche, anche quando ci si trova all’interno del perimetro aziendale.

Collegarsi fisicamente a una porta di rete cablata, a una rete Wi-Fi o a una VPN non deve garantire un accesso indiscriminato alle risorse più sensibili. Ad esempio, anche se ci si collega alla rete cablata, solo nel caso in cui il dispositivo disponga di certificati adeguati e sia conforme alle policy di conformità, sarà possibile proiettare il dispositivo in una rete con livello di fiducia normale; altrimenti, verrà relegato a un segmento a bassa fiducia fino a quando non saranno soddisfatte tutte le condizioni per una sua promozione.

## Evoluzione della Sicurezza di Rete: dal Perimetro Tradizionale allo Zero Trust

L’evoluzione del concetto di perimetro di rete ha portato all’emergere del “Software-Defined Perimeter” (SDP), un approccio che secondo il Cloud Security Alliance offre vantaggi significativi rispetto alle tradizionali architetture di rete. L’SDP implementa il principio “Black Cloud”, dove le risorse di rete sono invisibili sia agli utenti interni che esterni fino a quando non viene stabilita un’identità verific...
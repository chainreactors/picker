---
title: Tecniche di Onboarding dei dispositivi
url: https://www.ictsecuritymagazine.com/articoli/tecniche-onboarding/
source: ICT Security Magazine
date: 2025-07-05
fetch_date: 2025-10-06T23:25:44.824543
---

# Tecniche di Onboarding dei dispositivi

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/untitled-design-5_AzbVtQQn.png)

# Tecniche di Onboarding dei dispositivi

A cura di:[Fabrizio Giorgione e Giovanni Cappabianca](#molongui-disabled-link)  Ore 4 Luglio 202516 Luglio 2025

Questo approfondimento fa parte della [serie](https://www.ictsecuritymagazine.com/articoli/onboarding-iot/) dedicata alle tecniche di onboarding sicuro dei dispositivi IoT in piattaforma cloud. L’articolo esplora tre metodologie principali: l’autenticazione basata su informazioni hardware e di connessione, l’utilizzo di credenziali statiche precaricate, e l’implementazione di certificati a mutua autenticazione x.509. Viene analizzata in dettaglio ogni tecnica, evidenziandone vantaggi, svantaggi e considerazioni di sicurezza nel contesto delle moderne piattaforme cloud come AWS.

## Tecniche di Onboarding IoT: Metodi di Autenticazione e Sicurezza

L’onboarding può avvenire contattando un servizio oppure un intermediario che accetta operazioni di pubblicazione e sottoscrizione da parte dei dispositivi (il broker usato nei paradigmi di comunicazione [Message Oriented Middleware](https://ieeexplore.ieee.org/document/8905013)). Indipendentemente dalla modalità di scambio scelta con la piattaforma, possiamo distinguere questi approcci basandoci sul tipo di dati scambiato per il riconoscimento della legittimità del dispositivo alla comunicazione.

## Primo metodo. Utilizzo di Informazioni sulla connessione e l’hardware

In questo metodo la piattaforma ricorre alle informazioni correnti di connessione usate dal dispositivo per riconoscerlo e considerarlo affidabile.

![](https://www.ictsecuritymagazine.com/wp-content/uploads/onb.png)

Figura 5. Esempio di sequenza del primo metodo

**Step 1.** Un operatore autorizzato riceve l’indirizzo IP ed il codice seriale del dispositivo che dovrà essere installato in campo. Tramite un servizio presente in piattaforma, con il suo ruolo procederà all’aggiornamento della base dati contenente l’insieme delle coppie (indirizzo IP, codice seriale) autorizzate alla comunicazione.

**Step 2.** Il servizio dedicato all’Onboarding, a cadenza fissata recupererà dal database l’insieme di indirizzi IP e procederà con l’aggiornamento delle regole di apertura rotte in ingresso. Se stiamo lavorando sul cloud provider AWS, questa operazione consiste nell’aggiornamento delle regole in inbound del security group associato all’EC2.

**Step 3.** il dispositivo contatta il servizio di onboarding mandando nel suo primo messaggio il suo codice seriale. La piattaforma accerta che il codice seriale corrisponda a quello assegnato all’indirizzo IP. Se la verifica ha esito positivo, il dispositivo è abilitato alla comunicazione con i restanti servizi di monitoraggio e controllo offerti dalla piattaforma. Si noti che un dispositivo con indirizzo IP non presente in piattaforma o con codice seriale non conforme non è supportato dal servizio di onboarding.

Il vantaggio di questa tecnica consiste nel non dover mantenere alcuna credenziale a bordo del dispositivo per autenticarsi in piattaforma perché sarà la piattaforma stessa a gestire una whitelist contenente l’insieme degli indirizzi IP e dei codici seriali autorizzati al dialogo. Lo svantaggio di questo approccio consiste nel dover usare un riferimento fisso per la connessione, come un indirizzo IP pubblico statico oppure ricorrere ad una soluzione che permetta alla piattaforma di “seguire” le variazioni di connessione del dispositivo (Pensiamo ad un canonical name assegnato al dispositivo con un servizio DNS che si occupa di tradurlo).

In quest’ultimo scenario si aprono ulteriori complessità di gestione, come la scelta di chi e come dovrà aggiornare le variazioni della connessione. Delegare il dispositivo
 nell’aggiornamento richiederebbe l’introduzione di un ulteriore meccanismo di autenticazione e controllo.

Se volessimo lasciare questa Idra ad Ercole optando per il servizio di indirizzamento pubblico statico, un fattore da considerare sono i costi previsti dal proprio ISP (Internet Service Provider). Su logiche di larga scala potrebbe non essere la strategia migliore. Si potrebbe ovviare al problema dell’indirizzamento dinamico tramite l’allestimento di una VPN (menzionata in precedenza), accettando però i relativi costi di amministrazione e manutenzione.

## Secondo metodo. Utilizzo di credenziali statiche pre-caricate a bordo del dispositivo

Esempio. Utilizzo di Access Key e secret Key di un’utenza AWS pre-caricate a bordo del dispositivo:

**Step 1.** un operatore autorizzato assume un ruolo in piattaforma per poter censire l’utenza dedicata per il dispositivo con la definizione dei permessi associati.

**Step 2.** L’operatore immette e salva in un’area di memoria sicura del dispositivo le credenziali associate all’utenza creata.

**Step 3.** il dispositivo si autentica in piattaforma. Se il nostro cloud provider è AWS, abbiamo una coppia di valori noti come Access Key e Secret Key con cui il dispositivo può accedere in piattaforma. Qualsiasi operazione il dispositivo tenta di fare in piattaforma è soggetta a revisione. Viene consultata una tabella che definisce per un’utenza l’insieme delle azioni consentite. AWS offre questo servizio tramite L’[identity Access Management](https://ww...
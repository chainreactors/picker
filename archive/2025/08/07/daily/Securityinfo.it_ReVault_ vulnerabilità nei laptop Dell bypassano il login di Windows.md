---
title: ReVault: vulnerabilità nei laptop Dell bypassano il login di Windows
url: https://www.securityinfo.it/2025/08/06/revault-vulnerabilita-nei-laptop-dell-bypassano-il-login-di-windows/?utm_source=rss&utm_medium=rss&utm_campaign=revault-vulnerabilita-nei-laptop-dell-bypassano-il-login-di-windows
source: Securityinfo.it
date: 2025-08-07
fetch_date: 2025-10-07T00:50:14.146964
---

# ReVault: vulnerabilità nei laptop Dell bypassano il login di Windows

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

* [Home](https://www.securityinfo.it)
* [News](https://www.securityinfo.it/category/news/)
* [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/)
* [Opinioni](https://www.securityinfo.it/category/opinioni/)
* [Top Malware](https://www.securityinfo.it/top-malware-page/)
* [Minacce](https://www.securityinfo.it/category/minacce-2/)
* [Guide alla sicurezza](http://www.securityinfo.it/guide-alla-sicurezza/)
* [Podcast](https://www.securityinfo.it/podcast-page/)
* [Strumenti Utili](https://www.securityinfo.it/category/strumenti-utili/)

* Search for:

## ReVault: vulnerabilità nei laptop Dell bypassano il login di Windows

Ago 06, 2025  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/08/06/revault-vulnerabilita-nei-laptop-dell-bypassano-il-login-di-windows/#respond)

---

Un gruppo di vulnerabilità nel firmware *ControlVault3* espone oltre cento modelli di laptop Dell a scenari di attacco critici. A segnalarlo sono i ricercatori di Cisco Talos che hanno battezzato la serie di falle con il nome *ReVault*. Le vulnerabilità consentono a un attaccante di **ottenere accesso al sistema senza conoscere le credenziali dell’utente e di installare codice persistente** **nel firmware**, sopravvivendo anche a reinstallazioni di Windows.

![](https://www.securityinfo.it/wp-content/uploads/2025/08/Hacking_Dell-6-ago-2025CG-1024x683.png)

I dispositivi coinvolti appartengono principalmente alle **famiglie *Latitude* e *Precision***, impiegate frequentemente in ambiti aziendali, governativi e industriali. I moduli ControlVault sono progettati per gestire in modo sicuro credenziali, dati biometrici e codici di autenticazione all’interno di un componente hardware isolato: il *Unified Security Hub (USH)*.

Talos ha identificato **cinque vulnerabilità**: due di tipo *out-of-bounds* (CVE-2025-24311 e CVE-2025-25050), un *arbitrary free* (CVE-2025-25215), un *stack overflow* (CVE-2025-24922) e una *unsafe deserialization* (CVE-2025-24919). I ricercatori sottolineano che queste falle interessano sia il firmware del modulo ControlVault3 sia le API utilizzate da Windows per comunicare con esso.

In uno scenario d’attacco tipico, un aggressore con accesso fisico al laptop può aprire il dispositivo e collegarsi al modulo USH tramite una connessione USB custom. A quel punto, è possibile **sfruttare le vulnerabilità per eseguire codice arbitrario direttamente sul firmware**, eludendo le protezioni del sistema operativo e dei meccanismi di autenticazione. Secondo Cisco Talos, un impianto malevolo installato in questo modo può persistere anche dopo la formattazione e reinstallazione del sistema operativo.

Uno degli impatti più significativi riguarda la **possibilità di compromettere il sistema di autenticazione biometrica**. Un attacco riuscito può indurre il dispositivo ad accettare qualunque impronta digitale, bypassando il controllo su quelle autorizzate.

Dell ha pubblicato aggiornamenti tra marzo e maggio 2025 per correggere le vulnerabilità nei driver e nel firmware di ControlVault3. La lista completa dei modelli interessati è disponibile nella documentazione ufficiale dell’azienda. I ricercatori raccomandano di **applicare quanto prima gli aggiornamenti** e, nei contesti più sensibili, di disattivare periferiche di autenticazione non necessarie come lettori di impronte, smart card o NFC. È inoltre consigliabile abilitare nel BIOS la rilevazione di intrusioni fisiche e attivare la funzione *Enhanced Sign-in Security* di Windows, che consente di rilevare anomalie nei moduli di autenticazione.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [attacco fisico](https://www.securityinfo.it/tag/attacco-fisico/), [bypass login Windows](https://www.securityinfo.it/tag/bypass-login-windows/), [Dell ControlVault3](https://www.securityinfo.it/tag/dell-controlvault3/), [exploit firmware](https://www.securityinfo.it/tag/exploit-firmware/), [fingerprint spoofing](https://www.securityinfo.it/tag/fingerprint-spoofing/), [ReVault](https://www.securityinfo.it/tag/revault/), [sicurezza endpoint](https://www.securityinfo.it/tag/sicurezza-endpoint/), [sicurezza hardware](https://www.securityinfo.it/tag/sicurezza-hardware/), [Talos Cisco](https://www.securityinfo.it/tag/talos-cisco/), [vulnerabilità firmware](https://www.securityinfo.it/tag/vulnerabilita-firmware/)

[Anche Google vittima della campagna di ShinyHunters](https://www.securityinfo.it/2025/08/07/anche-google-vittima-della-campagna-di-shinyhunters/)
[Possibile zero-day su SonicWall: Akira colpisce le aziende](https://www.securityinfo.it/2025/08/05/possibile-zero-day-su-sonicwall-akira-colpisce-le-aziende/)

---

![](https://secure.gravatar.com/avatar/57d6369d65bf9ebecae351af675ce2fd?s=90&d=mm&r=g)

##### [Redazione](https://www.securityinfo.it/author/redazione/)

##### Articoli correlati

* [![Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor](https://www.securityinfo.it/wp-content/uploads/2025/08/nVidia-13-ago-2025CG-120x85.png)](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/ "Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor")

  [Cina contro Nvidia: dubbi sulla...](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/ "Permanent link to Cina contro Nvidia: dubbi sulla sicurezza dei chip AI e sospetti di backdoor")

  Ago 13, 2025  [0](https://www.securityinfo.it/2025/08/13/cina-contro-nvidia-dubbi-sulla-sicurezza-dei-chip-ai-e-sospetti-di-backdoor/#respond)

##### Altro in questa categoria

* [![Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/wp-content/uploads/2025/10/hacker-3342696_1920-120x85.jpg)](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/ "Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%")

  [Impennata delle scansioni dei portali.....
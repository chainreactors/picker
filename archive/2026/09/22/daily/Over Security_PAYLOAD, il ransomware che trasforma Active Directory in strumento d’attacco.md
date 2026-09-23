---
title: PAYLOAD, il ransomware che trasforma Active Directory in strumento d’attacco
url: https://www.cybersecurity360.it/nuove-minacce/ransomware/payload-il-ransomware-che-trasforma-active-directory-in-strumento-dattacco/
source: Over Security
date: 2026-09-22
fetch_date: 2026-09-23T06:54:41.006929
---

# PAYLOAD, il ransomware che trasforma Active Directory in strumento d’attacco

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=cybersecurity360.it)
[I nostri servizi](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## PAYLOAD, il ransomware che trasforma Active Directory in strumento d’attacco

* [Ultimi articoli](https://www.cybersecurity360.it/ultimi-articoli/)
* [Cybersecurity Nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* Malware e attacchi
  + [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
  + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)
* Norme e adeguamenti
  + [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)
* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
* [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
* [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
* [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
* [Chi siamo](https://www.cybersecurity360.it/about/)

* [![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_neg_logo-768x55.png)](https://www.cybersecurity360.it)
* Seguici
* + [X](https://twitter.com/Cybersec360)
  + [linkedin](https://www.linkedin.com/company/cybersecurity360/)
  + [Newsletter](https://www.cybersecurity360.it/newsletter-signin/)
  + [Rss Feed](#rssModal)
  + [Chi siamo](https://www.cybersecurity360.it/about)
* AREA PREMIUM
* [Whitepaper](https://www.cybersecurity360.it/whitepaper/)
* [Eventi](https://www.cybersecurity360.it/eventi/)
* [Webinar](https://www.cybersecurity360.it/webinar/)
* CANALI
* [Ultimi articoli](https://www.cybersecurity360.it/ultimi-articoli/)
* [Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
* + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)* [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  * + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
    * [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
    * [L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
    * [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
    * [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
    * [Chi siamo](https://www.cybersecurity360.it/about/)

[Ultimi articoli](https://www.cybersecurity360.it/ultimi-articoli/)
[Cybersecurity Nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
[Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
[Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
[Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
[Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
[Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
[Chi siamo](https://www.cybersecurity360.it/about/)

la ricerca

# PAYLOAD, il ransomware che trasforma Active Directory in strumento d’attacco

---

[Commenta l'articolo](#comments)

Indirizzo copiato

---

Niente malware sui PC, nessun file cifrato e nessun processo sospetto da intercettare. In un incidente analizzato da Kaspersky, gli attaccanti hanno utilizzato le Group Policy di Active Directory per colpire contemporaneamente l’intero dominio, trasformando uno degli strumenti più fidati dell’amministrazione Windows in un meccanismo di estorsione

Pubblicato il 22 set 2026

---

[Dario Fadda](https://www.cybersecurity360.it/giornalista/dario-fadda/)

Research Infosec, fondatore Insicurezzadigitale.com

---

---

![AI Questions Icon](data:image/gif;base64...)![AI Questions Icon](https://chatbotdev.ai.nextwork360.it/icons/NW360.svg)

Chiedi all'AI

Riassumi questo articolo

Approfondisci con altre fonti

![ransomware active directory](data:image/png;base64...)![ransomware active directory](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2026/09/ransomware-active-directory.jpg)

---

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=cybersecurity360.it)

---

---

---

Quando si pensa a un [attacco ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware-cose-come-rimuoverlo-e-come-difendersi/), la sequenza sembra ormai consolidata: accesso alla rete, escalation dei privilegi, movimento laterale, disattivazione delle difese, distribuzione del malware e infine cifratura dei sistemi. Ma nel caso di **PAYLOAD**, analizzato dal Global Emergency Response Team (GERT) di Kaspersky, manca proprio il passaggio che normalmente considereremmo centrale.

Sulle workstation Windows non è stato trovato alcun ransomware.

Non c’erano file cifrati, eseguibili malevoli residenti sul disco, servizi installati dagli attaccanti o processi sospetti in memoria. Eppure, l’organizzazione era stata colpita su scala di dominio: gli utenti si erano ritrovati davanti alla richiesta di riscatto, wallpaper e lock screen erano stati sostituiti e l’account amministratore locale era stato disabilitato.

Il ransomware, in sostanza, non era stato distribuito ai computer. Gli attaccanti avevano trasformato [Active Directory](https://www.cybersecurity360.it/news/patch-tuesday-il-record-che-nessuno-voleva-622-cve-e-un-nuovo-modo-di-fare-sicurezza/) nel proprio strumento di distribuzione.

Indice degli argomenti

* [Tutto comincia da una VPN](#Tutto_comincia_da_una_VPN)
* [Il ransomware diventa una Group Policy](#Il_ransomware_diventa_una_Group_Policy)
* [Windows Firewall spento su tutto il dominio](#Windows_Firewall_spento_su_tutto_il_dominio)
* [Una bomba a orologeria nascosta nelle GPO](#Una_bomba_a_orologeria_nascosta_nelle_GPO)
* [Il ransomware senza cifratura](#Il_ransomware_senza_cifratura)
* [Se non esiste un malware, cosa deve cercare il SOC?](#Se_non_esiste_un_malware_cosa_deve_cercare_il_SOC)
* [Prima Active Directory, poi gli endpoint](#Prima_Active_Directory_poi_gli_endpoint)
* [Quando l’infrastruttura fidata diventa il payload](#Quando_linfrastruttura_fidata_diventa_il_payload)

## Tutto comincia da una VPN

L’incidente risale all’aprile 2026 e ha coinvolto un’azienda manifatturiera del Medio Oriente. Secondo la ricostruzione di Kaspersky, l’11 aprile gli attaccanti sono entrati nella rete autenticandosi a una FortiGate SSL VPN utilizzando credenziali di dominio valide ma compromesse.

Non è stato possibile stabilire come quelle credenziali fossero state ottenute. La telemetria disponibile sul dispositivo FortiGate non era sufficiente per ricostruire la fase precedente all’accesso e gli investigatori considerano plausibili diversi scenari: password spraying o [credential stuffing](https://www.cybersecurity360.it/nuove-minacce/attacchi-credential-stuffing-cosa-sono-e-come-difendersi-dal-furto-di-identita-online/) contro il portale [VPN](https://www.cybersecurity360.it/cultura-cyber/il-segreto-per-navigare-in-sicurezza-ecco-come-installare-una-vpn/), [phishing](https://www.cybersecurity360.it/nuove-minacce/phishing-cose-e-come-proteggersi-la-guida-completa/) finalizzato al furto delle credenziali oppure l’acquisto di un account già compromesso da un [...
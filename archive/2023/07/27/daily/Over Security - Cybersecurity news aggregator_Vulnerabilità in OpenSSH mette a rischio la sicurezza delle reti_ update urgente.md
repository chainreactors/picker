---
title: Vulnerabilità in OpenSSH mette a rischio la sicurezza delle reti: update urgente
url: https://www.cybersecurity360.it/nuove-minacce/vulnerabilita-in-openssh-mette-a-rischio-la-sicurezza-delle-reti-update-urgente/
source: Over Security - Cybersecurity news aggregator
date: 2023-07-27
fetch_date: 2025-10-04T11:56:36.548367
---

# Vulnerabilità in OpenSSH mette a rischio la sicurezza delle reti: update urgente

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Vulnerabilità in OpenSSH mette a rischio la sicurezza delle reti: update urgente

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
* + [twitter](https://twitter.com/Cybersec360)
  + [linkedin](https://www.linkedin.com/company/cybersecurity360/)
  + [Newsletter](https://www.cybersecurity360.it/newsletter-signin/)
  + [Rss Feed](#rssModal)
  + [Chi siamo](https://www.cybersecurity360.it/about)
* AREA PREMIUM
* [Whitepaper](https://www.cybersecurity360.it/whitepaper/)
* [Eventi](https://www.cybersecurity360.it/eventi/)
* [Webinar](https://www.cybersecurity360.it/webinar/)
* CANALI
* [Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
* + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)* [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  * + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
    * [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
    * [L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
    * [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
    * [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
    * [Chi siamo](https://www.cybersecurity360.it/about/)

[Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
[Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
[Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
[Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
[Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
[L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
[Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
[Chi siamo](https://www.cybersecurity360.it/about/)

Nuove minacce

# Vulnerabilità in OpenSSH mette a rischio la sicurezza delle reti: update urgente

* [Home](https://www.cybersecurity360.it)
* [Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](https://www.cybersecurity360.it/nuove-minacce/)

La recente scoperta della vulnerabilità CVE-2023-38408 nel software OpenSSH mette in evidenza l’importanza della sicurezza informatica e degli aggiornamenti regolari. Il rischio è l’esecuzione di codice malevolo tramite l’agente ssh, ma c’è l’aggiornamento

Pubblicato il 26 Lug 2023

[Dario Fadda](https://www.cybersecurity360.it/giornalista/dario-fadda/)

Research Infosec, fondatore Insicurezzadigitale.com

![OpenSSH vulnerabilità](data:image/png;base64...)![OpenSSH vulnerabilità](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2023/07/openssh.png)

**OpenSSH**, la rinomata implementazione open source del protocollo [Secure Shell (SSH)](https://en.wikipedia.org/wiki/Secure_Shell), ha rilasciato un aggiornamento vitale per affrontare una vulnerabilità ritenuta critica.

Questo software, **essenziale per garantire comunicazioni crittografate su reti non protette**, è ampiamente utilizzato da innumerevoli aziende e organizzazioni per **consentire interazioni sicure all’interno delle reti**.

Indice degli argomenti

* [SSH agent può consentire l’esecuzione di codice malevolo](#SSH_agent_puo_consentire_lesecuzione_di_codice_malevolo)
* [L’importanza degli aggiornamenti software regolari](#Limportanza_degli_aggiornamenti_software_regolari)

## SSH agent può consentire l’esecuzione di codice malevolo

La vulnerabilità, **denominata CVE-2023-38408**, è stata scoperta dal team Qualys Security Advisory e riguarda l’agente ssh inoltrato di OpenSSH. L’agente ssh è un componente chiave che semplifica il processo di autenticazione dell’utente memorizzando le chiavi di identità e le passphrase utilizzate dagli utenti. Questo evita che gli utenti debbano reinserire la password o la passphrase durante le connessioni a server diversi, consentendo un’esperienza di [autenticazione “single sign-on” (SSO)](https://www.cybersecurity360.it/nuove-minacce/single-sign-on-accesso-facilitato-alle-risorse-di-rete-ecco-come-funziona/) più lineare.

Tuttavia, la vulnerabilità CVE-2023-38408 ha dimostrato che anche i sistemi utili per la sicurezza, possono contenere difetti potenzialmente gravi. Essa permette l’esecuzione di codice in modalità remota attraverso il socket agent inoltrato dell’agente ssh, con particolare rilevanza per gli standard crittografici PKCS#11. Ciò significa che un aggressore con i prerequisiti necessari potrebbe sfruttare la vulnerabilità per eseguire codice remoto su un sistema sotto il suo controllo.

Affinché l’attacco sia possibile, devono essere soddisfatti due requisiti: **la presenza di determinate librerie sul sistema di destinazione e l’invio dell’agente ssh a un sistema controllato dall’aggressore**. Nonostante sembri una vulnerabilità pericolosa, esistono misure di salvaguardia per mitigare i rischi. In particolare, **si raccomanda agli utenti di aggiornare OpenSSH alla versione 9.3p2 o successiva**, inoltre è possibile limitare l’accettazione di specifici provider PKCS#11 configurando il server. È fondamentale prestare attenzione quando si invia l’agente SSH a server non attendibili e, in caso di sospetto di violazione della sicurezza, effettuare una scansione del sistema per individuare eventuali malware dannosi.

## L’importanza degli aggiornamenti software regolari

**Gli esperti di sicurezza informatica sottolineano l’importanza di adottare una pratica di aggiornamento regolare e tempestiva**, proprio perché gli sviluppatori lavorano costantemente per identificare e correggere vulnerabilità simili.

Con l’aumento delle minacce informatiche, proteggere i sistemi dai rischi di sicurezza è una responsabilità fondamentale per qualsiasi organizzazione o azienda.

In conclusione, OpenSSH è un componente cruciale nell’arsenale della sicurezza informatica ed è essenziale mantenerlo aggiornato per garantire la protezione contro potenziali attacchi.

La scoperta della vulnerabilità CVE-2023-38408 serve come promemoria per tutte le aziende e gli utenti di essere vigili nella gestione della sicurezza delle proprie reti e nel mantenere i software utilizzati costantemente aggiornati.

Valuta la qualità di questo articolo

La tua opinione è importante per noi!

INVIA

-...
---
title: Grave vulnerabilità in OpenSSL: rischio di attacchi Man-in-the-Middle
url: https://www.cybersecurity360.it/news/grave-vulnerabilita-in-openssl-rischio-di-attacchi-man-in-the-middle/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-13
fetch_date: 2025-10-06T20:47:55.725706
---

# Grave vulnerabilità in OpenSSL: rischio di attacchi Man-in-the-Middle

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Grave vulnerabilità in OpenSSL: rischio di attacchi Man-in-the-Middle

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

l’exploit

# Grave vulnerabilità in OpenSSL: rischio di attacchi Man-in-the-Middle

---

[Home](https://www.cybersecurity360.it)

[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)

---

Indirizzo copiato

---

Scenari di sfruttamento con successo di questa vulnerabilità rendono possibile per l’attaccante fare da intermediario tra le azioni del cliente verso il server. Importante aggiornare tempestivamente

Pubblicato il 12 feb 2025

---

[Dario Fadda](https://www.cybersecurity360.it/giornalista/dario-fadda/)

Research Infosec, fondatore Insicurezzadigitale.com

---

---

![Vulnerabilità OpenSSL attacchi MitM](data:image/png;base64...)![Vulnerabilità OpenSSL attacchi MitM](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2025/02/Vulnerabilita-OpenSSL-attacchi-MitM.jpg)

---

Una vulnerabilità di **alta severità** è stata recentemente scoperta in OpenSSL, la libreria di [crittografia](https://www.cybersecurity360.it/soluzioni-aziendali/crittografia-per-le-aziende-protette-e-compliant-al-gdpr-ecco-come/) open-source ampiamente utilizzata per proteggere le comunicazioni su Internet.

La falla, identificata come **CVE-2024-12797**, è stata segnalata dai ricercatori di sicurezza di Apple e potrebbe consentire attacchi **[Man-in-the-Middle (MitM)](https://www.cybersecurity360.it/nuove-minacce/attacco-man-in-the-middle-tutti-i-modi-possibili-e-come-difenderci/)** in determinate configurazioni.

Indice degli argomenti

* [Dettagli della vulnerabilità](#Dettagli_della_vulnerabilita)
* [Scenario di attacco](#Scenario_di_attacco)
* [Versioni vulnerabili e correzioni](#Versioni_vulnerabili_e_correzioni)

## Dettagli della vulnerabilità

La vulnerabilità risiede nella gestione delle chiavi pubbliche non elaborate (Raw Public Keys, RPK) secondo lo standard RFC7250. In particolare, il problema si verifica quando i client utilizzano le RPK per autenticare un server.

A causa di una mancata interruzione delle handshake TLS/DTLS quando la verifica del peer SSL è impostata, i client vulnerabili potrebbero non rilevare che il server non è stato autenticato correttamente.

## Scenario di attacco

Un attaccante potrebbe sfruttare questa vulnerabilità intercettando la comunicazione tra un client e un server. L’attaccante si posizionerebbe come intermediario, intercettando e potenzialmente modificando i dati scambiati tra le due parti.

Questo è possibile perché il client, a causa della vulnerabilità, non riesce a verificare l’identità del server tramite RPK, aprendo la strada all’attacco MitM.

## Versioni vulnerabili e correzioni

Le versioni di OpenSSL interessate sono la 3.4, 3.3 e 3.2. Il problema è stato risolto con il [rilascio](https://openssl-library.org/news/secadv/20250211.txt) delle versioni **3.4.1, 3.3.2 e 3.2.4**. È fondamentale che gli amministratori di sistema aggiornino immediatamente le proprie installazioni di OpenSSL per proteggersi da questa minaccia.

È importante notare che l’uso di RPK è disabilitato di default sia nei client che nei server TLS. La vulnerabilità si manifesta solo quando i client abilitano esplicitamente l’uso di RPK da parte del server e quest’ultimo invia una RPK invece di una catena di certificati X.509.

Anche in presenza della vulnerabilità, i client possono rilevare il fallimento della verifica della chiave pubblica non elaborata chiamando la funzione “SSL\_get\_verify\_result()”. I client che eseguono questa verifica e intraprendono le azioni appropriate non sono vulnerabili.

@RIPRODUZIONE RISERVATA

Valuta la qualità di questo articolo

La tua opinione è importante per noi!

INVIA

![](data:image/png;base64...)![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2021/11/photo_2023-07-06_13-05-23-transformed-640x360.png)

##### Dario Fadda

###### Research Infosec, fondatore Insicurezzadigitale.com

---

Who's Who

* [D

  Dario Fadda](https://www.cybersecurity360.it/personaggi/dario-fadda/)

---

Argomenti

* [C

  Crittografia](https://www.cybersecurity360.it/tag/crittografia/)
* [M

  man-in-the-middle](https://www.cybersecurity360.it/tag/man-in-the-middle/)
* [M

  MitM](https://www.cybersecurity360.it/tag/mitm/)
* [V

  vulnerabilità](https://www.cybersecurity360.it/tag/vulnerabilita/)

---

Canali

* [![Attacchi hacker e Malware: le ultime news in tempo reale e gli approfondimenti](data:image/png;base64...)![Attacchi hacker e Malware: le ultime news in tempo reale...
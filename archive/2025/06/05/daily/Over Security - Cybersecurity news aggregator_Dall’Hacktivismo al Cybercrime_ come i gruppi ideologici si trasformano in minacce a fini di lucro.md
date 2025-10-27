---
title: Dall’Hacktivismo al Cybercrime: come i gruppi ideologici si trasformano in minacce a fini di lucro
url: https://www.insicurezzadigitale.com/dallhacktivismo-al-cybercrime-come-i-gruppi-ideologici-si-trasformano-in-minacce-a-fini-di-lucro/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-05
fetch_date: 2025-10-06T22:54:21.544324
---

# Dall’Hacktivismo al Cybercrime: come i gruppi ideologici si trasformano in minacce a fini di lucro

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

# Dall’Hacktivismo al Cybercrime: come i gruppi ideologici si trasformano in minacce a fini di lucro

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
4 Giugno 2025

![](https://insicurezzadigitale.com/wp-content/uploads/2025/06/image.png)

In uno scenario sempre più complesso, dove ideologia e crimine si intrecciano, **Rapid7** ha pubblicato un’analisi approfondita sull’evoluzione di alcuni gruppi hacktivisti verso modelli operativi orientati al profitto. La [ricerca](https://old.rapid7.com/blog/post/2025/06/03/from-ideology-to-financial-gain-exploring-the-convergence-from-hacktivism-to-cybercrime/) si concentra su tre attori emergenti: **FunkSec**, **KillSec** e **GhostSec**, evidenziando come il confine tra attivismo politico e attività criminali strutturate si stia dissolvendo.

### Dal dissenso politico all’estorsione

Nati come gruppi motivati da cause ideologiche – spesso legati a campagne pro-Palestina o ad attività anti-occidentali – molti attori hanno adottato modelli **Ransomware-as-a-Service (RaaS)**, incorporando tecniche di estorsione finanziaria che includono:

* **Doppia estorsione**: cifratura e successiva minaccia di pubblicazione dei dati.
* **Malware personalizzato** sviluppato anche tramite strumenti AI generativi.
* **Servizi per affiliati**: dashboard, builder, locker e gestione dei pagamenti.

---

### Focus tecnico: i gruppi in evoluzione

#### FunkSec

Nato come collettivo pro-“Free Palestine”, FunkSec è oggi un gruppo RaaS attivo dal dicembre 2024 con almeno **172 vittime** globali, inclusi target in **Italia**, **Francia** e **Israele**. Utilizza il **FunkLocker**, un encryptor AI-powered, e offre servizi di defacement e DDoS nel dark web.
**IoC** associati:

* `funksec53xh7j5t6ysgwnaidj5vkh3aqajanplix533kwxdz3qrwugid[.]onion`
* SHA-256: `0538d726ae3cc264...`

#### KillSec

Attivo dal 2021 e inizialmente affiliato ad Anonymous, ha virato su un’offerta RaaS nel 2023 con locker per ambienti **Windows ed ESXi**. La loro DLS (dedicated leak site) offre non solo leak, ma anche **dati in vendita tra i 5.000 e i 350.000 dollari**.
**Tecniche osservate**:

* Locker scritto in **C++**
* Costruzione payload tramite builder personalizzato
* TOX e Session ID documentati nei loro canali Telegram

#### GhostSec

Conosciuto per #OpISIS e altri attacchi ideologici, ha collaborato nel 2023 con **Stormous** per azioni ransomware contro enti governativi a Cuba. Ha sviluppato **GhostLocker** (poi GhostLocker 2.0 “Rewrite”) e un infostealer chiamato **GhostStealer**.
Nel 2024, ha annunciato il ritorno all’hacktivismo, lasciando a Stormous la gestione del proprio locker.

---

### Indicatori di Compromissione (IoC) selezionati

| Gruppo | IoC rilevanti |
| --- | --- |
| FunkSec | `http://funksec[.]top`, `funksecsekgasgjqlz...onion` |
| KillSec | `http://ks5424y3wpr5zlu...onion`, TOX: `9453686EAB...`, IP: `82[.]147[.]84[.]98` |
| GhostSec | SHA256: `8b758ccdfbfa5ff3a...`, Telegram: [GhostSecS](https://t.me/GhostSecS) |

---

### Italia: Target sempre più frequente

L’Italia è direttamente coinvolta: **FunkSec** e **KillSec** figurano tra gli attori che colpiscono il nostro Paese con attacchi ransomware e campagne DDoS. In particolare:

* Settori colpiti: **governo, istruzione, manifattura, energia**
* Finalità: da atti di protesta simbolica si è passati a **richieste di riscatto in criptovaluta**
* Modalità: operazioni spesso annunciate in anticipo su Telegram o dark web, con finalità di propaganda e intimidazione.

---

### Difesa e rilevamento

Rapid7 indica anche raccomandazioni operative per i team Blue e CTI:

* Monitoraggio attivo delle DLS conosciute
* Integrazione di questi IoC nei SIEM
* Threat hunting su canali Telegram e dark web

L’analisi Rapid7 dimostra come le motivazioni economiche stiano diventando il driver principale anche per attori nati come ideologici. L’adozione del modello **RaaS** da parte di questi gruppi rappresenta un’evoluzione significativa del panorama delle minacce, e pone nuove sfide in termini di **attribuzione, risposta e protezione**.

##### < tags />

[cybercrime](https://insicurezzadigitale.com/tag/cybercrime/)[ghostsec](https://insicurezzadigitale.com/tag/ghostsec/)[hacktivism](https://insicurezzadigitale.com/tag/hacktivism/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[ransomware](https://insicurezzadigitale.com/tag/ransomware/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Dall%E2%80%99Hacktivismo+al+Cybercrime%3A+come+i+gruppi+ideologici+si+trasformano+in+minacce+a+fini+di+lucro&url=https://insicurezzadigitale.com/dallhacktivismo-al-cybercrime-come-i-gruppi-ideologici-si-trasformano-in-minacce-a-fini-di-lucro/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/dallhacktivismo-al-cybercrime-come-i-gruppi-ideologici-si-trasformano-in-minacce-a-fini-di-lucro/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/dallhacktivismo-al-cybercrime-come-i-gruppi-ideologici-si-trasformano-in-minacce-a-fini-di-lucro/&title=Dall%E2%80%99Hacktivismo+al+Cybercrime%3A+come+i+gruppi+ideologici+si+trasformano+in+minacce+a+fini+di+lucro)

[== articolo precedente ==](https://insicurezzadigitale.com/cve-2025-45542-problemi-di-sql-injection-in-php-cloudclassroom/)

[:: articolo successivo ::](https://insicurezzadigitale.com/cyberwarfare-tra-cina-e-taiwan-nuove-frontiere-della-tensione-geopolitica/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/dallhacktivismo-al-cybercrime-come-i-gruppi-ideologici-si-trasformano-in-minacce-a-fini-di-lucro/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *Dall’Hacktivismo al Cybercrime: come i gruppi ideologici si trasformano in minacce a fini di lucro*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=Dall’Hacktivismo+al+Cybercrime:+come+i).
Condividi esempi, IOCs o tecniche di detection efficaci nel nostro 👉 [**forum community**](https://forum.ransomfeed.it/)

## [[ mastodon ]]

Su Mastodon mi trovi qui: [Mastodon](https://poliversity.it/%40nuke)

### :: i social ::

* [Facebook](https://www.facebook.com/spcnet.it)
* [Instagram](https://www.instagram.com/spcnet.it/)
* [Twitter](https://tw...
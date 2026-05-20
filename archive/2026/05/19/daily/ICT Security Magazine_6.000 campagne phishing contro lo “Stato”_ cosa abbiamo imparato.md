---
title: 6.000 campagne phishing contro lo “Stato”: cosa abbiamo imparato
url: https://www.ictsecuritymagazine.com/articoli/campagne-phishing-pagopa/
source: ICT Security Magazine
date: 2026-05-19
fetch_date: 2026-05-20T06:05:23.012678
---

# 6.000 campagne phishing contro lo “Stato”: cosa abbiamo imparato

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
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Mirko Caruso, Cyber Crime Conference 2026 - Pago PA](https://www.ictsecuritymagazine.com/wp-content/uploads/DSC_3444-scaled.jpg)

# 6.000 campagne phishing contro lo “Stato”: cosa abbiamo imparato

A cura di:[Redazione](#molongui-disabled-link)  Ore 19 Maggio 202614 Maggio 2026

*Intervento di Mirko Caruso (Area Security Governance, Risk & Compliance, PagoPA) alla 1[4ª Cyber Crime Conference,](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026) Roma, 6-7 maggio 2026*

Dal marzo 2025 un’ampia platea di cittadini italiani è finita nel mirino di un fenomeno di phishing su scala industriale, che sfrutta l’autorevolezza del brand PagoPA, insieme ai loghi e alle finalità della piattaforma, per sottrarre dati anagrafici e di pagamento. Nel suo intervento alla 14ª Cyber Crime Conference, Mirko Caruso ne ha ripercorso genesi ed evoluzione, illustrando nel dettaglio la risposta operativa e la piattaforma PATHOS (*Phishing Analysis and Takedown Harmonized Operation System*), sviluppata dal Dipartimento Security & ICT Operations di PagoPA.

## Campagne phishing contro lo Stato: i primi segnali a marzo 2025

I primi segnali sono stati intercettati nel marzo 2025 grazie a un monitoraggio basato su *typosquatting* e *Google dorking*. Il team Security di PagoPA ha rilevato, tra il 20 e il 31 marzo 2025, risultati indicizzati da Google che rimandavano a SMS di *phishing* a tema PagoPA, catturati e resi pubblici da servizi gratuiti di *virtual number* per la ricezione di SMS, come OnlineSim.

![Mirko caruso cybercrime conference pago pa 6.000 campagne phishing contro lo Stato cosa abbiamo imparato](https://www.ictsecuritymagazine.com/wp-content/uploads/chrome_tKqgHHhMIa-700x393.png)

*Mirko Caruso, Cyber Crime Conference 2026*

Un dettaglio rivelatore: nelle prime campagne gli attori malevoli avevano lasciato un refuso, probabilmente residuo di campagne precedenti, indicando “Netflix” come mittente di SMS che in realtà simulavano una multa per violazione del codice della strada, con *redirect* verso il dominio “pagopa-it.com”.

![Mirko Caruso, Cyber Crime Conference pago pa 6.000 campagne phishing contro lo Stato cosa abbiamo imparato](https://www.ictsecuritymagazine.com/wp-content/uploads/chrome_mLPVCssnKW-700x394.png)

*Mirko Caruso, Cyber Crime Conference 2026*

Il *template* iniziale conteneva errori grossolani: bastava notare l’accostamento fra il logo delle Capitanerie di Porto e il *footer* “ATAC S.p.A. PagoPA”. Eppure, fin dalle prime campagne emergeva una raccolta sistematica dei dati anagrafici, destinati a essere riutilizzati in campagne successive, più mirate e personalizzate.

#### Cittadini come fattore abilitante

Fin dai primi giorni di marzo 2025 i cittadini hanno iniziato a segnalare le campagne sospette: dapprima al canale di assistenza di primo livello (L1) e poi, dal luglio 2025, a una *mailbox* dedicata, truffe@pagopa.it.

Al 29 aprile 2026 PagoPA ha registrato 46.714 segnalazioni complessive, così distribuite per *brand*:

* pagoPA: 18.651 (di cui 14.556 via telefonate, 3.756 via *email*, 339 via *web*)
* truffe@pagopa.it: 27.060
* app IO: 856
* SEND: 145
* Self Care: 2

L’introduzione della *mailbox* dedicata ha ridotto drasticamente il carico sui canali di assistenza, separando il flusso delle segnalazioni di truffa da quello dell’assistenza ordinaria.

![Mirko Caruso, Cyber Crime Conference](https://www.ictsecuritymagazine.com/wp-content/uploads/chrome_3O1SmDu6bg-700x393.png)

*Mirko Caruso, Cyber Crime Conference 2026*

Caruso ha sottolineato come il cittadino non sia più “l’anello debole” della catena, ma una sentinella attiva del territorio digitale, capace, spesso, di intercettare nuove campagne prima ancora dei servizi commerciali di *phishing intelligence*.

#### Monitoraggio attraverso Google Trends e Google Alerts

L’analisi di [Google Trends](https://trends.google.com/trends/) si è rivelata uno strumento di *early warning* particolarmente efficace. Per la *query* “pagopa truffa” si sono registrate impennate degli argomenti correlati “Multa” e “Notifica”, con concentrazioni geografiche iniziali in Valle d’Aosta, Sicilia e Lombardia. Particolarmente significativi i picchi sulla *query* anomala “pagopa netflix”, osservati il 24 e il 30 marzo 2025: coincidevano con la diffusione degli SMS che citavano impropriamente Netflix, e raccontavano di cittadini che interrogavano Google per capire cosa stesse accadendo.

Il *framework* operativo che ne è derivato si articola in quattro fasi: rilevazione dei segnali dai cittadini; aggregazione e analisi su Google Trends; *intelligence* ed *early warning* di *Cyber Threat*; azione e protezione da parte di istituzioni e aziende.

#### Evoluzione dei *template* di *phishing*

Caruso ha illustrato la progressiva sofisticazione dei *template*:

* **Low-fidelity** (campagne iniziali): raccolta anagrafica basilare prima del pagamento, con errori grafici evidenti.
* **CTA diretta**: *template* con sola *call to action* al pagamento (ad esempio “Avviso di sollecito ufficiale”), senza raccolta anagrafica preliminare.
* **High-fidelity**: a oggi il *template* più diffuso. Include riferimenti completi (sede legale, P.IVA, dicitura “Finanziato dall’Unione Europea”), loghi *corporate* e di piattaforma, e s...
---
title: Bug 0-day di Salesforce sfruttato in una sofisticata campagna di phishing
url: https://www.securityinfo.it/2023/08/03/bug-0-day-di-salesforce-sfruttato-in-una-sofisticata-campagna-di-phishing/?utm_source=rss&utm_medium=rss&utm_campaign=bug-0-day-di-salesforce-sfruttato-in-una-sofisticata-campagna-di-phishing
source: Securityinfo.it
date: 2023-08-04
fetch_date: 2025-10-04T12:03:56.171087
---

# Bug 0-day di Salesforce sfruttato in una sofisticata campagna di phishing

Aggiornamenti recenti Ottobre 3rd, 2025 6:09 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)

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

## Bug 0-day di Salesforce sfruttato in una sofisticata campagna di phishing

Ago 03, 2023  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/minacce-2/), [News](https://www.securityinfo.it/category/news/), [Phishing](https://www.securityinfo.it/category/news/phishing/), [RSS](https://www.securityinfo.it/category/rss/), [Social engineering](https://www.securityinfo.it/category/minacce-2/social-engineering/)
 [0](https://www.securityinfo.it/2023/08/03/bug-0-day-di-salesforce-sfruttato-in-una-sofisticata-campagna-di-phishing/#respond)

---

I ricercatori di Guardio hanno individuato una **[campagna phishing](https://labs.guard.io/phishforce-vulnerability-uncovered-in-salesforces-email-services-exploited-for-phishing-32024ad4b5fa) che sfruttava una vulnerabilità 0-day nei servizi email e nei server SMTP di Salesforce.** Gli attaccanti hanno usato la vulnerabilità per crear**e email di phishing nel dominio Salesforce e indurre gli utenti Facebook a fornire informazioni sul proprio account**, incluso il nome, l’indirizzo email, il numero di telefono e la password.

Il gruppo ha utilizzato il bug per nascondere le email nel traffico legittimo del gateway, superando i controlli di sicurezza.

Le email analizzate dai ricercatori informavano le vittime che il loro account Facebook era stato coinvolto in un’indagine per aver violato le condizioni del servizio. Nel corpo del messaggio c’era un **pulsante che rimandava a una finta pagina del social** e dove si richiedeva all’utente di inserire le proprie informazioni per procedere coi controlli.

![Phishing Salesforce - Credits: IgorVetushko - Depositphotos](https://www.securityinfo.it/wp-content/uploads/2023/08/Depositphotos_173487336_L.jpg)

Credits: IgorVetushko – Depositphotos

**Le email provenivano da indirizzi legittimi come @case.salesforce.com** in di superare i controlli di phishing.

Nel dettaglio, gli attaccanti hanno sfruttato una v**ulnerabilità presente nella feature “Email-to-Case” di Salesforce.** La funzionalità è pensata per convertire le email in entrata verso gli indirizzi @xxxx.case.salesforce.com in ticket Salesforce; gli attaccanti hanno approfittato di questo particolare per ricevere email di verifica dell’indirizzo creato e, una volta attivato, lo hanno **usato per inviare email di phishing in grado di superare i controlli del gateway di** **posta,** compresi i filtri anti-spam e anti-phishing.

**La pagina di phishing, inoltre, era ospitata sul dominio legittimo apps.facebook.com usato per Web Games**, il portale dei giochi di Facebook. Anche se Meta ha disabilitato la possibilità di pubblicare nuovi giochi, è comunque possibile ricevere supporto per quelli già pubblicati. Gli attaccanti sono riusciti a ottenere l’accesso ad alcuni account degli sviluppatori e sostituire al gioco la pagina di phishing.

Guardio ha individuato la campagna a fine giugno e ha contattato immediatamente Salesforce fornendole tutti i dettagli per riprodurre l’attacco. **Il 28 luglio Salesforce ha annunciato di aver risolto la vulnerabilità** e di aver aggiornato tutti i servizi coinvolti con il fix di sicurezza.

![Phishing Salesforce](https://www.securityinfo.it/wp-content/uploads/2023/08/circles-gb3c02c7a3_1920.jpg)

Pixabay

I ricercatori hanno contattato anche Meta informandola dell’abuso in atto. **Il team di Facebook ha provveduto a eliminare tutti gli account compromessi** e ha annunciato di star proseguendo con le indagini per individuare altre attività sospette.

Questa sofisticata campagna dimostra ancora una volta che le capacità degli attaccanti stanno migliorando per evadere più controlli di sicurezza. L’essere riusciti a sfruttare dei servizi legittimi per le loro attività ha reso questi cybercriminali **una minaccia da non sottovalutare**.

Se da una parte gli utenti dovrebbero prestare la **massima attenzione al contenuto delle email e non fornire mai dati personali sul web**, dall’altra parte i provider dovrebbero rafforzare le proprie linee di difesa e condurre audit periodici sulle vulnerabilità delle infrastrutture.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [0-day](https://www.securityinfo.it/tag/0-day/), [email](https://www.securityinfo.it/tag/email/), [Meta](https://www.securityinfo.it/tag/meta/), [Phishing](https://www.securityinfo.it/tag/phishing/), [Salesforce](https://www.securityinfo.it/tag/salesforce/), [SMTP](https://www.securityinfo.it/tag/smtp/), [vulnerabilità](https://www.securityinfo.it/tag/vulnerabilita/)

[Emotet e Lokibot non mollano, e nascono nuove minacce: il report di Kaspersky](https://www.securityinfo.it/2023/08/04/emotet-e-lokibot-non-mollano-e-nascono-nuove-minacce-il-report-di-kaspersky/)
[Il malware AVrecon è alla base di un enorme servizio illegale di proxy](https://www.securityinfo.it/2023/08/03/avrecon-botnet-servizio-proxy-illegale/)

---

![](https://secure.gravatar.com/avatar/25fb9b2d4cf1cb03debb642c725b4309?s=90&d=mm&r=g)

##### [Marina Londei](https://www.securityinfo.it/author/marina-londei/)

##### Articoli correlati

* [![Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/wp-content/uploads/2025/09/Gemini_Generated_Image_d4x8rid4x8rid4x8-120x85.png)](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA")

  [Firewall Cisco sotto attacco: una nuova...](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/ "Permanent link to Firewall Cisco sotto at...
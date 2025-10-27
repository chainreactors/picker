---
title: Akamai individua “BadSuccessor” per l’elevation dei privilegi su Windows Server
url: https://www.securityinfo.it/2025/05/26/akamai-individua-badsuccessor-per-lelevation-dei-privilegi-su-windows-server/?utm_source=rss&utm_medium=rss&utm_campaign=akamai-individua-badsuccessor-per-lelevation-dei-privilegi-su-windows-server
source: Securityinfo.it
date: 2025-05-27
fetch_date: 2025-10-06T22:31:08.687624
---

# Akamai individua “BadSuccessor” per l’elevation dei privilegi su Windows Server

Aggiornamenti recenti Ottobre 6th, 2025 3:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)
* [Ricerca FireMon: il 60% dei firewall non supera i controlli di conformità](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)

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

## Akamai individua “BadSuccessor” per l’elevation dei privilegi su Windows Server

Mag 26, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [Hacking](https://www.securityinfo.it/category/approfondimenti/hacking/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/approfondimenti/minacce/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/05/26/akamai-individua-badsuccessor-per-lelevation-dei-privilegi-su-windows-server/#respond)

---

I ricercatori di **Akamai** [hanno individuato](https://www.akamai.com/blog/security-research/abusing-dmsa-for-privilege-escalation-in-active-directory) di recente “**BadSuccessor**“, una tecnica di attacco che sfrutta la feature dei **delegated Managed Service Account (dMSA)** di **Windows Server 2025**per effettuare l’**elevation dei privilegi**.

Il dSMA è un account di servizio gestito delegato che viene utilizzato per consentire agli utenti di applicare modifiche minime all’applicazione, disabilitando le password dell’account del servizio originale. Solitamente questo account viene usato per rimpiazzare gli account legacy esistenti, di fatto effettuando una migrazione dei permessi del profilo legacy.

![BadSuccessor](https://www.securityinfo.it/wp-content/uploads/2025/05/cyber-security-3411476_1920.jpg)

Analizzando il processo di migrazione, i ricercatori di Akamai hanno individuato una **vulnerabilità che consente a un attaccante di prendere il controllo del dominio** effettuando un’escalation dei privilegi. “*Tutto ciò che serve a un attaccante per eseguire questo attacco è un’autorizzazione benigna su qualsiasi unità organizzativa del dominio, un’autorizzazione che spesso passa inosservata*” ha affermato Yuval Gordon, ricercatore di sicurezza di Akamai.

Il problema è stato riscontrato durante la fase di autenticazione del processo di migrazione: in questo step viene generato il PAC, un certificato di attribuzione dei certificati. Nel caso della migrazione al dMSA, il PAC include non solo l’ID del nuovo account, ma anche quello dell’account originale e di tutti i gruppi a cui apparteneva.

I ricercatori hanno dimostrato che è possibile **manipolare gli attributi della migrazione per ottenere i permessi di qualsiasi altro account**, non solo quello di partenza, quindi anche quelli con privilegi elevati. La tecnica, denominata “BadSuccessor”, funziona con qualsiasi tipo di account, inclusi i Domain Admins.

Quel che è peggio è che un attaccante non ha necessità di effettuare un’effettiva migrazione per eseguire l’attacco: gli basta impostare due specifici attributi dell’account per definire l’ID dell’account “padre” e fingere che sia avvenuta una migrazione. Per di più non serve avere permessi sull’account di partenza, ma è **sufficiente possedere i permessi di scrittura sugli attributi di un dMSA.**Nel caso non ci fossero account di tipo dMSA, gli attaccanti potrebbero crearne di nuovi su cui hanno tutti i permessi e modificarli a loro piacimento per eseguire la tecnica.

![](https://www.securityinfo.it/wp-content/uploads/2025/04/13311414_v627-aew-41-technologybackground-scaled.jpg)

## La risposta di Microsoft a BadSuccessor

Il team di Akamai ha informato **Microsoft** della nuova tecnica. Pur riconoscendo la validità di BadSuccessor, la compagnia ritiene che **non abbia un rischio così elevato da richiedere un intervento urgente.**

“*Secondo Microsoft, un exploit di successo implica che l’attaccante abbia già dei permessi specifici sull’oggetto dMSA, il che è indicativo di privilegi elevati*“. I ricercatori hanno risposto evidenziando che è possibile per un attaccante creare un nuovo oggetto dMSA, ma Microsoft ha risposto citando della documentazione tecnica su *CreateChild* per evidenziare rischi e best practice di utilizzo.

Il team di Akamai si è detta in disaccordo con la risposta di Microsoft e ritiene che la compagnia non abbia realmente compreso le implicazioni di BadSuccessor. “*Q**uesta vulnerabilità introduce un exploit precedentemente sconosciuto e ad alto impatto che permette a qualsiasi utente con i permessi CreateChild su un’unità organizzativa di compromettere qualsiasi utente del dominio** e ottenere un potere simile al privilegio Replicating Directory Changes utilizzato per eseguire attacchi DCSync. Inoltre, non abbiamo trovato alcuna indicazione che le pratiche o gli strumenti attuali del settore segnalino l’accesso a CreateChild – o, più specificamente, CreateChild per i dMSA – come un problema critico. Riteniamo che ciò evidenzi la furtività e la gravità del problema*“.

Per mitigare gli impatti Akamai consiglia di controllare quali gruppi di account possono creare dMSA e **limitare questo permesso soltanto agli utenti amministratori.**

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [account privilegiati](https://www.securityinfo.it/tag/account-privilegiati/), [Akamai](https://www.securityinfo.it/tag/akamai/), [BadSuccessor](https://www.securityinfo.it/tag/badsuccessor/), [dMSA](https://www.securityinfo.it/tag/dmsa/), [escalation dei privilegi](https://www.securityinfo.it/tag/escalation-dei-privilegi/), [Microsoft Server 2025](https://www.securityinfo.it/tag/microsoft-server-2025/)

[Acronis: l'italia traina la crescita MSP](https://www.securityinfo.it/2025/05/27/acronis-litalia-traina-la-crescita-msp/)
[CERT-AGID 17 – 23 maggio: l’Agenzia delle Entrate e PagoPA sotto attacco](https://www.securityinfo.it/2025/05/26/cert-agid-17-23-maggio...
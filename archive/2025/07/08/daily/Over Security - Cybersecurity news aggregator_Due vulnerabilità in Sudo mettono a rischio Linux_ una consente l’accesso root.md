---
title: Due vulnerabilità in Sudo mettono a rischio Linux: una consente l’accesso root
url: https://www.securityinfo.it/2025/07/04/due-vulnerabilita-in-sudo-mettono-a-rischio-linux-una-consente-laccesso-root/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-08
fetch_date: 2025-10-06T23:49:50.581418
---

# Due vulnerabilità in Sudo mettono a rischio Linux: una consente l’accesso root

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

## Due vulnerabilità in Sudo mettono a rischio Linux: una consente l’accesso root

Lug 04, 2025  [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/ "Articoli scritti da Giancarlo Calzetta")
 [News](https://www.securityinfo.it/category/news/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/07/04/due-vulnerabilita-in-sudo-mettono-a-rischio-linux-una-consente-laccesso-root/#respond)

---

**Scoperti due gravi bug in Sudo**, il celebre strumento da riga di comando utilizzato nei sistemi Linux e Unix-like per l’esecuzione di comandi con privilegi elevati. Le vulnerabilità, segnalate dal ricercatore Rich Mirch di Stratascale, potrebbero essere sfruttate da utenti locali non privilegiati per **ottenere accesso root** su macchine vulnerabili. Una delle due falle, la più critica, ha ottenuto un punteggio **CVSS di 9.3**.

![](https://www.securityinfo.it/wp-content/uploads/2025/07/Linux_ferito_CG-1024x683.png)

Il progetto Sudo ha corretto entrambe le falle nella versione **1.9.17p1**, rilasciata a fine giugno 2025, dopo una disclosure responsabile avvenuta lo scorso 1 aprile. I principali vendor Linux, tra cui Ubuntu, Red Hat, Debian e SUSE, hanno già pubblicato **avvisi di sicurezza** e aggiornamenti correttivi.

### CVE-2025-32463: escalation di privilegi tramite `chroot`

La vulnerabilità più grave tra le due è **CVE-2025-32463**, che coinvolge l’opzione `-R` di Sudo, usata per cambiare la root directory durante l’esecuzione di un comando. **Un utente locale può creare una directory arbitraria contenente un file `/etc/nsswitch.conf` manipolato**, sfruttando il fatto che il comando Sudo, in alcuni casi, carica librerie condivise sulla base di quella configurazione.

**Questo permette l’esecuzione di codice arbitrario con privilegi di root**, anche se l’utente non dispone di alcuna regola nel file sudoers. **La configurazione predefinita di Sudo è vulnerabile**, e la falla non richiede complesse interazioni o conoscenze approfondite per essere sfruttata.

Todd C. Miller, maintainer del progetto Sudo, ha annunciato che l’opzione chroot sarà completamente rimossa nelle prossime release, definendola “intrinsecamente soggetta a errori” e difficilmente difendibile in modo sicuro.

### CVE-2025-32462: un bug silenzioso che esiste da oltre 12 anni

Meno pericolosa ma comunque degna di nota è **CVE-2025-32462**, con punteggio CVSS pari a 2.8. Questa vulnerabilità riguarda l’uso dell’opzione `-h` per specificare un host alternativo nel comando Sudo. **Se il file sudoers include regole che si applicano a macchine diverse dalla corrente**, un utente potrebbe eseguire comandi destinati a un altro host direttamente sulla macchina locale.

Il bug è presente **dal 2013**, anno in cui fu introdotto il supporto per l’opzione host nel comando Sudo. La falla **può avere conseguenze significative in ambienti dove il file sudoers è condiviso su più sistemi**, come accade spesso nelle infrastrutture basate su LDAP o su file sudoers centralizzati tramite SSSD.

### Distribuzioni coinvolte e mitigazioni

Entrambe le falle sono state risolte nella versione **1.9.17p1 di Sudo**. Le distribuzioni che hanno rilasciato patch per **CVE-2025-32463** includono Ubuntu, Debian, Red Hat, SUSE, Gentoo, Amazon Linux e Alpine Linux. La vulnerabilità **CVE-2025-32462** è stata invece corretta anche su AlmaLinux 8 e 9 e Oracle Linux.

**Tutti gli utenti Linux sono invitati ad aggiornare i pacchetti Sudo il prima possibile**, in particolare se utilizzano configurazioni avanzate o ambienti multi-host, dove le vulnerabilità possono avere impatti più estesi.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [chroot](https://www.securityinfo.it/tag/chroot/), [CVE-2025-32462](https://www.securityinfo.it/tag/cve-2025-32462/), [CVE-2025-32463](https://www.securityinfo.it/tag/cve-2025-32463/), [escalation privilegi](https://www.securityinfo.it/tag/escalation-privilegi/), [nsswitch.conf](https://www.securityinfo.it/tag/nsswitch-conf/), [patch sicurezza](https://www.securityinfo.it/tag/patch-sicurezza/), [root access](https://www.securityinfo.it/tag/root-access/), [sicurezza Linux](https://www.securityinfo.it/tag/sicurezza-linux/), [Sudo](https://www.securityinfo.it/tag/sudo/), [vulnerabilità Linux](https://www.securityinfo.it/tag/vulnerabilita-linux/)

[Un cartello messicano ha spiato l'FBI hackerando i suoi dispositivi](https://www.securityinfo.it/2025/07/04/un-cartello-messicano-ha-spiato-l-fbi-hackerando-i-suoi-dispositivi/)
[IconAds: quando le app fantasma diventano portali pubblicitari](https://www.securityinfo.it/2025/07/03/iconads-quando-le-app-fantasma-diventano-portali-pubblicitari/)

---

![](https://secure.gravatar.com/avatar/d6a6ecdad542d883704003e541413ca8?s=90&d=mm&r=g)

##### [Giancarlo Calzetta](https://www.securityinfo.it/author/giancarlo_security/)

##### Articoli correlati

* [![Qualcomm rilascia aggiornamenti per 17 vulnerabilità, ma soffre di altri bug 0-day](https://www.securityinfo.it/wp-content/uploads/2023/10/Depositphotos_424295152_L-120x85.jpg)](https://www.securityinfo.it/2023/10/05/qualcomm-rilascia-aggiornamenti-per-17-vulnerabilita-ma-soffre-di-altri-bug-0-day/ "Qualcomm rilascia aggiornamenti per 17 vulnerabilità, ma soffre di altri bug 0-day")

  [Qualcomm rilascia aggiornamenti per 17...](https://www.securityinfo.it/2023/10/05/qualcomm-rilascia-aggiornamenti-per-17-vulnerabilita-ma-soffre-di-altri-bug-0-day/ "Permanent link to Qualcomm rilascia aggiornamenti per 17 vulnerabilità, ma soffre di altri bug 0-day")

  Ott 05, 2023  [0](https://www.securityinfo.it/2023/10/05/qualcomm-rilascia-aggiornamenti-per-17-vulnerabilita-ma-soffre-di-altri-bug-0-day/#respond)
* [![LastPass ha nuovi problemi e gli utenti insorgono. È ora di cambiare password manager?](https:...
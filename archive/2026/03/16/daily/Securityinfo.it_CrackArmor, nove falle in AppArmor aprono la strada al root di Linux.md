---
title: CrackArmor, nove falle in AppArmor aprono la strada al root di Linux
url: https://www.securityinfo.it/2026/03/16/crackarmor-nove-falle-in-apparmor-aprono-la-strada-al-root-di-linux/?utm_source=rss&utm_medium=rss&utm_campaign=crackarmor-nove-falle-in-apparmor-aprono-la-strada-al-root-di-linux
source: Securityinfo.it
date: 2026-03-16
fetch_date: 2026-03-17T04:17:06.480519
---

# CrackArmor, nove falle in AppArmor aprono la strada al root di Linux

Aggiornamenti recenti Marzo 16th, 2026 2:50 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [CrackArmor, nove falle in AppArmor aprono la strada al root di Linux](https://www.securityinfo.it/2026/03/16/crackarmor-nove-falle-in-apparmor-aprono-la-strada-al-root-di-linux/)
* [I sistemi multi-agent aggirano controlli, rubano segreti ed esfiltrano](https://www.securityinfo.it/2026/03/13/incredibile-come-i-sistemi-multi-agent-possano-aggirare-i-controlli-rubare-segreti-e-diventare-minacce/)
* [Rapporto Clusit 2026: gli attacchi cyber crescono del 49%](https://www.securityinfo.it/2026/03/11/rapporto-clusit-2026-gli-attacchi-cyber-crescono-del-49/)
* [Plug-in di Chrome cambiano proprietà e diventano malware](https://www.securityinfo.it/2026/03/10/plug-in-di-chrome-cambiano-proprieta-e-diventano-malware/)
* [InstallFix: false guide di installazione CLI per installare infostealer](https://www.securityinfo.it/2026/03/06/installfix-false-guide-di-installazione-cli-per-installare-infostealer/)

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

## CrackArmor, nove falle in AppArmor aprono la strada al root di Linux

Mar 16, 2026  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/), [Vulnerabilità](https://www.securityinfo.it/category/approfondimenti/vulnerabilita-approfondimenti/)
 [0](https://www.securityinfo.it/2026/03/16/crackarmor-nove-falle-in-apparmor-aprono-la-strada-al-root-di-linux/#respond)

---

Secondo una ricerca di Qualys, il pacchetto di vulnerabilità individuato in **AppArmor** consente a un utente locale non privilegiato di **manipolare i profili di sicurezza, aggirare restrizioni del kernel, arrivare all’elevazione di privilegi fino a root e indebolire l’isolamento dei container**. Il problema, inoltre, non è confinato a un caso di laboratorio marginale: Qualys afferma che la falla esiste **dal kernel Linux v4.11, quindi dal 2017**, e riguarda distribuzioni in cui AppArmor è abilitato o integrato, tra cui **Ubuntu, Debian e SUSE**.

![](https://www.securityinfo.it/wp-content/uploads/2026/03/Vulnerabilità-Linux-1024x683.png)

L’impatto potenziale è molto ampio. Qualys stima che **oltre 12,6 milioni di sistemi enterprise Linux** operino con AppArmor abilitato di default, e questo rende CrackArmor una vulnerabilità particolarmente rilevante per server, ambienti cloud, cluster Kubernetes, infrastrutture edge e workload containerizzati. Il fatto che **non siano ancora stati assegnati identificativi CVE** non deve trarre in inganno: sia Qualys sia Canonical chiariscono che si tratta di vulnerabilità reali, già corrette o in fase di distribuzione tramite aggiornamenti kernel e mitigazioni userspace, ma non ancora formalmente catalogate con un ID pubblico.

**Il cuore del problema: un “confused deputy” che trasforma AppArmor da barriera a punto d’ingresso**

Il difetto più importante individuato da Qualys è una vulnerabilità strutturale definita **“confused deputy”**. In pratica, un utente locale senza privilegi può sfruttare il comportamento di componenti fidati del sistema per **caricare, sostituire o rimuovere profili AppArmor arbitrari** attraverso pseudo-file come /sys/kernel/security/apparmor/.load, .replace e .remove. Da qui si aprono diversi scenari: si possono rimuovere profili che proteggono servizi chiave come cupsd o rsyslogd, si possono caricare profili “deny all” capaci di bloccare un servizio come sshd, oppure si possono creare profili che **aggirano le restrizioni sui namespace utente**, restituendo a un account locale capacità che non dovrebbe avere.

È questo il tassello che rende pericolose anche le altre falle. Canonical spiega che **su host senza workload containerizzati** lo sfruttamento richiede normalmente la cooperazione di un’applicazione privilegiata, ad esempio un binario setuid come SU, mentre **in ambienti che eseguono container potenzialmente ostili** le vulnerabilità del kernel AppArmor possono teoricamente portare anche a **container escape**, senza bisogno di una controparte privilegiata in userspace. Canonical precisa che questa evasione non è stata dimostrata pubblicamente nella pratica al momento della pubblicazione, ma il rischio teorico esiste e per questo raccomanda l’applicazione degli aggiornamenti kernel come remediation primaria.

**Tutte le vulnerabilità di CrackArmor, una per una**

Il pacchetto CrackArmor comprende **nove vulnerabilità nel codice del kernel AppArmor**. Qualys ne descrive in dettaglio alcune e cita le altre attraverso la serie di patch upstream associate alla correzione. La prima è il già citato **confused deputy**, che permette a un utente non privilegiato di gestire profili AppArmor arbitrari e quindi di abbassare le difese del sistema o di creare le condizioni per exploit più avanzati. Qualys lo definisce la vulnerabilità fondamentale su cui poggia l’intera catena di attacco.

La seconda è una **out-of-bounds read in unpack\_pdb**, corretta dalla patch “validate DFA start states are in bounds in unpack\_pdb”. In sostanza, il parser dei DFA di AppArmor può accedere a memoria fuori dai limiti previsti. Qualys non la espande quanto altre, ma la include espressamente tra le nove falle corrette.

La terza è una **memory leak in verify\_header**, anch’essa citata direttamente nella lista delle patch. Non è la più pericolosa della serie in termini di exploitability immediata, ma resta parte del pacchetto di problemi che indeboliscono l’affidabilità del parser dei profili AppArmor.

La quarta è una **uncontrolled recursion** nel meccanismo di rimozione dei profili. Qualys spiega che la rimozione di sottoprofili profondamente annidati può portare a **esaurimento dello stack del kernel** e quindi a **kernel panic e crash completo del sistema**. Secondo i ricercatori, questo specifico bug sembra essere “solo” una vulnerabilità di **denial of service**, non una LPE diretta, perché la protezione CONFIG\_VMAP\_STACK impedirebbe il salto oltre la guard page dello stack. Resta però un problema molto serio per la disponibilità dei sistemi Linux esposti a utenti locali non fidati.

La quinta è una **out-of-bounds read in match\_char()**, descritta da Qualys nel dettaglio. Quando AppArmor confronta un pathname con una propria espressione regolare, un bug nella macro può far avanzare il puntatore oltre il byte nullo terminale e quindi oltre il buffer allocato. Qualys mostra come questa condizione possa essere trasformata in una **disclosure di memoria del kernel**, fino a circa **64 KB**, compresi **puntatori del kernel randomizzati da KASLR**. Questo significa che l’exploit non si limita a leggere memoria in modo improprio, ma ...
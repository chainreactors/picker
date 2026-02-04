---
title: NTLM verso lo “switch-off”: Microsoft si prepara a bloccarlo di default
url: https://www.securityinfo.it/2026/02/03/ntlm-verso-lo-switch-off-microsoft-si-prepara-a-bloccarlo-di-default/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-03
fetch_date: 2026-02-04T04:07:56.786657
---

# NTLM verso lo “switch-off”: Microsoft si prepara a bloccarlo di default

Aggiornamenti recenti Febbraio 3rd, 2026 4:00 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [NTLM verso lo “switch-off”: Microsoft si prepara a bloccarlo di default](https://www.securityinfo.it/2026/02/03/ntlm-verso-lo-switch-off-microsoft-si-prepara-a-bloccarlo-di-default/)
* [Abusato il sistema di update eScan per inviare malware multistage](https://www.securityinfo.it/2026/02/02/abusato-il-sistema-di-update-escan-per-inviare-malware-multistage/)
* [Hugging Face sfruttato per distribuire un trojan Android](https://www.securityinfo.it/2026/01/30/hugging-face-sfruttato-per-distribuire-un-trojan-android/)
* [OpenSSL ha fixato 12 vulnerabilità scoperte da AISLE](https://www.securityinfo.it/2026/01/29/openssl-ha-fixato-12-vulnerabilita-scoperte-da-aisle/)
* [PackageGate: trovati sei bug zero-day nei package manager, ma NPM non interviene](https://www.securityinfo.it/2026/01/27/packagegate-trovati-sei-bug-zero-day-nei-package-manager-ma-npm-non-interviene/)

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

## NTLM verso lo “switch-off”: Microsoft si prepara a bloccarlo di default

Feb 03, 2026  [Redazione news](https://www.securityinfo.it/author/redazione-news/ "Articoli scritti da Redazione news")
 [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Tecnologia](https://www.securityinfo.it/category/news/tecnologia-news/)
 [0](https://www.securityinfo.it/2026/02/03/ntlm-verso-lo-switch-off-microsoft-si-prepara-a-bloccarlo-di-default/#respond)

---

Microsoft ha comunicato che l’autenticazione NTLM verrà disabilitata di default nelle future versioni, lasciando comunque il protocollo presente nel sistema operativo e riattivabile solo tramite policy quando davvero necessario.

![](https://www.securityinfo.it/wp-content/uploads/2026/02/Lucchetto_Security.png)

**Perché NTLM è un bersaglio: relay, replay e pass-the-hash**

**Il problema di NTLM non è soltanto la sua età, ma la sua esposizione a classi di attacchi che si innestano bene in ambienti enterprise moderni.** Microsoft, e diversi esperti, citano esplicitamente relay, replay e man-in-the-middle come le “famiglie” di tecniche che diventano particolarmente pericolose quando un attore malevolo riesce a posizionarsi “in mezzo” a una conversazione di rete o a sfruttare autenticazioni legacy per muoversi lateralmente. In termini di tassonomie operative, il tema si collega a pattern noti come l’Adversary-in-the-Middle e il pass-the-hash, che continuano a comparire un po’ troppo spesso quando si fa la forensica di un attacco proprio perché “funzionano” quando l’azienda mantiene queste dipendenze.

**La roadmap in tre fasi: audit, nuove capability Kerberos, poi blocco di default**

**Microsoft ha strutturato la transizione in tre fasi per ridurre il rischio senza provocare un blackout improvviso di applicazioni e servizi.** La prima fase ruota attorno a capacità di auditing potenziate, già disponibili su Windows 11 24H2 e Windows Server 2025, utili a capire dove e perché NTLM viene ancora usato. La seconda fase, prevista per la seconda metà del 2026, introduce nuove funzionalità pensate per “chiudere” i buchi che oggi portano al fallback su NTLM, tra cui IAKerb e un Local Key Distribution Center (Local KDC). La terza fase è quella decisiva: nelle future release, l’NTLM di rete sarà disabilitato per impostazione predefinita, pur restando riabilitabile tramite policy per scenari legacy inevitabili.

**“Disabilitato di default” non significa “rimosso”: cosa cambia operativamente**

Microsoft sottolinea che non si tratta ancora della rimozione completa del protocollo, ma di una consegna del sistema in uno stato più sicuro “by default”, dove l’OS preferisce alternative moderne e Kerberos-based. Questo permetterà di usare NTLM ancora, ma sarà una scelta chiara dell’utente e non un possibile ripiego automatico in caso di sfruttamento di una vulnerabilità o un derivato di vecchie configurazioni di cui si è persa memoria.

**In molte reti, infatti, l’uso di NTLM non è “intenzionale”, ma il risultato di condizioni che impediscono a Kerberos di funzionare come previsto.** Microsoft, nella propria serie di hardening su Active Directory, entra nel dettaglio delle cause tipiche: problemi di connettività verso i domain controller, uso di account locali, errori o assenza di Service Principal Name (SPN), accesso alle risorse via indirizzo IP invece che tramite FQDN, oppure applicazioni configurate (o addirittura hardcoded) per chiamare NTLM. Ed è proprio qui che la roadmap prova a intervenire: IAKerb nasce per gestire scenari dove il client non ha una visione completa, mentre LocalKDC mira a ridurre l’uso di NTLM in autenticazioni basate su account locali, storicamente uno dei punti più difficili da eliminare.

**Audit potenziato: visibilità prima del blocco**

**La parte più importante, oggi, è ottenere telemetria affidabile su dove NTLM sta ancora transitando.** Microsoft indica esplicitamente che Windows 11 24H2 e Windows Server 2025 offrono auditing più ricco per identificare dipendenze e priorità di remediation, evitando di scoprire “a produzione ferma” che un pezzo di infrastruttura si appoggia ancora al legacy. Nella pratica, la stessa documentazione Microsoft enfatizza la necessità di mappare le dipendenze applicative e validare i workload critici con Kerberos, iniziando a testare configurazioni “NTLM-off” in ambienti non produttivi.

**Questo implica un uso approfondito dei log: NTLM va trattato come un “debito tecnico misurabile”, non come un dettaglio di protocollo.** Nei suggerimenti sull’hardening dello scenario, Microsoft cita famiglie di eventi utili a capire chi autentica, verso cosa e con quale versione negoziata; nelle build più recenti (24H2/Server 2025) compaiono anche eventi più dettagliati che aiutano a ricostruire il motivo del fallback e, in alcuni casi, il processo coinvolto. L’obiettivo operativo è trasformare l’eliminazione di NTLM in un percorso governato: riduzione progressiva, controllo dell’impatto e blocchi mirati dove non esistono più dipendenze.

**NTLMv1: già fuori gioco, ma attenzione ai “derivati” e alle eredità crittografiche**

**Il percorso di dismissione è iniziato da tempo: NTLMv1 risulta già rimosso in Windows 11 24H2 e Windows Server 2025, ma restano casi in cui sopravvivono elementi di crittografia legacy.** [Microsoft descrive esplicitamente](https://support.microsoft.com/en-us/topic/upcoming-changes-to-ntlmv1-in-windows-11-version-24h2-and-windows-server-2025-c0554217-cdbc-420f-b47c-e02b2db49b2e) scenari in cui “rimasugli” di NTLMv1 possono ancora emergere, ad esempio in contesti legati a MS-CHAPv2 in ambienti domain-joined, e introduce chiavi di registro e log dedicati per passare da una modalità di audit a una di enforcement. La timeline pubblica include anche un punto rilevante: a ottobre 2026, in assenza di configurazione esplici...
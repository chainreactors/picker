---
title: KSMBD, due RCE da CVSS 9,0 nel kernel Linux: fix nei rami dei maintainer, non in una release
url: https://www.ictsecuritymagazine.com/notizie/linux-ksmbd-due-rce-zdi-patch/
source: ICT Security Magazine
date: 2026-10-23
fetch_date: 2026-10-24T06:47:59.598480
---

# KSMBD, due RCE da CVSS 9,0 nel kernel Linux: fix nei rami dei maintainer, non in una release

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security.webp)](https://www.ictsecuritymagazine.com/)

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
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://eventi.ictsecuritymagazine.com/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security.webp)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026-1440.webp)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![linux_ksmbd_rce_cover_960x750_light](https://www.ictsecuritymagazine.com/wp-content/uploads/linux_ksmbd_rce_cover_960x750_light.webp)

# KSMBD, due RCE da CVSS 9,0 nel kernel Linux: fix nei rami dei maintainer, non in una release

A cura di:[Redazione](#molongui-disabled-link)  Ore 23 Ottobre 202623 Ottobre 2026

Due vulnerabilità di esecuzione di codice da remoto in **KSMBD**, il server SMB integrato nel kernel Linux, sono state rese pubbliche il 21 ottobre 2026 sulle liste di sviluppo del kernel, prima che esistesse una release corretta. Entrambe hanno punteggio CVSS 9,0 assegnato dalla Zero Day Initiative (ZDI) di Trend Micro, non dal database NVD, e nessuna ha ancora un identificativo CVE. I maintainer indicano per entrambe un fix in un proprio ramo di sviluppo; nessuno dei due è nel kernel mainline.

## Le due vulnerabilità

La pagina degli [advisory ZDI in arrivo](https://www.zerodayinitiative.com/advisories/upcoming/) elenca ZDI-CAN-33774 e ZDI-CAN-33549 come vulnerabilità del vendor “Linux”, con data di inserimento 21 ottobre 2026 e scadenza di divulgazione al 18 febbraio 2027. La pagina non nomina KSMBD: i dettagli tecnici si leggono nei report inviati alle liste del kernel, entrambi con vettore
`AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H`
.

**ZDI-CAN-33774** riguarda la gestione del protocollo in fase di negoziazione. Il gestore delle operazioni della connessione viene scelto quando la richiesta è accodata e letto quando viene elaborata; una richiesta SMB1 breve, seguita da una SMB2 nello stesso invio TCP, può essere quindi trattata con le funzioni SMB2 e letta oltre la fine del proprio buffer. Il report indica anche un percorso di scrittura fuori dai limiti e conclude che l’innesco richiede una *race condition* e una condivisione ad accesso *guest*.

**ZDI-CAN-33549** riguarda SMB Direct, il trasporto su RDMA. Un *integer underflow* nel calcolo della lunghezza dei descrittori di buffer fa scrivere oltre la memoria allocata. Il report indica come requisiti un dispositivo RDMA (nel test il driver software rxe), una condivisione scrivibile e SMB Direct attivo, e include script di riproduzione e sorgente di un client di prova. La prova è stata eseguita su un kernel 7.3-rc3 con una condivisione *guest*. Il credito è di Hyeontae Lee, che lavora con la TrendAI Zero Day Initiative.

## Stato delle correzioni

Per ZDI-CAN-33774 il maintainer di KSMBD Namjae Jeon ha risposto sulla lista il 22 ottobre che il problema è già corretto, indicando il [commit 68f410fa](https://git.kernel.org/pub/scm/linux/kernel/git/linkinjeon/smb.git/commit/?id=68f410faedaf6ee74d81e574733c50ebcc1bd8ed), presente nel suo albero: il codice attende il completamento della negoziazione prima di leggere un altro pacchetto. Il commit descrive la stessa dinamica del report; che corregga proprio quel difetto è l’indicazione del maintainer.

Per ZDI-CAN-33549 Stefan Metzmacher, responsabile di SMB Direct, ha chiesto al ricercatore di provare il ramo
`for-7.5/smbdirect`
del proprio repository, scrivendo di ritenere che il problema sia già risolto lì. È un’ipotesi del maintainer, non un fix confermato.

Nessuno dei due difetti ha un CVE, che il progetto kernel assegna dopo un fix in un ramo stabile. Il ramo mainline non li contiene, e il percorso verso i kernel delle distribuzioni richiede di norma settimane dopo l’accettazione upstream.

## Perché i report sono finiti su liste pubbliche

I report sono stati inviati all’indirizzo privato di sicurezza del kernel con le liste pubbliche in copia, senza patch. Greg Kroah-Hartman ha risposto nel thread di ZDI-CAN-33774: “And again, no patch, and a public list?”. [Phoronix](https://www.phoronix.com/news/LKML-New-Trend-Vulnerabilities) parla di un invio “seemingly an accident”. The Hacker News attribuisce la scelta alla documentazione di sicurezza del kernel aggiornata a maggio 2026 sui bug trovati da strumenti di intelligenza artificiale; il thread non lo conferma e la documentazione non è stata verificata.

## Chi è esposto

KSMBD non è attivo di default sulle principali distribuzioni; The Hacker News riporta che Red Hat Enterprise Linux non lo include. Sono esposti NAS, sistemi embedded e file server dove è stato abilitato al posto di Samba in *userspace*. Per ZDI-CAN-33549 serve anche un dispositivo RDMA. Il punto critico è la tempistica: la descrizione dei difetti, e per SMB Direct il codice per riprodurre la corruzione di memoria, sono pubblici prima di una release corretta. Sul fronte kernel il magazine ha già trattato [DirtyClone](https://www.ictsecuritymagazine.com/notizie/dirtyclone-cve-2026-43503-lpe-kernel-linux/); qui la superficie è raggiungibile dalla rete.

## Cosa fare subito

Verificare se il modulo è attivo con
`lsmod | grep ksmbd`
e
`systemctl status ksmbd`
, e controllare se la porta 445 è servita da KSMBD anziché da Samba. Dove non serve, fermarlo e inserirlo in *blacklist*. Dove serve, limitare la porta 445 con *firewall* a segmenti fidati ed eliminare le condivisioni ad accesso *guest*; il costo operativo è l’interruzione delle condivisioni servite dal kernel. Per SMB Direct, controllare la presenza di dispositivi RDMA. Non risultano mitigazioni ufficiali del progetto kernel...
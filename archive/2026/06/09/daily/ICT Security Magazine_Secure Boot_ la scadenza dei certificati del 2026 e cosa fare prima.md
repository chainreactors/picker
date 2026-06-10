---
title: Secure Boot: la scadenza dei certificati del 2026 e cosa fare prima
url: https://www.ictsecuritymagazine.com/cyber-security/secure-boot-scadenza-2026/
source: ICT Security Magazine
date: 2026-06-09
fetch_date: 2026-06-10T06:17:06.465149
---

# Secure Boot: la scadenza dei certificati del 2026 e cosa fare prima

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

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Secure Boot la scadenza dei certificati del 2026 e cosa fare prima](https://www.ictsecuritymagazine.com/wp-content/uploads/Secure-Boot-la-scadenza-dei-certificati-del-2026-e-cosa-fare-prima-2.png)

# Secure Boot: la scadenza dei certificati del 2026 e cosa fare prima

A cura di:[Redazione](#molongui-disabled-link)  Ore 9 Giugno 20268 Giugno 2026

A fine giugno 2026 alcuni dei certificati che reggono Secure Boot, il meccanismo che protegge l’avvio dei PC Windows, raggiungono la scadenza dopo quindici anni di servizio. Non è un dettaglio da amministratori di sistema: riguarda gran parte del parco macchine Windows e tocca il livello più delicato della sicurezza, quello che si gioca prima ancora che il sistema operativo si avvii. Il Patch Tuesday del 9 giugno è l’ultima finestra mensile ordinaria prima della scadenza, e questo lo rende un appuntamento da non mancare. Vediamo cosa scade davvero, cosa succede a chi non si prepara e quali passi compiere subito.

## Che cos’è Secure Boot e cosa scade

Secure Boot è una funzione dello standard UEFI (Unified Extensible Firmware Interface, il firmware che ha sostituito il vecchio BIOS) che verifica, all’accensione, la firma digitale dei componenti caricati durante l’avvio. Se la firma non corrisponde a un’autorità di certificazione (CA, Certificate Authority) considerata attendibile dal firmware, il componente non viene eseguito. È la barriera pensata per fermare i *bootkit*, i malware che si annidano nelle prime fasi di avvio per ottenere il controllo della macchina prima delle difese tradizionali, come l’archivio di ICT Security Magazine documenta da tempo analizzando casi storici di [bootkit](https://www.ictsecuritymagazine.com/articoli/i-bootkit-non-sono-morti-il-ritorno-di-pitou/).

La catena di fiducia si appoggia a certificati emessi da Microsoft nel 2011 e preinstallati nel firmware della maggior parte dei dispositivi. Secondo la [documentazione Microsoft](https://support.microsoft.com/en-us/topic/windows-secure-boot-certificate-expiration-and-ca-updates-7ff40d33-95dc-4c3c-8725-a9b95457578e), tre certificati arrivano a fine validità nel 2026: il *Microsoft Corporation KEK CA 2011*, che gestisce la chiave di scambio (KEK, Key Exchange Key) usata per aggiornare i database di Secure Boot, scade il 24 giugno 2026; il *Microsoft Corporation UEFI CA 2011*, che firma componenti di terze parti e *option ROM*, scade il 27 giugno 2026; il *Microsoft Windows Production PCA 2011*, che firma il Windows Boot Manager vero e proprio, scade più avanti, il 19 ottobre 2026.

## Cosa succede dopo la scadenza

Qui occorre evitare l’allarmismo, ma anche la sottovalutazione. I dispositivi che alla scadenza non avranno ricevuto i nuovi certificati continueranno ad accendersi, a funzionare e a ricevere i normali aggiornamenti di Windows. Non si tratta quindi di un blocco improvviso. Il problema è un altro e più sottile: quelle macchine smetteranno di poter ricevere i nuovi aggiornamenti relativi all’avvio sicuro. Niente più aggiornamenti del Windows Boot Manager, niente aggiornamenti dei database di Secure Boot, niente nuove voci nella lista di revoca (DBX) e, soprattutto, nessuna mitigazione per le vulnerabilità di avvio scoperte in futuro.

In pratica, un parco macchine fermo ai certificati del 2011 resta esposto alla prossima generazione di minacce a livello *boot*. La memoria di attacchi come BlackLotus, capace di aggirare Secure Boot, mostra perché la capacità di distribuire rapidamente nuove revoche e contromisure sia un presidio di sicurezza vivo e non un dettaglio formale. La conformità che funziona è quella che resta aggiornabile nel tempo, non quella congelata a una data.

La differenza tra utente domestico e organizzazione, qui, è sostanziale. Sul singolo PC consumer l’aggiornamento avviene in modo trasparente, purché il dispositivo riceva regolarmente gli aggiornamenti di Windows. In azienda il quadro è più complesso: il rischio non è il blocco operativo immediato, ma l’accumulo silenzioso di un debito di sicurezza che si manifesta solo quando emerge la prossima vulnerabilità di avvio e ci si accorge che le mitigazioni non possono più essere applicate. È il tipo di esposizione che non compare nei cruscotti di disponibilità dei sistemi e che per questo viene scoperta tardi, spesso durante un incidente o un audit. Tracciare lo stato dei certificati diventa quindi un indicatore di postura da inserire nei controlli periodici, accanto al normale *patch management*.

## I nuovi certificati del 2023

La soluzione passa dall’adozione della nuova famiglia di certificati emessi nel 2023, che sono quattro. Il *Windows UEFI CA 2023* sostituisce il certificato dei componenti di avvio Windows; il *Microsoft Corporation KEK 2K CA 2023* è la nuova chiave di scambio. Il vecchio *Microsoft Corporation UEFI CA 2011* viene invece rimpiazzato non da uno ma da due certificati distinti, pensati per un controllo più granulare della fiducia: il *Microsoft UEFI CA 2023*, che firma i boot loader di terze parti e le applicazioni EFI (incluso lo *shim* usato da molte distribuzioni Linux), e il *Microsoft Option ROM UEFI CA 2023*, dedicato alle *option ROM* dei componenti hardware di terze parti. Perché il passaggio sia completo, i nuovi certificati devono essere in...
---
title: BadSuccessor: vulnerabilità negli ambienti Active Directory Enterprise
url: https://www.ictsecuritymagazine.com/articoli/badsuccessor-vulnerabilita/
source: ICT Security Magazine
date: 2025-06-01
fetch_date: 2025-10-06T22:53:35.457285
---

# BadSuccessor: vulnerabilità negli ambienti Active Directory Enterprise

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
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2025](https://www.ictsecuritymagazine.com/wp-content/uploads/banner-header-2025.jpg)](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025)

![BadSuccessor, ulnerabilità critica in Active Directory - cybercrime](https://www.ictsecuritymagazine.com/wp-content/uploads/badsuccessor.jpeg)

# BadSuccessor: vulnerabilità negli ambienti Active Directory Enterprise

A cura di:[Redazione](#molongui-disabled-link)  Ore 31 Maggio 202530 Maggio 2025

Nel panorama della cybersecurity moderna, poche scoperte hanno avuto l’impatto della vulnerabilità BadSuccessor identificata dai ricercatori di Akamai nel maggio 2025. Questa falla di sicurezza rappresenta un perfetto esempio di come le innovazioni progettate per migliorare la sicurezza possano paradossalmente aprire nuovi vettori di attacco.

La storia inizia con le migliori intenzioni, Microsoft aveva introdotto in Windows Server 2025 una nuova funzionalità chiamata Delegated Managed Service Accounts (dMSA), pensata per risolvere uno dei problemi più persistenti nella gestione delle identità enterprise – gli attacchi di Kerberoasting. Tuttavia, come spesso accade nel mondo della sicurezza informatica, la soluzione ha creato un problema ancora più grave.

Yuval Gordon, ricercatore di sicurezza presso Akamai, ha scoperto che questa nuova funzionalità può essere sfruttata per compromettere qualsiasi utente in Active Directory, inclusi i Domain Administrator, utilizzando privilegi apparentemente innocui che molti utenti già possiedono.

## La vulnerabilità BadSuccessor: anatomia di un attacco sofisticato

#### Cosa sono i Delegated Managed Service Accounts

Per comprendere la gravità di BadSuccessor, dobbiamo prima spiegare cosa sono i dMSA e perché Microsoft li ha introdotti. I Delegated Managed Service Accounts rappresentano l’evoluzione degli account di servizio tradizionali utilizzati dalle applicazioni per autenticarsi nei domini Active Directory.

Storicamente, gli account di servizio hanno rappresentato un punto debole nella sicurezza enterprise. Questi account utilizzano password statiche che raramente vengono cambiate, rendendoli vulnerabili agli attacchi di Kerberoasting – una tecnica che permette agli attaccanti di estrarre e craccare offline le password degli account di servizio.

I dMSA dovevano risolvere questo problema attraverso:

1. **Rotazione automatica delle password**: Le credenziali vengono cambiate automaticamente senza intervento umano;
2. **Binding alle identità macchina**: L’autenticazione è legata a specifiche macchine, limitando l’uso improprio delle credenziali:
3. **Migrazione trasparente**: Gli account di servizio esistenti possono essere migrati verso dMSA senza interruzioni operative.

#### Come funziona l’attacco BadSuccessor

La vulnerabilità sfrutta il meccanismo di migrazione dei dMSA in modo estremamente sofisticato. Ecco come procede un attaccante:

**Fase 1: Creazione del dMSA Malicioso** L’attaccante crea un nuovo dMSA utilizzando permessi CreateChild su qualsiasi Organizational Unit (OU) del dominio. Questi permessi sono comunemente assegnati per operazioni di amministrazione di routine e spesso non destano sospetti.

**Fase 2: Manipolazione degli Attributi Critici**
 L’attacco si basa sulla modifica di due attributi specifici:

* msDS-ManagedAccountPrecededByLink: Viene impostato per puntare all’account target che si vuole compromettere (ad esempio, un Domain Admin);
* msDS-DelegatedMSAState: Viene configurato per simulare una migrazione in corso

**Fase 3: Impersonificazione Automatica** Il Key Distribution Center (KDC) di Active Directory, vedendo questi attributi, assume che il dMSA stia legittimamente sostituendo l’account target e gli concede automaticamente tutti i privilegi e le appartenenze ai gruppi dell’account originale.

#### L’aspetto più pericoloso: nessun permesso richiesto sull’account target

Quello che rende BadSuccessor particolarmente insidioso è che l’attaccante non ha bisogno di alcun permesso diretto sull’account che vuole compromettere. Come spiega Gordon: “*È sufficiente avere permessi di scrittura sugli attributi di un dMSA per compromettere qualsiasi utente del dominio.*”

Questo significa che un utente con privilegi apparentemente limitati può scalare i propri privilegi fino a diventare Domain Administrator senza lasciare tracce evidenti nelle configurazioni degli account target.

## L’impatto reale: numeri che fanno riflettere

#### Una vulnerabilità sistemica, non un caso isolato

Le ricerche condotte da Akamai hanno rivelato la portata allarmante del problema. In 91% degli ambienti Active Directory esaminati, sono stati trovati utenti al di fuori del gruppo domain admins con i permessi necessari per eseguire questo attacco. Questo dato trasforma BadSuccessor da una curiosità teorica in una minaccia concreta per la stragrande maggioranza delle organizzazioni enterprise.

#### Esposizione universale

Un aspetto particolarmente preoccupante è che la vulnerabilità diventa disponibile in qualsiasi dominio che abbia almeno un domain controller Windows Server 2025, anche se l’organizzazione non utilizza attivamente i dMSA. Questo significa che le organizzazioni potrebbero essere vulnerabili semplicemente per aver aggiornato i loro domain controller, senza aver mai configurato o utilizzato la nuova funzionalità.

## La controversia: Microsoft vs. Akamai sulla severità

#### Due visioni diverse del rischio

La scoperta di BadSucces...
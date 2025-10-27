---
title: La campagna zero-day ToolShell colpisce Microsoft SharePoint: ecco cosa sta succedendo
url: https://www.ictsecuritymagazine.com/notizie/microsoft-sharepoint/
source: ICT Security Magazine
date: 2025-07-22
fetch_date: 2025-10-06T23:51:10.606169
---

# La campagna zero-day ToolShell colpisce Microsoft SharePoint: ecco cosa sta succedendo

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

![cyber attack Microsoft SharePoint - Microsoft SharePoint: Toolshell](https://www.ictsecuritymagazine.com/wp-content/uploads/cyberattack-Microsoft.jpeg)

# La campagna zero-day ToolShell colpisce Microsoft SharePoint: ecco cosa sta succedendo

A cura di:[Redazione](#molongui-disabled-link)  Ore 21 Luglio 202522 Luglio 2025

Microsoft SharePoint si è trasformato in uno dei bersagli più ambiti dai cybercriminali moderni, rappresentando una superficie di attacco critica che combina la complessità architetturale con l’ubiquità aziendale. Nel luglio 2025, la campagna ToolShell ha dimostrato come le vulnerabilità zero-day possano compromettere rapidamente oltre 85 server in tutto il mondo, colpendo indiscriminatamente agenzie governative statunitensi, prestigiose università e multinazionali di primo piano.

La sofisticazione di questi attacchi ha raggiunto livelli senza precedenti. Non si tratta più di exploit opportunistici lanciati da script kiddies, ma di campagne orchestrate meticolosamente da gruppi APT (Advanced Persistent Threat) e [operatori ransomware](https://www.ictsecuritymagazine.com/articoli/minaccia-ransomware/) che comprendono profondamente l’architettura Microsoft. Questa evoluzione riflette una realtà inquietante: SharePoint non è semplicemente una piattaforma di collaborazione, ma un gateway privilegiato verso l’intero ecosistema aziendale Microsoft.

L’integrazione profonda di SharePoint con Active Directory, Exchange, SQL Server e i servizi cloud di Microsoft 365 crea una rete interconnessa di dipendenze che, se sfruttata abilmente, può portare alla compromissione sistemica dell’intera infrastruttura IT. Per i professionisti della cybersecurity, questo scenario richiede una comprensione tecnica approfondita che va ben oltre le best practice tradizionali.

## La vulnerabilità CVE-2025-53770: un caso di studio tecnico

La vulnerabilità CVE-2025-53770 rappresenta un esempio paradigmatico di come le moderne minacce sfruttino le debolezze architetturali profonde di SharePoint. Con un punteggio CVSS di 9.8, questa falla di remote code execution non è semplicemente un bug, ma una finestra diretta nel cuore del sistema di deserializzazione .NET di SharePoint.

Il meccanismo di attacco rivela una comprensione sofisticata della tecnologia Microsoft da parte degli attaccanti. L’exploit inizia con l’invio di richieste POST apparentemente innocue all’endpoint
`/_layouts/15/ToolPane.aspx`
, utilizzando header HTTP Referer falsificati per aggirare i controlli di base. Ma è qui che inizia la vera maestria tecnica: gli attaccanti non si limitano a sfruttare la vulnerabilità, ma procedono all’estrazione delle chiavi crittografiche ValidationKey e DecryptionKey del server SharePoint.

Questa estrazione non è casuale, ma rappresenta una strategia di persistenza a lungo termine. Una volta ottenute queste chiavi, gli attaccanti possono generare payload
`__VIEWSTATE`
validi che garantiscono accesso persistente anche dopo l’applicazione delle patch di sicurezza. È una tecnica che dimostra come i moderni threat actor pensino strategicamente, non tatticamente, pianificando la persistenza sin dalle fasi iniziali dell’attacco.

La CVE-2025-53771 completa questo quadro fornendo un bypass dell’autenticazione che aggira le correzioni per la precedente CVE-2025-49706. Quando queste vulnerabilità vengono concatenate, il risultato è una compromissione completa che permette movimento laterale attraverso l’intero ecosistema Microsoft con privilegi amministrativi.

## Analisi tecnica dei meccanismi di deserializzazione

Per comprendere veramente la pericolosità di questi attacchi, è necessario esaminare i meccanismi tecnici sottostanti. La deserializzazione .NET rappresenta un vector di attacco particolarmente insidioso perché sfrutta una funzionalità legittima del framework per eseguire codice arbitrario. Gli attaccanti utilizzano il framework ysoserial per generare payload che sfruttano il BinaryFormatter attraverso catene di oggetti ObjectDataProvider e XamlReader.

Questi payload non sono semplici exploit “point-and-click”, ma costruzioni sofisticate che dimostrano una comprensione profonda dell’architettura .NET. I pattern TypeConfuseDelegate e WindowsIdentity utilizzati negli attacchi più recenti sono specificamente progettati per aggirare le blacklist implementate nelle patch precedenti, suggerendo che gli attaccanti stiano studiando attivamente le contromisure Microsoft.

La complessità aumenta quando consideriamo le tecniche di evasion utilizzate per nascondere questi payload. Il request smuggling HTTP/2 permette di incorporare contenuti dannosi nei header Transfer-Encoding e Content-Length, rendendo inefficaci molti Web Application Firewall tradizionali. Questa tecnica rivela come gli attaccanti abbiano sviluppato una comprensione profonda non solo di SharePoint, ma dell’intero stack tecnologico che lo supporta.

## Microsoft SharePoint, le debolezze architetturali sistemiche

SharePoint presenta diverse debolezze architetturali che vanno oltre le singole vulnerabilità. Il Central Administration, ad esempio, rappresenta un single point of failure critico che controlla l’intera farm SharePoint. Una sua compromissione equivale alla perdita del controllo amministrativo completo su tutti i siti, database...
---
title: Vulnerabilità Veeam Backup: una RCE critica espone l’ultima linea anti-ransomware
url: https://www.ictsecuritymagazine.com/notizie/vulnerabilita-veeam-backup-cve-2026-44963-rce/
source: ICT Security Magazine
date: 2026-06-10
fetch_date: 2026-06-11T06:36:45.582704
---

# Vulnerabilità Veeam Backup: una RCE critica espone l’ultima linea anti-ransomware

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
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)
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

![Vulnerabilità Veeam Backup una RCE critica espone l'ultima linea anti-ransomware](https://www.ictsecuritymagazine.com/wp-content/uploads/Vulnerabilita-Veeam-Backup-una-RCE-critica-espone-lultima-linea-anti-ransomware.png)

# Vulnerabilità Veeam Backup: una RCE critica espone l’ultima linea anti-ransomware

A cura di:[Redazione](#molongui-disabled-link)  Ore 10 Giugno 202610 Giugno 2026

Gli attaccanti, prima di cifrare, smontano il backup. È la regola non scritta del ransomware moderno, ed è la ragione per cui la vulnerabilità Veeam corretta il 9 giugno conta più della media: CVE-2026-44963 è una *remote code execution* sui server di Backup & Replication, cioè proprio l’infrastruttura su cui un’organizzazione conta per dire no al riscatto. Con un punteggio di 9,4 sulla scala CVSS 3.1 [secondo Veeam](https://www.veeam.com/kb4869) e una soglia di accesso bassa, la falla mette in discussione la promessa stessa del backup, essere il piano B quando tutto il resto è compromesso.

## Il bersaglio è la difesa, non il dato

La logica del *double extortion* nasce per aggirare chi ha copie di sicurezza pulite. Da qui la mossa successiva degli attaccanti: neutralizzare i backup prima di muoversi sul resto della rete. Una RCE sul *backup server* salta tutti i passaggi intermedi e consegna all’attaccante il nodo che amministra le copie, le pianificazioni e i ripristini. Non è la compromissione di un dato, è la compromissione dell’arbitro. Non è teoria: BleepingComputer ricorda che le gang ransomware prendono di mira i server di backup Veeam per esfiltrare dati, muoversi lateralmente e cancellare le copie delle vittime, e che CISA ha già segnalato come attivamente sfruttate quattro precedenti falle di Backup & Replication, abusate da gruppi come Akira, Fog, Frag, FIN7 e Cuba.

## Anatomia della vulnerabilità Veeam

CVE-2026-44963 consente a un utente di dominio autenticato, anche con privilegi minimi, di eseguire codice da remoto sul server di Backup & Replication. La condizione è precisa: la falla colpisce soltanto le installazioni unite a un dominio Active Directory, scenario tutt’altro che raro nelle reti aziendali. Sono interessate la build 12.3.2.4465 e tutte le versioni 12 precedenti; la correzione è nella 12.3.2.4854, distribuita il 9 giugno 2026 e descritta nella *knowledge base* KB4696. Le installazioni della linea 13.x non sono vulnerabili, per via del cambio di architettura introdotto in quella major release.

La scoperta è del ricercatore Sina Kheirkhah di watchTowr. Al momento non risultano sfruttamenti in corso, ma è la stessa Veeam ad abbassare le aspettative: una volta pubblicata la patch, gli attaccanti ne ricostruiscono il contenuto per colpire i sistemi non aggiornati, e la combinazione tra criticità elevata e requisito d’accesso modesto, un qualsiasi account di dominio, rende i tentativi probabili a breve. Non è un episodio isolato: la 44963 è l’ultima di una serie ricorrente della stessa classe, RCE attivabili da un utente di dominio su installazioni *domain joined*, presente in vulnerabilità Veeam dei mesi precedenti scorate fino a 9,9.

## Perché un 9,4 sul backup pesa più di un 9,4 altrove

Il numero è lo stesso, il contesto no. Veeam è tra le piattaforme di *data protection* più diffuse nell’*enterprise*, il che rende la superficie d’attacco trasversale a settori e dimensioni. E un *backup server* compromesso non vale come un endpoint qualsiasi: detiene le credenziali per accedere a storage e repository, conosce la topologia dei ripristini e, se manipolato, può trasformare la rete di salvataggio in un vettore. Le buone pratiche più volte richiamate, *storage* immutabile con *object lock*, copie *air gapped*, regola del 3-2-1, restano valide, ma presuppongono che il server che le orchestra non sia esso stesso sotto controllo ostile. È qui che una falla come questa morde la [resilienza informatica](https://www.ictsecuritymagazine.com/articoli/resilienza-informatica/): non aggira le difese, le pilota.

## Cosa fare adesso

L’azione immediata è l’aggiornamento alla 12.3.2.4854, prioritario sui server uniti a dominio ed esposti internamente. Dove la patch non è applicabile subito, valgono le contromisure di contenimento: isolare il *backup server* dalla rete generale, restringere gli account di dominio che possono raggiungerlo, monitorare gli accessi anomali e verificare l’integrità delle copie, perché un backup non testato è una promessa non mantenuta. Sono gli stessi principi che governano le [contromisure al ransomware](https://www.ictsecuritymagazine.com/articoli/ransomware-le-contromisure/), applicati al punto in cui farebbero più male se trascurati. La vulnerabilità Veeam non è, per ora, una crisi in corso, ma un promemoria scomodo: l’ultima linea di difesa va difesa per prima.

Condividi sui Social Network:

Tag articolo:  [#Active Directory](https://www.ictsecuritymagazine.com/tag/active-directory/ "Active Directory")[#Backup](https://www.ictsecuritymagazine.com/tag/backup/ "Backup")[#Business Continuity](https://www.ictsecuritymagazine.com/tag/business-continuity/ "Business Continuity")[#CVE-2026-44963](https://www.ictsecuritymagazine.com/tag/cve-2026-44963/ "CVE-2026-44963")[#Dat...
---
title: Ransomware ESXiArgs: ecco il tool per ripristinare i server VMware ESXi compromessi
url: https://www.cybersecurity360.it/news/ransomware-esxiargs-ecco-il-tool-per-ripristinare-i-server-vmware-esxi-compromessi/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-10
fetch_date: 2025-10-04T06:15:39.821954
---

# Ransomware ESXiArgs: ecco il tool per ripristinare i server VMware ESXi compromessi

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Ransomware ESXiArgs: ecco il tool per ripristinare i server VMware ESXi compromessi

* [Cybersecurity Nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* Malware e attacchi
  + [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
  + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)
* Norme e adeguamenti
  + [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)
* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
* [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
* [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
* [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
* [Chi siamo](https://www.cybersecurity360.it/about/)

* [![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_neg_logo-768x55.png)](https://www.cybersecurity360.it)
* Seguici
* + [twitter](https://twitter.com/Cybersec360)
  + [linkedin](https://www.linkedin.com/company/cybersecurity360/)
  + [Newsletter](https://www.cybersecurity360.it/newsletter-signin/)
  + [Rss Feed](#rssModal)
  + [Chi siamo](https://www.cybersecurity360.it/about)
* AREA PREMIUM
* [Whitepaper](https://www.cybersecurity360.it/whitepaper/)
* [Eventi](https://www.cybersecurity360.it/eventi/)
* [Webinar](https://www.cybersecurity360.it/webinar/)
* CANALI
* [Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
* + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)* [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  * + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
    * [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
    * [L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
    * [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
    * [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
    * [Chi siamo](https://www.cybersecurity360.it/about/)

[Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
[Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
[Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
[Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
[Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
[L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
[Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
[Chi siamo](https://www.cybersecurity360.it/about/)

L'analisi tecnica

# Ransomware ESXiArgs: ecco il tool per ripristinare i server VMware ESXi compromessi

* [Home](https://www.cybersecurity360.it)
* [News, attualità e analisi sulla Cyber sicurezza](https://www.cybersecurity360.it/news/)

L’agenzia statunitense per la sicurezza informatica, CISA (Cybersecurity and Infrastructure Security Agency), ha reso disponibile lo script per ripristinare i server VMware ESXi compromessi dal ransomware ESXiArgs. Ecco come funziona

Pubblicato il 08 Feb 2023

[Dario Fadda](https://www.cybersecurity360.it/giornalista/dario-fadda/)

Research Infosec, fondatore Insicurezzadigitale.com

![Vulnerabilità VMware vCenter Server](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2021/02/Vulnerabilit%C3%A0-VMware.jpg)![Vulnerabilità VMware vCenter Server](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2021/02/Vulnerabilit%C3%A0-VMware.jpg)

L’agenzia statunitense per la cybersicurezza (CISA) ha rilasciato un **decryptor** che permette di **ripristinare i server VMware ESXi** che negli ultimi giorni sono stati presi di mira da una campagna malevola a livello globale condotta mediante il [**ransomware ESXiArgs**](https://www.cybersecurity360.it/nuove-minacce/ransomware/esxiargs-il-ransomware-dellattacco-ai-server-vmware-esxi-cosa-sappiamo-e-come-difendersi/).

Scopriamo come funziona, analizzando il sistema di cifratura operato dal malware.

Indice degli argomenti

* [Il decryptor per il ransomware ESXiArgs](#Il_decryptor_per_il_ransomware_ESXiArgs)
* [Uno sguardo allo script malevolo del ransomware](#Uno_sguardo_allo_script_malevolo_del_ransomware)

## Il decryptor per il ransomware ESXiArgs

Come avevamo riportato nell’[analisi dell’incidente](https://www.cybersecurity360.it/nuove-minacce/attacco-hacker-globale-cosa-sappiamo-degli-impatti-in-italia/) domenica, sembra che molti degli attacchi analizzati siano stati portati a termine utilizzando uno script di cifratura che mira, con rapidità, a rendere la virtual machine non operativa, piuttosto che comprometterne tutto il contenuto.

Proprio questo meccanismo ha reso possibile ai tecnici CISA la realizzazione dello [script](https://github.com/cisagov/ESXiArgs-Recover) che consente di ripristinare i sistemi compromessi in maniera automatizzata. Lo script di recupero funziona, appunto, solo **quando il file flat non è compromesso**.

È bene ricordare che questo script è stato realizzato unicamente grazie al tempestivo lavoro di ricerca operato da Enes Sonmez e Ahmet Aykac, che ne avevano anticipato la fattibilità, mediante un algoritmo da eseguire manualmente, già dal 4 febbraio 2023.

Il decryptor, dunque, non fa altro che creare, sulla base del file -flat.vmdk, i nuovi file .vmdk e .vmx che andranno a sostituire quelli ormai corrotti dal ransomware e non più utilizzabili. Questo viene fatto mediante l’utilizzo dello strumento “vmkfstools”.

Recenti rilevamenti, descritti da Bleeping Computer l’8 febbraio, fanno emergere l’esistenza di una nuova variante di questo ransomware, che sembra crittografare maggiori parti di dati del sistema coinvolto.

Non è al momento chiaro se il file -flat viene compromesso in questo nuovo algoritmo crittografico, tuttavia sembra che, le vittime non siano state in grado di ripristinare la situazione mediante l’utilizzo dello script offerto da CISA.

In attesa di ulteriori sviluppi si segnala che, qualora il sistema compromesso risulti non operativo e il file -flat.vmdk non compromesso, c’è comunque modo di ripristinare la situazione valutando di installare il sistema su una macchina terza, ex novo e basando l’installazione sul file -flat intatto. Questo consentirà di recuperarne il contenuto sotto forma di file su disco, come descritto da Enes Sonmez.

## Uno sguardo allo script malevolo del ransomware

Fin dai primi attacchi analizzati, era già noto dunque lo script incriminato, responsabile della compromissione dei vari server ESXi in giro per il mondo senza patch di sicurezza. Adesso possiamo analizzarlo nel dettaglio proprio grazie al fatto che lo si può considerare neutralizzato dal procedimento appena descritto, di ripristino.

![](data:image/png;base64...)![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2023/02/Screenshot_2023-02-08_10_59_41.png)

Il punto fondamentale del funzionamento di questo ransomware è proprio l’insieme di istruzioni che vengono rappresentate in figura. Da qui, notiamo che ...
---
title: Ripristinare i sistemi VMware ESXi compromessi dal ransomware ESXiArgs: ecco come
url: https://www.cybersecurity360.it/nuove-minacce/ransomware/ripristinare-i-sistemi-vmware-esxi-compromessi-dal-ransomware-esxiargs-ecco-come/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-10
fetch_date: 2025-10-04T06:15:12.154561
---

# Ripristinare i sistemi VMware ESXi compromessi dal ransomware ESXiArgs: ecco come

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Ripristinare i sistemi VMware ESXi compromessi dal ransomware ESXiArgs: ecco come

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

LA GUIDA PRATICA

# Ripristinare i sistemi VMware ESXi compromessi dal ransomware ESXiArgs: ecco come

* [Home](https://www.cybersecurity360.it)
* [Attacchi hacker e Malware: le ultime news in tempo reale](https://www.cybersecurity360.it/nuove-minacce/)
* [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)

Sono circa 3.000 i server VMware ESXi esposti su Internet e non aggiornati che, nei giorni scorsi, sono stati compromessi con un attacco informatico condotto a livello globale con il ransomware ESXiArgs. Ecco la procedura da seguire per ripristinarli (con tutte le accortezze del caso)

Pubblicato il 09 Feb 2023

[Antonio Pontrelli](https://www.cybersecurity360.it/giornalista/antonio-pontrelli/)

Responsabile del SOC Exprivia

![Ripristinare i sistemi VMware ESXi compromessi dal ransomware ESXiArgs: ecco come](data:image/png;base64...)![Ripristinare i sistemi VMware ESXi compromessi dal ransomware ESXiArgs: ecco come](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2023/02/Ransomware-ESXiArgs.jpg)

Come abbiamo [riportato nei giorni scorsi](https://www.cybersecurity360.it/nuove-minacce/attacco-hacker-globale-cosa-sappiamo-degli-impatti-in-italia/), un attacco informatico condotto su scala mondiale **ha compromesso circa 3.000 server VMware ESXi** esposti su Internet utilizzando il nuovo [ransomware ESXiArgs](https://www.cybersecurity360.it/nuove-minacce/ransomware/esxiargs-il-ransomware-dellattacco-ai-server-vmware-esxi-cosa-sappiamo-e-come-difendersi/).

I sistemi vittime dall’attacco ESXiArgs, si sono ritrovati con i file ***.vmdk*** e .***vmx*** crittografati. Di seguito saranno elencate una serie di procedure per tentare di ripristinare il server compromesso.

Si tratta di una procedura che ho verificato personalmente ma non posso in alcun modo garantire che funzioni sempre e che non abbia effetti collaterali.

## **Procedura passo passo per ripristinare i sistemi ESXi**

Il ransomware ESXiArgs crittografa i file di configurazione (.**vmdk** e **.vmx**) ma non il file **VM \_NAME-flat.vmdk**. Nella struttura e configurazione di ESXi, i dati sono conservati nel file **VM \_NAME-flat.vmdk**.

L’obiettivo di questo articolo è mostrare la procedura per ripristinare i file di configurazione crittografati, usando il file **VM \_NAME-flat.vmdk**.

Innanzitutto, verificare se è attivo il servizio SSH del server ESXi e abilitarlo in caso fosse disabilitato. Successivamente accedere tramite SSH e posizionarsi nella cartella virtual machine compromessa che s’intende ripristinare. Le virtual machine sono salvate nel seguente percorso **vmfs/volumes/datastoreXXX/**, pertanto il comando da eseguire è il seguente:

***cd vmfs/volumes/datastoreXXX/VM\_TEST***

Inserendo il nome datastoreXXX, il suo nome cambierà in un codice, nel seguente caso 600ebxxx.

![](data:image/png;base64...)![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2023/02/word-image-62572-1.jpg)

Dopo essere entrati nella cartella della virtual machine compromessa, nel seguente caso **VM\_TEST** eseguire il comando “***ls -la***”, per vedere l’elenco e la dimensione dei file. La dimensione di **VM\_Test-flat.vmdk** è di 53687091200.

A questo punto procedere con l’eliminazione del file .vmdk esistente e compromesso, digitando il comando **rm -rf xxx.vmdk** (come backup, anziché cancellare il file, si può spostare in un’altra directory oppure creare una nuova directory all’interno del percorso dove ci si trova e incollarci il file che si sta cancellando).

***NOTA: eliminare solo il file xxx.vmdk e non eliminare mai il file xxx-flat.vmdk**.*

![](data:image/png;base64...)![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2023/02/word-image-62572-2.png)

Digitare il comando **vmkfstools -c <dimensione\_file\_-flat.vmdk> -d thin temp.vmdk**, per procedere con la copia del file **-flat.vmdk**. Per recuperare la dimensione del file -flat-vmdk, eseguire il comando **ls -la**.

La dimensione del file **VM\_TEST-flat.vmdk**, in questo caso, è di 53687091200, come si può vedere da immagine seguente.

![](data:image/png;base64...)![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2023/02/word-image-62572-3.png)

Se non sono stati generati errori, nella cartella della macchina virtuale compromessa, ci saranno 2 nuovi file, denominati **temp.vmdk** e **temp-flat.vmdk**, dove “temp-flat.vmdk”, avrà la stessa dimensione del file -flat.vmd...
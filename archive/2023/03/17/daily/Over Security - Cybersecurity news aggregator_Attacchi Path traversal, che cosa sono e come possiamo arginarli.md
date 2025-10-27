---
title: Attacchi Path traversal, che cosa sono e come possiamo arginarli
url: https://www.cybersecurity360.it/outlook/attacchi-path-traversal-che-cosa-sono-e-come-possiamo-arginarli/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-17
fetch_date: 2025-10-04T09:52:34.142728
---

# Attacchi Path traversal, che cosa sono e come possiamo arginarli

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Attacchi Path traversal, che cosa sono e come possiamo arginarli

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

Le tecniche

# Attacchi Path traversal, che cosa sono e come possiamo arginarli

* [Home](https://www.cybersecurity360.it)
* [The Outlook](https://www.cybersecurity360.it/outlook/)

Gli attacchi Path traversal sono vulnerabilità che consentono di leggere file sui server che eseguono applicazioni. In alcuni casi, permettono di modificare i dati e il comportamento delle applicazioni stesse fino a prendere il controllo del server

Pubblicato il 16 Mar 2023

[Giuditta Mosca](https://www.cybersecurity360.it/giornalista/giuditta-mosca/)

Giornalista, esperta di tecnologia

![Attribuzione degli attacchi informatici di cosa si tratta](data:image/png;base64...)![Attribuzione degli attacchi informatici di cosa si tratta](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2021/06/Attribuzione-degli-attacchi-informatici.jpg)

Gli attacchi **Path traversal** vengono chiamati anche Directory traversal e sono exploit http, ossia porzioni di codice, sequenze di comandi o pacchetti di dati che sfruttano le vulnerabilità di un sistema per alterarne il comportamento.

Nel caso specifico si tratta di un attacco che riguarda i web server e mira ad accedere ai dati **archiviati al di fuori della directory principale** (la directory di root), arrivando così non soltanto a dare agli hacker la possibilità di visualizzare i file e, in alcuni casi, persino di eseguire comandi. C’è però modo di arginare i rischi.

Indice degli argomenti

* [Gli attacchi Path traversal](#Gli_attacchi_Path_traversal)
* [Gli attacchi LFI e FRI](#Gli_attacchi_LFI_e_FRI)
* [Come prevenire gli attacchi Path traversal](#Come_prevenire_gli_attacchi_Path_traversal)
* [Come testare un web server](#Come_testare_un_web_server)

## **Gli attacchi Path traversal**

Poiché un attacco Path traversal viene normalmente sferrato via browser, occorre considerare che vi sono esposti tutti i web server che accettano **input non convalidati**. Mediante una scansione dell’albero delle directory, i cyber criminali ottengono una mappa precisa dei percorsi dei file riuscendo a sapere così quali sono sottoposti a restrizioni e quali no.

Questo tipo di scansioni vengono effettuate con delle applicazioni per il rilevamento delle vulnerabilità, tool di tipo Dynamic Application Security Testing ([Dast](https://www.softwaretestinghelp.com/dynamic-application-security-testing-dast-software/)) che **vanno eseguiti outbound** e che segnalano vulnerabilità di vario tipo, tra cui quelle [cross-site scripting](https://www.cybersecurity360.it/news/un-nuovo-metodo-di-attacco-bypassa-le-web-application-firewall-come-proteggersi/), [SQL Injection](https://www.cybersecurity360.it/outlook/si-soffre-ancora-di-sql-injection-la-vulnerabilita-sempre-verde/), Command injection, quelle conseguenti a configurazioni perfettibili e, non da ultimo, quelle Path traversal.

Ciò che accade in pratica è persino elementare e può essere riassunto in quattro passaggi:

1. Un **hacker identifica applicazioni web** che non validano l’input degli utenti
2. Invia una richiesta al server per **ottenere un file legittimo** e consultabile da qualsiasi utente, per esempio https://nomefile.com/?file=nomefile.php
3. L’hacker **modifica l’URL** usando “../” per cambiare percorso nell’albero delle directory del web server
4. Accede così a informazioni sensibili quali, per esempio, ai dati contenuti **nel database passwd** che è di proprietà di root, ma è leggibile da utenti con privilegi minori (https://nomefile.com/?file=../../../etc/passwd)

Laddove non c’è validazione dell’input degli utenti, un hacker può muoversi con una certa libertà nell’albero delle directory, anche solo per visualizzare ciò che può essere modificato da root oppure utenti con privilegi sudo (i privilegi di superutente per gli utenti non root). Può, per esempio, accedere al file /etc/hosts e ottenere informazioni necessarie a sferrare un attacco **Local File Inclusion** (LFI) o **Remote File Inclusion** (RFI) che meritano un approfondimento.

## **Gli attacchi LFI e FRI**

Gli attacchi di tipo Local File Inclusion (LFI) permettono agli attaccanti di interferire con un’applicazione Web affinché, per esempio, esegua operazioni non desiderate o esponga dati, anche sensibili. Argomento che può essere compreso meglio con un esempio.

> [Attacco a Kaseya: il ruolo del supply chain risk e dei processi DevSecOps](https://www.cybersecurity360.it/nuove-minacce/attacco-a-kaseya-il-ruolo-del-supply-chai...
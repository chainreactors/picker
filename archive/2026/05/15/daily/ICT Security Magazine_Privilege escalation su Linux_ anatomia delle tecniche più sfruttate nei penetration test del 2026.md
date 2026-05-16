---
title: Privilege escalation su Linux: anatomia delle tecniche più sfruttate nei penetration test del 2026
url: https://www.ictsecuritymagazine.com/articoli/privilege-escalation/
source: ICT Security Magazine
date: 2026-05-15
fetch_date: 2026-05-16T05:15:30.177485
---

# Privilege escalation su Linux: anatomia delle tecniche più sfruttate nei penetration test del 2026

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

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![privilege escalation su linux.](https://www.ictsecuritymagazine.com/wp-content/uploads/privilege-escalation-su-linux.png)

# Privilege escalation su Linux: anatomia delle tecniche più sfruttate nei penetration test del 2026

A cura di:[Canio Campaniello](#molongui-disabled-link)  Ore 15 Maggio 202615 Maggio 2026

La fase di privilege escalation rappresenta uno dei principali fattori di rischio nei test di sicurezza moderni, spesso più determinante dell’accesso iniziale. È silenziosa, spesso automatizzabile, e si fonda quasi sempre su configurazioni errate che esistono di default in sistemi che non hanno mai ricevuto un hardening esplicito. Secondo il Rapporto Clusit 2025, l’Italia ha registrato 357 incidenti gravi nel 2024, con un incremento del 15,2% rispetto all’anno precedente, e il credential access rappresenta circa il 30% degli eventi rilevati, una base di partenza che rende la post-exploitation, inclusa la privilege escalation, un vettore critico in qualsiasi strategia di difesa.

## Il problema che nessuno vuole vedere

C’è una fase del penetration test che molte organizzazioni continuano a sottovalutare. Non è l’accesso iniziale – ormai riconosciuto come critico anche dal management meno tecnico – ma ciò che accade dopo: la capacità di un attaccante di muoversi verticalmente all’interno di un sistema già compromesso, scalando da un account limitato fino ai privilegi di root.

La privilege escalation su Linux è esattamente questa fase. È silenziosa, spesso automatizzabile, e si fonda quasi sempre su configurazioni errate che esistono di default in sistemi che non hanno mai ricevuto un hardening esplicito.

Questo articolo analizza i vettori di escalation più ricorrenti nella pratica operativa del 2026, con riferimento alle tecniche documentate nei [framework MITRE ATT&CK](https://www.ictsecuritymagazine.com/articoli/threat-actor-intelligence/) e PTES (Penetration Testing Execution Standard), e con i comandi effettivi utilizzati nei test autorizzati.

## Contesto normativo: perché la privilege escalation è rilevante per la compliance

Prima di entrare nel merito tecnico, vale la pena inquadrare il tema in prospettiva normativa.

Il [Digital Operational Resilience Act](https://www.ictsecuritymagazine.com/notizie/convergenza-normativa/) (DORA, Reg. UE 2022/2554), pienamente applicabile dal gennaio 2025 per le entità finanziarie europee, introduce l’obbligo di Threat-Led Penetration Testing (TLPT) basato sul framework TIBER-EU. Questi test richiedono la simulazione realistica di attacchi avanzati – incluse le tecniche di escalation dei privilegi – su sistemi in produzione.

Analogamente, [la Direttiva NIS2](https://www.ictsecuritymagazine.com/articoli/nis-2-e-sicurezza-informatica/) (recepita in Italia con il D.Lgs. 138/2024) richiede che le entità essenziali e importanti adottino misure “adeguate e proporzionate” ai rischi specifici identificati, ai sensi dell’Art. 21. La privilege escalation, in questo contesto, non è più una questione puramente tecnica: è un requisito di compliance.

## La fase che precede tutto: l’enumerazione sistematica

Un errore frequente, anche tra penetration tester con esperienza, è saltare o comprimere la fase di enumerazione per arrivare più velocemente all’escalation. Il risultato è quasi sempre lo stesso: si perde tempo su vettori che non esistono, mentre quello reale è lì, evidente, in attesa di essere trovato metodicamente.

L’enumerazione di un sistema Linux post-compromissione segue un ordine preciso:

`# Identità e contesto dell'utente corrente`

`id && whoami && groups`

`# Sistema operativo, versione kernel, architettura`

`uname -a && cat /etc/os-release && cat /proc/version`

`# Processi in esecuzione come root`

`ps aux | grep -v "^\[" | awk '{if($1=="root") print $0}'`

`# Servizi di rete in ascolto`

`ss -tulnp`

`# Scheduled tasks`

`cat /etc/crontab`

`ls -la /etc/cron.d/ /etc/cron.hourly/ /etc/cron.daily/`

`crontab -l 2>/dev/null`

`# Binari con SUID impostato`

`find / -perm -4000 -user root -type f 2>/dev/null`

`# File scrivibili da utenti non privilegiati`

`find / -writable -type f 2>/dev/null | grep -v proc | grep -v sys`

Strumenti come unix-privesc-check automatizzano questa raccolta e producono un output strutturato che evidenzia le anomalie più significative. Tuttavia, l’automazione non sostituisce la comprensione: un enumeratore automatico può segnalare centinaia di potenziali problemi, ma solo la lettura critica distingue un falso positivo da un vettore reale.

## Vettore 1: abuso di binari SUID

Il bit SUID (Set User ID) è un meccanismo del filesystem Unix che permette a un eseguibile di girare con i privilegi del suo proprietario, indipendentemente dall’utente che lo lancia. Quando un binario è di proprietà di root e ha il SUID impostato, chiunque lo esegua acquisisce temporaneamente i privilegi di root per la durata dell’esecuzione.

`find / -perm -4000 -user root -type f 2>/dev/null`

Il database GTFOBins (gtfobins.github.io) documenta ogni binario Linux noto che può essere sfruttato per l’escalation quando ha SUID impostato. Alcuni esempi pratici:

`# find con SUID impostato`

`/usr/bin/find . -exec /bin/sh -p \; -quit`

`# python3 con SUID`

`python3 -c 'import os; os.execl("/bin/sh", "sh", "-p")'`...
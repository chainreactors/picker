---
title: Certificati TLS, la falla che mette in discussione la catena di fiducia di Internet
url: https://www.cybersecurity360.it/nuove-minacce/certificati-tls-la-falla-che-mette-in-discussione-la-catena-di-fiducia-di-internet/
source: Over Security
date: 2026-10-22
fetch_date: 2026-10-23T06:46:33.849676
---

# Certificati TLS, la falla che mette in discussione la catena di fiducia di Internet

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=cybersecurity360.it)
[I nostri servizi](https://www.cybersecurity360.it/about-network/)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Certificati TLS, la falla che mette in discussione la catena di fiducia di Internet

* [Ultimi articoli](https://www.cybersecurity360.it/ultimi-articoli/)
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
* + [X](https://twitter.com/Cybersec360)
  + [linkedin](https://www.linkedin.com/company/cybersecurity360/)
  + [Newsletter](https://www.cybersecurity360.it/newsletter-signin/)
  + Rss Feed
  + [Chi siamo](https://www.cybersecurity360.it/about/)
* AREA PREMIUM
* [Whitepaper](https://www.cybersecurity360.it/whitepaper/)
* [Eventi](https://www.cybersecurity360.it/eventi/)
* [Webinar](https://www.cybersecurity360.it/webinar/)
* CANALI
* [Ultimi articoli](https://www.cybersecurity360.it/ultimi-articoli/)
* [Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
* + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)* [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  * + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
    * [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
    * [L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
    * [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
    * [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
    * [Chi siamo](https://www.cybersecurity360.it/about/)

[Ultimi articoli](https://www.cybersecurity360.it/ultimi-articoli/)
[Cybersecurity Nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
[Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
[Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
[Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
[Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
[Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
[Chi siamo](https://www.cybersecurity360.it/about/)

l'analisi

# Certificati TLS, la falla che mette in discussione la catena di fiducia di Internet

---

[Commenta l'articolo](#comments)

Indirizzo copiato

---

Otto certificati intermedi della Certification Authority eMudhra usavano chiavi private ricostruibili in pochi tentativi, nonostante dispositivi crittografici e audit indipendenti. Un caso che mette in discussione l’efficacia dei controlli e rivela quanto la fiducia digitale dipenda dalla sicurezza dei processi, non solo dalla conformità

Pubblicato il 22 ott 2026

---

[Sandro Sana](https://www.cybersecurity360.it/giornalista/sandro-sana-2/)

Esperto e divulgatore in cyber security, membro del Comitato Scientifico Cyber 4.0

---

---

![AI Questions Icon](data:image/gif;base64...)![AI Questions Icon](https://chatbotdev.ai.nextwork360.it/icons/NW360.svg)

Chiedi all'AI

Riassumi questo articolo

Approfondisci con altre fonti

![certificati TLS](data:image/png;base64...)![certificati TLS](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2026/10/certificati-TLS.jpg)

---

[Aggiungi tra i preferiti su Google](https://google.com/preferences/source?q=cybersecurity360.it)

---

---

---

La **sicurezza di Internet** si fonda su un meccanismo che utilizziamo ogni giorno senza pensarci: la **fiducia**. Quando ci colleghiamo a un sito HTTPS, il nostro browser verifica un certificato digitale e riconosce un’identità attraverso una catena di autorità considerate affidabili.

Ma cosa succede quando una delle organizzazioni incaricate di garantire questa fiducia produce chiavi crittografiche che chiunque potrebbe ricostruire?

È quanto emerso il 20 ottobre 2026, quando [Ars Technica ha riportato la scoperta](https://arstechnica.com/security/2026/10/the-internet-goes-on-high-alert-after-discovery-of-8-compromised-tls-certs/) di otto certificati intermedi appartenenti alla Certification Authority indiana eMudhra, associati a chiavi private di una debolezza difficilmente immaginabile.

Parliamo di valori come 4, 56, 66, 115, 155, 156, 230 e 237. Numeri che, in condizioni normali, avrebbero dovuto essere scelti casualmente all’interno di uno spazio crittografico di circa 384 bit, composto da un numero di possibilità praticamente inesplorabile.

In questo caso, invece, bastavano poche centinaia di tentativi per ricostruire le chiavi.

> [PHP2Shell, due vulnerabilità critiche in PHP: come proteggere i server](https://www.cybersecurity360.it/nuove-minacce/php2shell-due-vulnerabilita-critiche-in-php-come-proteggere-i-server-in-attesa-delle-patch/)

Indice degli argomenti

* [Il problema non è TLS, ma chi garantisce la fiducia](#Il_problema_non_e_TLS_ma_chi_garantisce_la_fiducia)
* [HSM certificati e audit: perché nessuno se n’è accorto?](#HSM_certificati_e_audit_perche_nessuno_se_ne_accorto)
* [I segnali erano già comparsi nel 2025](#I_segnali_erano_gia_comparsi_nel_2025)
* [La risposta dei browser e il problema dei sistemi dimenticati](#La_risposta_dei_browser_e_il_problema_dei_sistemi_dimenticati)
* [La fiducia digitale deve essere verificabile, non soltanto certificata](#La_fiducia_digitale_deve_essere_verificabile_non_soltanto_certificata)

## Il problema non è TLS, ma chi garantisce la fiducia

La vulnerabilità non deriva dalla scoperta di un nuovo attacco contro gli algoritmi crittografici utilizzati nelle connessioni TLS. Il problema è molto più concreto: durante la generazione delle chiavi private qualcosa è andato storto, producendo valori estremamente prevedibili.

La gravità dell’incidente dipende anche dalla tipologia dei certificati coinvolti. Non erano semplici certificati associati a singoli siti web, ma certificati di autorità intermedie, che possono essere utilizzati per emettere ulteriori certificati digitali.

Se un attaccante dispone della chiave privata di un’autorità intermedia ancora considerata affidabile, può potenzialmente produrre certificati falsi per domini che non controlla, impersonando servizi legittimi e intercettando comunicazioni quando riesce a posizionarsi nel percorso del traffico.

Sei delle otto autorità coinvolte erano abilitate all’emissione di certificati TLS, mentre le altre due erano destinate alla firma del codice.

La scoperta è arr...
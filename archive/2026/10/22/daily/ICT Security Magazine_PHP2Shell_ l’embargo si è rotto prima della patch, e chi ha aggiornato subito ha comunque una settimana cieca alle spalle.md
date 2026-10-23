---
title: PHP2Shell: l’embargo si è rotto prima della patch, e chi ha aggiornato subito ha comunque una settimana cieca alle spalle
url: https://www.ictsecuritymagazine.com/cyber-security/php2shell-embargo-rotto-finestra-prima-della-patch/
source: ICT Security Magazine
date: 2026-10-22
fetch_date: 2026-10-23T06:46:29.681310
---

# PHP2Shell: l’embargo si è rotto prima della patch, e chi ha aggiornato subito ha comunque una settimana cieca alle spalle

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

![PHP2Shell l'embargo si è rotto prima della patchFalla del server e patch tardiva](https://www.ictsecuritymagazine.com/wp-content/uploads/PHP2Shell-lembargo-si-e-rotto-prima-della-patchFalla-del-server-e-patch-tardiva.webp)

# PHP2Shell: l’embargo si è rotto prima della patch, e chi ha aggiornato subito ha comunque una settimana cieca alle spalle

A cura di:[Redazione](#molongui-disabled-link)  Ore 22 Ottobre 202622 Ottobre 2026

Il 21 ottobre 2026, alle 14:00 UTC, il progetto PHP ha pubblicato quattro versioni correttive per due vulnerabilità critiche nell’interprete. Sono la CVE-2026-109618 e la CVE-2026-109619, entrambe use after free, entrambe con punteggio CVSS v4.0 pari a 9,2, entrambe sfruttabili da remoto senza autenticazione. Il nome con cui circolano è PHP2Shell.

La parte tecnica è grave e si riassume in fretta. La parte che merita un articolo è un’altra: quando le patch sono uscite, qualcuno stava già provando a sfruttarle da giorni. Gli honeypot di Amazon registrano un tentativo il 17 ottobre. Cloudflare ha attivato le protezioni alle 03:02 UTC del 21, nove ore prima della divulgazione, e dichiara di avere osservato traffico di attacco contro i propri clienti. La divulgazione coordinata, in questo caso, non ha coordinato nulla.

La conseguenza operativa è contro intuitiva. Un’organizzazione che ha aggiornato il 21 ottobre entro poche ore ha fatto la cosa giusta e non ha chiuso il problema. Ha chiuso la finestra futura e si è lasciata alle spalle una finestra passata che nessun avviso italiano la aiuta a verificare.

## Che cosa rompono le due vulnerabilità

Entrambe nascono dallo stesso punto debole, ed è il modo in cui PHP gestisce gli errori fatali mentre sta elaborando una richiesta, in particolare l’esaurimento della memoria.

L’[advisory GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w), pubblicato il 21 ottobre, descrive la CVE-2026-109618. PHP usa la funzione longjmp() per uscire dal contesto corrente quando la memoria finisce. Se un’allocazione fallisce mentre la memoria della richiesta è già raggiungibile ma non ancora completamente inizializzata, l’uscita anticipata non viene contabilizzata. Lo spegnimento della richiesta legge allora strutture non valide. Il testo dell’advisory è asciutto: “If any allocation fails at that point, PHP does not properly account for the early exit”.

Le strategie per provocare l’esaurimento passano dal parsing multipart. Una richiesta multipart senza content-length utilizzabile che supera il controllo su post\_max\_size, un numero illimitato di intestazioni per parte, controlli di file vuoti che non contano in max\_file\_uploads ma generano comunque array di metadati. Il vettore CVSS è CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N.

L’[advisory GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp), pari data, descrive la CVE-2026-109619. Qui lo stato globale del worker, errori, sessione, oggetti ed estensioni, resta puntato alla memoria della richiesta precedente dopo che quella memoria è stata liberata. Una richiesta successiva, servita dallo stesso worker, usa quei riferimenti prima che l’inizializzazione li azzeri. L’advisory lo scompone in produttore e consumatore: il produttore è l’operazione che lascia pubblicato lo stato, il consumatore è quella che lo rilegge dopo.

Il caso dimostrato più forte è PHP 8.5 con fatal\_error\_backtraces attivo, ed è la base dello sfruttamento confermato su mod\_php. Il secondo caso confermato è il ciclo di vita del session upload progress, validato sia su mod\_php sia su PHP-FPM, con un innesco indipendente dall’applicazione.

Questa è la differenza che conta nel raccogliere le prove. Per la 109618 l’esecuzione di codice completa è stata validata via HTTP contro mod\_php, con limiti di memoria di default. PHP-FPM è indicato come suscettibile sulla base dell’analisi del sorgente, senza un exploit completo dimostrato. Per la 109619 il percorso del session upload progress è validato su entrambe le configurazioni.

Gli advisory estendono il quadro oltre le due configurazioni più note. Per la 109618 FrankenPHP, come mod\_php, richiama la procedura di spegnimento in modo incondizionato, quindi è indicato come probabilmente suscettibile ad attacchi indipendenti dall’applicazione. LSAPI segue il modello FPM, con exploit specifici dell’applicazione ritenuti probabili ma non validati.

Per la 109619 c’è un’esposizione di PHP-FPM che riguarda molte installazioni reali. È condizionata al frontend: nginx, Apache mod\_proxy\_fcgi o altro, quando inviano parametri PHP\_VALUE o PHP\_ADMIN\_VALUE che generano una diagnostica prima dell’inizializzazione della richiesta.

Un dettaglio del percorso session upload progress merita attenzione perché smonta un’ipotesi comune. La funzione è attiva per impostazione predefinita e non richiede alcuna chiamata a session\_start() da parte dell’applicazione. Non serve che il sito usi le sessioni.

La correzione, secondo l’advisory, rimuove longjmp() per le condizioni di esaurimento memoria. Al suo posto introduce un’uscita ritardata e ordinata al successivo punto sicuro della macchina virtuale, ...
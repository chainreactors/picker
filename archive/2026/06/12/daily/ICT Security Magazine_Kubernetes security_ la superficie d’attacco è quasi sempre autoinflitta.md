---
title: Kubernetes security: la superficie d’attacco è quasi sempre autoinflitta
url: https://www.ictsecuritymagazine.com/cyber-security/kubernetes-security/
source: ICT Security Magazine
date: 2026-06-12
fetch_date: 2026-06-13T06:11:59.639519
---

# Kubernetes security: la superficie d’attacco è quasi sempre autoinflitta

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

![Kubernetes security](https://www.ictsecuritymagazine.com/wp-content/uploads/Kubernetes-security.png)

# Kubernetes security: la superficie d’attacco è quasi sempre autoinflitta

A cura di:[Redazione](#molongui-disabled-link)  Ore 12 Giugno 20269 Giugno 2026

La Kubernetes security ha un avversario prevalente, e non è l’attaccante più sofisticato: è la configurazione. La piattaforma che orchestra i container in produzione nella maggior parte delle grandi organizzazioni è potente e flessibile, ma molte delle sue impostazioni predefinite privilegiano il funzionamento sulla restrizione. La conseguenza è che la superficie d’attacco di un cluster, più che subita, viene costruita da chi lo gestisce, una scelta di default accettata alla volta.

Non è un’impressione soggettiva, anche se le sfumature cambiano edizione per edizione. Le indagini Red Hat sullo stato della sicurezza di Kubernetes registrano da tempo che la grande maggioranza delle organizzazioni dichiara di aver subito almeno un incidente legato a container o cluster. Nelle rilevazioni del 2021 e del 2022 la configurazione errata era la preoccupazione più citata, intorno al 59 per cento; nelle edizioni più recenti il quadro si è distribuito tra errori di configurazione, vulnerabilità introdotte in fase di build e incidenti a runtime, segno che il problema non si è risolto ma si è articolato. Sono dati autodichiarati, da leggere come fotografia di percezione e non come misura assoluta, ma la configurazione resta uno dei vettori dominanti. La sicurezza di un cluster si gioca prima nelle scelte di chi lo configura che nella corsa alle patch.

## La superficie d’attacco è quasi sempre autoinflitta

Il caso limite lo ha mostrato il gruppo di vulnerabilità battezzato IngressNightmare, [divulgato nel marzo 2025](https://kubernetes.io/blog/2025/03/24/ingress-nginx-cve-2025-1974/). La falla più grave dell’insieme, CVE-2025-1974, valutata 9,8 su 10 nella scala CVSS, colpiva l’ingress controller basato su NGINX: concatenata a una delle vulnerabilità di annotation injection dello stesso gruppo, permetteva l’esecuzione di codice da remoto senza autenticazione. Il punto interessante non è il difetto in sé, ma il raggio dell’esplosione: secondo l’analisi pubblicata dai ricercatori di [Wiz sulla vulnerabilità](https://www.wiz.io/blog/ingress-nginx-kubernetes-vulnerabilities), da quel singolo componente un attaccante poteva leggere i segreti conservati in tutti i namespace del cluster, fino a prenderne il controllo completo. La stessa ricerca stimava che una quota rilevante degli ambienti cloud fosse esposta, con migliaia di cluster che pubblicavano il controller di ammissione direttamente su Internet.

Quel raggio d’azione è il vero insegnamento. In un cluster ben segmentato, la compromissione di un componente resta circoscritta. In un cluster configurato secondo i default, un punto di ingresso diventa una chiave per tutto. La differenza non la fa l’esistenza del CVE, la fa la postura del cluster intorno ad esso. Ed è qui che la sicurezza smette di essere una reazione e diventa progettazione.

## RBAC: il punto più sbagliato, quasi ovunque

Se esiste un singolo elemento in cui le configurazioni errate si concentrano, è il controllo degli accessi. Il modello di autorizzazione di Kubernetes, il [role-based access control](https://www.ictsecuritymagazine.com/articoli/role-based-access-control/) o RBAC, è potente ma facile da impostare male, e il margine tra un permesso ragionevole e un permesso pericoloso è sottile. L’errore archetipico ha una forma precisa: un binding che assegna il ruolo cluster-admin al service account predefinito di un namespace. Da quel momento ogni pod in quel namespace eredita il controllo totale del cluster, e un attaccante che comprometta una qualunque applicazione di quel namespace si trova in mano le chiavi dell’intera piattaforma.

La radice del problema è quasi sempre la stessa: permessi concessi in eccesso per comodità, e mai più ristretti. Un service account che potrebbe limitarsi a leggere una risorsa ottiene il diritto di crearne e cancellarne, perché così l’applicazione funziona subito e nessuno torna a stringere i privilegi dopo. Il principio del minimo privilegio, ovvio in teoria, è disatteso in pratica perché richiede di sapere esattamente cosa ciascun componente deve fare, e quella conoscenza costa tempo. La Kubernetes security su questo fronte non è una tecnologia da attivare, è una disciplina di igiene: assegnare il permesso necessario e niente di più, e verificare periodicamente che i token in circolazione non valgano più di quanto dovrebbero.

### I segreti che non sono segreti

C’è un corollario del controllo degli accessi che molti scoprono troppo tardi: in Kubernetes i Secret, l’oggetto pensato per custodire credenziali e chiavi, sono conservati per impostazione predefinita come stringhe codificate in base64, non cifrate. La codifica non è cifratura, e la differenza non è accademica: chiunque ottenga accesso in lettura a quegli oggetti, tramite l’API o direttamente dal datastore etcd, li riporta in chiaro in un istante. È esattamente il motivo per cui una falla capace di leggere i Secret di tutti i namespace, come ...
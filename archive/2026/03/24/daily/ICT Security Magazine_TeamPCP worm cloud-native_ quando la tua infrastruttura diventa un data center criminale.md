---
title: TeamPCP worm cloud-native: quando la tua infrastruttura diventa un data center criminale
url: https://www.ictsecuritymagazine.com/articoli/teampcp-worm-cloud-native/
source: ICT Security Magazine
date: 2026-03-24
fetch_date: 2026-03-25T04:17:39.841529
---

# TeamPCP worm cloud-native: quando la tua infrastruttura diventa un data center criminale

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

[![Cyber Crime Conference 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/Cyber-Crime-Conference-2026-1920x278-2.jpg)](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026)

![TeamPCP worm cloud-native](https://www.ictsecuritymagazine.com/wp-content/uploads/TeamPCP-worm-cloud-native.jpeg)

# TeamPCP worm cloud-native: quando la tua infrastruttura diventa un data center criminale

A cura di:[Redazione](#molongui-disabled-link)  Ore 24 Marzo 202613 Marzo 2026

Il TeamPCP *worm* cloud-native non è l’ennesimo *cryptominer* opportunistico che sfrutta un container mal configurato per rubare cicli di CPU. È qualcosa di strutturalmente diverso, e comprenderne la natura è urgente per chiunque gestisca infrastruttura cloud in produzione.

Il 5 febbraio 2026, il ricercatore Assaf Morag di [Flare](https://flare.io/learn/resources/blog/teampcp-cloud-native-ransomware) ha pubblicato un’analisi dettagliata di una campagna massiva osservata a partire dal 25 dicembre 2025: un’operazione *worm-driven* che ha compromesso sistematicamente API Docker esposte, cluster Kubernetes, dashboard Ray, server Redis e applicazioni vulnerabili a due distinte falle nei framework React e Next.js. L’obiettivo non era semplicemente infettare singoli host, ma costruire un’intera piattaforma criminale distribuita all’interno di ambienti cloud legittimi – una piattaforma capace di autopropagarsi, esfiltrare dati, distribuire *ransomware*, fare *mining* di criptovalute e fungere da trampolino per attacchi successivi.

La notizia ha raggiunto la comunità di sicurezza il 9 febbraio 2026 tramite [The Hacker News](https://thehackernews.com/2026/02/teampcp-worm-exploits-cloud.html), ma le implicazioni strategiche di TeamPCP vanno ben oltre la singola campagna. Questo articolo le analizza in profondità.

## Chi è TeamPCP: identikit di un ecosistema criminale cloud-native

TeamPCP – noto anche come DeadCatx3, PCPcat, PersyPCP e ShellForce – non è un singolo individuo né una gang *ransomware* tradizionale. È un’operazione ibrida che combina le funzioni di botnet, *access broker*, *data-leak crew* e piattaforma di *exploitation* cloud. Secondo il [report di Flare](https://flare.io/learn/resources/blog/teampcp-cloud-native-ransomware), l’attività del gruppo è tracciabile almeno da novembre 2025, con il primo messaggio registrato sul canale Telegram TeamPCP datato 17 novembre 2025. Il canale Telegram principale conta oltre 700 membri e viene utilizzato per pubblicare dati rubati, costruire reputazione e fare pressione sulle vittime. Il gruppo ha dichiarato pubblicamente di aver effettuato un *rebranding* a fine 2025, il che suggerisce attività precedente sotto altri nomi prima di consolidarsi come TeamPCP.

Un dettaglio investigativo rilevante riguarda il collegamento con il Kenya. Il 17 novembre 2025 – la stessa data del primo messaggio Telegram – un gruppo denominato “PCP@Kenya” ha [condotto un attacco coordinato](https://nation.africa/kenya/news/hackers-target-several-government-websites-temporarily-take-over-presidency-portal-5267412) contro i siti web del governo keniota, inclusi quelli della Presidenza e dei ministeri dell’Interno, della Sanità, dell’Istruzione e dell’Energia. Il sottosegretario all’Interno Raymond Omollo ha [attribuito l’attacco al gruppo PCP@Kenya](https://itweb.africa/article/update-cyber-attack-on-kenyas-government-sites/P3gQ2MGAQLwvnRD1). La coincidenza temporale e l’uso della sigla “PCP” suggeriscono un possibile legame con TeamPCP, sebbene l’attribuzione definitiva resti aperta.

Il dato più significativo, però, è un altro. La forza di TeamPCP non risiede in *exploit* innovativi o *malware* originale, ma nell’automazione su larga scala e nell’integrazione di tecniche d’attacco ben note. Come evidenziato nel report Flare, gran parte del codice dei *payload* è copiato e leggermente modificato – probabilmente con assistenza AI – piuttosto che sviluppato da zero. Il gruppo industrializza vulnerabilità esistenti, misconfigurazioni diffuse e strumenti open-source riadattati in una piattaforma di *exploitation* cloud-native che trasforma l’infrastruttura esposta in un ecosistema criminale autoproliferante.

In altre parole: TeamPCP è lo specchio oscuro del modello DevOps. Usa le stesse API, gli stessi *pattern* di automazione, la stessa logica di scalabilità che le organizzazioni impiegano per costruire le proprie infrastrutture. Solo che li usa per demolirle.

## La catena d’attacco: dall’API esposta al cluster compromesso

### Accesso iniziale: cinque porte aperte sul mondo

Il *playbook* di TeamPCP è opportunistico per *design*. Il gruppo esegue scansioni massicce su ampi range IP alla ricerca di servizi cloud-native esposti senza autenticazione o con credenziali deboli. I vettori di ingresso principali sono cinque:

1. **API Docker esposte** su Internet senza autenticazione, che consentono a chiunque di gestire container da remoto.
2. **API Kubernetes accessibili** con autenticazione anonima o credenziali deboli.
3. **Dashboard Ray non protette** – piattaforme di orchestrazione per *workload* di *machine learning* e AI.
4. **Istanze Redis** prive di password o raggiungibili dall’Internet pubblico.
5. **Applicazioni React/Next.js vulnerabili** a due falle critiche distinte: [CVE-2025-55182](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components) (React2Shell), la vulnerabilità di deserializzazione insicura nel protoco...
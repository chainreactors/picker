---
title: Adblock for YouTube: undici milioni di installazioni e una capacità di injection dormiente
url: https://www.ictsecuritymagazine.com/notizie/badblocker-adblock-youtube-chrome/
source: ICT Security Magazine
date: 2026-06-26
fetch_date: 2026-06-27T05:52:23.795897
---

# Adblock for YouTube: undici milioni di installazioni e una capacità di injection dormiente

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

![Adblock for YouTube undici milioni di installazioni e una capacità di injection dormiente](https://www.ictsecuritymagazine.com/wp-content/uploads/Adblock-for-YouTube-undici-milioni-di-installazioni-e-una-capacita-di-injection-dormiente.png)

# Adblock for YouTube: undici milioni di installazioni e una capacità di injection dormiente

A cura di:[Redazione](#molongui-disabled-link)  Ore 26 Giugno 202626 Giugno 2026

Un’estensione Chrome installata da oltre undici milioni di utenti, con 374.000 recensioni e 4,4 stelle, può trasformarsi in un canale di esecuzione di codice arbitrario su qualsiasi sito con una sola modifica lato server, senza aggiornamenti, senza una nuova revisione dello store e senza alcun segnale visibile per chi la usa. È la conclusione dell’analisi pubblicata il 25 giugno dai ricercatori Oleg Zaytsev e Shachar Gritzman di [Island](https://www.island.io/blog/badblocker-11-million-users-one-server-call-away-from-compromise), che hanno battezzato il caso *BadBlocker* esaminando *Adblock for YouTube* (ID
`cmedhionkhpnakcndndgjdbohmhepckk`
), presente sullo store dal 2014 e oggi trentunesima estensione complessivamente sul Chrome Web Store.

La precisazione è dovuta in apertura: i ricercatori non hanno osservato alcun *payload* malevolo distribuito agli utenti. Quella documentata è una capacità presente in produzione, non una compromissione in corso. La rilevanza per chi si occupa di sicurezza aziendale sta proprio nel divario fra ciò che una revisione statica mostra, un ad blocker funzionante, e ciò che l’estensione può ricevere l’istruzione di fare in seguito.

## Adblock for YouTube e i permessi da scrivere in bianco

Il primo elemento è il manifesto. Un blocco pubblicitario rivolto a un singolo sito dichiara
`host_permissions: ["<all_urls>"]`
, cioè il diritto di eseguire codice su ogni pagina visitata dal browser: webmail, applicazioni SaaS, console di amministrazione, strumenti interni. L’estensione contiene un controllo che dovrebbe limitare l’iniezione a YouTube, ma si tratta di una *regex* ingenua (
`/youtube.com/.test(url)`
) che cerca la stringa
`youtube.com`
in qualsiasi punto dell’URL completo. Un indirizzo come
`https://bank.example.com/search?q=youtube.com`
supera il filtro. Il risultato è un accesso a tutto il web governato da una verifica aggirabile con un parametro di query.

## Lo *scriptlet* che diventa esecuzione di codice

Ogni 24 ore l’estensione scarica la propria configurazione da un server remoto (
`api.adblock-for-youtube.com`
). La risposta include le normali regole di filtraggio, ma anche un campo
`scripletsRules`
con cui il server sceglie quali *scriptlet* eseguire e con quali argomenti. Uno di questi,
`trusted-create-element`
, può creare un tag
`<script>`
il cui contenuto arriva direttamente dal server e viene eseguito nel contesto della pagina (mondo
`MAIN`
), con accesso a DOM, sessioni, moduli e azioni dell’utente. Al momento dell’analisi lo *scriptlet* non era attivo nella risposta del server: la funzione è dormiente, non assente, e la sua attivazione richiede appunto una sola modifica di configurazione.

Per validare la catena, Island ha costruito una *proof of concept* con un server fittizio e l’estensione non modificata: partendo da YouTube, dove il controllo URL passa naturalmente, la stessa istruzione viene poi iniettata in una pagina Salesforce aperta nella sessione autenticata dell’utente (l’URL contiene ancora
`youtube.com`
in un parametro), leggendone i dati di account ed esfiltrandoli verso il server. La ricerca è stata [riepilogata anche](https://www.technadu.com/adblock-for-youtube-chrome-extension-hides-dormant-javascript-injection/629927/) da TechNadu, con diagramma e cronologia.

## Un’estensione che ha cambiato natura

Il profilo di rischio si aggrava guardando la storia del software, che ripropone uno schema già visto in altre [estensioni Chrome malevole](https://www.ictsecuritymagazine.com/articoli/estensioni-chrome-ai-malevole/). Intorno al 2018 l’estensione ha cambiato proprietà ed è stata riscritta, passando poi da alcune centinaia di migliaia a oltre dieci milioni di utenti; secondo [The Hacker News](https://thehackernews.com/2026/06/chrome-ad-blocker-with-10m-installs.html), percorsi di iniezione controllati da remoto sono presenti a partire da febbraio 2025. Versioni precedenti incorporavano l’SDK di ad-injection *Unistream*, associato ad attività di adware e rimosso a giugno 2024. Le estensioni sorelle *Adblock for Chrome* e *Adblock for You*, collegate alla stessa infrastruttura promozionale, sono state rimosse dal Chrome Web Store per malware, come documentato anche dal team di *threat intelligence* di GitLab (riferimento nel box fonti); una terza estensione collegata, *AdBlock Suite*, era già stata rimossa da Google a settembre 2023, e l’elenco non è esaustivo. L’estensione resta intanto disponibile (versione 7.2.2), operativa e segnalata dal badge *Featured* dello store, un dettaglio che alimenta la fiducia accumulata sul nome.

## Cosa cambia per le aziende

Il punto difeso da Island, che peraltro sviluppa un *enterprise browser* e ha quindi un interesse diretto nel tema della governance, è comunque solido sul piano t...
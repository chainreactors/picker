---
title: Account takeover: non è un attacco, è una catena di montaggio
url: https://www.ictsecuritymagazine.com/notizie/account-takeover/
source: ICT Security Magazine
date: 2026-07-05
fetch_date: 2026-07-06T06:18:21.396266
---

# Account takeover: non è un attacco, è una catena di montaggio

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

![account takeover](https://www.ictsecuritymagazine.com/wp-content/uploads/account-takeover.png)

# Account takeover: non è un attacco, è una catena di montaggio

A cura di:[Redazione](#molongui-disabled-link)  Ore 5 Luglio 20269 Giugno 2026

Account takeover è la presa di controllo di un account legittimo da parte di chi non ne è il titolare, e oggi assomiglia molto meno a un colpo ingegnoso che a una catena di montaggio. La ragione è che il presupposto su cui poggiava la sicurezza degli accessi, la segretezza della password, è venuto meno: le password non sono più segrete, sono già state rubate a miliardi e circolano in liste pronte all’uso. Un attaccante che vuole impossessarsi di un account, nella maggior parte dei casi, non deve violare nulla. Deve solo provare le credenziali giuste, e farlo su scala industriale.

Questo cambia la natura del problema. Non si tratta di fermare un intruso brillante che trova una falla, ma di reggere l’urto di un processo automatizzato, alimentato da credenziali rubate altrove e ripetuto miliardi di volte contro ogni pagina di accesso esistente. L’account takeover è la forma che la frode prende quando l’autenticazione si fonda su un segreto che non è più tale, ed è per questo che difendersi chiedendo agli utenti password più robuste è una battaglia già persa: la password, quasi sempre, è già nelle mani sbagliate.

## La password è un segreto già rubato

Il carburante di tutto questo è l’enorme massa di credenziali in circolazione. I programmi che rubano informazioni, gli *infostealer* come Lumma, StealC o Vidar, si installano sui dispositivi e ne estraggono le password salvate, i cookie e i token di sessione, riversando ogni giorno nuove credenziali fresche in un mercato che le rivende a poco; le [fughe da infostealer](https://www.f5.com/company/blog/16-billion-credentials-exposed-why-this-infostealer-leak-demands-a-rethink-of-bot-defense) hanno raggiunto una scala che impone di ripensare la difesa degli accessi. A questo si somma l’abitudine, durissima a morire, di riutilizzare la stessa password su più servizi: basta che trapeli da un sito qualunque perché diventi la chiave di decine di altri account della stessa persona. È il motore del [mercato nero delle credenziali](https://www.ictsecuritymagazine.com/notizie/mercato-nero-delle-credenziali/), dove l’attaccante non compra una vulnerabilità, compra direttamente le chiavi.

Il risultato è che, per moltissimi servizi, la barriera dell’accesso protegge un segreto che il difensore deve dare per già compromesso. L’attaccante non ha bisogno di indovinare nulla né di sfondare alcunché: prende un elenco di coppie nome utente e password ottenute da fughe precedenti, e le prova. Su questo terreno, l’errore più costoso è continuare a ragionare come se la password fosse ancora la prova dell’identità di chi la inserisce. Non lo è più, e la difesa deve partire da questa ammissione.

## Credential stuffing: il volume fa il danno

La tecnica che traduce le credenziali rubate in account compromessi si chiama *credential stuffing*, e la sua forza sta tutta nei numeri. Programmi automatici provano le coppie rubate contro le pagine di accesso di migliaia di servizi, in parallelo e senza sosta. La percentuale di tentativi che va a segno è bassissima, perché non tutte le credenziali sono ancora valide e non tutte sono riutilizzate, ma quando si moltiplica una probabilità minima per un volume enorme il prodotto resta grande. Pochi successi ogni mille tentativi, ripetuti su miliardi di tentativi, fanno una quantità industriale di account presi.

È un calcolo economico prima che tecnico. L’automazione costa pochissimo, le credenziali costano poco, e ogni account preso ha un valore, da svuotare, rivendere o usare come trampolino per altre frodi. La pagina di accesso, in questo schema, è la catena di montaggio su cui scorre il processo, e proteggerla significa rendere quel calcolo non più conveniente. Le linee guida dell’OWASP sulla [prevenzione del credential stuffing](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html) ruotano esattamente attorno a questo: alzare il costo e abbassare il tasso di successo dell’automazione.

## Difendere dall’account takeover: non basta una password migliore

Se la password è persa in partenza, la difesa deve agire su altri piani, e si costruisce a strati. Il primo è l’autenticazione a più fattori, che resta la misura singola più efficace: un’analisi di Microsoft del 2019, ormai un riferimento, stima che l’MFA avrebbe fermato oltre il 99,9 per cento delle compromissioni di account. È la fotografia di quel momento, precedente alla diffusione del furto di token e del phishing in tempo reale, e infatti stime più recenti della stessa Microsoft rivedono il valore di poco al ribasso. Aggiungere un secondo fattore vanifica gran parte del *credential stuffing*, perché la sola password non basta più a entrare. È il motivo per cui le stesse buone pratiche di settore la indicano come priorità, soprattutto per gli account più sensibili e i servizi esposti.

Ma l’MFA non è una linea di arrivo, e qui sta la sfumatura che molti trascurano. Lo stesso infostealer che ruba l...
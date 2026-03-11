---
title: Estensioni Chrome AI malevole: oltre 260.000 utenti trasformati in fonti di intelligence per il cybercrime
url: https://www.ictsecuritymagazine.com/articoli/estensioni-chrome-ai-malevole/
source: ICT Security Magazine
date: 2026-03-10
fetch_date: 2026-03-11T04:05:25.316234
---

# Estensioni Chrome AI malevole: oltre 260.000 utenti trasformati in fonti di intelligence per il cybercrime

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

![estensioni chrome ai malevole](https://www.ictsecuritymagazine.com/wp-content/uploads/estensioni-chrome-ai-malevole.jpeg)

# Estensioni Chrome AI malevole: oltre 260.000 utenti trasformati in fonti di intelligence per il cybercrime

A cura di:[Redazione](#molongui-disabled-link)  Ore 10 Marzo 20269 Marzo 2026

Le estensioni Chrome AI malevole stanno emergendo come uno dei vettori di compromissione più insidiosi nell’ecosistema *enterprise*, accanto al phishing tradizionale e alle tecniche di *social engineering* come ClickFix. [La settimana tra l’11 e il 16 febbraio 2026 ha reso questa realtà difficile da contestare](https://www.ictsecuritymagazine.com/notizie/zero-day-2026-patch-management/): in soli cinque giorni, tre campagne distinte e indipendenti hanno dimostrato che il browser non è più un semplice strumento di navigazione, ma un ambiente di esecuzione ad alto privilegio che gli attaccanti stanno imparando a sfruttare con precisione industriale.

Il 12 febbraio, i ricercatori di [LayerX](https://layerxsecurity.com/blog/aiframe-fake-ai-assistant-extensions-targeting-260000-chrome-users-via-injected-iframes/) hanno rivelato la campagna AiFrame: almeno 30 estensioni Chrome mascherate da assistenti AI – con nomi come “Gemini AI Sidebar”, “AI Assistant”, “ChatGPT Translate” – che hanno compromesso oltre 260.000 utenti (con alcune testate che riportano cifre fino a 300.000), sottraendo credenziali, contenuto delle email e cronologia di navigazione. L’11 febbraio, [Koi Security](https://www.koi.ai/blog/agreetosteal-the-first-malicious-outlook-add-in-leads-to-4-000-stolen-credentials) aveva documentato il primo add-in Outlook malevolo mai rilevato *in natura* – AgreeTo, un tool di scheduling abbandonato dal suo sviluppatore e rilevato da un attaccante che ne ha preso il controllo per rubare oltre 4.000 credenziali Microsoft. E nella stessa settimana, [Koi Security](https://www.koi.ai/blog/vk-styles-500k-users-infected-by-chrome-extensions-that-hijack-vkontakte-accounts) ha smascherato anche VK Styles, una rete di cinque estensioni che aveva silenziosamente dirottato oltre 500.000 account VKontakte.

Tre campagne. Due ecosistemi diversi – Chrome e Outlook. Un unico *pattern* strutturale: la fiducia implicita che utenti e organizzazioni ripongono nei marketplace ufficiali è diventata l’arma principale degli attaccanti.

Questo articolo non è un bollettino di sicurezza. È l’analisi di come il modello di distribuzione delle estensioni browser sia diventato strutturalmente vulnerabile e di cosa questo significhi per chi difende reti aziendali nel 2026.

## Il browser come superficie d’attacco privilegiata: perché le estensioni Chrome AI malevole funzionano

Per comprendere la gravità di quanto accaduto, occorre partire da un dato architetturale che la maggior parte dei professionisti della sicurezza conosce in teoria ma sottovaluta in pratica: le estensioni browser operano con privilegi che pochi altri componenti software possono vantare.

Un’estensione Chrome con i permessi giusti può leggere e modificare il contenuto di qualsiasi pagina web visitata dall’utente, accedere ai cookie di sessione, intercettare le richieste di rete, catturare il contenuto degli appunti e persino registrare audio attraverso l’API Web Speech. Il tutto in background, senza che l’utente noti nulla di anomalo. E la portata del fenomeno è tutt’altro che marginale: secondo il [LayerX Enterprise Browser Extension Security Report 2025](https://go.layerxsecurity.com/enterprise-browser-extension-security-report-2025), il 99% dei dipendenti enterprise ha almeno un’estensione browser installata, il che rende questa superficie d’attacco virtualmente universale negli ambienti aziendali.

Nel framework [MITRE ATT&CK](https://attack.mitre.org/), le tecniche sfruttate dalle campagne di febbraio 2026 si mappano con precisione: [T1176 – Browser Extensions](https://attack.mitre.org/techniques/T1176/) per l’installazione del componente malevolo, [T1539 – Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539/) per l’esfiltrazione dei cookie di sessione, [T1185 – Browser Session Hijacking](https://attack.mitre.org/techniques/T1185/) per l’intercettazione in tempo reale del contenuto delle pagine autenticate, e [T1557 – Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/) per l’architettura iframe che si interpone tra utente e servizio. Comprendere questa mappatura è essenziale per i SOC analyst che devono tradurre l’intelligence sulle minacce in regole di *detection* operative.

Secondo una [ricerca di Cybernews](https://cybernews.com/security/chrome-extensions-get-too-many-dangerous-permissions/), 86 delle 100 estensioni Chrome analizzate (selezionate tra le più diffuse e raccomandate) richiedono permessi classificabili come ad alto rischio al momento dell’installazione: *scripting*, accesso esteso agli host, monitoraggio delle tab. Un’[analisi condotta da Incogni](https://blog.incogni.com/chrome-extensions-privacy-2026/) nel gennaio 2026 su 442 estensioni AI ha rilevato che il 52% raccoglie almeno un tipo di dato utente e il 29% raccoglie informazioni personali identificabili.

Il problema non risiede nei permessi in sé – molte estensioni legittime ne necessitano di ampi per ...
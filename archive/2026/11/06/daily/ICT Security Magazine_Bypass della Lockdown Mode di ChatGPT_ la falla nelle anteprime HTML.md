---
title: Bypass della Lockdown Mode di ChatGPT: la falla nelle anteprime HTML
url: https://www.ictsecuritymagazine.com/notizie/bypass-lockdown-mode-chatgpt/
source: ICT Security Magazine
date: 2026-11-06
fetch_date: 2026-11-07T08:02:02.344376
---

# Bypass della Lockdown Mode di ChatGPT: la falla nelle anteprime HTML

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca nel magazine

* Argomenti

  [Cyber Security: tutti gli articoli 1.349 articoli](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

  Minacce e attacchi

  + [Vulnerabilità](https://www.ictsecuritymagazine.com/argomenti/vulnerabilita/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)

  Rischio, norme e privacy

  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)

  Tecnologie

  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)

  Scenari

  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Prospettive](https://www.ictsecuritymagazine.com/argomenti/prospettive/)

  Ultimi in **Cyber Security**

  [Tutti gli articoli di Cyber Security →](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Approfondimenti](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* [Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Eventi ↗](https://eventi.ictsecuritymagazine.com/)

[Newsletter](/newsletter/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/logo-ict-security-trasparente-1.webp)](https://www.ictsecuritymagazine.com/)

Cerca

Attiva/disattiva menu

[Vulnerabilità](https://www.ictsecuritymagazine.com/argomenti/vulnerabilita/) · [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/) · [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)

# Bypass della Lockdown Mode di ChatGPT: la falla nelle anteprime HTML

Check Point Research ha pubblicato il 5 novembre 2026 un bypass della Lockdown Mode di ChatGPT già corretto: le anteprime HTML permettevano di esfiltrare la chat. La correzione di OpenAI è del 18 settembre.

A cura di:[Redazione](https://www.ictsecuritymagazine.com/author/redazione/)  Ore Pubblicato il6 Novembre 20266 Novembre 2026  Condividi

![Bypass della Lockdown Mode di ChatGPT: la falla nelle anteprime HTML: Cornici concentriche di una finestra di anteprima da cui esce un riquadro che attraversa i bordi lasciando una scia di dati](https://www.ictsecuritymagazine.com/wp-content/uploads/bypass-lockdown-mode-chatgpt-anteprima-html.webp)

In sintesi

* Check Point Research ha aggirato la Lockdown Mode di ChatGPT sfruttando l'anteprima HTML dei blocchi di codice.
* Il difetto permetteva di inviare la cronologia della chat a un server esterno; in ChatGPT Classic bastava una conversazione.
* OpenAI ha corretto il problema il 18 settembre 2026 e Check Point, dopo una nuova prova, conferma che la tecnica non funziona più.

[Check Point Research](https://research.checkpoint.com/2026/chatgpt-lockdown-mode-bypass-phishing-malware-delivery-and-silent-data-exfiltration/) ha pubblicato il 5 novembre 2026 i dettagli di un bypass della Lockdown Mode di ChatGPT, già corretto da OpenAI. Il difetto non stava nella modalità di sicurezza, ma in un’altra funzione: l’anteprima HTML dei blocchi di codice. Finché non è stato corretto, un attaccante poteva portare la cronologia della chat su un server esterno, anche con la Lockdown Mode attiva.

La correzione è arrivata prima della pubblicazione. OpenAI ha comunicato a Check Point di averla rilasciata il 18 settembre 2026, quasi sette settimane prima. Check Point ha ripetuto la prova e la tecnica non funziona più.

## Che cos’è la Lockdown Mode

La [Lockdown Mode](https://openai.com/index/introducing-lockdown-mode-and-elevated-risk-labels-in-chatgpt/) è un’impostazione facoltativa di ChatGPT. OpenAI l’ha presentata il 13 febbraio 2026 per i piani Enterprise, Edu, Healthcare e Teachers. Il 4 giugno 2026 l’ha estesa agli account personali e a quelli Business self-service.

OpenAI la descrive come una scelta per chi ha esigenze di sicurezza particolari, per esempio dirigenti o team di sicurezza. Precisa che alla maggior parte degli utenti non serve.

Serve a ridurre l’esfiltrazione di dati tramite [prompt injection](/notizie/prompt-injection-negli-agenti-ai/), cioè tramite istruzioni ostili nascoste nei contenuti che il modello legge. La modalità non impedisce all’istruzione ostile di comparire. Limita le richieste di rete in uscita, che sono la strada con cui i dati arriverebbero a un attaccante. Secondo la [pagina di assistenza di OpenAI](https://help.openai.com/en/articles/20001061-lockdown-mode), applica queste restrizioni:

* navigazione web limitata ai contenuti in cache;
* niente immagini nelle risposte ordinarie né recupero di immagini dal web, mentre restano il caricamento di file e la generazione di immagini;
* Deep Research e Agent Mode disattivati;
* nessuna approvazione dell’accesso alla rete per il codice generato da Canvas;
* nessun download di file per l’analisi dei dati.

OpenAI avverte che la modalità riduce il rischio ma non garantisce che l’esfiltrazione sia impossibile. Il rischio può restare, scrive, attraverso le app abilitate, combinazioni impreviste di funzionalità o tecniche scoperte in seguito.

## Dove stava il problema: l’anteprima HTML

Secondo Check Point, OpenAI ha aggiunto a febbraio 2026 l’anteprima HTML ai blocchi di codice di ChatGPT. Quando il modello scrive una pagina HTML, la funzione la mostra direttamente nella chat. Come spiega The Hacker News, la pagina viene eseguita in una sandbox, cioè un ambiente isolato, pensato per impedire l’accesso a cookie e local storage e per bloccare le comunicazioni esterne senza consenso.

Secondo Check Point, la sandbox è formata da due iframe annidati, cioè due finestre incastrate una nell’altra. Tra le sue impostazioni c’erano
`allow-popups`
e
`allow-popups-to-escape-sandbox`
. La prima permette alla pagina di aprire finestre popup. La seconda lascia che il contenuto di quei popup esca dall’isolamento della sandbox.

## Come funzionava il bypass della Lockdown Mode di ChatGPT

Il bypass della Lockdown Mode di ChatGPT seguiva questi passaggi, secondo la ricostruzione di Check Point:

1. ChatGPT controllava la funzione JavaScript
   `window.open`
   , quella che apre un popup. Se l’indirizzo era vuoto o
   `about:blank`
   , non succedeva nulla e non compariva alcun avviso. Per qualsiasi altro indirizzo, ChatGPT chiedeva l’approvazione dell’utente.
2. Il controllo però valeva solo per quella copia della funzione. La pagina malevola creava un ulteriore iframe annidato e usava la funzione
   `contentWindow.open`
   di quell’iframe, che non aveva il controllo.
3. Il popup si apriva così senza approvazione e, grazie a
   `allow-popups-to-escape-sandbox`
   , usciva dalla sandbox.
4. Fuori dalla sandbox, il contenuto del popup non rispetta...
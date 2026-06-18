---
title: Prompt injection: dove dire una cosa significa farla
url: https://www.ictsecuritymagazine.com/notizie/prompt-injection-dire-significa-fare/
source: ICT Security Magazine
date: 2026-06-17
fetch_date: 2026-06-18T06:51:51.046191
---

# Prompt injection: dove dire una cosa significa farla

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

![Prompt injection](https://www.ictsecuritymagazine.com/wp-content/uploads/Prompt-injection.png)

# Prompt injection: dove dire una cosa significa farla

A cura di:[Redazione](#molongui-disabled-link)  Ore 17 Giugno 202611 Giugno 2026

Il prompt injection è in cima a tutte le classifiche di rischio dell’intelligenza artificiale. L’[OWASP](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) lo mette al primo posto tra le vulnerabilità dei sistemi a modello linguistico, e ne dà una spiegazione che vale più di mille allarmi: gli LLM non sono in grado di distinguere le istruzioni fidate dal contenuto non fidato. Il [NIST](https://csrc.nist.gov/pubs/ai/100/2/e2025/final), nella sua tassonomia del 2025, cataloga la variante diretta e quella indiretta, in cui l’ordine è nascosto in un documento, una pagina, una email che il modello si limita a leggere. E nel giugno 2025 [EchoLeak](https://nvd.nist.gov/vuln/detail/CVE-2025-32711) ha mostrato la cosa nella sua forma più pura: in una dimostrazione di ricerca, poi neutralizzata da una correzione lato server, una sola email senza un clic poteva indurre Microsoft 365 Copilot a esfiltrare dati riservati, perché tra le righe del messaggio c’era un’istruzione, e per il modello leggere un’istruzione o riceverla sono la stessa cosa. La chiamiamo vulnerabilità, e aspettiamo la patch. Ma non è un difetto del sistema. È la sua architettura.

## Prompt injection: un’architettura, non un bug

Per settant’anni la sicurezza informatica ha avuto un principio di fondo: tenere separate le istruzioni dai dati. Quasi ogni grande classe di attacchi, dall’SQL injection al buffer overflow, è il cedimento di quel confine, e la difesa è sempre stata ricostruirlo, spostando i dati in uno spazio che non verrà mai interpretato come comando. Già l’architettura di von Neumann, mettendo codice e dati nella stessa memoria, aveva reso quel confine fragile; il software vi aveva eretto sopra mille steccati. Il modello linguistico li abbatte tutti, per progetto.

Il prompt di sistema, l’input dell’utente, la pagina presa dal web, l’allegato: tutto arriva come un unico flusso di lingua naturale, e il modello decide in base al significato, non al canale. Nella lingua non esiste lo spazio separato in cui confinare i dati perché non vengano letti come ordini. Per questo il prompt injection non si neutralizza come si è neutralizzato l’SQL injection: là bastava una casella a parte, qui la casella non c’è. È quanto mostrano, nel concreto, le [vulnerabilità delle architetture AI](https://www.ictsecuritymagazine.com/notizie/architetture-ai-aziendali/) e perfino il malware che [si esegue appena letto](https://www.ictsecuritymagazine.com/notizie/worm-miasma-microsoft-github-agenti-ai-coding/) da un agente.

## Uso e menzione

La distinzione che la macchina perde ha un nome antico. Un essere umano sa benissimo che riferire un ordine non è darlo: «ha scritto: cancella tutto» racconta un comando, «cancella tutto» lo impartisce. La logica la chiama differenza tra uso e menzione, e le virgolette sono proprio il dispositivo della menzione, il modo di esibire una frase senza farla propria; un comando riferito è un comando messo tra virgolette. Lo distinguiamo con quelle virgolette, con il tono, con la cornice, con il sapere chi parla e con quale autorità. Il modello, che legge solo significato, appiattisce tutto: un’istruzione raccontata e un’istruzione data gli appaiono identiche, perché entrambe sono testo dotato di senso su cui può agire. La novità non è che leggere coincida con l’eseguire, cosa che un interprete di codice fa da decenni: è che sparisce il marcatore che separa il registro eseguibile da quello descrittivo. Nel codice una sintassi dice dove comincia il comando; nella lingua naturale no. Per la prima volta abbiamo un lettore-esecutore per cui capire un ordine e iniziare a eseguirlo non hanno più un confine segnato.

## Non esiste più il puro dire

Si scende ancora. Avevamo sempre dato per scontato di poter dire una cosa senza farla: descrivere, citare, ipotizzare, raccontare, pianificare, perfino mentire, tutto a distanza di sicurezza dall’atto. Austin chiamava costativo l’enunciato che descrive, performativo quello che, dicendo, fa. Per un agente che può agire su ciò che legge, la distinzione collassa: non c’è più enunciato puramente costativo, perché essere informati equivale a essere mossi.

E non basta apporre un timbro d’autorità sulle istruzioni legittime, perché, come aveva visto Derrida, la scrittura funziona in assenza di chi l’ha prodotta e di ogni contesto determinato: un segno scritto non porta in sé alcuna autorità, può essere citato, innestato, rigiocato altrove. Il modello legge scrittura pura, staccata da chi comanda. Il confine tra dato e istruzione non è mai stato nelle parole: lo mettevano il contesto e l’autorità, fuori di esse, e noi abbiamo costruito un lettore che non ha accesso né all’uno né all’altra. Il prompt injection è l’iterabilità della scrittura trasformata in arma.

Si obietterà che le difese esistono e per lo più funzionano: gerarchie di istruzioni, prompt di sistema, addestramento mirato, classificatori che fiutano l’iniezione. Alzano il costo, non chiud...
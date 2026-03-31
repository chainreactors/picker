---
title: Passkeys in azienda: guida tecnica alla migrazione FIDO2 per il CISO italiano
url: https://www.ictsecuritymagazine.com/notizie/passkeys-in-azienda/
source: ICT Security Magazine
date: 2026-03-30
fetch_date: 2026-03-31T04:37:25.658425
---

# Passkeys in azienda: guida tecnica alla migrazione FIDO2 per il CISO italiano

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

![passkeys](https://www.ictsecuritymagazine.com/wp-content/uploads/passkeys.jpeg)

# Passkeys in azienda: guida tecnica alla migrazione FIDO2 per il CISO italiano

A cura di:[Redazione](#molongui-disabled-link)  Ore 30 Marzo 202627 Marzo 2026

Nel febbraio 2026, Microsoft ha registrato oltre 600 milioni di attacchi alle identità al giorno secondo il [Microsoft Digital Defense Report 2025](https://www.microsoft.com/en-us/security/security-insider/intelligence-reports/microsoft-digital-defense-report-2025). La maggior parte sfrutta una sola debolezza strutturale: le password. Le passkeys non sono l’ennesimo upgrade alla MFA, sono la sua sostituzione.

## Il problema che le passkeys risolvono davvero

La MFA basata su TOTP (Google Authenticator, Microsoft Authenticator) e su SMS OTP ha rappresentato per anni lo standard de facto per la protezione degli account aziendali. Come già analizzato su ICT Security Magazine nell’approfondimento sull’[autenticazione multifattoriale nell’era della cyber-vulnerabilità](https://www.ictsecuritymagazine.com/articoli/mfa/), il paradigma passwordless rappresenta l’evoluzione naturale dell’MFA. Nel 2026, tuttavia, quella stessa MFA è diventata un bersaglio primario degli attaccanti.

[Gli attacchi Adversary-in-the-Middle (AiTM)](https://www.ictsecuritymagazine.com/notizie/email-di-phishing/) – implementati attraverso piattaforme Phishing-as-a-Service come EvilProxy e Tycoon 2FA – intercettano i token TOTP in tempo reale, trasmettendoli al servizio legittimo prima della scadenza. Il [Microsoft Digital Defense Report 2025](https://www.microsoft.com/en-us/security/security-insider/intelligence-reports/microsoft-digital-defense-report-2025) documenta una crescita rapida di queste tecniche, che rendono la MFA tradizionale inefficace contro attaccanti motivati.

Le passkeys eliminano il problema alla radice. Il meccanismo si basa su crittografia asimmetrica: il dispositivo dell’utente genera una coppia di chiavi, conserva la chiave privata in un enclave sicuro (TPM su Windows, Secure Enclave su iOS/macOS, TEE su Android) e invia al servizio solo la chiave pubblica. Al momento dell’autenticazione, il server invia una challenge; il dispositivo la firma con la chiave privata dopo che l’utente si è verificato tramite biometrica o PIN locale. Nessuna password, nessun codice OTP, nessun segreto condiviso trasmesso in rete. Senza un segreto da intercettare, l’attacco AiTM non ha superficie su cui agire.

### Come funziona tecnicamente una passkey

1. **Registrazione:** il dispositivo genera una coppia RSA/EC (chiave pubblica e privata). La pubblica viene inviata al server (Relying Party). La privata non lascia mai il dispositivo.
2. **Autenticazione:** il server invia una challenge casuale. Il dispositivo sblocca la chiave privata tramite biometrica o PIN, firma la challenge e invia la firma.
3. **Verifica:** il server verifica la firma con la chiave pubblica in suo possesso. Nessuna password, nessun OTP, nessun segreto condiviso.

Standard di riferimento: [WebAuthn (W3C)](https://www.w3.org/TR/webauthn-3/) + [CTAP2 (FIDO Alliance)](https://fidoalliance.org/specs/fido-v2.2-rd-20230321/fido-client-to-authenticator-protocol-v2.2-rd-20230321.html) = FIDO2

## Dove siamo: lo stato del mercato nel 2026

I numeri certificano che la transizione è in corso, non solo annunciata. Secondo la [ricerca FIDO Alliance e HID condotta su 400 executive](https://blog.hidglobal.com/passkey-adoption-workforce-what-numbers-say) in aziende con oltre 500 dipendenti, l’**87% delle organizzazioni** ha già effettuato il deployment delle passkeys enterprise o è in fase di rollout attivo, una crescita di 14 punti percentuali rispetto all’anno precedente. Due terzi dichiarano che il deployment è una priorità alta o critica.

Sul fronte consumer, il **75% degli utenti globali** è oggi consapevole delle passkeys ([FIDO Alliance, 2025](https://fidoalliance.org/passkey-index-2025/)), e quasi la metà dei 100 siti web più visitati al mondo le supporta già come metodo di accesso, più del doppio rispetto al 2022. [Bitwarden ha registrato](https://www.descope.com/blog/post/2025-fido-report) un incremento del **550%** nelle creazioni giornaliere di passkeys nel 2025, segnale che l’adozione cross-provider è diventata mainstream.

![passkeys](https://www.ictsecuritymagazine.com/wp-content/uploads/Screenshot-2026-03-27-alle-10.14.49.png)

## Passkeys sincronizzate vs. device-bound: la scelta che determina il livello di sicurezza

Prima di avviare qualsiasi progetto di migrazione, il CISO deve comprendere una distinzione fondamentale che determina il livello di assurance raggiungibile.

### Passkeys sincronizzate (synced passkeys)

Vengono conservate nel cloud keychain del produttore del sistema operativo (iCloud Keychain su Apple, Google Password Manager, Windows/Microsoft) e sincronizzate tra tutti i dispositivi associati allo stesso account. Sono comode per gli utenti – cambio dispositivo senza procedure di re-enrollment – e soddisfano il livello AAL2 secondo il [NIST SP 800-63-4](https://pages.nist.gov/800-63-4/) nella versione finale del luglio 2025. Sono adatte per applicazioni SaaS, portali self-service e accessi a sistemi non critici.

### Passkeys device-bound (hardware-bound)
...
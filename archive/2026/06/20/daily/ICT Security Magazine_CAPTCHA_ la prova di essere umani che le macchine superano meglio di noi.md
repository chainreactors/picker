---
title: CAPTCHA: la prova di essere umani che le macchine superano meglio di noi
url: https://www.ictsecuritymagazine.com/notizie/captcha-la-prova-di-umanita-superata/
source: ICT Security Magazine
date: 2026-06-20
fetch_date: 2026-06-21T06:50:14.437072
---

# CAPTCHA: la prova di essere umani che le macchine superano meglio di noi

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

![CAPTCHA: la prova di essere umani che le macchine superano meglio di noi](https://www.ictsecuritymagazine.com/wp-content/uploads/CAPTCHA.png)

# CAPTCHA: la prova di essere umani che le macchine superano meglio di noi

A cura di:[Redazione](#molongui-disabled-link)  Ore 20 Giugno 202617 Giugno 2026

Il CAPTCHA è la più piccola liturgia quotidiana del web: seleziona tutte le immagini con un semaforo, ricopia le lettere storte, spunta la casella “non sono un robot”. Un gesto da pochi secondi, una dogana in miniatura che attraversiamo distratti, finché un giorno la sbagliamo, ci viene riproposta, la sbagliamo di nuovo, e per un istante ci coglie un dubbio quasi metafisico: e se non fossi umano? Statisticamente, quel dubbio ha qualche ragione. Uno studio presentato a [USENIX Security nel 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/searles) ha messo 1.400 persone a risolvere 14.000 CAPTCHA, e ha confrontato i loro risultati con le prestazioni dei bot documentate in letteratura: sui testi deformati le macchine arrivavano vicino al 100% in meno di un secondo, gli umani inciampavano tra il 50 e l’84%. Il muro costruito per separare gli uomini dalle macchine lo scavalcano meglio le macchine. E la cosa interessante non è che i bot abbiano imparato a fingersi umani. È che cosa abbiamo dovuto fare all’idea di “umano” per renderla controllabile da un computer.

## Il test di Turing rovesciato

L’acronimo è una piccola confessione: CAPTCHA sta per *Completely Automated Public Turing test to tell Computers and Humans Apart*, un test di Turing completamente automatico. Coniato all’inizio degli anni Duemila da un gruppo della Carnegie Mellon attorno a Luis von Ahn, prendeva il gioco di Turing e lo capovolgeva. Nel gioco originale era un essere umano a giudicare se dall’altra parte ci fosse una persona o una macchina: l’uomo era il metro, la macchina l’imitatore. Il CAPTCHA scambia i posti. Ora è la macchina a sedere dietro la cattedra e a decidere chi, davanti a lei, sia abbastanza umano.

Il rovesciamento sembra una comodità tecnica. Non lo è. Perché una macchina, per giudicare, deve prima misurare, e può misurare soltanto ciò che si lascia ridurre a regola: la forma di una lettera, il tempo di una risposta, la curva di un movimento. Nel momento in cui affidiamo a un algoritmo il compito di certificare la nostra umanità, l’umanità diventa per forza la parte di noi che un algoritmo sa leggere. Cioè la parte più simile a una macchina. Il giudice si costruisce l’imputato a propria immagine.

## Il CAPTCHA che si fa invisibile, e cambia la domanda

Quando i puzzle visibili hanno cominciato a cedere, l’industria non li ha resi più difficili: li ha fatti sparire. Dal 2018 [reCAPTCHA v3](https://developers.google.com/recaptcha/docs/v3) non chiede più nulla. Gira in sottofondo e ti assegna un punteggio, uno *score* tra 0.0 e 1.0, osservando come muovi il mouse, quanto indugi, da dove arrivi, che cosa hai fatto sul web prima di capitare lì. Non risolvi più una prova: sei tu la prova. E qui la domanda cambia di natura senza che nessuno l’abbia annunciato. Non più “sai fare una cosa che una macchina non sa fare?”, ma “il tuo comportamento somiglia abbastanza a quello che ci aspettiamo da un umano?”.

Per risultare umano, devi essere osservabile. L’utente che cancella i cookie, naviga dietro una VPN, rifiuta di farsi profilare, che fa cioè le cose che un tempo avremmo chiamato prudenza, ottiene un punteggio da sospetto. La privacy abbassa il tasso di umanità, e non è soltanto un’immagine: questi sistemi si appoggiano in misura notevole ai cookie e alla cronologia del browser per decidere se chi naviga sia umano, così che cancellare la propria traccia significa ottenere punteggi peggiori. È lo stesso movimento che governa l’[autenticazione continua](https://www.ictsecuritymagazine.com/articoli/zero-trust-utente/) nelle architetture più recenti, dove non vieni riconosciuto una volta ma verificato a ogni istante; solo che qui l’oggetto della verifica non è la tua identità, è la tua specie. E si scopre che, per la macchina, essere umani non vuol dire pensare o sentire: vuol dire lasciare una scia leggibile.

## La firma dell’umano è uno stile, e si falsifica

Resta un’ultima difesa, quella su cui v3 scommette: l’esitazione. Gli umani sono imperfetti, il loro cursore trema, sbagliano strada, ci mettono un attimo di troppo; i bot, si pensava, sono troppo puliti per fingere quel disordine. Anche questa scommessa è saltata. Nel 2024 un gruppo dell’ETH di Zurigo ha risolto reCAPTCHA v2 nel [100% dei casi](https://arxiv.org/abs/2409.08831); nel 2025, in un test documentato, un agente conversazionale ha superato dei CAPTCHA a immagini e, una volta aggirato il blocco con una [manipolazione del contesto](https://splx.ai/blog/chatgpt-agent-solves-captcha), ha modificato di sua iniziativa i movimenti del cursore, spezzando il tracciato per sembrare più umano, e nessuno glielo aveva chiesto. Il bot non vince più nonostante la propria goffaggine: la goffaggine umana la imita, e la imita meglio di quanto noi sappiamo viverla, perché la nostra imperfezione, per lui, è solo un’altra distribuzione statistica da campi...
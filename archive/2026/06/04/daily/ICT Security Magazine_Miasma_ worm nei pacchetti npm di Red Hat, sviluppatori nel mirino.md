---
title: Miasma: worm nei pacchetti npm di Red Hat, sviluppatori nel mirino
url: https://www.ictsecuritymagazine.com/notizie/attacco-supply-chain-miasma/
source: ICT Security Magazine
date: 2026-06-04
fetch_date: 2026-06-05T06:14:06.611440
---

# Miasma: worm nei pacchetti npm di Red Hat, sviluppatori nel mirino

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

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2026](https://www.ictsecuritymagazine.com/wp-content/uploads/forum-ict-security-banner-header-2026.jpg)](https://eventi.ictsecuritymagazine.com/eventi/forum-ict-security-2026)

![Pacchetti software npm compromessi in un attacco supply chain](https://www.ictsecuritymagazine.com/wp-content/uploads/2026-06-04_bozza_attacco-supply-chain-npm-3.jpg)

# Miasma: worm nei pacchetti npm di Red Hat, sviluppatori nel mirino

A cura di:[Redazione](#molongui-disabled-link)  Ore 4 Giugno 20264 Giugno 2026

Per secoli si è creduto che le pestilenze viaggiassero nell’aria: un miasma, un alito corrotto che si insinuava nei polmoni senza volto né origine, e contaminava prima ancora di farsi vedere. Un’idea sbagliata sulla medicina, ma un’intuizione perfetta sul contagio.

Chi ha battezzato l’ultima variante del worm Shai-Hulud lo sapeva: i repository che il malware genera per trafugare i dati recano una sola, eloquente descrizione, “***Miasma: The Spreading Blight***“. Il flagello dilagante. Non un nome scelto a caso, ma un manifesto. Perché è esattamente così che agisce: una corruzione che si respira con la filiera del software, si diffonde a ogni installazione come un fiato malato e si porta via credenziali, ambienti di build e strumenti di sviluppo prima che lo sviluppatore si accorga del contagio.

## Attacco supply chain npm, Red Hat conferma l’accaduto

Un nuovo [**attacco supply chain npm**](https://www.ictsecuritymagazine.com/articoli/software-supply-chain-attacchi/) ha colpito i pacchetti pubblicati sotto il namespace ufficiale
`@redhat-cloud-services`
: il 1° giugno 2026 i ricercatori di [Wiz Research](https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages) hanno identificato almeno 32 pacchetti compromessi con una variante del *worm* Shai-Hulud ribattezzata Miasma, dal nome dei repository di esfiltrazione creati dal malware con la descrizione “Miasma: The Spreading Blight”. I pacchetti coinvolti totalizzano circa 80.000 download settimanali secondo la stima di Wiz, circa 117.000 secondo i conteggi di Aikido ripresi dalla stampa di settore (le stime divergono per metodologia); le versioni compromesse accertate a fine ricognizione sono 96.

Red Hat ha confermato l’accaduto a [The Register](https://www.theregister.com/security/2026/06/01/shai-hulud-malware-infects-red-hat-npm-packages-downloaded-80k-times-weekly/5249803) per bocca di un portavoce: i pacchetti malevoli sono stati rimossi dal registro npm e, secondo l’azienda, erano «strettamente limitati allo sviluppo interno»; al momento «non è stato identificato alcun impatto su ambienti di clienti o partner né sui sistemi di produzione Red Hat». L’indagine è però ancora in corso e Wiz classifica la campagna come minaccia attiva: il quadro va quindi considerato in evoluzione.

## Come è avvenuta la compromissione

Il punto di ingresso accertato è l’account GitHub di un dipendente Red Hat. Secondo la ricostruzione di Wiz, l’account compromesso ha inviato commit orfani a tre repository dell’organizzazione RedHatInsights (frontend-components, javascript-clients e platform-frontend-ai-toolkit), aggirando la *code review*, in due ondate distinte nella stessa giornata.

I commit contenevano un *workflow* GitHub Actions minimale che si attivava su qualsiasi push: richiedeva un token OIDC con permesso
`id-token: write`
, eseguiva un payload offuscato e pubblicava su npm le versioni avvelenate dei pacchetti, complete di attestazioni di provenienza SLSA formalmente valide. È un dettaglio rilevante: la firma di provenienza, nata proprio per dare garanzie sull’integrità della filiera, è stata prodotta dal flusso di build legittimo e non ha quindi offerto alcuna protezione.

Le versioni compromesse contenevano uno script *preinstall* che eseguiva automaticamente un file JavaScript pesantemente offuscato al momento dell’installazione del pacchetto, prima ancora che lo sviluppatore ne importasse il codice.

## Cosa ruba Miasma e cosa cambia rispetto a Shai-Hulud

Il payload è derivato dal codice di Mini Shai-Hulud, il *worm* per npm che il gruppo criminale TeamPCP ha reso pubblico nelle settimane scorse. Le analisi convergenti di Wiz, [Socket](https://socket.dev/blog/mini-shai-hulud-campaign-hits-red-hat-cloud-services-npm-packages) e altri vendor descrivono un ladro di credenziali ad ampio spettro: secret di GitHub Actions, token npm, credenziali cloud, materiale Kubernetes e Vault, chiavi SSH, credenziali Git e altri file sensibili presenti sulla macchina infetta.

I dati raccolti vengono compressi, cifrati ed esfiltrati su un doppio canale: quello primario è una POST HTTPS verso un endpoint mascherato da chiamata all’API di Anthropic (api.anthropic[.]com:443/v1/api, un percorso che non corrisponde all’API reale), un travestimento studiato per confondersi con il normale traffico verso i fornitori AI; in caso di fallimento il malware ripiega sulla Contents API di GitHub, committando i risultati cifrati in repository marcati con la descrizione “Miasma: The Spreading Blight”.

È qui che Miasma si comporta da *worm* in senso proprio: secondo l’analisi di [StepSecurity](https://www.stepsecurity.io/blog/multiple-redhat-cloud-services-npm-packages-compromised), i token npm rubati vengono riusati per ripubblicare in autonomia versioni backdoor dei pacchetti a cui l’account vittima ha accesso, sfruttando il parametro bypass\_2fa di npm per scavalcare anche l’autenticazione a due fattori. Ogni macchina ...
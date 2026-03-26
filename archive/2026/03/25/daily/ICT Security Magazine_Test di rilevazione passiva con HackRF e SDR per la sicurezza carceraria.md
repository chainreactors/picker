---
title: Test di rilevazione passiva con HackRF e SDR per la sicurezza carceraria
url: https://www.ictsecuritymagazine.com/articoli/hackrf-sdr/
source: ICT Security Magazine
date: 2026-03-25
fetch_date: 2026-03-26T04:32:01.814262
---

# Test di rilevazione passiva con HackRF e SDR per la sicurezza carceraria

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

![Test di rilevazione passiva con HackRF e SDR per la sicurezza carceraria](https://www.ictsecuritymagazine.com/wp-content/uploads/Test-di-rilevazione-passiva-con-HackRF-e-SDR-per-la-sicurezza-carceraria.jpeg)

# Test di rilevazione passiva con HackRF e SDR per la sicurezza carceraria

A cura di:[Stefano Cangiano](#molongui-disabled-link)  Ore 25 Marzo 202610 Marzo 2026

Dopo aver analizzato nei precedenti articoli la storia dell’adozione dei jammer nelle carceri italiane e i loro limiti tecnici, sanitari e normativi, questo ultimo approfondimento presenta i risultati concreti di test sperimentali condotti in ambiente controllato utilizzando hardware HackRF One. L’obiettivo era validare in condizioni realistiche l’efficacia dei sistemi di rilevazione passiva basati su tecnologia SDR (Software-Defined Radio), verificandone la capacità di rilevare, classificare e [localizzare attività cellulare non autorizzata](https://www.ictsecuritymagazine.com/articoli/imsi-catcher/).

Per validare l’efficacia dei sistemi di rilevazione passiva in condizioni realistiche, sono stati condotti *test* approfonditi utilizzando *hardware* HackRF One presso un sito isolato appositamente predisposto. L’obiettivo era verificare la capacità del sistema di rilevare, classificare e localizzare attività cellulare non autorizzata in un ambiente che simulasse le condizioni operative di un istituto penitenziario.

## Ambiente di test controllato per rilevazione passiva SDR

Per sviluppare e valutare il sistema di rilevamento in condizioni controllate, è stato creato un ambiente isolato completamente privo di copertura cellulare legittima, caratteristiche che lo rendevano analogo a un’ala carceraria idealmente schermata. In questo spazio “pulito” dal punto di vista elettromagnetico, ogni segnale radio percepito nelle bande cellulari proveniva necessariamente da un telefono di prova introdotto deliberatamente, eliminando qualsiasi ambiguità nell’interpretazione dei risultati.

Sono stati introdotti in modo casuale più telefoni di diversi operatori (Vodafone, TIM, WindTre, Iliad) in vari momenti della giornata e della notte, simulando l’accensione sporadica e imprevedibile dei dispositivi da parte di uno o più detenuti. L’uso dei telefoni è stato distribuito nel tempo secondo *pattern* variabili, talvolta concentrato nelle ore diurne, talaltra nelle ore notturne, per ricreare le condizioni di imprevedibilità che caratterizzano l’uso reale dei telefoni di contrabbando. Questo *setup* ha permesso di mettere alla prova il sistema nelle stesse condizioni operative di un vero carcere.

### Sorveglianza continua dello spettro

All’interno dell’area simulata, il sistema ha monitorato ininterrottamente tutte le bande cellulari rilevanti (700, 800, 900, 1800, 2600 MHz) oltre alle frequenze Wi-Fi e *Bluetooth*, 24 ore su 24, 7 giorni su 7. La sorveglianza continua è essenziale perché un telefono di contrabbando potrebbe trasmettere solo per pochi secondi in orari totalmente inaspettati: una chiamata breve alle 3 di notte, un SMS inviato durante il cambio turno, una sessione dati di pochi minuti durante l’ora d’aria.

Nella pratica carceraria reale si impiegano più sonde o antenne distribuite strategicamente nell’istituto, convogliando i dati su una *console* centrale per garantire che nessuna zona resti scoperta. Non appena un telefono avvia una chiamata, invia un SMS o si collega ai dati mobili, i suoi segnali RF di *uplink* vengono captati in tempo reale. In un ambiente privo di segnali cellulari legittimi, ogni *burst* di trasmissione risalta in modo netto e inequivocabile, come una luce accesa in una stanza buia.

### **Registrazione automatica e post-analisi**

Ogni evento RF catturato durante i *test* è stato registrato automaticamente dal sistema, generando un *log* cronologico completo con data, ora precisa al secondo, frequenza/banda di trasmissione, potenza del segnale ricevuto e classificazione automatica del tipo di attività (chiamata voce GSM, chiamata voce LTE, SMS, traffico dati). Ogni attivazione dei telefoni di prova ha creato un *record* dettagliato e permanente nel *database* del sistema.

Questo approccio garantisce che anche se il personale di sorveglianza non dovesse intervenire immediatamente – per qualsiasi ragione – [l’attività rimane tracciata e consultabile in seguito per analisi forensi](https://www.ictsecuritymagazine.com/articoli/digital-forensics-si-evolve-la-legge-reati-informatici/), procedimenti disciplinari o indagini penali. Il *log* costituisce una prova documentale solida, con *timestamp* verificabili e dati oggettivi non soggetti a interpretazione.

L’interfaccia del sistema permette di navigare agevolmente nei dati storici, selezionando data e ora per ottenere un resoconto visivo degli eventi rilevati in qualsiasi periodo. È possibile, ad esempio, ispezionare le ore notturne di un determinato giorno per verificare eventuali trasmissioni, o confrontare l’attività di settimane diverse per identificare *pattern* ricorrenti. Una *timeline* grafica mostra i *burst* rilevati con indicazione del tipo e della potenza, mentre filtri configurabili permettono di isolare le trasmissioni per operatore, per banda o per tipologia di traffico.

### Sistema di rilevamento intellige...
---
title: Protocolli ICS: il linguaggio della fabbrica è insicuro per progetto
url: https://www.ictsecuritymagazine.com/industrial-cyber-security/protocolli-ics-sicurezza/
source: ICT Security Magazine
date: 2026-07-20
fetch_date: 2026-07-21T05:03:09.191843
---

# Protocolli ICS: il linguaggio della fabbrica è insicuro per progetto

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

![Protocolli ICS](https://www.ictsecuritymagazine.com/wp-content/uploads/Protocolli-ICS.png)

# Protocolli ICS: il linguaggio della fabbrica è insicuro per progetto

A cura di:[Redazione](#molongui-disabled-link)  Ore 20 Luglio 202614 Giugno 2026

Protocolli ICS è il nome collettivo dei linguaggi con cui i sistemi di controllo industriale impartiscono ordini al mondo fisico: aprire una valvola, far girare un motore, leggere la temperatura di un reattore. Sono protocolli come Modbus, DNP3, EtherNet/IP, e condividono una caratteristica che continua a sorprendere chi viene dalla sicurezza informatica: non sono insicuri per un difetto, lo sono per progetto. Quando furono concepiti, decenni fa, l’idea stessa di proteggerli non aveva senso, perché vivevano in reti chiuse e isolate dove la presenza fisica equivaleva all’autorizzazione. Quell’assunzione non vale più, ma i protocolli sono rimasti gli stessi.

La conseguenza è netta e scomoda. Su questi protocolli un comando legittimo e un comando malevolo sono indistinguibili: nessuno dei due porta una firma, una credenziale, una prova di chi lo ha mandato. Un ordine che apre una valvola appare identico che provenga dal pannello dell’operatore o da un intruso che è riuscito a raggiungere la rete. E poiché milioni di dispositivi parlano questi linguaggi, non si tratta di un problema che si chiude con un aggiornamento: è un’eredità con cui la sicurezza industriale deve convivere.

## Modbus, o l’innocenza di una rete che si fidava

Modbus è l’archetipo, e la sua storia spiega il resto. Nato nel 1979 per la comunicazione seriale tra dispositivi industriali, presupponeva una rete chiusa in cui chiunque avesse accesso fisico era, per definizione, qualcuno di cui fidarsi. In quel contesto non serviva autenticazione, non serviva cifratura, non serviva nemmeno un controllo di integrità: il messaggio arrivava su un cavo a cui solo le persone autorizzate potevano collegarsi. La sua versione su rete IP, il Modbus TCP, non ha aggiunto sicurezza, ha solo messo quel linguaggio del 1979 su una rete moderna e raggiungibile.

Il risultato è che un server Modbus accetta comandi da qualunque indirizzo riesca a contattarlo, senza nome utente, senza password, senza scambio di certificati. E poiché il protocollo non distingue la lettura dalla scrittura come privilegi diversi, un attaccante che lo raggiunge non si limita a osservare: può scrivere nei registri che governano il processo, e anche una modifica minima ai valori da cui un impianto dipende può mandarlo fuori controllo. Modbus è solo il caso più noto: DNP3, EtherNet/IP, S7comm e gli altri protocolli industriali condividono lo stesso peccato d’origine, trasmettendo in chiaro e senza autenticazione.

## Quando la rete chiusa si è aperta

Tutto questo era sostenibile finché l’assunzione di partenza reggeva, cioè finché quelle reti restavano davvero isolate. La digitalizzazione degli impianti, la convergenza tra informatica e tecnologia operativa, l’accesso da remoto per la manutenzione hanno smontato quell’isolamento, collegando a reti raggiungibili sistemi nati per restare chiusi. In molti casi i dispositivi industriali sono finiti esposti direttamente su Internet. Le scansioni grezze contano oltre diecimila sistemi in ascolto sulla porta 502, quella predefinita di Modbus; non tutte quelle porte aperte corrispondono a veri dispositivi industriali, ma quando i ricercatori filtrano il rumore ciò che resta è comunque allarmante: un’[indagine di Comparitech](https://www.comparitech.com/news/critical-infrastructure-at-risk-179-ics-devices-exposed-online/) del 2026, scartando honeypot ed emulatori, ha confermato 179 dispositivi di controllo realmente esposti, alcuni appartenenti a infrastrutture critiche reali, tra cui una rete ferroviaria nazionale e due reti elettriche. Il punto non è il numero grande, è che bastano pochi sistemi raggiungibili sui bersagli giusti. E non serve illudersi che spostare la porta predefinita basti a nascondersi: i dispositivi si identificano dalla risposta del protocollo, non dal numero della porta, e uno scanner che interroga il linguaggio industriale li trova comunque.

Su questo terreno si sono mossi gli attacchi più gravi alle infrastrutture critiche. Industroyer, che nel dicembre 2016 colpì la rete elettrica ucraina, fece leva proprio sulla mancanza di meccanismi di sicurezza nei protocolli di controllo per impartire comandi agli impianti. [Triton, noto anche come Trisis](https://www.ic3.gov/CSA/2022/220325.pdf), andò oltre, prendendo di mira i controllori dei sistemi strumentati di sicurezza di un impianto, quelli che dovrebbero intervenire per evitare il disastro: un attacco concepito per disabilitare l’ultima barriera tra un processo fuori controllo e il danno fisico alle persone. In entrambi i casi i protocolli non hanno opposto alcuna resistenza, perché non erano fatti per opporne.

## Difendere i protocolli ICS che non si possono cambiare

Qui sta il cuore del problema pratico: non si può semplicemente correggere un protocollo del 1979 che milioni di dispositivi parlano, né riavviare in massa impianti che devono restare in funzione. La difesa, allora, non sta dentro il protocollo ma int...
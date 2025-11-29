---
title: Sicurezza SCADA e ICS tra persistenza degli attaccanti e opacità dei sistemi legacy
url: https://www.ictsecuritymagazine.com/articoli/sicurezza-scada-ics/
source: ICT Security Magazine
date: 2025-11-28
fetch_date: 2025-11-29T03:13:06.188696
---

# Sicurezza SCADA e ICS tra persistenza degli attaccanti e opacità dei sistemi legacy

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
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

![sicurezza dei sistemi ICS e SCADA, tra infrastrutture industriali connesse e vulnerabilità digitali.](https://www.ictsecuritymagazine.com/wp-content/uploads/sicurezza-scada-ics-scaled.jpeg)

# Sicurezza SCADA e ICS tra persistenza degli attaccanti e opacità dei sistemi legacy

A cura di:[Redazione](#molongui-disabled-link)  Ore 28 Novembre 202528 Novembre 2025

Quando parliamo di [sicurezza dei sistemi SCADA](https://www.ictsecuritymagazine.com/articoli/scada-insecurity-unanalisi-approfondita-sulla-superficie-di-attacco-del-noto-sistema-di-controllo-industriale/) e degli ambienti *Industrial Control Systems* (ICS), ci troviamo di fronte a un paradosso che raramente viene esplicitato con la necessaria chiarezza: stiamo applicando paradigmi di difesa concepiti per l’*information technology* a infrastrutture progettate in un’epoca in cui la connettività non era nemmeno contemplata come scenario di rischio. Questa discrasia temporale e concettuale non è una semplice curiosità storica, ma rappresenta il nucleo stesso delle vulnerabilità che caratterizzano gli ambienti di controllo industriale.

La convergenza IT-OT, termine divenuto quasi un mantra nel lessico della *cybersecurity* industriale, nasconde una verità scomoda: non stiamo assistendo a una vera convergenza, quanto piuttosto a una colonizzazione forzata di ecosistemi operativi da parte di tecnologie pensate per contesti radicalmente diversi. I sistemi SCADA che gestiscono [infrastrutture critiche](https://www.ictsecuritymagazine.com/notizie/ics-ot-e-scada-security-a-rischio-le-infrastrutture-critiche/) – dalle reti elettriche agli impianti di trattamento delle acque, dai processi petrolchimici ai sistemi di trasporto – sono nati in un paradigma di sicurezza basato sull’isolamento fisico e sull’oscurità attraverso la segretezza. L’*air gap* era la strategia difensiva per eccellenza, e la proprietà dei protocolli industriali garantiva una forma di sicurezza attraverso l’opacità.

Questo paradigma è stato progressivamente eroso non solo dalla necessità di interconnessione per finalità di efficienza operativa e manutenzione remota, ma anche dall’inevitabile obsolescenza tecnologica. I sistemi ICS hanno cicli di vita che possono estendersi per decenni, ben oltre qualsiasi orizzonte temporale concepibile per le tecnologie IT. Ne deriva una situazione in cui controllori logici programmabili (*Programmable Logic Controller*, PLC) che risalgono agli anni Novanta coesistono con interfacce *web* moderne, creando superfici d’attacco ibride che sfidano i tradizionali modelli di *threat modeling*.

## Vulnerabilità endemiche: oltre la superficie del CVE

La narrazione comune sulla sicurezza ICS tende a concentrarsi sulle vulnerabilità *software* catalogate nei database CVE (*Common Vulnerabilities and Exposures*), sulle *patch* mancanti, sui protocolli industriali privi di autenticazione. Questa prospettiva, pur tecnicamente accurata, rischia di essere riduttiva. Le vulnerabilità più insidiose dei sistemi SCADA non risiedono necessariamente in falle di codice sfruttabili con *exploit* preconfezionati, ma nella stessa architettura epistemologica che sottende questi sistemi.

Consideriamo la questione dell’autenticazione nei protocolli industriali *legacy* come **Modbus**, **DNP3** o **IEC 60870-5-104**. L’assenza di meccanismi crittografici in questi standard non è un difetto di progettazione nel senso convenzionale del termine: è la conseguenza di requisiti funzionali che privilegiavano la deterministica temporale, la semplicità di implementazione e la resilienza operativa rispetto a qualsiasi considerazione di sicurezza informatica. Questi protocolli, progettati decenni fa, non prevedevano autenticazione, trasmettevano in chiaro e operavano in ambienti considerati fisicamente isolati. Quando un PLC Modbus risponde a qualsiasi comando ricevuto senza verificare l’identità del mittente, non sta “sbagliando” – sta operando esattamente secondo le specifiche per cui è stato progettato.

La vulnerabilità vera, allora, non è tecnica ma sistemica: risiede nel fatto che questi protocolli sono oggi esposti a contesti di minaccia per i quali non erano stati concepiti. L’implementazione di *wrapper* crittografici o di soluzioni di *network segmentation*, per quanto necessarie, rappresentano toppe applicate *a posteriori* su una superficie che non era stata pensata per riceverle. Questo genera nuove categorie di rischi: l’*overhead* computazionale dei meccanismi di sicurezza può introdurre latenze incompatibili con i requisiti *real-time* dei processi industriali, mentre la complessità aggiuntiva aumenta la superficie di errori di configurazione.

Un’altra categoria di vulnerabilità frequentemente sottovalutata riguarda la dimensione fisica degli ambienti OT (*Operational Technology*). A differenza degli attacchi puramente informatici, gli scenari di compromissione ICS possono includere vettori che combinano accesso fisico e manipolazione digitale. La modifica di *setpoint* su un PLC accessibile fisicamente in un impianto poco presidiato, la sostituzione di sensori per fornire letture alterate, l’inserimento di dispositivi *rogue* nella rete industriale durante interventi di manutenzione: questi sono vettori d’attacco che sfuggono ai perimetri difensivi tradizionali e richiedono un approccio olistico che integri *physical security*, *supply chain security* e *cybersecurity* in senso stretto.

## APT su ICS: anatomia di una persis...
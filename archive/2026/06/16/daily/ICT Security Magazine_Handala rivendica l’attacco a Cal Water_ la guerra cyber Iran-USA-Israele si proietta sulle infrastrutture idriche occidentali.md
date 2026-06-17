---
title: Handala rivendica l’attacco a Cal Water: la guerra cyber Iran-USA-Israele si proietta sulle infrastrutture idriche occidentali
url: https://www.ictsecuritymagazine.com/notizie/handala-cal-water-guerra-cyber-iran-usa-israele/
source: ICT Security Magazine
date: 2026-06-16
fetch_date: 2026-06-17T07:03:57.675798
---

# Handala rivendica l’attacco a Cal Water: la guerra cyber Iran-USA-Israele si proietta sulle infrastrutture idriche occidentali

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

![Handala colpisce un'utility idrica USA la guerra cyber Iran-Israele](https://www.ictsecuritymagazine.com/wp-content/uploads/Handala-colpisce-unutility-idrica-USA-la-guerra-cyber-Iran-Israele-.png)

# Handala rivendica l’attacco a Cal Water: la guerra cyber Iran-USA-Israele si proietta sulle infrastrutture idriche occidentali

A cura di:[Redazione](#molongui-disabled-link)  Ore 16 Giugno 202616 Giugno 2026

Il fronte cibernetico del conflitto tra Iran e Israele esce dai confini mediorientali e raggiunge un servizio essenziale negli Stati Uniti. L’11 giugno 2026 la società di *intelligence* [Dataminr](https://www.dataminr.com/resources/intel-brief/cyber-intel-brief-handala-claims-breach-of-california-water-service/) ha emesso un *Flash alert* sulla rivendicazione del gruppo *Handala*, riconducibile agli interessi dell’intelligence iraniana, contro California Water Service (Cal Water), tra i maggiori operatori idrici statunitensi, con circa due milioni di utenti serviti in oltre 100 comunità della California; il 16 giugno [Industrial Cyber](https://industrialcyber.co/utilities-energy-power-water-waste/iran-linked-handala-group-targets-cal-water-exposing-potential-pathways-between-it-and-ot-environments/) ha ripreso e ampliato il caso. Non si tratta di un incidente isolato: è l’ennesima estensione, verso le infrastrutture critiche degli alleati di Israele, di una campagna che gli analisti collegano direttamente all’escalation militare regionale.

## Che cosa è successo

Gli attaccanti hanno diffuso un *data dump* dimostrativo da 5 GB che, secondo Dataminr, contiene informazioni di fatturazione dei clienti, dati personali e credenziali amministrative associate a una rete interna di correzione GPS distribuita su più distretti. Il distretto di Chico risulta confermato tra gli account compromessi, con tracce di accesso al database di *billing* (nomi, indirizzi di servizio, numeri di telefono, numeri di conto e storico dei pagamenti).

Il vettore tecnico è l’aspetto più istruttivo per chi gestisce reti convergenti IT/OT. Gli attaccanti hanno ottenuto l’accesso amministrativo a un’istanza di RTKBase, un *NTRIP caster* open source usato dalle squadre sul campo per ricevere correzioni GPS centimetriche durante la mappatura e la manutenzione delle reti idriche. La rete di correzione si estendeva su sette *mountpoint* distrettuali. Il sistema, esposto sulla porta HTTP 10000 e operativo da circa 783 ore continuative, è valutato come probabile punto di accesso iniziale o di movimento laterale verso l’ambiente di fatturazione. Le credenziali amministrative e la password di un *mountpoint* NTRIP sono state pubblicate in chiaro nel materiale dimostrativo: vanno considerate interamente compromesse e ruotate immediatamente, insieme a ogni sistema in cui possano essere state riutilizzate.

## Perché è una notizia geopolitica, non solo un data breach

*Handala* è valutato con alta confidenza come una struttura di facciata affiliata al MOIS, tracciata come *Void Manticore* (Check Point Research), Storm-0842 (Microsoft) e *Banished Kitten* (CrowdStrike). Operativo da dicembre 2023, ha intensificato in modo netto le operazioni contro obiettivi statunitensi dopo l’avvio dell’[ingaggio militare USA-Iran](https://www.ictsecuritymagazine.com/notizie/cyber-guerra-iran-usa-israele/) del 28 febbraio 2026. Il movente è più specifico di una generica ritorsione: *Handala* ha presentato l’intrusione come rappresaglia per presunti attacchi statunitensi contro le infrastrutture idriche iraniane. È questo schema acqua-per-acqua a spiegare la scelta del bersaglio e a saldarsi alla dottrina dichiarata del gruppo, che colpisce i sistemi *life-sustaining* per massimizzare l’impatto psicologico e sociale, con uno schema a doppio bersaglio (rete di supporto operativo più database rivolto ai cittadini) che privilegia la visibilità multidominio rispetto alla persistenza silenziosa.

Il dato rilevante per la *threat intelligence*: a oggi non vi è evidenza di manomissione dei processi di trattamento o di disservizi su sistemi SCADA o di distribuzione. [Cal Water](https://www.securityweek.com/cal-water-investigating-iranian-hackers-claims/) ha confermato il 16 giugno di avere aperto un’indagine; la rivendicazione e la pubblicazione del *dump* risalgono all’11 giugno e coinvolgono i sistemi collegati ai distretti di Bakersfield, Visalia e Chico, mentre il momento effettivo dell’intrusione potrebbe essere anteriore (lo suggeriscono le 783 ore di operatività continuativa di RTKBase). L’utility e le autorità dichiarano comunque che non vi è evidenza di compromissione dell’approvvigionamento idrico né di interruzioni del servizio. Va inoltre detto con chiarezza che nulla, nelle prove pubblicate, [sostiene la capacità del gruppo di interrompere l’erogazione](https://www.securitymagazine.com/articles/102368-security-experts-discuss-validity-of-handalas-cal-water-hacking-claim) idrica: gli esperti ricordano che *Handala* ha un precedente di sopravvalutazione delle proprie capacità, e il claim “potevamo chiudere l’acqua” va trattato come operazione psicologica più che come dimostrazione tecnica. Resta il fatto che il gruppo dispone di un arsenale distru...
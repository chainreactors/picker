---
title: APN privata: la rete che nessuno sorvegliava e che ha portato l’attaccante dentro una centrale di cogenerazione
url: https://www.ictsecuritymagazine.com/industrial-cyber-security/apn-privata-la-rete-che-nessuno-sorvegliava-e-che-ha-portato-lattaccante-dentro-una-centrale-di-cogenerazione/
source: ICT Security Magazine
date: 2026-08-11
fetch_date: 2026-08-12T04:02:48.607121
---

# APN privata: la rete che nessuno sorvegliava e che ha portato l’attaccante dentro una centrale di cogenerazione

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

![APN privata come vettore di attacco OT il caso polacco di CERT Polska](https://www.ictsecuritymagazine.com/wp-content/uploads/APN-privata-come-vettore-di-attacco-OT-il-caso-polacco-di-CERT-Polska.png)

# APN privata: la rete che nessuno sorvegliava e che ha portato l’attaccante dentro una centrale di cogenerazione

A cura di:[Redazione](#molongui-disabled-link)  Ore 11 Agosto 202611 Agosto 2026

CERT Polska ha pubblicato l’8 agosto 2026 il [rapporto integrativo](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf) sugli attacchi al settore energetico polacco del dicembre 2025. Emerge un secondo impianto colpito, mai reso noto prima, e soprattutto un vettore di accesso alla rete OT che, per quanto risulta al CERT, non era mai stato osservato in un attacco reale: una APN privata, cioè la rete cellulare dedicata che il distributore di energia usa per il telecontrollo dei propri impianti.

## Un guasto che non era un guasto

Il 29 dicembre 2025, verso le sette del mattino, i sistemi di controllo industriale di una centrale di cogenerazione che serve circa 50.000 residenti sono stati colpiti. Si sono fermati una turbina a vapore e l’impianto di trattamento delle acque di processo, con conseguente interruzione del ciclo di cogenerazione. La reazione rapida del personale ha contenuto il fermo a un intervallo breve, senza alcuna interruzione della fornitura di calore o di energia elettrica agli utenti finali.

Era in corso un’attività di manutenzione. L’esercente ha quindi ipotizzato in prima battuta un errore degli ingegneri dell’appaltatore e ha segnalato l’evento a titolo puramente informativo. CERT Polska, che in quelle ore stava già trattando altri eventi analoghi nel settore, ha però aperto la gestione dell’incidente muovendo dall’ipotesi di un attacco informatico. L’analisi ha confermato l’ipotesi, e ha ricondotto l’accesso iniziale a un percorso che nessuno stava sorvegliando: una APN privata.

Il punto merita di essere sottolineato, perché è quello che il CERT stesso mette in evidenza: senza una segnalazione trasmessa per un semplice malfunzionamento inspiegato, l’episodio non sarebbe stato ricondotto alla campagna. La cultura della notifica non riguarda soltanto gli incidenti confermati.

L’indagine è durata oltre tre mesi. Per questo l’episodio non compariva nel [rapporto iniziale del 30 gennaio 2026](https://cert.pl/en/posts/2026/01/incident-report-energy-sector-2025/), dedicato agli attacchi coordinati contro più di trenta impianti eolici e fotovoltaici, un’azienda privata del settore manifatturiero e una grande centrale di cogenerazione che fornisce calore a quasi mezzo milione di utenti. L’impianto di cui si parla qui è un secondo, più piccolo sito di cogenerazione, colpito in parallelo. Il rapporto integrativo è stato presentato da Marcin Dudek, responsabile di CERT Polska, al DEF CON di Las Vegas, ed è accompagnato da un [comunicato ufficiale del team](https://cert.pl/en/posts/2026/08/incident-follow-up-report-energy-sector-2025/).

## L’indagine a ritroso: un PLC come postazione dell’attaccante

L’analisi dei log ha permesso di individuare il dispositivo dal quale l’attaccante aveva operato: un controllore WAGO PFC200 dotato di modem cellulare integrato. Un’anomalia in sé, perché gli attacchi contro reti industriali condotti direttamente a partire da un PLC non rientrano fra gli scenari abitualmente osservati negli ambienti OT.

Il dispositivo, però, era stato danneggiato. Nonostante l’esame forense in laboratorio, che ha richiesto la dissaldatura del chip di memoria, non è stato possibile recuperare alcun dato. L’indagine è quindi proceduta per ipotesi successive, lavorando a ritroso dagli effetti osservati verso il punto di compromissione iniziale.

La prima ipotesi, quella di un’esposizione accidentale del controllore su Internet, è stata scartata analizzando la presenza di dispositivi di quel tipo nello spazio di indirizzamento polacco nel periodo rilevante. È emerso invece che il controllore comunicava con i sistemi di un operatore di distribuzione, il DSO, tramite una SIM attestata su una rete privata di trasmissione dati gestita dallo stesso DSO. Una APN privata, appunto.

Vale la pena anticipare un elemento metodologico, perché torna due volte nella ricostruzione e ha un peso non secondario: alcuni degli anelli della catena non sono stati ricavati dai sistemi delle vittime, ma dai log dell’operatore di rete mobile, correlati con quelli disponibili in centrale. Senza quella collaborazione, buona parte del percorso sarebbe rimasta indimostrabile.

## Dal parco eolico all’APN privata: il primo anello

Per capire come l’attaccante sia arrivato lì occorre tornare agli attacchi contro i parchi eolici, che avevano interessato oltre trenta punti di connessione alla rete, cioè i punti in cui un impianto di produzione rinnovabile si collega alla rete di distribuzione e al suo operatore.

Ogni sottostazione compromessa ospitava un dispositivo FortiGate con funzione di concentratore VPN e firewall. In tutti i casi l’interfaccia VPN era raggiungibile da Internet e consentiva l’autenticazione con account definiti localmente nella configurazione del disp...
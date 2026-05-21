---
title: POTÆbox: la minaccia hardware che bypassa la cybersecurity
url: https://www.ictsecuritymagazine.com/articoli/potaebox-hardware-cybersecurity/
source: ICT Security Magazine
date: 2026-05-20
fetch_date: 2026-05-21T06:03:58.810331
---

# POTÆbox: la minaccia hardware che bypassa la cybersecurity

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

![](https://www.ictsecuritymagazine.com/wp-content/uploads/Luca-Bongiorni-Director-del-Cybersecurity-Lab-di-ZTE-Italia-Cyber-Crime-Conference-2026-scaled.jpg)

# POTÆbox: la minaccia hardware che bypassa la cybersecurity

A cura di:[Redazione](#molongui-disabled-link)  Ore 20 Maggio 202615 Maggio 2026

*Dall’intervento di Luca Bongiorni, Director del Cybersecurity Lab di ZTE Italia, alla 1[4ª Cyber Crime Conference](https://eventi.ictsecuritymagazine.com/eventi/cyber-crime-conference-2026) (Roma, 6-7 maggio 2026).*

## Una sfida al SOC, prima ancora che una presentazione

Luca Bongiorni apre il suo intervento con una frase che è insieme titolo e provocazione: «POTÆbox, la minaccia hardware che bypassa la cybersecurity». Il sottotitolo, ammette lui stesso, ha il sapore di un *sales pitch*, ma è in realtà una sfida lanciata direttamente al pubblico in sala. La proposta è disarmante nella sua semplicità: costruite un pentest dropbox, installatelo nella vostra azienda o nel vostro dipartimento, e cronometrate quanto tempo impiegherà il SOC ad accorgersene. Se la detection arriva, fatemelo sapere.

Bongiorni, Director del Cybersecurity Lab di ZTE Italia e fondatore della community WHID (We Hack In Disguise), porta sul palco vent’anni di ricerca applicata su un tema che la narrazione mainstream tende a trascurare: l’impianto hardware malevolo. Un oggetto fisico, di pochi centimetri, capace di vanificare investimenti milionari in Endpoint Detection and Response, Network Access Control e Security Information and Event Management.

#### Il caso TechEx: il precedente più recente

Il primo esempio scelto da Bongiorni per inquadrare il fenomeno è di una freschezza sorprendente: 24 marzo 2026. I servizi di controintelligence ucraini rendono pubblica la scoperta di un impianto hardware nascosto dai servizi segreti russi all’interno del telaio di una porta, negli uffici di TechEx, contractor della difesa ucraina specializzato in sistemi counter-drone contro gli Shahed iraniani e i Geran-2 e Geran-3 russi.

![POTÆbox: la minaccia hardware che bypassa la cybersecurity - Luca Bongiorni, Director del Cybersecurity Lab di ZTE Italia, Cyber Crime Conference 2026: Hardware Threats hacking hardware Hardware Security hardware attacks ](https://www.ictsecuritymagazine.com/wp-content/uploads/POWERPNT_q6p12vb2IA-700x393.jpg)

*Luca Bongiorni, Director del Cybersecurity Lab di ZTE Italia, Cyber Crime Conference 2026*

Il dispositivo, mostrato nelle foto pubblicate da Kyiv, non è un capolavoro di *spycraft* sovietico: è una banale board di telecamera IP, modello XM 3MP Network Camera Module Chip IVG-G3H H.265 GK7201V200, acquistabile online per 8,72 euro. Una scheda che si collega via Wi-Fi o Ethernet (la versione installata sul campo era cablata, come si nota dall’immagine del cavo Ethernet) e che viene impiegata per condurre acoustic surveillance sulle conversazioni interne all’azienda.

La scelta operativa della controintelligence ucraina merita attenzione. Una volta scoperto l’impianto, anziché rimuoverlo subito, il personale di TechEx è stato istruito a immettere deliberatamente informazioni false nelle conversazioni captabili dal microfono: un’operazione di deception a costo zero, resa possibile proprio dalla natura passiva del bug hardware.

#### Una storia che si ripete: dai porti alle banche

La cronologia presentata da Bongiorni dimostra come l’uso offensivo di impianti hardware non sia né nuovo né confinato all’ambito nation-state. Alcuni esempi tra quelli citati:

* **NASA / Jet Propulsion Laboratory (2018):** un Raspberry Pi collegato abusivamente alla rete del laboratorio di Pasadena permette l’esfiltrazione di 500 MB di dati relativi a missioni. Il Single Board Computer viene rilevato solo dopo mesi.
* **Caso *Raspberry Pi in our network closet* (2019):** un’azienda austriaca scopre nel proprio rack un Raspberry Pi collegato alla LAN interna, dotato di chiavette USB Wi-Fi e Bluetooth, occupato a esfiltrare dati verso l’esterno. L’episodio, documentato sul blog di Christian Haschek, è diventato un classico della threat intel hardware-side.
* **Porto di Anversa (2011-2013), Operation Ocean’s 13:** uno dei casi più studiati nella letteratura sul cybercrime organizzato. Trafficanti olandesi ingaggiano black hat per violare i sistemi informatici dei porti di Anversa e Rotterdam con un obiettivo preciso: tracciare i container, dirottarne il ritiro e sottrarli ai controlli doganali. Dopo una prima fase di compromissione via spear phishing (rilevata e contenuta dalle autorità portuali), gli attaccanti cambiano strategia e passano al canale fisico, introducendo nelle sedi degli operatori portuali power strip modificate, farcite di Single Board Computer, keylogger hardware e connettività cellulare. Il caso, raccontato in dettaglio nell’inchiesta Bloomberg *The Mob’s IT Department* e in fonti Europol, si chiude con il sequestro di circa una tonnellata di cocaina e una di eroina.
* **DarkVishnya (2017-2018):** Kaspersky documenta una campagna contro istituti finanziari dell’Europa orientale in cui gli attaccanti accedono fisicamente alle filiali bancarie e collegano direttamente ai segmenti di rete interni dispositivi hardware a basso costo (notebook entry-level, Raspberry Pi, Bash Bunny) per condu...
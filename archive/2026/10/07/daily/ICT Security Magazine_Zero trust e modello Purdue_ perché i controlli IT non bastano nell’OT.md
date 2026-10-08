---
title: Zero trust e modello Purdue: perché i controlli IT non bastano nell’OT
url: https://www.ictsecuritymagazine.com/articoli/zero-trust-modello-purdue-ot/
source: ICT Security Magazine
date: 2026-10-07
fetch_date: 2026-10-08T08:08:20.933962
---

# Zero trust e modello Purdue: perché i controlli IT non bastano nell’OT

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

![raffigura i 4 livelli che spiegano la parte industriale, it e controllo: Modello Purdue e Zero Trust negli ambienti OT](https://www.ictsecuritymagazine.com/wp-content/uploads/Modello-Purdue-e-Zero-Trust-negli-ambienti-OT_Protezione-distribuita-tra-IT-e-OT.png)

# Zero trust e modello Purdue: perché i controlli IT non bastano nell’OT

A cura di:[Vincenzo Calabrò](#molongui-disabled-link)  Ore 7 Ottobre 20261 Ottobre 2026

*Il modello Purdue aiuta a comprendere perché latenza, disponibilità continua, sistemi legacy e requisiti di safety rendono inefficace il trasferimento diretto dei controlli IT agli ambienti OT.*

Nella [prima parte della serie](https://www.ictsecuritymagazine.com/articoli/zero-trust-ot-air-gap/) Vincenzo Calabrò ha spiegato perché la fine dell’air gap impone di ripensare la sicurezza degli impianti industriali, e perché lo zero trust non può essere applicato all’OT in modo uniforme.

Questa seconda parte fornisce gli strumenti per orientarsi: i principi della NIST SP 800-207, l’organizzazione degli impianti secondo il modello Purdue e le ragioni tecniche per cui i controlli IT non si trasferiscono. Il paragrafo 2.3 merita attenzione particolare: introduce i cinque attributi di idoneità che torneranno in tutto il framework.

## Modello Purdue e Zero Trust negli ambienti OT

Fondamenti dello Zero Trust, anatomia degli ambienti OT e limiti del trasferimento diretto dei controlli EIT.

### Zero Trust: dai perimetri alle identità

Lo zero trust non è un prodotto o una tecnologia specifica, ma una strategia di sicurezza basata su un insieme di principi. La NIST SP 800-207 ne enuncia i principi fondamentali:

* tutte le risorse di dati e di calcolo sono trattate come tali, indipendentemente dalla loro posizione;
* ogni comunicazione è protetta, a prescindere dalla rete su cui transita;
* l’accesso alle singole risorse è concesso per sessione, sulla base del principio del privilegio minimo;
* le decisioni di accesso sono determinate da una policy dinamica che considera l’identità del richiedente, lo stato del dispositivo e altri attributi comportamentali e ambientali;
* l’organizzazione monitora e misura costantemente l’integrità e la postura di sicurezza dei propri asset, applica e rivaluta in modo continuo l’autenticazione e l’autorizzazione e raccoglie quante più informazioni possibili sullo stato corrente, al fine di migliorare nel tempo la propria postura.[[1]](#_ftn1)

Sul piano logico, questi principi si traducono in un’architettura in cui il piano di controllo e il piano dei dati sono nettamente separati. Il policy engine, il cuore decisionale del sistema, esegue un algoritmo di fiducia per concedere, negare o revocare l’accesso; il policy administrator instaura o interrompe il canale di comunicazione in base alla decisione presa; il policy enforcement point, collocato lungo il percorso tra il soggetto e la risorsa, applica materialmente l’esito.[[2]](#_ftn2)

Il passaggio concettuale più rilevante consiste nello spostare il baricentro dei controlli dalla segmentazione basata su parametri di rete quali indirizzi, sottoreti e perimetri, verso l’identità di utenti, dispositivi e servizi, con politiche di autorizzazione costruite attorno ad attributi anziché a topologie.[[3]](#_ftn3)

La letteratura ha contribuito a sistematizzare il campo: la rassegna di Syed et al. offre una tassonomia esaustiva delle architetture e delle componenti zero trust,[[4]](#_ftn4) mentre Fernandez e Brazhuk ne propongono un’analisi critica, mettendo in luce le ambiguità definitorie e nodi irrisolti nella traduzione dei principi in pratica.[[5]](#_ftn5) Bertino, da parte sua, invita a una valutazione misurata dei benefici effettivi, ricordando che lo zero trust non è una panacea ma una strategia il cui valore dipende dalla qualità dell’implementazione.[[6]](#_ftn6)

### Modello Purdue: come sono organizzati gli ambienti OT

Per comprendere perché lo zero trust non può essere trasferito senza adattamenti nell’ambito OT, è necessario osservare la struttura tipica di un ambiente OT. Il modello architetturale dominante è il modello Purdue, derivato dalla Purdue Enterprise Reference Architecture, elaborata all’inizio degli anni Novanta da Williams e dal consorzio universitario sul Computer Integrated Manufacturing.[[7]](#_ftn7) Concepito originariamente per razionalizzare i flussi informativi negli impianti automatizzati, il modello è stato adottato dalla comunità della sicurezza, in quanto la gerarchia funzionale che descrive si presta a delimitare confini difensivi naturali.

La serie di standard ISA/IEC 62443 ha adottato questa stratificazione traducendola nei concetti di zone e conduits: raggruppamenti di sistemi con requisiti di sicurezza omogenei e canali di comunicazione controllati che li collegano e ciascuno associato a un livello di sicurezza target commisurato al rischio.[[8]](#_ftn8) La Figura 1 riassume questa organizzazione.

![L’architettura di rete OT secondo il modello Purdue prevedei livelli funzionali, la zona demilitarizzata IT/OT e l’intensificarsi dei vincoli di tempo reale verso il processo fisico.](https://www.ictsecuritymagazine.com/wp-content/uploads/chrome_M46f0OmqDP-700x613.png)
...
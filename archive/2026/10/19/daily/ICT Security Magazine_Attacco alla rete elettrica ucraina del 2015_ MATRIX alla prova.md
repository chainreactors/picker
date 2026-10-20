---
title: Attacco alla rete elettrica ucraina del 2015: MATRIX alla prova
url: https://www.ictsecuritymagazine.com/articoli/attacco-alla-rete-elettrica-ucraina-2015/
source: ICT Security Magazine
date: 2026-10-19
fetch_date: 2026-10-20T06:53:46.704256
---

# Attacco alla rete elettrica ucraina del 2015: MATRIX alla prova

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

![raffigurazione della rete elletrica tramite tralicci e cyber attacco che fa diventare i tralicci rossi. Attacco alla rete elettrica ucraina del 2015 MATRIX alla prova e modello zero trust](https://www.ictsecuritymagazine.com/wp-content/uploads/Attacco-alla-rete-elettrica-ucraina-del-2015-MATRIX-alla-prova-2.png)

# Attacco alla rete elettrica ucraina del 2015: MATRIX alla prova

A cura di:[Vincenzo Calabrò](#molongui-disabled-link)  Ore 19 Ottobre 20262 Ottobre 2026

*Dagli standard OT a un incidente reale: MATRIX viene confrontato con NIST, IEC 62443 e NIS2 e applicato retrospettivamente alla catena dell’attacco alla rete elettrica ucraina del 2015.*

Nella [quinta parte della serie](https://www.ictsecuritymagazine.com/articoli/zero-trust-sottostazioni-elettriche-novagrid/) il framework è stato applicato allo scenario delle sottostazioni NovaGrid. Questa sesta parte lo mette alla prova in tre modi.

Prima confronta le sei fasi con NIST SP 800-82r3, ISA/IEC 62443 e articolo 24 del d.lgs. 138/2024. Poi affianca MATRIX ai metodi di Cloud Security Alliance e Software Engineering Institute. Infine rilegge, passaggio per passaggio, l’attacco del 23 dicembre 2015 alle società di distribuzione elettrica ucraine.

## MATRIX e standard OT: NIST, IEC 62443 e NIS2

Il primo criterio di adeguatezza di un framework di selezione dei controlli è la sua completezza: le sei fasi devono generare, nel loro insieme, gli artefatti e le attività che gli standard di settore prescrivono, senza lasciare scoperti requisiti essenziali.

La Tabella 3 mappa ciascuna fase di MATRIX sui corrispondenti requisiti della NIST SP 800-82r3,[[1]](#_ftn1) della serie ISA/IEC 62443[[2]](#_ftn2) e dell’articolo 24 del decreto di recepimento della NIS2.[[3]](#_ftn3) La mappatura mostra che le fasi del framework coprono l’intero ciclo prescritto dalle tre fonti, dalla identificazione del contesto e degli asset fino al monitoraggio continuo e alla gestione del rischio residuo.

L’esercizio non rivela lacune di copertura. La specificità di MATRIX rispetto alle tre fonti non risiede dunque nell’aggiunta di requisiti nuovi, ma nel meccanismo, assente negli standard, che vincola la selezione di ciascun controllo all’idoneità tecnica dell’asset e alla criticità di missione, rendendo esplicita la logica di allocazione differenziata.

*Tabella 3. Mappatura di copertura delle fasi di MATRIX sui requisiti degli standard di riferimento.*

| **Fase MATRIX** | **NIST SP 800-82r3** | **ISA/IEC 62443** | **Art. 24 D.Lgs. 138/2024** |
| --- | --- | --- | --- |
| M, contesto di missione e DAAS | Identificazione di sistema e impatto; categorizzazione | Definizione del system under consideration e delle zone | Analisi del rischio orientata all’impatto |
| A, idoneità degli asset | Inventario e caratterizzazione degli asset OT | Assegnazione dei security level target per zona | Gestione e proporzionalità delle misure |
| T, superficie d’attacco | Analisi di minacce e vulnerabilità | Identificazione di threat e conduit esposti | Gestione delle vulnerabilità e della supply chain |
| R, rischio e compromessi | Valutazione e trattamento del rischio | Riconciliazione tra security level target e raggiunto | Selezione di misure adeguate e proporzionate |
| I, matrice di allocazione | Selezione e implementazione delle contromisure | Realizzazione dei requisiti di sicurezza per zona | Controllo accessi, MFA, crittografia, segmentazione |
| X, esecuzione ed evoluzione | Monitoraggio, manutenzione e miglioramento continuo | Gestione del ciclo di vita della sicurezza | Continuità operativa, gestione e notifica incidenti |

## MATRIX a confronto con CSA e Software Engineering Institute

La seconda componente confronta MATRIX con i due schemi metodologici a esso più prossimi: il processo in cinque fasi della Cloud Security Alliance per le infrastrutture critiche[[4]](#_ftn4) e l’approccio del Software Engineering Institute alla mappatura dei principi zero trust su ambienti a vincoli stringenti.[[5]](#_ftn5) Il confronto è condotto rispetto a cinque criteri rilevanti per l’adozione in ambito OT, sintetizzati nella Tabella 4.

Il confronto evidenzia che MATRIX eredita dal SEI la centralità dei compromessi e l’idea di profilazione dell’idoneità, ma le traduce in un artefatto operativo, la matrice di allocazione, che né il processo CSA né il lavoro SEI rendono esplicito. Il valore distintivo si concentra quindi nella capacità di produrre, asset per asset e capability per capability, una traccia decisionale comunicabile e verificabile.

*Tabella 4. Confronto strutturato tra MATRIX e gli schemi metodologici esistenti.*

| **Criterio** | **CSA cinque fasi** | **SEI principi e tradeoff** | **MATRIX** |
| --- | --- | --- | --- |
| Orientamento alla missione | Implicito | Parziale | Esplicito, fase M |
| Profilazione dell’idoneità degli asset | Assente | Presente, set di attributi | Presente e integrata nella selezione |
| Analisi esplicita dei compromessi | Limitata | Centrale | Centrale, fase R |
| Allocazione differenziata dei controlli | Assente | Concettuale | Operativa, matrice di allocazione |
| Tracciabilità documentale per la conformità | Bassa | Media | Alta, artefatto ...
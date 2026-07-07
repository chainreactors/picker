---
title: VEX: separare le vulnerabilità che contano dal rumore della SBOM
url: https://www.ictsecuritymagazine.com/cyber-security/vex-vulnerability-exploitability-exchange/
source: ICT Security Magazine
date: 2026-07-06
fetch_date: 2026-07-07T06:05:04.776233
---

# VEX: separare le vulnerabilità che contano dal rumore della SBOM

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

![Vulnerability Exploitability eXchange (VEX)](https://www.ictsecuritymagazine.com/wp-content/uploads/Vulnerability-Exploitability-eXchange-VEX-.png)

# VEX: separare le vulnerabilità che contano dal rumore della SBOM

A cura di:[Redazione](#molongui-disabled-link)  Ore 6 Luglio 20269 Giugno 2026

VEX, sigla di Vulnerability Exploitability eXchange, è la risposta a un problema che la distinta dei componenti di un software crea proprio mentre ne risolve un altro. La SBOM ha reso possibile sapere cosa c’è dentro un’applicazione, e da quell’elenco di componenti uno strumento automatico ricava subito tutte le vulnerabilità note che li riguardano, spesso centinaia, a volte migliaia. È un risultato prezioso, ma con un effetto collaterale pesante: la grande maggioranza di quelle vulnerabilità non riguarda davvero il prodotto, e il diluvio di allarmi finisce per seppellire i pochi che contano. VEX serve a separare i due insiemi, dicendo, per ciascuna vulnerabilità, se il prodotto ne è effettivamente esposto.

Il malinteso da sciogliere è il cuore della questione. Che una vulnerabilità sia presente in un componente non significa che sia sfruttabile nel prodotto che lo usa. Il codice difettoso potrebbe non essere mai eseguito, la funzione vulnerabile potrebbe non essere raggiungibile, un controllo a monte potrebbe già neutralizzare il problema. Senza un modo per distinguere la presenza dalla sfruttabilità, la SBOM si trasforma da strumento di trasparenza in generatore di rumore, e i team o annegano nei falsi positivi o smettono del tutto di leggere quegli elenchi. VEX nasce per evitare entrambi gli esiti.

## Il problema che la SBOM crea risolvendone un altro

Conviene vedere bene il meccanismo che produce il diluvio. Una distinta dei componenti elenca le librerie e i moduli che compongono un software; uno scanner incrocia quell’elenco con i database delle vulnerabilità note e restituisce ogni difetto associato a ciascun componente. È un abbinamento meccanico, che non sa nulla di come quel componente è usato nel prodotto: segnala tutto ciò che, in teoria, potrebbe riguardarlo. Per un’applicazione reale, fatta di decine o centinaia di dipendenze, il risultato è una lista lunghissima.

Il guaio è che quella lista mescola, senza distinguerli, i pochi difetti realmente pericolosi e la massa di quelli che non hanno alcun effetto pratico in quel contesto. È lo stesso problema che affligge tante fonti di allarme in sicurezza: un rapporto segnale-rumore così basso da rendere il segnale invisibile. La gestione delle [vulnerabilità](https://www.ictsecuritymagazine.com/notizie/vulnerability-management/) diventa così un lavoro di smistamento a tappeto, in cui correggere ciò che non serve sottrae tempo a ciò che conta, e l’adozione stessa degli [SBOM](https://www.ictsecuritymagazine.com/articoli/software-bill-of-materials/) rischia di produrre più fatica che sicurezza.

## Esposto non vuol dire sfruttabile

La distinzione su cui poggia tutto è quella tra presenza ed esposizione. Una vulnerabilità presente in una libreria è un fatto verificabile incrociando la distinta con i database; la sua sfruttabilità nel prodotto è un’altra cosa, e dipende dal contesto. La domanda giusta non è se il componente difettoso sia incluso, ma se il codice vulnerabile sia effettivamente raggiungibile durante l’esecuzione, se un attaccante possa controllarne l’ingresso, se esista già una mitigazione che chiude la strada all’attacco.

A queste domande non può rispondere chi sta a valle e si limita a incrociare elenchi, perché non conosce le viscere del software. Può rispondere chi quel software lo conosce dal di dentro: il suo produttore in primo luogo, ma anche un integratore o un fornitore di sicurezza che ne analizzi la raggiungibilità del codice. È qui che VEX inserisce la propria logica: spostare il giudizio sulla sfruttabilità a chi è in grado di darlo, e renderlo comunicabile in modo che chi sta a valle possa usarlo per dare priorità invece di rincorrere ogni segnalazione.

## VEX dice lo stato, e perché

In concreto, VEX è una forma di avviso di sicurezza che dichiara, per ogni vulnerabilità e per un dato prodotto, uno tra quattro stati: non interessato, interessato, già corretto, oppure sotto indagine. Il valore più utile è il primo, perché è quello che spegne il rumore: dire che il prodotto non è interessato da una vulnerabilità presente in un suo componente è ciò che permette di cancellarla dalla lista delle cose di cui preoccuparsi. Proprio per questo non può essere un’affermazione gratuita, e le [giustificazioni dello stato](https://www.cisa.gov/resources-tools/resources/vulnerability-exploitability-exchange-vex-status-justification-document-june-2022) codificate dalla CISA impongono di motivarla con una tra cinque categorie: il componente vulnerabile non è incluso nel prodotto, oppure è incluso ma il codice difettoso non è presente perché escluso in fase di build o configurazione, oppure quel codice non si trova mai nel percorso di esecuzione, oppure non può essere controllato da un avversario, oppure è già in atto una mitigazione integrata che ne neutralizza lo sfruttamento. In alternativa alla giustificazione codificata, lo s...
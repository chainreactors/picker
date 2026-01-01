---
title: Punto di “sniffing”
url: https://roccosicilia.com/2025/12/31/punto-di-sniffing/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-31
fetch_date: 2026-01-01T03:36:36.707217
---

# Punto di “sniffing”

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [Punto di “sniffing”](https://roccosicilia.com/2025/12/31/punto-di-sniffing/)

Published by

Rocco Sicilia

on

[31 dicembre 2025](https://roccosicilia.com/2025/12/31/punto-di-sniffing/)

[![Punto di “sniffing”](https://roccosicilia.com/wp-content/uploads/2025/08/youtube-live.png?w=1024)](https://roccosicilia.com/2025/12/31/punto-di-sniffing/)

In questi giorni ho rimesso mano al mio home lab aggiungendo qualche pezzo ed in particolare mi sono dotato di una componente hardware che solitamente, per esigenze di spazio e comodità, utilizzavo nelle sue versioni software e decisamente più limitate: lo switch.

Purtroppo non ho la possibilità di installare un vero rack con le relative componenti (spazio limitato), ho quindi ripiegato su alcuni strumenti che potessero comunque assolvere ai rispettivi ruoli mantenendo le dimensione del lab fisicamente ridotte.

> I dettagli sulla configurazione di base sono disponibili in questo post su Patreon: “[Nuovo lab (infrastruttura di base)](https://www.patreon.com/posts/nuovo-lab-di-146519953)“.

L’esigenza di uno switch “vero”, anche se non è esattamente uno switch quello che ho adottato, si riferisce ad alcuni test che vorrei fare sulle possibilità di detection a livello rete. In diverse occasioni, durante le attività di PenTesting, mi auto-impongo dei limiti in relazione all’utilizzo di specifiche tecniche di discovery, scansione ed enumerazione dei sistemi in quanto gli strumenti di network detection potrebbero facilmente identificare alcune tipologie di traffico.

A livello empirico so che alcune utility sono più “silenziose” di altre ma non ho mai approcciato la cosa in modo scientifico, ovvero non mi sono mai messo a controllare – sniffare – il traffico di ogni singola utility per vedere il dettaglio del traffico che genera e che tipo di detection rule fa scattare. Quello che spesso ho fatto è stato analizzare le funzionalità delle utilities e ricrearle in tools custom che utilizzo su campo. **È così che è nato il mio amore per scapy**.

Questa esigenza permane e con il tempo si estende a sempre più funzionalità presenti in diversi strumenti. Ricrearle tutte in una versione custom sarebbe estremamente inefficiente, ho quindi pensato di riprendere il task e strutturarlo meglio: tramite il mio home lab andrò ad analizzare il traffico dei tools che utilizzo più frequentemente e lo sottoporrò alle più frequenti detection rules. L’obiettivo è trovare dei setup che non facciano scattare allarmi e, laddove non possibile, trovare delle alternativa valide che mi consentano di rimanere silenzioso in rete.

Per sniffare tutto il traffico comodamente e senza rischiare di perdere pezzi ho pensato che dotare il lab di uno switch fosse la scelta migliore ed in effetti avendo la possibilità estrarre un dump completo di tutto quello che è connesso al device (tutto il lab) la scelta risulta la più logica.

*Video demo*

Nota importante — VirtualBox, come molti software di virtualizzazione, utilizza dei virtual-switch per fornire una rete virtuale alle VMs. Condividendo il virtual-switch o una NIC (ad esempio in configurazione di bridge) il traffico L2 “intra VMs” verrà gestito direttamente dall’host. Questo significa che sullo switch HW sarà possibile intercettare il traffico tra un host fisico ed una guest ma non tra due guest attive sullo stesso host.

Possiamo fare un semplice test per verificare sia la possibilità di intercettare il traffico tra un host fisico ed una guest, sia per accertarci dell’impossibilità di vedere il traffico tra due guest nella stessa rete posizionandoci sullo switch fisico.

![](https://roccosicilia.com/wp-content/uploads/2025/12/image-1.png?w=1024)

*Dettaglio del lab*

Questo dettaglio è importante da comprendere in un contesto di Network Detection: le la sonda IDS opera “solo” sulla base del mirroring del traffico di uno switch fisico (il CORE switch ad esempio) potremmo trovarci nelle condizioni di trascurare importanti porzioni di traffico.

Nel test ho eseguito una cattura del traffico dal sistema RouterBoard ed in particolare è stato raccolto, per qualche secondo, il traffico del bridge denominato “bridge-lan” che sostanzialmente rappresenta lo switch a cui sono fisicamente cablati il mio laptop e l’host su cui gira VirtualBox (lo schema sopra è abbastanza fedele).

Le NIC in LAN delle due VMs sono in configurazione di bridge con la NIC fisica dell’host connessa direttamente al RouterBoard, questo mi consente di ottenere la comunicazione L2 tra tutti i sistemi ma, come detto, il traffico tra le due guest non transita dal mondo fisico e non può quindi essere raccolto dal RouterBoard.

![](https://roccosicilia.com/wp-content/uploads/2025/12/image.png?w=831)

*Estrazione del pcap da MikroTik*

Analizzando il pcap è infatto possibile vedere il traffico RDP tra il mio laptop e l’host su cui gira VirtualBox ma non c’è traccia del traffico che stavo generando tra le due VMs (ICMP e HTTP).

![](https://roccosicilia.com/wp-content/uploads/2025/12/image-2.png?w=1024)

*Porzione del traffico intercettato*

Ovviamente resta possibile raccogliere ed analizzare il traffico che resta configurato all’interno del virtual switch: è sufficiente inserire nella virtual-network una macchina con una vNIC in modalità promiscua da utilizzare come sonda passiva.

---

Se i miei articoli ti interessano iscriviti al canale [YouTube](https://youtube.com/%40roccosicilia) e [Patreon](https://patreon.com/roccosicilia) per supportarmi, iscriviti al blog per rimanere sempre aggiornato:

Digita la tua e-mail…

Iscriviti

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2025/12/31/punto-di-sniffing/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2025/12/31/punto-di-sniffing/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2025/12/31/punto-di-sniffing/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2025/12/31/punto-di-sniffing/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: Dove avete messo il vostro codice?](https://roccosicilia.com/2025/12/01/dove-avete-messo-il-vostro-codice/)

Ciao,

### sono Rocco

![](https://sheliakblog.wordpress.com/wp-content/uploads/2025/04/photo.jpeg?w=389)

… e questo è mio sito personale dove condivido idee, riflessioni ed esperienze su hacking e sicurezza informatica.

### Let’s connect

* [Patreon](https://patreon.com/roccosicilia)

* [YouTube](https://youtube.com/%40roccosicilia)

* [LinkedIn](https://www.linkedin.com/in/roccosicilia/)

### Rimani aggiornato!

Iscriviti per ricevere gli update dei nuovi post e video.

Digita la tua e-mail…

→

### Recent posts

* [![Punto di “sniffing”](https://roccosicilia.com/wp-content/uploads/2025/08/youtube-live.png?w=1024)](https://roccosicilia.com/2025/12/31/punto-di-sniffing/)

  ## [Punto di “sniffing”](https://roccosicilia.com/2025/12/31/punto-di-sniffing/)
* ## [Dove avete messo il vostro codice?](https://roccosicilia.com/2025/12/01/dove-avete-messo-il-vostro-codice/)
* ## [API ed info-sec](https://roccosicilia.com/2025/11/30/api-ed-info-sec/)
* [![Info Sec Unplug...
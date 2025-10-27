---
title: OT security bias (1): “non espongo servizi, quindi non mi riguarda”.
url: https://roccosicilia.com/2025/04/14/ot-security-bias-1-non-espongo-servizi-quindi-non-mi-riguarda/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-15
fetch_date: 2025-10-06T22:08:15.185954
---

# OT security bias (1): “non espongo servizi, quindi non mi riguarda”.

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/)

## [OT security bias (1): “non espongo servizi, quindi non mi riguarda”.](https://roccosicilia.com/2025/04/14/ot-security-bias-1-non-espongo-servizi-quindi-non-mi-riguarda/)

Published by

Rocco Sicilia

on

[14 aprile 2025](https://roccosicilia.com/2025/04/14/ot-security-bias-1-non-espongo-servizi-quindi-non-mi-riguarda/)

[![OT security bias (1): “non espongo servizi, quindi non mi riguarda”.](https://roccosicilia.com/wp-content/uploads/2024/08/homelab.png?w=545)](https://roccosicilia.com/2025/04/14/ot-security-bias-1-non-espongo-servizi-quindi-non-mi-riguarda/)

Quest’anno, assieme ad [Andrea](https://www.adainese.it/), abbiamo scelto di fare un piccolo focus sul mondo OT Security portando l’argomento in diversi tavoli di confronto, compreso il nostro [Podcast](https://www.youtube.com/%40roccosicilia/podcasts) e workshop che abbiamo strutturato assieme ai [colleghi](https://www.linkedin.com/company/nts-italy-gmbh-srl/posts/?feedView=all).

In questa miniserie porto alcuni temi discussi più volte ed in diversi anni di attività sul campo. Ne ho/abbiamo scelti quattro e probabilmente li riprenderemo, almeno in parte, nel Podcast.

### La base

Parto da una delle obiezioni che anni fa abbiamo tutti dovuto affrontare anche in ambito IT, ovvero la credenza che la sicurezza sia legata al solo fatto di esporre o meno servizi verso “l’esterno”. È una questione di comprensione del problema: si sta dando per scontato che esista un solo tipo di vettore di attacco: l’exploiting di un servizio che presenta una vulnerabilità sfruttabile. Ma questa possibilità, per quanto sia effettivamente da considerare, non è l’unica da considerare.

---

Se trovi utili i miei post ed i miei video di approfondimento puoi restare aggiornato iscrivendoti al blog con la tua email:

Digita la tua e-mail…

Iscriviti

Se vuoi sostenere il mio progetto di divulgazione trovi qui i dettagli: <https://roccosicilia.com/sostieni-il-progetto/>

---

Per prima cosa dobbiamo metterci d’accordo su cosa significhi esporre un servizio: il fatto che l’utilizzatore del sistema non abbia, in prima persona, installato e configurato un servizio non significa che il sistema non ne abbia in generale. La precisazione è banale ma è doverosa: negli anni mi è capitato di dover precisare che la *porta* *tcp 3389* alla quale i colleghi della manutenzione si collegano via Remote Desktop espone a tutti gli effetti un servizio, così come la *porta tcp 22* usata via SSH. A livello di sicurezza una falla su questi servizi potrebbe esporre il sistema a diverse tecniche di attacco.

In generale anche esporre un servizio alle sole reti interne può generare dei rischi in caso di presenza di vulnerabilità gravi: esistono malware che sfruttano proprio la presenza di host vulnerabili all’interno della rete per diffondersi. Ora, nel mondo OT la presenza di host con sistemi operativi obsoleti non è una cosa strana e molti team devono imparare a conviverci. Questo non significa far finta che non ci siano sistemi vulnerabili, al contrario vanno introdotte delle misure per ridurre il rischio. Possiamo valutare se il servizio sia veramente necessario ed in caso contrario potremmo rimuoverlo, potremmo ridurre il livello di visibilità e accesso, potremmo utilizzare soluzioni IDS/IPS per garantire un accesso protetto. Le opzioni non mancano.

### Protocolli insicuri

Alcuni protocolli OT, come Modbus o DNP3, non sono mai stati progettati pensando alla sicurezza informatica. Nati in un’epoca in cui le reti erano isolate (air-gapped), questi protocolli non prevedono né autenticazione né cifratura, e quindi sono estremamente esposti ad attacchi di tipo Man-In-The-Middle (MITM).

In pratica, è sufficiente che un attaccante riesca a posizionarsi tra un master (es. SCADA) e uno slave (es. PLC) per intercettare, manipolare o addirittura iniettare comandi falsi nel traffico di rete. Questo può essere fatto con tecniche banali come l’ARP spoofing, utilizzando strumenti liberamente disponibili come Bettercap o Ettercap, e consente all’attaccante di alterare i dati letti/scritti dal PLC in tempo reale — ad esempio modificando i valori di temperatura o pressione visualizzati sull’HMI.

Questa vulnerabilità non è puramente teorica: capita con una certa frequenza che dispositivi compromessi vengano introdotti inconsapevolmente all’interno della rete OT. Un caso comune riguarda gli interventi di manutenzione onsite da parte di fornitori esterni, che connettono i propri laptop — magari mai aggiornati o esposti in precedenza a reti insicure — alla rete degli impianti. Se quel laptop fosse infetto, o se fosse sfruttato come ponte, l’attaccante potrebbe lanciare un attacco MITM sulla rete Modbus con pochissima resistenza.

Un caso interessante su quello di [***VPNFilter***](https://it.wikipedia.org/wiki/VPNFilter), un malware multi-stage pensato per infettare router e NAS che nelle fasi avanzate utilizzava specifiche plugin tra cui una componente in grado di intercettare traffico di dispositivi industriali.

### Periferiche e porte I/O

Per esigenze operative, le postazioni in ambito OT consentono frequentemente l’utilizzo di dispositivi esterni come chiavette USB, hard disk portatili o strumenti di diagnostica. Questi supporti, se non adeguatamente controllati, rappresentano un vettore di infezione estremamente efficace per i threat actor, soprattutto in ambienti in cui non sono attivi sistemi anti-malware e policy di controllo dei dispositivi rimovibili, dove spesso le postazioni di lavoro devono restare “unlocked”.

Riporto un caso reale che mi è capitato di studiare: durante un assessment di sicurezza, vengono rilevati segnali di infezione da Conficker, un malware che sfrutta vulnerabilità note nei sistemi Windows e si propaga anche tramite supporti USB. Quattro workstation in un segmento di rete OT risultavano infette. Si procede inizialmente con una bonifica manuale, ma nel giro di pochi giorni le infezioni ricompaiono. Dopo ulteriori indagini, emerge la causa: una chiavetta USB infetta utilizzata regolarmente da un manutentore esterno durante le operazioni onsite. Ogni volta che il dispositivo veniva inserito in una postazione, il malware riprendeva a diffondersi silenziosamente nella rete.

Questo caso sottolinea un bias frequente: pensare che il perimetro fisico basti a proteggere la rete OT, quando in realtà è sufficiente un gesto quotidiano – come inserire una chiavetta – per compromettere l’intero ambiente operativo.

### Accesso Remoto

L’accesso remoto agli impianti OT è ormai una necessità operativa irrinunciabile. Le aziende devono garantire supporto tecnico, manutenzione, aggiornamenti e troubleshooting anche a distanza, spesso su impianti distribuiti geograficamente o con risorse limitate in loco. Tuttavia, questa esigenza viene ancora oggi soddisfatta in modo insicuro, spesso con soluzioni improvvisate o fuori dal controllo della funzione IT.

In molti contesti OT, l’accesso remoto avviene tramite strumenti non gestiti, come software di remote desktop installati ad hoc su singole macchine (es. TeamViewer, AnyDesk, UltraVNC), configurati senza criteri di sicurezza condivisi, log, MFA o segmentazione. Questi strumenti vengono spesso lasciati attivi in background, con credenziali statiche o addirittura senza password, esponendo direttamente l’interfaccia delle macchine industriali a Internet o a reti insicure.

Un’altra prassi comune, ancora più critica, è l’utilizzo di router o gateway di rete di terze parti, installati direttamente ...
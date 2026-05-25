---
title: Threat Hunting and Defending #1 (study)
url: https://roccosicilia.com/2026/05/24/threat-hunting-and-defending-1-study/
source: Over Security
date: 2026-05-24
fetch_date: 2026-05-25T06:22:58.140137
---

# Threat Hunting and Defending #1 (study)

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/divulgazione/)
* [Progetti](https://roccosicilia.com/progetti/)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/), [study with me](https://roccosicilia.com/category/study-with-me/)

## [Threat Hunting and Defending #1 (study)](https://roccosicilia.com/2026/05/24/threat-hunting-and-defending-1-study/)

Published by

Rocco Sicilia

on

[24 Maggio 2026](https://roccosicilia.com/2026/05/24/threat-hunting-and-defending-1-study/)

[![Threat Hunting and Defending #1 (study)](https://roccosicilia.com/wp-content/uploads/2026/05/gemini-threat-hunting.png)](https://roccosicilia.com/2026/05/24/threat-hunting-and-defending-1-study/)

### Premessa

Ricomincio a studiare per una nuova certificazione Cyber Security e quest’anno ho scelto “*Conducting Threat Hunting and Defending using Cisco Technologies for Cybersecurity*“. Giustamente molti, già lo scorso anno, mi avevano scritto incuriositi da quella che poteva sembrare una deriva Defense (non che ci sia nulla di male), considerando che di “mestiere” io mi occupo della parte offensiva della sicurezza informatica. In realtà la risposta è molto semplice: il mondo dei SOC e dei servizi MDR si sta evolvendo molto (e molto ancora si deve evolvere) e buona parte dei miei task operativi è finalizzata alla verifica della capacità di detection di sistemi e Blue Team. Comprenderne a fondo metodologie e strumenti (il mio target attuale) è parte integrante, per come la vedo io, del mio percorso di crescita.

Alle dovute premesse aggiungo che vorrei condividervi i miei appunti di studio e come sempre utilizzerò i canali che ho a disposizione, in particolare questo Blog e [YouTube](https://youtube.com/%40roccosicilia).

Se trovi utili i contenuti che condiviso e vuoi restare aggiornato puoi sostenere il mio progetto di divulgazione [iscrivendoti al mio Substack](https://roccosicilia.substack.com/subscribe). Per gli abbonati metto a disposizione articoli e video di approfondimento.

### Threat Hunting: la teoria

Come disciplina, il threat hunting, si applica soprattutto alle strutture di difesa come i Security Operations Center (SOC). Da questo tipo di struttura solitamente ci aspettiamo che siano in grado di rilevare, contenere e rimediare ad eventuali attacchi informatici contro la nostra struttura.

É giusto fare una precisazione – non presente nel corso – sui compiti dei SOC: sicuramente in Italia ma anche in molti paesi europei ho notato la tendenza a limitare la copertura del SOC ai compiti di detection e prima risposta di contenimento e tutto il resto sta al team del cliente. Questo modo di concepire il SOC personalmente non l’ho mai visto positivamente, ma a prescindere dal mio parere oggi è sicuramente limitato e poco efficace rispetto a strutture che garantiscono una gestione completa dell’incident fino ad arrivare, se le condizioni lo prevedono, all’attivazione di un team specialistico per operazioni complesse di responce (IT team). Nel corso in oggetto quando si parla di SOC si fa riferimento ad un servizio completo.

È evidente che un approccio come quello che ho riportato ha il limite della reattività: succede qualcosa, scatta un allarme, qualcuno analizza e decide se intervenire. Lineare ma già da qualche è chiaro che attendere passivamente che un qualche strumento generi un allarme è insufficiente. Il Threat Hunting è una disciplina che piò restituire efficacia ed efficienza alla struttura di difesa rendendole “proattive”.

La tesi su cui si basa il Threat Hunting è che i sistemi e le automazioni di detection tendono ad una certa staticità ed è necessario condurre delle analisi anche in assenza di allarmi chiari. Inoltre, mi permetto di aggiungere rispetto al materiale del corso, andare a caccia di tecnico non note consente di arricchire le regole di detection dei sistemi.

### Il concept

Avendo recentemente parlato molto di “evasion” possono rimandare ad uno dei miei ultimi video per arricchire il concetto. Il modello di detection oggi in uso da molti SOC consente di intercettare la stragrande maggioranza dei threat (95% stima la documentazione Cisco). La domanda è quindi: cosa succede con il restante 5% dei threat in grado di aggirare la nostra capacità di detection?

Vi lascio uno dei video dove ho parlato di evasion:

Se il problema è andare a caccia di minacce che non siamo in grado di intercettare realtime una possibile soluzione è implementare un processo di “ricerca” di queste minacce nella base dati a nostra disposizione: stiamo quindi parlando di ***Threat Hunting***.

> Threat hunting is the security practice of looking for threats that evaded the security controls and are hiding within the environment.

Un documento interessante da leggersi è [TTP-Based Hunting](https://www.mitre.org/sites/default/files/2021-11/prs-19-3892-ttp-based-hunting.pdf) di MITRE che in un prossimo post vedrò di riassumere.

Un problema molto serio a cui i SOC devono far fronte è l’aumento dei tentativi di attacco combinato con una crescente complessità delle tecnologie in campo: il numero di segnalazioni ed allarmi aumenta come la quantità di falsi positivi da gestire. Inevitabilmente gli analisti rischiano di essere distratti da molti allarmi e talvolta di abbassa la “sensibilità” dei sistemi di detection per ridurre il numero di falsi positivi, ma così facendo si aumenta il rischio di non intercettare comportamenti malevoli.

Il threat hunting può aiutare il Blue Team ad intercettare azioni offensive, che non sono state viste dai sistemi di detection, prima che l’attaccante giunga all’obiettivo dell’operazione. Inoltre le attività di threat hunting (come anche l’output delle azioni di Red Teaming) possono aiutare il Blue Team ad individuare nuove politiche e regole di detection grazie all’individuazione di GAP o nuove minacce che non hanno generato segnalazioni.

Le principali aree in cui il threat hunter opera sono relative alle informazioni che possono essere raccolte dagli Endpoint e dalla rete. Uno degli strumenti che oggi non manca praticamente mai all’interno delle infrastrutture enterprise sono gli EDR, ottimo punto di partenza. È comunque utile e suggerito andare più a fondo tramite tools di analisi forense e strumenti di analisi specifici in base a quello che stiamo cercando ed il tipo di sistemi su cui stiamo operando. Anche in relazione alla verifica del traffico possono essere usati diversi strumenti, dagli immancabili firewall log (se il design della rete lo consente) alla cattura del traffico.

Centralizzare le informazioni che ci arrivano dagli EDR e dalla rete grazie alle sonde e le appliance (es: IDS o sistemi Firewall) non è facile e molti vendor implementano il concetto di XDR per mettere a disposizione uno strumento che consenta la massima visibilità e la massima capacità di risposta.

Anche Cisco ha una sua piattaforma [XDR](https://www.cisco.com/site/us/en/products/security/xdr/index.html) che differisce a livello di struttura rispetto a come molti altri vendor hanno implementato il concetto. Non voglio in questa sede fare paragoni, non è lo scopo dei miei studi ne di questi post, va messa in evidenza una sostanziale differenza sull’interpretazione del concetto: Cisco ha preferito creare una piattaforma di aggregazione di sistemi terze parti compresi altri EDR, Firewall, logs, ecc.
Questa configurazione non è impossibile con altri vendor ma va considerato che solitamente gli XDR di mercato estendono le capacità della piattaforma EDR accettando ed integrando diverse fonti.
Si tratta di una differenza di Design che fa valutata prima dell’implementazione di questo tipo di soluzioni.

Il Threat Hunter deve quindi poter accedere a strumenti che gli consentano di analizzare il dettaglio di ciò che sta avvenendo s...
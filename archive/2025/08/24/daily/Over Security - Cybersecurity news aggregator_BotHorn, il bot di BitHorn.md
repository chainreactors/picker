---
title: BotHorn, il bot di BitHorn
url: https://roccosicilia.com/2025/08/23/bothorn-il-bot-di-bithorn/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-24
fetch_date: 2025-10-07T00:17:42.806762
---

# BotHorn, il bot di BitHorn

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/), [update](https://roccosicilia.com/category/update/)

## [BotHorn, il bot di BitHorn](https://roccosicilia.com/2025/08/23/bothorn-il-bot-di-bithorn/)

Published by

Rocco Sicilia

on

[23 agosto 2025](https://roccosicilia.com/2025/08/23/bothorn-il-bot-di-bithorn/)

[![BotHorn, il bot di BitHorn](https://roccosicilia.com/wp-content/uploads/2025/08/screenshot-2025-08-23-at-09.08.00.png?w=1024)](https://roccosicilia.com/2025/08/23/bothorn-il-bot-di-bithorn/)

Visto che ho dedicato uno spazio del mio venerdì sera, compreso il secondo pezzo della live, al bot che ho introdotto e che vorrei espandere, ho pensato di scrivere due note sul funzionamento e sui possibili sviluppi.

#### Obiettivi base

Come [spiego nella live](https://youtube.com/live/0V73TF9yScg) l’idea nasce dall’esigenza di mantenere un certo livello di integrazione tra subreddit e gruppo Telegram e la prima proposta che è stata avanzata è stata quella di inviare un messaggio su Telegram che notifichi nuove discussioni. Ho fatto una variazione sul tema ed ho preparato uno script che va ad estrarre le discussioni presenti nel subreddit individuando quelle aperte nella giornata in corso, di queste viene fatto un summary ed inviato al gruppo.

![](https://roccosicilia.com/wp-content/uploads/2025/08/image-12.png?w=870)

Summary del 22 agosto

A questa funzione se ne possono aggiungere altre ed alcune le ho ipotizzate nel readme file del progetto, che ovviamente è rilasciato open source qui: <https://github.com/b1th0rn/BotHorn>.

#### Struttura dello script

La cosa divertente di questi micro-progetti è che in poco si impara sempre qualcosa di nuovo. Ad esempio in questa occasione ho appreso che Reddit consente agli utenti di accedere ad alcune API senza particolari automazioni. Ad esempio che sul browser eseguite la richiesta <https://www.reddit.com/r/BitHorn/new.json?limit=10> otterrete l’export in JSON degli ultimi 10 topic del subreddit.

Sono partito da questo livello di accesso per fare il prototipo che però ha smesso di funzionare quando ho spostato lo script sul server dove avrebbe poi dovuto girare. Analizzando meglio prima il codice di errore (reddit non rispondeva più e mi restituiva un sonoro 403) e poi la documentazione, ho appreso che l’accesso alle informazioni è negato senza autenticazione se la richiesta arriva da una rete provider che evidentemente reddit censisce.

Questo è il motivo per il quale ho, infine, utilizzato Oauth:

```
def get_reddit_token():
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    data = {
        'grant_type': 'client_credentials'
    }
    headers = {'User-Agent': 'BitHornBot/0.2'}
    response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        print(f"Error Reddit OAuth: {response.status_code}")
        print(response.text)
        return None
```

Mentre scrivo mi sono accorto che ho lasciato nel codice le mie bruttissime *print* per avere l’output di cosa stava succedendo, poi le tolgo ![:-/](https://s1.wp.com/wp-content/mu-plugins/wpcom-smileys/uneasy.svg)
Ad ogni modo a noi interessa il fatto che, una volta passati a reddit CLIENT\_ID e CLIENT\_SECRET il sistema ci ritorni il token di autenticazione. Con quello possiamo tornare a chiedere le informazioni che ci servono.

#### Hosting

Mentre cercavo info sul funzionamento della API di Telegram ho notato che molti utilizzato la piattaforma PythonAnywhere per i propri script. Ho quindi deciso di provarla per l’occasione.

Effettivamente il servizio è molto comodo e consente di istanziare script ed applicazioni in Python. Ho quindi configurato un semplice task (che non credo usi crontab) che esegue lo script tutte le sere alle 23:55. Il risultato è che tutte le sere sul gruppo Telegram arriva il messaggio con la lista dei nuovi post, ovviamente se ne esistono.

#### Note di chiusura

Come dicevo il bot è stato creato su una esigenza specifica ma ho intenzione di aggiungere alcune funzionalità e può facilmente essere riadattato. Il codice resta disponibile e se qualcuno vuole prendere spunto o proporre variazioni è liberissimo di farlo.

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2025/08/23/bothorn-il-bot-di-bithorn/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2025/08/23/bothorn-il-bot-di-bithorn/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2025/08/23/bothorn-il-bot-di-bithorn/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2025/08/23/bothorn-il-bot-di-bithorn/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: r/BitHorn su reddit](https://roccosicilia.com/2025/08/21/r-bithorn-su-reddit/)

[Successivo: MISP how-to: intro](https://roccosicilia.com/2025/08/25/misp-how-to-intro/)→

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

* [![Info Sec Unplugged [1b] – DR e Cyber recovery (parte 2)](https://roccosicilia.com/wp-content/uploads/2025/01/vlog.png?w=600)](https://roccosicilia.com/2025/10/04/info-sec-unplugged-1b-dr-e-cyber-recovery-parte-2/)

  ## [Info Sec Unplugged [1b] – DR e Cyber recovery (parte 2)](https://roccosicilia.com/2025/10/04/info-sec-unplugged-1b-dr-e-cyber-recovery-parte-2/)
* [![Info Sec Unplugged [1a] – DR e Cyber recovery (parte 1)](https://roccosicilia.com/wp-content/uploads/2024/12/podcast.png?w=541)](https://roccosicilia.com/2025/09/22/info-sec-unplugged-1a-dr-e-cyber-recovery-parte-1/)

  ## [Info Sec Unplugged [1a] – DR e Cyber recovery (parte 1)](https://roccosicilia.com/2025/09/22/info-sec-unplugged-1a-dr-e-cyber-recovery-parte-1/)
* [![Live del 05.09.2025: http_c2](https://roccosicilia.com/wp-content/uploads/2025/08/youtube-live.png?w=1024)](https://roccosicilia.com/2025/09/09/live-del-05-09-2025-http_c2/)

  ## [Live del 05.09.2025: http\_c2](https://roccosicilia.com/2025/09/09/live-del-05-09-2025-http_c2/)
* [![Info Sec Unplugged [19] – Threat Int. (3a parte)](https://roccosicilia.com/wp-content/uploads/2024/12/podcast.png?w=541)](https://roccosicilia.com/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/)

  ## [Info Sec Unplugged [19] – Threat Int. (3a parte)](https://roccosicilia.com/2025/09/08/info-sec-unplugged-18-threat-int-3a-parte/)
* [![Assume Breach: evoluzione di uno scenario](https://roccosicilia.com/wp-content/uploads/2025/01/coding.png?w=562)](https://roccosicilia.com/2025/09/05/assume-breach-evoluzione-di-uno-scenario/)

  ## [Assume Breach: evoluzione di uno scenario](https://roccosicilia.com/2025/09/05/assume-breach-evoluzione-di-uno-scenario/)
* [![100 video](https://roccosicilia.com/wp-content/upl...
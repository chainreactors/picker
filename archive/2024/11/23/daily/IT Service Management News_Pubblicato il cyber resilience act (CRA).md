---
title: Pubblicato il cyber resilience act (CRA)
url: http://blog.cesaregallotti.it/2024/11/pubblicato-il-cyber-resilience-act-cra.html
source: IT Service Management News
date: 2024-11-23
fetch_date: 2025-10-06T19:20:29.365909
---

# Pubblicato il cyber resilience act (CRA)

# [IT Service Management News](http://blog.cesaregallotti.it/)

Sicurezza delle informazioni, IT service management e qualità da Cesare Gallotti

## venerdì 22 novembre 2024

### Pubblicato il cyber resilience act (CRA)

Pubblicato il Regolamento UE 2024/2847, detto cyber resilience act (CRA): <https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32024R2847>. Ringrazio Chiara Ponti degli Idraulici della privacy per la segnalazione.

In merito avevo letto un breve articolo (la seconda parte): <https://www.altalex.com/documents/news/2024/10/28/sistema-ai-provoca-danno-scatta-risarcimento-utente-danneggiato>.

In sostanza, il Regolamento mira a garantire "che i prodotti con componenti digitali, ad esempio i prodotti dell'internet delle cose, siano resi sicuri lungo l'intera catena di approvvigionamento e per tutto il ciclo di vita".

Nei considerando, il Regolamento specifica che altre normative, come il Cyber security act e la NIS2, "non contemplano direttamente requisiti obbligatori per la sicurezza dei prodotti con elementi digitali".

Innanzi tutto, segnalo che "Il presente regolamento si applica dall’11 dicembre 2027". L'obbligo di segnalare incidenti che hanno sfruttato vulnerabilità dei propri prodotti scatta invece l'11 giugno 2026.

Di seguito i miei appunti di lettura. Vi prego di segnalarmi errori, dimenticanze, imprecisioni e, in breve, qualsiasi possibile miglioramento.

Distingue tra prodotti con elementi digitali "normali", importanti e critici.

Per i prodotti normali:

* sono descritti nell'articolo 6;
* vanno applicate le misure "minime" dell'Allegato 1 e il processo di gestione delle vulnerabilità, sempre in allegato 1.

Per i prodotti importanti:

* Sono descritti all'art. 7 e nell'Allegato III; in sintesi si tratta di prodotti di sicurezza informatica e prodotti i cui malfunzionamenti e compromissioni possono avere impatti significativi su altri sistemi informatici o sulle persone.
* Entro l'11 dicembre 2025, la Commissione fornirà migliori indicazioni (descrizioni tecniche) delle categorie di tali prodotti.
* Vanno applicate le verifiche descritte nell'articolo 32; in particolare, se non sono seguite norme armonizzate (norme ETSI) o specifiche comuni della Commissione, va coinvolto un organismo di certificazione ("organismo notificato") per la verifica o del tipo o del sistema di gestione per la qualità (si tratta quindi di due opzioni distinte, a scelta del fabbricante). Per alcuni prodotti la verifica del tipo va accompagnata anche dalla verifica della produzione. In alternativa, si può usare il meccanismo di certificazione del prodotto.

Per i prodotti critici:

* Sono descritti all'art. 8 e nell'Allegato IV; mi pare che al momento siano molto pochi e alcuni siano già certificati secondo i Common Criteria (ISO/IEC 15408).
* Devono applicare le misure dell'Allegato 1 ed essere certificati con livello di affidabilità almeno "sostanziale", secondo quanto previsto dal Cybersecurity Act (regolamento UE 2019/881), sempre che esista uno schema di certificazione sia stato adottato; mi sembra che, quindi, si possa immaginare un obbligo di certificazione secondo la ISO/IEC 15408 (ossia lo schema EUCC, l'unico adottato secondo il Cybersecurity act per ora con la Implementing Regulation EU 2024/482) di tali prodotti e, sempre che non abbia capito male, con livello EAL anche 1 o 2.
* Nel caso in cui non sia disponibile lo schema di certificazione, va coinvolto un organismo di certificazione ("organismo notificato") per la verifica o del tipo e della produzione o del sistema di gestione per la qualità (si tratta quindi di due opzioni distinte, a scelta del fabbricante).

Ulteriori misure saranno dettagliate in norme armonizzate (probabilmente della ETSI) o in atti di esecuzione della Commissione (art. 27). Bisognerà monitorare con attenzione la pubblicazione di tali norme e atti.

In generale, i fabbricanti devono condurre valutazioni del rischio relativo alla cibersicurezza dei prodotti, identificare e applicare i controlli di sicurezza tecnici e di processo (incluse le attività di manutenzione, assistenza e gestione vulnerabilità). L'assistenza deve essere garantita per almeno 5 anni (art. 13).

Sono quindi fornite indicazioni ulteriori sulla documentazione tecnica (art. 13 e 31, Allegato VII), sul tracciamento dei prodotti (art. 13), sulle informazioni e istruzioni per gli utilizzatori (Allegato II), sui punti di contatto (art. 13), sul ritiro o richiao dei prodotti (art. 13), sul come redigere la dichiarazione di conformità UE (art. 28 e Allegato V), sulla marcatura CE (art. 29 e 30)

L'articolo 14, come in altre normative, richiede ai fabbricanti di notificare al CSIRT gli incidenti determinati dallo sfruttamento di vulnerabilità dei prodotti. L'articolo 15 prevede che fabbricanti e persone possano segnalare vulnerabilità al CSIRT (elemento sicuramente molto interessante).

Gli articoli 24 e 25 sono relativi ai software liberi e open source. C'è anche un richiamo per la certificazione di tali software all'articolo 32.

Ci sono riferimenti alle normative relative alla sicurezza generale dei prodotti (va applicato sia il CRA sia il Regolamento 2023/988), ai sistemi di IA ad alto rischio.

Relativamente alla certificazione (articoli 35-51), deve essere istituita l'autorità di notifica (in Italia sarà probabilmente Accredia, ma non deve esserlo necessariamente), che a sua volta deve approvare gli organismi di notifica (ancora una volta, penso che molti saranno gli organismi di certificazione già presenti sul mercato per la ISO 9001, la ISO/IEC 27001 eccetera).

Interessante osservare che (art. 32): "Si dovrebbe tener conto degli interessi e delle esigenze specifici delle microimprese e delle piccole e medie imprese, comprese le start-up, nel definire le tariffe per le procedure di valutazione della conformità e tali tariffe sono ridotte proporzionalmente agli interessi e alle esigenze specifici di tali imprese".

Il regolamento prevede quindi la possibilità per la Commissione di modificare alcuni punti tra quelli sopra riportati. E' quindi necessario attivare canali di aggiornamento, anche se al momento non ne vedo di affidabili (ENISA non prevede newsletter, ma aggiornamenti solo via social network, che, con tutti i problemi noti, andrebbero sconsigliati; sottoscrivere agli RSS è molto macchinoso, ma almeno ci sono).

Altro riferimento da tenere monitorato è il gruppo di cooperazione amministrativa (ADCO), ma al momento non mi sembra che abbia prodotto cose significative. Vedere la pagina: <https://single-market-economy.ec.europa.eu/single-market/goods/building-blocks/market-surveillance/organisation/adcos_en>.

L'articolo 33 prevede "misure di sostegno per le microimprese e le piccole e medie imprese", che includono attività di formazione e di comunicazione. Immagino ne possano beneficiare anche le grandi.

Gli articoli 52-60 trattano delle attività di vigilanza, non di mio interesse, così come gli articoli finali, con l'eccezione delle scadenze riportate all'inizio.

Pubblicato da

[Cesare Gallotti](https://www.blogger.com/profile/02941990619036529409 "author profile")

alle
[11:32:00](http://blog.cesaregallotti.it/2024/11/pubblicato-il-cyber-resilience-act-cra.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/3090080509035095684/5691192097511966117 "Post per email")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=3090080509035095684&postID=5691192097511966117&from=pencil "Modifica post")

[Invia tramite email](https://www.blogger.com/share-post.g?blogID=3090080509035095684&postID=5691192097511966117&target=email "Invia tramite email")[Postalo sul blog](https://www.blogger.com/share-post.g?blogID=3090080509035095684&postID=5691192097511966117&target=blog "Postalo sul blog")[Condividi su X](https://www.blogger.com/share-post.g?blogID=3090080509035095684&postID=5691192097511966117&target=twitter "Condividi ...
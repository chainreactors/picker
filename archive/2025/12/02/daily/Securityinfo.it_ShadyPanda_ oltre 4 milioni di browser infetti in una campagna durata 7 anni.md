---
title: ShadyPanda: oltre 4 milioni di browser infetti in una campagna durata 7 anni
url: https://www.securityinfo.it/2025/12/02/shadypanda-oltre-4-milioni-di-browser-infetti-in-una-campagna-durata-7-anni/?utm_source=rss&utm_medium=rss&utm_campaign=shadypanda-oltre-4-milioni-di-browser-infetti-in-una-campagna-durata-7-anni
source: Securityinfo.it
date: 2025-12-02
fetch_date: 2025-12-03T03:17:06.330458
---

# ShadyPanda: oltre 4 milioni di browser infetti in una campagna durata 7 anni

Aggiornamenti recenti Dicembre 2nd, 2025 5:36 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [ShadyPanda: oltre 4 milioni di browser infetti in una campagna durata 7 anni](https://www.securityinfo.it/2025/12/02/shadypanda-oltre-4-milioni-di-browser-infetti-in-una-campagna-durata-7-anni/)
* [Coupang conferma il data breach: esposti i dati di oltre 30 milioni di utenti](https://www.securityinfo.it/2025/12/01/coupang-conferma-il-data-breach-esposti-i-dati-di-oltre-30-milioni-di-utenti/)
* [CERT-AGID 22–28 novembre: boom di phishing PagoPA e nuovi malware via SMS](https://www.securityinfo.it/2025/12/01/cert-agid-22-28-novembre-boom-phishing-pagopa-malware-sms/)
* [Ecco il tool gratuito per verificare se un IP fa parte di un botnet](https://www.securityinfo.it/2025/11/28/ecco-il-tool-gratuito-per-verificare-se-un-ip-fa-parte-di-un-botnet/)
* [Gli LLM malevoli aiutano i piccoli cybercriminali, ma non sono (ancora) così pericolosi](https://www.securityinfo.it/2025/11/27/gli-llm-malevoli-aiutano-i-piccoli-cybercriminali-ma-non-sono-ancora-cosi-pericolosi/)

* [Home](https://www.securityinfo.it)
* [News](https://www.securityinfo.it/category/news/)
* [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/)
* [Opinioni](https://www.securityinfo.it/category/opinioni/)
* [Top Malware](https://www.securityinfo.it/top-malware-page/)
* [Minacce](https://www.securityinfo.it/category/minacce-2/)
* [Guide alla sicurezza](http://www.securityinfo.it/guide-alla-sicurezza/)
* [Podcast](https://www.securityinfo.it/podcast-page/)
* [Strumenti Utili](https://www.securityinfo.it/category/strumenti-utili/)

* Search for:

## ShadyPanda: oltre 4 milioni di browser infetti in una campagna durata 7 anni

Dic 02, 2025  [Marina Londei](https://www.securityinfo.it/author/marina-londei/ "Articoli scritti da Marina Londei")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [Hacking](https://www.securityinfo.it/category/news/hacking-news/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [Minacce](https://www.securityinfo.it/category/news/minacce-news/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2025/12/02/shadypanda-oltre-4-milioni-di-browser-infetti-in-una-campagna-durata-7-anni/#respond)

---

Una campagna durata sette anni che ha infettato 4.3 milioni di utenti Edge e Chrome: è il bilancio degli impatti di **ShadyPanda**, una campagna che ha colpito estensioni browser per installare backdoor ed eseguire codice da remoto.

L’indagine di Koi Security [ha rivelato](https://www.koi.ai/blog/4-million-browsers-infected-inside-shadypanda-7-year-malware-campaign) **due operazioni principali:** una **Backdoor RCE** che ha colpito 300.000 utenti e un’**operazione spyware** contro 4 milioni di utenti. I ricercatori hanno identificato cinque estensioni “militarizzate” a metà 2024 che eseguono codice arbitrario da remoto su base oraria, sfruttando il pieno accesso al browser. Altre cinque estensioni si occupano invece di collezionare ogni URL visitato, le query di ricerca e i click del mouse, trasmettendo poi questi dati a dei server in Cina.

“*Alcune delle estensioni di ShadyPanda sono state segnalate e verificate da Google, garantendo fiducia immediata e distribuzione massiccia. **Per sette anni, questo attore ha imparato a sfruttare i marketplace dei browser come arma, costruendo fiducia, accumulando utenti e colpendo con aggiornamenti silenziosi***” hanno spiegato i ricercatori.

![ShadyPanda](https://www.securityinfo.it/wp-content/uploads/2025/12/Gemini_Generated_Image_hnl02xhnl02xhnl0.png)

## Le quattro fasi di ShadyPanda

Il team ha identificato quattro fasi principali della campagna attive più o meno a lungo negli ultimi sette anni. Un primo filone riguarda la “truffa degli sfondi”, una campagna molto massiccia, ma meno sofisticata degli altri flussi, avvenuta nel 2023. Si parla di 145 estensioni (20 su Chrome Web Store, 125 su Microsoft Edge) mascherate da app per sfondi o produttività. Le estensioni **iniettavano silenziosamente codici di tracciamento affiliato** ogni volta che l’utente visitava siti come eBay, Amazon o Booking.com, guadagnando commissioni nascoste su ogni acquisto. Gli attaccanti hanno usato il tracciamento di Google Analytics per registrare e vendere i dati di navigazione.

A inizio 2024 ShadyPanda è diventato più aggressivo ed è **passato dalla monetizzazione passiva al controllo attivo del browser.** In questo caso, le estensioni malevole reindirizzavano le ricerche verso un browser hijacker (trovi.com)  per monetizzare e manipolare i risultati. Le estensioni leggevano i cookie da domini specifici per inviare dati di tracciamento, creando identificatori univoci per monitorare l’attività. Le stringhe digitate dall’utente nella barra di ricerca venivano inviata a server esterni per profilare in tempo reale degli interessi dell’utente.

**Una terza fase della campagna è iniziata tra il 2018 e il 2019** quando cinque estensioni (tra le quali Clean Master che conta oltre 200.000 installazioni) sono state caricate e hanno cominciato a operare in modo legittimo, ottenendo lo status di “In Evidenza” e “Verificate” dai marketplace. In seguito, a metà del 2024 gli attaccanti hanno distribuito un aggiornamento malevolo a oltre 300.000 installazioni tramite il meccanismo di aggiornamento automatico di Chrome ed Edge. L’aggiornamento ha installato una backdoor sui browser che ha consentito agli attaccanti di **scaricare ed eseguire JavaScript arbitrario con pieno accesso alle API del browser**, per veicolare ransomware, sottrarre credenziali o per motivi di spionaggio. un meccanismo che consente potenzialment. Capacità: Si tratta di una backdoor completa. Sebbene il payload attuale sia la sorveglianza, l’attore può decidere in qualsiasi momento di trasformarlo in un veicolo per ransomware, furto di credenziali o spionaggio aziendale.

Infine, l’ultimo flusso è il più grande e ha coinvolto oltre 4 milioni di installazioni combinate. A differenza delle estensioni militarizzate della Fase 3 (che sono state rimosse), questa vasta operazione di sorveglianza da 4 milioni di utenti è attualmente ancora attiva nel marketplace di Microsoft Edge. L’estensione di punta di questa fase è WeTab 新标签页 (WeTab New Tab Page).  Mascherata da strumento di produttività WeTab agisce come una sofisticata piattaforma di spyware che raccoglie numerose informazioni, comprese le query di ricerca, i movimenti del mouse, i dati di interazione con le pagine e i cookie.

![Chrome](https://www.securityinfo.it/wp-content/uploads/2022/01/browser-g0d427d70c_1280.jpg)

Poiché le estensioni sono ancora attive, hanno già i permessi di accesso che servono per esfiltrare i dati. Questo significa che l’attore può sfruttare in qualsiasi momento il meccanismo di aggiornamento automatico per distribuire il framework di esecuzione remota di codice della Fase 3 o altri payload più pericolosi.

“*Il successo di ShadyPanda non è solo una questione di sofisticazione tecnica. **Si tratta piuttosto dello sfruttamento sistematico della stessa vulnerabilità per sette anni: i marketplace esaminano le estensioni al momento della presentazione, ma non controllano cosa succede dopo l’approvazione***” hanno sottolineato i ricercatori di Koi Security. Insomma, la “fiducia” si è rivelata la vulnerabilità più grande.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

-...
---
title: Prompt injection nelle immagini: l’image scaling trasforma un JPEG in un esfiltratore
url: https://www.securityinfo.it/2025/08/22/prompt-injection-nelle-immagini-limage-scaling-trasforma-un-jpeg-in-un-esfiltratore/?utm_source=rss&utm_medium=rss&utm_campaign=prompt-injection-nelle-immagini-limage-scaling-trasforma-un-jpeg-in-un-esfiltratore
source: Securityinfo.it
date: 2025-08-23
fetch_date: 2025-10-07T00:49:00.873567
---

# Prompt injection nelle immagini: l’image scaling trasforma un JPEG in un esfiltratore

Aggiornamenti recenti Ottobre 6th, 2025 5:03 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Impennata delle scansioni dei portali di login di Palo Alto Networks: +500%](https://www.securityinfo.it/2025/10/06/impennata-delle-scansioni-dei-portali-di-login-di-palo-alto-networks-500/)
* [Microsoft Sentinel: arriva l’era degli agenti AI e della difesa predittiva](https://www.securityinfo.it/2025/10/06/microsoft-sentinel-arriva-lera-degli-agenti-ai-e-della-difesa-predittiva/)
* [CERT-AGID 27 settembre – 3 ottobre: Weebly, tessera sanitaria e CieID sotto attacco](https://www.securityinfo.it/2025/10/06/cert-agid-27-settembre-3-ottobre-weebly-tessera-sanitaria-e-cieid-sotto-attacco/)
* [RedHat vittima di un breach: sottratti oltre 500 GB di dati](https://www.securityinfo.it/2025/10/03/redhat-vittima-di-un-breach-sottratti-oltre-500-gb-di-dati/)
* [Clearskies: la suite di sicurezza avanzata made in Europe arriva in Italia](https://www.securityinfo.it/2025/10/03/clearskies-la-suite-di-sicurezza-avanzata-tutta-made-in-europe-arriva-in-italia/)

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

## Prompt injection nelle immagini: l’image scaling trasforma un JPEG in un esfiltratore

Ago 22, 2025  [Redazione](https://www.securityinfo.it/author/redazione/ "Articoli scritti da Redazione")
 [Attacchi](https://www.securityinfo.it/category/news/attachi/), [In evidenza](https://www.securityinfo.it/category/in-evidenza/), [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/), [Vulnerabilità](https://www.securityinfo.it/category/news/vulnerabilita/)
 [0](https://www.securityinfo.it/2025/08/22/prompt-injection-nelle-immagini-limage-scaling-trasforma-un-jpeg-in-un-esfiltratore/#respond)

---

Un’immagine apparentemente innocua, inviata a un assistente AI multimodale, e senza nessun clic da parte dell’utente inizia l’esfiltrazione dei dati. [È lo scenario dimostrato da un gruppo di ricercatori di Trail of Bits](https://blog.trailofbits.com/2025/08/21/weaponizing-image-scaling-against-production-ai-systems/) che ha sfruttato una debolezza tutt’altro che marginale: molte piattaforme AI, prima di passare un’immagine al modello, la ridimensionano. Durante il downscaling emergono porzioni del contenuto che a piena risoluzione non sono visibili all’occhio umano, ma che il modello è perfettamente in grado di leggere come testo o istruzioni. Dentro quella “zona grigia” prende forma una prompt injection multimodale che guida l’agente a compiere azioni non autorizzate, fino a spedire all’esterno informazioni private dell’utente.

![](https://www.securityinfo.it/wp-content/uploads/2025/08/SPY-22-ago-2025CG-1024x683.png)

**Dove funziona l’attacco e perché è subdolo**

I test mostrano impatti su implementazioni reali, inclusi Gemini CLI, Vertex AI Studio, interfacce web e API di Gemini, Google Assistant su Android e piattaforme come Genspark. Il denominatore comune non è il modello in sé, ma la catena che prepara l’input: l’immagine viene ridotta di dimensioni per motivi di prestazioni o compatibilità e il risultato consegnato al modello non corrisponde a ciò che l’utente ha visto nel proprio client. Questo scollamento percettivo consente di nascondere una istruzione malevola nel file sorgente che, una volta rimpicciolito, diventa leggibile dall’OCR o dal parser visivo del modello. L’utente è convinto di aver inviato un’immagine pulita; il modello in realtà “vede” un contenuto trasformato, che contiene un prompt strutturato per pilotarne il comportamento.

**La catena di esfiltrazione su Gemini CLI con MCP Zapier**

Il caso più eclatante riguarda Gemini CLI configurato con un server MCP di Zapier settato in modalità permissiva. La presenza di trust=true nel file di configurazione implica che le chiamate agli strumenti siano pre-approvate e non richiedano conferma esplicita. In questo contesto l’immagine truccata funziona da miccia: una volta ridimensionata e interpretata dal modello, il prompt nascosto chiede all’agente di utilizzare le integrazioni MCP, ad esempio per interrogare Google Calendar e inviare eventi e dettagli a un indirizzo controllato dall’attaccante. L’intera sequenza avviene dietro le quinte, senza anteprima dell’input effettivo e senza segnali di allarme per l’utente.

**Dalle visioni classiche al multimodale: perché lo scaling è una superficie d’attacco**

Gli attacchi di image scaling hanno un passato che affonda nel mondo della computer vision classica, dove i modelli imponevano dimensioni fisse e il pre-processing includeva riduzioni aggressive. Oggi i modelli multimodali sono più flessibili, ma le infrastrutture che li circondano continuano spesso a ridimensionare gli input. Questo riapre la porta a un vettore che sfrutta le proprietà dei filtri di ricampionamento. Quando si passa da un’immagine grande a una più piccola, gli algoritmi fondono più pixel in uno solo. Se i pattern ad alta frequenza non sono filtrati in modo adeguato, si produce aliasing: l’informazione originale si “ricostruisce” in modo ambiguo e può far emergere linee e caratteri che non erano percepibili a piena risoluzione. È il cuore della teoria di Nyquist–Shannon applicata in modo adversarial: manipolando i pixel sorgente si induce il downscaler a generare un messaggio mirato nella versione ridotta.
Non tutti i downscaler si comportano allo stesso modo. I ricercatori hanno messo a punto una metodologia per identificare l’algoritmo di ridimensionamento utilizzato dai vari sistemi. Tra i più diffusi compaiono nearest neighbor, bilinear e bicubic, ma le differenze non si fermano al nome: librerie come Pillow, PyTorch, OpenCV o TensorFlow implementano varianti con anti-aliasing, allineamento e kernel differenti. Attraverso una batteria di immagini di test – scacchiere, cerchi concentrici, bande verticali e orizzontali, pattern Moiré, spigoli inclinati – è possibile osservare artefatti di ringing, blur, gestione dei bordi e incoerenze cromatiche, sufficienti a riconoscere la pipeline e scegliere il crafting più efficace.

Nel caso del bicubico il team spiega come sfruttare la dipendenza del pixel di output dai sedici vicini (4×4) e dai relativi pesi, individuando i pixel a massima importanza. Regolando in modo millimetrico la luminanza dei punti in aree scure e utilizzando un’ottimizzazione ai minimi quadrati, la versione ridotta dell’immagine tende verso uno sfondo di un colore specifico con testo ad alto contrasto che il modello interpreta senza difficoltà. Il messaggio non è percepibile a occhio nella sorgente ad alta risoluzione, ma diventa leggibile dopo il downscaling.

**Anamorpher: l’officina open source per attacchi su misura**

Per industrializzare l’approccio i ricercatori presentano Anamorpher, uno strumento open source pensato per generare e visualizzare immagini adversarial compatibili con i principali metodi di downscaling. L’interfaccia consente di selezionare l’algoritmo, pilotare i parametri e iterar...
---
title: Tecnologie Utilizzate In Ambito AI e Blockchain (GPU, CPU, FPGA)
url: http://darkwhite666.blogspot.com/2024/12/tecnologie-utilizzate-in-ambito-ai-e.html
source: Dark Space Blogspot
date: 2024-12-04
fetch_date: 2025-10-06T19:47:37.749249
---

# Tecnologie Utilizzate In Ambito AI e Blockchain (GPU, CPU, FPGA)

## Visualizzazioni Totali

[![Dark Space Blogspot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZgt0RUZjHgbkLsu7CbFNAiyAMd0qvDL2fubvcBv5c6R04keICe8K0ig6oXxzqa6519xC3S7eBHP3_F60rvo_NqafkHR83xyZwscmsQgwCw_EPQpiDWkgarGw08kUDwteX-zWL_I_uP1w/s1600/ask-fm.png)](https://darkwhite666.blogspot.com/)

TRA I PRIMI IN ITALIA A PARLARE DI BITCOIN (DAL 2012!): PER ESSERE SEMPRE AGGIORNATI SULLE NOVITA' TECNOLOGICHE DEL WEB SEGUITE LA PAGINA FACEBOOK (LINK A SINISTRA)

## martedì 3 dicembre 2024

### Tecnologie Utilizzate In Ambito AI e Blockchain (GPU, CPU, FPGA)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiV668eMhvIZrNrvrBCM4eXGBgyrTWty8pbhuKxmRQ4wgpYHoADsOBauPJHwNvgblElq3hukwNMvFhF9MMFsRctL45lrMvfaJdEomknSSvN2oer_XhpWvEj0RhKoXZzgA0MIWlwGTXEAH4O6YwJDZ0mPO5LN81WK0ZmxhUVo4tCIcnSVAYXFFV1ZOuPkeo/s320/AI-cloud-shutterstock_2200588925.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiV668eMhvIZrNrvrBCM4eXGBgyrTWty8pbhuKxmRQ4wgpYHoADsOBauPJHwNvgblElq3hukwNMvFhF9MMFsRctL45lrMvfaJdEomknSSvN2oer_XhpWvEj0RhKoXZzgA0MIWlwGTXEAH4O6YwJDZ0mPO5LN81WK0ZmxhUVo4tCIcnSVAYXFFV1ZOuPkeo/s555/AI-cloud-shutterstock_2200588925.jpg)

In questo articolo vedremo alcune aziende e tecnologie utilizzate anche in ambito AI (blockchain e non). Sicuramente la più famosa è NVIDIA ma si può citare anche AMD (e Xilinx), Intel, TPU di Google, IPU di Graphcore,  Azure AI di Microsoft, Cerebras Systems, Huawei Ascend, Baidu Kunlun e Tenstorrent.

NVIDIA: GPU

Sicuramente **[NVIDIA](https://www.nvidia.com/it-it/)** è la più nota perchè può essere utilizzata su infrastrutture cloud, specialmente per carichi di lavoro che richiedono molta potenza di calcolo, come l'intelligenza artificiale (AI), il machine learning e il deep learning. Infrastrutture cloud (tipo Akash, altre decentralizzate o centralizzate tipo AWA o Google Cloud) permettono a chiunque di mettere a disposizione risorse di calcolo, comprese GPU NVIDIA, che sono ampiamente utilizzate per eseguire applicazioni AI. NVIDIA è famosa per le sue GPU (unità di elaborazione grafica), utilizzate per i videogiochi ma adatte anche per l'AI. Le GPU hanno una capacità di elaborazione parallela superiore rispetto alle CPU, che le rende ideali per il training di modelli di machine learning, specialmente quelli basati su reti neurali.

Tramite NVIDIA è possibile velocizzare l'addestramento dei modelli di AI, riducendo i tempi da giorni (o settimane) a ore o minuti. Viene utilizzato anche la piattaforma CUDA (Compute Unified Device Architecture) sviluppata da NVIDIA, che permette agli sviluppatori di usare le sue GPU per scopi generali, come l'intelligenza artificiale e il machine learning.

NVIDIA ha creato una vasta gamma di software e framework per l'AI (come TensorRT), Deep Learning SDK (strumenti e librerie per accelerare il deep learning su GPU), GPU Cloud (hub di risorse AI che include container preconfigurati per AI), DGX Systems (sistemi hardware dedicati all'AI, come i server DGX. Alcuni progetti di intelligenza artificiale, come quelli di OpenAI, Tesla (per la guida autonoma) utilizzano GPU di NVIDIA per migliorare i loro modelli (vengono processati dati in tempo reali provenienti dai sensori dei veicoli, prendendo decisioni). Inoltre NVIDIA è parte integrante dello sviluppo di supercomputer per l'AI (Selene, uno dei supercomputer più potenti al mondo, è basato sulle tecnologie NVIDIA e viene utilizzato per eseguire applicazioni AI su larga scala) e di AI generativa (modelli che generano testo, immagini e video).  Nell’ambito dell’AI edge, NVIDIA fornisce tecnologie per applicazioni AI in dispositivi più piccoli e distribuiti, come droni, robot industriali (automazione) e dispositivi IoT, dove il calcolo AI deve essere fatto localmente.

AMD: GPU E FPGA

**[AMD (Advanced Micro Devices)](https://www.amd.com/en.html)** è un altro produttore di GPU che, come NVIDIA, è utilizzato per accelerare carichi di lavoro di AI e deep learning. In particolare le serie Radeon Instinct sono progettate per il calcolo intensivo e sono utilizzate in alcuni progetti di AI e blockchain.

AMD offre anche la piattaforma ROCm (Radeon Open Compute), un ambiente di sviluppo open-source per il calcolo parallelo e l’intelligenza artificiale, simile a CUDA di NVIDIA. La società Xilinx è stata assorbita da AMD, in particolare essa produce FPGA (Field-Programmable Gate Arrays), utili per applicazioni di intelligenza artificiale poiché possono essere configurati per eseguire modelli di AI ottimizzati per specifici casi d’uso. A differenza delle GPU, gli FPGA offrono un’elevata compatibilità e sono spesso utilizzati in settori come la guida autonoma e il calcolo decentralizzato, compreso il calcolo Edge Computing (IoT e Realtà Aumentata).

INTEL: CPU

**[Intel](https://www.intel.com/content/www/us/en/homepage.html)** è noto nel settore hardware ma anche per l'intelligenza artificiale. Le CPU Intel Xeon sono molto popolari per il training e l'inferenza di modelli AI e machine learning, specialmente in combinazione con FPGA (Field-Programmable Gate Arrays) o altri acceleratori.

Intel Nervana è stato usato per creare un'architettura specifica per l'AI. Intel ha costruito anche il suo ecosistema OpenVINO, che facilita l’ottimizzazione dei modelli AI per una varietà di hardware.

TPU DI GOOGLE

Google ha sviluppato i suoi propri acceleratori hardware chiamati **[TPU (Tensor Processing Units)](https://cloud.google.com/tpu?hl=it)**, progettati specificamente per eseguire modelli di machine learning, in particolare TensorFlow, la piattaforma AI di Google. Le TPU sono altamente ottimizzate per l'elaborazione di modelli di deep learning e sono utilizzate da Google Cloud, oltre che in vari progetti di AI distribuita. Esse possono essere utilizzate per sviluppare modelli AI che successivamente potrebbero essere integrati in sistemi decentralizzati.

IPU DI GRAPHCORE

Si tratta di una società specializzata nella produzione di hardware per l’AI. La loro architettura chiamata **[IPU (Intelligence Processing Unit)](https://www.graphcore.ai/products/ipu)** è progettata specificamente per accelerare i modelli di machine learning, offrendo una soluzione alternativa alle GPU per l'AI.

Le IPU di Graphcore sono utilizzate per migliorare l’efficienza del calcolo in reti neurali profonde.

WSE DI CEREBRAS SYSTEMS

**[Cerebras Systems](https://cerebras.ai/)** ha sviluppato WSE (Wafer-Scale Engine), che è il chip per AI più grande al mondo progettato per accelerare massivamente il training di modelli AI complessi. WSE ha la capacità di gestire enormi carichi di lavoro AI che potrebbero essere integrati in piattaforme di blockchain decentralizzate focalizzate sull’intelligenza artificiale. Cerebras viene impiegato in blockchain AI per velocizzare il calcolo decentralizzato.

ASCEND COMPUTING DI HUAWEI

Huawei ha sviluppato la propria linea di processori per AI chiamati **[Ascend](https://e.huawei.com/en/products/computing/ascend)**, specializzati per deep learning e machine learning. Gli acceleratori Ascend sono utilizzati in vari settori, dalle applicazioni cloud ai data center e sono compatibili con diversi framework di AI.

AZURE AI DI MICROSOFT

Microsoft offre **[Azure AI](https://ai.azure.com/)**, un'infrastruttura di cloud computing che fornisce accesso a potenza di calcolo accelerata per AI tramite CPU, GPU (incluso NVIDIA) e FPGA. Project Brainwave, in particolare, è una piattaforma AI di Microsoft che utilizza FPGA per accelerare le inferenze di AI in tempo reale. Microsoft ha un ecosistema in espansione che combina blockchain e AI, e le sue tecnologie di calcolo AI possono essere integrate con progetti blockchain AI.

BAIDU KUNLUN

**[Baidu](https://www.baidu.com/)** ha sviluppato la sua linea di chip Kunlun per AI, progettata per ottimizzare l’elaborazione di modelli di intelligenza artificiale nei data center e nelle applicazioni edge. Questi chip potrebbero trovare impiego in progetti blockchain AI per migliorare la velocità e l’efficienza...
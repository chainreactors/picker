---
title: Un pericoloso scambio di identità
url: https://hackerjournal.it/11186/un-pericoloso-scambio-di-identita/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-17
fetch_date: 2025-10-04T04:04:17.847374
---

# Un pericoloso scambio di identità

[![Hackerjournal.it](https://hackerjournal.it/wp-content/uploads/2017/12/hjnegw-1.png)](https://hackerjournal.it/)

* [Forum](https://hackerjournal.it/forum/)
* [News](https://hackerjournal.it/category/news/)
* [Tech](https://hackerjournal.it/category/tecno/)
* [Articoli](https://hackerjournal.it/category/tech/)
* [Trending](https://hackerjournal.it/trending/)
* [Accademia](https://hackerjournal.it/corsi/)
* [Contest](https://hackerjournal.it/contest/)
* [Glossario](https://hackerjournal.it/encyclopedia/)
* [Abbonati](https://hackerjournal.it/81/abbonati-ad-hacker-journal/)
* [Arretrati](https://hackerjournal.it/arretrati-hackerjournal/)

Connect with us

[![Hackerjournal.it](https://hackerjournal.it/wp-content/uploads/2017/12/hjnew-1.png)](https://hackerjournal.it/)
[![Hackerjournal.it](https://hackerjournal.it/wp-content/uploads/2017/12/hjnegw-1.png)](https://hackerjournal.it/)

## Hackerjournal.it

#### Un pericoloso scambio di identità

* [Forum](https://hackerjournal.it/forum/)
* [News](https://hackerjournal.it/category/news/)

  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/coppadelmondo-400x240.png)

    Mondiali 2026: la truffa corre sul Web](https://hackerjournal.it/14527/mondiali-2026-la-truffa-corre-sul-web/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/massive_npm-400x240.png)

    Il virus che “ruba” il codice](https://hackerjournal.it/14522/il-virus-che-ruba-il-codice/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/stellarium-400x240.jpg)

    Il malware che spia chi visita siti porno](https://hackerjournal.it/14518/il-malware-che-spia-chi-visita-siti-porno/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/kaspesky_corso-400x240.png)

    Un corso online per difendere gli LLM](https://hackerjournal.it/14504/un-corso-online-per-difendere-gli-llm/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/truffa_iphone-400x240.png)

    Truffe online dell’iPhone 17](https://hackerjournal.it/14495/truffe-online-delliphone-17/)
* [Tech](https://hackerjournal.it/category/tecno/)
* [Articoli](https://hackerjournal.it/category/tech/)

  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/deepin_home-400x240.png)

    Linux incontra il design](https://hackerjournal.it/14508/linux-incontra-il-design/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/09/concetto-di-gestione-delle-relazioni-con-i-clienti-400x240.jpg)

    L’arte di ascoltare le reti](https://hackerjournal.it/14474/larte-di-ascoltare-le-reti/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/04/attacchi-cibenetici-400x240.jpg)

    Attacchi ai servizi di rete](https://hackerjournal.it/14439/attacchi-ai-servizi-di-rete/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/08/persona-che-scrive-su-un-primo-piano-del-computer-portatile-400x240.jpg)

    Enumerazione: la vera identità della rete](https://hackerjournal.it/14421/enumerazione-la-vera-identita-della-rete/)
  + [![](https://hackerjournal.it/wp-content/uploads/2025/08/codice-binario-con-globo-sul-computer-portatile-400x240.jpg)

    I migliori tool per la scansione di rete](https://hackerjournal.it/14410/i-migliori-tool-per-la-scansione-di-rete/)
* [Trending](https://hackerjournal.it/trending/)
* [Accademia](https://hackerjournal.it/corsi/)
* [Contest](https://hackerjournal.it/contest/)
* [Glossario](https://hackerjournal.it/encyclopedia/)
* [Abbonati](https://hackerjournal.it/81/abbonati-ad-hacker-journal/)
* [Arretrati](https://hackerjournal.it/arretrati-hackerjournal/)

### [Articoli](https://hackerjournal.it/category/tech/)

# Un pericoloso scambio di identità

Il servizio EKS di Amazon Web Services utilizza il sistema di identità AWS IAM per gestire gli utenti e li traduce nel sistema di ruoli e permessi tipici di Kubernetes. Questa traduzione, però, nasconde un punto debole

![Avatar](https://secure.gravatar.com/avatar/7b274a75782cdb25f96daff3132a6c9c?s=46&d=mm&r=g)

Pubblicato

il

16 Gennaio 2023

By

[hj\_backdoor](https://hackerjournal.it/author/hj_backdoor/ "Articoli scritti da hj_backdoor")

![](https://hackerjournal.it/wp-content/uploads/2023/01/soluzione.png)

* Share
* Tweet

**[Amazon Web Services](https://aws.amazon.com/it/) è il cloud di Amazon, una delle principali piattaforme cloud disponibili**. La quantità di servizi che offre è enorme, praticamente qualsiasi cosa si possa immaginare nel mondo del cloud computing, e sono solitamente indicati con delle sigle. S3, per esempio, è un semplice storage cloud. EC2 offre macchine virtuali. Mentre **EKS** (**Elastic Kubernetes Service**) è l’implementazione in chiave Amazon di Kubernetes. Naturalmente, nella logica di Amazon, tutti i vari servizi sono interconnessi, in particolare per quanto riguarda l’autenticazione. Su [Kubernetes](https://kubernetes.io/it/docs/concepts/overview/what-is-kubernetes/) è, infatti, presente un meccanismo di autenticazione basato su utenti e ruoli, per cui a ogni utente vengono assegnati dei token identificativi e una serie di autorizzazioni per l’accesso a specifiche risorse. Questo permette di definire con estrema precisione quali attività possano essere svolte da ciascun utente, rendendo l’ambiente molto sicuro, perché non è necessario dare a qualcuno più permessi di quanti ne servono. **L’aspetto interessante è che già da prima che esistesse Kubernetes, il sistema di autenticazione di Amazon, AWS IAM, funzionava con la stessa logica**.

### **DOVE RISIEDE LA VULNERABILITÀ**

Per evitare di dover ripetere tutto due volte, cosa piuttosto complicata in aziende con centinaia o migliaia di dipendenti, **Amazon ha deciso di integrare il proprio IAM con la sua implementazione di Kubernetes**, così è possibile utilizzare le utenze AWS preesistenti, magari già in uso per accedere a servizi come S3 o CloudFront, per accedere anche alle risorse allocate sul cluster Kubernetes. È quindi stato pubblicato il **modulo AWS IAM authenticator for Kubernetes**, che permette l’utilizzo del sistema di autenticazione di Amazon per accedere alle risorse di un cluster Kubernetes (uno qualsiasi, in realtà, non necessariamente EKS). **Kubernetes è infatti open source**, quindi chiunque può realizzarsi un cluster sul proprio hardware, e **Amazon ha rilasciato come open source anche la propria implementazione, col nome di “EKS Anywhere**”. **E chiunque può decidere di utilizzare come autenticatore il servizio IAM di Amazon, su qualsiasi cluster Kubernetes**. Semplicemente, Kubernetes continua a gestire i suoi ruoli e permessi come al solito, ma per l’autenticazione di un accesso non si fa il classico scambio di chiave direttamente in Kubernetes: l’utente si autentica su Amazon e riceve un token di autorizzazione temporaneo, che viene poi utilizzato nelle varie chiamate alle KubeAPI per collegare l’attività all’utente. Il modulo  **aws-iam-authenticator** si occupa proprio di mettere in relazione i ruoli nativi di Kubernetes con l’autenticazione di Amazon. Ed è in questa “traduzione” che è stato trovata una vulnerabilità, a meno di un anno dalla pubblicazione di EKS Anywhere.

[![](https://hackerjournal.it/wp-content/uploads/2023/01/bug-1024x474.png)](https://hackerjournal.it/wp-content/uploads/2023/01/bug.png)

*Figura 1 – Il problema è che il nome utente viene cercato come lowercase, quindi è possibile che due nomi, che differiscono solo per le maiuscole, vengano confusi. [[Fonte](https://github.com/kubernetes-sigs/aws-iam-authenticator/blob/27337b2b74c3140cf745a64f7154fe8ff7592258/pkg/token/token.go#L483)]*

### **UN DIZIONARIO PER LA TRADUZIONE**

La procedura di autenticazione percorre sostanzialmente sei passi:

1. L’utente invia una richiesta alle API di EKS, per ottenere delle risorse Kubernetes (per esempio, “kubectl get pods”). La richiesta include un token di autorizzazione nell’intestazione, che è una stringa base64 di AWS Security Token Service.
2. Il server riceve la richiesta, estrae il token, e lo invia nel corpo della richiesta verso il server di A...
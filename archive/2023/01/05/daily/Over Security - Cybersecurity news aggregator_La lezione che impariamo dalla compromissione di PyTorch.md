---
title: La lezione che impariamo dalla compromissione di PyTorch
url: https://www.insicurezzadigitale.com/la-lezione-che-impariamo-dalla-compromissione-di-pytorch/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-05
fetch_date: 2025-10-04T03:05:21.270853
---

# La lezione che impariamo dalla compromissione di PyTorch

[(in)sicurezza digitale](https://insicurezzadigitale.com/)

* Incidenti e violazioni
  + [Roundup – Flash](https://insicurezzadigitale.com/category/roundup/)
  + [Incidenti e Violazioni](https://insicurezzadigitale.com/category/incidenti-e-violazioni/)
  + [Phishing](https://insicurezzadigitale.com/category/phishing/)
  + [Privacy](https://insicurezzadigitale.com/category/privacy/)
  + [Data Breach](https://insicurezzadigitale.com/category/data-breach/)
* [Ransomware](https://insicurezzadigitale.com/category/ransomware/)
* [Malware e Vulnerabilità](https://insicurezzadigitale.com/category/malware-e-vulnerabilita/)
  + [Analisi](https://insicurezzadigitale.com/category/analisi/)
* [La stampa dice](https://insicurezzadigitale.com/la-stampa-dice/)
* Altro…
  + [Chi siamo](https://insicurezzadigitale.com/chi-siamo/)
  + [> Whistleblowing <](https://insicurezzadigitale.com/whistleblowing/)
  + [Eventi](https://insicurezzadigitale.com/category/eventi/)
  + [Editoriali di Dario Fadda](https://blogsicurezza.myblog.it/)
  + [Data Leaks list](https://insicurezzadigitale.com/data-leaks-list/)
  + [Archivio Cyber Security Notes](https://insicurezzadigitale.com/archivio-cyber-security-notes/)
  + [Archivio Malware samples](https://insicurezzadigitale.com/archivio-malware-samples/)
  + [Infosec Tools list](/tool)
* Il Network
  + [NINAsec – Newsletter](https://ninasec.substack.com/)
  + [Spcnet.it](https://www.spcnet.it)
  + [Ziobudda](https://www.ziobudda.org)
  + [ilGlobale.it](https://www.ilglobale.it)
  + [SecureBulletin.com](https://securebulletin.com/)
* [I Forums](https://forum.ransomfeed.it/)

[Malware e Vulnerabilità](https://insicurezzadigitale.com/category/malware-e-vulnerabilita/)

# La lezione che impariamo dalla compromissione di PyTorch

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
4 Gennaio 2023

![](https://insicurezzadigitale.com/wp-content/uploads/2023/01/pytorch-768x432-1.png)

Si parla di:

Toggle

* [Dipendenza malevola in PyTorch versione nightly](#Dipendenza_malevola_in_PyTorch_versione_nightly)
* [Il problema delle dipendenze](#Il_problema_delle_dipendenze)
* [Dietro PyTorch c’è Meta](#Dietro_PyTorch_ce_Meta)

Durante le festività natalizie, momento in cui l’igiene informatica è vistosamente più blanda del resto dell’anno, attori malevoli hanno approfittato di questa situazione per compromettere uno degli elementi chiave per la ricerca sull’intelligenza artificiale: PyTorch che, in questo caso ha poche “colpe”. Il problema delle dipendenze è qualcosa di più grande.

## Dipendenza malevola in PyTorch versione nightly

Di recente, gli attori delle minacce hanno compromesso un repository di codice in PyPI, **il più grande Indice di Pacchetti Python** (quelli che installiamo nei nostri progetti con l’installer `pip`, per intenderci), finendo per installare una dipendenza dannosa sul progetto PyTorch.

Gli hacker [hanno creato](https://pytorch.org/blog/compromised-nightly-dependency/) un pacchetto Python chiamato **torchtriton** su PyPI, che è identico al nome di un pacchetto nel sistema PyTorch stesso, solo che gli impatti sono altamente malevoli:

* Il pacchetto contiene l’eseguibile del malware Triton che si rivolge specificamente agli ambienti Linux a 64 bit.
* Il malware ruba dati sensibili, incluse informazioni di sistema come nome host, nome utente, configurazione Git locale, chiavi SSH e i primi 1.000 altri file nella home directory di dimensioni inferiori a 100 KB.
* Invece di esfiltrare i dati, il malware li comprime, li codifica in una sequenza di quelli che sembrano nomi di server appartenenti a un nome di dominio (h4ck[.]cfd) controllato dai criminali.
* I server compromessi perdono le chiavi di accesso con il pretesto di una semplice ricerca diretta al server DNS ufficiale wheezy[.]io.

Il team di PyTorch avverte coloro che hanno scaricato e installato **PyTorch-nightly su Linux** tramite `pip` tra il **25 dicembre 2022 e il 30 dicembre 2022**, dovrebbero disinstallarlo.

Dovrebbe essere sostituito con binari nightly datati 30 dicembre 2022 e successivi.

“I pacchetti PyTorch-nightly Linux installati tramite pip durante quel periodo hanno installato una dipendenza, torchtriton, che è stata compromessa nel repository di codice Python Package Index (PyPI) e ha eseguito un binario dannoso”, dice l’avviso. “Questo è ciò che è noto come attacco alla catena di approvvigionamento e influisce direttamente sulle dipendenze per i pacchetti che sono ospitati su indici di pacchetti pubblici”.

Gli utenti dei pacchetti stabili di PyTorch non sono interessati da questo problema.

## Il problema delle dipendenze

PyTorch, utilizzando la dipendenza `torchtriton` da progetto, non ha molte altre responsabilità su questo grave incidente informatico. In effetti l’unica colpa è appunto, quella di utilizzare da progetto questa dipendenza. Il problema risiede infatti a monte, la compromissione è avvenuta nel repository di pacchetti Python, il più importante e famoso al mondo, calando di conseguenza poi il problema, direttamente al progetto di PyTorch (così come a qualsiasi altro progetto che utilizzi questa dipendenza).

Invito a riflettere sul meccanismo delle dipendenze: in pratica, qualsiasi progetto mettiamo in piedi, a meno che ogni volta non si voglia *reinventare la ruota*, deve ereditare delle dipendenze terze. In quel momento e in qualsiasi altro momento della vita del nostro progetto, **non possiamo sapere cosa succeda nel dietro le quinte delle dipendenze** che stiamo utilizzando. Questo vale per tantissimi progetti software che utilizziamo quotidianamente e per tantissime altre dipendenze che ognuno di questi software sfrutta.

Utilizzare solo le versioni stable sia delle dipendenze che dei progetti finali che installiamo, potrebbe essere una mitigazione valida, anche se non garantirà nemmeno questo di evitare di incorrere in problemi come questi.

Oltre al fatto di aver rimosso il pacchetto dannoso **torchtriton**, il gestore **PyPI** sta cercando di migliorare la sicurezza.

La scorsa estate infatti, ha iniziato a richiedere l’implementazione dell’autenticazione a due fattori (2FA) per i progetti ritenuti critici, definiti come qualsiasi progetto nell’uno per cento più alto dei download degli ultimi sei mesi. I manutentori idonei di progetti critici [possono ottenere due chiavi di sicurezza gratuite per configurare 2FA](https://pypi.org/security-key-giveaway/).

## Dietro PyTorch c’è Meta

Dal 2016, quando Facebook ha cominciato a collaborare con la comunità IA per creare il framework PyTorch per la ricerca sull’intelligenza artificiale, **migliaia di collaboratori hanno sviluppato più di 150.000 progetti utilizzando PyTorch**, che è diventata così una delle piattaforme leader per la ricerca e la produzione in tutta la comunità AI. A [settembre](https://www.ilsole24ore.com/art/meta-lancia-fondazione-pytorch-ecco-cosa-cambia-mercato-deep-learning-AERnWuzB) 2022, **Mark Zuckerberg** ha annunciato che il progetto PyTorch si trasformerà nella fondazione senza scopo di lucro **PyTorch Foundation** che farà parte della *Linux Foundation*, un consorzio tecnologico la cui missione principale è **lo sviluppo collaborativo di software open source.**

##### < tags />

[bug](https://insicurezzadigitale.com/tag/bug/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[PyTorch](https://insicurezzadigitale.com/tag/pytorch/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=La+lezione+che+impariamo+dalla+compromissione+di+PyTorch&url=https://insicurezzadigitale.com/la-lezione-che-impariamo-dalla-compromissione-di-pytorch/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/la-lezione-che-impariamo-dalla-compromissione-di-pytorch/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/la-lezione-che-impariamo-dalla-compromissione-di-pytorch/&title=La+lezione+che+impari...
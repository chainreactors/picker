---
title: Makop Ransomware Gang: uno sguardo all’interno
url: https://www.insicurezzadigitale.com/makop-ransomware-gang-uno-sguardo-allinterno/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-17
fetch_date: 2025-10-04T09:52:08.675414
---

# Makop Ransomware Gang: uno sguardo all’interno

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

[Ransomware](https://insicurezzadigitale.com/category/ransomware/)

# Makop Ransomware Gang: uno sguardo all’interno

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
16 Marzo 2023

![](https://insicurezzadigitale.com/wp-content/uploads/2023/03/12ec_shutterstock_687323650.jpg)

Si parla di:

Toggle

* [Cosa è stato scoperto?](#Cosa_e_stato_scoperto)
* [Esternalizzare l’attacco](#Esternalizzare_lattacco)
* [In sintesi](#In_sintesi)

La banda di ransomware Makop è un attore di ransomware di livello secondario che è operativo dal 2020.

Il ricercatore di sicurezza informatica Luca Mella ha condiviso approfondimenti tecnici sul ransomware Makop che raggiunge la persistenza attraverso strumenti .NET dedicati.

Nonostante la sua bassa classificazione, l’attore di minacce ha preso di mira con successo le aziende in Europa e in Italia con il suo arsenale ibrido di sviluppato su misura e pronto all’uso strumenti software. In questo articolo, diamo un’occhiata più da vicino ad alcuni dei dettagli tecnici dell’arsenale di Makop ransomware.

## Cosa è stato scoperto?

[È stato scoperto che la banda di ransomware Makop](https://medium.com/%40lcam/makop-the-toolkit-of-a-criminal-gang-53cd44563c11) utilizza una serie di strumenti sviluppati su misura per eseguire i propri attacchi.

* Tra questi c’è uno strumento chiamato **ARestore** che è stato creato nel 2020 e parzialmente offuscato.
* Questo strumento genera elenchi combinati di nomi utente Windows locali e potenziali password e li verifica localmente.
* I truffatori lo usano dopo la fase di accesso iniziale della loro catena di attacco.
* Inoltre, gli operatori sfruttano altri assembly .NET personalizzati, come **PuffedUp**, per raggiungere ulteriori fasi della kill chain.
* Questo particolare strumento è progettato per garantire la persistenza dopo l’accesso iniziale.
* Lo strumento si basa su un file di configurazione testuale posto nella stessa cartella, contenente una o più stringhe di 42 caratteri che verranno inserite negli appunti dell’utente.

## Esternalizzare l’attacco

La banda di ransomware utilizza anche strumenti open source e freeware pronti all’uso per proseguire il movimento laterale e la scansione del sistema.

* Insieme all’abuso di strumenti Microsoft SysInternal come **PsExec** e altri noti strumenti open source come Putty e Mimikatz , Makop ha abusato di software ancora più peculiari.
* Ad esempio, gli aggressori hanno recentemente utilizzato **Advanced Port Scanner** e lo strumento **Windows Everything**.
* Un altro strumento unico utilizzato dal gruppo include uno strumento di amministrazione del sistema, soprannominato **YDArk**. È uno strumento open source disponibile su GitHub.

[![](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/0_WNJJEN1IfaTQwYj1.png)](https://www.insicurezzadigitale.com/wp-content/uploads/2023/03/0_WNJJEN1IfaTQwYj1.png)

## In sintesi

La banda di ransomware Makop ha a sua disposizione un arsenale di strumenti software sia sviluppati su misura che pronti all’uso.

L’uso di questi strumenti è una chiara indicazione delle tecniche in evoluzione che i criminali informatici utilizzano per condurre estorsioni digitali. Le organizzazioni devono adottare misure proattive per difendersi dagli attacchi di tipo ransomware Makop, mantenendo il software aggiornato e conducendo controlli di sicurezza regolari.

##### < tags />

[infosec](https://insicurezzadigitale.com/tag/infosec/)[Makop](https://insicurezzadigitale.com/tag/makop/)[ransomware](https://insicurezzadigitale.com/tag/ransomware/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Makop+Ransomware+Gang%3A+uno+sguardo+all%26%238217%3Binterno&url=https://insicurezzadigitale.com/makop-ransomware-gang-uno-sguardo-allinterno/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/makop-ransomware-gang-uno-sguardo-allinterno/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/makop-ransomware-gang-uno-sguardo-allinterno/&title=Makop+Ransomware+Gang%3A+uno+sguardo+all%26%238217%3Binterno)

[== articolo precedente ==](https://insicurezzadigitale.com/mondo-tech-in-crisi-per-il-collasso-di-silicon-valley-bank/)

[:: articolo successivo ::](https://insicurezzadigitale.com/chipmixer-e-stato-chiuso-da-europol-e-la-collaborazione-di-protonmail-google-paypal/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/makop-ransomware-gang-uno-sguardo-allinterno/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *Makop Ransomware Gang: uno sguardo all’interno*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=Makop+Ransomware+Gang:+uno+sguardo).
Condividi esempi, IOCs o tecniche di detection efficaci nel nostro 👉 [**forum community**](https://forum.ransomfeed.it/)

## [[ mastodon ]]

Su Mastodon mi trovi qui: [Mastodon](https://poliversity.it/%40nuke)

### :: i social ::

* [Facebook](https://www.facebook.com/spcnet.it)
* [Instagram](https://www.instagram.com/spcnet.it/)
* [Twitter](https://twitter.com/nuke86)
* [Linkedin](https://www.linkedin.com/in/dariofadda86/)

## == forum community ==

💬 Partecipa alla community con i nostri [Forum](https://forum.ransomfeed.it), unico spazio per tutto il Network!

### ~~ il network ~~

* [Spcnet.it](https://www.spcnet.it/)
* [ZioBudda.org](https://www.ziobudda.org)
* [dariofadda.it](https://dariofadda.it)
* [SecureBulletin.com](https://securebulletin.com)

### [[ NINAsec - la newsletter ]]

##### (in)sicurezza digitale

Notizie cybersecurity, malware, ransomware e sicurezza dei dati

Cerca

##### :: navigazione ::

* [A proposito di…](https://insicurezzadigitale.com/chi-siamo/)
* [La stampa dice](https://insicurezzadigitale.com/la-stampa-dice/)
* [Privacy Policy](https://insicurezzadigitale.com/privacy-policy/)
* [Cookie Policy](https://insicurezzadigitale.com/cookie-policy/)

##### ~~ contatti ~~

* info@spcnet.it
* [Whistleblowing](/whistleblowing/)
* [DarioFadda.it](https://me.dariofadda.it/)

---

© 2025 (in)sicurezza digitale. Tutti i diritti riservati.
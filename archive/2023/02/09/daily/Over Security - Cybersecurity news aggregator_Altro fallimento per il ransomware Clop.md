---
title: Altro fallimento per il ransomware Clop
url: https://www.insicurezzadigitale.com/altro-fallimento-per-il-ransomware-clop/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-09
fetch_date: 2025-10-04T06:08:53.779343
---

# Altro fallimento per il ransomware Clop

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

# Altro fallimento per il ransomware Clop

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
8 Febbraio 2023

![](https://insicurezzadigitale.com/wp-content/uploads/2023/02/clop-ransomware-low-detection-signed-executable_en.jpg)

La prima versione di ransomware per Linux, del gruppo criminale Clop, si è rivelata difettosa. Ciò ha consentito alle vittime di decrittografare i propri dati gratuitamente negli ultimi due mesi grazie agli esperti di SentinelLabs.

Sembra ormai noto ad eventi curiosi e imbarazzanti, la cyber gang Clop. Già nell’agosto 2022 infatti aveva “confuso” un’azienda di fornitura idrica del Regno Unito, rivendicando invece l’attacco come contro il più grande gestore idrico del Paese. Non si è mai saputo se l’errore fosse intenzionale (al fine di estorcere con prove false un’azienda più “ricca”), oppure accidentale, ma non fece una splendida figura.

Ora, come hanno scoperto i ricercatori, il ransomware non crittografa con le sue chiavi RC4, come nella versione Windows. La chiave principale viene semplicemente codificata nel malware, genera una chiave di crittografia, la decrittografa con essa e la memorizza localmente tra i file crittografati.

Inoltre, non supera la convalida per la decrittazione, il malware scrive i nuovi dati con la loro dimensione e data di crittografia, il che facilita anche la decrittazione.

Anche l’offuscamento e il rilevamento del bypass non sono stati ancora implementati.

Di conseguenza, un semplice [script Python](https://gist.github.com/Tera0017S1/c62a928a911442e1509d127fdcd93b71) è sufficiente per ripristinare quanto “danneggiato”.

##### < tags />

[Clop](https://insicurezzadigitale.com/tag/clop/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[ransomware](https://insicurezzadigitale.com/tag/ransomware/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=Altro+fallimento+per+il+ransomware+Clop&url=https://insicurezzadigitale.com/altro-fallimento-per-il-ransomware-clop/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/altro-fallimento-per-il-ransomware-clop/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/altro-fallimento-per-il-ransomware-clop/&title=Altro+fallimento+per+il+ransomware+Clop)

[== articolo precedente ==](https://insicurezzadigitale.com/uno-sguardo-allo-script-ransomware-esxiargs-che-ha-messo-in-difficolta-le-vmware/)

[:: articolo successivo ::](https://insicurezzadigitale.com/ninasec-sanzioni-ai-membri-di-trickbot/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/altro-fallimento-per-il-ransomware-clop/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *Altro fallimento per il ransomware Clop*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=Altro+fallimento+per+il+ransomware).
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
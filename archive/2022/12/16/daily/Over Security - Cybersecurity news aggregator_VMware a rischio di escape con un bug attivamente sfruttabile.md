---
title: VMware a rischio di escape con un bug attivamente sfruttabile
url: https://www.insicurezzadigitale.com/vmware-a-rischio-di-escape-con-un-bug-attivamente-sfruttabile/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-16
fetch_date: 2025-10-04T01:41:02.436403
---

# VMware a rischio di escape con un bug attivamente sfruttabile

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

# VMware a rischio di escape con un bug attivamente sfruttabile

![](https://secure.gravatar.com/avatar/0706373a7341ff1dd0bc60952232b77edfc2fcce715f4397e0ecab569e94cfc0?s=48&d=mm&r=g)

Dario Fadda
15 Dicembre 2022

![](https://insicurezzadigitale.com/wp-content/uploads/2022/12/vmware-patches-critical-guest-to-host-escape-issue-in-esxi-workstation-fusion-523712-2-1024x585.jpg)

Il colosso della virtualizzazione **VMware** martedì ha rilasciato aggiornamenti di emergenza per risolvere tre problemi di sicurezza.

Uno di questi include un errore di uscita dalla macchina virtuale dimostrato al concorso di hacking **GeekPwn 2022** ospitato dal Tencent Keen Security Lab cinese.

La vulnerabilità di *virtual machine escape*, documentata come **CVE-2022-31705**, è stata sfruttata dal ricercatore di Ant Security **Yuhao Jiang** su sistemi che eseguono prodotti VMware Fusion, ESXi e Workstation con patch complete.

> Here is my demo of the VM escape exploit on the latest version of VMware Fusion along with ESXi and Workstation. It was used to participate in GeekPwn 2022 and won the championship. [pic.twitter.com/Ze2rtCVAsv](https://t.co/Ze2rtCVAsv)
>
> — Danis Jiang (@danis\_jiang) [November 14, 2022](https://twitter.com/danis_jiang/status/1592051275088424961?ref_src=twsrc%5Etfw)

VMware ha descritto il bug come una vulnerabilità di scrittura out-of-heap nel controller USB 2.0 (EHCI). L’exploit ha vinto il primo premio su Geekpwn.

Secondo il [bollettino](https://www.vmware.com/security/advisories/VMSA-2022-0033.html), VMWare gli ha assegnato un punteggio **CVSS di 9.3** e allerta che un utente malintenzionato con privilegi amministrativi locali sulla VM potrebbe sfruttare questo problema per eseguire del codice.

Su ESXi, l’exploit è contenuto in una sandbox VMX, mentre su Workstation e Fusion può provocare un RCE sulla macchina su cui è installato Workstation o Fusion.

VM escape è il processo di un programma che esce dalla macchina virtuale su cui è in esecuzione e interagisce con il sistema operativo host.

La società ha rilasciato correzioni che correggono i bug di command injection e directory traversal che interessano VMware vRealize Network Insight (vRNI).

Anche la vulnerabilità nell’API REST vRNI è [classificata](https://www.vmware.com/security/advisories/VMSA-2022-0031.html) da VMware come critica con un **punteggio CVSSv3 di base di 9,8** perché un utente malintenzionato con accesso alla rete l’API REST vRNI, può potenzialmente eseguire comandi senza autenticazione.

##### < tags />

[bug](https://insicurezzadigitale.com/tag/bug/)[infosec](https://insicurezzadigitale.com/tag/infosec/)[vmware](https://insicurezzadigitale.com/tag/vmware/)

##### < condividi />

[Twitter](https://twitter.com/intent/tweet?text=VMware+a+rischio+di+escape+con+un+bug+attivamente+sfruttabile&url=https://insicurezzadigitale.com/vmware-a-rischio-di-escape-con-un-bug-attivamente-sfruttabile/)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https://insicurezzadigitale.com/vmware-a-rischio-di-escape-con-un-bug-attivamente-sfruttabile/)
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://insicurezzadigitale.com/vmware-a-rischio-di-escape-con-un-bug-attivamente-sfruttabile/&title=VMware+a+rischio+di+escape+con+un+bug+attivamente+sfruttabile)

[== articolo precedente ==](https://insicurezzadigitale.com/ursnifleak-la-nuova-fuga-di-dati-fatta-dai-criminali-contro-i-criminali/)

[:: articolo successivo ::](https://insicurezzadigitale.com/infragard-compromessa-la-piattaforma-interna-dellfbi-intervistiamo-immuniweb/)

### Vuoi commentare? Accendi la discussione[Annulla risposta](/vmware-a-rischio-di-escape-con-un-bug-attivamente-sfruttabile/#respond)

### 💬 [[ unisciti alla discussione! ]]

Se vuoi **commentare** su *VMware a rischio di escape con un bug attivamente sfruttabile*, utilizza la discussione sul [Forum](https://forum.ransomfeed.it/?q=VMware+a+rischio+di+escape).
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
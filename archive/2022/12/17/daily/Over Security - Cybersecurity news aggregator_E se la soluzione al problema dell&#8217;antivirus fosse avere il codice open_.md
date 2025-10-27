---
title: E se la soluzione al problema dell&#8217;antivirus fosse avere il codice open?
url: https://codiceinsicuro.it/2022/04/04/e-se-il-problema-dell-antivirus-fosse-avere-il-codice-open/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-17
fetch_date: 2025-10-04T01:48:03.620500
---

# E se la soluzione al problema dell&#8217;antivirus fosse avere il codice open?

[![Codice Insicuro](https://codiceinsicuro.it/assets/images/logo.png)](https://codiceinsicuro.it/)

* [Blog](https://codiceinsicuro.it/index.html)
* [About](https://codiceinsicuro.it/about)
* [Chi sono](https://codiceinsicuro.it/chi-sono/)
* [Talks](https://codiceinsicuro.it/talks/)
* [Contatti](https://codiceinsicuro.it/contatti)

Share

##### Iscriviti alla mailing list

Basta la tua email

![Paolo Perego](https://www.gravatar.com/avatar/d05560cd673cf2f4114012616fd57c33?s=250&d=mm&r=x)

[Paolo Perego](https://codiceinsicuro.it)[Follow](https://twitter.com/thesp0nge)
Specialista di sicurezza applicativa e certificato OSCE e OSCP, amo spaccare e ricostruire il codice in maniera sicura. Sono cintura nera di taekwon-do, marito e papà. Ranger Caotico Neutrale, scrivo su @codiceinsicuro.

# E se la soluzione al problema dell’antivirus fosse avere il codice open?

671
parole -  Lo leggerai in 3 minuti

---

Sul mio profilo [LinkedIN](https://www.linkedin.com/in/paolo-perego) ho lanciato una provocazione, non fine a sé stessa: [supportare ClamAV come antivirus](https://www.linkedin.com/posts/paolo-perego_github-cisco-talosclamav-clamav-documentation-activity-6916672325501259776-6MFf?utm_source=linkedin_share&utm_medium=member_desktop_web).

Da quando è scoppiato il conflitto tra Russia ed Ucraina, [si parla spesso](https://codiceinsicuro.it/2022/03/23/di-antivirus-etica-e-rischi-pindaric/) del potenziale rischio che Kaspersky rappresenti per i paesi ostili a Mosca.

Non voglio tornare alla domanda “è veramente un rischio?” perché la risposta non è così netta, non è così facile da dare e perché non ho la sfera di cristallo. Va detto, che l’azienda russa, da anni consente ad università, governi e partner di [visionare il codice nella sua sede](https://www.kaspersky.com/transparency-center-offices) in Svizzera.

Se questo non ha rassicurato i Governi, tanto che quello Italiano ne ha annunciato la dismissione, mi domando: ha veramente senso affidarsi ancora a qualcosa di commerciale, il cui codice è chiuso?

Certo, scegliere un antivirus europeo, o comunque alleato, o magari italiano, potrebbe essere una soluzione. Tuttavia il codice è sempre chiuso, non sai quello che può fare, quindi di fatto le stesse critiche che sono state mosse finora a Kaspersky possono essere replicate.

## Modello opensource: problemi e soluzioni

### Il codice aperto

Problema numero uno: il codice dell’antivirus, che gira con privilegi elevati sui nostri sistemi, è chiuso e non sappiamo quello che fa. Benissimo, apriamo il codice quindi.

Il codice liberamente disponibile permette a ricercatori, auditor indipendenti e agenzie governative, di verificare che non siano presenti backdoor, killswitch o meccanismi che possano consentire la compromissione dell’endpoint.

### Mancanza di supporto

Effettivamente, le licenze opensource sono molto chiare: il codice lo prendi così com’è, non c’è un supporto o un helpdesk dietro. Non c’è chi fa dei servizi di post-vendita.

C’è solo la community. Questo vuol dire da una parte avere gente con passione che ci dedica del tempo e delle competenze, dall’altra però il tempo può mancare, le risorse possono mancare e quindi anche il supporto in termini di aggiornamenti. Questo però ci porta a…

### Le sponsorizzazioni

I progetti opensource più importanti, penso a Firefox, al kernel di Linux, a LibreOffice, non sono abbandonati a loro stessi ma ci sono realtà private che ne sponsorizzano lo sviluppo.

Prendiamo anche le principali di distribuzioni Linux: accanto a versioni destinate al mondo enterprise, dove il codice del pacchetto opensource è lo stesso, ma vengono cambiate configurazioni e vengono forniti servizi a valore aggiunto, previo pagamento di una fee, ci sono versioni completamente prive di un supporto ufficiale ma praticamente gestite di fatto dalla community, spesso con l’aiuto di dipendenti di queste società che partecipano attivamente alle versioni open.

In particolare [ClamAV](https://www.clamav.net/), il principale antivirus opensource, ha alle spalle il gruppo [Talos Intelligence](https://talosintelligence.com/), parte di Cisco.

### Ok, ma quindi… nel concreto?

La PA sta sostituendo un antivirus e sta suggerendo alle PMI, alle accademie e ai privati di fare lo stesso. Perché non investire i fondi destinati a comprare un altro software chiudo e supportare un progetto come ClamAV? Nulla vieterebbe poi a società di consulenza o ad esempio all’agenzia che governa la sicurezza informatica in Italia, di offrire supporto, essendo parte attiva dello sviluppo stesso.

Investire quindi soldi in un progetto come questo, porterebbe a:

* avere un antivirus dal codice open, su cui si possa fare audit e su cui si possano fare build riproducibili del software
* creare lavoro in termini di team di specialisti dedicati allo sviluppo o alla gestione delle firme ad esempio
* aiutare la comunità opensource ed in generale la comunità internazionale, rendendo bene comune un software così critico

### Off by one

Mi rendo conto che la mia riflessione sia migliorabile e prenda di petto il problema. Mi piacerebbe si alimentasse un’accesa discussione sui punti e soprattutto su come i soldi pubblici possano essere utilizzati, finanziando un progetto che porta benefici a tutti, sia come utilizzatori che come persone che si affacciano al mondo del lavoro che quindi possano venir pagate per contribuire a questo antivirus.

Lasciami un commento per dirmi cosa ne pensi e cosa secondo te potrebbe essere migliorato.

Non vedo l’ora di leggere la tua opinione.

Enjoy it!

04 Apr 2022
(Updated: Dec 16, 2022)

* [Riflessioni](/categories#Riflessioni)

* [#clamav](/tags#clamav)
* [#governo](/tags#governo)
* [#kaspersky](/tags#kaspersky)
* [#opensource](/tags#opensource)
* [#virus](/tags#virus)

Vuoi aiutarmi a portare avanti il progetto [Codice Insicuro](https://codiceinsicuro.it) con una donazione?
Fantastico, allora non ti basta che premere il pulsante qui sotto.

[Supporta il progetto](https://www.buymeacoffee.com/thesp0nge)

---

[« Facciamo behavior-driven development con il C](https://codiceinsicuro.it/2022/04/01/facciamo-behavior-driven-development-con-il-c/)
[Non mettete regole troppo complesse alle vostre password »](https://codiceinsicuro.it/2022/04/16/non-mettete-regole-troppo-complesse-alle-vostre-password/)

---

### Simili a "E se la soluzione al problema dell’antivirus fosse avere il codice open?"

Se questo post ti è piaciuto, sono abbastanza sicuro che troverai questi contenuti altrettanto interessanti. Buona lettura.

![](https://codiceinsicuro.it/assets/images/tesla_crypt.png)

##### Una nuova ondata di ransomware

Hai sul tuo laptop le foto del bimbo, sereno, mentre ti sorride alla festa
dell’asilo. In una cartella, nascosta, hai il frutto di altro genere di
navigazioni. Sorridono sempre, hanno la maggiore età[1](#fn:1) e guardano in camera
con aria birichina mentre aspettano l’idraulico.

1. il porno lo abbiamo guardato tutti. Ci limitiamo al porno che non [↩](#fnref:1)

[Continua la lettura](/blog/una-nuova-ondata-di-ransomware/)

![](https://codiceinsicuro.it/assets/images/stolen_identity.jpg)

##### SPID: con SSL3 e TLS1.0 saremo tutti securizzati

Con fanfare, l’[AGID](http://www.agid.gov.it), l’Agenzia per l’Italia Digitale,
ha annunciato la partenza del progetto
[SPID](http://www.agid.gov.it/agenda-digitale/infrastrutture-architetture/spid),
il Sistema Pubblico per la gestione dell’Identità Digitale.

[Continua la lettura](/blog/spid-con-ssl3-e-tls1-dot-0-saremo-tutti-securizzati/)

![](https://codiceinsicuro.it/assets/images/)

##### Cosa fa un security engineer in SUSE?

Cosa vuol dire essere un product security engineer in SUSE? È facile lavorare completamente da remoto? Ecco com'è cambiata la mia vita da qualche mese...

[Continua la lettura](/2022/05/24/cosa-fa-un-security-engineer-in-suse/)

Please enable JavaScript to view the [comments powered by Disqus.](http://disqus.com/?ref_noscript)
[comments powered by Disqus](http://disqus.co...
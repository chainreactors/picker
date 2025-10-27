---
title: Dipendenze open source, best practices per gli sviluppatori
url: https://www.ictsecuritymagazine.com/notizie/dipendenze-open-source-best-practices-per-gli-sviluppatori/
source: ICT Security Magazine
date: 2022-11-16
fetch_date: 2025-10-03T22:55:07.664458
---

# Dipendenze open source, best practices per gli sviluppatori

[Salta al contenuto](#main)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

* [Home](https://www.ictsecuritymagazine.com/)
* [Articoli](https://www.ictsecuritymagazine.com/argomenti/articoli/)
* RubricheEspandi
  + [Cyber Security](https://www.ictsecuritymagazine.com/argomenti/cyber-security/)
  + [Cyber Crime](https://www.ictsecuritymagazine.com/argomenti/cyber-crime/)
  + [Cyber Risk](https://www.ictsecuritymagazine.com/argomenti/cyber-risk/)
  + [Cyber Law](https://www.ictsecuritymagazine.com/argomenti/cyber-law/)
  + [Digital Forensic](https://www.ictsecuritymagazine.com/argomenti/digital-forensic/)
  + [Digital ID Security](https://www.ictsecuritymagazine.com/argomenti/digital-id-security/)
  + [Business Continuity](https://www.ictsecuritymagazine.com/argomenti/business-continuity/)
  + [Digital Transformation](https://www.ictsecuritymagazine.com/argomenti/digital-transformation/)
  + [Cyber Warfare](https://www.ictsecuritymagazine.com/argomenti/cyber-warfare/)
  + [Ethical Hacking](https://www.ictsecuritymagazine.com/argomenti/ethical-hacking/)
  + [GDPR e Privacy](https://www.ictsecuritymagazine.com/argomenti/gdpr-e-privacy/)
  + [IoT Security](https://www.ictsecuritymagazine.com/argomenti/iot-security/)
  + [Industrial Cyber Security](https://www.ictsecuritymagazine.com/argomenti/industrial-cyber-security/)
  + [Blockchain e Criptovalute](https://www.ictsecuritymagazine.com/argomenti/blockchain-e-criptovalute/)
  + [Intelligenza Artificiale](https://www.ictsecuritymagazine.com/argomenti/intelligenza-artificiale/)
  + [Geopolitica e Cyberspazio](https://www.ictsecuritymagazine.com/argomenti/geopolitica-cyberspazio/)
  + [Interviste](https://www.ictsecuritymagazine.com/argomenti/interviste/)
* [Notizie](https://www.ictsecuritymagazine.com/argomenti/notizie/)
* [Pubblicazioni](https://www.ictsecuritymagazine.com/pubblicazioni/)
* [Cybersecurity Video](https://www.ictsecuritymagazine.com/argomenti/cybersecurity-video/)
* [Eventi](https://www.ictsecuritymagazine.com/eventi/)
* [Newsletter](https://www.ictsecuritymagazine.com/newsletter/)

[Linkedin](https://www.linkedin.com/company/ict-security-magazine/) [YouTube](https://www.youtube.com/%40ictsecuritymagazine1403) [RSS](https://www.ictsecuritymagazine.com/feed/)

[![ICT Security Magazine](https://www.ictsecuritymagazine.com/wp-content/uploads/2016/01/logo-ict-security.jpg)](https://www.ictsecuritymagazine.com/)

Attiva/disattiva menu

[![Forum ICT Security 2025](https://www.ictsecuritymagazine.com/wp-content/uploads/banner-header-2025.jpg)](https://www.ictsecuritymagazine.com/eventi/forumictsecurity2025)

![](https://www.ictsecuritymagazine.com/wp-content/uploads/sicurezza-opebsource.jpg)

# Dipendenze open source, best practices per gli sviluppatori

A cura di:[Redazione](#molongui-disabled-link)  Ore 15 Novembre 2022

Il software open source (OS) è ovunque. Indipendentemente dal settore, ogni azienda fa affidamento sul software per soddisfare le proprie esigenze di business; e la maggior parte delle applicazioni in uso contiene elementi di codice OS. La migrazione verso sempre più complesse applicazioni *cloud-native* fa registrare un aumento del rischio legato alla sicurezza del software, che costringe le organizzazioni a implementare pratiche di gestione delle componenti open source durante l’intero ciclo di vita dello sviluppo del software (SLDC – Software Development Life Cycle) e ad adottare gli strumenti corretti per gestire i rischi correlati.

La formazione degli sviluppatori alla sicurezza open source e l’implementazione di validi strumenti di analisi della composizione del software (SCA) sono entrambi passaggi cruciali per proteggere il codice rispetto ai rischi veicolati dal software open source.

### “Software risk is real”

Il [**rapporto OSSRA 2022**](https://www.synopsys.com/software-integrity/resources/analyst-reports/open-source-security-risk-analysis.html?cmp=pr-sig&amp;utm_medium=referral) offre alcuni spunti essenziali sull’ampia adozione del software open source e sui relativi rischi per la sicurezza. In esso vengono infatti esaminati 17 settori industriali, quattro dei quali – hardware per computer e semiconduttori, sicurezza informatica, energia e tecnologia pulita, *Internet of Things* – contenevano **componenti open source n****el 100% del codice analizzato**; nei restanti settori, la percentuale di elementi open source all’interno del codice risultava compresa tra il 93% e il 99%.

Il rapporto rileva che, sebbene i conflitti di licenza appaiano diminuiti (sono state riscontrate problematiche nel 53% del codice, mentre nel 2020 si raggiungeva il 65%) aumentano i casi di dipendenze non esaminate: ovvero, quando gli sviluppatori introducono dipendenze open source spesso non sono a conoscenza delle sotto-dipendenze contenenti ulteriori termini e condizioni di licenza. Ad esempio, alcune versioni del popolare componente node.js includono una dipendenza che sfrutta il codice concesso ai sensi della licenza CC-SA 3, la quale potrebbe imporre requisiti indesiderati e richiedere una valutazione legale rispetto ai potenziali problemi di IP.

Sebbene la [**diminuzione dei conflitti di licenza e delle vulnerabilità ad alto rischio**](https://www.synopsys.com/blogs/software-security/manage-license-compliance-with-black-duck/?cmp=pr-sig&amp;utm_medium=referral) appaia incoraggiante, resta il fatto che più della metà dei codici sorgente controllati conteneva conflitti di licenza e includeva, in percentuali simili, vulnerabilità ad alto rischio. C’è un dato ancora più preoccupante: tra i 2.097 codici sorgente controllati per cui erano state anche eseguite valutazioni del rischio, **l’88% conteneva versioni obsolete di componenti open source.** In altre parole i necessari aggiornamenti o *patch*, pur disponibili, non erano stati applicati.

Senza esplorare le diverse ragioni che spingono a non mantenere aggiornato il software, una possibile soluzione che eviti problemi futuri all’organizzazione è realizzare un inventario accurato e aggiornato dell’open source utilizzato all’interno del codice, visto che un componente non aggiornato può essere ignorato fino a quando non risulti vulnerabile a un *exploit* ad alto rischio.

Questo è esattamente ciò che è successo con [**Log4j**](https://www.synopsys.com/blogs/software-security/mitigating-impact-of-log4j-log4shell/?cmp=pr-sig&amp;utm_medium=referral). Sebbene l’*exploit* fosse effettivamente pericoloso, il panico e la perdita di clienti che ne sono derivati sono stati in gran parte causati dalle organizzazioni che non sapevano dove si trovasse Log4j all’interno dei loro sistemi e applicazioni: diverse di esse, infatti, hanno faticato innanzitutto per controllare se fosse presente o meno.

### Gestire le dipendenze open source: best practice preventive

Stabilire un programma completo di gestione del software open source può sembrare un’impresa talmente ardua da apparire scoraggiante, ma esistono alcune *best practice* che possono aiutarti a iniziare.

Prevedere una corretta governance del software aiuta a proteggere le risorse e i dati della tua organizzazione, evitando i problemi che sorgono quando viene annunciata una vulnerabilità zero-day: ciò implica la definizione di una strategia, l’impostazione di un processo di approvazione e l’esecuzione di un audit completo circa le dipendenze legate al software open source.

### 1. Definisci una strategia

La creazione di una policy open source per la tua organizzazione riduce al minimo i rischi legali, tecnici ed economici derivanti dall’utilizzo di software open source. Policy e programmi di governance possono concentrarsi sia sull’impiego del codice open source nel processo di sviluppo sia sull’utilizzo del software stesso, così facilitando, ad esempio, le operazioni e il supporto del reparto IT. Alcune organizzazioni creano persino un ufficio dedicato a gestire qualsiasi attività coin...
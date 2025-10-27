---
title: Text4Shell: grave vulnerabilità in Apache, ma non sarà una nuova Log4Shell. C’è la patch
url: https://www.cybersecurity360.it/news/text4shell-grave-vulnerabilita-in-apache-ma-non-sara-una-nuova-log4shell-ce-la-patch/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-22
fetch_date: 2025-10-03T20:37:46.269558
---

# Text4Shell: grave vulnerabilità in Apache, ma non sarà una nuova Log4Shell. C’è la patch

[Vai al contenuto principale](#main-content)
[Vai al footer](#footer-content)

![logo](data:image/png;base64...)![logo](https://cdnd360.it/networkdigital360/nd360-neg.svg)

[I NOSTRI SERVIZI](https://www.cybersecurity360.it/about-network)

Menu

[![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_logo-768x55.png)](https://www.cybersecurity360.it)

## Text4Shell: grave vulnerabilità in Apache, ma non sarà una nuova Log4Shell. C’è la patch

* [Cybersecurity Nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* Malware e attacchi
  + [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
  + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)
* Norme e adeguamenti
  + [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)
* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
* [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
* [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
* [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
* [Chi siamo](https://www.cybersecurity360.it/about/)

* [![Vai alla homepage di CyberSecurity](data:image/png;base64...)![Vai alla homepage di CyberSecurity](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2024/03/cybersecurity_neg_logo-768x55.png)](https://www.cybersecurity360.it)
* Seguici
* + [twitter](https://twitter.com/Cybersec360)
  + [linkedin](https://www.linkedin.com/company/cybersecurity360/)
  + [Newsletter](https://www.cybersecurity360.it/newsletter-signin/)
  + [Rss Feed](#rssModal)
  + [Chi siamo](https://www.cybersecurity360.it/about)
* AREA PREMIUM
* [Whitepaper](https://www.cybersecurity360.it/whitepaper/)
* [Eventi](https://www.cybersecurity360.it/eventi/)
* [Webinar](https://www.cybersecurity360.it/webinar/)
* CANALI
* [Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
* [Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
* + [Ransomware](https://www.cybersecurity360.it/nuove-minacce/ransomware/)* [Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
  * + [Privacy e Dati personali](https://www.cybersecurity360.it/legal/privacy-dati-personali/)* [Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
    * [Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
    * [L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
    * [News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
    * [Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
    * [Chi siamo](https://www.cybersecurity360.it/about/)

[Cybersecurity nazionale](https://www.cybersecurity360.it/cybersecurity-nazionale/)
[Malware e attacchi](https://www.cybersecurity360.it/nuove-minacce/)
[Norme e adeguamenti](https://www.cybersecurity360.it/legal/)
[Soluzioni aziendali](https://www.cybersecurity360.it/soluzioni-aziendali/)
[Cultura cyber](https://www.cybersecurity360.it/cultura-cyber/)
[L'esperto risponde](https://www.cybersecurity360.it/esperto-risponde/)
[News, attualità e analisi Cyber sicurezza e privacy](https://www.cybersecurity360.it/news/)
[Corsi cybersecurity](https://www.cybersecurity360.it/corsi-cybersecurity/)
[Chi siamo](https://www.cybersecurity360.it/about/)

Nuove minacce

# Text4Shell: grave vulnerabilità in Apache, ma non sarà una nuova Log4Shell. C’è la patch

* [Home](https://www.cybersecurity360.it)
* [News, attualità e analisi sulla Cyber sicurezza](https://www.cybersecurity360.it/news/)

Una nuova vulnerabilità in Apache, identificata nella libreria open source Commons Text, allarma gli amministratori IT, ma l’impatto non sembra essere paragonabile a quello provocato da Log4j. Inoltre, c’è già l’aggiornamento. Ecco tutti i dettagli e come mitigare il rischio

Pubblicato il 21 Ott 2022

[Dario Fadda](https://www.cybersecurity360.it/giornalista/dario-fadda/)

Research Infosec, fondatore Insicurezzadigitale.com

![Text4Shell: grave vulnerabilità in Apache, ma non sarà una nuova Log4Shell. C’è la patch](data:image/png;base64...)![Text4Shell: grave vulnerabilità in Apache, ma non sarà una nuova Log4Shell. C’è la patch](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2022/10/Apache1212.png)

È stata ribattezzata **Text4Shell** (nome che rievoca la [ben più pericolosa Log4Shell](https://www.cybersecurity360.it/nuove-minacce/log4j-una-vulnerabilita-endemica-che-persistera-negli-anni-raccomandazioni-per-mitigarla/)) l’**importante vulnerabilità** in **Apache Commons Text** corretta con l’aggiornamento della **libreria open source** alla versione 1.10.0.

La vulnerabilità Text4Shell, tracciata come [CVE-2022-42889](https://nvd.nist.gov/vuln/detail/CVE-2022-42889) e classificata con un indice di gravità CVSS di 9.8 su 10.0, è di tipo RCE (esecuzione di codice in modalità remota) e potrebbe consentire a un attaccante di eseguire codice arbitrario sul computer target e compromettere l’intero host.

Ricordiamo che Apache Commons Text è una libreria Java con un “sistema di interpolazione” che consente agli sviluppatori di modificare, decodificare, generare ed eseguire l’escape in base alla ricerca di stringhe.

Indice degli argomenti

* [Che cos’è Text4Shell](#Che_cose_Text4Shell)
  + [Come si può sfruttare Text4Shell](#Come_si_puo_sfruttare_Text4Shell)
* [Come mitigare il rischio di sfruttamento](#Come_mitigare_il_rischio_di_sfruttamento)

## Che cos’è Text4Shell

La vulnerabilità, che è stata scoperta per la prima volta il 9 marzo 2022, interessa varie versioni della libreria open source Apache Commons Text comprese tra la 1.5 e la 1.9 ed è causata da uno script di convalida non sicura da parte del sistema di interpolazione che potrebbe attivare l’esecuzione di codice durante l’elaborazione di input dannosi nella configurazione predefinita della libreria.

Come dicevamo, il nome con il quale è stata battezzata quest’ultima vulnerabilità è sicuramente evocativo della recente [Log4Shell](https://www.cybersecurity360.it/soluzioni-aziendali/log4j-una-vulnerabilita-endemica-che-persistera-negli-anni-raccomandazioni-per-mitigarla/), exploit d’impatto globale e persistente sulla libreria Apache Log4j. Tuttavia, è doveroso sottolineare come non sia facilmente sfruttabile come il bug di Log4j. Secondo il ricercatore di sicurezza Sean Wright e il ricercatore di GitHub Security Lab Alvaro Munoz, che hanno scoperto la vulnerabilità a marzo, si prevede che tale difetto sarà anche meno diffuso poiché l’utilizzo di Commons Text è inferiore rispetto a Log4j.

“Per la natura della vulnerabilità si evince che, a differenza di Log4Shell, sarà raro che un’applicazione utilizzi il componente vulnerabile di Commons Text per elaborare input non attendibili e potenzialmente dannosi”, ha affermato Rapid7 in un suo report.

### Come si può sfruttare Text4Shell

Nell’exploit, sostanzialmente verrebbe utilizzato il comando “netcat”(nc) per aprire una shell inversa sull’applicazione vulnerabile. Il payload viene costruito con l’abuso della ricerca di stringhe, ovvero “${prefix:name}.

![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2022/10/Screenshot-2022-10-21-at-00-05-42-Detecting-and-mitigating-CVE-2022-42889-a-k-a-Text4shell-%E2%80%93-Sysdig.png)![](https://dnewpydm90vfx.cloudfront.net/wp-content/uploads/2022/10/Screenshot-2022-10-21-at-00-05-42-Detecting-and-mitigating-CVE-2022-42889-a-k-a-Text4shell-%E2%80%93-Sysdig.png)

## Come mitigare il rischio di sfruttamento

Come detto, Apache ha rilasciato un aggiornamento della libreria che risolve il problema. Inoltre, è bene far notare che sebbene questa vulnerabilità sia rimasta non corretta per sette mesi, non sono apparsi casi di sfruttamento no...
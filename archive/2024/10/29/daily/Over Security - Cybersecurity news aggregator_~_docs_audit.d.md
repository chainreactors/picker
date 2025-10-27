---
title: ~/docs/audit.d
url: https://blog.lobsec.com/2024/04/configurare-auditd/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-29
fetch_date: 2025-10-06T18:53:39.897818
---

# ~/docs/audit.d

[Vai al contenuto](#content "Vai al contenuto")

[Lobsec](https://blog.lobsec.com/)

Yet another security blog

Menu

Menu

* [CV (ITA)](https://blog.lobsec.com/cv-ita/)
* [Privacy policy](https://blog.lobsec.com/privacy-policy/)

# ~/docs/audit.d

2024-04-11 di [lobst3r](https://blog.lobsec.com/author/lobst3r/ "Visualizza tutti gli articoli di lobst3r")

## Introduzione

La sicurezza dei server Linux è fondamentale per la protezione dei dati e la continuità del business. Auditd rappresenta un potente strumento per aumentare la visibilità e la profondità dei log di sistema, fornendo informazioni dettagliate sulle attività svolte sul server. In questo articolo, esploreremo il funzionamento di auditd e come utilizzarlo per rafforzare la sicurezza del tuo ambiente Linux.

## Funzionalità

* Registrazione di eventi: Auditd registra una vasta gamma di eventi, tra cui accessi ai file, chiamate di sistema, modifiche alle configurazioni e attività di login/logout.
* Filtraggio e analisi: è possibile definire regole per specificare quali eventi devono essere registrati e come analizzarli.
* Generazione di report: Auditd può generare report dettagliati in diversi formati, facilitando l’analisi e l’identificazione di potenziali minacce.

## Pre installazione

Installare prima il pacchetto `audispd-plugins` per la spedizione degli eventi.

```
dnf install audispd-plugins
```

Successivamente, **anche se non strettamente indispensabile**, si potrebbe andare a modificare il rate-limit di systemd-journald. Questo sarebbe da fare se il server ha un numero molto ingente di log da processare. Per fare ciò modificare il file `/etc/systemd/journald.conf` e andare a modificare le direttive

```
#RateLimitInterval=30s
#RateLimitBurst=1000
```

in

```
RateLimitInterval=0
RateLimitBurst=0
```

Uscire e salvare e riavviare il systemd-journald con

```
systemctl restart systemd-journald
```

Analogamente andare ad editare il file di rsyslog e aggiungere le direttive sotto riportate subito dopo il caricamento del modulo imjournal

```
module(load="imjournal"             # provides access to the systemd journal
       StateFile="imjournal.state") # File to store the position in the journal

$imjournalRatelimitInterval 0
$imjournalRatelimitBurst 0
```

in questa maniera si disabilitano i limiti di invio file. Poi, riavviare il servizio rsyslog con il comando

```
systemctl restart rsyslog
```

## Installazione

##### Testata su Ubuntu 20.04, CentOS 7.x

Per prima cosa è importante controllare se auditd è installato e in esecuzione, per farlo

```
# systemctl status auditd
● auditd.service - Security Auditing Service
     Loaded: loaded (/usr/lib/systemd/system/auditd.service; enabled; preset: enabled)
     Active: active (running) since Thu 2024-04-11 11:17:26 CEST; 6s ago
       Docs: man:auditd(8)
             https://github.com/linux-audit/audit-documentation
    Process: 2018797 ExecStart=/sbin/auditd (code=exited, status=0/SUCCESS)
    Process: 2018803 ExecStartPost=/sbin/augenrules --load (code=exited, status=0/SUCCESS)
   Main PID: 2018798 (auditd)
      Tasks: 4 (limit: 11025)
     Memory: 6.3M
        CPU: 288ms
     CGroup: /system.slice/auditd.service
             ├─2018798 /sbin/auditd
             └─2018800 /usr/sbin/sedispatch
```

Successivamente bisogna andare ad editare il file `/etc/audit/plugins.d/syslog.conf` (su Debian/CentOS 7.x e derivate il file è `/etc/audisp/plugins.d/syslog.conf`) il quale specifica le direttive con le quali i log vengono inviati al syslog. Nel mio caso ho deciso di inviare lo stram dei log su una facility.

```
active = yes
direction = out
path = builtin_syslog
type = builtin
args = LOG_LOCAL6
format = string
```

Modificare il syslog (su RHEL e derivate il file è `/etc/rsyslog.conf` su Debian e derivate il file è `/etc/rsyslog.d/50-default.conf`) andando ad aggiungere la direttiva

```
local6.*    @@ip-del-SIEM
```

## Installazione

##### Testata su Alma Linux 9.x

L’unica differenza è dettata dal file del plugin `syslog.conf` il quale deve essere modificato in questa maniera

```
active = yes
direction = out
path = /sbin/audisp-syslog
args = LOG_LOCAL6
format = string
```

## Auditd rules

Arrivati a questo punto è importante andare a definire le regole che auditd utilizzerà per loggare gli eventi. Una buona base di partenza è possibile trovarla a [questo](https://github.com/Neo23x0/auditd) indirizzo.

### I file audit.rules

Il file `audit.rules` è un file di configurazione per il sistema di audit di Linux, `auditd`. Questo sistema registra gli eventi di sicurezza del sistema, come l’accesso ai file, l’esecuzione di comandi e le modifiche alle configurazioni. Il file `audit.rules` specifica quali eventi devono essere registrati e come devono essere registrati.

Il file è suddiviso in sezioni, ognuna delle quali definisce un set di regole per un particolare tipo di evento. Alcune delle sezioni più importanti includono:

* **audit\_defaults:** Questa sezione definisce le impostazioni predefinite per tutte le regole.
* **syscalls:** Questa sezione definisce le regole per gli eventi di syscall, che sono le chiamate che i programmi fanno al kernel.
* **files:** Questa sezione definisce le regole per gli eventi relativi ai file, come l’accesso ai file, la modifica dei file e l’eliminazione dei file.
* **users:** Questa sezione definisce le regole per gli eventi relativi agli utenti, come l’accesso al sistema, l’esecuzione di comandi e la modifica delle configurazioni.
* **processes:** Questa sezione definisce le regole per gli eventi relativi ai processi, come la creazione di processi, la terminazione di processi e la modifica delle priorità dei processi.

## Nella pratica

Andare nella directory `/etc/audit/rules.d` e creare un nuovo file chiamato `audit.rules` ed incollare il contenuto presente nel [repository](https://raw.githubusercontent.com/Neo23x0/auditd/master/audit.rules) (il file originale può essere eliminato in quanto le informazioni presenti sono riportate anche nel file che verrà sostituito).

In ultima battuta riavviare auditd con

```
service auditd restart
```

e successivamente riavviare rsyslog

```
systemctl restart rsyslog
```

Happy logging!

EOF

Categorie [blue team](https://blog.lobsec.com/category/blue-team/), [cyber](https://blog.lobsec.com/category/cyber/), [tips](https://blog.lobsec.com/category/tips/), [tutorial](https://blog.lobsec.com/category/tutorial/) Tag [audit](https://blog.lobsec.com/tag/audit/), [auditd](https://blog.lobsec.com/tag/auditd/), [login](https://blog.lobsec.com/tag/login/), [siem](https://blog.lobsec.com/tag/siem/), [ssh](https://blog.lobsec.com/tag/ssh/), [syslog](https://blog.lobsec.com/tag/syslog/)

[./cve/CVE-2024-3094/xz.wtf](https://blog.lobsec.com/2024/04/cve-2024-3094-su-xz-utils/)

[MadLicense](https://blog.lobsec.com/2024/08/madlicense/)

### Lascia un commento [Annulla risposta](/2024/04/configurare-auditd/#respond)

Commento

Nome
Email
Sito web

[ ]  Salva il mio nome, email e sito web in questo browser per la prossima volta che commento.

Δ

* [Analisi di un dropper HTML/JS per Internet Explorer basato su ActiveX e regsvr32](https://blog.lobsec.com/2025/08/analisi-di-un-dropper-html-js-per-internet-explorer-basato-su-activex-e-regsvr32/)
* [Kekpi trojan dissection](https://blog.lobsec.com/2025/03/kekpi-malware-dissection/)
* [NIS2: il caos di cui non avevamo (forse) bisogno](https://blog.lobsec.com/2024/12/nis2-il-caos-di-cui-non-avevamo-forse-bisogno/)
* [~/news/blocklist.news](https://blog.lobsec.com/2024/10/blocklist-ioc-updated/)
* [~/tips/fortigate\_malware.feed](https://blog.lobsec.com/2024/10/fortigate-malware-feed/)
* [/usr/bin/touch nuova\_era](https://blog.lobsec.com/2024/10/lobsec-nuova-era/)

© 2025 Lobsec • Creato con [GeneratePress](https://generatepress.com)

Manage Consent

To provide the best experiences, we use technologies like cookies to store and/or access device information. Consenting to these technologies will allow us to process data such as bro...
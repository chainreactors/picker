---
title: Una soluzione temporanea ai problemi di Exchange Online in Outlook
url: https://www.securityinfo.it/2022/10/20/una-soluzione-temporanea-ai-problemi-di-exchange-online-in-outlook/?utm_source=rss&utm_medium=rss&utm_campaign=una-soluzione-temporanea-ai-problemi-di-exchange-online-in-outlook
source: Over Security - Cybersecurity news aggregator
date: 2022-10-21
fetch_date: 2025-10-03T20:31:19.554995
---

# Una soluzione temporanea ai problemi di Exchange Online in Outlook

Aggiornamenti recenti Ottobre 1st, 2025 2:22 PM

* [Registrati](https://www.securityinfo.it/registrazione/)
* Login
* Filtro

# [![](https://securityinfo.it/wp-content/uploads/2016/08/LogoSquadrato_750px-1.jpg)](https://www.securityinfo.it)

### partner

[![In collaborazione con](https://www.securityinfo.it/wp-content/uploads/2025/06/Security_empty-1.jpg)](https://securityinfo.it/partner "partner")

### News Recenti

* [Transparency Center Initiative di Kaspersky Lab: cosa significa per l’Italia](https://www.securityinfo.it/2019/01/18/transparency-center-initiative-di-kaspersky-lab-cosa-significa-per-litalia/)
* [Il 60% dei firewall non supera i controlli di conformità: la ricerca di FireMon](https://www.securityinfo.it/2025/10/01/il-60-dei-firewall-non-supera-i-controlli-di-conformita-la-ricerca-di-firemon/)
* [Scoperto ShadowLeak, un attacco che sfrutta un bug zero-click di ChatGPT](https://www.securityinfo.it/2025/09/30/scoperto-shadowleak-un-attacco-che-sfrutta-un-bug-zero-click-di-chatgpt/)
* [Firewall Cisco sotto attacco: una nuova campagna prende di mira i device ASA](https://www.securityinfo.it/2025/09/29/firewall-cisco-sotto-attacco-una-nuova-campagna-prende-di-mira-i-device-asa/)
* [CERT-AGID 20–26 settembre: phishing, malware e PEC compromesse](https://www.securityinfo.it/2025/09/29/cert-agid-20-26-settembre-phishing-malware-e-pec-compromesse/)
* [Nuova variante del malware XCSSET prende di mira gli sviluppatori Xcode su macOS](https://www.securityinfo.it/2025/09/26/nuova-variante-del-malware-xcsset-prende-di-mira-gli-sviluppatori-xcode-su-macos/)

* [Home](https://www.securityinfo.it)
* [News](https://www.securityinfo.it/category/news/)
* [Approfondimenti](https://www.securityinfo.it/category/approfondimenti/)
* [Opinioni](https://www.securityinfo.it/category/opinioni/)
* [Top Malware](https://www.securityinfo.it/top-malware-page/)
* [Minacce](https://www.securityinfo.it/category/minacce-2/)
* [Guide alla sicurezza](http://www.securityinfo.it/guide-alla-sicurezza/)
* [Podcast](https://www.securityinfo.it/podcast-page/)
* [Strumenti Utili](https://www.securityinfo.it/category/strumenti-utili/)

* Search for:

## Una soluzione temporanea ai problemi di Exchange Online in Outlook

Ott 20, 2022  [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/ "Articoli scritti da Dario Orlandi")
 [News](https://www.securityinfo.it/category/news/), [RSS](https://www.securityinfo.it/category/rss/)
 [0](https://www.securityinfo.it/2022/10/20/una-soluzione-temporanea-ai-problemi-di-exchange-online-in-outlook/#respond)

---

Microsoft è al lavoro per risolvere un problema noto che **impedisce la configurazione degli account Exchange Online** nella versione Windows di Outlook.

Quando si effettua il test di connessione di Outlook dopo aver inserito le informazioni di configurazione, in alcuni casi il software restituisce un errore con **codice 603**, accompagnato dal messaggio “*Deleted objects will not be found with a session scoped to TenantLocal or AllTenants, unless search is scoped to Deleted Objects container”.*

![](https://www.securityinfo.it/wp-content/uploads/2022/10/Outlook-603-error-code.jpg)

Il dettaglio dell’errore riportato da Outlook

L’azienda di Redmond ha individuato l’origine del problema e distribuirà presto una patch per eliminare l’errore, ma già oggi propone una [**soluzione temporanea**](https://support.microsoft.com/it-it/topic/can-t-configure-exchange-online-mailbox-in-outlook-desktop-1acf6010-b356-48da-8036-94d2625670df) che permette agli amministratori It di risolvere il problema in modo manuale.

I passaggi suggeriti sono i seguenti:

1. Connettersi a Exchange Online PowerShell, seguendo [queste istruzioni](https://learn.microsoft.com/it-it/powershell/exchange/connect-to-exchange-online-powershell?view=exchange-ps).
2. Verificare che Get-Mailbox punti effettivamente SharingPolicy a un oggetto eliminato, con il comando: *Get-Mailbox -ResultSize 10 |fl \*sharingpol\**
3. Ripristinare Default SharingPolicy con il comando: *New-SharingPolicy -Name “Default Sharing Policy” -Domains ‘\*:CalendarSharingFreeBusySimple’, ‘Anonymous:CalendarSharingFreeBusyReviewer’ -Enabled:$true -Default:$true*
4. Verificare che SharingPolicy non indichi più un oggetto eliminato, digitando: *Get-Mailbox -ResultSize 10 |fl \*sharingpol\**

Dopo aver completato questa sequenza di comandi, la configurazione della casella postale in Outlook dovrebbe riprendere a funzionare come previsto.

Condividi l'articolo

* [Tweet](https://twitter.com/share)

---

* [errore](https://www.securityinfo.it/tag/errore/), [Exchange](https://www.securityinfo.it/tag/exchange/), [Exchange Online](https://www.securityinfo.it/tag/exchange-online/), [Microsoft](https://www.securityinfo.it/tag/microsoft/), [Outlook](https://www.securityinfo.it/tag/outlook/), [workaround](https://www.securityinfo.it/tag/workaround/)

[Apache Commons Text ha un bug: torna l'incubo Log4Shell](https://www.securityinfo.it/2022/10/20/apache-commons-text-bug-log4shell/)
[DeadBolt: la polizia tedesca recupera 150 chiavi di decrittazione](https://www.securityinfo.it/2022/10/20/deadbolt-ransomware-chiavi-decrittazoine/)

---

![](https://secure.gravatar.com/avatar/9ba6108fae91c2be66a7ef45ac2db49a?s=90&d=mm&r=g)

##### [Dario Orlandi](https://www.securityinfo.it/author/dario-orlandi/)

##### Articoli correlati

* [![Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP](https://www.securityinfo.it/wp-content/uploads/2025/08/Gemini_Generated_Image_jk74qwjk74qwjk74-120x85.png)](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/ "Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP")

  [Secret Blizzard attacca le ambasciate...](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/ "Permanent link to Secret Blizzard attacca le ambasciate straniere a Mosca tramite gli ISP")

  Ago 01, 2025  [0](https://www.securityinfo.it/2025/08/01/secret-blizzard-attacca-le-ambasciate-straniere-a-mosca-tramite-gli-isp/#respond)
* [![Grave alerta SharePoint: attacco in corso che elude le difese](https://www.securityinfo.it/wp-content/uploads/2025/07/SharePoint_lug-2025CG-120x85.png)](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/ "Grave alerta SharePoint: attacco in corso che elude le difese")

  [Grave alerta SharePoint: attacco in...](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/ "Permanent link to Grave alerta SharePoint: attacco in corso che elude le difese")

  Lug 21, 2025  [0](https://www.securityinfo.it/2025/07/21/grave-alerta-per-sharepoint-toolshell-e-un-attacco-in-corso-che-elude-le-difese-tradizionali/#respond)
* [![Windows 10: ancora un anno di aggiornamenti (quasi) gratis](https://www.securityinfo.it/wp-content/uploads/2025/06/Windows_10_version_22H2_Update_screen-120x85.png)](https://www.securityinfo.it/2025/06/25/windows-10-ancora-un-anno-di-aggiornamenti-quasi-gratis/ "Windows 10: ancora un anno di aggiornamenti (quasi) gratis")

  [Windows 10: ancora un anno di...](https://www.securityinfo.it/2025/06/25/windows-10-ancora-un-anno-di-aggiornamenti-quasi-gratis/ "Permanent link to Windows 10: ancora un anno di aggiornamenti (quasi) gratis")

  Giu 25, 2025  [0](https://www.securityinfo.it/2025/06/25/windows-10-ancora-un-anno-di-aggiornamenti-quasi-gratis/#respond)
* [![Microsoft rilascia patch per 67 bug, di cui uno già sfruttato](https://www.securityinfo.it/wp-content/uploads/2025/06/Gemini_Generated_Image_xaqqtnxaqqtnxaqq-scaled-120x85.jpg)](https://www.securityinfo.it/2025/06/11/microsoft-rilascia-patch-per-67-bug-di-cui-uno-gia-sfruttato/ "Microsoft rilascia patch per 67 bug, di cui uno già sfruttato")

  [Microsoft rilascia patch per 67 bug, di...](https://www.securityinfo....
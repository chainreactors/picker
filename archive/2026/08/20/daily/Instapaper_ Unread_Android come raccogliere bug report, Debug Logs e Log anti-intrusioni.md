---
title: Android come raccogliere bug report, Debug Logs e Log anti-intrusioni
url: https://www.forenser.it/android-come-raccogliere-bug-report-debug-logs-e-log-anti-intrusioni/
source: Instapaper: Unread
date: 2026-08-20
fetch_date: 2026-08-21T03:05:07.953045
---

# Android come raccogliere bug report, Debug Logs e Log anti-intrusioni

Search for:

 Search

Menu

Close

* [Servizi](https://www.forenser.it/servizi-informatica-forense/)
* [Formazione](https://www.forenser.it/formazione/)
* [News](https://www.forenser.it/news/)
* [Staff](https://www.forenser.it/staff/)
* [Press](https://www.forenser.it/press/)
  + [Video e TV](https://www.forenser.it/press/video-tv/)
  + [Radio](https://www.forenser.it/press/radio/)
  + [Quotidiani e Periodici](https://www.forenser.it/press/quotidiani-e-periodici/)
* [Guide](https://www.forenser.it/category/guide/)
* [Contatti](https://www.forenser.it/contatti/)
  + [Cookie Policy](https://www.forenser.it/contatti/cookie-policy/)
  + [Privacy Policy](https://www.forenser.it/contatti/privacy-policy/)

Search for:

 Search

[![Forenser Srl](https://www.forenser.it/wp-content/uploads/forenser-digital-investigations.png)](https://www.forenser.it/)

[Forenser Srl](https://www.forenser.it/)

Studio Informatica Forense

* [Servizi](https://www.forenser.it/servizi-informatica-forense/)
* [Formazione](https://www.forenser.it/formazione/)
* [News](https://www.forenser.it/news/)
* [Staff](https://www.forenser.it/staff/)
* [Press](https://www.forenser.it/press/)
  + [Video e TV](https://www.forenser.it/press/video-tv/)
  + [Radio](https://www.forenser.it/press/radio/)
  + [Quotidiani e Periodici](https://www.forenser.it/press/quotidiani-e-periodici/)
* [Guide](https://www.forenser.it/category/guide/)
* [Contatti](https://www.forenser.it/contatti/)
  + [Cookie Policy](https://www.forenser.it/contatti/cookie-policy/)
  + [Privacy Policy](https://www.forenser.it/contatti/privacy-policy/)

# Android: come raccogliere bug report, Debug Logs e Log anti-intrusioni

[![](https://secure.gravatar.com/avatar/65af508883433ee06fa507bcdcb1e77747fc2aba840a2130e6877e5be7ffdded?s=44&d=mm&r=g)](https://www.forenser.it/author/forenser/ "Posts by forenser")

[forenser](https://www.forenser.it/author/forenser/)
on
19 Agosto 2026

![](https://www.forenser.it/wp-content/uploads/bug_pulita-1-1024x576.png)

Durante un’analisi, un incidente o una semplice attività di assistenza tecnica può essere necessario raccogliere informazioni diagnostiche da uno smartphone Android.

A differenza di iPhone e iPad, Android non dispone di un singolo archivio perfettamente equivalente al sysdiagnose, il pacchetto diagnostico unico dei dispositivi Apple. Le fonti principali sono tre:

* il bug report, che raccoglie in un archivio lo stato diagnostico del dispositivo;
* i Debug Logs, ottenuti tramite logcat, utili per osservare ciò che accade durante un problema;
* il Log anti-intrusioni, introdotto con Android 16 per conservare nel tempo eventi rilevanti per la sicurezza.

Sono strumenti complementari e non intercambiabili.

Table of Contents

Toggle

* [Generare un bug report dal dispositivo](#Generare_un_bug_report_dal_dispositivo)
* [Generare il bug report da computer con ADB](#Generare_il_bug_report_da_computer_con_ADB)
* [Raccogliere i Debug Logs con logcat](#Raccogliere_i_Debug_Logs_con_logcat)
* [Il nuovo Log anti-intrusioni di Android 16](#Il_nuovo_Log_anti-intrusioni_di_Android_16)
* [Attivare ed esportare il Log anti-intrusioni](#Attivare_ed_esportare_il_Log_anti-intrusioni)
* [Alcuni limiti da conoscere](#Alcuni_limiti_da_conoscere)
* [Come condividere i file](#Come_condividere_i_file)

## Generare un bug report dal dispositivo

Il bug report è un archivio .zip che raccoglie log di sistema, crash, informazioni sui processi e altri dati tecnici prodotti dai componenti interni del sistema. Le dimensioni possono variare da alcune decine a diverse centinaia di MB, in base al dispositivo e ai dati disponibili.

Può essere utile per analizzare crash, blocchi, errori ANR (le app che si bloccano senza rispondere), consumi energetici anomali, problemi di rete e altri comportamenti inattesi.

Per generarlo direttamente dal dispositivo è necessario attivare le Opzioni sviluppatore, un menu nascosto di funzioni avanzate.

Nella maggior parte dei dispositivi:

1. aprite Impostazioni > Informazioni sul telefono;
2. individuate la voce Numero build;
3. toccatela sette volte;
4. inserite il PIN, se richiesto.

Successivamente:

1. aprite Impostazioni > Sistema > Opzioni sviluppatore;
2. selezionate Crea report bug, Segnalazione bug o una voce equivalente;
3. se vengono proposte due varianti, il Report interattivo è adatto alla maggior parte dei casi e permette di aggiungere dettagli e screenshot; il Report completo include tutte le sezioni diagnostiche, ma non permette queste integrazioni: sceglietelo quando chi riceverà il file lo richiede espressamente;
4. avviate la raccolta.

La raccolta richiede qualche minuto: al termine comparirà una notifica attraverso la quale sarà possibile salvare o condividere l’archivio.

Su Pixel e su alcuni altri dispositivi, sempre nelle Opzioni sviluppatore, è disponibile anche la Scorciatoia segnalazione bug: aggiunge la voce al menu di accensione e consente di avviare la raccolta nel momento esatto in cui il problema si manifesta, senza dover navigare nei menu. Sui Pixel recenti il menu si apre premendo insieme Accensione e Volume Su, come indicato nella [guida Pixel](https://support.google.com/pixelphone/answer/6398243?hl=it).

Il nome del file sarà generalmente simile a:

```
bugreport-BUILD_ID-DATE.zip
```

dove al posto di BUILD\_IDeDATE troverete la versione del software e la data di creazione.

Il percorso e il nome delle opzioni possono variare in base al produttore. La procedura generale è documentata da [Android Developers](https://developer.android.com/studio/debug/bug-report).

## Generare il bug report da computer con ADB

Il bug report può essere generato anche da computer, su macOS, Linux o Windows, tramite ADB (Android Debug Bridge): è lo strumento a riga di comando con cui il computer dialoga con un dispositivo Android, ed è incluso negli [SDK Platform Tools ufficiali di Google](https://developer.android.com/tools/releases/platform-tools). Non serve installare nulla: scaricate l’archivio, estraetelo e aprite il Terminale nella cartella appena estratta. Su Windows il modo più rapido è digitare cmd nella barra degli indirizzi di quella cartella e premere Invio; su Mac si fa clic destro sulla cartella e si sceglie “Nuovo terminale nella cartella”.

Negli esempi successivi viene utilizzato adb. Su macOS e Linux, se state eseguendo il programma direttamente dalla cartella estratta, sostituitelo con ./adb, per esempio ./adb devices.

Sul dispositivo:

1. abilitate Debug USB nelle Opzioni sviluppatore: è l’interruttore che consente al computer di comunicare con lo smartphone;
2. collegate lo smartphone al computer via USB;
3. sbloccatelo;
4. confermate la richiesta di autorizzazione che compare sullo schermo: l’impronta RSA mostrata identifica il computer che state autorizzando, quindi accettatela solo se siete voi ad aver appena collegato il dispositivo al vostro computer.

Dal computer verificate che il dispositivo sia visibile:

```
adb devices
```

Se tutto è a posto comparirà il numero di serie dello smartphone seguito dalla parola device. Se invece compare unauthorized, sbloccate lo smartphone e confermate l’autorizzazione.

A questo punto avviate la generazione:

```
adb bugreport
```

Non serve altro: ADB chiede al dispositivo di generare il bug report, attende che sia pronto e salva l’archivio .zip nella cartella in cui vi trovate. L’operazione può richiedere alcuni minuti.

Se sono collegati più dispositivi, indicate quale usare con il numero di serie mostrato da adb devices:

```
adb -s NUMERO_SERIALE bugreport
```

Conservate il file .zip originale senza estrarlo, modificarlo o ricomprimerlo.

## Raccogliere i Debug Logs con logcat

I Debug Logs sono i messaggi prodotti in tempo reale dal sistema operativo e dalle applicazioni. Android li conserva in aree di memoria di dimensione limitata, i buffer: quando si riempiono, i dati più vecchi vengono sovrascritti dai nuovi.

Per questo motivo devono essere raccolti il prima possibile.

Si presentano due si...
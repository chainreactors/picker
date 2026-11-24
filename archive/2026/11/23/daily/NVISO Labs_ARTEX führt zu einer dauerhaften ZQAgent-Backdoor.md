---
title: ARTEX führt zu einer dauerhaften ZQAgent-Backdoor
url: https://blog.nviso.eu/2026/11/23/https-blog-nviso-eu-2026-11-20-artex-fog0003-zqagent-backdoor-de/
source: NVISO Labs
date: 2026-11-23
fetch_date: 2026-11-24T11:47:47.417669
---

# ARTEX führt zu einer dauerhaften ZQAgent-Backdoor

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Prevent](https://blog.nviso.eu/category/prevent/)
  + [Application Security](https://blog.nviso.eu/category/prevent/application-security/)
    - [IoT Security](https://blog.nviso.eu/category/prevent/iot-security/)
    - [Web Security](https://blog.nviso.eu/category/prevent/web-security/)
    - [Mobile Security](https://blog.nviso.eu/category/prevent/mobile-security/)
    - [Industrial Security](https://blog.nviso.eu/category/prevent/industrial-security/)
    - [AI Security](https://blog.nviso.eu/category/prevent/application-security/ai-security/)
  + [Cloud Security](https://blog.nviso.eu/category/prevent/cloud-security/)
    - [AWS](https://blog.nviso.eu/category/prevent/cloud-security/aws/)
    - [Azure](https://blog.nviso.eu/category/prevent/cloud-security/azure/)
    - [GCP](https://blog.nviso.eu/category/prevent/cloud-security/gcp/)
    - [Microsoft 365](https://blog.nviso.eu/category/prevent/cloud-security/microsoft-365/)
  + [Awareness](https://blog.nviso.eu/category/prevent/awareness/)
  + [Cyber Strategy](https://blog.nviso.eu/category/prevent/cyber-strategy/)
  + [Red Team](https://blog.nviso.eu/category/prevent/red-team/)
* [Detect](https://blog.nviso.eu/category/detect/)
  + [Blue Team](https://blog.nviso.eu/category/detect/blue-team/)
  + [Purple Team](https://blog.nviso.eu/category/detect/purple-team/)
* [Respond](https://blog.nviso.eu/category/respond/)
  + [Forensics](https://blog.nviso.eu/category/respond/forensics/)
* Other
  + [Events](https://blog.nviso.eu/category/events/)

# ARTEX führt zu einer dauerhaften ZQAgent-Backdoor

[Maxime Thiebaut](https://blog.nviso.eu/author/maxime-thiebaut/)

[Reverse Engineering](https://blog.nviso.eu/category/reverse-engineering/), [Respond](https://blog.nviso.eu/category/respond/)

November 23, 2026November 23, 2026
11 Minutes

By

[Maxime Thiebaut](https://blog.nviso.eu/author/maxime-thiebaut/) , [Kilian Neumair](https://blog.nviso.eu/author/kilian-neumair/)

November 23, 2026

In den vergangenen Monaten hat NVISO eine zunehmende Zahl von Angriffen untersucht, bei denen Angreifer LLM-gestützte Tools wie ARTEX einsetzen. Auch andere Unternehmen der Branche bestätigen diesen [Anstieg](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks)[1](#24b45bd9-b0d1-49a2-8916-ab1f2e5dedbd) . Besonders beim Ausnutzen von Schwachstellen und beim Missbrauch von Zugangsdaten erweisen sich diese Tools als leistungsfähig. Bislang folgen LLM-gestützte Angriffe einer weitgehend einheitlichen Angriffskette. Häufig lassen sie sich eindämmen, indem der ursprüngliche Zugangsweg (initial-access vector) isoliert wird und anschließend kompromittierte sowie hinterlegte Zugangsdaten umfassend gesperrt oder zurückgesetzt werden.

Durch das hohe Tempo und die auffälligkeit LLM-gestützter Tools wirken diese Angriffe häufig wie schnelle Beutezüge (smash-and-grab): Abgesehen von gesammelten und für spätere Zugriffe hinterlegten Zugangsdaten hinterlassen sie nur selten einen dauerhaften Zugang zur Zielumgebung. Bei einem kürzlich durchgeführten Incident-Response-Einsatz **beobachtete NVISO jedoch, wie ARTEX die neue Backdoor ZQAgent installierte. Diese ermöglicht dem Angreifer, sich dauerhaft in der Zielumgebung festzusetzen. Der Einsatz einer persistenten Backdoor weicht vom bislang beobachteten autonomen Vorgehen LLM-gestützter Tools ab und wird stattdessen als spezifische Angreiferanweisung vermutet.**

Bei der klassischen Installation von Backdoors wird der Einsatz von LLMs bislang nur [selten beobachtet](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)[2](#dd3973d2-918d-45e5-92a7-e6de6102dc4a) . Wir sehen jedoch keinen Grund, warum sich ihr Einsatz nicht schon in naher Zukunft auch bei diesen bisher konventionell durchgeführten Angriffen verbreiten sollte.

## ZQAgent

ZQAgent, dessen Name aus ARTEX-Artefakten abgeleitet wurde, ist eine neue, unauffällig agierende Backdoor. Sie bietet Angreifern typische Funktionen wie die Ausführung beliebigen Codes, Dateisystemoperationen und Netzwerk-Tunneling. NVISO beobachtete den Einsatz von ZQAgent in Belgien, wo die Backdoor zunächst unter `/tmp/zqa/systemd-timesyncd` abgelegt wurde. [Ähnliche samples](https://www.virustotal.com/gui/file/0319739869e1aadb2d598152a0290215c057c8364257f3a84a42164cf863019f)[3](#eb461316-e70d-4b95-b013-4b03e8ec3ef8),[4](#fd347696-532c-49fe-97f4-11e7b04cdc19) wurden auch aus Taiwan gemeldet. Im Rahmen unserer Incident-Response-Aktivitäten konnten wir bestätigen, dass alle bekannten Samples für die Command-and-Control-Kommunikation mit `37.122.150[.]15` und `bloonspace[.]com` konfiguriert waren. Diese Infrastruktur ordnen wir derzeit FOG0003 zu.

![](https://blog.nviso.eu/wp-content/uploads/2026/11/image-52.png)

Entschlüsselte Konfiguration von ZQAgent.

Von Team Cymru bereitgestellte Netzwerkdaten deuten zudem darauf hin, dass FOG0003 ZQAgent vermutlich auch in Asien eingesetzt hat. Betroffen waren dabei offenbar Regierungsstellen und Menschenrechtsorganisationen.

### Umgehung von Erkennungsmechanismen zur Laufzeit

Um die Erkennung zu erschweren, verlagert sich ZQAgent im Arbeitsspeicher in eine temporäre, anonyme Datei. Dadurch erscheint der Prozess unter dem Dateinamen `/memfd:a (deleted)`. Dieses Verhalten wurde auch bei den zuvor beschriebenen öffentlich verfügbaren Samples beobachtet.

![](https://blog.nviso.eu/wp-content/uploads/2026/11/image-4.png)

Zuweisung temporärer anonymer Dateien durch ZQAgent.

![](https://blog.nviso.eu/wp-content/uploads/2026/11/image-49.png)

Öffentlich verfügbare ZQAgent-Samples mit dem Namen memfd:a (deleted).

Nachdem sich ZQAgent in die temporäre, anonyme Datei kopiert hat, startet die Backdoor als unabhängiger Prozess neu und tarnt sich dabei als [`dbus-daemon` utility](https://linux.die.net/man/1/dbus-daemon)[5](#5cc49869-471f-400f-909f-72f2536c7733)..

![](https://blog.nviso.eu/wp-content/uploads/2026/11/image-3.png)

ZQAgent’s Befehlszeilen-Manipulation.

Durch die Manipulation der Kommandozeile erscheint ZQAgent als der folgende getarnte Prozess, ohne dass eine Verbindung zur ursprünglichen ausführbaren Datei erkennbar ist.

```
/usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
```

```
/usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
```

Weitere Maßnahmen zur Umgehung von Erkennungsmechanismen zur Laufzeit umfassen die dynamische Verschlüsselung von Konfigurationseinstellungen, die nur für ihre Verarbeitung kurzzeitig entschlüsselt werden, sowie mehrere Verschlüsselungsschichten für die Netzwerkkommunikation, etwa auf Basis von ChaCha20-Varianten.

### **Funktionen für Angreifer**

ZQAgent stellt Angreifern eine Vielzahl von Funktionen zur Verfügung. Die in der nachfolgenden Tabelle aufgeführten Operationscodes decken den Großteil des Funktionsumfangs von ZQAgent ab.

| Codes | Aktionen |
| --- | --- |
| `0x04`, `0x08` | Aktuelles Arbeitsverzeichnis mit `getcwd` abrufen bzw. mit `chdir` wechseln |
| `0x0A`, `0x15` | Teile der Laufzeitkonfiguration von ZQAgent aktualisieren |
| `0x0C` | Eine Datei verschieben, ähnlich wie mit `cp`\* |
| `0x0E` | Verzeichnisinhalt auflisten, ähnlich wie mit `ls` |
| `0x0F` | Typen der eingebundenen Dateisysteme auflisten |
| `0x11` | Eine Datei oder ein Verzeichnis entfernen, ähnlich wie mit `rm` |
| `0x12` | Eine Datei mit `rename` umbenennen |
| `0x16` | Aktuellen Benutzerkontext abrufen, ähnlich wie mit `id` |
|...
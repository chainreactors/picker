---
title: Sysmon 2026 XDR Edition: telemetria avanzata e detection su Domain Controller
url: https://blog.lobsec.com/2026/10/sysmon-2026-xdr-configurazione-domain-controller/
source: Over Security
date: 2026-10-13
fetch_date: 2026-10-14T06:53:08.957758
---

# Sysmon 2026 XDR Edition: telemetria avanzata e detection su Domain Controller

[Vai al contenuto](#content "Vai al contenuto")

[LobSec](https://blog.lobsec.com/)

Layered Offensive Barrier of Security

Menu

Menu

* [CV (ITA)](https://blog.lobsec.com/cv-ita/)
* [Privacy policy](https://blog.lobsec.com/privacy-policy/)
* [GPG](https://blog.lobsec.com/gpg/)

# Sysmon 2026 XDR Edition: telemetria avanzata e detection su Domain Controller

2026-10-13 di [lobst3r](https://blog.lobsec.com/author/lobst3r/ "Visualizza tutti gli articoli di lobst3r")

[Download](https://blog.lobsec.com/wp-content/uploads/2026/10/sysmonconfig-2026-DC-XDR.zip)

Il panorama delle minacce è mutato drasticamente. Tecniche come il BYOVD (Bring Your Own Vulnerable Driver), l’esfiltrazione raw di `NTDS.dit` e l’abuso di LOLBAS non sono più appannaggio esclusivo degli attori APT, ma standard de facto per le gang ransomware e gli initial access broker.

Per alimentare un SIEM moderno o un XDR con telemetria ad alto segnale, le vecchie configurazioni Sysmon “catch-all” o basate su esclusioni cieche per firma (come la storica config base del 2021) non sono più sufficienti: generano rumore bianco e creano enormi *blind spot*.

In questo articolo vi presento la mia **`sysmonconfig-2026-DC-XDR.xml`**, una configurazione *purpose-built* per Domain Controller e macchine tier-0. L’obiettivo non è solo la detection, ma fornire context arricchito per innescare i playbook di remediation automatica sui vostri XDR.

Di seguito il breakdown ingegneristico della configurazione, suddiviso per Event ID.

## Event ID 1 & 3: Process Creation & Network Connect (Focus LOLBAS)

Ho abbandonato il tracciamento passivo dei processi comuni per concentrarmi sull’execution chain. Oltre a PowerShell e CMD, la telemetria ora copre l’uso di `pwsh.exe` (PowerShell Core), `msdt.exe` (sfruttato per Follina e affini), `diskshadow.exe` e `appvlp.exe`. Sul fronte network, traccio i callback di questi binari (Event 3).

*Remediation playbook:* Un evento di `NetworkConnect` verso porte non standard o IP esterni originato da `forfiles.exe` o `wab.exe` deve triggerare un’azione SOAR di Network Containment immediata dell’endpoint.

```
	<!--SYSMON EVENT ID 1 : PROCESS CREATION [ProcessCreate]-->
	<RuleGroup name="" groupRelation="or">
		<ProcessCreate onmatch="exclude">
			<!--SECTION: Microsoft Windows (Esclusioni base mantenute dalla rev.1)-->
			<CommandLine condition="begin with"> "C:\Windows\system32\wermgr.exe" "-queuereporting_svc" </CommandLine>
			<CommandLine condition="begin with">C:\Windows\system32\DllHost.exe /Processid</CommandLine>
			<CommandLine condition="begin with">C:\Windows\system32\wbem\wmiprvse.exe -Embedding</CommandLine>
			<CommandLine condition="begin with">C:\Windows\system32\wbem\wmiprvse.exe -secured -Embedding</CommandLine>
			<CommandLine condition="is">C:\Windows\system32\wermgr.exe -upload</CommandLine>
			<CommandLine condition="is">C:\Windows\system32\SearchIndexer.exe /Embedding</CommandLine>
			<CommandLine condition="is">C:\windows\system32\wermgr.exe -queuereporting</CommandLine>
			<CommandLine condition="is">\??\C:\Windows\system32\autochk.exe *</CommandLine>
			<CommandLine condition="is">\SystemRoot\System32\smss.exe</CommandLine>
			<CommandLine condition="is">C:\Windows\System32\RuntimeBroker.exe -Embedding</CommandLine>
			<Image condition="is">C:\Windows\System32\plasrv.exe</Image>
			<Image condition="is">C:\Windows\system32\CompatTelRunner.exe</Image>
			<Image condition="is">C:\Windows\system32\audiodg.exe</Image>
			<Image condition="is">C:\Windows\system32\conhost.exe</Image>
			<Image condition="is">C:\Windows\system32\sppsvc.exe</Image>
			<Image condition="is">C:\Windows\system32\wbem\WmiApSrv.exe</Image>
			<IntegrityLevel condition="is">AppContainer</IntegrityLevel>
			<!--SECTION: Microsoft:Edge-->
			<CommandLine condition="begin with">"C:\Program Files (x86)\Microsoft\Edge Dev\Application\msedge.exe" --type=</CommandLine>
			<CommandLine condition="begin with">"C:\Program Files\Microsoft\Edge\Application\msedge.exe" --type=</CommandLine>
			<!--SECTION: Microsoft:dotNet-->
			<CommandLine condition="begin with">C:\Windows\Microsoft.NET\Framework\v4.0.30319\ngen.exe</CommandLine>
			<CommandLine condition="begin with">C:\WINDOWS\Microsoft.NET\Framework64\v4.0.30319\Ngen.exe</CommandLine>
			<Image condition="is">C:\Windows\Microsoft.NET\Framework64\v4.0.30319\mscorsvw.exe</Image>
			<!--SECTION: Google-->
			<CommandLine condition="begin with">"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --type=</CommandLine>
			<CommandLine condition="begin with">"C:\Program Files\Google\Chrome\Application\chrome.exe" --type=</CommandLine>
		</ProcessCreate>
	</RuleGroup>

		<RuleGroup name="" groupRelation="or">
		<NetworkConnect onmatch="include">
			<Image name="Usermode" condition="begin with">C:\Users</Image>
			<Image name="Caution" condition="begin with">C:\Recycle</Image>
			<Image condition="begin with">C:\ProgramData</Image>
			<Image condition="begin with">C:\Windows\Temp</Image>
			<Image condition="image">cmd.exe</Image>
			<Image condition="image">cscript.exe</Image>
			<Image condition="image">mshta.exe</Image>
			<Image condition="image">powershell.exe</Image>
			<Image condition="image">pwsh.exe</Image>
			<Image condition="image">wmic.exe</Image>
			<Image condition="image">wscript.exe</Image>
			<Image condition="image">bitsadmin.exe</Image>
			<Image condition="image">certutil.exe</Image>
			<!-- LOLBAS -->
			<Image condition="image">msdt.exe</Image>
			<Image condition="image">forfiles.exe</Image>
			<Image condition="image">diskshadow.exe</Image>
			<Image condition="image">pcalua.exe</Image>
			<Image condition="image">wab.exe</Image>
			<Image condition="image">odbcconf.exe</Image>
			<Image condition="image">Register-CimProvider.exe</Image>
			<Image condition="image">appvlp.exe</Image>
			<Image condition="image">control.exe</Image>
			<Image condition="image">ftp.exe</Image>
			<!--Ports: Suspicious-->
			<DestinationPort name="SSH" condition="is">22</DestinationPort>
			<DestinationPort name="RDP" condition="is">3389</DestinationPort>
			<DestinationPort name="Alert,Metasploit" condition="is">4444</DestinationPort>
			<DestinationPort name="Proxy" condition="is">8080</DestinationPort>
		</NetworkConnect>
	</RuleGroup>
	<RuleGroup name="" groupRelation="or">
		<NetworkConnect onmatch="exclude">
			<DestinationIp condition="is">127.0.0.1</DestinationIp>
			<DestinationIp condition="begin with">fe80:0:0:0</DestinationIp>
		</NetworkConnect>
	</RuleGroup>
```

```
	<!--SYSMON EVENT ID 1 : PROCESS CREATION [ProcessCreate]-->
	<RuleGroup name="" groupRelation="or">
		<ProcessCreate onmatch="exclude">
			<!--SECTION: Microsoft Windows (Esclusioni base mantenute dalla rev.1)-->
			<CommandLine condition="begin with"> "C:\Windows\system32\wermgr.exe" "-queuereporting_svc" </CommandLine>
			<CommandLine condition="begin with">C:\Windows\system32\DllHost.exe /Processid</CommandLine>
			<CommandLine condition="begin with">C:\Windows\system32\wbem\wmiprvse.exe -Embedding</CommandLine>
			<CommandLine condition="begin with">C:\Windows\system32\wbem\wmiprvse.exe -secured -Embedding</CommandLine>
			<CommandLine condition="is">C:\Windows\system32\wermgr.exe -upload</CommandLine>
			<CommandLine condition="is">C:\Windows\system32\SearchIndexer.exe /Embedding</CommandLine>
			<CommandLine condition="is">C:\windows\system32\wermgr.exe -queuereporting</CommandLine>
			<CommandLine condition="is">\??\C:\Windows\system32\autochk.exe *</CommandLine>
			<CommandLine condition="is">\SystemRoot\System32\smss.exe</CommandLine>
			<CommandLine condition="is">C:\Windows\System32\RuntimeBroker.exe -Embedding</CommandLine>
			<Image condition="is">C:\Windows\System32\plasrv.exe</Image>
			<Image condition="is">C:\Windows\system32\CompatTelRunner.exe</Image>
			<Image condition="is">C:\Windows\system32\audiodg.exe</Image>
			<Image condition="is">C:\Windows\system32\conhost.exe</Image>
			<Image condition="is">C:\Windows\system32\sppsvc.exe</...
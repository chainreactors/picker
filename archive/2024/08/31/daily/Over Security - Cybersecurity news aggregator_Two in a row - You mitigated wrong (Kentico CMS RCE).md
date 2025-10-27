---
title: Two in a row - You mitigated wrong (Kentico CMS RCE)
url: https://dfir.ch/posts/kentico_cms_rce/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:08:00.504391
---

# Two in a row - You mitigated wrong (Kentico CMS RCE)

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Two in a row - You mitigated wrong (Kentico CMS RCE)

6 Mar 2024

**Table of Contents**

* [How it started](#how-it-started)
* [Chainsaw](#chainsaw)
* [How it’s going](#how-its-going)
* [Hunting Webshells](#hunting-webshells)
* [Kentico Remote Code Execution](#kentico-remote-code-execution)
* [Stop the bleeding (almost)](#stop-the-bleeding-almost)
* [Second Investigation (5 months later)](#second-investigation-5-months-later)
* [Sysmon](#sysmon)
* [dll.bat](#dllbat)
* [IIS Modules](#iis-modules)
* [WebPartZone.ashx](#webpartzoneashx)
* [Conclusion](#conclusion)
* [IOC](#ioc)

## How it started

![An unhandled exception occurred in w3wp.exe](/images/kentico/w3wp.png "An unhandled exception occurred in w3wp.exe")

Figure 1: An unhandled exception occurred in w3wp.exe

The customer contacted us regarding sporadic crashes of the IIS worker process (w3wp.exe). Before engaging an Incident Response company, the customer attempted to resolve the issue by repeatedly restoring the websites from backup. Moreover, they set up an entirely new server and migrated the affected sites to it, only to encounter the same outcomes (crashing the w3wp process). Additionally, the client passed on the following information:

*We from the National Cybersecurity Center (NCSC) of Switzerland got notified about an infected domain hosted in your ip range. When you go to one of the affected domains and use a Googlebot useragent example: “Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)”. Then you get a lot of Backlinks to Vietnamese Websites like here: <https://www.idm.ch/Vn/mBLwi7aJ.html> and then land on pages like “wavesgamefi (dot) info”*

The first part of this investigation was conducted with my colleague [Asger Deleuran Strunk](https://www.linkedin.com/in/asgerstrunk/).

## Chainsaw

For the quick identification of anomalies or suspicious behavior, [DetectRaptor](https://github.com/mgreen27/DetectRaptor) is one option, or Chainsaw, as in the following example.

*[Chainsaw](https://github.com/WithSecureLabs/chainsaw) provides a powerful âfirst-responseâ capability to quickly identify threats within Windows forensic artefacts such as Event Logs and the MFT file. Chainsaw offers a generic and fast method of searching through event logs for keywords, and by identifying threats using built-in support for Sigma detection rules, and via custom Chainsaw detection rules.*

![Chainsaw](/images/kentico/chainsaw.png "Chainsaw")

Figure 2: Chainsaw

Here is a snippet from the Chainsaw results:

![fChainsaw results](/images/kentico/chainsaw_results.png "Chainsaw results")

Figure 3: Chainsaw results

Chainsaw pointed out the executable *PrintNotifyPotato.exe* inside the *C:\ProgramData* as suspicious. Well.. because it is: *Another potato, using PrintNotify COM service for lifting rights*, quoted from the [official GitHub repository](https://github.com/BeichenDream/PrintNotifyPotato).

![PrintNotifyPotato](/images/kentico/PrintNotifyPotato.png "PrintNotifyPotato")

Figure 4: PrintNotifyPotato

Within a few minutes into the investigation, we knew the server was 100% compromised. Otherwise, the PrintNotifyPotato.exe would not have been there. Where thereâs smoke, thereâs fire, suggesting that additional findings are likely awaiting discovery, right?

## How it’s going

Within the website’s files, we also discovered suspicious code that initiates a connection to an external domain upon page loading, retrieves content from that external domain, and subsequently integrates this content into the compromised website.

![xoso.aspx](/images/kentico/xoso.png "xoso.aspx")

Figure 5: xoso.aspx

The funny attacker left a note, asking politely not to delete the xoso.aspx file ;)

![Message from the attacker](/images/kentico/look-it.png "Message from the attacker")

Figure 6: Message from the attacker

The attacker ran the following command from a batch script, creating a new rewrite rule:

> appcmd.exe set config /section:system.webServer/rewrite/globalRules /[name=‘xoso’] action.type:“Rewrite” /[name=‘xoso’] action.url:"/CMSWebParts/Viewers/Effects/Carousel\_files/xoso.aspx?id={R:1}" /commit:apphost

A slightly different rewrite rule is also visible from within the IIS config file:

![Rewrite rule<](/images/kentico/carousel.png "Rewrite rule<")

Figure 7: Rewrite rule

The attacker added code to the (legitimate) file *PortalTemplate.aspx*. Then, whenever any hosted website requested an {anything}.html file, it would attempt to load the xoso.aspx page. This, in turn, requested HTML from a remote server (as we saw before) and returned the content - but only if the user agent contained “oogle” (the Google bot).

![PortalTemplate.aspx](/images/kentico/PortalTemplate.png "PortalTemplate.aspx")

Figure 8: PortalTemplate.aspx

## Hunting Webshells

By utilizing the Velociraptor Yara hunt and using effective Yara rules (as a starter, use the excellent [Thor Webshell](https://github.com/Neo23x0/signature-base/blob/master/yara/thor-webshells.yar) yara file), one can thoroughly search for webshells on a host. This approach enables streamlining the search process by narrowing the examination to specific file extensions, thereby reducing search time.

![Hunting Webshells with Velociraptor](/images/kentico/webshell_velo.png "Hunting Webshells with Velociraptor")

Figure 9: Hunting Webshells with Velociraptor

Individual IOCs, such as the string “xoso” in our case, can be explicitly searched by creating supplementary Yara Rules (pretty basic, but it gets the job done).

![YaraRule](/images/kentico/rule_webshell.png "YaraRule")

Figure 10: YaraRule

## Kentico Remote Code Execution

When examining compromised web servers, I prioritize determining whether a content management system (CMS) is installed and, if so, which one. Frequently, these CMS platforms harbor vulnerabilities that attackers exploit to inject malicious code or compromise the server entirely. In this instance, Kentico was identified on the affected host; the version(s) installed was vulnerable to remote code execution. A technical deep dive into the root cause of vulnerability can be found [here](https://dreadlocked.github.io/2019/10/25/kentico-cms-rce/).

![Kentico Remote Code Execution](/images/kentico/github.png "Kentico Remote Code Execution")

Figure 11: Kentico Remote Code Execution

The version of Kentico currently running on the web server can be identified through the file *CMS.DataEngine.dll*.

![CMS.DataEngine.dll](/images/kentico/DLL.png "CMS.DataEngine.dll")

Figure 12: CMS.DataEngine.dll

In addition to the exploit code available on GitHub, there is a [Metasploit module](https://www.rapid7.com/db/modules/exploit/windows/http/kentico_staging_syncserver/) for exploiting this vulnerability.

![Kentico Remote Code Execution - Rapid 7 Blog](/images/kentico/rapid7.png "Kentico Remote Code Execution - Rapid 7 Blog")

Figure 13: Kentico Remote Code Execution - Rapid 7 Blog

The exploit code reveals that the URL */CMSPages/Staging/SyncServer.asmx* must be accessible, which was the case with our CMS.

![Kentico SyncServer](/images/kentico/SyncServer.png "Kentico SyncServer")

Figure 14: Kentico SyncServer

Following an excerpt from the [Metasploit exploit code](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/http/kentico_staging_syncserver.rb):

```
def execute_command(cmd, _opts = {})
  sploit = ::Msf::Util::DotNetDeserialization.generate(
    cmd,
    gadget_chain: :WindowsIdentity,
    formatter: :SoapFormatter
  )

  res = send_request_cgi({
    'uri' => normalize_uri(target_uri.path, '/ProcessSynchronizationTaskData'),
    'method' => 'POST',
    'vars_post' => { 'stagingTaskData' => sploit }
  })
```

## Stop the bleeding (almost)

The customer implemented a rewrite rule to block access to all .asmx files unless the access originated within the cu...
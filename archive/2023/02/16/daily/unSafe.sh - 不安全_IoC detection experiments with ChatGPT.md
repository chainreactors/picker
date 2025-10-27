---
title: IoC detection experiments with ChatGPT
url: https://buaq.net/go-149521.html
source: unSafe.sh - 不安全
date: 2023-02-16
fetch_date: 2025-10-04T06:44:56.750954
---

# IoC detection experiments with ChatGPT

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/094ee254bd60ce0ac4c20d43459d75c5.jpg)

IoC detection experiments with ChatGPT

ChatGPT is a groundbreaking chatbot powered by the neural network-based language model
*2023-2-15 18:0:53
Author: [securelist.com(查看原文)](/jump-149521.htm)
阅读量:48
收藏*

---

ChatGPT is a groundbreaking chatbot powered by the neural network-based language model text-davinci-003 and trained on a large dataset of text from the Internet. It is capable of generating human-like text in a wide range of styles and formats.

ChatGPT can be fine-tuned for specific tasks, such as answering questions, summarizing text, and even solving cybersecurity-related problems, such as [generating incident reports](https://www.cadosecurity.com/experimenting-with-chatgpt-for-incident-response/) or [interpreting decompiled code](https://github.com/JusticeRage/Gepetto/). Apparently, attempts have been made to generate malicious objects, such as [phishing emails](https://research.checkpoint.com/2023/opwnai-cybercriminals-starting-to-use-chatgpt/), and even [polymorphic malware](https://www.cyberark.com/resources/threat-research-blog/chatting-our-way-into-creating-a-polymorphic-malware).

It is common for security and threat researches to publicly disclose the results of their investigations (adversary indicators, tactics, techniques, and procedures) in the form of reports, presentations, blog articles, tweets, and other types of content.

[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/02/14120201/Experiments_with_ChatGPT_for_IoC_detection_01-1024x422.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/02/14120201/Experiments_with_ChatGPT_for_IoC_detection_01.png)

Therefore, we initially decided to check what ChatGPT already knows about threat research and whether it can help with identifying simple, well-known adversary tools like Mimikatz and Fast Reverse Proxy, and spotting the common renaming tactic. The output looked promising!

What about classic indicators of compromise, such as well-known malicious hashes and domains? Unfortunately, during our quick experiment, ChatGPT was not able to produce satisfying results: it failed to identify the well-known hash of Wannacry (hash: [5bef35496fcbdbe841c82f4d1ab8b7c2](https://opentip.kaspersky.com/5bef35496fcbdbe841c82f4d1ab8b7c2/?utm_source=SL&utm_medium=SL&utm_campaign=SL)).

For various APT[1](#ftn1) domains, ChatGPT produced a list of mostly the same legitimate domains — or is it that we may not know something about these domains? — despite it provided description of APT actors[1](#ftn1).

As for FIN7[1](#ftn1) domains, it correctly classified them as malicious, although the reason it gave was, “the domain name is likely an attempt to trick users into believing that it is a legitimate domain”, rather than there being well-known indicators of compromise.

While the last experiment, which targeted domains that mimicked a well-known website, gave an interesting result, more research is needed: it is hard to say why ChatGPT produces better results for host-based artifacts than for simple indicators like domain names and hashes. Certain filters might have been applied to the training dataset, or the questions themselves should be constructed if a different way (a problem well-defined is a problem half-solved!).

Anyway, since the responses for host-based artifacts looked more promising, we instructed ChatGPT to write some code to extract various metadata from a test Windows system and then to ask itself whether the metadata was an indicator of compromise:

[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/02/14120829/Experiments_with_ChatGPT_for_IoC_detection_12.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/02/14120829/Experiments_with_ChatGPT_for_IoC_detection_12.png)

Certain code snippets were handier then others, so we decided to continue developing this proof of concept manually: we filtered the output for events where the ChatGPT response contained a “yes” statement regarding the presence of an indicator of compromise, added exception handlers and CSV reports, fixed small bugs, and converted the snippets into individual cmdlets, which produced a simple IoC scanner, *HuntWithChatGPT.psm1*, capable of scanning a remote system via WinRM:

[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/02/14120853/Experiments_with_ChatGPT_for_IoC_detection_13.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/02/14120853/Experiments_with_ChatGPT_for_IoC_detection_13.png)

|  |  |
| --- | --- |
| **HuntWithChatGPT.psm1** | |
| Get-ChatGPTAutorunsIoC | Modules configured to run automatically (Autoruns/ASEP) |
| Get-ChatGPTRunningProcessesIoC | Running processes and their command lines |
| Get-ChatGPTServiceIoC | Service installation events (event ID 7045) |
| Get-ChatGPTProcessCreationIoC | Process creation event ID 4688 from Security log |
| Get-ChatGPTSysmonProcessCreationIoC | Process creation event ID 1 from Sysmon log |
| Get-ChatGPTPowerShellScriptBlockIoC | PowerShell Script blocks (event ID 4104 from Microsoft-Windows-PowerShell/Operational) |
| Get-ChatGPTIoCScanResults | Runs all functions one by one and generates reports |

|  |  |
| --- | --- |
|  | Get-ChatGPTIoCScanResults      -apiKey <Object>          OpenAI API key https://beta.openai.com/docs/api-reference/authentication      -SkipWarning [<SwitchParameter>]      -Path <Object>      -IoCOnly [<SwitchParameter>]          Export only Indicators of compromise      -ComputerName <Object>          Remote Computer's Name      -Credential <Object>          Remote Computer's credentials |

We infected the target system with the Meterpreter and PowerShell Empire agents, and emulated a few typical adversary procedures. Upon executing the scanner against the target system, it produced a scan report enriched with ChatGPT conclusions:

[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/02/14120933/Experiments_with_ChatGPT_for_IoC_detection_14.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/02/14120933/Experiments_with_ChatGPT_for_IoC_detection_14.png)

Two malicious running processes were identified correctly out of 137 benign processes, without any false positives.

[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/02/14120955/Experiments_with_ChatGPT_for_IoC_detection_15-1024x346.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/02/14120955/Experiments_with_ChatGPT_for_IoC_detection_15.png)

Note that ChatGPT provided a reason why it concluded that the metadata were indicators of compromise, such as “command line is attempting to download a file from an external server” or “it is using the “-ep bypass” flag which tells PowerShell to bypass security checks that are normally in place”.

For service installation events, we slightly modified the question to instruct ChatGPT to “think step by step”, so that it would slow down and avoid cognitive bias, as advised by multiple researchers on Twitter:

> Is following Windows service name ‘$ServiceName’ with following Launch String ‘$Servicecmd’ – an indicator of compromise? Think about it step by step.

ChatGPT successfully identified suspicious service installations, without false positives. It produced a valid hypothesis that “the code is being used to disable logging or other security measures on a Windows system”. For the second service, it provided a conclusion about why the service should be classified as an indicator of...
---
title: New ValleyRAT Campaign Spotted with Advanced Techniques
url: https://any.run/cybersecurity-blog/new-valleyrat-campaign/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:06:17.738087
---

# New ValleyRAT Campaign Spotted with Advanced Techniques

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2022/10/mini-logo.png)](/cybersecurity-blog/)

* + Search

![New ValleyRAT Campaign Spotted with Advanced Techniques ](/cybersecurity-blog/wp-content/uploads/2024/08/valley_blog.jpg)

[News](/cybersecurity-blog/category/news/)

# New ValleyRAT Campaign Spotted with Advanced Techniques

August 20, 2024

[Add comment](#comments-8626)
3776 views
3 min read

[Home](/cybersecurity-blog/)[News](/cybersecurity-blog/category/news/)

New ValleyRAT Campaign Spotted with Advanced Techniques

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1370
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3016
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3014
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[News](/cybersecurity-blog/category/news/)

New ValleyRAT Campaign Spotted with Advanced Techniques

A sophisticated campaign is targeting Chinese-speaking users, [distributing](https://thehackernews.com/2024/08/multi-stage-valleyrat-targets-chinese.html) a malware known as ValleyRAT.

## What’s happening?

There’s a new campaign spreading a multi-stage threat designed to monitor and control infected systems while deploying additional plugins to cause further damage.

### Key components of the campaign:

| Component | Details |
| --- | --- |
|  |  |
| --- | --- |
| Target | Chinese-speaking users |
| Attack Method | Email messages with URLs pointing to compressed executables |
| Malware | ValleyRAT |
| Affected systems | Windows |

ValleyRAT employs a range of techniques to evade detection, including the use of shellcode to execute its components directly in [memory](https://blog-adm.susp.io/cybersecurity-blog/fileless-malware/), minimizing its footprint on the victim’s system. The campaign initially came to light in June 2024, with the latest iteration featuring enhanced capabilities for persistence and privilege escalation.

Analyze ValleyRAT and other malware in ANY.RUN sandbox

[Sign up for free](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=valleyrat_campaign&utm_term=200824&utm_content=linktoregistration#register/)

## Breaking down the attack chain

The attack begins with a first-stage loader disguised as legitimate applications like Microsoft Office, using filenames such as “工商年报大师.exe” or “补单对接更新记录txt.exe” to appear non-threatening. When launched, the executable drops a decoy document and loads shellcode that advances the attack to the next stage.

This shellcode initiates communication with a command-and-control (C2) server, downloading two critical components: RuntimeBroker and RemoteShellcode. These components are responsible for setting persistence on the host, gaining administrator privileges through exploitation techniques, and further escalating privileges by abusing legitimate binaries like fodhelper.exe and the CMSTPLUA COM interface.

RuntimeBroker’s primary task is to retrieve another loader from the C2 server, which repeats the initial infection process while performing additional checks to determine if it is running in a sandbox. It also scans the Windows Registry for keys related to apps like Tencent WeChat and Alibaba DingTalk, reinforcing the notion that ValleyRAT is specifically targeting Chinese systems.

RemoteShellcode is configured to fetch the ValleyRAT downloader, which uses network protocols like UDP or TCP to connect to the C2 server and receive the final payload. ValleyRAT, attributed to the Silver Fox threat group, is a fully-featured backdoor capable of remotely controlling compromised systems, taking screenshots, executing files, and loading additional plugins.

Remote Shellcode, on the other hand, is responsible for fetching the ValleyRAT downloader, which then uses network protocols to connect to the server and receive the final payload.

## Analyzing ValleyRAT in ANY.RUN

[ValleyRAT](https://app.any.run/tasks/bd4926c1-eb84-44f7-8ce3-89d055cb3023/?utm_source=anyrunblog&utm_medium=article&utm_campaign=valleyrat_campaign&utm_term=200824&utm_content=linktoservice) can be analyzed in [ANY.RUN sandbox](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=valleyrat_campaign&utm_term=200824&utm_content=linktolanding), a powerful tool that provides detailed insights into the malware’s behavior.

![](/cybersecurity-blog/wp-content/uploads/2024/08/valley_new-1024x565.png)

The sandbox analysis shows that the MSBuild.exe executed with a command line pointing to the file.exe located in the Temp directory.

Legitimate programs often use MSBuild.exe, a Microsoft build engine, to compile and build projects, especially those developed using .NET Framework.

In a malicious context, the use of MSBuild.exe indicates an attempt to hide malicious activities within a seemingly legitimate process.

![](/cybersecurity-blog/wp-content/uploads/2024/08/valley_two-1024x577.png)

The sandbox also provides informatio...
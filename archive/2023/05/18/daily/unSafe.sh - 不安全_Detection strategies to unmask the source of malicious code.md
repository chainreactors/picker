---
title: Detection strategies to unmask the source of malicious code
url: https://buaq.net/go-163840.html
source: unSafe.sh - 不安全
date: 2023-05-18
fetch_date: 2025-10-04T11:38:30.550450
---

# Detection strategies to unmask the source of malicious code

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

![](https://8aqnet.cdn.bcebos.com/8a10ca50d1af567394633ce94cf6a7a2.jpg)

Detection strategies to unmask the source of malicious code

Posted by on Wednesday, May 17, 2023
*2023-5-17 22:35:58
Author: [www.synopsys.com(查看原文)](/jump-163840.htm)
阅读量:20
收藏*

---

Posted by on Wednesday, May 17, 2023

*Having malicious code detection strategies in place is critical to keeping your software supply chain secure.*

Let’s imagine you discover a string of suspicious code within one of your applications. Perhaps a routine scan by your application testing team finds a point of interest that indicates malicious code, such as a time bomb or back door, has been inserted by a malicious insider within your [software supply chain](https://www.synopsys.com/software-integrity/solutions/software-supply-chain-security.html).

[![discovery of malicious code | Synopsys](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2017/02/points-of-interest.jpg)](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2017/02/points-of-interest.jpg)

First, you breathe a huge sigh of relief that you found the problem before it caused any lasting damage (data theft, log keystrokes, money siphoning, or some other subverted functions of the application).

But then you think, if someone inserted malicious code into one application, what’s to stop them from targeting another?

You need to unmask the culprit.

Malicious code can be injected into an executable as early as the development of an open source component, and as late as the final production build, which means your adversary could be anyone within your software supply chain.

## Round up the usual suspects

Your suspect list includes people with the necessary access or ability to insert malicious code.

* **Administration/operations**
  + Production environment access
  + LAN access
  + Credentials
* **Developers**
  + Ability to alter source code
  + Ability to select third-party and open source libraries
  + Ability to modify configuration files
* **Change/build/control management**
  + Ability to repackage binaries
  + Ability to modify dependencies on the build server
  + Ability to configure build files to use malicious binaries

## Gather your evidence

Analysis of the executable alone will not provide enough information to narrow down the list of potential suspects. For that type of detection work, you need to get your hands on dependencies, source code, build files, and design documents. In combination, these assets can help you put together a timeline of when the malicious code was inserted. Here’s how it works.

[![Analyze the executable | Synopsys](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2017/02/actionable-intelligence.jpg)](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2017/02/actionable-intelligence.jpg)

## Analyze the executable and source code

If you find malicious code in both the executable and the source code of an application, you’ve got a strong indicator that your culprit is a developer of your proprietary code or an external dependency.

If the malicious code is not present in the source code, it could mean that the malicious code was removed from the source code before it was analyzed, or that the code was injected at a later stage in the software development life cycle ([SDLC](https://www.synopsys.com/glossary/what-is-sdlc.html)).

In order to narrow down the search, you need to take into account the location where code was obtained. If it was obtained from a repository where any code changes are tracked and from which code is retrieved for the build process, it is another strong indicator that the malicious finding was injected at a later stage in the SDLC.

## Analyze the executable, source code, and build files

Since malicious code can also be injected in an application at a stage after development, you also need to analyze build files.

For example, build files can be made to execute programs that inject malicious code at build time by adding a simple task, as shown in the following ant build file snippet:

[![snippet 1 | Synopsys](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2017/02/snippet-1.jpg)](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2017/02/snippet-1.jpg)

Build files can also be configured to retrieve malicious dependencies from locations outside the build servers, as shown in the following snippets:

[![snippet 2 | Synopsys](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2017/02/snippet-2.jpg)](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2017/02/snippet-2.jpg)

or

[![snippet 3 | Synopsys](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2017/02/snippet-3.jpg)](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2017/02/snippet-3.jpg)

An insider can also replace existing dependencies in the build server’s local repository with malicious ones. During the build process, these malicious dependencies will be used even by a benign build file and will result in malicious code being injected into every application using those dependencies. The presence of malicious code in an executable where the source code and build file both appear benign points toward this case.

Keep in mind that an “insider” may not always be an employee or contractor of the impacted organization. An insider can also be someone who, through some malicious means, has gained access to the same systems and information that an employee has access to. For example, look at how attackers gained access to the SolarWinds build process to insert malicious code, which went undetected before making its way to customers.

## Analyze the design documents

Design documents are helpful in determining whether code that *looks* malicious *is* actually malicious. For example, consider the snippet below from a web.xml. The code shows an application that has an alternate servlet with an alternate path mapping. A design document would show if this alternate path is required by design or if it is potentially malicious.

[![snippet 4| Synopsys](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2017/02/snippet4.jpg)](https://www.synopsys.com/blogs/software-security/wp-content/uploads/2017/02/snippet4.jpg)

## Build your case

The more information you have, the easier it will be to find the source of any insider threat. Once you believe you know the stage at which malicious code was inserted, you may have enough information to track actions to a specific individual or source, or you may need to monitor the team more closely. Keep the investigation team small so you don’t raise any flags before your suspicions are confirmed.

---

文章来源: https://www.synopsys.com/blogs/software-security/detection-strategies-to-unmask-the-source-of-malicious-code/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
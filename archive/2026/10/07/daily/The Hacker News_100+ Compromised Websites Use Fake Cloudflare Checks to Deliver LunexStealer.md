---
title: 100+ Compromised Websites Use Fake Cloudflare Checks to Deliver LunexStealer
url: https://thehackernews.com/2026/10/100-compromised-websites-use-fake.html
source: The Hacker News
date: 2026-10-07
fetch_date: 2026-10-08T08:08:37.095905
---

# 100+ Compromised Websites Use Fake Cloudflare Checks to Deliver LunexStealer

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [100+ Compromised Websites Use Fake Cloudflare Checks to Deliver LunexStealer](https://thehackernews.com/2026/10/100-compromised-websites-use-fake.html)

**Ravie Lakshmanan**Oct 07, 2026Malware / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4fqqLhgtSTncznc3k2vTS6LJlp8_v3RMx7LaYawiUYEMDuhQ1pOdqrYqlFeyAG5TPBmEnbkLI8vu43GMDxPvaZX6kABd1zQGpIAbVpD2pwtl5v4TohuwbBjlz4dMcjYUv11ogWwPoMoOFJn0aHmxX46xc5Y3ocuxOrg7ix9RrzPzfHtjlW2rAElAV-9-p/s1700-nu-rw-lo-l85-e365/cf-malware.jpg)

The Computer Emergency Response Team of Ukraine (CERT-UA) has identified more than 100 compromised websites that have been injected with malicious JavaScript to serve an information-stealing malware called **[LunexStealer](https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html)** (aka Psychedelic Stealer).

The activity, which was observed by the agency in September 2026, has been attributed to a threat cluster dubbed UAC-0277. It did not disclose who the victims of the campaign were or if any systems were successfully compromised as a result of these attacks.

"When visiting such a site, users were shown a forged Cloudflare verification page that, under the pretext of confirming the visitor is human, prompted them to execute a command," CERT-UA [said](https://cert.gov.ua/article/6319983) in an advisory. "Executing the command caused a malicious MSI package to be downloaded and installed from a remote server (the ClickFix technique)."

The attacks also make use of the [EtherHiding](https://thehackernews.com/2026/08/trojanized-npm-packages-decode-c2-ip.html) technique to retrieve the domain name of the resource from which the fake verification page is loaded, as well as the script's operating mode, from a smart contract on the Polygon or Ethereum network.

According to CERT-UA, there are three operating modes: 0 – inactive; 1 – passive tracking of visitors that includes gathering data about the website and the page from which the visitor arrived; and 2 – displaying the fake verification page.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

In Mode 2, the bogus verification page is shown only to Windows users who arrive at the site from search engine results and not more than twice in 12 hours. These ClickFix lures lead to the distribution of MSI packages that deliver LunexStealer.

At least three different variants of the MSI packages have been discovered -

* **Variant 1**, which installs LunexStealer on the system.
* **Variant 2**, which attempts to bypass Windows account control (UAC), configures Microsoft Defender exclusions, leverages the legitimate-but-vulnerable AMD driver ("PDFWKRNL.sys") to blind security software, and then retrieves and runs LunexStealer from a remote server.
* **Variant 3**, which launches LunexStealer via DLL sideloading by using the legitimate binary ("FnHotkeyUtility.exe") to load a rogue DLL ("spkvol.dll"), which decrypts and executes the stealer.

As documented by both [Arctic Wolf Labs](https://thehackernews.com/2026/09/hacked-ukrainian-sites-serve-fake.html) and [Ontinue](https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html), LunexStealer is also designed to install a malicious browser extension called LUNARAXE. The extension masquerades as "Microsoft Office Word Editor" to steal cookies, browsing history, and credentials entered into web forms. It also allows the operator to remotely control the browser and execute arbitrary JavaScript on web pages.

The stealer also deploys an auxiliary component named NAIVEMESS that's installed based on a configuration received from the command-and-control (C2) server. Its primary responsibility is to provide LUNARAXE with access to the Windows file system through a PowerShell-based Native Messaging Host.

"NAIVEMESS functionality includes retrieving the list of drives, browsing directories, reading, creating and overwriting files, as well as executing them," CERT-UA said. "Files are transferred in chunks encoded in Base64, and directories and file groups are pre‑archived into ZIP."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The component does have its own communication channel with the C2 server. Rather, commands are received via the extension, which houses three other modules -

* LUNARAXE.CORE, which handles C2 communication, receives commands, executes them, and exfiltrates browser data (i.e., cookies, browsing history, bookmarks, details about installed extensions, and intercepted credentials). It can also manage tabs, enable/disable extensions, serve notifications, run JavaScript on web pages, and display bogus overlays. It can also copy files from the computer, write files to it, and execute them if NAIVEMESS is installed.
* LUNARAXE.STEALER, which captures credentials entered into web forms and sends them to LUNARAXE.CORE, along with the page URL.
* LUNARAXE.STRIP, which disables Content Security Policy ([CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)) protections on web pages by stripping CSP headers from HTTP responses with an aim to run arbitrary JavaScript code.

CERT-UA is advising organizations to prohibit regular users from using the Windows Run dialog via group policies, restrict the installation of MSI packages by users without administrator rights, monitor for the execution of "msiexec.exe," enable blocking of vulnerable drivers via Microsoft's vulnerable driver blocklist, and limit the installation of browser extensions to allowlisted ones.

Microsoft also [recommends](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/microsoft-recommended-driver-block-rules) turning on the Attack Surface Reduction (ASR) rule "Block abuse of exploited vulnerable signed drivers" to prevent an application from writing a vulnerable signed driver...
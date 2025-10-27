---
title: Malicious Browser Extensions Infect Over 700 Users Across Latin America Since Early 2025
url: https://thehackernews.com/2025/06/malicious-browser-extensions-infect-722.html
source: The Hacker News
date: 2025-06-09
fetch_date: 2025-10-06T22:54:44.527483
---

# Malicious Browser Extensions Infect Over 700 Users Across Latin America Since Early 2025

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Malicious Browser Extensions Infect Over 700 Users Across Latin America Since Early 2025](https://thehackernews.com/2025/06/malicious-browser-extensions-infect-722.html)

**Jun 08, 2025**Ravie LakshmananMalware / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUAQHGfPwsMGi_VlhnfYhfS44xBQLg8SRFOHPc6hkuog7awdUP7oXpgRsbN8Wvlr10p6VEiVOH2HgQgvqJnjFGIkTSggI0cvGu8IzuOB1O6eWfzJHSCnuXtWVK7OjmWN56ATj3oweBnFzoyRSrqp7vaoR-OGCoTspfShKxe6FDa2CgLWG4P3h8rHipe7QQ/s790-rw-e365/chain-1.jpg)

Cybersecurity researchers have shed light on a new campaign targeting Brazilian users since the start of 2025 to infect users with a malicious extension for Chromium-based web browsers and siphon user authentication data.

"Some of the phishing emails were sent from the servers of compromised companies, increasing the chances of a successful attack," Positive Technologies security researcher Klimentiy Galkin [said](https://global.ptsecurity.com/analytics/pt-esc-threat-intelligence/operation-phantom-enigma) in a report. "The attackers used a malicious extension for Google Chrome, Microsoft Edge, and Brave browsers, as well as Mesh Agent and PDQ Connect Agent."

The Russian cybersecurity company, which is tracking the activity under the name **Operation Phantom Enigma**, said the malicious extension was downloaded 722 times from across Brazil, Colombia, the Czech Republic, Mexico, Russia, and Vietnam, among others. As many as 70 unique victim companies have been identified. Some aspects of the campaign were disclosed in early April by a researcher who goes by the alias [@johnk3r](https://x.com/johnk3r/status/1907837072750063687) on X.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attack starts with phishing emails disguised as invoices that trigger a multi-stage process to deploy the browser extension. The messages encourage recipients to download a file from an embedded link or open a malicious attachment contained within an archive.

Present within the files is a batch script that's responsible for downloading and launching a PowerShell script, which, in turn, performs a series of checks to determine if it's running in a virtualized environment and the presence of a software named Diebold Warsaw.

Developed by GAS Tecnologia, Warsaw is a security plugin that's used to secure banking and e-commerce transactions through the Internet and mobile devices in Brazil. It's worth noting that Latin American banking trojans like Casbaneiro have incorporated similar features, as [disclosed](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/) by ESET in October 2019.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnU60hLdzp1X06aoJ8JnB9r-A1SzGhqsHmRGLt_R9oLmZ-JT7KJcfdPDGQMkroCzkZZg9Y4cSX5sMZyvezpd8uDEIx5UN-Ked0iwV5bnNVZFbvjgCJwnJ-kDG2ohxxHe1IwEzQzmvE1ZvyZ1aTfPq7XWX7e4Ogdu-N6OXiDdBAeW_NZUYM2dH3Yp3ybCPB/s790-rw-e365/second.png)

The PowerShell script is also engineered to disable User Account Control (UAC), set up persistence by configuring the aforementioned batch script to be launched automatically upon system reboot, and establish a connection with a remote server to await further commands.

The list of supported commands is as follows -

* PING - Send a heartbeat message to the server by sending "PONG" in response
* DISCONNECT - Stop the current script process on the victim's system
* REMOVEKL - Uninstall the script
* CHECAEXT - Check the Windows Registry for the presence of a malicious browser extension, sending OKEXT if it exists, or NOEXT, if the extension is not found
* START\_SCREEN - Install the extension in the browser by modifying the [ExtensionInstallForcelist](https://chromeenterprise.google/policies/?policy=ExtensionInstallForcelist) policy, which specifies a list of apps and extensions that can be installed without user interaction

The detected extensions (identifiers: nplfchpahihleeejpjmodggckakhglee, ckkjdiimhlanonhceggkfjlmjnenpmfm, and lkpiodmpjdhhhkdhdbnncigggodgdfli) have already been removed from the Chrome Web Store.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFeiAZnR1myCgaH38CDRBOGpDA7geIeMCsKlHSg1WUcgNFVunT55v_Rw7GgRpPas7UNA6NukiqG8Dz1U1w62Goi4fLAw_13_9IU1kOKS4t3phuXWRHt8U-CpwcBMIbir7QU4m4ixKJ55j6i8U0X3xorZLB3cxQpUrGgHXmcV9newTSvEukEbbF1ZPRHNrs/s790-rw-e365/map.png)

Other attack chains swap the initial batch script for Windows Installer and Inno Setup installer files that are utilized to deliver the extensions. The add-on, per Positive Technologies, is equipped to execute malicious JavaScript code when the active browser tab corresponds to a web page associated with Banco do Brasil.

Specifically, it sends the user's authentication token and a request to the attackers' server to receive commands to likely display a loading screen to the victim (WARTEN or SCHLIEBEN\_WARTEN) or serve a malicious QR code on the bank's web page (CODE\_ZUM\_LESEN). The presence of German words for the commands could either allude to the attacker's location or that the source code was repurposed from somewhere else.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In what appears to be an effort to maximize the number of potential victims, the unknown operators have found to leverage invoice-related lures to distribute installer files and deploy remote access software such as MeshCentral Agent or PDQ Connect Agent instead of a malicious browser extension.

Positive Technologies said it also identified an open directory belonging to the attacker's auxiliary scripts containing links with parameters that included the EnigmaCyberSecurity identifier ("<victim-domain>/about.php?key=EnigmaCyberSecurity").

"The study highlights the use of rather unique techniques in Latin America, including a malicious browser extension and distribution via Windows Installer and Inno Setup installers," Galkin sa...
---
title: Signed, Trusted, and Abused: Proxy Execution via WebView2
url: https://www.blackhillsinfosec.com/proxy-execution-via-webview2/
source: Black Hills Information Security, Inc.
date: 2026-04-15
fetch_date: 2026-04-16T04:52:52.796205
---

# Signed, Trusted, and Abused: Proxy Execution via WebView2

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-consultants/)
  + [Admin Team](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [Active SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [Antisyphon Training](https://www.blackhillsinfosec.com/about/antisyphon/)
  + [BHIS Tribe of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://bhispodcasts.transistor.fm/)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

15
Apr
2026

[C2](https://www.blackhillsinfosec.com/category/red-team/c2/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Matthew Eidelberg](https://www.blackhillsinfosec.com/category/author/matthew-eidelberg/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/)
[DLL sideloading](https://www.blackhillsinfosec.com/tag/dll-sideloading/), [initial access](https://www.blackhillsinfosec.com/tag/initial-access/)

# [Signed, Trusted, and Abused: Proxy Execution via WebView2](https://www.blackhillsinfosec.com/proxy-execution-via-webview2/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/03/MEidelberg-150x150.png)

| [Matthew Eidelberg](https://x.com/Tyl0us)

![Proxy execution via WebView2 banner](https://www.blackhillsinfosec.com/wp-content/uploads/2026/04/Proxy-execution-via-WebView2.png)

In today’s rapidly evolving digital landscape, Windows and its ecosystem of applications are transforming faster than ever, often leaving the door open for new exploitation techniques. Microsoft Edge WebView2 Runtime, with its presence on hundreds of millions of Windows endpoints, is an integral part of this attack surface and has gone largely unnoticed by both defenders and attackers. This article provides an offensive security perspective on Microsoft Edge WebView2 Runtime, including architectural weaknesses, existing vulnerabilities, and exploitation methods.

## **Windows Apps**

Modern “Windows Apps” are Store‑delivered, sand-boxed applications built as a container for a web-based application that can run on a Windows endpoint as standalone executable. This differs from traditional applications that require first installing a series of files and dependencies onto the endpoint before being used. A Windows App is lighter in size and faster (operating as if it were a web app). This shifts to signed/trusted applications that offer runtime integrity safeguards, Smart App Control, and clearer permission prompts—reducing risks from legacy installers, COM add‑ins, dropped drivers, or third-party dependencies.

In [Proxying Your Way to Code Execution – A Different Take on DLL Hijacking](https://www.blackhillsinfosec.com/a-different-take-on-dll-hijacking/) I talk about how these applications *“do not have any third-party or external addons that reside in user-controlled areas (i.e. Appdata), it’s not possible to do any DLL hijacking attacks in the traditional sense. Even with elevated permissions, it’s not possible to access or write to these folders.”*

![Admins not able to view the contents of the folder](https://www.blackhillsinfosec.com/wp-content/uploads/2026/04/Figure-1-1024x576.png)

Admins not able to view the contents of the folder

Windows Apps are becoming more common and replacing legacy applications. This includes business applications as well as default applications that come on all Windows 10 and 11 systems. Some examples are:

* Outlook for Windows (olk.exe)
* Word.exe
* Excel.exe
* Ms-Teams
* Edge Browser
* M365Copilt
* Photos
* Calculator
* Media player
* Spotify
* WeChat

These apps work great in running their content as an isolated container, but all depend on Microsoft Edge WebView2 Runtime, which opens an attack vector.

## **What is WebView2?**

The Microsoft Edge WebView2 Runtime is a Chromium-based browser engine that can be utilized by Windows applications to render the web content without the requirement of opening a new browser window or loading an external web application. This enables the execution of web applications locally without the need to port them into a conventional GUI-based Windows application that requires an extensive installation process, thus enabling the integration of web technologies such as HTML, CSS, and JavaScript into Windows applications without the requirement of opening the browser window. This enables:

* Displaying dynamic web content inside apps.
* Reusing web-based UI components.
* Ensuring consistent rendering across platforms.

![Process Monitor – Showing the Child Process of Ms-Teams.exe](https://www.blackhillsinfosec.com/wp-content/uploads/2026/04/Figure-2-1024x434.png)

Process Monitor – Showing the Child Process of Ms-Teams.exe

## **What Makes WebView2 Problematic?**

So why do we care about this? From an attacker’s perspective, WebView2 presents an interesting target. These Windows Apps are “self-contained” to prevent the loading of third-party add-ons or requiring external libraries, while relying on WebView2 to render the application; but WebView2 is not designed in the same way. This means that despite their strengths, Windows Apps are still susceptible to DLL sideloading because WebView2 is susceptible to DLL sideloading a...
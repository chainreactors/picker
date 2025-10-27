---
title: Putting Our Hooks Into Windows
url: https://trustedsec.com/blog/putting-our-hooks-into-windows
source: TrustedSec
date: 2024-09-13
fetch_date: 2025-10-06T18:30:08.873392
---

# Putting Our Hooks Into Windows

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Putting Our Hooks Into Windows](https://trustedsec.com/blog/putting-our-hooks-into-windows)

September 12, 2024

# Putting Our Hooks Into Windows

Written by
Scott Nusbaum

Malware Analysis

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/PuttingHooksIntoWindows_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1726063870&s=bcdd92906c5e54c68faf892b6dbad7d8)

Table of contents

* [1.1      How Does it Work?](#How)
* [1.2      Code Demonstration in C and C#](#CodeDemo)
* [1.3      Reversing the Code](#Reversing)
* [1.4      Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#5a65292f38303f392e6719323f39317f686a352f2e7f686a2e3233297f686a3b282e3339363f7f686a3c2835377f686a0e282f292e3f3e093f397f686b7c3b372a6138353e23670a2f2e2e33343d7f686a152f287f686a12353531297f686a13342e357f686a0d33343e352d297f691b7f686a322e2e2a297f691b7f681c7f681c2e282f292e3f3e293f39743935377f681c3836353d7f681c2a2f2e2e33343d77352f287732353531297733342e35772d33343e352d29 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fputting-our-hooks-into-windows "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Putting%20Our%20Hooks%20Into%20Windows%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fputting-our-hooks-into-windows "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fputting-our-hooks-into-windows&mini=true "Share on LinkedIn")

We're back with another post about common malware techniques. This time we are talking about setting Windows hooks. This is a simple technique that can be used to log keystrokes or inject code into remote processes. We will be employing the use of ***SetWindowsHookEx*** to register a function to be called whenever an event is triggered.

We will demonstrate this method in C and C# like we have in previous posts.

## 1.1      How Does it Work?

This attack works by utilizing the Windows ***SetWindowsHookEx*** function. This function allows the programmer to tell Windows to add a specified hook procedure into a hook chain. An example would be to hook the ***WH\_KEYBOARD*** type to create a keystroke logger.

Every time a key is pressed or released, a message will be placed in a message list or chain known as a hook chain. Each link in the chain will process the message and then pass it to the next link. The listening function then can store the keystrokes in memory, on disk, or sent to a C2 server.

The parameters for the ***SetWindowsHookEx*** function are shown below.

```
HHOOK SetWindowsHookExA(
  [in] int       idHook,
  [in] HOOKPROC  lpfn,
  [in] HINSTANCE hmod,
  [in] DWORD     dwThreadId
);
```

* ***idHook*** is the type of hook to be added. There is a list of [14 different types of hooks](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setwindowshookexa), although some are depreciated in newer windows. For our purposes, we are going to focus on the ***WH\_KEYBOARD*** hook type. This will signal our application-defined function whenever a keyboard event is triggered.
* ***lpfn*** is a pointer to the application-defined function that will be called when the event is triggered. This function must contain the following parameters: ***nCode***, ***wParam***, and ***lParam***.
* ***hmod*** is a pointer to the library containing the application-defined function. In our case, this will be a malicious DLL that is loaded onto the target system. We will be using an obvious name called ***evil.dll***.
* ***dwThreadID*** is the thread identifier for the hook to be tied to. This parameter with the value of ***0 (zero)***, on desktops, will add this hook to all threads running on the desktop not just the current thread.

After the hook has been added to the ***hook\_chain***, the registered DLL will be loaded into any process that triggers that hooks event. So, any process that a key is pressed will execute our malicious code. The following image is of a X64dbg breakpoint set for when a new DLL is loaded. The debugger was attached to Microsoft Notepad.exe after the malicious process was started. It was verified that the ***evil.dll*** was not loaded into the Notepad memory space. Then, typing a single character into the Notepad application caused the ***evil.dll*** to be loaded into that memory space and executed.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HooksWindows_Nusbaum/Fig1_Nusbaum.png?w=320&q=90&auto=format&fit=max&dm=1725456847&s=f00f4ac3a8c76e081e6975eb3b42f369)

Figure 1 - Notepad ...
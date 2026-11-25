---
title: An 8088, 640 KB of RAM and a Really Bad Idea
url: https://decoder.cloud/2026/11/24/an-8088-640-kb-of-ram-and-a-really-bad-idea/
source: Over Security
date: 2026-11-24
fetch_date: 2026-11-25T10:48:12.550817
---

# An 8088, 640 KB of RAM and a Really Bad Idea

# [Decoder's Blog](https://decoder.cloud/ "Decoder's Blog")

Decoder's Blog

[Skip to content](#content "Skip to content")

* [Home](/)
* [Decoder’s Blog](https://decoder.cloud/)
* [Contact](https://decoder.cloud/contact/)

Search for:

Posted on [November 24, 2026November 24, 2026](https://decoder.cloud/2026/11/24/an-8088-640-kb-of-ram-and-a-really-bad-idea/) by [Decoder](https://decoder.cloud/author/decoderblogblog/)

# An 8088, 640 KB of RAM and a Really Bad Idea

# Why I built UMIX/86

For years, I had a crazy idea: to build a preemptive multitasking operating system for my old 8088 PC, with just 640 KB of RAM, a 5.25-inch floppy drive, a 20 MB hard disk, and MS-DOS as its original environment.

Of course, the idea itself is nothing new. Multitasking operating systems
ran on similar hardware decades ago. My goal wasn’t to reinvent the wheel,
but to build my own system from scratch, bring an old idea to life, and see
how far I could push this old machine with the help of AI.

**And it became a working system.**

None of this was magic. The hard part wasn’t the idea itself, but the
thousand small technical details, any one of which could bring the whole
system down.

Even transferring files was a pain. I first had to write a small
GW-BASIC script on the old PC so I could send the Telix communications
program from my workstation over the serial connection. Once Telix was
running, I could finally use ZMODEM for file transfers.

That was practically the only way I had to get the OS disk image onto
the old machine and write it to a 360 KB, 5.25-inch floppy disk.
Getting software onto the machine was a project in itself!

I also wanted my old 8088 to communicate over the Internet through
its 9600-baud serial port. So I built a serial-to-TCP/IP bridge and a
lightweight, X.25-inspired protocol to multiplex ten independent
terminal sessions over a single COM1 connection.

**An old PC, connected to the modern Internet through
a 9600-baud serial link! 😜**

I built UMIX/86 with the help of DeepSeek and GLM. I’m not an Assembly
developer, and I never pretended to be one. I brought the idea, the
vision, the specifications, and the hardware. They wrote the Assembly
code, explored solutions, caught race conditions, and chased bugs that
would have taken me an enormous amount of time to solve on my own.
Or perhaps I would never have finished it at all.

Is a multitasking OS for a processor architecture introduced almost
50 years ago useful in 2026?

Probably not. **But that’s not the point.**

Maybe AI won’t replace us. Maybe it will help us finally build the
projects we once thought were impossible, too difficult, or simply too
time-consuming. In the age of AI, perhaps the real advantage belongs to
people with ideas, curiosity, and the imagination to turn them into
reality. 😜

[More details about UMIX/86 »](https://decoder-it.gotdns.ch/UMX001.HTM)

***And yes, that link really points to a web server running
on my old 8088 PC!*** 😜

The modern workstation acts only as a serial-to-IP bridge.
UMIX/86 handles the requests and serves the content directly from
its own C: or M: drive, over a 9600-baud serial connection.

Of course, the system is still experimental and somewhat unstable,
so don’t expect 100% uptime! If the server is down, or you somehow
manage to crash it, well… remember, it’s a very old PC running a
homemade operating system. **What could possibly go wrong?**
😜

And here’s the actual machine running UMIX/86:
[A good old Commodore PC 20!](https://oldcomputer.info/pc/commodore20/index.htm)
😜

I’ll be publishing the source code on GitHub soon, for anyone
curious enough to explore it, experiment with it, or simply see how
this crazy little project works!

### Share this:

* [Share on X (Opens in new window)
  X](https://decoder.cloud/2026/11/24/an-8088-640-kb-of-ram-and-a-really-bad-idea/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://decoder.cloud/2026/11/24/an-8088-640-kb-of-ram-and-a-really-bad-idea/?share=facebook)

Like Loading...

# Post navigation

[Previous Article Oh MyAudi!](https://decoder.cloud/2026/05/08/oh-myaudi/)

### Leave a Reply [Cancel reply](/2026/11/24/an-8088-640-kb-of-ram-and-a-really-bad-idea/#respond)

Name

Email

Website

Turn on JavaScript to leave a comment.

Δ

## Search

Search for:

[Blog at WordPress.com.](https://wordpress.com/?ref=footer_blog)

* [Facebook](http://www.facebook.com)
* [LinkedIn](http://www.linkedin.com)
* [Twitter](http://www.twitter.com)
* [Instagram](http://www.instagram.com)

Privacy & Cookies: This site uses cookies. By continuing to use this website, you agree to their use.
To find out more, including how to control cookies, see here:
[Cookie Policy](https://automattic.com/cookies/)

* [Comment](https://decoder.cloud/2026/11/24/an-8088-640-kb-of-ram-and-a-really-bad-idea/#respond)
* Reblog
* Subscribe
  Subscribed

  [![](https://s-ssl.wordpress.com/i/logo/wpcom-gray-white.png?m=1479929237i)Decoder's Blog](https://decoder.cloud)

  Join 40 other subscribers

   Sign me up

  Have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fdecoder.cloud%252F2026%252F11%252F24%252Fan-8088-640-kb-of-ram-and-a-really-bad-idea%252F)
* [![](https://s-ssl.wordpress.com/i/logo/wpcom-gray-white.png?m=1479929237i)Decoder's Blog](https://decoder.cloud)

  [Copy shortlink](https://wp.me/p8ggv8-7R7)[View post in Reader](https://wordpress.com/reader/blogs/122087370/posts/30201)

  [Manage subscriptions](https://subscribe.wordpress.com/)[Sign up](https://wordpress.com/start/)[Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fdecoder.cloud%252F2026%252F11%252F24%252Fan-8088-640-kb-of-ram-and-a-really-bad-idea%252F)

  [Report this content](https://wordpress.com/abuse/?report_url=https://decoder.cloud/2026/11/24/an-8088-640-kb-of-ram-and-a-really-bad-idea/)

  Collapse this bar

%d

![](https://pixel.wp.com/b.gif?v=noscript)
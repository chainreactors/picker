---
title: Hilarious Buffer Overflow  Mitigation and TCL Injection in CheckPoint Gaia Portal
url: https://buaq.net/go-140304.html
source: unSafe.sh - 不安全
date: 2022-12-17
fetch_date: 2025-10-04T01:46:36.007364
---

# Hilarious Buffer Overflow  Mitigation and TCL Injection in CheckPoint Gaia Portal

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

![](https://8aqnet.cdn.bcebos.com/c0f65ac286c57735a42c08df216fc300.jpg)

Hilarious Buffer Overflow Mitigation and TCL Injection in CheckPoint Gaia Portal

Hey there,I am going to disclose two bug classes I found a while ago in CheckPoin
*2022-12-16 18:5:17
Author: [insinuator.net(查看原文)](/jump-140304.htm)
阅读量:30
收藏*

---

Hey there,

I am going to disclose two bug classes I found a while ago in CheckPoint R77.30: Two buffer overflows in the username (no shit) and HTTP method of a request to the administrative UI pre-auth and some interesting injections into the TCL web interface.

Let’s start with the TCL part. The web interface reacted pretty weird when a payload contained a colon. Diving deeper into this it became clear that a colon would actually cause an error from the TCL interpreter. By going down this rabbit hole and learning some TCL (:D) you could see that injecting a colon breaks some part of the application code, probably because colons are control characters in TCL e.g. preceding a global variable in TCL (::MyVar) or separating namespaces.

That’s bad. Reaching a point where the target application is giving you syntax errors because of your input is always a red flag. By diving into this and understanding the application code a bit more it turned out that you can actually set global variables in the TCL environment unauthenticated! A request to the TCL like this

will set a global variable *OMFG* with the value *wtf*. This behavior can not only be used to set new global variables (that will probably not be useful), but also to set existing ones. There are some that have a direct impact on the application logic, like *MP\_PREFIX*. This can be used to e.g., inject stuff into the response, therefore works like a reflected XSS. This increases the attack surface a lot and I leave it up to the reader to experiment. My assumption is, that the authenticated part will also have a bunch of nice logic flaws that can be abused in a similar way. I never checked. Ping me if you found something nice with this technique. 🙂

Checkpoint fixed the issue for the unauthenticated part by introducing something like global wrapper variables to ensure they are not being set via this mechanism. If you want to have a quick peek at the symptoms you can login to your Checkpoint (should also work for the latest version R81) and append the following after the session token in the URL:
 `/cgi-bin/home.tcl?::env(REMOTE_USER)=ERNW%22-alert('by%20ERNW')-%22`

This will result in a Reflected Cross-Site Scripting (XSS). Unfortunately, you have to know the session token in the URL to trigger this attack, so in the wild it should not be an issue. The session token in the URL kind of works like a XSRF protection, mitigating this specific XSS. Ping me if you think this is still exploitable.

Let’s move on to the buffer overflow. The TCL is mostly interpreted by a binary called *ipstcl2*. This binary uses multiple environment variables to do its work. Two of those environment variables are *REMOTE\_USER* and *REQUEST\_METHOD*. And now you probably guessed what happens. During the execution, both variables are copied to a fixed size buffer with *strcpy* resulting in a classic buffer overflow. A request like the following triggers the overflow for the username:
 `POST /cgi-bin/home.tcl HTTP/1.1
Host: 192.168.56.2
Cookie: Session=Login
[...]
Connection: close`

`userName=AAAAAAAAAAAAAAA[...]&userPass=admin`

The pseudo code in the binary looks like this:
 `remote_user = getenv("REMOTE_USER");
if ( remote_user )
{
blablabla;
strcpy(szUser, remote_user);
}`

Now let’s talk about why this is probably and unfortunately not exploitable. The overflow is into .bss. Normally, you would try to overflow into function pointers or interesting variables, or maybe try to reach the heap. In this case we need to overflow quite a bit to reach anything interesting (e.g. there are variables like *szScriptName* that might enable interesting attack ideas).

Overflowing into interesting parts seems to be mitigated in a hilarious way:

* Overflowing via setting the global variable ::env(REMOTE\_USER) in TCL via the technique mentioned above is not giving us anything. We have to use a GET to make the technique work and we are limited to 8139 chars for the value of the REMOTE\_USER variable. The web server will reply with a 414 Request-URI Too Large if we supply more chars and nothing reaches our application logic.
* But who cares about GET. We can at least use the POST request from above specifying the username directly to bypass the GET limitation. Now, the problem with this approach is that our username variable will be written to the environment variables of the OS (the approach above bypasses this and sets the TCL global variable directly), and we also have a limit for the size of the environment variable REMOTE\_USER: around 8183 chars (depending on the size of the other environment variables).

All of this would not be a problem. We could reach interesting variables or function pointers within the next 8k bytes easily. But now to the hilarious part:

* The number of chars is not only limited by the Request-URI and the size of environment variables, but also by a variable that comes right after the variables we are overflowing. The layout looks like that:

![](https://insinuator.net/wp-content/uploads/2022/11/var_Layout.png)

*szUser* or *szMethod* are the variables that we can overflow. Additionally, there is this annoying and unused “guard variable” *szHelpBuf* that does nothing and seems to be here just to provide a buffer space of 65k right after the two problematic variables. This additionally limits the possibility to overflow into something interesting right after that guard variable. WTF?

I refuse to believe that this ends the story, this doesn’t seem like a sane way of mitigating a buffer overflow. If you have any ideas on how to get around this, let me know! 😀

CheckPoint has fixed the buffer overflow with *strncpy* and introduced wrapper variables used in most parts of the unauthenticated TCLs to ensure they are not being set from the outside. Later versions do not seem to be vulnerable to the buffer overflow and at least not to the unauthenticated injection of TCL variables.

Let me know what you think! Enjoy your upcoming holidays!

Cheers,

Flo

M: https://chaos.social/@0x79
T: https://twitter.com/0x79

## Post navigation

文章来源: https://insinuator.net/2022/12/hilarious-buffer-overflow-mitigation-and-tcl-injection-in-checkpoint-gaia-portal/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
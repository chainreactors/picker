---
title: Registry FeatureUsage
url: http://windowsir.blogspot.com/2025/11/registry-featureusage.html
source: Instapaper: Unread
date: 2025-11-28
fetch_date: 2025-11-29T03:13:01.087738
---

# Registry FeatureUsage

# [Windows Incident Response](http://windowsir.blogspot.com/)

The Windows Incident Response Blog is dedicated to the myriad information surrounding and inherent to the topics of IR and digital analysis of Windows systems. This blog provides information in support of my books; "Windows Forensic Analysis" (1st thru 4th editions), "Windows Registry Forensics",
as well as the book I co-authored with Cory Altheide, "Digital Forensics with Open Source Tools".

## Wednesday, November 26, 2025

### Registry: FeatureUsage

[Maurice](https://www.linkedin.com/in/mauricefielenbach/) [posted on LinkedIn](https://www.linkedin.com/posts/mauricefielenbach_threatintel-threathunting-infostealer-activity-7398793861206212609-AycP/) recently about one of the *FeatureUsage* Registry key subkeys; specifically, the *AppSwitched* subkey. Being somewhat, maybe even only slightly aware of the Windows Registry, I read the post with casual, even mild interest.

Someone posted recently that cybersecurity runs on caffeine and sarcasm...I've got my cup of coffee right in front of me, and I've placed the sarcasm in front of us all.  ;-)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJDYa7LzI5yU4pAyGbupASIdYz8iOHA8yG-Q13PEJU_ykS0SDT7JAF29CARYvKjZQrKN_2ZN6JJwn7joEXKfSAEZZIL2oXV1H03QukEp9X6wv9WBOd07J2V0xEiirKxPWehtottSqPZIMJxVL06LFCQYu14lVrcMmrYPpet9YcFLlRFptMWQ/s320/appswitched.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJDYa7LzI5yU4pAyGbupASIdYz8iOHA8yG-Q13PEJU_ykS0SDT7JAF29CARYvKjZQrKN_2ZN6JJwn7joEXKfSAEZZIL2oXV1H03QukEp9X6wv9WBOd07J2V0xEiirKxPWehtottSqPZIMJxVL06LFCQYu14lVrcMmrYPpet9YcFLlRFptMWQ/s745/appswitched.png)

The RegRipper [featureusage plugin](https://github.com/keydet89/RegRipper3.0/blob/master/plugins/featureusage.pl) was originally written in 2019, and includes a reference to a [Crowdstrike blog post](https://www.crowdstrike.com/en-us/blog/how-to-employ-featureusage-for-windows-10-taskbar-forensics/) written in 2020, authored by [Jai Minton](https://www.linkedin.com/in/jaiminton/) (who is now with Huntress). The figure to the right was captured from the blog post, and provides a succinct description of how the *AppSwitched* key is populated. Specifically, Jai stated, "This key provides the number of times an application switched focus (was left-clicked on the taskbar)." This helps us understand a bit more about process execution, as for the application to exist on the taskbar and to have it's focus switched, that application has to have been executed.

After finding and reading the blog post, I wrote [a brief blog](https://windowsir.blogspot.com/2020/06/plugin-spotlight-printersettings.html) post here on this blog that mentioned the Registry key, and referenced Jai's blog post.

To Maurice's point, this is, in fact, a valuable artifact, so kudos to Maurice for pointing it out and mentioning it again. If you read through the comments to Maurice's post, there are some hints there as to how to use the value data in your analysis. As you'll note, neither the value names nor the data itself  includes a timestamp, but the *AppSwitched* subkey does have a LastWrite time, and this can be included in a timeline. The value names can be used as pivot points into a timeline, adding something of a "third dimension" to timeline analysis. You can use this alongside timestamped information, such as Prefetch entries, Registry data, SRUM DB data, etc.

Posted by
H. Carvey

at
[9:40 AM](http://windowsir.blogspot.com/2025/11/registry-featureusage.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/9518042/6098321519193259126 "Email Post")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=9518042&postID=6098321519193259126&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=9518042&postID=6098321519193259126&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=9518042&postID=6098321519193259126&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=9518042&postID=6098321519193259126&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=9518042&postID=6098321519193259126&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=9518042&postID=6098321519193259126&target=pinterest "Share to Pinterest")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/9518042/6098321519193259126)

[Older Post](http://windowsir.blogspot.com/2025/11/unprecedented-complexity.html "Older Post")
[Home](http://windowsir.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://windowsir.blogspot.com/feeds/6098321519193259126/comments/default)

## Pages

* [Home](http://windowsir.blogspot.com/)
* [Timelines](http://windowsir.blogspot.com/p/timelines.html)
* [Books](http://windowsir.blogspot.com/p/books.html)
* [Malware](http://windowsir.blogspot.com/p/malware.html)
* [FOSS Tools](http://windowsir.blogspot.com/p/foss-tools.html)

## Subscribe To WindowsIR

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Posts

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=http%3A%2F%2Fwindowsir.blogspot.com%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=http%3A%2F%2Fwindowsir.blogspot.com%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](http://windowsir.blogspot.com/feeds/posts/default)

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)

![](https://resources.blogblog.com/img/icon_feed12.png)
Posts

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Comments

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=http%3A%2F%2Fwindowsir.blogspot.com%2Ffeeds%2F6098321519193259126%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=http%3A%2F%2Fwindowsir.blogspot.com%2Ffeeds%2F6098321519193259126%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](http://windowsir.blogspot.com/feeds/6098321519193259126/comments/default)

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)

![](https://resources.blogblog.com/img/icon_feed12.png)
Comments

## WindowsIR Blog List

* ![]()

  [Brett Shavers](https://brettshavers.com/brett-s-blog)

  [Fight City Hall: If You Missed the Webinar, You’re Making Mistakes You
  Don’t Know About](https://brettshavers.com/brett-s-blog/entry/fight-city-hall-if-you-missed-the-webinar-youre-making-mistakes-you-dont-know-about)

  2 weeks ago
* ![]()

  [The Philosophy of DFIR](https://dfirphilosophy.blogspot.com/)

  [Selling the Science: Marketing of DF/IR Services](https://dfirphilosophy.blogspot.com/2025/11/selling-science-marketing-of-dfir.html)

  3 weeks ago
* ![]()

  [c-APT-ure](https://c-apt-ure.blogspot.com/)

  [Using NetBIOS names for pivoting and threat clustering](https://c-apt-ure.blogspot.com/2025/10/using-netbios-names-for-pivoting-and.html)

  1 month ago
* ![]()

  [Open Source DFIR](https://osdfir.blogspot.com/)

  [Less is More](https://osdfir.blogspot.com/2025/09/less-is-more.html)

  2 months ago
* ![]()

  [dfirtnt.wordpress.com](https://dfirtnt.wordpress.com)

  [Huntable – AI Assistant for Tactical Threat Intel](https://dfirtnt.wordpress.com/2025/08/06/huntable-gpt-tactical-threat-intelligence-assistant/)

  3 months ago
* ![]()

  [CyberDefNerd](https://cyberdefnerd.com)

  [Xworm – Static Analysis (part 3)](https://cyberdefnerd.com/2025/08/04/xworm-static-analysis-part-3/)

  3 months ago
*...
---
title: What Are Normal Users Supposed to Do with IDS Alerts from Network Gear?
url: https://taosecurity.blogspot.com/2024/10/what-are-normal-users-supposed-to-do.html
source: TaoSecurity Blog
date: 2024-10-12
fetch_date: 2025-10-06T18:55:45.193692
---

# What Are Normal Users Supposed to Do with IDS Alerts from Network Gear?

[Skip to main content](#main)

### Search This Blog

# [TaoSecurity Blog](https://taosecurity.blogspot.com/)

Richard Bejtlich's blog on digital security, strategic thought, and military history.

### What Are Normal Users Supposed to Do with IDS Alerts from Network Gear?

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[October 11, 2024](https://taosecurity.blogspot.com/2024/10/what-are-normal-users-supposed-to-do.html "permanent link")

Probably once a week, I see posts like this in the [r/Ubiquiti](https://www.reddit.com/r/Ubiquiti/) subreddit. Ubiquiti makes network gear that includes an "IDS/IPS" feature. I own some older Ubiquiti gear so I am familiar with the product.

When you enable this feature, you get alerts like this one, posted by a Redditor:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0XO6m_cF0RF1_CSnhHJFJInxpor6-KqKuZdffTPD2OLbkxE2bRmfl1FAcxhE5eUm6LnXOSoY7YvitvZdVBpV5lHV80gTSBouQnxfbtf2GQpD8spRByeYqPV7Bi54GTTIyG0uFF_8jhlBAq4mdenRp5HrV9omP3ynmlJZkNhz2MYfzRGW5oZ7D/w292-h640/help-me-understand-this-exploit-alert-v0-95ce20g025ud1.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0XO6m_cF0RF1_CSnhHJFJInxpor6-KqKuZdffTPD2OLbkxE2bRmfl1FAcxhE5eUm6LnXOSoY7YvitvZdVBpV5lHV80gTSBouQnxfbtf2GQpD8spRByeYqPV7Bi54GTTIyG0uFF_8jhlBAq4mdenRp5HrV9omP3ynmlJZkNhz2MYfzRGW5oZ7D/s907/help-me-understand-this-exploit-alert-v0-95ce20g025ud1.webp)

This is everything you get from Ubiquiti.

The Redditor is concerned that their system may be trying to compromise someone on the Internet.

This is my [answer](https://www.reddit.com/r/Ubiquiti/comments/1g1bd19/comment/lrfxrk5/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) to how to handle these alerts.

==

This is another example of this sort of alert being almost worthless for most users.

The key is trying to understand what COULD have caused the alert to trigger. CVEs, whatever, are irrelevant at this point.

Here is one way to get SOME idea of what is happening.

Go to

<https://rules.emergingthreats.net/open/suricata-7.0.3/rules/>

Download the file that is named as the first part of the alert. Here that is EXPLOIT.

<https://rules.emergingthreats.net/open/suricata-7.0.3/rules/emerging-exploit.rules>

Find the rule that fired. This can take some digging. Here is what I ended up doing.

**grep -i possible emerging-exploit.rules | grep -i log4j | grep -i obfuscation | grep -i udp | grep -i outbound**

Here it is.

alert udp $HOME\_NET any -> any any (msg:"ET EXPLOIT Possible Apache log4j RCE Attempt - 2021/12/12 Obfuscation Observed M2 (udp) (Outbound) (CVE-2021-44228)"; content:"|24 7b|"; content:"|24 7b 3a 3a|"; within:100; fast\_pattern; reference:cve,2021-44228; classtype:attempted-admin; sid:2034805; rev:3; metadata:attack\_target Server, created\_at 2021\_12\_18, cve CVE\_2021\_44228, deployment Perimeter, deployment Internal, signature\_severity Major, tag Exploit, updated\_at 2023\_06\_05, mitre\_tactic\_id TA0001, mitre\_tactic\_name Initial\_Access, mitre\_technique\_id T1190, mitre\_technique\_name Exploit\_Public\_Facing\_Application;)

You can ignore 90% of this. The key is here:

content:"|24 7b|"; content:"|24 7b 3a 3a|"; within:100

and here:

udp $HOME\_NET any -> any any

Now, you have to guess how likely it might be there you could have ANY UDP traffic from your home network to anywhere, on any ports, that contain this string

24 7b

followed by this string

24 7b 3a 3a

within the next 100 bytes?

I'm guessing there's a decent chance that could happen in random, normal traffic.

Therefore, without any other evidence, I think you can ignore this alert.

If you want to have a better chance at understanding this in the future, please feel free to check out anything I've written about network security monitoring. Good luck!

==

This problem is why I have promoted network security monitoring since 1998 and subtitled my first book "Beyond Intrusion Detection." Network intrusion detection, by itself, with no supporting data and without even rule explanations, is almost worthless.

Thankfully in this case the vendor is at least using an open rule set, enabling this feeble exploration.

[nsm](https://taosecurity.blogspot.com/search/label/nsm)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Comments

[Post a Comment](https://www.blogger.com/comment/fullpage/post/4088979/975032447879323114)

### Popular posts from this blog

### [Zeek in Action Videos](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html)

[July 29, 2021](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcWFyS3aGQrT6UiiiBbLkOiUs5W_Y9cYMLeH2Z7KkzzqINSWjFIEG8inSUNbYNGTjF7dcEUOOOkK7DzHQXcNMY3Nhl1PIFsdZZeJOH7bzRzpQMUdez5M7_g3t_xyygra49FBKK/w640-h360/capture_001_29072021_143006.jpg)](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html)

This is a quick note to point blog readers to my Zeek in Action YouTube video series for the Zeek network security monitoring project .  Each video addresses a topic that I think might be of interest to people trying to understand their network using Zeek and adjacent tools and approaches, like Suricata, Wireshark, and so on.  I am especially pleased with Video 6 on monitoring wireless networks . It took me several weeks to research material for this video. I had to buy new hardware and experiment with a Linux distro that I had not used before -- Parrot .  Please like and subscribe, and let me know if there is a topic you think might make a good video.

[Read more](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html "Zeek in Action Videos")

### [MITRE ATT&CK Tactics Are Not Tactics](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html)

[October 23, 2020](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh8UtkHOxII5KLGuTgeVk3iVj3KMfkoFLyDb11MrasYGQ9J2Q5NPBgNUX4-Dk5YKF_26s2quTQ_ve4bEh4yIF1H97CJeNqoGqlpAATJPzThQ_IGALsANV3MZLlF_zogZNHM-LI/s320/on+tactics.jpg)](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html)

Just what are "tactics"? Introduction MITRE ATT&CK  is a great resource, but something about it has bothered me since I first heard about it several years ago. It's a minor point, but I wanted to document it in case it confuses anyone else. The MITRE ATT&CK Design and Philosophy document from March 2020 says the following: At a high-level, ATT&CK is a behavioral model that consists of the following core components: • Tactics, denoting short-term, tactical adversary goals during an attack; • Techniques, describing the means by which adversaries achieve tactical goals; • Sub-techniques, describing more specific means by which adversaries achieve tactical goals at a lower level than techniques; and • Documented adversary usage of techniques, their procedures, and other metadata. My concern is with MITRE's definition of "tactics" as "short-term, tactical adversary goals during an attack," which is oddly recursive. The key word in the tacti...

[Read more](https://taosecurity.blogspot.com/2020/10/mitre-att-tactics-are-not-tactics.html "MITRE ATT&CK Tactics Are Not Tactics")

### [New Book! The Best of TaoSecurity Blog, Volume 4](https://taosecurity.blogspot.com/2021/04/new-book-best-of-taosecurity-blog.html)

[April 13, 2021](https://taosecurity.blogspot.com/2021/04/new-book-best-of-taosecurity-blog.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhe6YF9WJiKp0uULA6gH7y4zgy_L4W5xkOUmCV3fENBessbRL3bdnf6xy2y-uWNS1ScWWzyQ5qBL56XVyeknUtWhFk29Ol6pGst3H78RCAT2c53h7VCq4bU00BGhRhXRygZs8kZ/w400-h640/The+Best+of+TaoSecurity+Blog%252C+Volume+4.jpg)](https://taosecurity.blogspot.com/2021/04/new-book-best-of-taosecurity-blog.html)

I've completed...
---
title: Profiling a Russia-Based Bulletproof Hosting Provider - An Analysis
url: https://ddanchev.blogspot.com/2022/10/profiling-russia-based-bulletproof.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2022-11-01
fetch_date: 2025-10-03T21:25:08.925049
---

# Profiling a Russia-Based Bulletproof Hosting Provider - An Analysis

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

Independent Contractor. Bitcoin: 15Zvie1j8CjSR52doVSZSjctCDSx3pDjKZ Email: dancho.danchev@hush.com OMEMO: ddanchev@conversations.im | OTR: danchodanchev@xmpp.jp | TOX ID: 53B409440A6DC34F1BA458869A0462D92C15B467AF6319D481CA353690C88667833A0EE82969

## Monday, October 31, 2022

### Profiling a Russia-Based Bulletproof Hosting Provider - An Analysis

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEica0mosec-AMkEdDNmWOL7FOf3U1BSCXHc1Uq7SZGpfzuDs1SMnoExA6bpK3sHbpZxZ0Loop1Eui7-xH5zc82cKlWxOYWrzPxwlEQnHXa4FoTWgm02g5xS2K2i-v5ZI_650OhLmaf1wK970ulCmT5fPw36qlUYD6J1bFIrhNVzhyFBar_m9A/s320/abuzhost_1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEica0mosec-AMkEdDNmWOL7FOf3U1BSCXHc1Uq7SZGpfzuDs1SMnoExA6bpK3sHbpZxZ0Loop1Eui7-xH5zc82cKlWxOYWrzPxwlEQnHXa4FoTWgm02g5xS2K2i-v5ZI_650OhLmaf1wK970ulCmT5fPw36qlUYD6J1bFIrhNVzhyFBar_m9A/s1280/abuzhost_1.png)

It should be clearly noted that in today's modern cybercrime ecosystem which is largely driven by the existence of bulletproof hosting providers which basically either ignore abuse notifications or on purposely launch rogue and fraudulent online hosting operations using their own resources or in combination with cloud-based service providers who unknowingly participate in such type of fraudulent and rogue bulletproof hosting schemes including actual malicious software spam and botnet C&C hosting we've continuing to observe an increase in the overall volume of these providers where we're also witnessing their use by both novice and experienced cybercriminals where the ultimate goal would be to increase the average time it takes for vendors organizations and researchers to take offline their rogue fraudulent and malicious campaigns.

In this post I'll discuss several of the high-profile bulletproof hosting providers that were active circa 2010 and I'll provide some actionable intelligence on the infrastructure behind them with the idea to assist everyone in their cyber attack and cyber campaign attribution efforts.

* **Recommended reading** - [Historical OSINT - How TROYAK-AS Utillized BGP-Over-VPN To Serve The Avalance Botnet](https://ddanchev.blogspot.com/2015/08/historical-osint-how-troyak-as.html)

**Sample screenshots include:**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEio51Fr9SBHwWaBZPrqIlUwYHF3sK30cvvel6Qdb1lLSYDLmz6EvQ_9R7tqr_WDP9B6Lwx3kxGqpPEqUVwO6FkS-rlNr1W2UgbEjytcnE3KdYtWNRgs4El2eteRv32ofp98CM-XFT52YtiMhXhR0YC1zH-YWZlq5j1Sk056ZcyVmI6NcT1Fgg/s320/abuzhost_2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEio51Fr9SBHwWaBZPrqIlUwYHF3sK30cvvel6Qdb1lLSYDLmz6EvQ_9R7tqr_WDP9B6Lwx3kxGqpPEqUVwO6FkS-rlNr1W2UgbEjytcnE3KdYtWNRgs4El2eteRv32ofp98CM-XFT52YtiMhXhR0YC1zH-YWZlq5j1Sk056ZcyVmI6NcT1Fgg/s859/abuzhost_2.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj29vXK5DNAtdAgQPKkFw4DLmH22MjymI0Jul7136hbq8DUXDK-6LV4n9BQAUgUgB_CRA5vaCFpseU2NaAB5fIpQy23uxn-jZnea8B3nHE7bqAa1Cr307dMbJWyYWhUif4zcSbO0FbBo7D9SvIXrZHHZlIegH13hZUciAkJhOfZ01nlgyPnzw/s320/skrin4.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj29vXK5DNAtdAgQPKkFw4DLmH22MjymI0Jul7136hbq8DUXDK-6LV4n9BQAUgUgB_CRA5vaCFpseU2NaAB5fIpQy23uxn-jZnea8B3nHE7bqAa1Cr307dMbJWyYWhUif4zcSbO0FbBo7D9SvIXrZHHZlIegH13hZUciAkJhOfZ01nlgyPnzw/s1259/skrin4.jpg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcGD1ur_FKrceFe3ldu_KqQ14JGkx0e4u04wobeOhOdvn0j17Tfa47QVkdZDjcO_BKK9D1xsEZcTEMeR5uL8cAJN0deLDMWCqUocyjDobL_FIBaSfl1683OC_NEefDNzXLEMUiOJWGcTyBBxHeENeZK3P_sQ5GiATWok0IP84ISG8O6YoM8g/s320/skrin3.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcGD1ur_FKrceFe3ldu_KqQ14JGkx0e4u04wobeOhOdvn0j17Tfa47QVkdZDjcO_BKK9D1xsEZcTEMeR5uL8cAJN0deLDMWCqUocyjDobL_FIBaSfl1683OC_NEefDNzXLEMUiOJWGcTyBBxHeENeZK3P_sQ5GiATWok0IP84ISG8O6YoM8g/s1260/skrin3.jpg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiakwepsot1wae3F-SLVOircDQ3WIzPKR7aTY2fU_LTpIoA0hVCaR3AmwzVfViGQVuMnxyPbZ03k_kRo89m1qIu0n7QoBBhW3FADNG9VITTH6SQrqW9j9kPjXVo-2SzpfvG3SWU2K-ADSGzQ4YshFDHOOJsknPpayz7QvfdX645KY1X6VmY2A/s320/skrin2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiakwepsot1wae3F-SLVOircDQ3WIzPKR7aTY2fU_LTpIoA0hVCaR3AmwzVfViGQVuMnxyPbZ03k_kRo89m1qIu0n7QoBBhW3FADNG9VITTH6SQrqW9j9kPjXVo-2SzpfvG3SWU2K-ADSGzQ4YshFDHOOJsknPpayz7QvfdX645KY1X6VmY2A/s1260/skrin2.jpg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6JFGgYxkSmzr1rwRcOQ5rUeANTsuPURhOsStlTEigF1KjcPDJCO6YwAO08pr8jo2R3pP__ElrtI9uhmMgRWoU4eHc3Pp7DYVcHzG0CPl-KP-CLXvNBUOcLWYRtCAgCMzz82CSsNZg9nE2J7psrQ4bn4plHGLk3CSOZQXbyRupPj8L60CI9A/s320/skrin1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6JFGgYxkSmzr1rwRcOQ5rUeANTsuPURhOsStlTEigF1KjcPDJCO6YwAO08pr8jo2R3pP__ElrtI9uhmMgRWoU4eHc3Pp7DYVcHzG0CPl-KP-CLXvNBUOcLWYRtCAgCMzz82CSsNZg9nE2J7psrQ4bn4plHGLk3CSOZQXbyRupPj8L60CI9A/s1280/skrin1.jpg)

**Related bulletproof hosting providers that were active back in 2010 include:**

hxxp://securehost.com

hxxp://ccihosting.com

hxxp://wrzhost.com

hxxp://underhost.com

hxxp://shinjiru.com

hxxp://offshorehosting.com

hxxp://offshoreracks.com

hxxp://hostimizer.com

hxxp://zentek-international.com

hxxp://anonhoster.com

hxxp://webcare360.com

hxxp://altushost.com

hxxp://anonymoushosting.org

hxxp://nodmca.nl

hxxp://goip.com

hxxp://serverslease.net

hxxp://e-investhost.com

hxxp://eukhost.com

hxxp://adulthosting.com

hxxp://webhostingchoice.com

hxxp://adulthostingservers.com

hxxp://hostsearch.com

hxxp://adult-host.ru

hxxp://layeredlink.ru

hxxp://xlhost.ru

hxxp://park-web.ru

hxxp://web750.com

hxxp://cirtexhosting.com

hxxp://wlw.su

hxxp://warez-host.com

hxxp://abuzhost.ru

hxxp://peterhost.ru

hxxp://fastvps.ru

Stay tuned!

-
[October 31, 2022](https://ddanchev.blogspot.com/2022/10/profiling-russia-based-bulletproof.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/18493443/8858667942370335017 "Email Post")

[Email This](https://www.blogger.com/share-post.g?blogID=18493443&postID=8858667942370335017&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=18493443&postID=8858667942370335017&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=18493443&postID=8858667942370335017&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=18493443&postID=8858667942370335017&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=18493443&postID=8858667942370335017&target=pinterest "Share to Pinterest")

![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimxCSbi25rfvHIa7H8x-VuFqcOZaIMyVWQpCC9QOCEqIoU3vgZwnlXz5Ee7Vhoel0LK4iK1XrVIxlaCPLV4nO66Ug2qFireNLDJ4DxzdyEX0ce7Z-zJlEEBx8T6U-xDQ/s113/126817412_103684408239911_5047637022297351917_n.jpg)

[Dancho Danchev](https://www.blogger.com/profile/09989733095447891258 "author profile")

Independent Security Consultancy, Threat Intelligence Analysis (OSINT/Cyber Counter Intelligence) and Competitive Intelligence research on demand. Insightful, unbiased, and client-tailored assessments, neatly communicated in the form of interactive reports - because anticipating the emerging threatscape is what shapes the big picture at the end of the day. Approach me at dancho.danchev@hush.com

#### No comments:

#### Post a Comment

[Newer Post](https://ddanchev.blogspot.com/2022/10/a-peek-inside-russian-web-based-managed.html "Newer Post")

[Older Post](https://ddanchev.blogspot.com/2022/10/do-you-want-to-become-guest-blogger-or.html "Older Post")
[Home](https://ddanchev.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://ddanchev.blogspot.com/feeds/8858667942370335017/comments/default)

[![Web Analytics Made Easy - Statcounter](https://c.statcounter.com/1212632/0/91125b67/1/)](https://statcounter.com/ "Web Analytics Made Easy - Statcount...
---
title: Yanluowang's Ransomware Group's Internal Communications Leaked by Russian Threat Actors - An Analysis
url: https://ddanchev.blogspot.com/2022/11/yanluowangs-ransomware-groups-internal.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2022-11-02
fetch_date: 2025-10-03T21:31:32.846182
---

# Yanluowang's Ransomware Group's Internal Communications Leaked by Russian Threat Actors - An Analysis

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

Independent Contractor. Bitcoin: 15Zvie1j8CjSR52doVSZSjctCDSx3pDjKZ Email: dancho.danchev@hush.com OMEMO: ddanchev@conversations.im | OTR: danchodanchev@xmpp.jp | TOX ID: 53B409440A6DC34F1BA458869A0462D92C15B467AF6319D481CA353690C88667833A0EE82969

## Tuesday, November 01, 2022

### Yanluowang's Ransomware Group's Internal Communications Leaked by Russian Threat Actors - An Analysis

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLXOcQfa1tOFsWepWtKvTVYljEnH_mkuwKUXiGXwaQG3jdaIOjweKOt183fKcctPgAbYRC9_kOWp0qM3t1ec2gD2QxSmtyMtfRs_kPL6ApmHEmfmdWjKWLsuLVg-iRxylg5J8r0PjmyYlZ_OSR7izIw-JAemUto-UohF-uB0xwDQJNqpIWtg/s320/Screenshot_57.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLXOcQfa1tOFsWepWtKvTVYljEnH_mkuwKUXiGXwaQG3jdaIOjweKOt183fKcctPgAbYRC9_kOWp0qM3t1ec2gD2QxSmtyMtfRs_kPL6ApmHEmfmdWjKWLsuLVg-iRxylg5J8r0PjmyYlZ_OSR7izIw-JAemUto-UohF-uB0xwDQJNqpIWtg/s1556/Screenshot_57.png)

Yanluowang's ransomware group has recently had their internal communications leak online prompting various researcher into looking into them and analyzing them. The breach of the gang's internal communications happened courtesy of Russian threat actors who also defaced and left a message on their front page.

The leak's initiative has also released various source code in terms of the decryption tool for the ransomware including the source code of the builder.

**Sample screenshots include:**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhVlXBn3-Wj26TOqCiKwIjo-ksbWXh59ZlV4mBO3CGuk_SxFjugBE7T02fjFUItJd6EmH84n3NnfD6FufwJh67SB2PfyS2OJhfqs_SwjA-cbDYKTW7DJxL9eY3tmQ00H2vR0S0_dDyT67jxmu-Xsf6_6N5HRnTMcOCWZm2Jkdko57-ZhZ28Q/s320/Screenshot_58.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhVlXBn3-Wj26TOqCiKwIjo-ksbWXh59ZlV4mBO3CGuk_SxFjugBE7T02fjFUItJd6EmH84n3NnfD6FufwJh67SB2PfyS2OJhfqs_SwjA-cbDYKTW7DJxL9eY3tmQ00H2vR0S0_dDyT67jxmu-Xsf6_6N5HRnTMcOCWZm2Jkdko57-ZhZ28Q/s1067/Screenshot_58.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiE1yomRZhVZaqdqHZ3P3kkZMpzlEza4nCPCh6s6ajENGfT5XF8GYSssvbxooZJPgc67ygt5Dra-Z1EPNiSpUdIur4faBEFbtDSDgi8JSIMN8-W6uPBvJoSIBfC6rkuPzjf3oudPj1zDL1klDo3dFNj-DI_QxLNb2AzO6RLCIczqxtKhtM6HA/s320/Screenshot_59.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiE1yomRZhVZaqdqHZ3P3kkZMpzlEza4nCPCh6s6ajENGfT5XF8GYSssvbxooZJPgc67ygt5Dra-Z1EPNiSpUdIur4faBEFbtDSDgi8JSIMN8-W6uPBvJoSIBfC6rkuPzjf3oudPj1zDL1klDo3dFNj-DI_QxLNb2AzO6RLCIczqxtKhtM6HA/s1077/Screenshot_59.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBz_THNRXc8Or4yOpQArZ_pcYO0brD3gLg_OK-7t1RaPgDvBL-q-xdXcCnObhldIUM2rB6HWYAemOF9__9-fyWOEGw1ncK-lOiTVM9naLC8U94lqP1Vp2Em0EjbT_KZWB7QEzyQ5b8tSHni5BTL_O0CQK_WFisKlqmuU0smonByrBlb8rqaw/s320/Screenshot_60.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBz_THNRXc8Or4yOpQArZ_pcYO0brD3gLg_OK-7t1RaPgDvBL-q-xdXcCnObhldIUM2rB6HWYAemOF9__9-fyWOEGw1ncK-lOiTVM9naLC8U94lqP1Vp2Em0EjbT_KZWB7QEzyQ5b8tSHni5BTL_O0CQK_WFisKlqmuU0smonByrBlb8rqaw/s598/Screenshot_60.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcQua9iqYe1EMQBKLwM84NOFABG8NBS7AI6xbdxsGKL2RZDKCU_iLZFEvJoe5EP5pFpmrW8zov_o-SyRZjjRb_Ua_ZNOsrMxW40I4TI6OLIfJQCbtWWuymcOnStbd7k1B31SCXP1tPrav5isJcZcZ4Asdt4J6G4U9tfFbjxLMZKEXZMJ66JA/s320/Screenshot_63.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcQua9iqYe1EMQBKLwM84NOFABG8NBS7AI6xbdxsGKL2RZDKCU_iLZFEvJoe5EP5pFpmrW8zov_o-SyRZjjRb_Ua_ZNOsrMxW40I4TI6OLIfJQCbtWWuymcOnStbd7k1B31SCXP1tPrav5isJcZcZ4Asdt4J6G4U9tfFbjxLMZKEXZMJ66JA/s376/Screenshot_63.png)

The recent communication leaks are similar to the Conti leaks which I extensively data mined and profiled [here](https://ddanchev.blogspot.com/2022/02/exposing-conti-ransomware-gang-osint_28.html).

**Related actionable intelligence on the C&C server infrastructure:**

hxxp://mtololo.com - 81.19.72.59

hxxp://matrix.mtololo.com - 62.113.100.124

**Related domains known to have been involved in the campaign:**

hxxp://api.views-24.ru

hxxp://lohicageeg.beget.app

hxxp://fr124.aha.ru

hxxp://aktiver-id.fun

hxxp://aktiver-bankid.website

hxxp://matrix.mtololo.com

Stay tuned!

-
[November 01, 2022](https://ddanchev.blogspot.com/2022/11/yanluowangs-ransomware-groups-internal.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/18493443/2290506345249340673 "Email Post")

[Email This](https://www.blogger.com/share-post.g?blogID=18493443&postID=2290506345249340673&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=18493443&postID=2290506345249340673&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=18493443&postID=2290506345249340673&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=18493443&postID=2290506345249340673&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=18493443&postID=2290506345249340673&target=pinterest "Share to Pinterest")

![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimxCSbi25rfvHIa7H8x-VuFqcOZaIMyVWQpCC9QOCEqIoU3vgZwnlXz5Ee7Vhoel0LK4iK1XrVIxlaCPLV4nO66Ug2qFireNLDJ4DxzdyEX0ce7Z-zJlEEBx8T6U-xDQ/s113/126817412_103684408239911_5047637022297351917_n.jpg)

[Dancho Danchev](https://www.blogger.com/profile/09989733095447891258 "author profile")

Independent Security Consultancy, Threat Intelligence Analysis (OSINT/Cyber Counter Intelligence) and Competitive Intelligence research on demand. Insightful, unbiased, and client-tailored assessments, neatly communicated in the form of interactive reports - because anticipating the emerging threatscape is what shapes the big picture at the end of the day. Approach me at dancho.danchev@hush.com

#### No comments:

#### Post a Comment

[Newer Post](https://ddanchev.blogspot.com/2022/11/my-old-twitter-account-sample-twitter.html "Newer Post")

[Older Post](https://ddanchev.blogspot.com/2022/10/a-peek-inside-earnings4u-managed.html "Older Post")
[Home](https://ddanchev.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://ddanchev.blogspot.com/feeds/2290506345249340673/comments/default)

[![Web Analytics Made Easy - Statcounter](https://c.statcounter.com/1212632/0/91125b67/1/)](https://statcounter.com/ "Web Analytics Made Easy - Statcounter")

## Wikipedia Draft

[Shoutcast Hosting](https://www.caster.fm) [Stream Hosting](https://www.caster.fm) [Radio Server Hosting](https://www.caster.fm)

## Followers

[![Clicky](//static.getclicky.com/media/links/badge.gif)](https://clicky.com/101422166 "Privacy-friendly Web Analytics")

## This Blog - 2005 - 2024

[![This Blog - 2005 - 2024](https://blogger.googleusercontent.com/img/a/AVvXsEglFTGC9ReBriBRRDJHu0UpCxPcZ28KUFPwLqLVYhrY-_4Pjo5dB1FXbWpfStmu2IVfXoU7srml6TDcFnvdwEJ1HKHD6xM8kV6HbZJfpPGC5zzUJjPD5Adu3IFFCAW_4vVDKsQN6Bq0bOt9hb6VUBQ6Ek7cF2dC55e6H7f1vJd6FJVfFWQzZczc=s302)](https://web.archive.org/web/20240000000000%2A/ddanchev.blogspot.com)

## Astalavista.com

[![Astalavista.com](https://blogger.googleusercontent.com/img/a/AVvXsEgfBngbw2oNmVoIq0oK494_i9CUAmtx4JRo1XIESvEVatJyDC_RVWXZL7YCBHl1dzPthpW61flqs6EXrg9gUfQc8uRnfrfMFiOzC_NJRCKAtpJNaSfsDLnZxRfMAVk6Ix3MhpR3Y8H8KHgLBJba6mjVFKOacste9--uVG3ZSRFbpVUVjEdZa8je=s302)](https://astalavista.com)

![](https://www.paypalobjects.com/en_US/i/scr/pixel.gif)

## About Me

[![My photo](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimxCSbi25rfvHIa7H8x-VuFqcOZaIMyVWQpCC9QOCEqIoU3vgZwnlXz5Ee7Vhoel0LK4iK1XrVIxlaCPLV4nO66Ug2qFireNLDJ4DxzdyEX0ce7Z-zJlEEBx8T6U-xDQ/s113/126817412_103684408239911_5047637022297351917_n.jpg)](https://www.blogger.com/profile/09989733095447891258)

[Dancho Danchev](https://www.blogger.com/profile/09989733095447891258)
:   Independent Security Consultancy, Threat Intelligence Analysis (OSINT/Cyber Counter Intelligence) and Competitive Intelligence research on deman...
---
title: Inside the KillNet Crowd-Sourced DDoS Attack Campaign Targeting International Web Sites - An OSINT Analysis
url: https://ddanchev.blogspot.com/2022/10/inside-killnet-crowd-sourced-ddos.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2022-10-27
fetch_date: 2025-10-03T21:00:02.316075
---

# Inside the KillNet Crowd-Sourced DDoS Attack Campaign Targeting International Web Sites - An OSINT Analysis

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

Independent Contractor. Bitcoin: 15Zvie1j8CjSR52doVSZSjctCDSx3pDjKZ Email: dancho.danchev@hush.com OMEMO: ddanchev@conversations.im | OTR: danchodanchev@xmpp.jp | TOX ID: 53B409440A6DC34F1BA458869A0462D92C15B467AF6319D481CA353690C88667833A0EE82969

## Wednesday, October 26, 2022

### Inside the KillNet Crowd-Sourced DDoS Attack Campaign Targeting International Web Sites - An OSINT Analysis

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9kZjwied7sCzHy0bIx1q_p8AgjPamKBoPSqZEH7ULnlXCYsvIuaa9Og718MH1nSjxIV9H-vRn-5eNxWi_5g47QrKge7y-irQi--zCtP-RIKIAOknsMHLlZlq6oIn6iN5T1eZGS0FVQ_Vt2yRiexUHl4C85UZOXY6CqHN_FCTQTmFcZh-7zg/s320/Screenshot_31.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9kZjwied7sCzHy0bIx1q_p8AgjPamKBoPSqZEH7ULnlXCYsvIuaa9Og718MH1nSjxIV9H-vRn-5eNxWi_5g47QrKge7y-irQi--zCtP-RIKIAOknsMHLlZlq6oIn6iN5T1eZGS0FVQ_Vt2yRiexUHl4C85UZOXY6CqHN_FCTQTmFcZh-7zg/s928/Screenshot_31.png)

I've decided to take a deeper look inside the currently ongoing crowd-sourced DDoS infrastructure platform known as KillNet where multiple pro-Russian groups including various Pro-Ukraine groups are basically soliciting users internationally to "donate" their bandwidth to a central command and control server under the operation of KillNet botnet operators that further orchestrate the actual Target List and the actual DDoS attack campaigns.

What's new here? Nothing really as crowd-sourcing DDoS attacks has been around for a while. It doesn't take a rocket scientist to entice a thousand users into installing a rogue and bogus crowd-sourced DDoS attack application under a central management command of KillNet who will be responsible for issuing managing and updating the Targets List that also includes the actual launching of the DDoS attack campaigns.

**Sample screenshots include:**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnsr3N3x8wuqRHvW32ZGzfmInfNY18V2jmjheLSrPRqBhB7QiDuPksEql9oj1by4XunN4dVdWtHdmvMLcS0SUV2cMtE8PgyIVezCLrIIRY_SOPxfUOPi_QzNIKujU-HOuQ01pG9Dif7ogkV8Q5cxclNQOvL8vY0WR9bDbflW_3zdU6aOdNYg/s320/66e249d7-4df9-45f9-9e63-6dd6a36fc5fe.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnsr3N3x8wuqRHvW32ZGzfmInfNY18V2jmjheLSrPRqBhB7QiDuPksEql9oj1by4XunN4dVdWtHdmvMLcS0SUV2cMtE8PgyIVezCLrIIRY_SOPxfUOPi_QzNIKujU-HOuQ01pG9Dif7ogkV8Q5cxclNQOvL8vY0WR9bDbflW_3zdU6aOdNYg/s1256/66e249d7-4df9-45f9-9e63-6dd6a36fc5fe.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIqbZPJr73snEiWY7ZPY4BMNfV-uSwghFSE3WZp9mtNlnWQ0Q4k3AbXdu5NUxci4pG43eJE3iZNypdtyvrJ0is3UDBw7NrejqwlFY5Mh5_ckjs7nhlxJPwTZ7Un3_-84SlwZ2IvFwqGnAGasdgQv21ZzpFgKG-ngXXswqKdm49DASsi5ImIQ/s320/FfRikgiXgAEnG-n.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIqbZPJr73snEiWY7ZPY4BMNfV-uSwghFSE3WZp9mtNlnWQ0Q4k3AbXdu5NUxci4pG43eJE3iZNypdtyvrJ0is3UDBw7NrejqwlFY5Mh5_ckjs7nhlxJPwTZ7Un3_-84SlwZ2IvFwqGnAGasdgQv21ZzpFgKG-ngXXswqKdm49DASsi5ImIQ/s843/FfRikgiXgAEnG-n.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkCwebYrrXDp0s0005hxLN-DfVW7FQUwXihV1VhkJYwAFO7Jf-Sy22KLCwwhce6u3yY1qExEQ8aqbi4L8gX2M-gSxl95qdpXku6YkGrZJLXlCeOG-XpnEmwalArHb7r7QHnPMT-sQmHnrrd4gHhJ3qorMFgbhRPauKmC3F8T6D002-1OxEdQ/s320/FfRikgpXwAAJnCD.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkCwebYrrXDp0s0005hxLN-DfVW7FQUwXihV1VhkJYwAFO7Jf-Sy22KLCwwhce6u3yY1qExEQ8aqbi4L8gX2M-gSxl95qdpXku6YkGrZJLXlCeOG-XpnEmwalArHb7r7QHnPMT-sQmHnrrd4gHhJ3qorMFgbhRPauKmC3F8T6D002-1OxEdQ/s843/FfRikgpXwAAJnCD.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKS8IfJiG6V3bqw87IvgMu6zIckQYhm9-ILYGxrxYm0SnX-rmRUX7lQSrR8ACIjWWwco1a10kv3vu5X7ncYT-oVldJVmiia53Jj85L_ugfd0Y_9RKkiQQGNTFL_l6A4hpPuFimxD2L6IvTcdoJsiV6KfXln218jRj7HF66ozwGvbsj-E5_YA/s320/Killnet.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKS8IfJiG6V3bqw87IvgMu6zIckQYhm9-ILYGxrxYm0SnX-rmRUX7lQSrR8ACIjWWwco1a10kv3vu5X7ncYT-oVldJVmiia53Jj85L_ugfd0Y_9RKkiQQGNTFL_l6A4hpPuFimxD2L6IvTcdoJsiV6KfXln218jRj7HF66ozwGvbsj-E5_YA/s700/Killnet.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9cbohqULlX4F4eOJyZJS9tCiNhCvHQ9DRfBxLRiYz3KP20j3eJcRjLHOH2zIvv66wps4Zp-Tt3nzQpxDYLQlyiwHBxUoM0wHbGp34b166bCwLo2ndfRvVvmxEYvpniHT_iP-Zb0xcSesPDJQIML4K9mSewM11LbACg45u8qKD0s14P-bJxw/s320/Misc_8600.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9cbohqULlX4F4eOJyZJS9tCiNhCvHQ9DRfBxLRiYz3KP20j3eJcRjLHOH2zIvv66wps4Zp-Tt3nzQpxDYLQlyiwHBxUoM0wHbGp34b166bCwLo2ndfRvVvmxEYvpniHT_iP-Zb0xcSesPDJQIML4K9mSewM11LbACg45u8qKD0s14P-bJxw/s1052/Misc_8600.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguKMCPRhY5Mci3uwBc7ATqSHE_Fani7ZxVLCWonw0p-OH5CmGLABuyy10or0lkr1eIPafZYYASibRUY4WanfjxvQBvEvZ7BxzE-5Rb0U17NF4V-MpweST5BQ427H2LvRBGxe9WQ93DG6WTcLuT5BRLujmYfVmnmWhwpCtZjlGVrLEw0n8d5A/s320/Misc_8700.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguKMCPRhY5Mci3uwBc7ATqSHE_Fani7ZxVLCWonw0p-OH5CmGLABuyy10or0lkr1eIPafZYYASibRUY4WanfjxvQBvEvZ7BxzE-5Rb0U17NF4V-MpweST5BQ427H2LvRBGxe9WQ93DG6WTcLuT5BRLujmYfVmnmWhwpCtZjlGVrLEw0n8d5A/s709/Misc_8700.jpg)

**Sample URLs known to have been involved in the campaign include:**

hxxp://killnethackers.com

hxxp://killnet.tilda.ws

hxxp://wawsquad.cf

Stay tuned!

-
[October 26, 2022](https://ddanchev.blogspot.com/2022/10/inside-killnet-crowd-sourced-ddos.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/18493443/879703720001383331 "Email Post")

[Email This](https://www.blogger.com/share-post.g?blogID=18493443&postID=879703720001383331&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=18493443&postID=879703720001383331&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=18493443&postID=879703720001383331&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=18493443&postID=879703720001383331&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=18493443&postID=879703720001383331&target=pinterest "Share to Pinterest")

![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimxCSbi25rfvHIa7H8x-VuFqcOZaIMyVWQpCC9QOCEqIoU3vgZwnlXz5Ee7Vhoel0LK4iK1XrVIxlaCPLV4nO66Ug2qFireNLDJ4DxzdyEX0ce7Z-zJlEEBx8T6U-xDQ/s113/126817412_103684408239911_5047637022297351917_n.jpg)

[Dancho Danchev](https://www.blogger.com/profile/09989733095447891258 "author profile")

Independent Security Consultancy, Threat Intelligence Analysis (OSINT/Cyber Counter Intelligence) and Competitive Intelligence research on demand. Insightful, unbiased, and client-tailored assessments, neatly communicated in the form of interactive reports - because anticipating the emerging threatscape is what shapes the big picture at the end of the day. Approach me at dancho.danchev@hush.com

#### No comments:

#### Post a Comment

[Newer Post](https://ddanchev.blogspot.com/2022/10/how-to-build-information-security.html "Newer Post")

[Older Post](https://ddanchev.blogspot.com/2022/10/my-new-rss-feed.html "Older Post")
[Home](https://ddanchev.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://ddanchev.blogspot.com/feeds/879703720001383331/comments/default)

[![Web Analytics Made Easy - Statcounter](https://c.statcounter.com/1212632/0/91125b67/1/)](https://statcounter.com/ "Web Analytics Made Easy - Statcounter")

## Wikipedia Draft

[Shoutcast Hosting](https://www.caster.fm) [Stream Hosting](https://www.caster.fm) [Radio Server Hosting](https://www.caster.fm)

## Followers

[![Clicky](//static.getclicky.com/media/links/badge.gif)](https://clicky.com/101422166 "Privacy-friendly Web Analytics")

## This Blog - 2005 - 2024

[![This Blog - 2005 - 2024](https://blogger.googleusercontent.com/img/a/AVvXsEglFTGC9ReBriBRRDJHu0UpCxPcZ28KUFPwLqLVYhrY-_4Pjo5dB1FXbWpfStmu2IVfXoU7srml6TDcFnvdwEJ1HKHD6xM8kV6HbZJfpPGC5zzUJjPD5Adu3IFFCAW_...
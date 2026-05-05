---
title: Bulgarian Parcel Shipping Company Speedy Under Phishing Attack - An Analysis
url: https://ddanchev.blogspot.com/2026/05/bulgarian-parcel-shipping-company.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2026-05-04
fetch_date: 2026-05-05T05:03:42.172702
---

# Bulgarian Parcel Shipping Company Speedy Under Phishing Attack - An Analysis

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

In the overwhelming sea of information, access to timely, insightful and independent open-source intelligence (OSINT) analyses is crucial for maintaining the necessary situational awareness to stay on the top of emerging security threats. This blog covers trends and fads, tactics and strategies, intersecting with third-party research, speculations and real-time CYBERINT assessments, all packed with sarcastic attitude

## Monday, May 04, 2026

### Bulgarian Parcel Shipping Company Speedy Under Phishing Attack - An Analysis

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhobjvfYxLIC4rCGuyA2qCbui3P3kd8canNqHl734q9IiMkv5rCWdCDtzYOY_6AfUbxiGtdzuYXN71zd8aybTN_1ajEpWc6Jj0kLhAegPdGrc8ez3MKa9YDPgjfp9X_FWEMbdvhlb2Ld_836I-vNpr_r-KfNqOQ3vTZplradwkkCCAFrPlJwZMn/s320/Bulgaria_Speedy_Parcel_Service_Phishing_01.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhobjvfYxLIC4rCGuyA2qCbui3P3kd8canNqHl734q9IiMkv5rCWdCDtzYOY_6AfUbxiGtdzuYXN71zd8aybTN_1ajEpWc6Jj0kLhAegPdGrc8ez3MKa9YDPgjfp9X_FWEMbdvhlb2Ld_836I-vNpr_r-KfNqOQ3vTZplradwkkCCAFrPlJwZMn/s1600/Bulgaria_Speedy_Parcel_Service_Phishing_01.png)

Dear blog readers,

I recently intercepted a relatively interesting phishing attempt impersonating the Bulgarian parcel shipping company Speedy that also includes propagation using SMS messages targeting Bulgarian users prompting them to click on bogus and phishing links and I decided to dig a little bit deeper into the infrastructure behind the phishing campaign.

With the [company](https://www.speedy.bg/bg/post/Misleading-Messages-on-behalf-of-Speedy-20231218) [acknowledging](https://www.speedy.bg/bg/post/Misleading-Messages-on-behalf-of-Speedy-20231218) the [existence](https://www.speedy.bg/bg/post/Misleading-Messages-on-behalf-of-Speedy-20231218) of the campaign and prompting users to stay vigilant and avoid interacting with the SMS messages and don't click on the phishing domain links in this post I'll provide actionable intelligence on the infrastructure behind the phishing campaign.

It's worth emphasizing on the fact that based on publicly accessible information and based on my own personal analysis methodology I was able to find out that this specific phishing campaign was originally active since 2023 which makes it a persistent phishing attack campaign that targets Bulgarian parcel shipping services which also includes Bulgarian Post Service and DHL Bulgaria.

**[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpOY3FE9jtt2lxEqO9E3yx8rokksCtyUe8jroHLM5eIQOlEy1NmI2qg8wxPl4G8geM6Iqr_SkNcEXN9EjoZj9NPRPxkIPO7962JsN5Tr8BnTNsoSNKdxZYh3FEL5gAo1Pf7umm0DAI5UxPi6J7tBhUgOIIOBZKowuDS9-pHPteZHCXZFtr50YD/s320/Bulgaria_Speedy_Parcel_Service_Phishing_02.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpOY3FE9jtt2lxEqO9E3yx8rokksCtyUe8jroHLM5eIQOlEy1NmI2qg8wxPl4G8geM6Iqr_SkNcEXN9EjoZj9NPRPxkIPO7962JsN5Tr8BnTNsoSNKdxZYh3FEL5gAo1Pf7umm0DAI5UxPi6J7tBhUgOIIOBZKowuDS9-pHPteZHCXZFtr50YD/s1129/Bulgaria_Speedy_Parcel_Service_Phishing_02.png)

Sample domains known to have been involved in the campaign include:**

hxxp://bg-paci.com

hxxp://bg-sof.com

hxxp://bg-imy.com

hxxp://bg-myk.com

hxxp://bg-myck.com

hxxp://bg-tck.com

hxxp://bg-tmy.com

hxxp://bg-il.com

hxxp://bg-tzc.com

hxxp://bg-tiack.com

hxxp://bg-myb.com

hxxp://bg-tack.com

**Responding IPs:**

165.154.239.211

165.154.212.18

**[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLDWIaG5ywOkRxNiQB5uduLF5IJurIzmJDYA-0a4Nf2Ir63nL511RMKjOPRc69k9Lb0fkAZn0M1blULmjv-uqhQtvFJ9k-PtiAVPGo9wg1ZYUGHuGbC2spONG9us8mN3ioB1I8ONeS95U58EWk0ywadKl0iinh3tfiuYxe3gAslrFeb-Y5oK6_/s320/Bulgaria_Speedy_Parcel_Service_Phishing_03.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLDWIaG5ywOkRxNiQB5uduLF5IJurIzmJDYA-0a4Nf2Ir63nL511RMKjOPRc69k9Lb0fkAZn0M1blULmjv-uqhQtvFJ9k-PtiAVPGo9wg1ZYUGHuGbC2spONG9us8mN3ioB1I8ONeS95U58EWk0ywadKl0iinh3tfiuYxe3gAslrFeb-Y5oK6_/s1012/Bulgaria_Speedy_Parcel_Service_Phishing_03.png)

Sample URLs known to have been used in the campaign include:**

hxxp://speedy.bg-myb.com/en/speedy.html

hxxp://speedy.bg-tiack.com/en/speedy.html

hxxp://speedy.bg-tiack.com/en/speedy.html

hxxp://speedybg.cfd/en/speedy.html

hxxp://speedy-i.com/bg/speedy.html

hxxp://speedy-blg.com/bg/speedy.html

hxxp://speedy.bg-na.qpon/my/speedy.html

hxxp://speedy.bg-ip.qpon/my/speedy.html

hxxp://speedy.bg-ic.qpon/my/speedy.html

hxxp://speedy.bg-it.qpon/my/speedy.html

hxxp://speedy.bg-ip.qpon/my/speedy.html

hxxp://speedy.bg-ia.qpon/my/speedy.html

hxxp://speedy.bg-gl.qpon/my/speedy.html

hxxp://speedy.bu-bd.qpon/my/speedy.html

hxxp://speedy.bu-bd.qpon/my/speedy.html

hxxp://speedy.bg-pv.cfd/my/speedy.html

hxxp://speedy.bg-bz.qpon/my/speedy.html

hxxp://speedy.bg-z.qpon/my/speedy.html

hxxp://speedy.bg-pot.qpon/bg/speedy.html

hxxp://speedy.bg-pot.qpon/bg/speedy.html

hxxp://speedy.bg-packl.cfd/bg/speedy.html

hxxp://speedy.bg-pack.cfd/bg/speedy.html

hxxp://speedy.bg-packg.cfd/bg/speedy.html

hxxp://speedy.bg-packg.cfd/bg/speedy.html

hxxp://speedy.bg-packg.cfd/bg/speedy.html

hxxp://speedy.bg-packi.cfd/bg/speedy.html

hxxp://speedyi.cfd/bg/speedy.html

hxxp://speedyi.cfd/bg/speedy.html

-
[May 04, 2026](https://ddanchev.blogspot.com/2026/05/bulgarian-parcel-shipping-company.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/18493443/6263719294808489198 "Email Post")

[Email This](https://www.blogger.com/share-post.g?blogID=18493443&postID=6263719294808489198&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=18493443&postID=6263719294808489198&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=18493443&postID=6263719294808489198&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=18493443&postID=6263719294808489198&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=18493443&postID=6263719294808489198&target=pinterest "Share to Pinterest")

![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimxCSbi25rfvHIa7H8x-VuFqcOZaIMyVWQpCC9QOCEqIoU3vgZwnlXz5Ee7Vhoel0LK4iK1XrVIxlaCPLV4nO66Ug2qFireNLDJ4DxzdyEX0ce7Z-zJlEEBx8T6U-xDQ/s113/126817412_103684408239911_5047637022297351917_n.jpg)

[Dancho Danchev](https://www.blogger.com/profile/09989733095447891258 "author profile")

Independent Security Consultancy, Threat Intelligence Analysis (OSINT/Cyber Counter Intelligence) and Competitive Intelligence research on demand. Insightful, unbiased, and client-tailored assessments, neatly communicated in the form of interactive reports - because anticipating the emerging threatscape is what shapes the big picture at the end of the day. Approach me at dancho.danchev@hush.com

#### No comments:

#### Post a Comment

[Older Post](https://ddanchev.blogspot.com/2026/05/when-data-mining-conti-leaks-leads-to.html "Older Post")
[Home](https://ddanchev.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://ddanchev.blogspot.com/feeds/6263719294808489198/comments/default)

## About Me

[![My photo](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimxCSbi25rfvHIa7H8x-VuFqcOZaIMyVWQpCC9QOCEqIoU3vgZwnlXz5Ee7Vhoel0LK4iK1XrVIxlaCPLV4nO66Ug2qFireNLDJ4DxzdyEX0ce7Z-zJlEEBx8T6U-xDQ/s113/126817412_103684408239911_5047637022297351917_n.jpg)](https://www.blogger.com/profile/09989733095447891258)

[Dancho Danchev](https://www.blogger.com/profile/09989733095447891258)
:   Independent Security Consultancy, Threat Intelligence Analysis (OSINT/Cyber Counter Intelligence) and Competitive Intelligence research on demand. Insightful, unbiased, and client-tailored assessments, neatly communicated in the form of interactive reports - because anticipating the emerging threatscape is what shapes the big picture at the end of the day. Approach me at dancho.danchev@hush.com

[V...
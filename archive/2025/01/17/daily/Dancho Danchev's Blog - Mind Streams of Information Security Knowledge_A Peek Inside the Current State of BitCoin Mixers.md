---
title: A Peek Inside the Current State of BitCoin Mixers
url: https://ddanchev.blogspot.com/2025/01/a-peek-inside-current-state-of-bitcoin.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2025-01-17
fetch_date: 2025-10-06T20:08:39.712732
---

# A Peek Inside the Current State of BitCoin Mixers

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

Independent Contractor. Bitcoin: 15Zvie1j8CjSR52doVSZSjctCDSx3pDjKZ Email: dancho.danchev@hush.com OMEMO: ddanchev@conversations.im | OTR: danchodanchev@xmpp.jp | TOX ID: 53B409440A6DC34F1BA458869A0462D92C15B467AF6319D481CA353690C88667833A0EE82969

## Friday, January 17, 2025

### A Peek Inside the Current State of BitCoin Mixers

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_jWQjm9Q_IlepynPYDo2mQ6NscXJUrObR1v3N2qNqLVUG4O2HCkd00HtLCjO4zbKbIg5dNLiyNFiZMZ27qNI9o70ipnVtRcFLsVxsRZhFqDMMiWAGfckDxJrbFegDzoUShZF1kpSaWEw7A1CoORk1rsiuvr8WGvkA83VvaY9OD2whr-N6HpsD/s320/Misc_02.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_jWQjm9Q_IlepynPYDo2mQ6NscXJUrObR1v3N2qNqLVUG4O2HCkd00HtLCjO4zbKbIg5dNLiyNFiZMZ27qNI9o70ipnVtRcFLsVxsRZhFqDMMiWAGfckDxJrbFegDzoUShZF1kpSaWEw7A1CoORk1rsiuvr8WGvkA83VvaY9OD2whr-N6HpsD/s1295/Misc_02.png)

Dear blog readers,

In this post I'll provide some actionable intelligence on the current state of active BitCoin Mixers landscape with the idea to assist everyone on their way to properly attribute a fraudulent or malicious transaction or to dig a little bit deeper inside the infrastructure and financial infrastructure behind these BitCoin Mixers.

**Sample known BitCoin Mixer URLs:**

hxxp://anonymixer.com
hxxp://bitmixer.online
hxxp://chipmixer.com
hxxp://coinomize.biz
hxxp://coinomize.co
hxxp://coinomize.is
hxxp://cryptomixer.io
hxxp://gingerwallet.io
hxxp://jambler.io
hxxp://jokermix.to
hxxp://medusamixer.io
hxxp://blindmixer.com
hxxp://mixer.money
hxxp://mixerdream.com
hxxp://mixero.io
hxxp://mixtum.io
hxxp://mixtura.money
hxxp://mixy.money
hxxp://puremixer.io
hxxp://sparrowwallet.com
hxxp://swamplizard.io
hxxp://tengricrypto.com
hxxp://thormixer.io
hxxp://unijoin.io
hxxp://webmixer.io
hxxp://whir.to

**[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiiaGGrFeQBdm7RpjzTsrn9nzNZYf_x_gZoKOYkeT70sTzdy6AWXd2fBLMjT1VcYbr1ovCjQvrc2V-EMFaXhtYMv6A43SxZLWGDfH0lz4MuF4bs4sYi4HAbqP2ljsOV3mINLWlu8scC07ifGZ_6utAZIc3hIAygrasjU0T0fHeWaQYa_tbjO26/s320/Misc_03.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiiaGGrFeQBdm7RpjzTsrn9nzNZYf_x_gZoKOYkeT70sTzdy6AWXd2fBLMjT1VcYbr1ovCjQvrc2V-EMFaXhtYMv6A43SxZLWGDfH0lz4MuF4bs4sYi4HAbqP2ljsOV3mINLWlu8scC07ifGZ_6utAZIc3hIAygrasjU0T0fHeWaQYa_tbjO26/s1263/Misc_03.png)**

**Sample known responding IPs:**
104.21.14.15
172.67.133.191
136.228.192.103
172.64.101.28
172.64.98.33
104.21.36.129
172.67.158.129
188.114.97.3
188.114.97.1
172.67.142.24
185.205.69.10
135.181.110.78
93.95.231.89
34.102.136.180
172.67.188.123
104.26.3.240
198.177.120.27
104.21.58.174
188.114.99.229
188.114.98.224
104.21.79.112
34.102.155.139
216.246.46.117
172.67.170.136
172.67.172.23
108.167.189.28
162.241.61.115
108.167.189.61
192.185.4.130
188.114.97.0
172.67.180.202
188.114.96.4
104.21.34.115
172.67.160.123
46.101.27.21
108.160.143.236
188.114.96.3
172.67.170.175
104.21.63.126
65.109.166.143
103.224.212.100
93.95.231.80
199.59.243.226
37.120.206.181
172.64.174.24
152.89.162.34
188.114.96.0
46.17.96.4
103.224.212.210
186.2.163.238
101.99.91.215
172.67.154.113
104.21.69.169
185.178.208.78
172.67.210.143

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrMVmlGhKj9X62G7TnyOgzseVdFrvEPVCX7ZR3DENr2652Zr3gexTitwz9e0bJjgDRMDTRKJhiNra0Hcu_mWx7CIsrAe8CwoSekBuj_63KcQRvhZ-xI6yfVL3VK0xBXQHB-2DKSZ17uzeaOq4hpCYid2KbtHhdjEbJHD1O5JP3kfJ1OuLmEcHm/s320/Misc_04.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrMVmlGhKj9X62G7TnyOgzseVdFrvEPVCX7ZR3DENr2652Zr3gexTitwz9e0bJjgDRMDTRKJhiNra0Hcu_mWx7CIsrAe8CwoSekBuj_63KcQRvhZ-xI6yfVL3VK0xBXQHB-2DKSZ17uzeaOq4hpCYid2KbtHhdjEbJHD1O5JP3kfJ1OuLmEcHm/s1364/Misc_04.png)

188.114.98.229
188.114.97.4
188.114.96.14
172.67.158.73
188.114.97.2
172.67.70.29
188.114.97.14
104.26.5.134
186.2.163.228
23.202.231.167
104.21.96.1
198.54.117.210
188.114.97.22
198.54.117.200
188.114.97.7
149.28.138.23
45.180.20.12
185.86.149.239
218.93.250.18
185.178.208.139
172.67.191.198
188.114.99.224
104.21.43.207
46.28.207.19
104.26.3.196
13.248.151.237
104.21.36.95
172.64.80.1
36.86.63.182
172.64.165.7
23.217.138.112

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7PEWh5sBbsezKv-Qmi39Rl94hYBmJNmoaAhhD2cVTAzEyk43PBIWx-efh4IW4DYTVkZHRxyOW1JaGU1DWoKxjH18WaEMEwFbLDgTAGSQNKi1pKqj7EgVANYfahZ1tfCqh0fDHOu4tYgqQPIvWyxuSPLQD-thWF7ss4Thoc-QPdGhSY_N5Mpcb/s320/Misc_05.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7PEWh5sBbsezKv-Qmi39Rl94hYBmJNmoaAhhD2cVTAzEyk43PBIWx-efh4IW4DYTVkZHRxyOW1JaGU1DWoKxjH18WaEMEwFbLDgTAGSQNKi1pKqj7EgVANYfahZ1tfCqh0fDHOu4tYgqQPIvWyxuSPLQD-thWF7ss4Thoc-QPdGhSY_N5Mpcb/s1219/Misc_05.png)

185.178.208.159
172.67.206.39
104.21.16.160
172.67.154.213
104.21.6.88
5.61.48.183
172.67.154.211
104.239.213.7
45.76.91.219
46.101.124.25
23.195.69.112
104.21.6.90
164.92.229.238

Stay tuned.

-
[January 17, 2025](https://ddanchev.blogspot.com/2025/01/a-peek-inside-current-state-of-bitcoin.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/18493443/4295113816493096564 "Email Post")

[Email This](https://www.blogger.com/share-post.g?blogID=18493443&postID=4295113816493096564&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=18493443&postID=4295113816493096564&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=18493443&postID=4295113816493096564&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=18493443&postID=4295113816493096564&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=18493443&postID=4295113816493096564&target=pinterest "Share to Pinterest")

![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimxCSbi25rfvHIa7H8x-VuFqcOZaIMyVWQpCC9QOCEqIoU3vgZwnlXz5Ee7Vhoel0LK4iK1XrVIxlaCPLV4nO66Ug2qFireNLDJ4DxzdyEX0ce7Z-zJlEEBx8T6U-xDQ/s113/126817412_103684408239911_5047637022297351917_n.jpg)

[Dancho Danchev](https://www.blogger.com/profile/09989733095447891258 "author profile")

Independent Security Consultancy, Threat Intelligence Analysis (OSINT/Cyber Counter Intelligence) and Competitive Intelligence research on demand. Insightful, unbiased, and client-tailored assessments, neatly communicated in the form of interactive reports - because anticipating the emerging threatscape is what shapes the big picture at the end of the day. Approach me at dancho.danchev@hush.com

#### No comments:

#### Post a Comment

[Newer Post](https://ddanchev.blogspot.com/2025/01/a-peek-inside-current-state-of-bitcoin_17.html "Newer Post")

[Older Post](https://ddanchev.blogspot.com/2025/01/profiling-ispoof-cybercrime-enterprise.html "Older Post")
[Home](https://ddanchev.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://ddanchev.blogspot.com/feeds/4295113816493096564/comments/default)

[![Web Analytics Made Easy - Statcounter](https://c.statcounter.com/1212632/0/91125b67/1/)](https://statcounter.com/ "Web Analytics Made Easy - Statcounter")

## Wikipedia Draft

[Shoutcast Hosting](https://www.caster.fm) [Stream Hosting](https://www.caster.fm) [Radio Server Hosting](https://www.caster.fm)

## Followers

[![Clicky](//static.getclicky.com/media/links/badge.gif)](https://clicky.com/101422166 "Privacy-friendly Web Analytics")

## This Blog - 2005 - 2024

[![This Blog - 2005 - 2024](https://blogger.googleusercontent.com/img/a/AVvXsEglFTGC9ReBriBRRDJHu0UpCxPcZ28KUFPwLqLVYhrY-_4Pjo5dB1FXbWpfStmu2IVfXoU7srml6TDcFnvdwEJ1HKHD6xM8kV6HbZJfpPGC5zzUJjPD5Adu3IFFCAW_4vVDKsQN6Bq0bOt9hb6VUBQ6Ek7cF2dC55e6H7f1vJd6FJVfFWQzZczc=s302)](https://web.archive.org/web/20240000000000%2A/ddanchev.blogspot.com)

## Astalavista.com

[![Astalavista.com](https://blogger.googleusercontent.com/img/a/AVvXsEgfBngbw2oNmVoIq0oK494_i9CUAmtx4JRo1XIESvEVatJyDC_RVWXZL7YCBHl1dzPthpW61flqs6EXrg9gUfQc8uRnfrfMFiOzC_NJRCKAtpJNaSfsDLnZxRfMAVk6Ix3MhpR3Y8...
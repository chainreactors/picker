---
title: Who DDoS-ed Georgia/Bobbear.co.uk and a Multitude of Russian Homosexual Sites in 2009? - An OSINT Analysis
url: https://ddanchev.blogspot.com/2022/10/who-ddos-ed-georgiabobbearcouk-and.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2022-10-28
fetch_date: 2025-10-03T21:07:28.307378
---

# Who DDoS-ed Georgia/Bobbear.co.uk and a Multitude of Russian Homosexual Sites in 2009? - An OSINT Analysis

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

Independent Contractor. Bitcoin: 15Zvie1j8CjSR52doVSZSjctCDSx3pDjKZ Email: dancho.danchev@hush.com OMEMO: ddanchev@conversations.im | OTR: danchodanchev@xmpp.jp | TOX ID: 53B409440A6DC34F1BA458869A0462D92C15B467AF6319D481CA353690C88667833A0EE82969

## Thursday, October 27, 2022

### Who DDoS-ed Georgia/Bobbear.co.uk and a Multitude of Russian Homosexual Sites in 2009? - An OSINT Analysis

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQsN_nA7drafO3koSLDYIO-sIvLl9WlBqTyrS9ixJiqR38Cc08Ha2LQiCYZdPQN7hprIgu5P-Mp8BjKxpcFqboEnDHk-yScMZOXvG9Ku3V5tU-3EYCn85UP9gF6pexODUdirWQLoYcQRRsWzOCf6XTLRnhJ0vOe37RPlBrRcz5oD8evvpRMg/s320/Misc_150000.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQsN_nA7drafO3koSLDYIO-sIvLl9WlBqTyrS9ixJiqR38Cc08Ha2LQiCYZdPQN7hprIgu5P-Mp8BjKxpcFqboEnDHk-yScMZOXvG9Ku3V5tU-3EYCn85UP9gF6pexODUdirWQLoYcQRRsWzOCf6XTLRnhJ0vOe37RPlBrRcz5oD8evvpRMg/s1232/Misc_150000.png)

**NOTE:**

I took these screenshots circa 2009.

**UPDATE:**

Here are some of the related botnet C&C server domains known to have been involved in the campaign:

hxxp://cxim.inattack.ru/www3/www/

hxxp://i.clusteron.ru/bstatus.php

hxxp://203.117.111.52/www7/www/getcfg.php (cxim.inattack.ru)

hxxp://cxim.inattack.ru/www2/www/stat.php

hxxp://cxim.inattack.ru/www3/www/stat.php

hxxp://cxim.inattack.ru/www4/www/stat.php

hxxp://cxim.inattack.ru/www5/www/stat.php

hxxp://cxim.inattack.ru/www6/www/stat.php

hxxp://finito.fi.funpic.org/black/stat.php

hxxp://logartos.org/forum/stat.php - 195.24.78.242

hxxp://weberror.cn/be1/stat.php

hxxp://prosto.pizdos.net/\_lol/stat.php

hxxp://h278666y.net/www/stat.php - 72.233.60.254

I've decided to share this post including related screenshots and technical details with the idea to inspire everyone to continue doing their research including cyber attack and campaign tracking and monitoring including cyber attack and cyber attack campaign attribution efforts.

Back in 2009 there was a major speculation that Russia indeed launched a massive DDoS (Distributed Denial of Service) attack against Georgia which was in fact true. What was particularly interesting about this campaign was the fact that the same DDoS for hire including the managed DDoS service that was behind the attack was also observed to launch related DDoS attack campaigns against bobbear.co.uk including a multi-tude of Russian homosexual Web sites where the actual Web sites indeed posted a message back then on their official Web sites signaling the existence of the DDoS attack targeting their Web sites.

Who was behind the campaigns? An image is worth a thousand words including the actual use of the original Maltego Community Edition back then which used to produce outstanding results in a variety of cases and cyber attack incidents and campaigns.

**Sample screenshots include:**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFpw8H7J_rKYeCxwd6CSWj9tpzxK7LijT0UyytyuSDe7GonmVfrrMezpULFsz5f7S6qjsXzYpP6_PFMXbKesLakJk50n8OrL8t5EUGNfXvzed2riyJKSW_KkMv1qMqwCfXlc7lSp9O_sHkQQ8aY_EnXtA_mjKTt4c5JJRJMMxQqyFrK0oEMA/s320/Misc_980000.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFpw8H7J_rKYeCxwd6CSWj9tpzxK7LijT0UyytyuSDe7GonmVfrrMezpULFsz5f7S6qjsXzYpP6_PFMXbKesLakJk50n8OrL8t5EUGNfXvzed2riyJKSW_KkMv1qMqwCfXlc7lSp9O_sHkQQ8aY_EnXtA_mjKTt4c5JJRJMMxQqyFrK0oEMA/s1280/Misc_980000.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnt5GXcDv3_XEjcl8aRMeqXpmudA-Pfsw0oqIwZl54sgYZ3AJi-N2o43ireBeX_yXFJAOPkohLt5FNdAIb7WcYaioHzMRDqYRh6pMzAzsSKmsnoP4J7heu5XQtvs9wrzt-u4wsm0741pXCV1Me7b1Lmtn6lxlVI6pJJL2A1dCAFQNfD1qKow/s320/Misc_990000.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnt5GXcDv3_XEjcl8aRMeqXpmudA-Pfsw0oqIwZl54sgYZ3AJi-N2o43ireBeX_yXFJAOPkohLt5FNdAIb7WcYaioHzMRDqYRh6pMzAzsSKmsnoP4J7heu5XQtvs9wrzt-u4wsm0741pXCV1Me7b1Lmtn6lxlVI6pJJL2A1dCAFQNfD1qKow/s1280/Misc_990000.PNG)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJ6YLX1z9TJgCJyiV3wADGXPBgZQG9EQtLMVUokeZZuOHK5_h2NPxUHkN-dQDAvw-i7BF54blgQ3RXfT3FaHy214L3HNxL46uJjbb-MeW7UX0cNqQofpinIhCPFKPomLnWz70LphXK2k0Za1C4PtVDVDvN6zvIpNS3OOkw_BPHjd5ZNvEhGg/s320/Misc_965000.bmp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJ6YLX1z9TJgCJyiV3wADGXPBgZQG9EQtLMVUokeZZuOHK5_h2NPxUHkN-dQDAvw-i7BF54blgQ3RXfT3FaHy214L3HNxL46uJjbb-MeW7UX0cNqQofpinIhCPFKPomLnWz70LphXK2k0Za1C4PtVDVDvN6zvIpNS3OOkw_BPHjd5ZNvEhGg/s791/Misc_965000.bmp)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjaMH6dxD3mj0ZnSSL2o6-T26BKoeKZxxbzIaDSv_JIeaLo8OPUrNBJ_Dqat18X4CvviAyFxIkGarrR4brqTcuA3Dh1HNG_0riBrkM_mCZ6vQuvjjn4ycO1VyHU-eFNZA18cn8UU_WeV9z0gBAOiEOS-7E1iRbwvdozHgnuh9pQ4yWcK5oUjA/s320/Misc_967000.bmp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjaMH6dxD3mj0ZnSSL2o6-T26BKoeKZxxbzIaDSv_JIeaLo8OPUrNBJ_Dqat18X4CvviAyFxIkGarrR4brqTcuA3Dh1HNG_0riBrkM_mCZ6vQuvjjn4ycO1VyHU-eFNZA18cn8UU_WeV9z0gBAOiEOS-7E1iRbwvdozHgnuh9pQ4yWcK5oUjA/s1204/Misc_967000.bmp)

**Sample DDoS C&C domains known to have been involved in the campaign include:**

hxxp://emultrix.org

hxxp://yandexshit.com

hxxp://ad.yandexshit.com

hxxp://a-nahui-vse-zaebalo-v-pizdu.com

hxxp://killgay.com

hxxp://ns1.guagaga.net

hxxp://ns2.guagaga.net

hxxp://ohueli.net

hxxp://pizdos.net

**Sample DDoS C&C domain URLs known to have been involved in the campaign include:**

hxxp://a-nahui-vse-zaebalo-v-pizdu.com/a/nahui/vse/zaebalo/v/pizdu/

hxxp://prosto.pizdos.net/\_lol/

**Related domains known to have been involved in the campaign include:**

hxxp://candy-country.com

hxxp://best-info.in

hxxp://megadwarf.com.com

hxxp://good412.com

hxxp://oceaninfo.co.kr

hxxp://kukutrustnet777.info

hxxp://kukutrustnet888.info

hxxp://kukutrustnet987.info

hxxp://asjdiweur87wsdcnb.info

hxxp://pedmeo222nb.info

hxxp://gondolizo18483.info

hxxp://technican.w.interia.pl

hxxp://pzrk.ru

hxxp://bpowqbvcfds677.info

hxxp://bmakemegood24.com

hxxp://bperfectchoice1.com

hxxp://bcash-ddt.net

hxxp://bddr-cash.net

hxxp://bxxxl-cash.net

hxxp://balsfhkewo7i487fksd.info

hxxp://buynvf96.info

hxxp://httpdoc.info

hxxp://piceharb.com

hxxp://ultra-shop.biz

hxxp://googlets.info

hxxp://kokaco.info

hxxp://simdream.info

hxxp://simdream.biz

hxxp://lamour.ws

hxxp://prosto.pizdos.net

hxxp://vse.ohueli.net

hxxp://uploder.ws

hxxp://oole.biz

hxxp://yandexshit.com

hxxp://emultrix.org

hxxp://snail.pc.cz

hxxp://bibi.hamachi.cc

hxxp://killgay.com

hxxp://installs.bitacc.com

hxxp://hg7890.com

hxxp://dungcoivb.googlepages.com

hxxp://toggle.com

hxxp://nhatquanglan2.0catch.com

hxxp://svxela.com

hxxp://united-crew.org

**Sample malicious MD5s known to have been involved in the campaign include:**

MD5: cde613793e24508f32c38249d396f686

MD5:f13e24a0d7372e096392855d423db4da

MD5:ac43d13455ef4ba50ed522e4a54137dc

MD5:e729f992bea0896f104742e5cbc522c2

MD5:88bed9482f6e0578b59710c41ab890d7

MD5:0472379daba0ab1abee7468786a0953a

MD5:7507022e3cab75888ea960fb48476f2d

MD5:0fd3521e3e150f45a7b243de8760d74d

MD5:ad4007f5ee084e27f7149a98dfa469ba

MD5:d2b08dfcd438d8c106f9be5157553454

MD5:cd193c00728634b6ac3f91c0c5bcf196

MD5:8f69e9577380fd9ba37c1d0d9d5603c4

MD5:eea49d19db46f2cb8767270b019a427a

MD5:372db70ffa24bc0e1bc0ceb2375537b0

MD5:a738127a58985d233e52ee1eacce1bab

MD5:51a33d949644923332f192346aa38569

MD5:f47315c7623954c18c8ce83231044ab4

MD5:21823675dc1cc678ae28228bbfbdf9e2

MD5:38ed6d225770518deedae8c906d11d6c

MD5:b37e79d7ae5315d1479fc140ec8f049e

MD5:39a0f4c388d18b67ebed3c8c1b29dc4e

09f89b063f884b11fdf785e7eab8548b

MD5:ce2e644d48492dd254149b51a0d32fe7

MD5:25c65d3634ee36b1c99a45ce3d5f8fdc

MD5:e5950a5269c79a7e0158814749f3effc

MD5:561002ecbef499fc0624cedaacd81066

MD5:f6fe1019d426535765ae3800eafb7b9b

MD5:a4f51e896be7e9f5474d24e0c20b0d24

MD5:0d294580dafad0a16849fae4af757c3b

MD5:1ad98858daf6d7f570918b4c3402d824

MD5:0230f77066c14f50b42f32bcb195c8a3

MD5:95158942a3b730307abbd863a0cc6ab6

M...
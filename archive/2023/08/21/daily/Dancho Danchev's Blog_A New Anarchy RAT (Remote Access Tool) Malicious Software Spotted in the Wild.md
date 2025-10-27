---
title: A New Anarchy RAT (Remote Access Tool) Malicious Software Spotted in the Wild
url: https://ddanchev.blogspot.com/2023/08/a-new-anarchy-rat-remote-access-tool.html
source: Dancho Danchev's Blog
date: 2023-08-21
fetch_date: 2025-10-04T11:59:25.042687
---

# A New Anarchy RAT (Remote Access Tool) Malicious Software Spotted in the Wild

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

Independent Contractor. Bitcoin: 15Zvie1j8CjSR52doVSZSjctCDSx3pDjKZ Email: dancho.danchev@hush.com OMEMO: ddanchev@conversations.im | OTR: danchodanchev@xmpp.jp | TOX ID: 53B409440A6DC34F1BA458869A0462D92C15B467AF6319D481CA353690C88667833A0EE82969

## Sunday, August 20, 2023

### A New Anarchy RAT (Remote Access Tool) Malicious Software Spotted in the Wild

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEianU5OezFUVBlMsRmJgNlvXDxj4S5yt_R2Pzy8M9eUuCbElN9-9_ioAq1kTSoJ8EG2H5HklHu0BEKKH9FMRPhXhs12v_FEefJxjiLpV3SeqX9kv8lwvI_Dz2XhfQ7_3rzL1dx3jg73VPZjUpH4azaoyzUb5wQCTGzU4yjAVjXTjfwbAz57zKKh/s320/sCs8FzS.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEianU5OezFUVBlMsRmJgNlvXDxj4S5yt_R2Pzy8M9eUuCbElN9-9_ioAq1kTSoJ8EG2H5HklHu0BEKKH9FMRPhXhs12v_FEefJxjiLpV3SeqX9kv8lwvI_Dz2XhfQ7_3rzL1dx3jg73VPZjUpH4azaoyzUb5wQCTGzU4yjAVjXTjfwbAz57zKKh/s1920/sCs8FzS.jpeg)

An image is worth a thousand words - part two.

I've recently came across to a newly released malicious software which basically allows novice and experienced users with the ability to launch and manage access to compromised corporate and home networks and PCs where the ultimate goal would be to do this as easy as possible.

**Sample screenshots include:**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2XV_N9vUaLKI1Nm-BBM2eiFuywimK-Ysp5UaY_ZzdYycRwJJCbp81jkhKMuXaEsJxgiuG1QnZe86m_NKuzjU1kCVgbVx0lMsOmfAesa0yYAPCLGH7MIzE4swsioECF5pHWbFoJ5EbI6InL_P-Nkpru20l8gw9UiU99ByarRhr5kdJN-NzX1Xa/s320/7Cp4hob.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2XV_N9vUaLKI1Nm-BBM2eiFuywimK-Ysp5UaY_ZzdYycRwJJCbp81jkhKMuXaEsJxgiuG1QnZe86m_NKuzjU1kCVgbVx0lMsOmfAesa0yYAPCLGH7MIzE4swsioECF5pHWbFoJ5EbI6InL_P-Nkpru20l8gw9UiU99ByarRhr5kdJN-NzX1Xa/s1920/7Cp4hob.jpeg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3uRy10QB8F5OLg4DVQc0XbyIUoRkJ_sBqPXyAB2krA_XGQ4Cdfj0yk588N522jOaA0ZHdvDIjS4vpljUe3hJMFQlpRADzDXZrtsaeVhnbPlCYoiUYDFVTL_IXiYJgAlG3MKsX3qnmCYRVYihcWvmV4ixf-Mc-WDiS1LXIDyKqrVUQzotE5Lls/s320/cIW3t3S.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3uRy10QB8F5OLg4DVQc0XbyIUoRkJ_sBqPXyAB2krA_XGQ4Cdfj0yk588N522jOaA0ZHdvDIjS4vpljUe3hJMFQlpRADzDXZrtsaeVhnbPlCYoiUYDFVTL_IXiYJgAlG3MKsX3qnmCYRVYihcWvmV4ixf-Mc-WDiS1LXIDyKqrVUQzotE5Lls/s1918/cIW3t3S.jpeg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8B_smGB3O7UxQg1juCP1QxpaF6FOLN8cynOau1WQCQOrc5fayUZqeFHHM1V-RL7KOw8PADzBShp_sQlH_0JwaldfGjf-eKURGExdqp02NuRp5wFAPVrQb370k0CUxgVjZzDBaF0WcGtKt0cYi0Jolec80UVMpdITfkXrrfBu1mzyWDtT_C9_z/s320/DlvZPyT.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8B_smGB3O7UxQg1juCP1QxpaF6FOLN8cynOau1WQCQOrc5fayUZqeFHHM1V-RL7KOw8PADzBShp_sQlH_0JwaldfGjf-eKURGExdqp02NuRp5wFAPVrQb370k0CUxgVjZzDBaF0WcGtKt0cYi0Jolec80UVMpdITfkXrrfBu1mzyWDtT_C9_z/s1920/DlvZPyT.jpeg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitJ6EGOqt40MVK0wkokHkDEsV5CoMy_OYQllsW_mj6QvaIH8MFyOFw8aDBx_e_ETXalDLekC6EWZPbjUNcGPsVARgz1tViKdn5L1fEbdBKT9ljLC1gTrVBuzyjSZdC_dw6_YBMgDgAXWnh0X_i3bpoUN0q6zMR5Ivz2afJH5cOJV2LvFJ7rGE3/s320/ZWB5zPR.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitJ6EGOqt40MVK0wkokHkDEsV5CoMy_OYQllsW_mj6QvaIH8MFyOFw8aDBx_e_ETXalDLekC6EWZPbjUNcGPsVARgz1tViKdn5L1fEbdBKT9ljLC1gTrVBuzyjSZdC_dw6_YBMgDgAXWnh0X_i3bpoUN0q6zMR5Ivz2afJH5cOJV2LvFJ7rGE3/s1920/ZWB5zPR.jpeg)

Stay tuned!

-
[August 20, 2023](https://ddanchev.blogspot.com/2023/08/a-new-anarchy-rat-remote-access-tool.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://draft.blogger.com/email-post/18493443/7333076634831619009 "Email Post")

[Email This](https://draft.blogger.com/share-post.g?blogID=18493443&postID=7333076634831619009&target=email "Email This")[BlogThis!](https://draft.blogger.com/share-post.g?blogID=18493443&postID=7333076634831619009&target=blog "BlogThis!")[Share to X](https://draft.blogger.com/share-post.g?blogID=18493443&postID=7333076634831619009&target=twitter "Share to X")[Share to Facebook](https://draft.blogger.com/share-post.g?blogID=18493443&postID=7333076634831619009&target=facebook "Share to Facebook")[Share to Pinterest](https://draft.blogger.com/share-post.g?blogID=18493443&postID=7333076634831619009&target=pinterest "Share to Pinterest")

![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimxCSbi25rfvHIa7H8x-VuFqcOZaIMyVWQpCC9QOCEqIoU3vgZwnlXz5Ee7Vhoel0LK4iK1XrVIxlaCPLV4nO66Ug2qFireNLDJ4DxzdyEX0ce7Z-zJlEEBx8T6U-xDQ/s113/126817412_103684408239911_5047637022297351917_n.jpg)

[Dancho Danchev](https://draft.blogger.com/profile/09989733095447891258 "author profile")

Independent Security Consultancy, Threat Intelligence Analysis (OSINT/Cyber Counter Intelligence) and Competitive Intelligence research on demand. Insightful, unbiased, and client-tailored assessments, neatly communicated in the form of interactive reports - because anticipating the emerging threatscape is what shapes the big picture at the end of the day. Approach me at dancho.danchev@hush.com

#### No comments:

#### Post a Comment

[Newer Post](https://ddanchev.blogspot.com/2023/08/a-compilation-of-personally.html "Newer Post")

[Older Post](https://ddanchev.blogspot.com/2023/08/a-diy-cryptocurrency-exchange-phishing.html "Older Post")
[Home](https://ddanchev.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://ddanchev.blogspot.com/feeds/7333076634831619009/comments/default)

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

[![My photo](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimxCSbi25rfvHIa7H8x-VuFqcOZaIMyVWQpCC9QOCEqIoU3vgZwnlXz5Ee7Vhoel0LK4iK1XrVIxlaCPLV4nO66Ug2qFireNLDJ4DxzdyEX0ce7Z-zJlEEBx8T6U-xDQ/s113/126817412_103684408239911_5047637022297351917_n.jpg)](https://draft.blogger.com/profile/09989733095447891258)

[Dancho Danchev](https://draft.blogger.com/profile/09989733095447891258)
:   Independent Security Consultancy, Threat Intelligence Analysis (OSINT/Cyber Counter Intelligence) and Competitive Intelligence research on demand. Insightful, unbiased, and client-tailored assessments, neatly communicated in the form of interactive reports - because anticipating the emerging threatscape is what shapes the big picture at the end of the day. Approach me at dancho.danchev@hush.com

[View my complete profile](https://draft.blogger.com/profile/09989733095447891258)

## Advertising

[![Advertising](https://blogger.googleusercontent.com/img/a/AVvXsEidy2Zb8F-XChMCcR5UILmNDe-GU6DfbE6HZIhEHNunMnXIln_LZHiRlq3HpZGu0BH-waH9H364iVLwFELKVuwi6S8T1nLefnEYpGp_0CZa7-PaYq7gH69fJSk_NPrjxoX_6zkGLQm_OhSCMekkvV4pNVklcNOlxmZ7qAYZrIFQs3aYyGT3bt03=s302)](https://paranoidlab.com/)

## Advertising

[![Advertising](https://blogger.googleusercontent.com/img/a/AVvXsEhcrNd5G6iJ_PiE-nM0oSLWzvbkBx5cDm...
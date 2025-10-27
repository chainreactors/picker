---
title: Exposing Hacking Team GhostSec - An Analysis
url: https://ddanchev.blogspot.com/2023/05/exposing-hacking-team-ghostsec-analysis.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2023-05-21
fetch_date: 2025-10-04T11:37:59.815327
---

# Exposing Hacking Team GhostSec - An Analysis

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

Independent Contractor. Bitcoin: 15Zvie1j8CjSR52doVSZSjctCDSx3pDjKZ Email: dancho.danchev@hush.com OMEMO: ddanchev@conversations.im | OTR: danchodanchev@xmpp.jp | TOX ID: 53B409440A6DC34F1BA458869A0462D92C15B467AF6319D481CA353690C88667833A0EE82969

## Saturday, May 20, 2023

### Exposing Hacking Team GhostSec - An Analysis

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSvcnYYY17N_UBVADe8CNoeMoGPVbwwcgRQou5GyFubNjuVDIJAasIgQY-2bjJmWHxRdIpQUgrk9WRVc_vhGMpkRpbFgxhDG6itY2szsb6zVITRz59YmHQu2v9YATKfZlqRpP9p3qZ7YP5ujohAy0Jq928BL--fL4b0TRBCEVT1vFhYaykzw/s320/326553170_1243379373055728_773401334921176637_n.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSvcnYYY17N_UBVADe8CNoeMoGPVbwwcgRQou5GyFubNjuVDIJAasIgQY-2bjJmWHxRdIpQUgrk9WRVc_vhGMpkRpbFgxhDG6itY2szsb6zVITRz59YmHQu2v9YATKfZlqRpP9p3qZ7YP5ujohAy0Jq928BL--fL4b0TRBCEVT1vFhYaykzw/s789/326553170_1243379373055728_773401334921176637_n.png)

In this post I'll profile Hacking Team GhostSec and I'll provide all the relevant and necessary IoCs (Indicators of Compromise) including all the relevant personally identifiable information in terms of assisting U.S Law Enforcement and the U.S Intelligence Community on its way to properly track down and monitor and prosecute the cybercriminals behind these campaigns.

**Personal Photos:**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgr0-LPZxubfPjEF4nCX9Cut3s7FXStdwze2KcMmlzD-uo-TCYxecoSFX6A2hJQKrd3esC4rGna7e7CsNOT08ahNeOZjt2Seda0KLbLbz1tSP6KeQEyZZCQ2za4lGemx5tpPDdjb7FyVD-qtmiymKk1IExA_BNMXXu13NMzA2FVQbPh4tx3Iw/s320/7809930_20150710101658.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgr0-LPZxubfPjEF4nCX9Cut3s7FXStdwze2KcMmlzD-uo-TCYxecoSFX6A2hJQKrd3esC4rGna7e7CsNOT08ahNeOZjt2Seda0KLbLbz1tSP6KeQEyZZCQ2za4lGemx5tpPDdjb7FyVD-qtmiymKk1IExA_BNMXXu13NMzA2FVQbPh4tx3Iw/s640/7809930_20150710101658.jpg)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCOOcVHyrrCVSa7F0VBYI-XJk4zxy5GF0WJYph_TAPInIcHFH1DLzmeHim5BYuhKbsAMaEHPQHdYenIj3KMqJuqSUsrpyQpstKo8mgznutuP04F5DURAaGG2yExj5cejYbKgFN0D1rhwAdh4VjRbXRFLL92W2YWmvtnqi_QVXeEEabMJ-VQA/s320/7809930_20150710101833.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCOOcVHyrrCVSa7F0VBYI-XJk4zxy5GF0WJYph_TAPInIcHFH1DLzmeHim5BYuhKbsAMaEHPQHdYenIj3KMqJuqSUsrpyQpstKo8mgznutuP04F5DURAaGG2yExj5cejYbKgFN0D1rhwAdh4VjRbXRFLL92W2YWmvtnqi_QVXeEEabMJ-VQA/s640/7809930_20150710101833.jpg)

**Related IoCs and personally identifiable information for GhostSec:**

**Official Web Site URL:** hxxp://opiceisis.strangled.net

**Official Web Site URL:** hxxp://81.4.124.11/index.php

**Official Web Site URL:**hxxp://pst.klgrth.io

**Official Group's Twitter account:** hxxp://twitter.com/ghost\_s3curity

**Official Group's Telegram account:**hxxp://t.me/GhostSecc

**Official Group's Medium account:**hxxp://medium.com/@OfficialGhostSec

**Official Group's Web Site URL:** hxxp://ghostsec-team.org

**Official Group's Web Site URL:** hxxp://ghostsecret-team.blogspot.com

**Official Group's Email Address Account:** ghostsecteam.org@gmail.com

Stay tuned!

-
[May 20, 2023](https://ddanchev.blogspot.com/2023/05/exposing-hacking-team-ghostsec-analysis.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/18493443/6562373832069093781 "Email Post")

[Email This](https://www.blogger.com/share-post.g?blogID=18493443&postID=6562373832069093781&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=18493443&postID=6562373832069093781&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=18493443&postID=6562373832069093781&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=18493443&postID=6562373832069093781&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=18493443&postID=6562373832069093781&target=pinterest "Share to Pinterest")

![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimxCSbi25rfvHIa7H8x-VuFqcOZaIMyVWQpCC9QOCEqIoU3vgZwnlXz5Ee7Vhoel0LK4iK1XrVIxlaCPLV4nO66Ug2qFireNLDJ4DxzdyEX0ce7Z-zJlEEBx8T6U-xDQ/s113/126817412_103684408239911_5047637022297351917_n.jpg)

#### No comments:

#### Post a Comment

[Newer Post](https://ddanchev.blogspot.com/2023/05/exposing-denis-gennadievich-kulkov-aka.html "Newer Post")

[Older Post](https://ddanchev.blogspot.com/2023/05/happy-holidays-from-not-republic-of.html "Older Post")
[Home](https://ddanchev.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://ddanchev.blogspot.com/feeds/6562373832069093781/comments/default)

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
:   Independent Security Consultancy, Threat Intelligence Analysis (OSINT/Cyber Counter Intelligence) and Competitive Intelligence research on demand. Insightful, unbiased, and client-tailored assessments, neatly communicated in the form of interactive reports - because anticipating the emerging threatscape is what shapes the big picture at the end of the day. Approach me at dancho.danchev@hush.com

[View my complete profile](https://www.blogger.com/profile/09989733095447891258)

## Advertising

[![Advertising](https://blogger.googleusercontent.com/img/a/AVvXsEidy2Zb8F-XChMCcR5UILmNDe-GU6DfbE6HZIhEHNunMnXIln_LZHiRlq3HpZGu0BH-waH9H364iVLwFELKVuwi6S8T1nLefnEYpGp_0CZa7-PaYq7gH69fJSk_NPrjxoX_6zkGLQm_OhSCMekkvV4pNVklcNOlxmZ7qAYZrIFQs3aYyGT3bt03=s302)](https://paranoidlab.com/)

## Advertising

[![Advertising](https://blogger.googleusercontent.com/img/a/AVvXsEhcrNd5G6iJ_PiE-nM0oSLWzvbkBx5cDmCDPL2kHIPHTOsaxg5cg1YUe_lOXhXjO380aNfHztAWMSAC-8k5wNfQUn3WwgAO_P9kqm7I0hEZVvz9ga8-KMRtu5OrwVlY0qeuU6YWkA3z74n23Tl28__-ktoGX0oGLM7vMjNF05udxmOEptyotwTq=s302)](https://steeletrezza.com/)

## Dark Web Onion

[![Dark Web Onion](https://blogger.googleusercontent.com/img/a/AVvXsEgszW6q5yn9T94NAAJQWwQoh59gj-UruZmEdrL4jM3wJ_B_pwybMpBD7Qpt5FmJDoNbZK1kz_R77eLy472Yl8zFGstlo-jYQA_m4tNkNWSEBPCfRqbc04AWrHwxOFBumM4gnoc0OPezxbzQ-16t3RO1kYiNWT8lYZ5sw7yjKZ8FSXm_pWVLUPVT=s302)](http://ddancmx2pxxxkpelzwenwrbiq2t5p3quh4jihdjzr6z4rupi4wuxauad.onion/)

## Dark Web Onion E-Shop for Threat Intelligence Deliverables

[![Dark Web Onion E-Shop for Threat Intelligence Deliverables](https://blogger.googleusercontent.com/img/a/AVvXsEhTR0H8gEbNxJMlDe2GgNMMLpZMb2aleqaCEppu6O1KORvLqwfqEnK53KDlfAQaum3Y7o1GV0J5kgRm...
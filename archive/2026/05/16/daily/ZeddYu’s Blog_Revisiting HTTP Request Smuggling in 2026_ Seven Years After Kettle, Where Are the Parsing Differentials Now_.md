---
title: Revisiting HTTP Request Smuggling in 2026: Seven Years After Kettle, Where Are the Parsing Differentials Now?
url: https://blog.zeddyu.info/2026/05/16/Revisiting-HTTP-Smuggling-2026/
source: ZeddYu’s Blog
date: 2026-05-16
fetch_date: 2026-05-17T05:47:36.351027
---

# Revisiting HTTP Request Smuggling in 2026: Seven Years After Kettle, Where Are the Parsing Differentials Now?

* [Skip to primary navigation](#site-nav)
* [Skip to content](#main)
* [Skip to footer](#footer)

[ZeddYu's Blog](/)

Toggle menu

### [ZeddYu](https://blog.zeddyu.info/)

Security Researcher. HTTP Smuggling, Web Security, CTF.

Follow

# [Revisiting HTTP Request Smuggling in 2026: Seven Years After Kettle, Where Are the Parsing Differentials Now?](https://blog.zeddyu.info/2026/05/16/Revisiting-HTTP-Smuggling-2026/)

12 minute read

#### On this page

* [ä¸­æé¨å](#ä¸­æé¨å)
  + [2026 å¹´çç ç©¶èæ¯](#2026-å¹´çç ç©¶èæ¯)
  + [å®éªææ](#å®éªææ)
  + [ä¸ä¸ªåå§åä½å¨ 2026 å¹´çç¶æ](#ä¸ä¸ªåå§åä½å¨-2026-å¹´çç¶æ)
    - [CL.TE](#clte)
    - [TE.CL](#tecl)
    - [TE.TEï¼Transfer-Encoding æ··æ·ï¼](#tetetransfer-encoding-æ··æ·)
  + [ä¸ä¸ªæ°ç 2020-2025 åä½](#ä¸ä¸ªæ°ç-2020-2025-åä½)
    - [CL.0ï¼Content-Length: 0 + åç½® bodyï¼](#cl0content-length-0--åç½®-body)
    - [HTTP/2 â HTTP/1.1 éçº§ desync](#http2--http11-éçº§-desync)
    - [Transfer-Encoding å¤éå¤´é¨](#transfer-encoding-å¤éå¤´é¨)
  + [ç¼å­ææ¯åèµ°ç§çå³ç³»](#ç¼å­ææ¯åèµ°ç§çå³ç³»)
  + [ä¸­æé¨åå°ç»](#ä¸­æé¨åå°ç»)
* [English section](#english-section)
  + [Why I am writing this in 2026](#why-i-am-writing-this-in-2026)
  + [Method](#method)
  + [The three classical variants in 2026](#the-three-classical-variants-in-2026)
    - [CL.TE direct](#clte-direct)
    - [TE.CL direct](#tecl-direct)
    - [TE.TE obfuscation](#tete-obfuscation)
  + [Three new variants from 2020-2025 research](#three-new-variants-from-2020-2025-research)
    - [CL.0](#cl0)
    - [HTTP/2 â HTTP/1.1 downgrade desync](#http2--http11-downgrade-desync)
    - [Transfer-Encoding header repetition not collapsed](#transfer-encoding-header-repetition-not-collapsed)
  + [Results table](#results-table)
  + [What I take from this seven years on](#what-i-take-from-this-seven-years-on)
  + [What I will publish next](#what-i-will-publish-next)
  + [References](#references)

This post is a 2026 follow-up to two 2019 articles I wrote on this blog: the Chinese-language [HTTP Request Smuggling ç ç©¶ç¬è®°](/2019/12/05/HTTP-Smuggling/) and its English counterpart [HTTP Request Smuggling - A Complete Guide](/2019/12/08/HTTP-Smuggling-en/). Both posts described the CL.TE / TE.CL / TE.TE matrix as it existed after James Kettleâs [HTTP Desync Attacks: Request Smuggling Reborn](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn) at Black Hat USA 2019, and recorded a Waitress finding I reported to the Pylons project at the time ([Pylons/waitress#273](https://github.com/Pylons/waitress/issues/273)).

Seven years later, I wanted to re-run the same test plan against current versions of the proxies and back-ends that anchored the 2019 results, and to incorporate the variants the community has documented since then (HTTP/2 downgrade desync, CL.0, HTTP/2 stream splitting). The aim is not a comprehensive survey. It is to give a 2026 practitioner an honest read on which of the 2019 primitives still produce parsing differentials in mainstream deployments, and which have been closed.

This post is bilingual. The Chinese half comes first, mirroring the format of the 2019 twin articles. The English half follows.

---

## ä¸­æé¨å

### 2026 å¹´çç ç©¶èæ¯

2019 å¹´ Kettle å¨ Black Hat USA æ¼è®²ä¹åï¼HTTP è¯·æ±èµ°ç§ä»ä¸ä¸ªè¢«éå¿ç 2005 å¹´ç ç©¶æ¹åéæ°è¿å¥ä¸»æµãPylons é¡¹ç®ç»´æ¤èçº¿ç¨ä¸­æå°ç [HTTP-Smuggling-Lab](https://github.com/ZeddYu/HTTP-Smuggling-Lab) å¤ç°äºå½æ¶å·²ç¥çææåä½ãè¿å»ä¸å¹´éåçäºä¸ä»¶å¼å¾è®°å½çäºï¼

1. **è§èå±é¢ï¼** RFC 7230 å¨ 2022 å¹´è¢« RFC 9110 å RFC 9112 åä»£ãæ°è§èå¯¹ Content-Length å Transfer-Encoding çå³ç³»ç»åºäºæ´æç¡®çå¤çï¼[RFC 9112 Section 6.1](https://www.rfc-editor.org/rfc/rfc9112#section-6.1) æç¡®è¦æ±å®ç°æç»åæ¶åå«ä¸¤ä¸ªé¿åº¦å¤´é¨çè¯·æ±ãè¿æ¯ä¸ä¸ªæ åå±é¢çä¿®å¤ï¼ä½åªå¯¹å¨ 2022 å¹´ä¹åæå¤§å¹éåè§£ææ çå®ç°ææä¹ã
2. **åè®®å±é¢ï¼** Kettle å¨ 2021 å¹´åå¸ç [HTTP/2: The Sequel is Always Worse](https://portswigger.net/research/http2) æç ç©¶éå¿ä» HTTP/1.1 ä¸ç CL.TE / TE.CL æ¨å°äº HTTP/2 â HTTP/1.1 éçº§æé æç desyncã2022 å¹´ [Browser-Powered Desync Attacks](https://portswigger.net/research/browser-powered-desync-attacks) æåä¸ä¸ªæ»å»é¢è¿ä¸æ­¥æ¾å¤§å°å®¢æ·ç«¯å¯ä»¥è¯±å¯¼æµè§å¨åä¸çåºæ¯ã
3. **å®ç°å±é¢ï¼** NginxãHAProxyãEnvoyãCaddyãCloudflareãFastly å¨è¿å»ä¸å¹´éé½è³å°å¯¹ CL.TE / TE.CL åäºä¸è½®æç¡®çç¡¬åãå¶ä¸­ä¸é¨åç¡¬åæ¯è§èé©±å¨çï¼å¦ä¸é¨åæ¯å¨ PortSwigger Top 10 Web Hacking Techniques æåé¡µå¬å¼ä¹åçè¡¥ä¸ã

æå¨è¿æ¬¡å¤ç°ä¸­éæ°æ§è¡äº 2019 å¹´é£ç¯æç« éçæ ¸å¿æ¹æ³ï¼æ­ä¸ä¸ªåç«¯ä»£ç + åç«¯æå¡å¨çæå°ææï¼å¾åç«¯ååæ¶åå« Content-Length å Transfer-Encoding çè¯·æ±ï¼æä¸ç³»åå·²ç¥çæ··æ·æ¹å¼ï¼è§å¯åç«¯æ¯å¦æ¥åäºèµ°ç§åºå»çä¸ä¸ä¸ªè¯·æ±ã

### å®éªææ

ææµè¯äºå­ç§åç«¯ Ã ä¸ç§åç«¯çç»åï¼

**åç«¯ä»£çï¼**

* Nginx 1.27ï¼å¼æºçï¼HTTP/1.1 æ¨¡å¼ï¼
* HAProxy 2.9
* Envoy 1.32
* Caddy 2.8
* Cloudflareï¼çäº§è¾¹ç¼ï¼2026-05 æµè¯æ¶æ®µï¼
* Fastly VCL æå¡ï¼çäº§è¾¹ç¼ï¼

**åç«¯æå¡å¨ï¼**

* Gunicorn 22.0ï¼CPython 3.12ï¼
* Waitress 3.0ï¼Pylons é¡¹ç®ï¼2019 å¹´é£æ¬¡èµ°ç§çåä¸ä¸ª WSGI æå¡å¨ï¼
* Node.js 22 LTSï¼`http.createServer`ï¼æªå¯ç¨ `insecureHTTPParser`ï¼

å¯¹æ¯ä¸å¯¹ç»åï¼ææ 2019 é£ç¯æç« éä½¿ç¨çå­ä¸ª payload éæ°è·äºä¸éï¼å¹¶å ä¸ 2020-2025 å¹´å¬å¼æ«é²çä¸ä¸ªæ°åä½ï¼CL.0ãHTTP/2 â HTTP/1.1 éçº§ãTE å¤´é¨å¤æ¬¡éå¤ç obfuscationï¼ã

### ä¸ä¸ªåå§åä½å¨ 2026 å¹´çç¶æ

#### CL.TE

åç«¯æ Content-Length è§£æï¼åç«¯æ Transfer-Encoding è§£æãè¿æ¯ 2019 å¹´æå¸¸è§çåä½ã

```
POST / HTTP/1.1
Host: target.example
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
```

2026 å¹´ç»æï¼å­ä¸ªåç«¯ä¸­æ **äºä¸ª** ç´æ¥æç»äºåæ¶åå«ä¸¤ä¸ªå¤´é¨çè¯·æ±ï¼è¿å 400ãè¿ä¸ RFC 9112 Â§6.1 çæç¡®è¦æ±ä¸è´ãå©ä¸çä¸ä¸ªï¼Caddy 2.8ï¼è½¬åäºè¯·æ±ï¼ä½æ¯ä¼æ Transfer-Encoding å¤´é¨è§èåä¸º `chunked` å­é¢å¼ï¼ä½¿åç«¯è§£æçç»æä¸åç«¯æå¾çä¸è´ãè¿ä¸ä¸ªç»åä¸ææå¯å©ç¨ç CL.TE åè¯­ã

ç»è®ºï¼ç´æ¥ç CL.TE åä½å¨ 2026 å¹´çä¸»æµé¨ç½²ä¸­å·²ç»æ æ³äº§ç desyncã

#### TE.CL

åç«¯æ Transfer-Encoding è§£æï¼åç«¯æ Content-Length è§£æã

```
POST / HTTP/1.1
Host: target.example
Content-Length: 3
Transfer-Encoding: chunked

8
SMUGGLED
0
```

2026 å¹´ç»æï¼å CL.TE ç±»ä¼¼ï¼å¤§å¤æ°åç«¯å¨çå°åæ¶å­å¨ä¸¤ä¸ªå¤´é¨æ¶æç»è¯·æ±ãWaitress 3.0 å¨æçæµè¯ä¸­å¯¹ Content-Length çå¤çæ¯ 2019 å¹´ç 1.4 çæ¬ä¸¥æ ¼å¾å¤ãPylons é¡¹ç®å¨ 2020 è³ 2022 å¹´é´åå¸äºå¤æ¬¡å®å¨ç¸å³çè§£æç¡¬åï¼åå§ç [Pylons/waitress#273](https://github.com/Pylons/waitress/issues/273) å·²ç»ä¿®å¤å¹¶è¢«åç»­æäº¤è¿ä¸æ­¥å åºãWaitress ä¸åæ¯å¯èµ°ç§çåç«¯ã

ç»è®ºï¼ç´æ¥ç TE.CL åä½å¨ 2026 å¹´ä¹å·²ç»æ æ³å¯é å°äº§ç desyncã

#### TE.TEï¼Transfer-Encoding æ··æ·ï¼

éè¿éæ³è¡ç»æç¬¦æ header åå­å¤§å°åå·®å¼ï¼è®©ä¸å°æå¡å¨è¯å« Transfer-Encoding å¤´é¨èå¦ä¸å°ä¸è¯å«ã

```
Transfer-Encoding: xchunked
Transfer-Encoding : chunked
Transfer-Encoding: chunked
Transfer-Encoding: x
```

2026 å¹´ç»æï¼è¿æ¯ä¸ä¸ªåå§åä½é **å¯ä¸ä¸ä¸ªæä»ç¶è½å¨ä¸»æµç»åä¸è§å¯å° desync ç**ãå·ä½å°ï¼

* Envoy 1.32 + Gunicorn 22.0ï¼å½ `Transfer-Encoding` å¤´é¨åé¢å¸¦æä¸ä¸ª vertical-tab å­ç¬¦ï¼`\x0b`ï¼ä½ä¸ºåéç¬¦æ¶ï¼Envoy æå®å½ä½ä¸åè§ä½ä»ç¶è§£æï¼normalizing åä¸¢å¼ï¼ï¼è Gunicorn ç´æ¥æç»è¯¥å¤´é¨ãåç«¯æ chunked å¤çï¼...
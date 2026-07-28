---
title: One Header Away from 10+ GB of Customer Documents (PII) — $6K Bounty
url: https://infosecwriteups.com/one-header-away-from-10-gb-of-customer-documents-pii-6k-bounty-0c0ac8c335f2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-27
fetch_date: 2026-07-28T04:58:45.469675
---

# One Header Away from 10+ GB of Customer Documents (PII) — $6K Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fone-header-away-from-10-gb-of-customer-documents-pii-6k-bounty-0c0ac8c335f2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fone-header-away-from-10-gb-of-customer-documents-pii-6k-bounty-0c0ac8c335f2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0c0ac8c335f2---------------------------------------)

·

1. [The first bug — Forgeable Referer Header Bypass](/?source=post_page-----0c0ac8c335f2---------------------------------------#ed41 "The first bug — Forgeable Referer Header Bypass")
   1. [How I got to the bucket in the first place??](/?source=post_page-----0c0ac8c335f2---------------------------------------#36c0 "How I got to the bucket in the first place??")
2. [The second bug — Unauthenticated Signer](/?source=post_page-----0c0ac8c335f2---------------------------------------#6aa9 "The second bug — Unauthenticated Signer")
   1. [Proving overwrite, not just upload](/?source=post_page-----0c0ac8c335f2---------------------------------------#0cd8 "Proving overwrite, not just upload")
3. [Whose bug is this?](/?source=post_page-----0c0ac8c335f2---------------------------------------#ee63 "Whose bug is this?")
4. [Remediation](/?source=post_page-----0c0ac8c335f2---------------------------------------#d885 "Remediation")
5. [Closing](/?source=post_page-----0c0ac8c335f2---------------------------------------#7fed "Closing")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0c0ac8c335f2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Bug Bounty Writeup

Bucketlist

Bug Bounty

Bug Bounty Tips

Authentication

# **One Header Away from 10+ GB of Customer Documents (PII) — $6K Bounty**

[![Alvin Ferdiansyah](https://miro.medium.com/v2/resize:fill:64:64/1*jCQW4Dcioim59s1E0JwOqQ@2x.jpeg)](https://alvinferd.medium.com/?source=post_page---byline--0c0ac8c335f2---------------------------------------)

[Alvin Ferdiansyah](https://alvinferd.medium.com/?source=post_page---byline--0c0ac8c335f2---------------------------------------)

7 min read

·

2 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D0c0ac8c335f2&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fone-header-away-from-10-gb-of-customer-documents-pii-6k-bounty-0c0ac8c335f2&source=---header_actions--0c0ac8c335f2---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

Sample Document Leaked

An anonymous attacker could fully enumerate, read, and overwrite the production customer-service attachment bucket of a major insurer’s China operation.

The bucket backs the file-upload flow of their WeChat customer-service chatbot, held massive customer chat attachments; photos of identity cards, hospital certificates, policy screens, confidential documents, etc. Anyone on the internet could read all of it.

> **A quick aside, if you’ve never touched a Chinese cloud stack.** This bucket lives on **Volcengine** (火山引擎), ByteDance’s public cloud, same parent company as TikTok and Douyin. Their object storage is called **TOS**, and it’s S3-compatible in the way that matters: same API verbs, same virtual-hosted URLs, same XML error bodies, its own HMAC-SHA256 signing scheme. Every instinct you have from S3 transfers over.
>
> What doesn’t transfer is the console. 防盗链 sits right there in the bucket settings, a few rows under CORS, presented as a normal thing to turn on. On AWS you’d have to go out of your way to write a bucket policy that conditions on aws:Referer. Here it’s a checkbox. That difference is most of the reason this bug exists.

The issue is caused by two independent authentication control failures on the same storage workflow:

1. **Anonymous read bypass**: the bucket allows unauthenticated listing of object keys, and object reads are protected only by a forgeable Referer header pointing at the app’s own domain. Any attacker can spoof this header and retrieve the full object content.
2. **Anonymous write / overwrite**: the upload signer at /api/tos/presigned-post is unauthenticated and signs attacker-supplied bucket/key values using the company’s Volcengine TOS credential. This allows anonymous uploads and overwrite-in-place of existing object keys.

## The first bug — Forgeable Referer Header Bypass

Same object, same second, same URL. Only one header changes.

```
GET /chat/message/[REDACTED]/20251211/images/[REDACTED].png
Host: [REDACTED]-prod.[REDACTED].volces.com

(no Referer)                          →  403  AccessDenied, 213 bytes
Referer: https://evil.example.com.cn/    →  403  AccessDenied, 213 bytes
Referer: https://[REDACTED].[Target].com.cn/  →  200  image/png, 7828 bytes
```

**That’s the whole bypass.**

Press enter or click to view image in full size

![]()

403 Forbidden

Press enter or click to view image in full size

![]()

Auth Bypassed

The bucket had **防盗链** switched on; anti-leech, hotlink protection. You give it a list of allowed referring domains and it blocks requests that come from anywhere else. Every Chinese cloud ships it. It exists to stop someone embedding your images on their forum and running up your bandwidth bill.

It’s a billing control. Somebody left it holding the door as an access control.

And Referer is a request header. The client writes it. There is no signature on it, no secret in it, nothing to verify. I typed the allowed domain and the bucket believed me.

### How I got to the bucket in the first place??

Well, it was pretty straightforward, although getting there took a fair amount of time. I spent hours collecting, deobfuscating, and going through JavaScript bundles from the host target, following one small clue after another. One URL led to a new function, that function pointed to another endpoint, and little by little, the trail eventually brought me to the bucket URL itself.

## The second bug — Unauthenticated Signer

Take a look at this part of the code from the bundle.

```
  cc = "[REDACTED]-prod"

  fetch("https://[app-host]/volces/api/tos/presigned-post",
        {method:"POST", headers:{"Content-Type":"application/json"},
         body:JSON.stringify({bucket:cc, key:h})})

  m = `${cc}.[REDACTED].volces.com`
  f = `https://${m}/${encodeURI(h)}`
```

The headers object has exactly one key. No Authorization, no token, nothing to strip, because nothing was ever there. It calls the app’s own backend rather than a cloud SDK, so somebody hand-wrote a signer. And both bucket and key come from th...
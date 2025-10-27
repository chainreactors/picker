---
title: How to Prove That An Email Was Received
url: https://www.metaspike.com/how-to-prove-email-was-received/
source: Instapaper: Unread
date: 2025-06-27
fetch_date: 2025-10-06T23:04:09.834347
---

# How to Prove That An Email Was Received

[Skip to main content](#ajax-content-wrap)

[![Metaspike](https://www.metaspike.com/wp-content/uploads/2017/06/Metaspike_Logo_Dark_Sm.png)![Metaspike](https://www.metaspike.com/wp-content/uploads/2017/06/Metaspike_Logo_Light_Sm.png)![Metaspike](https://www.metaspike.com/wp-content/uploads/2017/06/Metaspike_Logo_Dark_Sm.png)](https://www.metaspike.com)

[0](https://www.metaspike.com/cart/)

[Menu](#slide-out-widget-area)

* [Software](https://www.metaspike.com/software/)
* [Training](https://www.metaspike.com/product-category/training/)
* [Blog](https://www.metaspike.com/blog/)
* [FAQ](https://www.metaspike.com/faq/)
* [Resources](https://www.metaspike.com/resources/)
* [Community](https://community.metaspike.com)
* [Resellers](https://resellers.metaspike.com)
* [Contact](https://www.metaspike.com/contact/)
* [BUY NOW](https://www.metaspike.com/product-category/software/)

* [twitter](https://twitter.com/MetaspikeHQ) [bluesky](https://bsky.app/profile/metaspike.bsky.social) [linkedin](https://www.linkedin.com/company/metaspike/) [youtube](https://www.youtube.com/Metaspike)
* [0](https://www.metaspike.com/cart/)

  was successfully added to your cart.
* [Menu](#slide-out-widget-area)

![Metaspike](https://www.metaspike.com/wp-content/uploads/2017/06/Metaspike_Logo_Dark_Sm.png)

*Press enter to begin your search*
Search

Close Search

![How to Prove That An Email Was Received](https://www.metaspike.com/wp-content/uploads/2025/06/received-email.jpg)

# How to Prove That An Email Was Received

By [Arman Gungor](https://www.metaspike.com/author/agungor/ "Posts by Arman Gungor")June 25, 2025June 27th, 2025[Articles](https://www.metaspike.com/category/articles/)

[One Comment](https://www.metaspike.com/how-to-prove-email-was-received/#comments)

Proving or disproving that an email of interest was received by the intended recipient is a request I received countless times throughout my digital forensics career. The request often goes as follows: “*My opponent produced an email they claim to have sent me. I want to prove I never received this email.*” Or, occasionally, it is the reverse: “*I sent an email to my opponent, and they claim that they never received it. How can I prove that they did receive my email?*“

In this article, I aim to discuss what the evidence can reveal when we review the sender’s copy of an email, how one can further investigate if the email was received, and what senders can do proactively to position themselves so that they are prepared to prove receipt of an email they send.

## Sender’s Copy of The Email — Printout

Let’s start with a scenario where all that is available to us is a printout or screenshot of the sender’s copy of the email. What can this tell us, and how can it be authenticated?

The printout displays the message body and standard email metadata, including the sender, recipient, subject, attachment names, and origination date (although without the time zone and with only minute precision). One may examine such a printout and potentially determine the following:

* What email client was used to print the email
* If the printout was prepared from an electronic copy of the email (can help us surmise if a native or near-native copy of the email was available to the producing party at the time the printout was prepared)
* If the printout was modified after the email had been printed (e.g., by editing a PDF)
* If there are any apparent timing or time zone discrepancies
* If the signature blocks and company-wide disclaimers, if any, are where they should be
* What font was used in the email, if there are any timing issues related to the use of that font, and if there are any font, font size, or font color discrepancies within the email that would suggest copy / paste or modification
* If any stylistic patterns in the email body could help identify the author

And more.

In short, while far from ideal, an email printout is not useless by any means. That said, it would be challenging to authenticate an email based on a printout alone conclusively. At best, the investigator can examine the email for red flags. The lack of red flags does not guarantee authenticity.

What is often more important is what the email printout does not show us. I will cover this in the next section. As Craig Ball once wrote about converting an electronic document to an image format:

> “*It’s* *like photographing a steak. You can see it, but you can’t smell, taste or touch it; you can’t hear the sizzle, and you surely can’t eat it.*“

This apt description also applies here. We can see what the email looks like, but we cannot see the email’s structure or many key metadata fields.

## Sender’s Copy of The Email — Electronic MIME Message

What if, instead of a printout, we had an electronic version of the sender’s copy of the message in MIME format? What can we glean from an electronic copy that we were missing with the printout? As it turns out, a lot.

```
Return-Path: <ornatdilwen@gmail.com>
Received: from DESKTOPOI5E6B6 ([169.150.218.87])
        by smtp.gmail.com with ESMTPSA id gs19-20020a170906f19300b00992f81122e1sm2947754ejb.21.2023.07.19.16.23.10
        for <fecdev@yahoo.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);
        Wed, 19 Jul 2023 16:23:11 -0700 (PDT)
From: "Ornat Dilwen" <ornatdilwen@gmail.com>
To: <fecdev@yahoo.com>
Subject: Upcoming Project
Date: Wed, 19 Jul 2023 16:23:07 -0700
Organization: Tekoa Damyun, LLC
Message-ID: <015301d9ba97$fb561110$f2023330$@gmail.com>
MIME-Version: 1.0
Content-Type: multipart/mixed;
  boundary="----=_NextPart_000_0154_01D9BA5D.4EF73910"
X-Mailer: Microsoft Outlook 14.0
Thread-Index: Adm6l7GMpPw44vDsSjOFgADxIFhLeA==
Content-Language: en-us

This is a multipart message in MIME format.

------=_NextPart_000_0154_01D9BA5D.4EF73910
Content-Type: multipart/related;
  boundary="----=_NextPart_001_0155_01D9BA5D.4EF73910"

------=_NextPart_001_0155_01D9BA5D.4EF73910
Content-Type: multipart/alternative;
  boundary="----=_NextPart_002_0156_01D9BA5D.4EF73910"

------=_NextPart_002_0156_01D9BA5D.4EF73910
Content-Type: text/plain;
  charset="us-ascii"
Content-Transfer-Encoding: 7bit

Hello,

After carefully considering your requirements and objectives, our team has
formulated a comprehensive plan that aligns with your vision. I have
attached the detailed financial analysis outlining the scope, timeline, and
cost estimates for your review.

We are confident that our expertise and tailored approach will result in a
successful partnership. Should you have any questions or require further
information, please do not hesitate to reach out. We look forward to the
opportunity to work together and bring this project to fruition.

Ornat Dilwen

Tekoa Damyun, LLC

Description: tdamyun

------=_NextPart_002_0156_01D9BA5D.4EF73910
Content-Type: text/html;
  charset="us-ascii"
Content-Transfer-Encoding: quoted-printable

<html xmlns:v=3D"urn:schemas-microsoft-com:vml" =
xmlns:o=3D"urn:schemas-microsoft-com:office:office" =
xmlns:w=3D"urn:schemas-microsoft-com:office:word" =
xmlns:m=3D"http://schemas.microsoft.com/office/2004/12/omml" =
xmlns=3D"http://www.w3.org/TR/REC-html40"><head><META =
HTTP-EQUIV=3D"Content-Type" CONTENT=3D"text/html; =
charset=3Dus-ascii"><meta name=3DGenerator content=3D"Microsoft Word 14 =
(filtered medium)"><!--[if !mso]><style>v\:* =
{behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
w\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style><![endif]--><style><!--
/* Font Definitions */
@font-face
  {font-family:Calibri;
  panose-1:2 15 5 2 2 2 4 3 2 4;}
@font-face
  {font-family:Tahoma;
  panose-1:2 11 6 4 3 5 4 4 2 4;}
@font-face
  {font-family:Bahnschrift;
  panose-1:2 11 5 2 4 2 4 2 2 3;}
/* Style Definitions */
p.MsoNormal, li.MsoNormal, div.MsoNormal
  {margin:0in;
  margin-bottom:.0001pt;
  font-size:11.0pt;
  font-family:"Calibri","sans-serif";}
a:link, span.MsoHyperlink
  {mso-style-priority:99;
  color:blue;
  text-decorat...
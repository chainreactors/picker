---
title: Account Takeover Via Poising Forget Password Port in ASDA
url: https://infosecwriteups.com/account-takeover-via-poising-forget-password-port-in-asda-60f1a5417a75?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-24
fetch_date: 2025-10-04T10:28:47.097454
---

# Account Takeover Via Poising Forget Password Port in ASDA

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F60f1a5417a75&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccount-takeover-via-poising-forget-password-port-in-asda-60f1a5417a75&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccount-takeover-via-poising-forget-password-port-in-asda-60f1a5417a75&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-60f1a5417a75---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-60f1a5417a75---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Account Takeover Via Host Header Poisoning in ASDA

[![M7arm4n](https://miro.medium.com/v2/resize:fill:64:64/1*M_MP-PvKnGRNvTWFHcVI7g.jpeg)](https://m7arm4n.medium.com/?source=post_page---byline--60f1a5417a75---------------------------------------)

[M7arm4n](https://m7arm4n.medium.com/?source=post_page---byline--60f1a5417a75---------------------------------------)

7 min read

·

Mar 23, 2023

--

1

Listen

Share

Hi amazing researcher, Welcome to another review of the vulnerability discovery on ASDA. Today I want to discuss Host Header Poisoning leading to a one-click-to-account takeover BUT that wasn’t a normal one. technically I used open redirect and Port Poisoning to exploit this vulnerability. Be my guest…

Press enter or click to view image in full size

![]()

Let’s talk about the basic knowledge of Host Header Poisoning. Normally this method uses for cache Poisoning or forgets password function. The Cache Poisoning has a long way but today our story is about forgetting password functionality.

when a hacker faces a forget password function, which sends a link with a token to update the password. If the hacker can access the victim’s fresh token. Takeover the victim’s account is piece of cake. there are many ways to bypass it and access the token, such as weaknesses in the token’s cryptography or leaking, etc.

One of the popular exploits is manipulating a vulnerable website into generating a password reset link pointing to a domain under their control till when the victim opens the poisoned link the victim’s redirected to the attacker’s website and the user’s unused token logging to the attacker’s domain control. Here is an example of exploit flow:

Press enter or click to view image in full size

![]()

**Why does this vulnerability exist?**

It exists when potential user-controlled data is used to create a password reset link. That may be in the host header request which already exists or should add manually, or even on parameters in the body or get parameters, as long as it is user-controlled and is not filtered/checked, it may result in Password Reset Poisoning. Here’s an example PHP code that checks for the `host` parameter in the JSON body of the request. If the `host` parameter exists, it uses it to construct the reset password URL. If the `host` parameter does not exist, it falls back to the X-Forwarded-Host header from the request. If both the `host` parameter and X-Forwarded-Host header do not exist, it uses the main host as the default. Can you exploit it!? Well done👏. Now try to make it safe😄

```
<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $json_body = json_decode(file_get_contents('php://input'), true);
  $email = $json_body['email'];
  $host = isset($json_body['host']) ? $json_body['host'] : $_SERVER['HTTP_X_FORWARDED_HOST'];

  // If the host parameter is not set and the X-Forwarded-Host header is not set, use the main host as the default
  if (empty($host)) {
    $host = $_SERVER['HTTP_HOST'];
  }

  // Check if email exists in the database
  // If the email exists, generate a unique reset password token
  // Store the token and email in the database

  $reset_password_url = 'https://' . $host . '/reset_password.php?token=' . $token;

  $to = $email;
  $subject = 'Reset Password Link';
  $message = 'Click the following link to reset your password: ' . $reset_password_url;
  $headers = 'From: example@example.com' . "\r\n" .
      'Reply-To: example@example.com' . "\r\n" .
      'X-Mailer: PHP/' . phpversion();

  // Send the reset password link to the user's email
  if (mail($to, $subject, $message, $headers)) {
    echo 'Reset password link has been sent to your email';
  } else {
    echo 'Failed to send reset password link';
  }
}

?>
```

Here are some useful headers you can use in forget password requests, Be my guest…😉

```
    - Replace Host Header → Host: attacker.com [Report](https://hackerone.com/reports/226659)
    - Add Commons Header:
        - X-Forwarded-Host: attacker.com [Report](https://hackerone.com/reports/182670)
        - X-Forwarded-For: attacker.com
        - X-Forwarded-Proto: attacker.com
        - X-Host: attacker.com
        - X-Forwarded-Server: attacker.com
        - X-HTTP-Host-Override: attacker.com
        - Forwarded: attacker.com
        - X-Forwarded: attacker.com
    - Change Origin → Origin: attacker.com
    - Change Referer → Referer: attacker.com [Report](https://hackerone.com/reports/229498)
    - Redirect X-Forwarded-Host (whitelist) → X-Forwarded-Host: attacker.com/.site.com [Report](https://hackerone.com/reports/698416)
    - Change Path URI → GET https://attacker.com/forget-pass [Report](https://hackerone.com/reports/158482)
```

Sometimes it’s possible when you try to exploit you faced some errors such as 400 status, etc. One of the usual bypasses for this position is adding line wrapping:

```
POST /reset-password HTTP/1.1
 Host: Site.com
Host: evil.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0
```

Now we have good knowledge of **Host Header Poisoning**, It’s time to back the original story. I skip the recon part and want to talk about the exploit part.

After I reached to website tried to analyze the flow of the forgetting password part. The website generates a reset password and emails it to the user. So I tried to use common exploits and fuzz for a hidden parameter or a hidden request header that is user-controlled data that effect on reset password link. Unfortunately, my testing wasn’t successful, and unable to reach any parameter or header that effect the reset password link. but I wasn’t losing hope and a sound in my head said this is vulnerable just keep working.

Most programs and platforms do not accept HTML injection on email or mark it as low impact, But sometimes that helps us to steal user tokens or even OTP codes from email but **HOW**!? We have an unpopular vulnerability called **Dan...
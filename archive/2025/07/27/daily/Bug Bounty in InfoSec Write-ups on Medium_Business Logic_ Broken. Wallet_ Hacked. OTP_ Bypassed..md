---
title: Business Logic: Broken. Wallet: Hacked. OTP: Bypassed.
url: https://infosecwriteups.com/business-logic-broken-wallet-hacked-otp-bypassed-d82e6591a63a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-27
fetch_date: 2025-10-06T23:17:35.761607
---

# Business Logic: Broken. Wallet: Hacked. OTP: Bypassed.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd82e6591a63a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbusiness-logic-broken-wallet-hacked-otp-bypassed-d82e6591a63a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbusiness-logic-broken-wallet-hacked-otp-bypassed-d82e6591a63a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d82e6591a63a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d82e6591a63a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Business Logic: Broken. Wallet: Hacked. OTP: Bypassed.

[![Het Patel](https://miro.medium.com/v2/resize:fill:64:64/1*0xmi1m3lKtIdhh3vz8hFsA.jpeg)](https://hettt.medium.com/?source=post_page---byline--d82e6591a63a---------------------------------------)

[Het Patel](https://hettt.medium.com/?source=post_page---byline--d82e6591a63a---------------------------------------)

5 min read

·

Jul 19, 2025

--

5

Listen

Share

Press enter or click to view image in full size

![]()

📌 **Special thanks to**

[**Shah kaif**](https://medium.com/u/10f677056bcd?source=post_page---user_mention--d82e6591a63a---------------------------------------)

 **—** my dedicated learning partner — for collaborating on this research and finding.

![]()

During a recent security assessment of **redacted.ai**, a virtual assistance platform that connects clients with remote talent including engineers, mentors, and co-founders, I uncovered several critical vulnerabilities that could compromise user accounts, financial data, and platform integrity.

> ⚠️ This post is for **educational purposes only**. I follow responsible disclosure. The name `redacted.ai` replaces the real domain for confidentiality.

## 🧠 What’s redacted.ai?

`redacted.ai` is an AI-based job-matching platform that:

* Lets users sign up using email, Verify their account using Digilocker services for KYC,
* Rewards actions with wallet coins,
* Provided Virtual assistance and Job matching,
* Helped with Mock interviews,

Also they were hiring for Remote Cybersecurity Specialist, and that was the main reason I had visited the site. Everything seemed to be perfect.

![]()

Simple idea. Good UX.
 — But one weekend, I got curious and poked around.

Let’s just say… **things fell apart fast.**

## Vulnerabilities at a Glance

Press enter or click to view image in full size

![]()

## 1️⃣ OTP? Nah, Who Needs That!

![]()

redacted.ai used **4-digit OTPs** for login and forgot-password flows — with **no rate limiting**, no CAPTCHA, and **no timeouts**.

I could easily bruteforce OTPs as they were only of 4 digits and Rate limits were not enforced.

### **Screenshot of The Attack:**

Press enter or click to view image in full size

![]()

**This confirmed Pre-Account Takeover + Account Takeover of any user using forgot-otp feature.**

📉 **Impact**:

* Any user account can be hijacked.
* OTP system is meaningless.
* Attacker doesn’t need the password, just the email address.

## 2️⃣ Business Logic Flaw — Wallet Be Like “Make It Rain 💸”

![]()

After creating a new account, I explored the “Wallet” feature. A popup appeared allowing me to request an amount — in **dollars** — despite my wallet balance being exactly **$0**. 🫠

Press enter or click to view image in full size

![]()

I sent request of some dollars and naturally, I intercepted the request using **Burp Suite**. When I sent a payment request for some random amount, the response was:

![]()

```
{
  "error':"Insufficient wallet balance for this request."
}
```

Here, I changed the 400 Bad Request to 200 OK and removed the body of request and forwarded the request. To my surprise, The frontend accepted this and sent:

![]()

```
{
  "userId':"6872b......",
  "amount":1000000,
  "type":"debited"
}
```

Here, All I had to do is changed the “type” → “debited” to “credited”.

So, Here’s what I did,

```
{
  "userId':"6872b......",
  "amount":10000000000......,
  "type":"credited"
}
```

And this is what I got:

![]()

And the frontend:

Press enter or click to view image in full size

![]()

### 💡 Why This Is Critical:

* **No server-side validation** for wallet transactions.
* **Trusting frontend logic** for financial operations is a **massive red flag**.
* I was able to **manipulate the wallet balance** to any amount without any authentication or verification.

### 🛡️ Impact:

* Unauthorized wallet crediting
* Leads to potential purchase abuse, gift card fraud, or platform exploitation
* Possible **financial loss** to the platform

## **3️⃣ Stored XSS in Resume Upload (PDF) and SVG Upload**

![]()

The platform allowed users to upload their **resumes as PDFs** and **profile pictures as SVGs** — both of which were vulnerable to **Stored Cross-Site Scripting (XSS)**.

### **PDF Upload: Stored XSS 🪓**

I crafted a malicious PDF file containing JavaScript payloads and uploaded it via the resume upload section. When any admin or HR opened this document **in-browser**, the JavaScript executed silently in their context.

This led to **persistent XSS**, as the PDF was stored and retrievable via a direct link — no sanitization or validation of file contents!

### **SVG Upload: Stored XSS Again!** 🧠

All I had to do is update :

```
filename="example2.jpg" --> "example2.svg"
Content-Type: image/jpeg --> image/svg+xml

Remove the jpeg content and replace it by js script.
```

![]()

SVG images are actually **XML files** — and JavaScript can be embedded directly in them. I uploaded an SVG with the following payload:

```
<svg xmlns="http://www.w3.org/2000/svg">
  <script>alert('Hello from SVG script');</script>
</svg>
```

**Boom!** ⚠️ Whenever someone visited the profile or page rendering this SVG, the script fired.

Press enter or click to view image in full size

![]()

## 5️⃣ Mobile Number Verification Bypass

![]()

While updating the profile, the platform sends an OTP to verify the mobile number. However, this mechanism was flawed due to **poor frontend-side validation and lack of backend enforcement**.

I entered invalid mobile number and requested for OTP.

![]()

And also did provided false OTP. As expected the response was:

![]()

**SAME!!!** Again I tried changing bad request to → 200 OK and changed the body content to:

```
{
  "success":true,
  "error":"Invalid...."
}
```

And this fired an another POST request at an /api/update-user-data:

![]()

Press enter or click to view image in full size

![]()

And that returned with:

![]()

## About the Authors:

![]()

* [**He...
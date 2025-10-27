---
title: The $1000 Critical Bug: Unauthorised Access Leading to Support Admin Panel Takeover
url: https://infosecwriteups.com/the-1000-critical-bug-unauthorised-access-leading-to-support-admin-panel-takeover-572d687566cd?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-14
fetch_date: 2025-10-02T20:08:57.177330
---

# The $1000 Critical Bug: Unauthorised Access Leading to Support Admin Panel Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F572d687566cd&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-1000-critical-bug-unauthorised-access-leading-to-support-admin-panel-takeover-572d687566cd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-1000-critical-bug-unauthorised-access-leading-to-support-admin-panel-takeover-572d687566cd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-572d687566cd---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-572d687566cd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# The $1000 Critical Bug: Unauthorised Access Leading to Support Admin Panel Takeover

[![V3D](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*iktULMfPmum8bAIj)](https://v3d.medium.com/?source=post_page---byline--572d687566cd---------------------------------------)

[V3D](https://v3d.medium.com/?source=post_page---byline--572d687566cd---------------------------------------)

3 min read

·

Sep 12, 2025

--

Listen

Share

Hello Hackers, Ram Ram Bhyi Sarya Ne

Hope you’re doing great. This is V3D, and I’m sharing a quick write-up with my friend [Gaurav](https://x.com/Zero2Infinity_) Gajre on one of our recent findings, an “Unauthorised Access Leading to Support Admin Panel Takeover.”

> **Note**: This was on a private Bug Bounty Program, so I can’t reveal the actual program name. Let’s just call it REDACTED.COM.

Without any further ado… let’s buckle up.

Buckle Up

**Initial Discovery**

While hunting on target.com, we stumbled upon **REDACTED.COM**. At first, we assumed it was a subsidiary or asset of target.com. To be sure, we reached out to their security team. They confirmed it wasn’t part of their scope but advised us to report the issue, saying they’d pass it along to the right team.

We then received a response from the parent company of **REDACTED.COM**:

> “Regarding your request related to bug bounty on <https://www.redacted.com>, please read the policies on <https://parentcompany.com/security-policies/> and submit the report to us (security@parentcompany.com
> ) to be eligible under the company’s bug bounty program. We’ll assess the report and get back to you accordingly.”

After reviewing their bounty policy, we began testing REDACTED.COM.

**Registration Flow**

The platform’s registration was based on a mobile number. While analyzing the signup request, we noticed two interesting parameters:

```
_token=ALPHANUMERIC-VALUE&userType=0&Mobile=9999999999&h_otp=1&0tp=877430&Name=asdfg&Email=v3d%40wearehackerone.com&PinCode=111111&Date0fBirth=01%2F01%2F2000&referralCode=&termCondition=2&UtmTerm=&UtmMedium=&UtmCampaign=&proengsoft_jsvalidation=&_jsvalidation=termCondition&_jsvalidation_validate_all=false
```

The two key parameters were:

1. userType=0

2. jsvalidation\_validate\_all=false

We tampered with the request:

Changed userType=0 → userType=1

Changed jsvalidation\_validate\_all=false → jsvalidation\_validate\_all=true

Upon forwarding this modified request, we received a 200 OK response. Shortly after, another similar request appeared with the parameter jsvalidation\_validate\_all=. Again, we set userType=1 and forwarded it. This time, the response was 302 Found, redirecting us to:

<https://www.redacted.com/partner-dashboard>

> **Here’s something important**: during our initial reproduction attempts, we missed the second request modification and couldn’t recreate the privileged account. We tried multiple times and failed until we carefully revisited the flow. Lesson learned — always check every request in the chain.

**Accessing the Dashboard**

Once logged in, the system asked for KYC documents. We uploaded dummy documents and proceeded. At first, the dashboard looked similar to a regular user account, but while exploring the options, we stumbled upon the support ticketing system.

And that’s where things got interesting.

Upon clicking My Tickets, we suddenly had access to **73,000+ support tickets** 🤯, including customer queries, PII, attached documents, and even the ability to reply on behalf of support staff.

Press enter or click to view image in full size

![]()

**Reporting**

It was around 4 A.M. when we found this. We immediately prepared a report and submitted it to the security team. By 10 A.M., we had sent them a full PoC with detailed reproduction steps.

The team responded quickly, fixed the issue within an hour, and asked us to retest. We confirmed the fix.

**Bounty Twist**

Afterwards, they said they’d get back with the bounty amount. Two days later, I asked for an update, and instead of telling me the reward, they directly requested my bank details. I asked them to first disclose the amount, but they ignored my request.

When I followed up again, they repeated the same thing. Something felt off.

Finally, I received the bounty mail:

Press enter or click to view image in full size

![]()

But here’s the twist, their policy clearly stated $3000–$5000 for Critical. When I confronted them, they claimed the old policy had been updated, and the new range was $500–$2000.

On checking, we realised they had backdated their updated policy (dated 10th Jan), while we reported the bug on 12th Jan when the old payout range was still live.

Despite multiple arguments over email and calls, they stood firm on $1000. In the end, we accepted it, though it was disappointing.

Hope you find this write-up helpful.

Hope you learned something new. If you like the write-up, give it a clap and follow me on [**X( Twitter)**](https://x.com/v3d_bug) and[**LinkedIn**](https://www.linkedin.com/in/ved-parkash-320602110/)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----572d687566cd---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----572d687566cd---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----572d687566cd---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----572d687566cd---------------------------------------)

[Hacker](https://medium.com/tag/hacker?source=post_page-----572d687566cd---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--572d687566cd---------------------------------------)

[![InfoSec Write-ups](https://miro.medium...
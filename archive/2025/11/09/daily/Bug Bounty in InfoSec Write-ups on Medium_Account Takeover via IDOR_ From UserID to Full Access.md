---
title: Account Takeover via IDOR: From UserID to Full Access
url: https://infosecwriteups.com/account-takeover-via-idor-from-userid-to-full-access-ade4f980cfb4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-11-09
fetch_date: 2025-11-10T03:17:41.625594
---

# Account Takeover via IDOR: From UserID to Full Access

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fade4f980cfb4&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccount-takeover-via-idor-from-userid-to-full-access-ade4f980cfb4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccount-takeover-via-idor-from-userid-to-full-access-ade4f980cfb4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ade4f980cfb4---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ade4f980cfb4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Account Takeover via IDOR: From UserID to Full Access

[![0xP0L73R63157](https://miro.medium.com/v2/resize:fill:64:64/1*CKPgLkAKP6ueNv0w01Nhrw.jpeg)](https://medium.com/%400xP0L73R63157?source=post_page---byline--ade4f980cfb4---------------------------------------)

[0xP0L73R63157](https://medium.com/%400xP0L73R63157?source=post_page---byline--ade4f980cfb4---------------------------------------)

4 min read

·

Oct 17, 2025

--

Listen

Share

Press enter or click to view image in full size

![]()

After discovering an unauthenticated endpoint leaking sensitive user data in the same application ([see my previous writeup here](https://medium.com/%400xP0L73R63157/how-i-found-an-unauthenticated-goldmine-of-pii-8f1fc93d8a0d)), I had a feeling there was more waiting beneath the surface. The app was behaving oddly, and I was still navigating it through an anonymous session.

While browsing the profile settings page, I noticed the input fields were blank. This was probably because no real user was associated with the session. Still, I decided to fill them out and observe what happened behind the scenes.

When I submitted the form and captured the request, something in the structure caught my attention. It was subtle but interesting enough to take a closer look.

### 1. The PII leak that started it all

Earlier in this same application, I discovered an unauthenticated endpoint that exposed detailed user information. By manipulating a `factoryId` parameter, I was able to enumerate users across different tenants and retrieve sensitive fields like names, email addresses, phone numbers, and admin flags; all without authentication:

Press enter or click to view image in full size

![]()

That vulnerability had already raised concerns, but the user data I found there ended up playing a key role in this second discovery.

### 2. Finding the entry point

After revisiting the data I had uncovered earlier, I decided to go back into the application and interact with as many features as I could. I clicked through every visible option, trying to understand what kind of functionality was available inside the anonymous session.

That’s when I found the profile settings page.

At first, the page looked empty. All of the input fields were blank, with no user data filled in. Still, I was curious. I filled in every field with dummy values and submitted the form while intercepting the request. What came through in Burp caught my attention.

![]()

**Note:** This screenshot was captured in a local testing environment that replicates the original application’s behavior. The vulnerability demonstrated here behaves the same way as it did on the actual target.

### 3. Exploitation

After submitting the form and intercepting the request in Burp Suite, I took a closer look:

Press enter or click to view image in full size

![]()

I replaced the default user ID in both the query parameter (`id`) and the request body (`User.Id`) with the ID of a real user I had previously identified during the PII enumeration.

I left everything else the same and changed only one field: the email address.

When I forwarded the request, the server responded with a `302 Found` status and redirected me to `/users/u001`:

Press enter or click to view image in full size

![]()

That path itself redirected again back to the blank profile settings page, just like before. Nothing in the UI indicated whether the update had worked.

### 4. Proving the vulnerability

After submitting the modified request, I wanted to confirm whether the change had any real impact beyond the user interface. Specifically, I was interested in seeing if the updated email address was being used by the application in account-related workflows.

I found a password reset feature on the login page and entered the new email address I had used during testing: `pwned@example.com`. Shortly after, I received a password reset email containing a working reset link.

![]()

This confirmed that the application had successfully updated the user’s email and was relying on that field for account recovery. In a real-world scenario, this would have allowed a malicious actor to take full control of another user’s account by triggering a password reset.

To avoid any disruption, I immediately used the same request format to revert the email address back to its original value. No further actions were taken.

This was enough to fully confirm the vulnerability and demonstrate its severity without causing any lasting impact.

### 5. Reporting

After verifying the impact and restoring the affected data, I submitted a detailed report to the program. I included full reproduction steps, the modified request, and the confirmation via the password reset flow.

The response was quick and professional. The issue was acknowledged, reproduced, and triaged shortly after submission.

The vulnerability was assessed as critical due to its potential to allow full account takeover without authentication.

> It only takes one forgotten check to open the door completely.

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----ade4f980cfb4---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----ade4f980cfb4---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----ade4f980cfb4---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----ade4f980cfb4---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----ade4f980cfb4---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ade4f980cfb4---------------------------------------)

[![InfoSec Write-up...
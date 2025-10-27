---
title: Checklist for Forgot Password functionality
url: https://infosecwriteups.com/checklist-for-forgot-password-functionality-3f61c34a15eb?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-02
fetch_date: 2025-10-06T17:42:39.650437
---

# Checklist for Forgot Password functionality

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F3f61c34a15eb&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fchecklist-for-forgot-password-functionality-3f61c34a15eb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fchecklist-for-forgot-password-functionality-3f61c34a15eb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40sup26)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-3f61c34a15eb---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-3f61c34a15eb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Checklist for Forgot Password functionality

[![Suprajabaskaran](https://miro.medium.com/v2/resize:fill:64:64/1*qv5PO65J3cFJJHpIoEa8EA.png)](https://medium.com/%40suprajabaskaran8?source=post_page---byline--3f61c34a15eb---------------------------------------)

[Suprajabaskaran](https://medium.com/%40suprajabaskaran8?source=post_page---byline--3f61c34a15eb---------------------------------------)

3 min read

·

Jun 26, 2024

--

Listen

Share

Hello hackers! It’s been a long time. Today, we will delve into a small curated checklist for Forgot password functionality. Security testing for a forgot password functionality is crucial to ensure that the system is robust against various threats.

Let’s quickly dive into the list :)

![]()

### 1. Input Validation Testing:

* ***Email enumeration:*** Check if the system leaks information about the registered and non-registered email addresses. This comes under user enumeration. If a user receives a different message for an invalid email, such as “Email not found” versus a valid email “Password reset email is sent”, it allows attackers to enumerate valid emails.
* ***SQL Injection and XSS:*** Test if the input fields are susceptible to SQL injection or XSS attacks by injecting scripts and observing the behavior

### 2. Brute Force Protection:

* ***Rate Limiting:*** Verify if there are protections against brute force attacks. The system should limit the number of attempts to request a password reset
* ***Automated requests:*** Ensure measures such as CAPTCHA verification are implemented to prevent automated requests.

### 3. Email Security:

* ***Email content***: Verify that the email content does not disclose any sensitive information and includes a secure link
* ***Email spoofing:*** Ensure the email sent by the system cannot be spoofed. Ensure the email is sent from a legitimate domain and that SPF, DKIM, and DMARC are properly configured.

### 4. Token Security:

* ***Token Expiry:*** Ensure that the password reset token has an expiry time and cannot be reused after it has expired.
* ***Secure Token Generation***: Use cryptographically secure tokens that are unique and difficult to guess. Avoid using predictable identifiers such as user IDs or email addresses directly in the reset link.
* ***Token Uniqueness***: Check that the tokens are unique and sufficiently random to prevent guessing.
* ***Token Scope:*** Verify that the token is tied to a specific user and cannot be used for other accounts.
* ***Check for IDOR vulnerabilities:*** Ensure that the password reset functionality is not vulnerable to IDOR attacks, where attackers might manipulate identifiers (e.g., user IDs, tokens) in the password reset link to gain unauthorized access to other users’ accounts.

### 5. Error Handling:

* ***Consistent Messaging***: Ensure that the system displays consistent messages for both valid and invalid email addresses to avoid email enumeration.
* ***Error Handling***: Verify that the application handles errors gracefully without disclosing stack traces or technical details.

### 6. Session Management:

* ***Invalidate Old Sessions***: Ensure that resetting the password invalidates all active sessions for the user to prevent unauthorized access with an old password.

Thanks for joining me on this journey through Forgot Password pentesting! I’ve poured my heart into crafting a personalized checklist, aiming to cover all bases. Your feedback means the world! Let’s dive in together and brainstorm more test cases or new elements to add. Together, we can support developers in creating secure systems.

Cheers to a community-driven effort for more secure development practices!

P.S> Let me know if you are interested in this checklist, I can create a GitHub repo with this checklist with an easy to use excel sheet for you all :)

If you have not checked out my other checklists, please visit them as well :)

[## Mastering API Penetration Testing: A Comprehensive Guide for Security Pentesters

### Understanding API Penetration Testing:

infosecwriteups.com](/mastering-api-penetration-testing-a-comprehensive-guide-for-security-pentesters-bf62f65b5b21?source=post_page-----3f61c34a15eb---------------------------------------)

[## Recon like a Pro!

### Hey there, fellow bug hunters and curious minds! Are you ready to dive into the fascinating world of reconnaissance?

infosecwriteups.com](/recon-like-a-pro-594845934fd0?source=post_page-----3f61c34a15eb---------------------------------------)

[## Testing vulnerabilities beyond traditional cases — around login/signup features

### Hey there, fellow hackers and bounty hunters! Today, we’re diving into some nifty techniques to poke around login…

infosecwriteups.com](/testing-vulnerabilities-beyond-traditional-cases-around-login-signup-features-9d496bd283d4?source=post_page-----3f61c34a15eb---------------------------------------)

[## Ways I followed to Bypass ‘403’ — Your checklist

### Hello people! Hope you all are doing well.

infosecwriteups.com](/ways-i-followed-to-bypass-403-your-checklist-fa3fc1256d2a?source=post_page-----3f61c34a15eb---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page-----3f61c34a15eb---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----3f61c34a15eb---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----3f61c34a15eb---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----3f61c34a15eb---------------------------------------)

[Passwords](https://medium.com/tag/passwords?source=post_page-----3f61c34a15eb---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---...
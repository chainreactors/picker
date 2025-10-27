---
title: STRIPE Live Key Exposed:: Bounty: $1000
url: https://infosecwriteups.com/stripe-live-key-exposed-bounty-1000-dc670f2c5d9c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-10
fetch_date: 2025-10-04T01:06:35.428808
---

# STRIPE Live Key Exposed:: Bounty: $1000

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdc670f2c5d9c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstripe-live-key-exposed-bounty-1000-dc670f2c5d9c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fstripe-live-key-exposed-bounty-1000-dc670f2c5d9c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-dc670f2c5d9c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-dc670f2c5d9c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# STRIPE Live Key Exposed:: Bounty: $1000

[![Vipul Sahu](https://miro.medium.com/v2/resize:fill:64:64/1*s81_1pBeT2o5kQ2pvZsB6Q.jpeg)](https://medium.com/%40vipul_sahu?source=post_page---byline--dc670f2c5d9c---------------------------------------)

[Vipul Sahu](https://medium.com/%40vipul_sahu?source=post_page---byline--dc670f2c5d9c---------------------------------------)

2 min read

·

Dec 9, 2022

--

Listen

Share

Hey Hunters,

I have found a sensitive stripe live token leaking on a private program.[let’s say redacted.com]

## Initial Foothold

I collected all the subdomains using tools like Subfinder and Amass. After that, I filtered the live subdomains using httprobe. Found a subdomain admin.redacted.com which redirects the user/admin to google OAuth.

Your browser can execute JavaScript, which can, in turn, change the document; in this case, it redirects to google OAuth. After this, I used curl for admin.redacted.com to get the plain original output and nothing else.

Press enter or click to view image in full size

![]()

Leaking stripe live token

Now I have a leaking stripe live token, but the token’s validity needs to be checked.

## Exploiting Stripe Tokens

After checking the [Keyhacks](https://github.com/streaak/keyhacks) and the [Stripe API Documentation](https://stripe.com/docs/api). I was able to get a bunch of information, including:

**Balance:** It retrieves the current balance in the Stripe account.

> curl <https://api.stripe.com/v1/balance> -u sk\_live\_<Secret-Key>:

Press enter or click to view image in full size

![]()

Balance in the Stripe Account

**Customers:** It retrieves the customer’s data and tracks payments. Including the Customer’s Name, Email, IP used, and many more.

> curl <https://api.stripe.com/v1/customers> -u sk\_live\_<Secret-Key>:

Press enter or click to view image in full size

![]()

Multiple customer’s data and upcoming payments

**Charges:** It retrieves charges and card information. One such card details are also attached below. Stripe only gives you the last four digits.

> curl <https://api.stripe.com/v1/charges> -u sk\_live\_<Secret-Key>:

![]()

Card Details

**Files:** Retrieves Files that the admin uploads. Files generally have invoices, disputes, events, balances, bank accounts, tokens, charges, and more.

> curl <https://api.stripe.com/v1/files> -u sk\_live\_<Secret-Key>:

Press enter or click to view image in full size

![]()

Files retrieved

## Impact and Timeline

Companies and other end users Sensitive Information Disclosure.

Reported — 21st August

Rewarded and Fixed — 30th August

**Let's connect:** <https://www.linkedin.com/in/vipul-sahu-a7a420174/>

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----dc670f2c5d9c---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----dc670f2c5d9c---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----dc670f2c5d9c---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----dc670f2c5d9c---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----dc670f2c5d9c---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dc670f2c5d9c---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dc670f2c5d9c---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--dc670f2c5d9c---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--dc670f2c5d9c---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--dc670f2c5d9c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Vipul Sahu](https://miro.medium.com/v2/resize:fill:96:96/1*s81_1pBeT2o5kQ2pvZsB6Q.jpeg)](https://medium.com/%40vipul_sahu?source=post_page---post_author_info--dc670f2c5d9c---------------------------------------)

[![Vipul Sahu](https://miro.medium.com/v2/resize:fill:128:128/1*s81_1pBeT2o5kQ2pvZsB6Q.jpeg)](https://medium.com/%40vipul_sahu?source=post_page---post_author_info--dc670f2c5d9c---------------------------------------)

[## Written by Vipul Sahu](https://medium.com/%40vipul_sahu?source=post_page---post_author_info--dc670f2c5d9c---------------------------------------)

[134 followers](https://medium.com/%40vipul_sahu/followers?source=post_page---post_author_info--dc670f2c5d9c---------------------------------------)

·[2 following](https://medium.com/%40vipul_sahu/following?source=post_page---post_author_info--dc670f2c5d9c---------------------------------------)

Penetration Tester | IITJ <https://x.com/GodSpeed000123>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----dc670f2c5d9c---------------------------------------)

[Status](https://status.medium.com/?source=post_...
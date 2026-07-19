---
title: 600$ For Stealing Podcasts/Show via RSS Feed Manipulation
url: https://infosecwriteups.com/600-for-stealing-podcasts-show-via-rss-feed-manipulation-f3f2cef08adf?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-18
fetch_date: 2026-07-19T05:01:50.532253
---

# 600$ For Stealing Podcasts/Show via RSS Feed Manipulation

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F600-for-stealing-podcasts-show-via-rss-feed-manipulation-f3f2cef08adf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F600-for-stealing-podcasts-show-via-rss-feed-manipulation-f3f2cef08adf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f3f2cef08adf---------------------------------------)

·

1. [The Logic](/?source=post_page-----f3f2cef08adf---------------------------------------#5dd7 "The Logic")
2. [The Bug](/?source=post_page-----f3f2cef08adf---------------------------------------#3bbd "The Bug")
3. [Steps to Reproduce](/?source=post_page-----f3f2cef08adf---------------------------------------#e484 "Steps to Reproduce")
4. [1. Pick a Target](/?source=post_page-----f3f2cef08adf---------------------------------------#a266 "1. Pick a Target")
5. [2. Manipulate the Feed](/?source=post_page-----f3f2cef08adf---------------------------------------#61c9 "2. Manipulate the Feed")
6. [3. Host the Malicious Feed](/?source=post_page-----f3f2cef08adf---------------------------------------#4943 "3. Host the Malicious Feed")
7. [4. Submit & Takeover](/?source=post_page-----f3f2cef08adf---------------------------------------#766e "4. Submit & Takeover")
8. [The Impact](/?source=post_page-----f3f2cef08adf---------------------------------------#a857 "The Impact")
9. [Remediation](/?source=post_page-----f3f2cef08adf---------------------------------------#6e5a "Remediation")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f3f2cef08adf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Bug Bounty

Bugs

Penetration Testing

Bug Bounty Tips

Bug Bounty Writeup

# 600$ For Stealing Podcasts/Show via RSS Feed Manipulation

[![Anas NadY](https://miro.medium.com/v2/resize:fill:64:64/1*7M9J9UNPG2jyrUAW_psYaw.jpeg)](https://medium.com/%40anas-nady?source=post_page---byline--f3f2cef08adf---------------------------------------)

[Anas NadY](https://medium.com/%40anas-nady?source=post_page---byline--f3f2cef08adf---------------------------------------)

3 min read

·

Jan 5, 2026

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Df3f2cef08adf&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2F600-for-stealing-podcasts-show-via-rss-feed-manipulation-f3f2cef08adf&source=---header_actions--f3f2cef08adf---------------------post_audio_button------------------)

Share

![]()

Press enter or click to view image in full size

![]()

Hello hunters! 👋

In this write-up, I will share a **Business Logic Flaw** I discovered in a major podcasting platform (`redacted.com`).

By manipulating a simple XML file (RSS Feed), I was able to bypass the ownership verification process and claim legitimate podcasts as my own. This allowed me to create duplicate entries and hijack the identity of famous podcasts on the platform.

Let’s get into the details! 🚀

## The Logic

The target platform allows creators to submit their podcasts using an **RSS Feed URL**. To verify that you own the podcast, the system reads the `<itunes:email>` tag inside the RSS file and sends a verification code to that email.

**The mechanism:**

1. User submits RSS URL (e.g., `mysite.com/feed.xml`).
2. System reads the XML
3. System extracts email from `<itunes:email>owner@example.com</itunes:email>`.
4. System sends a code to `owner@example.com`.

## The Bug

The system failed to fingerprint the **content** of the podcast to check for duplicates. It trusted *any* RSS feed as long as the email inside matched the submitter’s account.

## Get Anas NadY’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

This means if I download a famous podcast’s RSS feed, change the email inside it to **my email**, and host it on a public cloud storage, the system treats it as a **new, valid podcast** owned by me.

## Steps to Reproduce

Here is how I exploited this logic:

## 1. Pick a Target

I found a valid, already published podcast on `redacted.com`. I copied their legitimate RSS feed URL.

## 2. Manipulate the Feed

I downloaded the RSS XML file to my local machine. I opened it and modified two lines:

1. **Title:** Changed it slightly (to avoid exact name matches).
2. **Email:** Changed the `<itunes:email>` tag to **MY** email address (the one I used to sign up on the target site).

**The Payload (RSS XML):**

```
<channel>
    <title>HACKED PODCAST NAME</title>
    <itunes:email>attacker@gmail.com</itunes:email>
</channel>
```

## 3. Host the Malicious Feed

I uploaded this modified `.rss` file to a **Google Cloud Storage** bucket (or any public cloud storage) to get a valid URL. *URL Example:* `https://storage.googleapis.com/.../exploit.rss`

## 4. Submit & Takeover

* I went to `https://redacted.com/submitـrss`.
* I submitted my Google Cloud Storage URL.
* The system parsed the file, saw **my email** in the tag, and sent **me** the verification email.
* I clicked verify.

**Result:** The podcast was successfully added to my account! I now controlled a duplicate version of the victim's content on the main streaming platform.

## The Impact

This was a simple but effective Logic Bypass.

* **Impersonation:** Attackers can claim ownership of content they don't own.
* **Phishing/Spam:** Attackers can clone popular podcasts and inject their own descriptions or links.
* **Platform Confusion:** Listeners see duplicate versions of the same show.

## Remediation

The platform patched this by:

* Implementing stricter checks on RSS feed content (hashing content to find duplicates).
* Improving validation to detect if a feed is simply a re-hosted copy of an existing one.

Bug Bounty

Bugs

Penetration Testing

Bug Bounty Tips

Bug Bounty Writeup

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f3f2cef08adf---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f3f2cef08adf---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f3f2cef08adf---------------------------------------)

[87K followers](/followers?source=post_page---post_publication_info--f3f2cef08adf-------------------------------------...
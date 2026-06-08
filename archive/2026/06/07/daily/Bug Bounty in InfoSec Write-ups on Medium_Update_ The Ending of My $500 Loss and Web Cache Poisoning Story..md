---
title: Update: The Ending of My $500 Loss and Web Cache Poisoning Story.
url: https://infosecwriteups.com/update-the-ending-of-my-500-loss-and-web-cache-poisoning-story-153603be845a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-07
fetch_date: 2026-06-08T06:32:41.401787
---

# Update: The Ending of My $500 Loss and Web Cache Poisoning Story.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fupdate-the-ending-of-my-500-loss-and-web-cache-poisoning-story-153603be845a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fupdate-the-ending-of-my-500-loss-and-web-cache-poisoning-story-153603be845a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-153603be845a---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-153603be845a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Update: The Ending of My $500 Loss and Web Cache Poisoning Story.

[![kjulius](https://miro.medium.com/v2/resize:fill:64:64/1*pNjTItx95RQhfspL_MnSoA.jpeg)](https://kjulius.medium.com/?source=post_page---byline--153603be845a---------------------------------------)

[kjulius](https://kjulius.medium.com/?source=post_page---byline--153603be845a---------------------------------------)

3 min read

·

1 day ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D153603be845a&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fupdate-the-ending-of-my-500-loss-and-web-cache-poisoning-story-153603be845a&source=---header_actions--153603be845a---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

By kjulius

In my previous article, I published a story about how losing $500 unexpectedly led me back to a Web Cache Poisoning vulnerability that I had previously documented and forgotten about.

If you haven’t read the original story, you can find it here:
<https://medium.com/bugbountywriteup/when-bug-bounty-hunting-hit-me-back-how-losing-500-led-me-to-a-web-cache-poisoning-bug-36fb2f196b9a>

At the time of writing that article, there were still a lot of unanswered questions. The account remained active, the charge had already gone through, and I wasn’t sure how the situation would eventually end.

Well, here’s the update.

## The Account Was Eventually Deactivated.

Over the following weeks, I started receiving multiple payment reminder emails from the service.

The emails ranged from payment notifications to overdue invoice reminders and eventually account-blocking notices.

Press enter or click to view image in full size

![]()

Proof of Concept Image.

At first, I ignored them because I had already contacted both the company and my bank regarding the charge.

Then one day, I logged back into the account and noticed a message stating that the account had been temporarily deactivated due to unpaid invoices.

Shortly afterward, the service access was effectively disabled and the subscription was no longer active.

Press enter or click to view image in full size

![]()

Proof of Concept Image.

At that point, it became clear that the account would not remain active indefinitely.

## The Unexpected Refund.

The most surprising part came later.

A few days after the account was deactivated, the money that had been debited from my account was returned.

Since the day I noticed the original charge, I had immediately contacted my bank, cancelled the card, and requested a dispute/chargeback investigation.

Because of that, I believe the refund was most likely the result of the bank’s dispute process rather than a direct refund from the company.

I cannot say that with complete certainty, but the timing strongly suggests it.

Either way, seeing that notification was a huge relief.

Press enter or click to view image in full size

![]()

Proof of Concept Image.

## Looking Back.

When the entire situation started, I honestly thought the money was gone for good.

## Get kjulius’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

Instead, several things happened:

* The account was eventually deactivated.
* The subscription was cancelled.
* The disputed funds were returned.
* The cache poisoning bug I discovered turned out to be a duplicate.

Not exactly the ending I expected.

I didn’t receive a bounty.

I didn’t keep the subscription.

And I didn’t get a unique vulnerability report accepted.

But I did get my money back.

And sometimes that’s a win on its own.

## Final Thoughts.

One thing bug bounty hunting teaches you very quickly is that not every story ends with a payout.

Sometimes you find a valid bug and lose the race.

Sometimes you spend weeks investigating something that goes nowhere.

And sometimes life throws unexpected distractions right in the middle of a hunt.

What matters is continuing to learn and continuing to improve.

The duplicate report was disappointing.

The $500 charge was frustrating.

But the experience itself was valuable.

The hunt continues.

And as I’ve learned many times before:

> *As long as software continues to evolve, there will always be vulnerabilities waiting to be discovered.*

Never give up, till we meet again… 🙏

Web Cache Poisoning

Bug Bounty

Refund

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--153603be845a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--153603be845a---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--153603be845a---------------------------------------)

[87K followers](/followers?source=post_page---post_publication_info--153603be845a---------------------------------------)

·[Last published 2 hours ago](/oscp-windows-enumeration-checklist-my-complete-privilege-escalation-workflow-for-every-box-7f85ce678f40?source=post_page---post_publication_info--153603be845a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![kjulius](https://miro.medium.com/v2/resize:fill:96:96/1*pNjTItx95RQhfspL_MnSoA.jpeg)](https://kjulius.medium.com/?source=post_page---post_author_info--153603be845a---------------------------------------)

[![kjulius](https://miro.medium.com/v2/resize:fill:128:128/1*pNjTItx95RQh...
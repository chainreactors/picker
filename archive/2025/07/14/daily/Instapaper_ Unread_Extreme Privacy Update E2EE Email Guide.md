---
title: Extreme Privacy Update E2EE Email Guide
url: https://inteltechniques.com/blog/2025/07/12/extreme-privacy-update-e2ee-email-guide/
source: Instapaper: Unread
date: 2025-07-14
fetch_date: 2025-10-06T23:26:56.089352
---

# Extreme Privacy Update E2EE Email Guide

[Skip to content](#main)

[# IntelTechniques](https://inteltechniques.com)

[IntelTechniques Blog](https://inteltechniques.com/blog/)

* [Training](https://inteltechniques.com/training.html)
* [Services](https://inteltechniques.com/services.html)
* [Resources](https://inteltechniques.com/links.html)
* [Tools](https://inteltechniques.com/tools/)
* [Blog](https://inteltechniques.com/blog/)
* [Podcast](https://inteltechniques.com/podcast.html)
* [Magazine](https://unredactedmagazine.com)
* [Books](https://inteltechniques.com/books.html)
* [Contact](https://inteltechniques.com/contact.html)

# Extreme Privacy Update: E2EE Email Guide

* [Posted on
  July 12, 2025](https://inteltechniques.com/blog/2025/07/12/extreme-privacy-update-e2ee-email-guide/)
* Posted in
  [Privacy](https://inteltechniques.com/blog/category/privacy/), [Security](https://inteltechniques.com/blog/category/security/)

Email was never meant to be private or secure. The protocol was created decades ago, and was first used to share files and messages between groups of researchers. We have come a long way since then. Today, we rely on email to pay our bills, confirm our identities, and communicate globally. I believe there are currently only two private and secure email providers, and every reader of this blog should establish accounts with both. First, let's understand the reasons we should care about email privacy and security.

Traditional email providers can read all of your messages. While they typically encrypt the data while it is in transit from one provider to another, they hold the keys and there is no end-to-end encryption (E2EE) protecting your content. A malicious employee or criminal hacker can access the data, and a court order can force the provider to hand over everything you have ever said. For a long time, Gmail was scanning every message in order to present advertisements relevant to your conversation.

This is where providers such as [Proton Mail](https://go.getproton.me/aff_c?offer_id=7&aff_id=1519) and [Tuta](https://tuta.com/?t-src=inteltechniques) come in. These services, each offering free tiers, provide email communications with true zero-knowledge E2EE. This means that your email is encrypted from your device before it is stored on their servers. Even with a court order, an employee of Proton Mail or Tuta would be unable to view any message content. If an email is sent from one Proton Mail user to another Proton Mail user (or one Tuta user to another Tuta user), it is never exposed to interception from a third party. Is this bulletproof? No, nothing is. There will always be some slight chance that an adversary could compromise your communications. However, it is extremely unlikely. On the other side, a court order to Google, Yahoo, Microsoft, or any other traditional provider will hand over all of your account details and email communications stored with them without any resistance.

While I am not very concerned about court orders being executed on my accounts, I am extremely bothered by data breaches and internal abuses. If a breach occurs at [Proton Mail](https://go.getproton.me/aff_c?offer_id=7&aff_id=1519) or [Tuta](https://tuta.com/?t-src=inteltechniques), the thief gets a bunch of encrypted data that is of no use. In 2016, a large breach at Yahoo handed over access to over 500 million accounts to unknown criminal culprits. In 2021, Yandex caught an employee selling access to entire inboxes of targeted users. These scenarios are no longer theoretical. Verified threats toward your sensitive email content exist. A big part of being private is simply making better choices, even if they are not fool-proof.

I have a few opinions on email which may not be accepted by the security community. First, email is broken and outdated. I assume every email I write could be seen by someone else. I trust services such as [Proton Mail](https://go.getproton.me/aff_c?offer_id=7&aff_id=1519) and [Tuta](https://tuta.com/?t-src=inteltechniques) over any other mainstream provider because of the zero-knowledge environment. Even if they secretly had bad intentions, they could not access my data. Multiple independent third-party audits verify this protection. These audits carry more weight than online promises by the companies.

The bigger problem is on the other side of your messages. If you send a message from your Proton or Tuta account to a non-encrypted provider, then you lose most of the protection. Proton Mail and Tuta can only safeguard your information on their servers They cannot control what happens when you leave their ecosystem. However, You can have comfort knowing that your historical email archive is protected from prying eyes.

In the most recent edition of [Extreme Privacy](https://inteltechniques.com/book7.html), I recommended both Proton Mail and Tuta, but displayed slight favor for Proton Mail due to wider adoption. I still see more Proton Mail users contacting me than Tuta fans, but the numbers are closing in. Also, both companies have made several improvements to their platforms. Let's dive into the latest comparisons for a full picture of each provider, sorted by the features I find most vital.

**Email Security:** This is a tie. Both services still provide industry standard E2EE and possess proper password and 2FA protocols.

**Custom Domains:** This is also a tie. I explain in the book the importance of owning your own domains for email communication. I place custom domains within each provider. If one service were to fail, shut down, kick me out, or become compromised, I can simply forward my DNS records to the other provider with almost no downtime. I am in true control of my addresses.

**Adoption:** This will vary, but Proton generally wins. Only a year ago, 99% or my contacts using secure email were Proton Mail users. Therefore, it simply made more sense to primarily use Proton Mail for communications. As I write this, 29% of the people who have emailed me from a secure provider in the past year are using Tuta. The other 71% are using Proton. That is quite a jump. When I have a contact using Tuta, whether a Tuta address or a custom domain on Tuta, I always communicate with that person via my own Tuta account. This protects the entire conversation, and is the right thing to do. This is why I believe we should all have accounts at each provider, even if only on the free tier.

**Contacts:** Tuta has a slight edge on this one. Both Proton Mail and Tuta do NOT fully encrypt the email addresses of incoming and outgoing mail. They must see the addresses to be able to facilitate the communications. However, Tuta encrypts the subject line while Proton does not. Is this a huge deal? Not to me, but it may be to you. Both providers encrypt everything else stored within a contact on their service. Personally, I do not store my sensitive contacts within any online service. I keep them in my offline desktop and mobile applications.

**Calendars:** This is a tie. Both providers offer a true E2EE calendar experience, and both now offer the ability to share a calendar between multiple users.

**Offline Email Clients:** The winner on this one will depend on how you want to store your email. I believe everyone should have an offline backup of every email communication. What if your email provider gets hacked or disappears? What if you logged in one day and all of your email was gone? An offline copy prevents this concern. Proton Mail offers a bridge application which allows you to use any traditional email desktop application to synchronize your emails to your computer. If you want to use Thunderbird or any other IMAP option, then Proton is the winner. Tuta allows you to export messages in bulk, which could then be imported into your email program, but that is an ongoing hassle. However, Tuta users can download their desktop application and synchronize all email for offline use. Make sure you select "Email" and change the "local data" to "999999 days" to get everythi...
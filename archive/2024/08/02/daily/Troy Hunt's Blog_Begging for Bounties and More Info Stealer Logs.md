---
title: Begging for Bounties and More Info Stealer Logs
url: https://www.troyhunt.com/begging-for-bounties-and-more-info-stealer-logs/
source: Troy Hunt's Blog
date: 2024-08-02
fetch_date: 2025-10-06T18:05:28.995495
---

# Begging for Bounties and More Info Stealer Logs

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Begging for Bounties and More Info Stealer Logs

01 August 2024

**TL;DR — Tens of millions of credentials obtained from info stealer logs populated by malware were posted to Telegram channels last month and used to shake down companies for bug bounties under the misrepresentation the data originated from their service.**

How many attempted scams do you get each day? I woke up to yet another "redeem your points" SMS this morning, I'll probably receive a phone call from "my bank" today (edit: I was close, it was "Amazon Prime" 🤷‍♂️) and don't even get me started on my inbox. We're bombarded to the point of desensitisation, which itself is dangerous because it creates the risk of inadvertently dismissing something that really does require your attention. Which brings me to the email [Scott Helme](https://scotthelme.co.uk/?ref=troyhunt.com) from [Report URI](https://report-uri.com/?ref=troyhunt.com) (disclosure: [a service I've long partnered with and advised](https://report-uri.com/home/about?ref=troyhunt.com)) received yesterday titled "Bug bounty Program - PII leak Credentials more than 170". It began as follows:

> Through open-source intelligence gathering, I discovered a significant amount of **"**[**report-uri.com**](https://report-uri.com/?ref=troyhunt.com)**"**user credentials and sensitive documents have been leaked and are publicly accessible.

The sender then attached a text file with 197 lines of email addresses and passwords belonging to users of Scott's pride and joy. The first lines looked like this (url:email:password):

![](https://www.troyhunt.com/content/images/2024/07/image-6.png)

Imagine the heart-in-mouth moment he had when first seeing that; had someone compromised his service? Was this the data of his customers who had entrusted it to him and it was now floating around the internet? [*Isn't he the guy who's meant to be teaching others about application security?!*](https://www.troyhunt.com/im-teaming-up-with-scott-helme-to-run-hack-yourself-first-workshops-in-europe/) The email went on:

> The impact of this vulnerability is severe, potentially resulting in:
> Mass account takeovers by malicious actors.
> Exposure of sensitive user data including names, emails, addresses, and documents.
> Unauthorized transactions or malicious activities using compromised accounts.
> Further compromise of organizational infrastructure through account abuse.
> Financial and reputational damage due to security breaches.

Just to avoid any semblance of doubt as to the motive of the sender, the subject began by flagging the desire for a bug bounty (Report URI does not advertise a bounty program, but clearly a reward was being sought), followed by an email body stating it related to leaked Report URI credentials and then highlighted that "this vulnerability is severe". And then there's that last line about financial and reputation damage. It looked bad. However, cooler heads prevailed, and we started looking closer at the email addresses in the "breach" by checking them against [Have I Been Pwned](https://haveibeenpwned.com/?ref=troyhunt.com). Very quickly, a pattern emerged:

![](https://www.troyhunt.com/content/images/2024/07/image-2.png)![](https://www.troyhunt.com/content/images/2024/07/image-4.png)![](https://www.troyhunt.com/content/images/2024/07/image-3.png)

*Most* of the addresses we checked had appeared in [the lists posted to Telegram I'd loaded into HIBP a couple of months ago.](https://www.troyhunt.com/telegram-combolists-and-361m-email-addresses/) *These were stealer logs, not a breach of Report URI!* To validate that assertion, I pulled the original data source and parsed out every line containing "report-uri.com". Sure enough, the lines from the file sent to Scott were usually contained in the stealer log files. So, let's talk about how this works:

Take the URL you saw at the beginning of each line earlier on, the one being for [the registration page](https://report-uri.com/register?ref=troyhunt.com). Here's what it looks like:

![](https://www.troyhunt.com/content/images/2024/07/image-5.png)

Now, imagine you're filling out this form and your machine is infected with malware that can observe the data entered into each field. It takes that data, "steals" it and logs it at the attacker's server, hence the term "info stealer logs". There is absolutely nothing Scott can do to prevent this; the user's machine is compromised, *not* Report URI.

To illustrate the point, I grabbed the first email address in the file Scott was sent and pulled the rows *just for that address* rather than solely the Report URI rows. This would show us all the other services this person's credentials were snared from, and there were dozens. Here are just the first ten:

![](https://www.troyhunt.com/content/images/2024/07/image-7.png)

Google. Apple. Twitter. Most with the same password too, because a normal person obviously owns this email address. So, has each of these organisations also received a [beg bounty](https://www.troyhunt.com/beg-bounties/)? No, that's not a typo, this is classic behaviour where unsophisticated and self-proclaimed "security researchers" use automated tooling to identify largely benign security configurations that could be construed as vulnerabilities. For example, they'll send through a report that an [SPF record](https://www.mimecast.com/content/sender-policy-framework/?ref=troyhunt.com) is too permissive (they probably can't even spell "SPF", let alone understand the nuances of sender policies), then try to shake people like Scott down for money under the guise of a "bug bounty". This isn't Scott's problem, nor is it Google's or Apple's or Twitter's, it's something only the malware infected victim's can address.

In this post, I referred to "most" of the addresses already being in HIBP and the lines from the file he was sent "usually" occurring in the logs I had. But there were gaps. For example, whilst there were 197 rows in "his" file, I only found 161 in the data I'd previously loaded. But I had a hunch on how to fill that gap and make up the difference...

Two weeks ago, I was sent a further 22GB of stealer logs found in Telegram channels. Unlike the previous corpus of data, this set contained *only* stealer logs (no credential stuffing lists) and had a total of 26,105,473 unique email addresses. That's significant, as it implies that every single one of those addresses belongs to someone infected with malware that's stealing their creds. Of the total count, 89.7% had been seen in previous data breaches already in HIBP which is a high crossover, but it also meant that 2,679,550 addresses were all new. I'd been considering whether or not it made sense to load this data given corpuses such as this create frustration when people don't know which site their record was snared from nor which password was impacted. One particular frustration you'll read in comments on the previous post was that people weren't sure whether their email address was in a stealer log or a credential stuffing list; did they have a machine infected with malware or was it merely recycled credentials from an old data breach? But given the way in which this new corpus of data is being used (to attempt to scam Scott and, one would assume, many others), the 7-figure number of previously unseen addresses and the fact that this time, they can all emphatically be tied back to malware campaigns, this is now searchable in HIBP as "Stealer Logs Posted to Telegram".

Ultimately, this is just scam on top of scam: the victims in the logs have had their credentials scammed, and the person who emailed Scott attempted to use that to s...
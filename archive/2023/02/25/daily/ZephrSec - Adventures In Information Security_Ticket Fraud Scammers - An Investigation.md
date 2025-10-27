---
title: Ticket Fraud Scammers - An Investigation
url: https://blog.zsec.uk/an-investigation-into-ticketscams/
source: ZephrSec - Adventures In Information Security
date: 2023-02-25
fetch_date: 2025-10-04T08:06:35.757526
---

# Ticket Fraud Scammers - An Investigation

[![ZephrSec - Adventures In Information Security](https://blog.zsec.uk/content/images/2025/05/YoutubeHeader-Recovered-1.png)](https://blog.zsec.uk)

* [About Andy Gill/ZephrFish](https://blog.zsec.uk/about/)
* [Pre-register for my course](https://blog.zsec.uk/mae/)
* [My Books](https://leanpub.com/b/LearningTheRopes)
* [LTR101 Posts](https://blog.zsec.uk/tag/ltr101/)
* [Photo Blog](https://photos.zsec.uk/)
* [Pre-register for my course](https://blog.zsec.uk/mae/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

[project](/tag/project/)

# Ticket Fraud Scammers - An Investigation

If you're reading this, it's a blog post that's not my regular write-up but more of an investigation and a hypothesis on the anatomy of a scam. I also put it together to raise awareness for those who read my blog and who might not be overtly technical-focused.

* [![Andy Gill](/content/images/size/w100/2017/10/ZSIcon.png)](/author/andy/)

#### [Andy Gill](/author/andy/)

24 Feb 2023
• 4 min read

![Ticket Fraud Scammers - An Investigation](/content/images/size/w2000/2023/02/DSC00079--1-.jpg)

So recently, I came across someone selling tickets to various gigs and events; a friend also got scammed for money when they thought they were buying.  So it got me thinking, how deep does the rabbit hole go. If you're reading this, it's a blog post that's not my regular write-up but more of an investigation and a hypothesis on the anatomy of a scam. I also put it together to raise awareness for those who read my blog and who might not be overtly technical-focused.

## Hypothesis

With my mindset and naturally inquisitive of this kind of thing, I figured I'd dive a little deeper; my hypothesis of the scam is as follows:

The attacker either compromises a Ticketmaster account or associated Twitter(sometimes both), works out what tickets the person has then used a sock to sell the tickets or at least advertise them. To try to get money out of folks via Twitter DMs.

The ultimate aim is to extract money from the target using simple transactional social engineering and falsified proof.

## Setup

An example tweet from one of the many accounts doing this looks like so:

![](https://blog.zsec.uk/content/images/2023/02/image-8.png)

A fairly benign-looking tweet of someone advertising that they want to sell their tickets for a gig; in this case, it was Chris Brown, but I've seen examples of many different types, basically anything with a large demand on Twitter and usually based in the UK.

## Language Structure

Searching the language structure with structured search engine queries returned several accounts with similar operating methods. However, the accounts had been deleted or related tweets deleted. The screenshots below show some examples of the common phrase used:

```
I've got tickets for INSERT HERE can send via Ticketmaster; Kindly send a Dm if interested
```

![](https://blog.zsec.uk/content/images/2023/02/image-4.png)![](https://blog.zsec.uk/content/images/2023/02/image-3.png)![](https://blog.zsec.uk/content/images/2023/02/image-7.png)![](https://blog.zsec.uk/content/images/2023/02/image-9.png)![](https://blog.zsec.uk/content/images/2023/02/image-5.png)

## Making Conversation

Upon making contact with the adversary, some small talk about the tickets was undertaken to try and work out what they have, how much they want, and to get some proof out of them:

![](https://blog.zsec.uk/content/images/2023/02/image.png)

In this example, the tickets retailed for £80+, so selling for half price on the afternoon of a gig wasn't unheard of, but it still is a bit of a red flag. Anyway conversation continued, and they eventually dropped off. But I did notice that the user deleted their tweets daily and then re-advertising something else, essentially rinse and repeat.

## Proof Method

The adversary shows proof via a screen recording; here are two examples, in both videos, the same blurred background can be seen, and the method is to show the Twitter conversation and Gmail right next to each other to somehow prove that they have the tickets and are speaking to you:

![](https://blog.zsec.uk/content/images/2023/02/image-1.png)

Also note that while the blurred background is the same, the name in both examples is different, the first shows an email sent to a Dmytro. In contrast, the second is Nataliia, which plays into the suspected compromised accounts.

![](https://blog.zsec.uk/content/images/2023/02/image-2.png)

## IOCs/Historic Accounts/Etc

The IOCs or indicators of the accounts I've found so far have been the following Twitter handles and associated bank accounts/names. The adversary typically posts once or twice per account before deleting the account and relevant tweets.

#### Twitter Handles

Doing a bit of analysis, I've found the following handles to have been used historically; these are no longer active, and it may well be the same account just changing their handle or having different accounts each time:

* `mer_m_a`
* `be_a__ut__y` - Current active account hxxps://twitter[.]com/be\_a\_\_ut\_\_y
* `C__Mel_1`
* `_fan_of_myself`
* `O_l_e_k1`

#### Bank Details

On both occasions, I managed to get the adversary to send me bank details, both of which matched, the ACC no  has been partially obfuscated, but they were the same account on Revolut:

* Sort Code: `04-29-09`
* Account Number: `030301xx`
* Name on Account: `Dmytro Suranov`
* Bank: `Revolut`

The account might also have been compromised, so don't use the account as a specific IOC.

## Conclusion

It's a low-level scam, but realistically, this post is more to raise awareness, and hopefully, someone at either Ticketmaster, Revolut or Twitter can look into the accounts. This post is more to raise awareness and something that piqued my interest.

[![OmniProx: Multi-Cloud IP Rotation Made Simple](/content/images/size/w600/2025/09/Layered-Images-2.jpg)](/omniprox/)

[## OmniProx: Multi-Cloud IP Rotation Made Simple

TLDR: If you want to use the tool without reading the post here's the GitHub:
GitHub - ZephrFish/OmniProx: IP Rotation from different providers - Like FireProx but for GCP, Azure, Alibaba and CloudFlareIP Rotation from different providers - Like FireProx but for GCP, Azure, Alibaba and CloudFlare](/omniprox/)

28 Sep 2025
5 min read

[![pyLDAPGui - How It was Born](/content/images/size/w600/2025/09/image-1.png)](/pyldapgui/)

[## pyLDAPGui - How It was Born

pyLDAPGui is an app I've been playing about with for a few months but it wasn't until recently that I decided, probably a good idea to release it in a proof of concept form for people to play about. The concept came about while working on](/pyldapgui/)

15 Sep 2025
8 min read

[![AI Assisted Development - FAFO](/content/images/size/w600/2025/08/L1061670-2.jpg)](/ai-assisted-dev/)

[## AI Assisted Development - FAFO

Artificial Intelligence (AI) aka large language models (LLM) and generative AI development also referred to as vibecoding is the current buzzword and everyone wants to have some degree of AI integration with tooling and use-cases.
At its core a LLM is flawed and only as good as the data it](/ai-assisted-dev/)

23 Aug 2025
7 min read

[ZephrSec - Adventures In Information Security](https://blog.zsec.uk) © 2025

* [About Andy](https://blog.zsec.uk/about/)
* [Github](https://github.com/zephrfish)
* [Twitter](https://twitter.com/ZephrFish)
* [LinkedIn](https://www.linkedin.com/in/norecruiters/)
* [Photo Blog](https://photos.zsec.uk/)
* [Pre-register MAE](https://blog.zsec.uk/mae/)

[Powered by Ghost](https://ghost.org/)

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg)](https://www.digitalocean.com/?refcode=24ca2070f1f5&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
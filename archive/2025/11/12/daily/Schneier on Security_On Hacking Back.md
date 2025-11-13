---
title: On Hacking Back
url: https://www.schneier.com/blog/archives/2025/11/on-hacking-back.html
source: Schneier on Security
date: 2025-11-12
fetch_date: 2025-11-13T03:16:20.089236
---

# On Hacking Back

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## On Hacking Back

Former DoJ attorney John Carlin [writes](https://www.aspendigital.org/blog/so-you-want-to-hack-back/) about hackback, which he defines thus: “A hack back is a type of cyber response that incorporates a counterattack designed to proactively engage with, disable, or collect evidence about an attacker. Although hack backs can take on various forms, they are—­by definition­—not passive defensive measures.”

His conclusion:

> As the law currently stands, specific forms of purely defense measures are authorized so long as they affect only the victim’s system or data.
>
> At the other end of the spectrum, offensive measures that involve accessing or otherwise causing damage or loss to the hacker’s systems are likely prohibited, absent government oversight or authorization. And even then parties should proceed with caution in light of the heightened risks of misattribution, collateral damage, and retaliation.
>
> As for the broad range of other hack back tactics that fall in the middle of active defense and offensive measures, private parties should continue to engage in these tactics only with government oversight or authorization. These measures exist within a legal gray area and would likely benefit from amendments to the CFAA and CISA that clarify and carve out the parameters of authorization for specific self-defense measures. But in the absence of amendments or clarification on the scope of those laws, private actors can seek governmental authorization through an array of channels, whether they be partnering with law enforcement or seeking authorization to engage in more offensive tactics from the courts in connection with private litigation.

Tags: [hackback](https://www.schneier.com/tag/hackback/), [laws](https://www.schneier.com/tag/laws/)

[Posted on November 12, 2025 at 7:01 AM](https://www.schneier.com/blog/archives/2025/11/on-hacking-back.html) •
[6 Comments](https://www.schneier.com/blog/archives/2025/11/on-hacking-back.html#comments)

### Comments

Privacy •
[November 12, 2025 7:07 AM](https://www.schneier.com/blog/archives/2025/11/on-hacking-back.html/#comment-449822)

I hacked back exactly once, around 30 years ago. I noticed an invader in the network, launched a counterattack that knocked them off the Internet. It was of course symbolic, to let them know they had been noticed.

Clive Robinson •
[November 12, 2025 8:56 AM](https://www.schneier.com/blog/archives/2025/11/on-hacking-back.html/#comment-449826)

@ Bruce,

What happens when the US hacks to steal money?

Not even “hacking back” making them just like they accuse the NorKs and others in their “propaganda…

<https://www.theregister.com/2025/11/12/cverc_prince_grou_scam_bitcoin/>

At least it confirms the lies put out this century…

Ray Dillinger •
[November 12, 2025 3:59 PM](https://www.schneier.com/blog/archives/2025/11/on-hacking-back.html/#comment-449829)

I had never even considered the possibility that “hack backs” as he calls them might possibly ever be illegal.

Trace-and-hack-back has was one of my security SOPs for over 20 years. I could go through a list of tactics but given this article it seems that might be poor judgement. Still, it’s true. And I’m not doing security jobs any more so why not?

I’ve never been particularly destructive. I think the most aggressive thing I did in 20 years was breaking a botnet control node’s router. I found control input packets and couldn’t identify their source behind a Chinese VPN provider. But I could definitely identify the packet destination. I got into the router, verified that that machine’s routing requests had the rapid but steady timing and aggressively random destinations typical of botnet control, and then crashed the router. It needed reset and reconfigured to get working again, but wasn’t damaged.

At a security-conscious data center they’d probably never trust that router again, so I may have cost somebody some hardware. I doubt it because it probably wasn’t a security-conscious data center. It was probably just somebody who reset it and put it back on the line. If I did prompt someone to get rid of it, then good riddance. The CVE I used to break it was six years old at the time and their failure to have already thrown it out was enshittifying network security anyway.

(Side note: Most VPN’s are Chinese, and in China all businesses that use the Internet have to turn over logs to the CCP, decrypted in full, either on a regular basis or on request. Considering China’s adversarial behavior w/r/t information security in other countries and position in the supply-chain via hardware manufacture, realizing that they also have access to everything that goes through most VPN connections makes me worry.)

Kevin •
[November 12, 2025 6:25 PM](https://www.schneier.com/blog/archives/2025/11/on-hacking-back.html/#comment-449842)

The problem with hackback is collateral damage.

What if you ID’d the PC where the attack is coming from, and managed to shut that machine down. Soft kill right? No damage to anything.

But what if that machine was actually not ‘owned’ by the attacker, and simply a compromised middle man. What if that PC was inside a hospital, managing some crucial system? It had minimal security so the attacker got in and routed his attack through it. And you shut the crucial machine down. Now what’s the damage?

Star Chamber •
[November 12, 2025 8:24 PM](https://www.schneier.com/blog/archives/2025/11/on-hacking-back.html/#comment-449843)

@Ray Dillinger

Would you be willing to share why you assumed that they were legal?

For example: if someone breaks into your office and steals a box of documents (all on paper), can you follow him to his lair, enter without his permission, and re-take possession of your documents? How is this any different if the documents were stored electronically rather than on paper, and he hacked into your data storage system rather than physically broke into your office?

@Kevin

The answer to your question probably depends on whether you have permission to do anything to the compromised middle man’s systems. If the hospital doesn’t grant you access, you probably have no greater right to be there than the black hat hacker.

Jon (a different Jon) •
[November 12, 2025 10:00 PM](https://www.schneier.com/blog/archives/2025/11/on-hacking-back.html/#comment-449844)

Yep. @Kevin and at the OP, ‘misattribution’ is a colossal thing.

Spam email since day one has faked their return addresses, and even reverse paths. “Hacking Back” against an innocent bystander is, and should be, fantastically criminally liable.

So be very very careful about that.

J.

(For a literary reference, try Charlie Stross’s novel “Iron Sunrise”, wherein a specific stellar civilization attempts to wreck another and blame it on someone else – so the victim’s doomsday retaliation devices retaliate against someone else.) J.

[![Atom Feed](https://www.schneier.com/...
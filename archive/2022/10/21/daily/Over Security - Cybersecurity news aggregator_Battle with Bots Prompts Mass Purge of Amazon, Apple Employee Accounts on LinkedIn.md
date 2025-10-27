---
title: Battle with Bots Prompts Mass Purge of Amazon, Apple Employee Accounts on LinkedIn
url: https://krebsonsecurity.com/2022/10/battle-with-bots-prompts-mass-purge-of-amazon-apple-employee-accounts-on-linkedin/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-21
fetch_date: 2025-10-03T20:30:41.296030
---

# Battle with Bots Prompts Mass Purge of Amazon, Apple Employee Accounts on LinkedIn

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Battle with Bots Prompts Mass Purge of Amazon, Apple Employee Accounts on LinkedIn

October 20, 2022

[38 Comments](https://krebsonsecurity.com/2022/10/battle-with-bots-prompts-mass-purge-of-amazon-apple-employee-accounts-on-linkedin/#comments)

On October 10, 2022, there were 576,562 **LinkedIn** accounts that listed their current employer as **Apple Inc.** The next day, half of those profiles no longer existed. A similarly dramatic drop in the number of LinkedIn profiles claiming employment at **Amazon** comes as LinkedIn is struggling to combat a significant uptick in the creation of fake employee accounts that pair AI-generated profile photos with text lifted from legitimate users.

[Jay Pinho](https://www.linkedin.com/in/jaypinho/) is a developer who is working on a product that tracks company data, including hiring. Pinho has been using LinkedIn to monitor daily employee headcounts at several dozen large organizations, and last week he noticed that two of them had far fewer people claiming to work for them than they did just 24 hours previously.

Pinho’s screenshot below shows the daily count of employees as displayed on [Amazon’s LinkedIn homepage](https://www.linkedin.com/company/amazon/). Pinho said his scraper shows that the number of LinkedIn profiles claiming current roles at Amazon fell from roughly 1.25 million to 838,601 in just one day, a 33 percent drop:

![](https://krebsonsecurity.com/wp-content/uploads/2022/10/LI-Amazon.png)

As stated above, the number of LinkedIn profiles that claimed to work at Apple fell by approximately 50 percent on Oct. 10, according to Pinho’s analysis:

![](https://krebsonsecurity.com/wp-content/uploads/2022/10/LI-Apple.png)

Image: twitter.com/jaypinho

Neither Amazon or Apple responded to requests for comment. LinkedIn declined to answer questions about the account purges, saying only that the company is constantly working to keep the platform free of fake accounts. In June, LinkedIn [acknowledged it was seeing a rise in fraudulent activity](https://blog.linkedin.com/2022/june/16/working-together-to-keep-linkedin-safe) happening on the platform.

KrebsOnSecurity hired Menlo Park, Calif.-based **SignalHire** to check Pinho’s numbers. SignalHire keeps track of active and former profiles on LinkedIn, and during the Oct 9-11 timeframe SignalHire said it saw somewhat smaller but still unprecedented drops in active profiles tied to Amazon and Apple.

“The drop in the percentage of 7-10 percent [of all profiles], as it happened [during] this time, is not something that happened before,” SignalHire’s **Anastacia Brown** told KrebsOnSecurity.

Brown said the normal daily variation in profile numbers for these companies is plus or minus one percent.

“That’s definitely the first huge drop that happened throughout the time we’ve collected the profiles,” she said.

In late September 2022, KrebsOnSecurity warned about [the proliferation of fake LinkedIn profiles for Chief Information Security Officer (CISO) roles](https://krebsonsecurity.com/2022/09/fake-ciso-profiles-on-linkedin-target-fortune-500s/) at some of the world’s largest corporations. A [follow-up story on Oct. 5](https://krebsonsecurity.com/2022/10/glut-of-fake-linkedin-profiles-pits-hr-against-the-bots/) showed how the phony profile problem has affected virtually all executive roles at corporations, and how these fake profiles are creating an identity crisis for the businesses networking site and the companies that rely on it to hire and screen prospective employees.

A day after that second story ran, KrebsOnSecurity [heard from a recruiter](https://twitter.com/briankrebs/status/1578134158752227328) who noticed the number of LinkedIn profiles that claimed virtually any role in network security had dropped seven percent overnight. LinkedIn declined to comment about that earlier account purge, saying only that, “We’re constantly working at taking down fake accounts.”

![](https://krebsonsecurity.com/wp-content/uploads/2022/10/botgroup2.png)

A “swarm” of LinkedIn AI-generated bot accounts flagged by a LinkedIn group administrator recently.

It’s unclear whether LinkedIn is responsible for this latest account purge, or if individually affected companies are starting to take action on their own. The timing, however, argues for the former, as the account purges for Apple and Amazon employees tracked by Pinho appeared to happen within the same 24 hour period.

It’s also unclear who or what is behind the recent proliferation of fake executive profiles on LinkedIn. Cybersecurity firm **Mandiant** (recently acquired by **Google**) [told Bloomberg](https://www.yahoo.com/video/north-korean-fraudsters-suspected-copying-153907880.html) that hackers working for the North Korean government have been copying resumes and profiles from leading job listing platforms LinkedIn and **Indeed**, as part of an elaborate scheme to land jobs at cryptocurrency firms.

On this point, Pinho said he noticed an account purge in early September that targeted fake profiles tied to jobs at cryptocurrency exchange **Binance**. Up until Sept. 3, there were 7,846 profiles claiming current executive roles at Binance. The next day, that number stood at 6,102, a 23 percent drop (by [some accounts](https://twitter.com/cz_binance/status/1558894008893669378) that 6,102 head count is still wildly inflated).

![](https://krebsonsecurity.com/wp-content/uploads/2022/10/LI-Binance.png)

Fake profiles also may be tied to so-called [“pig butchering” scams](https://krebsonsecurity.com/2022/07/massive-losses-define-epidemic-of-pig-butchering/), wherein people are lured by flirtatious strangers online into investing in cryptocurrency trading platforms that eventually seize any funds when victims try to cash out.

In addition, identity thieves have been known [to masquerade on LinkedIn as job recruiters](https://krebsonsecurity.com/2021/05/how-to-tell-a-job-offer-from-an-id-theft-trap/), collecting personal and financial information from people who fall for employment scams.

**Nicholas Weaver**, a researcher for the [International Computer Science Institute](https://www.icsi.berkeley.edu/icsi/) at **University of California, Berkeley**, suggested another explanation for the recent glut of phony LinkedIn profiles: Someone may be setting up a mass network of accounts in order to more fully scrape profile information from the entire platform.

“Even with just a standard LinkedIn account, there’s a pretty good amount of profile information just in the default two-hop networks,” Weaver said. “We don’t know the purpose of these bots, but we know creating bots isn’t free and creating hundreds of thousands of bots would require a lot of resources.”

In response to last week’s story about the explosion of phony accounts on LinkedIn, the company said it was exploring new ways to protect members, such as expanding email domain verification. Under such a scheme, LinkedIn users would be able to publicly attest that their profile is accurate by verifying that they can respond to email at the domain associated with their current employer.

LinkedIn claims that its security systems detect and block approximately 96 percent of fake accounts. And despite the recent purges, L...
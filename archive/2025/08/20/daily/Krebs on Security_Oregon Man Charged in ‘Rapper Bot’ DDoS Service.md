---
title: Oregon Man Charged in ‘Rapper Bot’ DDoS Service
url: https://krebsonsecurity.com/2025/08/oregon-man-charged-in-rapper-bot-ddos-service/
source: Krebs on Security
date: 2025-08-20
fetch_date: 2025-10-07T00:50:51.931350
---

# Oregon Man Charged in ‘Rapper Bot’ DDoS Service

Advertisement

[![](/b-knowbe4/36.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

Advertisement

[![](/b-knowbe4/41.png)](https://gateway.on24.com/wcc/eh/1815783/human-risk-management-summit?partnerref=krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Oregon Man Charged in ‘Rapper Bot’ DDoS Service

August 19, 2025

[28 Comments](https://krebsonsecurity.com/2025/08/oregon-man-charged-in-rapper-bot-ddos-service/#comments)

A 22-year-old Oregon man has been arrested on suspicion of operating “**Rapper Bot**,” a massive botnet used to power a service for launching distributed denial-of-service (DDoS) attacks against targets — including a March 2025 DDoS that knocked Twitter/X offline. The Justice Department asserts the suspect and an unidentified co-conspirator rented out the botnet to online extortionists, and tried to stay off the radar of law enforcement by ensuring that their botnet was never pointed at KrebsOnSecurity.

![](https://krebsonsecurity.com/wp-content/uploads/2025/08/rapperbotpanel.png)

On August 6, 2025, federal agents arrested **Ethan J. Foltz** of Springfield, Ore. on suspicion of operating Rapper Bot, a globally dispersed collection of tens of thousands of hacked Internet of Things (IoT) devices.

The complaint against Foltz explains the attacks usually clocked in at more than two terabits of junk data per second (a terabit is one trillion bits of data), which is more than enough traffic to cause serious problems for all but the most well-defended targets. The government says Rapper Bot consistently launched attacks that were “hundreds of times larger than the expected capacity of a typical server located in a data center,” and that some of its biggest attacks exceeded six terabits per second.

Indeed, Rapper Bot was [reportedly responsible](https://cyberpress.org/rapperbot-exploits-dvrs-to-take-control-of-surveillance-cameras/) for the March 10, 2025 attack that caused intermittent outages on Twitter/X. The government says Rapper Bot’s most lucrative and frequent customers were involved in extorting online businesses — including numerous gambling operations based in China.

The criminal complaint was written by **Elliott Peterson**, an investigator with the **Defense Criminal Investigative Service** (DCIS), the criminal investigative division of the **Department of Defense** (DoD) Office of Inspector General. The complaint notes the DCIS got involved because several Internet addresses maintained by the DoD were the target of Rapper Bot attacks.

Peterson said he tracked Rapper Bot to Foltz after a subpoena to an ISP in Arizona that was hosting one of the botnet’s control servers showed the account was paid for via **PayPal**. More legal process to PayPal revealed Foltz’s **Gmail** account and previously used IP addresses. A subpoena to Google showed the defendant searched security blogs constantly for news about Rapper Bot, and for updates about competing DDoS-for-hire botnets.

According to the complaint, after having a search warrant served on his residence the defendant admitted to building and operating Rapper Bot, sharing the profits 50/50 with a person he claimed to know only by the hacker handle “**Slaykings**.” Foltz also shared with investigators the logs from his Telegram chats, wherein Foltz and Slaykings discussed how best to stay off the radar of law enforcement investigators while their competitors were getting busted.

Specifically, the two hackers chatted about [a May 20 attack against KrebsOnSecurity.com](https://krebsonsecurity.com/2025/05/krebsonsecurity-hit-with-near-record-6-3-tbps-ddos/) that clocked in at more than 6.3 terabits of data per second. The brief attack was notable because at the time it was the largest DDoS that Google had ever mitigated (KrebsOnSecurity sits behind the protection of **Project Shield**, a free DDoS defense service that **Google** provides to websites offering news, human rights, and election-related content).

The May 2025 DDoS was launched by an IoT botnet called **Aisuru**, which I discovered was operated by a 21-year-old man in Brazil named **Kaike Southier Leite**. This individual was more commonly known online as “**Forky**,” and Forky told me he wasn’t afraid of me or U.S. federal investigators. Nevertheless, the complaint against Foltz notes that Forky’s botnet seemed to diminish in size and firepower at the same time that Rapper Bot’s infection numbers were on the upswing.

“Both FOLTZ and Slaykings were very dismissive of attention seeking activities, the most extreme of which, in their view, was to launch DDoS attacks against the website of the prominent cyber security journalist Brian Krebs,” Peterson wrote in the criminal complaint.

“You see, they’ll get themselves [expletive],” Slaykings wrote in response to Foltz’s comments about Forky and Aisuru bringing too much heat on themselves.

“Prob cuz [redacted] hit krebs,” Foltz wrote in reply.

“Going against Krebs isn’t a good move,” Slaykings concurred. “It isn’t about being a [expletive] or afraid, you just get a lot of problems for zero money. Childish, but good. Let them die.”

“Ye, it’s good tho, they will die,” Foltz replied.

The government states that just prior to Foltz’s arrest, Rapper Bot had enslaved an estimated 65,000 devices globally. That may sound like a lot, but the complaint notes the defendants weren’t interested in making headlines for building the world’s largest or most powerful botnet.

Quite the contrary: The complaint asserts that the accused took care to maintain their botnet in a “Goldilocks” size — ensuring that “the number of devices afforded powerful attacks while still being manageable to control and, in the hopes of Foltz and his partners, small enough to not be detected.”

The complaint states that several days later, Foltz and Slaykings returned to discussing what that they expected to befall their rival group, with Slaykings stating, “Krebs is very revenge. He won’t stop until they are [expletive] to the bone.”

“Surprised they have any bots left,” Foltz answered.

“Krebs is not the one you want to have on your back. Not because he is scary or something, just because he will not give up UNTIL you are [expletive] [expletive]. Proved it with Mirai and many other cases.”

[Unknown expletives aside, that may well be the highest compliment I’ve ever been paid by a cybercriminal. I might even have part of that quote made into a t-shirt or mug or something. It’s also nice that they didn’t let any of their customers attack my site — if even only out of a paranoid sense of self-preservation.]

Foltz admitted to wiping the user and attack logs for the botnet approximately once a week, so investigators were unable to tally the total number of attacks, customers and targets of this vast crime machine. But the data that was still available showed that from April 2025 to early August, Rapper Bot conducted over 370,000 attacks, targeting 18,000 unique victims across 1,000 networks, with the bulk of victims residing in China, Japan, the United States, Ireland and Hong Kong (in that order).

According to the government, Rapper Bot borrows much of its code from **fBot**, a DDoS malware strain also known as **Satori**. In 2020, [authorities in Northern Ireland charged a then 20-year-old man](https://krebsonsecurity.com/2020/06/new-charges-sentencing-in-satori-iot-botnet-conspiracy/) named **Aaron “Vamp” Sterritt** with operating fBot with a co-conspirator. U.S. prosecutors are still seeking Sterritt’s extradition to the United States. fBot is itself a variation of the **Mira...
---
title: Corruption and Control: How Turkmenistan turned internet censorship into a business
url: https://blog.torproject.org/Corruption-Control-Turkmenistan-internet-censorship-business/
source: Tor Project blog
date: 2025-08-28
fetch_date: 2025-10-07T00:50:50.852331
---

# Corruption and Control: How Turkmenistan turned internet censorship into a business

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Corruption and Control: How Turkmenistan turned internet censorship into a business

by [gus, nina](/author/gus%2C%20nina)
| August 27, 2025

![](/Corruption-Control-Turkmenistan-internet-censorship-business/lead.png)

In July 2021, a sudden drop in Tor usage in Turkmenistan [called our attention](https://archive.is/5Kp4s). Tor would come to understand that this marked the beginning of a new era of censorship and restriction in this post-Soviet country. But let's rewind...

The Tor Community has long been defending internet freedom, running relays and [providing bridges to combat internet censorship](https://blog.torproject.org/2024-defend-internet-freedom-during-elections/).

Over the years, the Tor Project has called for action to [run more bridges](https://forum.torproject.org/t/tor-relays-help-turkmens-to-bypass-internet-censorship-run-an-obfs4-bridge/7002), Snowflake proxies, while we've investigated and adapted our anti-censorship strategies, and shared information about online censorship in Turkmenistan.

Modern censorship circumvention systems are generally built around the concept of ["collateral damage"](https://www.bamsoftware.com/papers/fronting/), where a censor cannot block access without blocking the entire internet or popular online services. However, in Turkmenistan, the censors' behavior has been strikingly different. They have openly blocked vast parts of the internet without concern for the collateral consequences, sparking curiosity: why do Turkmenistan's censors seem unbothered by the collateral damage their actions cause?

### Turkmenistan in context

Turkmenistan is ruled by the autocratic Berdimuhamedov family. The country consistently ranks at the bottom of global freedom and transparency indexes. In the 2025 Reporters Without Borders (RSF) Press Freedom Index, Turkmenistan placed [174th out of 180](https://rsf.org/en/country/turkmenistan). [Freedom House](https://freedomhouse.org/country/turkmenistan) gives the country a 1/100 rating for overall freedom. The capital, Ashgabat - often called the "White Marble City" - is both a showcase of authoritarian extravagance and a place where [citizens depends on circumvention tools to bypass censorship](https://theurbanactivist.com/governance/protecting-internet-freedom-in-the-city-of-white-marble/).

With an official population of about 6 million citizens, or - according to [some estimates](https://www.rferl.org/a/turkmenistan-population-decline-exodus/31355045.html) - less than 3 million, it is clear that millions left the country over the last decade. Main destinations are countries like Turkey and Russia, but [other countries too](https://eurasianet.org/turkmen-labor-migrants-turning-elsewhere-as-turkey-is-less-welcoming). To reduce the exodus, the Turkmen government asked Turkey to implement visas for Turkmen citizens (the request was fulfilled).

In Turkmenistan, the **corruption is systemic.** It's been the focus of several [investigative reportings](https://www.occrp.org/en/investigation/how-a-51-million-state-built-beauty-clinic-in-turkmenistan-ended-up-in-the-hands-of-the-presidents-family-at-a-massive-discount) and documentaries, like [The Shadow of the Holy Book](https://archive.org/details/shadow-of-the-holy-book-19353633-163997017). Internet penetration remains among the lowest in the world and also one of the [slowest internet in the world](https://bestbroadbanddeals.co.uk/broadband/speed/worldwide-speed-league/#speed).

Human rights violations are systematic with forced labour (including child labour) in [the cotton fields](https://www.cottoncampaign.org/turkmenistan). Women are an especially vulnerable group with lower salaries, [enforced dress code](https://www.rferl.org/a/turkmenistan-color-clothing-women-rules-repression/33349460.html), and informal restrictions like ban on beauty procedures or extreme difficulties in [obtaining a driver's license](https://turkmen.news/vlasti-turkmenistana-obyasnili-pochemu-ne-vydavali-voditelskie-prava-zhenshchinam/).

A very small number of activists are ready to talk about what is happening in the country. Even if they leave the country, they still face the risk of being sent back to Turkmenistan, like in the case of [bloggers Alisher Sahtov and Abdulla Orusov](https://www.hrw.org/news/2025/07/30/turkiye-turkmen-risking-deportation-reported-missing) who lived in Turkey and it seems was [deported to Turkmenistan](https://turkmen.news/istochnik-blogerov-sahatova-i-orusova-estradirovali-v-turkmenistan/) this year.

Many Turkmenistan citizens do not dare to speak openly, fearing for the lives and well-being of their loved ones who still live in Turkmenistan. Methods used inside the country can be seen with the example of 75-years old journalist Soltan Achilova. She was planning to travel to Switzerland to get a Martin Ennals award for human rights defenders. To prevent that, Turkmen authorities tried to [poison her](https://rsf.org/en/turkmenistan-rsf-denounces-poisoning-attempt-soltan-achilova) and when the attempt failed she was [forcibly hospitalized](https://cpj.org/2024/11/turkmen-journalist-soltan-achilova-forcibly-hospitalized-prevented-from-traveling-abroad/).

While millions of Turkmenistan citizens live abroad, their government does everything to cut the family ties of the country's residents with the diaspora: and severe online censorship is one of their tools.

### Online censorship and the war against the Internet

Since its beginning, the Internet in Turkmenistan has always been restricted and censored. The entire telecommunications sector of the country either belongs to the state itself or to people affiliated with the ruling family. Although the former president has passed [a law banning press censorship in 2013](https://cpj.org/2013/02/turkmenistan-opens-up-media-in-name-only/), the law exists only on paper. In practice, nearly all social media websites and messaging apps are blocked. Popular services like YouTube, Facebook, Instagram, WhatsApp, TikTok, Discord, Signal, [IMO](https://www.rferl.org/a/turkmenistan-last-messaging-app-internet/32535618.html), and Telegram are blocked in the country. It was reported by Progres Foundation that this Internet shutdown has potentially costed [8% of Turkmenistan's annual GDP](https://progres.online/reports/internet-freedom/what-does-internet-shutdown-cost-the-turkmen-economy).

In 2021, citizens were literally forced to [swear on the Koran that they wouldn't use VPNs](https://www.rferl.org/a/turkmenistan-vpn-koran-ban/31402718.html). If caught, a fine for using a VPN is 1,500 manats ($80 at the market exchange rate). This is around an average monthly salary. Yet for years, there's been no official list of banned sites.

Measuring online censorship from inside Turkmenistan is nearly impossible due to the extent and scale of their blocking, but sporadic test results appear on [OONI Explorer](https://explorer.ooni.org/chart/mat?probe_cc=TM&test_name=web_connectivity&since=2024-07-23&until=2025-07-24&axis_x=measurement_start_day&time_grain=day). In 2022, a [team of researchers](https://tmc.np-tokumei.net/) managed to map the regime's censorship using [a novel measurement technique](https://arxiv.org/pdf/2304.04835) that didn't rely on local testing or vantage points. Their finding revelead over 183,000 blocking rules and [more than 122,000 domains censored](https://advox.globalvoices.org/2023/04/12/new-study-finds-internet-censorship-in-turkmenistan-reaches-over-122000-domains/).

### The Internet censorship business in Turkmenistan

The truth came out from an investigative piece by [Turkmen.news](https://en.turkmen.news/news/internet-access-a-money-spinner-for-turkmenistan-s-cyber-security-service...
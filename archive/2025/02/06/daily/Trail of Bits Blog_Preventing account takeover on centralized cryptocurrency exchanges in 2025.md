---
title: Preventing account takeover on centralized cryptocurrency exchanges in 2025
url: https://blog.trailofbits.com/2025/02/05/preventing-account-takeover-on-centralized-cryptocurrency-exchanges-in-2025/
source: Trail of Bits Blog
date: 2025-02-06
fetch_date: 2025-10-06T20:35:17.270549
---

# Preventing account takeover on centralized cryptocurrency exchanges in 2025

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Preventing account takeover on centralized cryptocurrency exchanges in 2025

Evan Sultanik, Kelly Kaoudis

February 05, 2025

[blockchain](/categories/blockchain/), [research-practice](/categories/research-practice/)

This blog post highlights key points from our new white paper [*Preventing Account Takeovers on Centralized Cryptocurrency Exchanges*](https://resources.trailofbits.com/hubfs/Resources/trailofbits-20250205-account-takeover-recommended-practices.pdf), which documents ATO-related attack vectors and defenses tailored to CEXes.

Imagine trying to log in to your centralized cryptocurrency exchange (CEX) account and your password and username just… don’t work. You try them again. Same problem. Your heart rate increases a little bit at this point, especially since you are using a password manager. Maybe a service outage is all that’s responsible (knock on wood), and your password will work again as soon as it’s fixed? But it is becoming increasingly likely that you’re the victim of an account takeover (ATO).

CEXes’ choices dictate how (or if) the people who use them can secure their funds. Since account security features vary between platforms and are not always documented, the user might not know what to expect nor how to configure their account best for their personal threat model. Design choices like not supporting [phishing-resistant](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf) multifactor authentication ([MFA](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314/section-314.4#:~:text=Implement%20multi%2Dfactor%20authentication%20for%20any%20individual%20accessing%20any%20information%20system)) methods like [U2F hardware security keys](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html#:~:text=In%20fact%2C%20zero%20users%20that%20exclusively%20use%20security%20keys%20fell%20victim%20to%20targeted%20phishing%20during%20our%20investigation.), or not tracking user events in order to push in-app “[was this you?](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html#:~:text=Here%E2%80%99s%20how%20it%20works%3A%20if%20we%20detect%20a%20suspicious%20sign%2Din%20attempt%20(say%2C%20from%20a%20new%20location%20or%20device)%2C%20we%E2%80%99ll%20ask%20for%20additional%20proof%20that%20it%E2%80%99s%20really%20you.%20This%20proof%20might%20be%20confirming%20you%20have%20access%20to%20a%20trusted%20phone%20or%20answering%20a%20question%20where%20only%20you%20know%20the%20correct%20response.)” account lockdown prompts when anomalies happen invite the attacker in.

Our white paper’s goal is to inform and enable CEXes to provide a [secure-by-design](https://www.cisa.gov/sites/default/files/2023-10/SecureByDesign_1025_508c.pdf) platform for their users. Executives can get a high-level overview of the vulnerabilities and entities involved in user account takeover. We recommend a set of overlapping security controls that they can bring to team leads and technical product managers to check for and prioritize if not yet implemented. Security engineers and software engineers can also use our work as a reference for the risks of not integrating, maintaining, and documenting appropriate ATO mitigations.

### Account takeover

When the topic of fraud involving crypto comes up, our minds might jump to [the FTX collapse](https://apnews.com/article/sam-bankman-fried-ftx-cryptocurrency-sentencing-sbf-d7bb1a5e94b4c22039d74dfeab1a2ff1#:~:text=Prosecutors%20said%20tens,and%20live%20lavishly.), [blackmail scams](https://www.cbsnews.com/minnesota/news/home-image-email-extortion-scam/), [romance scams](https://darknetdiaries.com/transcript/141/#:~:text=She%20was%20the%20victim%20of%20a%20scam%20known%20as%20pig%20butchering.%20A%20scammer%20pretends%20to%20be%20looking%20for%20love%20online.%20They%20find%20a%20love%20interest%2C%20casually%20encourage%20them%20to%20invent%20in%20crypto%20via%20a%20fake%20app%2C%20but%20eventually%20they%20can%E2%80%99t%20access%20the%20money%20at%20all.%20The%20money%20is%20gone.%20The%20investments%3F%20Not%20real.), or maybe to [social media posts](https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2022/06/reports-show-scammers-cashing-crypto-craze#:~:text=Nearly%20half%20the%20people%20who%20reported%20losing%20crypto%20to%20a%20scam%20since%202021%20said%20it%20started%20with%20an%20ad%2C%20post%2C%20or%20message%20on%20a%20social%20media%20platform.) advertising “[investment opportunities](https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/watch_out_for_digital_fraud.html#:~:text=In%20some%20cases%2C%20the%20fraudsters%20claim%20to%20invest%20customers%E2%80%99%20funds%20in%20proprietary%20crypto%20trading%20systems%20or%20in%20%E2%80%9Cmining%E2%80%9D%20farms).” ATO is another common type of fraud that happens due to security failures, even though [financial institutions](https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know#Financial_institution) like CEXes that serve US customers must protect their users’ information from (among other harms) [unauthorized access](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314#:~:text=Protect%20against%20unauthorized%20access%20to%20or%20use%20of%20such%20information%20that%20could%20result%20in%20substantial%20harm%20or%20inconvenience%20to%20any%20customer.).

In an ATO, the attacker obtains access to someone else’s account, then locks the rightful account owner out by changing the access credentials. In 2023, the Sift Q3 Digital Trust and Safety Index disclosed an [808% year-over-year increase](https://pages.sift.com/rs/526-PCC-974/images/Sift-2023-Q3-Index-Report_ATO.pdf#page=2&search=crypto) in reported takeovers of financial (including crypto) accounts, and the Sift Q3 2024 index reported a [further](https://sift.com/index-reports-account-takeover-fraud-q3-2024?aliId=eyJpIjoiU3QxV1BmVFZ5aXFKcjh2WSIsInQiOiJXRUxtbDFycXdjTVdndERJcVd3VndRPT0ifQ%25253D%25253D#:~:text=The%20average%20ATO%20attack%20rate%20saw%20a%20significant%2024%25%20increase%20across%20the%20Sift%20Global%20Network%20in%20Q2%202024%20compared%20to%20the%20same%20period%20in%202023%2C%20rising%20from%202.9%25%20to%203.6%25.) increase in ATO across all industries since 2023.

Not only has ATO become more common, not all platforms have sufficient logging and [monitoring](https://dl.acm.org/doi/pdf/10.1145/3342220.3343651?casa_token=lMFUEleafPEAAAAA:5_XUL2raCe3Fc2lrBqTayEsxKbHYwHwaSPTb6FxOJVDSQuQV4zCXxXvWeM2lnVOhaLNpzMBrPvwU) in place to be able to detect it when it occurs and alert users promptly. Fewer than half of the victims that Sift [surveyed](https://pages.sift.com/rs/526-PCC-974/images/Sift-2023-Q3-Index-Report_ATO.pdf#page=5&search=%22notified%20by%20the%20company%20that%20their%20information%20had%20been%20compromised%22) were notified that any data loss or breach had occurred. In addition to damaging user trust in the platform, if users are not quickly and appropriately notified (and steps to prevent further future abuse aren’t taken), ATO can be costly for victims. A 2016 RAND survey of consumer attitudes toward data breach notifications and loss of personal information included the grim statistic that 68% of their respondents had suffered a [median financial loss of $864](https://www.rand.org/content/dam/rand/pubs/research_reports/RR1100/RR1187/RAND_RR1187.pdf#page=12) if their financial information was compromised1.

### Attacker tactics and opportunities

Attackers can gain initial access to user accounts through multiple vectors. In our whitepaper, we cover common weaknesses that CEX platforms must actively guard against.

For example, the user might have failed to use a strong password and a second factor. Maybe the attacker then can brute-force the use...
---
title: Risky Biz News: Microsoft rolls out number matching to counter MFA push notification spam attacks
url: https://riskybiznews.substack.com/p/risky-biz-news-microsoft-rolls-out
source: Over Security - Cybersecurity news aggregator
date: 2022-10-29
fetch_date: 2025-10-03T21:16:06.304844
---

# Risky Biz News: Microsoft rolls out number matching to counter MFA push notification spam attacks

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Microsoft rolls out number matching to counter MFA push notification spam attacks

### In other news: US Treasury sanctions MOIS cyber contractors; Apple paid $20 million to bug hunters since 2019; Raspberry Robin USB worm linked to Clop ransomware attacks.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Oct 28, 2022

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

Earlier this week, Microsoft [announced](https://techcommunity.microsoft.com/t5/microsoft-entra-azure-ad-blog/advanced-microsoft-authenticator-security-features-are-now/ba-p/2365673) the general availability of several new security features for Azure AD tenants, including "***number matching**,*" a feature to protect against an increasingly popular attack known as ***MFA push notification spam***.

Also known as ***MFA fatigue***or***MFA prompt-bombing***, this MFA bypass technique has been a little-known secret of infosec red teams for years, but it has also become extremely popular with several threat actors over the past 12 months.

The technique is typically used when a threat actor has managed to obtain a victim's valid user credentials. If the account is protected by a multi-factor authentication (MFA) solution, the attacker uses the credentials and then intentionally triggers a smartphone push notification on the account owner's phone to grant them access to the account.

The idea behind an MFA fatigue attack is to trigger repeated push notifications in the hopes that the account owner gets tired of the "spam" and approves the attacker's access to the account, or they accidentally click "yes/approve" and allow the attacker access.

Cyber-espionage groups like [APT29](https://www.mandiant.com/resources/blog/russian-targeting-gov-business) were among the first major threat actors seen using this technique, which has also since been adopted by the APT (advanced persistent teen) group Lapsus$ in their recent intrusions at Cisco, Microsoft, Okta, Nvidia, and Uber.

[![Twitter avatar for @Laughing_Mantis](https://substackcdn.com/image/twitter_name/w_96/Laughing_Mantis.jpg)

Greg Linares @Laughing\_Mantis

Lapsus$ did not invent 'MFA prompt bombing' please stop crediting them with them as creating it.
This attack vector has been a thing used in real world attacks 2 years before lapsus was a thing](https://twitter.com/Laughing_Mantis/status/1507398843587231745)[4:47 PM ∙ Mar 25, 2022

---

114Likes14Retweets](https://twitter.com/Laughing_Mantis/status/1507398843587231745)

The new "*number matching*" feature works to protect accounts by showing a number inside the push notification message received by account owners. Even if the user clicks "yes/approve" by accident, the attacker won't be able to log in without entering this number as well, which most attackers would not be able to do.

[![](https://substackcdn.com/image/fetch/$s_!PAxo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fefef3964-f512-417e-9a4f-f1431c6dafb2_509x519.png)](https://substackcdn.com/image/fetch/%24s_%21PAxo%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/efef3964-f512-417e-9a4f-f1431c6dafb2_509x519.png)

Microsoft announced this feature [earlier this year](https://techcommunity.microsoft.com/t5/microsoft-entra-azure-ad-blog/defend-your-users-from-mfa-fatigue-attacks/ba-p/2365677)—after Lapsus$ compromised its network—but a similar number matching feature has also been available in other secure authentication providers like [Cisco Duo](https://duo.com/docs/policy), [Okta](https://help.okta.com/oie/en-us/Content/Topics/identity-engine/authenticators/configure-okta-verify-options.htm), and others.

However, it must be mentioned that this technique is not foolproof, and attackers who contact employees posing as IT staff have been known to extract these numbers from employees in some attacks. But if you're forcing employees into MFA that rely on push notifications, it's better to have numbers matching enabled than not. Either way, if FIDO-based MFA is an option, better use that, as that form of cryptographic device-based authentication is not vulnerable to MFA fatigue attacks.

### Breaches and hacks

**Twilio breach:** Twilio said it concluded its investigation into its July security breach and has posted a [final version](https://www.twilio.com/blog/august-2022-social-engineering-attack) of its IR report on its blog. Conclusions below:

* The last observed unauthorized activity in our environment was on August 9, 2022;
* 209 customers – out of a total customer base of over 270,000 – and 93 Authy end users – out of approximately 75 million total users – had accounts that were impacted by the incident; and
* There is no evidence that the malicious actors accessed Twilio customers' console account credentials, authentication tokens, or API keys.

**Phishing "compensation":** Cryptocurrency exchange platform FTX said it is providing $6 million in compensation for some of its users who fell victim to a phishing scam last week. The company said the users didn't fall victim to sites posing as FTX but to sites posing as another cryptocurrency platform named 3Commas. FTX said its users provided this fake site copies of their FTX API keys, usually provided to integrate two different services, which the hackers then used to drain accounts. FTX CEO Sam Bankman-Fried called this action a "one-time" compensation and said that the platform does not intend to compensate users again for losses due to phishing at other platforms. [*Additional coverage in [CoinTelegraph](https://cointelegraph.com/news/ftx-to-give-a-one-time-6m-compensation-to-phishing-victims)*]

**Team Finance hack:** DeFi platform Team Finance confirmed on Twitter on Thursday that a hacker exploited a platform migration feature and stole roughly $14.5 million worth of cryptocurrency from its wallets.

**New York Post hack:** Controversial right-wing tabloid the New York Post [said](https://twitter.com/nypost/status/1585629621521100801) it suffered a security breach on Thursday. No official details were provided, but users on social media reported that the NY Post website and Twitter accounts were seen posting [calls for the assassination](https://twitter.com/disclosetv/status/1585625370711425025) of several prominent Democrat figures.

[![](https://substackcdn.com/image/fetch/$s_!rOw2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3e0859fa-efe1-4021-bd97-f96174e5599a_557x304.png)](https://substackcdn.com/image/fetch/%24s_%21rOw2%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/3e0859fa-efe1-4021...
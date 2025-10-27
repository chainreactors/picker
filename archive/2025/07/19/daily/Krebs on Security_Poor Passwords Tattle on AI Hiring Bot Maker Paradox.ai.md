---
title: Poor Passwords Tattle on AI Hiring Bot Maker Paradox.ai
url: https://krebsonsecurity.com/2025/07/poor-passwords-tattle-on-ai-hiring-bot-maker-paradox-ai/
source: Krebs on Security
date: 2025-07-19
fetch_date: 2025-10-07T00:01:51.763346
---

# Poor Passwords Tattle on AI Hiring Bot Maker Paradox.ai

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Poor Passwords Tattle on AI Hiring Bot Maker Paradox.ai

July 17, 2025

[23 Comments](https://krebsonsecurity.com/2025/07/poor-passwords-tattle-on-ai-hiring-bot-maker-paradox-ai/#comments)

Security researchers recently revealed that the personal information of millions of people who applied for jobs at **McDonald’s** was exposed after they guessed the password (“123456”) for the fast food chain’s account at **Paradox.ai**, a company that makes artificial intelligence based hiring chatbots used by many Fortune 500 firms. Paradox.ai said the security oversight was an isolated incident that did not affect its other customers, but recent security breaches involving its employees in Vietnam tell a more nuanced story.

![](https://krebsonsecurity.com/wp-content/uploads/2025/07/paradoxai.png)

Earlier this month, security researchers **Ian Carroll** and **Sam Curry** [wrote about](https://ian.sh/mcdonalds) simple methods they found to access the backend of the AI chatbot platform on McHire.com, the McDonald’s website that many of its franchisees use to screen job applicants. As first reported by [Wired](https://www.wired.com/story/mcdonalds-ai-hiring-chat-bot-paradoxai/), the researchers discovered that the weak password used by Paradox exposed 64 million records, including applicants’ names, email addresses and phone numbers.

Paradox.ai acknowledged the researchers’ findings but said the company’s other client instances were not affected, and that no sensitive information — such as Social Security numbers — was exposed.

“We are confident, based on our records, this test account was not accessed by any third party other than the security researchers,” the company wrote in [a July 9 blog post](https://www.paradox.ai/blog/responsible-security-update). “It had not been logged into since 2019 and frankly, should have been decommissioned. We want to be very clear that while the researchers may have briefly had access to the system containing all chat interactions (NOT job applications), they only viewed and downloaded five chats in total that had candidate information within. Again, at no point was any data leaked online or made public.”

However, a review of stolen password data gathered by multiple breach-tracking services shows that at the end of June 2025, a Paradox.ai administrator in Vietnam suffered a malware compromise on their device that stole usernames and passwords for a variety of internal and third-party online services. The results were not pretty.

The password data from the Paradox.ai developer was stolen by a malware strain known as “**Nexus Stealer**,” a form grabber and password stealer that is sold on cybercrime forums. The information snarfed by stealers like Nexus is often recovered and indexed by data leak aggregator services like **Intelligence X**, which reports that the malware on the Paradox.ai developer’s device exposed hundreds of mostly poor and recycled passwords (using the same base password but slightly different characters at the end).

Those purloined credentials show the developer in question at one point used the same seven-digit password to log in to Paradox.ai accounts for a number of [Fortune 500 firms listed as customers on the company’s website](https://www.paradox.ai/clients-stories), including **Aramark**, **Lockheed Martin**, **Lowes**, and **Pepsi.**

Seven-character passwords, particularly those consisting entirely of numerals, are highly vulnerable to “brute-force” attacks that can try a large number of possible password combinations in quick succession. According to [a much-referenced password strength guide](https://www.hivesystems.com/blog/are-your-passwords-in-the-green) maintained by **Hive Systems**, modern password-cracking systems can work out a seven number password more or less instantly.

![](https://krebsonsecurity.com/wp-content/uploads/2025/07/hivesystems-pwdcrack.png)

Image: hivesystems.com.

In response to questions from KrebsOnSecurity, Paradox.ai confirmed that the password data was recently stolen by a malware infection on the personal device of a longtime Paradox developer based in Vietnam, and said the company was made aware of the compromise shortly after it happened. Paradox maintains that few of the exposed passwords were still valid, and that a majority of them were present on the employee’s personal device only because he had migrated the contents of a password manager from an old computer.

Paradox also pointed out that it has been requiring single sign-on (SSO) authentication since 2020 that enforces multi-factor authentication for its partners. Still, a review of the exposed passwords shows they included the Vietnamese administrator’s credentials to the company’s SSO platform — paradoxai.okta.com. The password for that account ended in 202506 — possibly a reference to the month of June 2025 — and the digital cookie left behind after a successful Okta login with those credentials says it was valid until December 2025.

Also exposed were the administrator’s credentials and authentication cookies for an account at **Atlassian**, a platform made for software development and project management. The expiration date for that authentication token likewise was December 2025.

Infostealer infections are among the leading causes of data breaches and ransomware attacks today, and they result in the theft of stored passwords and any credentials the victim types into a browser. Most infostealer malware also will siphon authentication cookies stored on the victim’s device, and depending on how those tokens are configured thieves may be able to use them to bypass login prompts and/or multi-factor authentication.

Quite often these infostealer infections will open a backdoor on the victim’s device that allows attackers to access the infected machine remotely. Indeed, it appears that remote access to the Paradox administrator’s compromised device was offered for sale recently.

In February 2019, Paradox.ai [announced](https://www.paradox.ai/news/paradox-receives-iso-27001-and-soc-2-type-ii-security-certifications) it had successfully completed audits for two fairly comprehensive security standards (ISO 27001 and SOC 2 Type II). Meanwhile, the company’s security disclosure this month says the test account with the atrocious 123456 username and password was last accessed in 2019, but somehow missed in their annual penetration tests. So how did it manage to pass such stringent security audits with these practices in place?

Paradox.ai told KrebsOnSecurity that at the time of the 2019 audit, the company’s various contractors were not held to the same security standards the company practices internally. Paradox emphasized that this has changed, and that it has updated its security and password requirements multiple times since then.

It is unclear how the Paradox developer in Vietnam infected his computer with malware, but a closer review finds a Windows device for another Paradox.ai employee from Vietnam was compromised by similar data-stealing malware at the end of 2024 (that compromise included the victim’s GitHub credentials). In the case of both employees, the stolen credential data includes Web browser logs that indicate the victims repeatedly downlo...
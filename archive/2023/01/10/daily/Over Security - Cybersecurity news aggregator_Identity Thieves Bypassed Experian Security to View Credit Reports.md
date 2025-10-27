---
title: Identity Thieves Bypassed Experian Security to View Credit Reports
url: https://krebsonsecurity.com/2023/01/identity-thieves-bypassed-experian-security-to-view-credit-reports/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-10
fetch_date: 2025-10-04T03:26:54.610378
---

# Identity Thieves Bypassed Experian Security to View Credit Reports

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/8.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Identity Thieves Bypassed Experian Security to View Credit Reports

January 9, 2023

[77 Comments](https://krebsonsecurity.com/2023/01/identity-thieves-bypassed-experian-security-to-view-credit-reports/#comments)

Identity thieves have been exploiting a glaring security weakness in the website of **Experian**, one of the big three consumer credit reporting bureaus. Normally, Experian requires that those seeking a copy of their credit report successfully answer several multiple choice questions about their financial history. But until the end of 2022, Experian’s website allowed anyone to bypass these questions and go straight to the consumer’s report. All that was needed was the person’s name, address, birthday and Social Security number.

![](https://krebsonsecurity.com/wp-content/uploads/2023/01/exp-1.png)

In December, KrebsOnSecurity heard from **Jenya Kushnir**, a security researcher living in Ukraine who said he discovered the method being used by identity thieves after spending time on **Telegram** chat channels dedicated to the cashing out of compromised identities.

“I want to try and help to put a stop to it and make it more difficult for [ID thieves] to access, since [Experian is] not doing shit and regular people struggle,” Kushnir wrote in an email to KrebsOnSecurity explaining his motivations for reaching out. “If somehow I can make small change and help to improve this, inside myself I can feel that I did something that actually matters and helped others.”

Kushnir said the crooks learned they could trick Experian into giving them access to anyone’s credit report, just by editing the address displayed in the browser URL bar at a specific point in Experian’s identity verification process.

Following Kushnir’s instructions, I sought a copy of my credit report from Experian via **annualcreditreport.com** — a website that is required to provide all Americans with a free copy of their credit report from each of the three major reporting bureaus, once per year.

Annualcreditreport.com begins by asking for your name, address, SSN and birthday. After I supplied that and told Annualcreditreport.com I wanted my report from Experian, I was taken to Experian.com to complete the identity verification process.

![](https://krebsonsecurity.com/wp-content/uploads/2023/01/exp-ssna.png)

Normally at this point, Experian’s website would present four or five multiple-guess questions, such as “Which of the following addresses have you lived at?”

Kushnir told me that when the questions page loads, you simply change the last part of the URL from “/acr/oow/” to “/acr/report,” and the site would display the consumer’s full credit report.

But when I tried to get my report from Experian via annualcreditreport.com, Experian’s website said it didn’t have enough information to validate my identity. It wouldn’t even show me the four multiple-guess questions. Experian said I had three options for a free credit report at this point: Mail a request along with identity documents, call a phone number for Experian, or upload proof of identity via the website.

But that didn’t stop Experian from showing me my full credit report after I changed the Experian URL as Kushnir had instructed — modifying the error page’s trailing URL from “/acr/OcwError” to simply “/acr/report”.

Experian’s website then immediately displayed my entire credit file.

[![](https://krebsonsecurity.com/wp-content/uploads/2023/01/exp-4.png)](https://krebsonsecurity.com/wp-content/uploads/2023/01/exp-4.png)

Even though Experian said it couldn’t tell that I was actually me, it still coughed up my report. And thank goodness it did. The report contains so many errors that it’s probably going to take a good deal of effort on my part to straighten out.

Now I know why Experian has NEVER let me view my own file via their website. For example, there were four phone numbers on my Experian credit file: Only one of them was mine, and that one hasn’t been mine for ages.

I was so dumbfounded by Experian’s incompetence that I asked a close friend and trusted security source to try the method on her identity file at Experian. Sure enough, when she got to the part where Experian asked questions, changing the last part of the URL in her address bar to “/report” bypassed the questions and immediately displayed her full credit report. Her report also was replete with errors.

KrebsOnSecurity shared Kushnir’s findings with Experian on Dec. 23, 2022. On Dec. 27, 2022, Experian’s PR team acknowledged receipt of my Dec. 23 notification, but the company has so far ignored multiple requests for comment or clarification.

By the time Experian confirmed receipt of my report, the “exploit” Kushnir said he learned from the identity thieves on Telegram had been patched and no longer worked. But it remains unclear how long Experian’s website was making it so easy to access anyone’s credit report.

In response to information shared by KrebsOnSecurity, **Senator Ron Wyden** (D-Ore.) said he was disappointed — but not at all surprised — to hear about yet another cybersecurity lapse at Experian.

“The credit bureaus are poorly regulated, act as if they are above the law and have thumbed their noses at Congressional oversight,” Wyden said in a written statement. “Just last year, Experian ignored repeated briefing requests from my office after you revealed another cybersecurity lapse the company.”

Sen. Wyden’s quote above references a story published here in July 2022, which broke the news that identity thieves were hijacking consumer accounts at Experian.com just by signing up as them at Experian once more, [supplying the target’s static, personal information (name, DoB/SSN, address) but a different email address](https://krebsonsecurity.com/2022/07/experian-you-have-some-explaining-to-do/).

From interviews with multiple victims who contacted KrebsOnSecurity after that story, it emerged that Experian’s own customer support representatives were actually telling consumers who got locked out of their Experian accounts to recreate their accounts using their personal information and a new email address. This was Experian’s advice even for people who’d just explained that this method was what identity thieves had used to lock them in out in the first place.

Clearly, Experian found it simpler to respond this way, rather than acknowledging the problem and addressing the root causes (lazy authentication and abhorrent account recovery practices). It’s also worth mentioning that reports of hijacked Experian.com accounts persisted into late 2022. That screw-up has since prompted [a class action lawsuit against Experian](https://krebsonsecurity.com/2022/08/class-action-targets-experian-over-account-security/).

Sen. Wyden said the **Federal Trade Commission** (FTC) and **Consumer Financial Protection Bureau** (CFPB) need to do much more to protect Americans from screw-ups by the credit bureaus.

“If they don’t believe they have the authority to do so, they should endorse legislation like my [Mind Your Own Business Act](https://www.congress.gov/bill/117th-congress/senate-bill/1444), which gives the FTC power to set tough mandatory cybersecurity standards for companies like Experian,” Wyden said.

Sad...
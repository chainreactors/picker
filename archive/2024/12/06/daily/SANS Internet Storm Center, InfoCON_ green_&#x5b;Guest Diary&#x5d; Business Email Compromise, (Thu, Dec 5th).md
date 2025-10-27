---
title: &#x5b;Guest Diary&#x5d; Business Email Compromise, (Thu, Dec 5th)
url: https://isc.sans.edu/diary/rss/31474
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-06
fetch_date: 2025-10-06T19:41:55.481383
---

# &#x5b;Guest Diary&#x5d; Business Email Compromise, (Thu, Dec 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31472)
* [next](/diary/31476)

# [[Guest Diary] Business Email Compromise](/forums/diary/Guest%2BDiary%2BBusiness%2BEmail%2BCompromise/31474/)

**Published**: 2024-12-05. **Last Updated**: 2024-12-05 00:09:30 UTC
**by** [Chris Kobbe, SANS.edu BACS Student](/handler_list.html#chris-kobbe,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/Guest%2BDiary%2BBusiness%2BEmail%2BCompromise/31474/#comments)

[This is a Guest Diary by Chris Kobee, an ISC intern as part of the SANS.edu Bachelor's Degree in Applied Cybersecurity (BACS) program [1].

Business Email Compromise (BEC) is a lucrative attack, which FBI data shows 51 billion dollars in losses between 2013 to 2022 [2]. According to SentinelOne, nearly all cybersecurity attacks (98%) contain a social engineering component [3].The social engineering attacks include phishing, spear phishing, smishing, whaling , etc.  Figure 1 is a distribution of social engineering attacks from Statista depicting Scamming, Phishing, and BEC attacks worldwide [4]. Scamming is the leader, followed by Phishing and BEC [5]. BEC and other social engineering attacks are the path of least resistance with a high rate of success versus attempting technical network intrusions.

In May 2024, a significant cybersecurity incident unfolded within an organization, showcasing the vulnerabilities that can arise from BEC harvesting user credentials and the exploitation of cloud services like Microsoft 365  . This post aims to break down the events, identify the vulnerabilities exploited, and review implemented and proposed mitigations to thwart similar threats.

**![](https://isc.sans.edu/diaryimages/images/2024-12-05_figure1.png)
Figure 1: Distribution of Worldwide Social Engineering Attacks**

## Organization Incident Overview

From May 20 to 23, 2024, a threat actor successfully accessed a Microsoft 365 account belonging to a user in the organization’s accounting department with the user’s valid credentials. The actor manipulated account details in a pending invoice and redirected funds to their own bank account. The incident was characterized by several key actions  beginning on May 20 when the actor successfully logged into the Microsoft 365 account after a rejection pattern of an expired session ID and MFA denials.

The actor conducted reconnaissance on May 22, potentially identifying the pending vendor invoices for payment. The attacker logged into the user’s email account on May 23rd and created a new inbox rule to direct any correspondence with the vendor organization’s name to the RSS Feeds folder in the inbox. The actor altered the target document and sent it to the next stage in the approval process. The accounting department’s processes broke down and did not catch spelling and grammar errors that could have tipped off potential fraud. The document was approved, the ACH payment was authorized, and payment was completed. The organization’s Managed Service Provider/Managed Security Service Provider (MSP/MSSP) receive an alert and re-secured the account later in the early evening, effectively locking out the actor. Figures 2 and 3 display a high-level summary of the events and timeline.

**![](https://isc.sans.edu/diaryimages/images/2024-12-05_figure2.PNG)
Figure 2: Business Email Compromise Attack Timeline**

**![](https://isc.sans.edu/diaryimages/images/2024-12-05_figure3.PNG)
Figure 3: Threat Actor Login Attempts**

## Initial Access

The  attacker logged into the organization's M365 tenant using compromised credentials on May 20, 2024, and re-entered the system on May 22 for reconnaissance. The actor appears to have conducted reconnaissance on May 22 for approximately thirty-four minutes, during which the pending invoice was potentially discovered.

## Fraud Executed

On May 23, the attacker logged into the email exchange and executed bank fraud by altering the invoice's destination bank account. They also implemented new inbox rules  (Figure 4) within the Outlook account to obscure their activities by redirecting any email traffic with the vendor’s name to an obscure folder. The newly created inbox rules, one rule for each organizational name the vendor employs, directed any incoming communications to the RSS Feeds folder for obscurity from the authorized account user. The target vendor was purchased by another company and sends correspondence from both companies, which the attacker covered with both rules. The attacker sent the fraudulent invoice to the next accounting staff member for further processing.

**![](https://isc.sans.edu/diaryimages/images/2024-12-05_figure4.PNG)
Figure 4: Threat Actor Action on Objective**

## Covered Tracks

The threat actor attempted to cover their actions by deleting items and folders created while in the organization’s cloud account (Figure 5),  withdrew the funds shortly after the transfer, and closed the bank account. The organization reached out to the actor’s financial institution to reverse the payment, but the financial institution rejected the request to reverse the payment due to the account closure.

**![](https://isc.sans.edu/diaryimages/images/2024-12-05_figure5.PNG)
Figure 5: Threat Actor’s Covering Tracks Attempt**

## Detection

The organization's MSP/MSSP detected an unusual inbox rule change and resecured the compromised account (Figure 6), but not before the attacker could execute their plan.

**![](https://isc.sans.edu/diaryimages/images/2024-12-05_figure6.PNG)
Figure 6: Threat Actor Activity Detected by MSP/MSSP**

## Analysis

Analysis of the logs, provided by the Cloud Service Provider, suggests MFA was bypassed and potential collusion or manipulation of the organization’s assigned user. Further research revealed a CVE written against the Microsoft Authenticator application employed by the organization on company issue and BYOD mobile devices.

## Multi-Factor Authentication (MFA)

MFA was enabled during the attack, with logs indicating the attacker faced several denied attempts before successfully logging in. This suggests potential insider collusion, manipulation of the authorized user, and/or an Attacker-in-the-Middle tool, such as evilginx2 [5] or later version used for to phish user credentials, session cookies, and bypass MFA. Figure 7 depicts the pattern of a failed login with an expired session ID, followed by three failed logins due to MFA denials, and a successful login on May 20th and 22nd [6].

**![](https://isc.sans.edu/diaryimages/images/2024-12-05_figure7.PNG)
Figure 7: Threat Actor Login Attempt Pattern**

## Vulnerability in Microsoft Authenticator

The incident points to a specific vulnerability (CVE-2024-21390) in the Microsoft Authenticator application (Figure 5), which can be exploited if an attacker gains access to the user's local device and convinces the user to relaunch the authenticator app [7][8]. The threat actor potentially compromised the user’s mobile device through malware delivered via phishing or smishing vector allowing the opportunity to manipulate the user to close and re-launch the application on the mobile device.

**![](https://isc.sans.edu/diaryimages/images/2024-12-05_figure8.PNG)
Figure 8: Microsoft Authenticator Vulnerability**

## Conclusion, Mitigations, Lessons Learned

Business Email Compromise was the main factor in this attack as the threat actor used it as the attack vector and sent emails between the accounting department from the compromised user’s account to commit bank fraud. The attacker most likely obtained the user’s credentials through a phishing email tricking the user into clicking a link and inputting credentials on a web page highly resembling a Microsoft login page. Due to the nature of the Cloud Service Provider (CSP) / Cloud Customer Software as a Service (SaaS) model ...
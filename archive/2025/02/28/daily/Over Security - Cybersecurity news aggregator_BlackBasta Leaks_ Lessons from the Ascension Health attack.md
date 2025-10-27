---
title: BlackBasta Leaks: Lessons from the Ascension Health attack
url: https://blog.bushidotoken.net/2025/02/blackbasta-leaks-lessons-from-ascension.html
source: Over Security - Cybersecurity news aggregator
date: 2025-02-28
fetch_date: 2025-10-06T20:39:36.158461
---

# BlackBasta Leaks: Lessons from the Ascension Health attack

[Skip to main content](#main)

### Search This Blog

# [@BushidoToken Threat Intel](https://blog.bushidotoken.net/)

### BlackBasta Leaks: Lessons from the Ascension Health attack

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-
[February 27, 2025](https://blog.bushidotoken.net/2025/02/blackbasta-leaks-lessons-from-ascension.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-qoL0E4JtCsVj8ok2ypVL4NMiNd8empJ3AiU6daFD2D3V2yxMZVoGgrWlwLlb4eC2HwbS5HRB-6k0nMEht3aEVc-f_Cgt4ei5exGzbq3v_uf_L9VTnMf2x3RATanSrAAnlrRKJJWzuFTD-as1pcQi1QmRFgHCBXqxk9smz41AUl-0JUL_bIuWleszY5Vu/w640-h270/blackbasta.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-qoL0E4JtCsVj8ok2ypVL4NMiNd8empJ3AiU6daFD2D3V2yxMZVoGgrWlwLlb4eC2HwbS5HRB-6k0nMEht3aEVc-f_Cgt4ei5exGzbq3v_uf_L9VTnMf2x3RATanSrAAnlrRKJJWzuFTD-as1pcQi1QmRFgHCBXqxk9smz41AUl-0JUL_bIuWleszY5Vu/s613/blackbasta.png)

The BlackBasta ransomware group’s [leaked chat logs](https://www.bleepingcomputer.com/news/security/black-basta-ransomware-gang-s-internal-chat-logs-leak-online/) have proven
to already be another unique and fascinating opportunity for researchers to
better understand the internal operations of a Russia-based organised
cybercrime enterprise. These leaks followed a major leak of Conti chat logs in
2022, which also proved to be a [treasure trove of intelligence](https://blog.bushidotoken.net/2022/04/lessons-from-conti-leaks.html) on the cybercrime
enterprise. The BlackBasta gang consists of former Conti ransomware members and
it should come as no surprise that their operations are similar in nature and
structure.

Ransomware researchers have several valuable resources to
conduct investigations with nowadays. This includes [ransomware.live](https://www.ransomware.live/), which contains several
resources including [ransomch.at](https://ransomch.at/), a
collection of negotiation chats between ransomware gangs and their victims, as
well as the [ransomware
tool matrix](https://github.com/BushidoUK/Ransomware-Tool-Matrix) and [ransomware
vulnerability matrix](https://github.com/BushidoUK/Ransomware-Vulnerability-Matrix). These resources allow to deeply understand the
capabilities and motivations of these ransomware gangs. However, leaked chat logs
are the final missing piece of the puzzle and offer a deeper understanding from
the cybercriminal’s very own perspective and organisational structure.

Active [since
April 2022](https://www.bleepingcomputer.com/news/security/new-black-basta-ransomware-springs-into-action-with-a-dozen-breaches/), BlackBasta is one of the top-tier ransomware gangs and one of
the largest cybercrime enterprises in the world. According to the [US
Cybersecurity Infrastructure and Security Agency (CISA)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-131a), BlackBasta impacted
up to 500 different businesses and critical infrastructure in North America,
Europe, and Australia as of May 2024.

## The importance of the Ascension Health incident

This blog shall dive deep into the Ascension Health attack
by BlackBasta. It is a step-by-step extraction of the conversation between the
BlackBasta members while they decide how to handle the attack.

The new insights around how BlackBasta and other ransomware
gangs perceive being involved with incidents at healthcare sector victim should
prove useful for incident responders, law enforcement, and governments that have
to resolve these types of attacks on the healthcare sector on an alarmingly
regularly basis.

## Background

On 9 May 2024, mainstream news organisations in the US
reported about a cyberattack and significant disruption of services of
Ascension Health, one of the largest healthcare providers in the country. On 11
May 2024, [BleepingComputer](https://www.bleepingcomputer.com/news/security/healthcare-giant-ascension-redirects-ambulances-after-suspected-Black-Basta-ransomware-attack/)
reported that BlackBasta was to blame for the attack on Ascension Health and
that ambulances had been disrupted and patients were being redirected to other
hospitals.

## How the Incident Began

The BlackBasta attack on Ascension Health began many months
before the ransomware was deployed on their network. Reconnaissance of
Ascension Health by members of BlackBasta began around 3 November 2023. They shared
14 email addresses of Ascension Health employees, which we can only assume were
used for phishing or password guessing. Ransomware gangs often used Zoominfo to
profile their targets to determine whether it is worth it for them to attack
and get a ransom from them.

![A screenshot of a chat  AI-generated content may be incorrect.](data:image/png;base64...)

The ransomware gang themselves wrote in their Matrix chat
that [CBS
News](https://d.docs.live.net/62bce0f216f5575d/Documents/Blogs/%E2%80%A2%09https%3A/www.cbsnews.com/chicago/news/ascension-health-care-network-disrupted-cyberattack/) had written about a cyberattack on Ascension Health on 9 May 2024 and
exclaimed that “it looks like one of the largest attacks of the year.”

![A screenshot of a chat  AI-generated content may be incorrect.](data:image/png;base64...)

Another BlackBasta member “gg” confirmed in the chat that it
was them and appeared to be surprised that the news was writing about it.

![](data:image/png;base64...)

Later, “gg” appeared to feel bad about the attack and
concerned that cancer patients were suffering. However, at this stage it is
hard to tell if they are serious or being sarcastic.

![A close-up of a white rectangular object  AI-generated content may be incorrect.](data:image/png;base64...)

One member of BlackBasta who used the moniker “tinker” then
stated that he wanted to be the negotiator for the BlackBasta team and began to
strategize how to extract a ransom payment.

![A close-up of a white background  AI-generated content may be incorrect.](data:image/png;base64...)

“gg” says they encrypted Ascension Health’s network using
the Windows [Safe Mode Boot](https://attack.mitre.org/techniques/T1562/009/)
technique, which is a function that [BlackBasta
is well-known](https://www.trendmicro.com/en_gb/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html) to do.

![A screenshot of a computer  AI-generated content may be incorrect.](data:image/png;base64...)

The negotiator, “tinker” begins to weigh up their options.
He states he believes the FBI and CISA will be involved, as well as Mandiant
and begins to compare the incident to the [Change
Healthcare attack](https://www.wired.com/story/alphv-change-healthcare-ransomware-payment/) by ALPHV/BlackCat (and later RansomHub) who received a 22
million USD ransom payment.

![A close-up of a sign  AI-generated content may be incorrect.](data:image/png;base64...)

![A screenshot of a message  AI-generated content may be incorrect.](data:image/png;base64...)

“gg” shares that all the stolen data was put on a server
named “ftp8” and tagged as “ALBIR\_DS” and says to “tinker” that he should “look
at the folder name, everything we downloaded from them is there."

The operator, “gg” also shared a summary of the target
environment of Ascension Health. This includes number of servers being over
12,000, what security tools they use such as Cylance, Tanium, and McAfee. Plus,
“gg” said they downloaded over 1.4TB of data to "ftp8" and used
BlackBasta ransomware version 4.0 and attacked them on 8 May 2024.

![A screenshot of a chat  AI-generated content may be incorrect.](data:image/png;base64...)

Interestingly, “gg” appears to have also recommended to
bluff to the victim that they stole more than 1.5TB and say to the victim that
they stole 3TB instead.

## Negotiation Strategizing

After having established the details of the incident, Tinker
(the negotiator) began to wonder about the likelihood of getting a ransom
payment as well as estimate how much Ascension Health is likely losing per day.

![A close-up of a message  AI-generated content may be incorrect.]...
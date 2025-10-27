---
title: Using Newly Surfaced Data Breaches for OSINT Research
url: https://www.secjuice.com/osint-data-breach-research/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-26
fetch_date: 2025-10-06T19:22:24.521333
---

# Using Newly Surfaced Data Breaches for OSINT Research

[![Secjuice](https://www.secjuice.com/content/images/2018/12/Logo-1.png)](https://www.secjuice.com)

* [Donate](https://opencollective.com/secjuice)
* [About Us](https://secjuice.com/about-us/)
* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/OSINT/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write With Us](https://secjuice.com/join-secjuice-writing-team/)
* [Hire A Writer](https://secjuice.com/hire-infosec-cybersecurity-writer/)
* [Rankings](https://secjuice.com/secjuice-writers-ranking/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

[OSINT](/tag/osint/)

 Featured

# Using Newly Surfaced Data Breaches for OSINT Research

Data Breach Search Engines (DBSEs) collect and organize leaked information from data breaches, enabling OSINT investigators to access it.

* [![Tom Caliendo](/content/images/size/w100/2022/07/square-profile.png)](/author/tom-caliendo/)

#### [Tom Caliendo](/author/tom-caliendo/)

Nov 24, 2024
• 5 min read

![Using Newly Surfaced Data Breaches for OSINT Research](/content/images/size/w2000/2024/11/turkeys-doing-cirque-du-soleil.png)

Turkeys performing at a modern circus show. Microsoft Copilot created this image.

Data breaches are an unfortunate reality for many websites, leading to leaked information often posted on dark web forums or discovered by security researchers. Before this data disappears or is removed, Data Breach Search Engines (DBSEs) gather, verify, and categorize it, making it accessible to people seeking to understand what information may have been compromised. DBSEs like *Have I Been Pwned* allow OSINT (open-source intelligence) investigators to enter an email address and see if it was used on a breached site, often revealing critical information about the target’s online footprint. These DBSEs serve as an important privacy service, allowing users to know if their information has been exposed and, in some cases, request its removal from these databases.

## **What are Data Breach Search Engines?**

DBSEs provide a way to find out where an email address, phone number, username, or other identifier has been used, giving researchers a clearer sense of a person’s digital presence. If a DBSE search shows that an email was compromised in a LinkedIn breach, for example, an investigator knows the person likely had a LinkedIn account. This information is invaluable for OSINT researchers, as it offers hints about a target’s professional network, social media presence, and even connections to colleagues or alternate emails. Some of the most popular DBSEs include *Have I Been Pwned* (searchable by email or phone), *IntelX.io* (email), and *dehashed.com* (email, username, domain, password, IP). There are also more specific breach-focused tools, such as *haveibeenzucked.com* for Facebook data and *checkashleymadison.com* for the Ashley Madison breach. These tools maintain deep web databases, and the information within them can often be accessed only through the website itself. For OSINT investigators, understanding DBSE resources is critical, as each can reveal unique details about where an email address, phone number, or other identifier was registered and whether it has been compromised.

## **Data Breaches Now Available on Data Breach Information Sites**

This month, four major data breaches have appeared on platforms like *Have I Been Pwned*, each offering unique insights into different user communities. Although some breaches occurred years ago, the data is newly available on DBSEs, presenting OSINT researchers with new avenues to explore.

1. Internet Archive (October 2024)

In October 2024, the Internet Archive, famous for its digital preservation efforts and the Wayback Machine, experienced a breach affecting 31 million user accounts. Data exposed includes email addresses, screen names, and bcrypt-hashed passwords. The Internet Archive responded to the breach quickly and transparently, immediately implementing security measures, disabling compromised libraries, and restoring service in read-only mode while the organization strengthened its defenses. This breach is notable for OSINT researchers interested in online archives and historical data access, as it suggests users engaged in digital research or preservation activities.

2. VimeWorld (October 2018)

VimeWorld, a Russian Minecraft service, experienced a data breach in 2018 that exposed data on 3.1 million users. The compromised information includes usernames, email addresses, IP addresses, and hashed passwords (MD5 or bcrypt). This breach’s recent availability in DBSEs presents new opportunities for researchers interested in gaming communities, particularly among Russian-speaking audiences.

3. StreamCraft (July 2020)

The StreamCraft breach in July 2020 affected 1.8 million records, exposing usernames, email addresses, IP addresses, and hashed passwords (MD5 or bcrypt). StreamCraft data, newly accessible for OSINT purposes, provides a look into the online behavior of gaming communities, especially among users who favor multiplayer gaming.

4. AlpineReplay (2019)

The 2019 breach of AlpineReplay, a fitness-tracking app later integrated into Trace, exposed 900,000 records, including email addresses, usernames, dates of birth, gender, weight, and passwords hashed with MD5 or bcrypt. Recently appearing in DBSEs, this data gives insights into the interests of fitness enthusiasts, particularly those who use digital tools to track performance in sports like skiing and snowboarding.

## **Why These Data Breaches Matter to Researchers**

When an OSINT researcher finds an email address in one of these breaches, it can reveal valuable information about the target’s digital activities. Each platform represents a specific online community or interest, giving clues about an individual’s preferences, affiliations, or lifestyle.

• Internet Archive: If someone’s data is in the Internet Archive breach, it might indicate an interest in digital preservation, academic research, or access to open-source content. This can suggest a background in academia or a strong interest in historical records.

• VimeWorld and StreamCraft: The presence of someone’s account in these gaming-related breaches points to involvement in online gaming, possibly within Russian-speaking or international communities. This can help an investigator understand the target’s recreational interests and engagement in gaming culture.

• AlpineReplay: An account in the AlpineReplay breach implies an interest in fitness, specifically in winter sports like skiing and snowboarding. The individual is likely health-conscious and inclined toward tracking their performance, providing insights into their lifestyle and personal values.

Simply knowing that a target’s email address is associated with one of these platforms can reveal a lot about them. However, OSINT researchers should approach this data cautiously. While these accounts provide contextual information, they don’t give a complete picture of a person’s behavior or habits, so researchers should use this information as a starting point rather than a conclusive profile.

## **Detailed Look at the Internet Archive Data Breach**

The October 2024 Internet Archive breach involved the exposure of data from around 31 million user accounts. This breach, linked to a compromised GitLab token, allowed attackers to access development servers, revealing email addresses, screen names, and bcrypt-hashed passwords. The first breach occurred on October 9, with attackers exploiting a GitLab configuration file on the Internet Archive’s servers that contained an exposed authentication token. This gave them access to the source code, credentials, and, ultimately, the database management system, where they downloaded user data and modified site elements. Reports suggest this token had been accessible since December 2022, giving attackers a prolonge...
---
title: I Hacked BellaBot and Every Robot from China's Biggest Robotics Company (Pudu Only Fixed It When I Told Their Clients)
url: https://bobdahacker.com/blog/hacked-biggest-chinese-robot-company
source: Over Security
date: 2026-11-02
fetch_date: 2026-11-03T08:51:36.820425
---

# I Hacked BellaBot and Every Robot from China's Biggest Robotics Company (Pudu Only Fixed It When I Told Their Clients)

[bobdahacker](/)

☰

* [home](/)
* [blog](/blog)

# I Hacked BellaBot and Every Robot from China's Biggest Robotics Company (Pudu Only Fixed It When I Told Their Clients)

August 29, 2025

BobDaHacker

*Critical vulnerabilities in Pudu Robotics' entire fleet - BellaBot, KettyBot, and all their service robots used globally. They ignored emails until I contacted their biggest customers.*

## More Than Just Robot Waiters

![A photo of bellabot](/static/images/blogs/pudu/bellabot.png)
You've probably seen these cat-faced robots delivering food in restaurants. Pudu Robotics is the world's largest commercial service robotics company, making not just the famous BellaBot robot waiter, but an entire [product line](https://www.pudurobotics.com/en/products) including:

* Delivery robots (BellaBot, KettyBot, PuduBot)
* Cleaning robots (CC1, PUDU SH1)
* Disinfection robots
* Building delivery robots with mechanical arms that can use elevators

These robots operate in restaurants, hospitals, hotels, offices, and retail stores worldwide. hundereds of thousands if not more of them, serving millions of people daily.

## The Vulnerabilities

On August 12th, I discovered Pudu's robot management APIs had zero authentication checks (it checked if you had a valid auth token but not your permissions). Any of their robots could be controlled by anyone:

1. **View any robot's call history** - Accepts up to 20,000 store IDs in a single array with no rate limiting
   ![Postman yes](/static/images/blogs/pudu/apiRequest1.png)
2. **Create calls/control any robots you don't own** - Send any robot anywhere
   ![Postman yes](/static/images/blogs/pudu/apiRequest2.png)
3. **Update any robot's settings** - Change nicknames, configurations, behaviors
   ![Postman yes](/static/images/blogs/pudu/apiRequest3.png)
4. **List any stores robots globally** - List robots by a Store Id
   ![Postman yes](/static/images/blogs/pudu/apiRequest4.png)
5. **Systematic authentication failure** - Almost every API endpoint was vulnerable, and didnt check ownership.

Whether it's a BellaBot in a restaurant, a FlashBot in an office building, or a disinfection robot in a hospital - all controllable by anyone who found the API.

## What Could Go Wrong?

The possibilities for chaos were endless:

**Restaurant Mayhem:**

* Make a BellaBot deliver food to your table instead of the people who ordered it
* Cancel all robot tasks during rush hour
* Have robots continuously circle the dining room playing music

**Office Espionage:**
Their FlashBot has arms and elevator integration. Someone could remotely control it to grab confidential documents from an office, ride the elevator alone, and deliver them to the back exit. An action movie irl.

**Robot Ransom:**

* Hold an entire fleet hostage by canceling all their tasks
* Make robots go to wrong locations repeatedly
* Demand payment to stop the chaos (some of their robots have screens, so an attacker could put a bitcoin qr code and text saying "pay 69 bitcoin and we will stop ransoming your robot" )

**Hospital Havoc:**

* Redirect medicine delivery robots
* Send cleaning robots to operating rooms
* Make disinfection robots skip critical areas

I could have orchestrated a synchronized robot dance party across every Pudu robot globally. Thankfully, I just reported it instead.

## The Silent Treatment

I reported these vulnerabilities to Pudu on August 12th:

* Sales team - ignored
* Support team - ignored
* Tech team - ignored
* **email to 50+ staff** - (after not receiving a reply, I emailed 50+ staff emails on the 21st of August) - ignored

Weeks of silence while their robots continued operating in hospitals and restaurants worldwide.

## The Nuclear Option

After being ignored by literally everyone at Pudu, I escalated. I emailed:

* **Skylark Holdings** (7,000+ restaurants in Japan)
* **Zensho** (massive restaurant chain operator)
* **Major Pudu distributors** (S.P.A.R.C, etc.)

I explained that anyone could control the robots in their facilities.

## The Instant "Discovery"

Within 48 hours of contacting their customers, Pudu miraculously discovered my emails! They responded with this obvious ChatGPT special:

```
Dear BobDaHacker

On behalf of Pudu Robotics, I would like to extend our sincere gratitude for taking the time to report the security vulnerability to us. We highly appreciate your efforts in following responsible disclosure practices and helping us make our systems more secure.

We have received your report and our security team has promptly investigated the issue you've outlined. We have a patch in development and expect to have this vulnerability remediated by the end of this week.

Additionally, as part of our ongoing commitment to security, we are planning to update numerous security components across our systems in the near future to further enhance our overall security posture.

We are treating this matter with the highest priority. We will keep you updated once the fix is fully deployed.

Once again, thank you for your valuable contribution to our security. If you have any further details or questions, please do not hesitate to reach out to me directly at [Your Email Address].

We appreciate your cooperation and look forward to potentially working with you in the future.

Sincerely
```

They couldn't even be bothered to replace the "[Your Email Address]" placeholder from their ChatGPT template. Peak effort right there.

"Promptly investigated" - after weeks of silence and ignored emails. "Responsible disclosure practices" - which they ignored until their revenue was threatened.

## Fixed in 48 Hours

Two days after sending that AI-generated response, they actually fixed everything. Amazing how fast you can move when Skylark Holdings knows their robot fleet is compromised.

## The Safety Implications

These aren't just restaurant robots:

* **Hospitals** use them for medicine delivery (the literal hospital of bangkok uses them etc)
* **Hotels** use them for room service
* **Offices** use them for document transport
* **Schools** use them in cafeterias

A compromised robot in a hospital could interfere with medicine delivery. In an office, it could steal documents. In a restaurant, it could cause chaos during rush hour.

## To Pudu Robotics

Your robots operate around vulnerable populations - hospital patients, elderly residents, children in schools. The fact that you only acted when revenue was at risk shows where your priorities lie.

Your "ongoing commitment to security" apparently doesn't include:

* Having a security contact
* Responding to vulnerability reports
* Basic API authentication
* Caring until customers complain
* Replacing placeholders in your ChatGPT responses

# Update: (2025-09-03)

After a Google Meet meeting with Pudu Robotics, I need to correct some misunderstandings in my original post:

**The Timeline:** Pudu didn't ignore my reports. They didn't receive my initial emails to sales/support, but once they saw my report through other channels, they immediately began working on fixes. They only contacted me once the fix was ready to deploy, which explains the timing.

**The First Response:** The '[Your Email Address]' placeholder was an unfortunate oversight during editing. However, in the full email, the Pudu team clearly stated, "We have a patch in development and expect to have this vulnerability remediated by the end of this week." This is the part from my blog's citation that was omitted.

**Their Response:** They actually treated this seriously from the moment they became aware of it. The delay in response was them fixing the issues, not ignoring them.

**Moving Forward:**

* Pudu is upgrading its SRC (PUDU Security Response Center) to more effectively handle issues.
* They already made a [[email protected]](/cdn-cgi/l/email-protection#c4b7a1a7b1b6adb0bd84b4b1a0b1b0a1a7aceaa7aba9) email
* We're exploring ongoing security collaboration

I was wrong to assume malice when it was actually a communication breakdown. Pudu does...
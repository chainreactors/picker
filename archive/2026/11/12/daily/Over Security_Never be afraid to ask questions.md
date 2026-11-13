---
title: Never be afraid to ask questions
url: https://blog.talosintelligence.com/never-be-afraid-to-ask-questions/
source: Over Security
date: 2026-11-12
fetch_date: 2026-11-13T09:07:21.313250
---

# Never be afraid to ask questions

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# Never be afraid to ask questions

By
[Amy Ciminnisi](https://blog.talosintelligence.com/author/amy-ciminnisi/)

Thursday, November 12, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week's edition of the Threat Source newsletter.

Back in college, I took an anthropology course called “Peoples and Cultures of Southeast Asia.” While the title sounded like your everyday anthro course, this one was a little different. It had fewer students, maybe around 10, and took place from 7 – 9 p.m., most college kids’ nightmare — but it was the perfect time of day to videochat with Malaysian students on the other side of the globe with a 12-hour time difference.

My university had a 14-week semester, while the university in Kuala Lumpur had seven weeks, so our class had time before meeting the students to study Malaysia’s pre- and post-colonial history, political climate, and cultural and religious dynamics; watch famous Petronas Deepavali and Chinese New Year [ads](https://www.youtube.com/watch?v=xfnWtMmLtus); and (of course) drool over pictures of nasi lemak and teh tarik.

When both classes began videochatting with one another (yeah, we used Zoom before it was cool), our questions were quite tame. This was partly because we were afraid of offending one another, and partly due to some thorny laws around political speech. They’d ask, “Where do you store your winter clothes during the summer? They’re so puffy!” or “How often do you eat at McDonald’s?” We’d ask, “What's your favorite food at pasar malams (night markets)?” and “How do you deal with the heat and humidity?” (The answer to that one: Malaysia, which is around the size of New Mexico, has around 1,000 shopping malls with heavenly air conditioning.)

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/11/Untitled-1-1.png)

Over the weeks, with encouragement from our professors, a few brave souls from both countries began to open up about their opinions on the government, social justice movements, discrimination, and more. Their vulnerability was contagious and soon encouraged others to speak up more in class, and everyone began to ask more pointed questions. They’d ask, “What is it like to be openly LGBT+ in the U.S.?” We’d ask, “Do you think the new political party gaining the prime ministership will bring more change?” We soon developed a class motto: **Never be afraid to ask questions.**

I firmly believe that questions asked in good faith create a space where it is safe to be curious, when everyone understands that the goal is understanding, not judgment. It’s perfectly fine to be honest about your lack of knowledge, and you’re always allowed to decline a question if the topic is too complex or personal to unpack in the moment.

I'm grateful to still carry this philosophy with me today. I work with Talosians from around the world, where diverse backgrounds and communication styles can make it easy to misinterpret intentions. But assuming positive intent, asking questions, and being appreciative of the answers ensures that everyone is aligned, respected, and heard. To take a page out of Bill’s book (pun intended)...

*“I wish we could all live in a big house with lots of rooms, and windows, and doors, and none of them locked.” – Ursula K. Le Guin*

*“I want to know why. Why everything. I don't know the answers, but a few days ago I didn't know there were questions.” – Terry Pratchett*

## The one big thing

Cisco Talos is breaking down a huge [Microsoft Patch Tuesday release](https://blog.talosintelligence.com/microsoft-patch-tuesday-for-november-2026/) for November 2026, which addresses 1,095 vulnerabilities across various products. This month's massive update features 64 critical flaws, 48 of which could allow for remote code execution (RCE). Most notably, Microsoft warned that a spoofing flaw in Microsoft Office Outlook (CVE-2026-124194) is already being actively exploited in the wild.

Additionally, don’t miss Google’s patch for a zero-day in Google Chrome’s XML component (CVE-2026-125350), released on Wednesday. The vulnerability is caused by a use-after-free memory management error that could allow a remote attacker to execute arbitrary code within Chrome's sandbox through a specially crafted HTML page. Google confirmed an exploit exists in-the-wild.

### Why do I care?

When a Patch Tuesday drops with over 1,000 vulnerabilities, it is easy to feel overwhelmed. However, the sheer volume shouldn't distract from the handful of flaws that actually require immediate attention. Address the most realistic threats to your environment first to avoid burning out your team.

### So now what?

Take a targeted, risk-based approach to this month's rollout. Start by addressing the actively exploited Outlook vulnerability (CVE-2026-124194), the Google Chrome vulnerability, and the critical RCEs in externally facing or core services like Exchange and Active Directory. To help protect your network and buy your team some time while patching, implement the new suite of Snort rules available in the [full blog post](https://blog.talosintelligence.com/microsoft-patch-tuesday-for-november-2026/).

## Top security headlines of the week

**Recently patched Barracuda vulnerabilities exploited in attacks**
Threat actors have started exploiting two recently patched Barracuda vulnerabilities that could be chained to bypass authorization controls and gain root access. ([SecurityWeek](https://www.securityweek.com/recently-patched-barracuda-vulnerabilities-exploited-in-attacks/))

**N-able took cloud platform offline after 30+ "zero-days" published**
N-able took its hosted N-central environments offline and urged on-premises customers to shut down their servers after a security researcher publicly disc...
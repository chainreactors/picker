---
title: Same Problem, Different Angles: When Red Team and Blue Team Actually Talk to Each Other
url: https://www.blackhillsinfosec.com/same-problem-different-angles/
source: Black Hills Information Security, Inc.
date: 2026-05-20
fetch_date: 2026-05-21T06:02:56.210642
---

# Same Problem, Different Angles: When Red Team and Blue Team Actually Talk to Each Other

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-consultants/)
  + [Admin Team](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [Active SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [Antisyphon Training](https://www.blackhillsinfosec.com/about/antisyphon/)
  + [BHIS Tribe of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://bhispodcasts.transistor.fm/)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

20
May
2026

[Active SOC](https://www.blackhillsinfosec.com/category/blue-team/active-soc/), [Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/)
[BHISinterviews](https://www.blackhillsinfosec.com/tag/bhisinterviews/), [Melissa Lauro](https://www.blackhillsinfosec.com/tag/melissa-lauro/), [purple teaming](https://www.blackhillsinfosec.com/tag/purple-teaming/), [Security Operations](https://www.blackhillsinfosec.com/tag/security-operations/), [SOC](https://www.blackhillsinfosec.com/tag/soc/)

# [Same Problem, Different Angles: When Red Team and Blue Team Actually Talk to Each Other](https://www.blackhillsinfosec.com/same-problem-different-angles/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/12/melissal-150x150.jpg)

| [Melissa Lauro](http://linkedin.com/in/melissarsl)

*Melissa is a content strategist with a 20-year background in writing instruction and editorial work across B2B and B2C industries. She joined the security world five years ago as a BHIS penetration-test report editor, helping her team to sharpen the structure and impact of every client report. Lately, she’s been digging into the stories behind BHIS’s tools, analysts, and culture—capturing narratives of how cybersecurity really works behind the scenes.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/05/redblue_header.png)

There is a certain kind of conversation that doesn’t get written up in a post-mortem, doesn’t generate a ticket, and never makes it into an end-of-quarter report. It happens on the margins—at a conference, in a hallway, or, in this case, at 30,000 feet above sea level. It’s the conversation where two people who are solving the same problem from opposite ends of the table finally sit down next to each other.

Hayden Covington, who leads SOC operations at Black Hills Information Security, had that conversation on a flight home from a security conference. The person sitting next to him was Beau Bullock, one of BHIS’s Senior Security Consultants. It was the first time they’d met in person.

What came out of it wasn’t a formal knowledge transfer or a structured debrief. It was just two people, curious about each other’s work, talking shop at altitude.

What I find interesting about that—and what I keep coming back to in this series—is how much of what makes BHIS’s culture work doesn’t happen inside a process. It happens in the spaces between.

## “We’re Solving the Same Problem From Different Sides”

To understand why that plane conversation mattered, it helps to understand why it’s rare.

In most cybersecurity organizations, red teams and blue teams don’t interact much. The separation is structural and, to a degree, intentional. Red teams run offensive engagements: they simulate real-world attackers, test assumptions, probe for weaknesses. Blue teams—SOC analysts, incident responders—monitor live environments, detect anomalies, and respond to what’s happening right now. Different objectives, different timelines, different pressure. The adversarial framing is even baked into the naming convention.

*Melissa:* Hayden, when you think about the relationship between the SOC and the red team at most companies, how would you describe it?

*Hayden:* “Honestly, most of the time, you’re just doing completely different jobs. There’s no built-in back-and-forth. No natural overlap.”

*Beau:* “On our side, we’re usually focused on a specific engagement. We’re trying to answer: Can we get in? How far can we go?”

*Hayden:* “And on our side, it’s, ‘What’s happening right now, and how fast can we stop it?’ Same domain. Different lenses and opposing technical goals.”

And in most companies, that’s where the relationship ends: cleanly separated, clearly defined, rarely questioned.

At BHIS, the line still exists—but it’s more permeable than most. Sometimes by design. Sometimes informally. Sometimes on an airplane.

## The Flight

*Melissa:* Tell me about actually sitting next to Beau for a few hours.

*Hayden:* “We had just wrapped up this big event, and on the flight back, I ended up sitting next to Beau. It was the first time I’d met him in person, actually. I’d heard great things and was kind of intimidated—but he’s super friendly. We just started talking shop.”

*Melissa:* What kind of things?

*Hayden:* “It was this perfect mix of casual and deeply technical. Beau was telling me about some stuff he was working on in cloud pentesting. And I’m sitting there taking mental notes—like, we need to make sure we can detect that. Then he’s like, ‘What are you guys str...
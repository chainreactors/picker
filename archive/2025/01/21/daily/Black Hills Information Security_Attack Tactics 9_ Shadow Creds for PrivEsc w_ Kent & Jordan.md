---
title: Attack Tactics 9: Shadow Creds for PrivEsc w/ Kent & Jordan
url: https://www.blackhillsinfosec.com/attack-tactics-9-shadow-creds-for-privesc-wrapup/
source: Black Hills Information Security
date: 2025-01-21
fetch_date: 2025-10-06T20:10:41.020702
---

# Attack Tactics 9: Shadow Creds for PrivEsc w/ Kent & Jordan

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
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
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
Jan
2025

[Informational](https://www.blackhillsinfosec.com/category/informational/), [Jordan Drysdale](https://www.blackhillsinfosec.com/category/author/jordan-drysdale/), [Kent Ickler](https://www.blackhillsinfosec.com/category/author/kent-ickler/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/)
[Active Directory](https://www.blackhillsinfosec.com/tag/active-directory/), [AD](https://www.blackhillsinfosec.com/tag/ad/), [penetration testing](https://www.blackhillsinfosec.com/tag/penetration-testing/), [Pentesting](https://www.blackhillsinfosec.com/tag/pentesting/), [Shadow Credentials](https://www.blackhillsinfosec.com/tag/shadow-credentials/)

# [Attack Tactics 9: Shadow Creds for PrivEsc w/ Kent & Jordan](https://www.blackhillsinfosec.com/attack-tactics-9-shadow-creds-for-privesc-wrapup/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/01/WC_wrap-up_W0014.png)

*This webcast was originally published on January 9, 2025.*

In this video, Kent Ickler and Jordan Drysdale discuss Attack Tactics 9: Shadow Credentials for Primaries, focusing on a specific technique used in penetration testing services at Black Hills Information Security. They delve into the intricacies of how this local privilege escalation method exploits features in Active Directory to gain unauthorized access. The talk also covers mitigation strategies for these types of attacks, emphasizing the importance of auditing and implementing security measures to prevent exploitation.

* The webcast focuses on the use of shadow credentials as a technique for local privilege escalation (LPE) in cybersecurity attacks.
* The technique of using shadow credentials exploits features in Active Directory rather than vulnerabilities, making it a complex but effective method for attackers.
* Defensive measures such as LDAP signing and channel binding are crucial to prevent abuse of shadow credentials in Active Directory environments.

## **Highlights**

## **Full Video**

## **Transcript**

**Jason Blanchard**

Hello everybody and welcome to today’s Black Hills Information Security webcast. My name is Jason Blanchard. I’m the content & community director here at Black Hills. We don’t have a traditional marketing team. We have a content and community team.

And what that means is we like to create content. We like to bring people together that also enjoy that content, give them a chance to talk to each other about that content. Which is why we have Discord. We have a lot of opportunities for you to get a chance to meet each other.

So we have Kent and Jordan here today doing Attack Tactics 9: Shadow Creds for PrivEsc.

So we have done attack tactics 1, 2, 3, 4, 5, 6, 7, 8 and now 9. I’ve been here for six years. I think we started with like four maybe when I got here six years ago.

So it’s been a long running series. We probably could do one a month if we wanted to. But right now we’re on attack tactics 9 and Kent and Jordan are going to do a deep dive in some of the attacks that we do here at Black Hills as far as our pen testing services.

Now if you ever need a pen test, Red Team, threat hunt, ANTISOC, which is continuous pen testing with your friendly apt group, then where to find us. And with that I’m going to turn it over to Kent and Jordan.

And if you need anything at all, ask in Discord. If you need anything beyond that, ask in Zoom. And we are happy that you’re here today. All right, Kent and Jordan, it’s all yours.

**Kent Ickler**

Thank you. Jason, you are one of the best. We appreciate everything you do, the community you’ve built and much love sir. Thank you.

**Jordan Drysdale**

Truly Jason, you’re great. Best. The best.

**Jason Blanchard**

Good lord.

**Jordan Drysdale**

So yeah, there have been eight of these prior and they very much are some of the methodology that we use at BHIS for some of our pen tests. Not all of them, not all of our methodologies. But today we’re going to be talking about one specific one that’s been up and coming.

In fact, if, you’ve watched some of our recent webcasts, one of them more recently noticed we talked about a specific attack vector and we kind of took it from the perspective of a detection and we went deep dive into how the detection works.

Now we’re going to deep dive into how the actual attack works.

**Kent Ickler**

Yeah, the detection there is relatively complicated. We’ll get there toward the end. We’ll talk about that for a moment. So on that webcast we did share some of this methodology with you as well.

But we flew through it, right? The intention of that webcast was to demonstrate detections, talked about defenses, why this is kind of relatively insidious attack vector being a feature and not a ...
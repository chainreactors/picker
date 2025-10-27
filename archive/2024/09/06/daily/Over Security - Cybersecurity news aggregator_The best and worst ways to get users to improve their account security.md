---
title: The best and worst ways to get users to improve their account security
url: https://blog.talosintelligence.com/threat-source-newsletter-sept-5-2024/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-06
fetch_date: 2025-10-06T18:28:37.858630
---

# The best and worst ways to get users to improve their account security

# Cisco Talos Blog

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

# The best and worst ways to get users to improve their account security

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, September 5, 2024 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

As most quality thoughts go, my most recent musing on security came about because of fantasy football.

I had to log into my Yahoo Sports account, which I admittedly only ever have to log in to, at most, three times a year for the one fantasy football draft I have on that platform each year and then the handful of other times my phone logs me out during the five months that I’m adjusting my lineups on a weekly basis.

Admittedly, I’d never thought much about the security of my Yahoo Sports account because I don’t have any sensitive information tied to it, and if someone did want to break in, they could probably do a better job of managing my team in that league than I have the past few years. It’s the old “out of sight, out of mind” compared to something like my work email account where I’m logging in every morning, or online banking which I’m using several times a week, and the knowledge that my financial wellbeing is tied to those account credentials.

But I have to give credit to Yahoo for how they handled my account being less secure. When I logged in, probably for the first time since January, this weekend, before it would even display my homepage or enter the fantasy draft, it took me to an account management page where it warned me that I was using a “less secure” password and still hadn’t enrolled in multi-factor authentication. It took me less than a minute to update my password to something more secure, and maybe another two minutes to enroll in passcode MFA.

![](https://blog.talosintelligence.com/content/images/2024/09/data-src-image-49ef3316-467f-44ba-ad90-ea4b51c77c0b.png)

The account management page also had some helpful information, such as how long it had been since my last password change, offering the ability to manage my password through a third-party app, and multiple options to set up MFA, including using the Yahoo Sports app directly (this is always more appealing to me than having to download yet another MFA app on my phone).

This also got me thinking about the ways in which I don’t like being asked or reminded to enroll in MFA. It never made any sense to me that sites would give users the option to click away from the screen when being asked to enroll in MFA — make it mandatory or don’t. Also, one of my biggest pet peeves in using the internet is when you confirm this is a personal device or “Remember Me” for the next time I log in and the site doesn’t, in fact, remember me, and I have to go through the same approval process multiple times in the same day.

Our friends at Cisco Duo also have a [few other great recommendations](https://duo.com/blog/best-practices-for-enrolling-users-in-mfa) for getting people to enroll in MFA, but in my opinion, mandatory enrollment is best enrollment. If I had never displayed that screen on Yahoo’s login page, I wouldn’t have even thought twice about how secure my account was. And seeing a red “!” next to my password gave off an immediate sign that my password needed to be improved, which is something I wish other sites would start doing.

It’s not like having my fantasy football login credentials compromised would be the end of the world, but when it comes to something more high stakes, there are a few small UI steps sites could take to help nudge us in the right direction.

## The one big thing

Threat actors are increasingly using a traditional [Red Teaming tool called MacroPack](https://blog.talosintelligence.com/threat-actors-using-macropack/) to create new malware payloads. These malicious files deliver multiple payloads, including the Havoc and Brute Ratel post-exploitation frameworks and a new variant of the PhantomCore remote access trojan (RAT). Several different actors are using this tactic based on files uploaded to VirusTotal that Talos analyzed. They are written in different languages and rely on different themes centered on different geographies, which leads us to believe these are disparate campaigns.

### Why do I care?

The threat of VBA macros has diminished since Microsoft prevented the execution of macros in Microsoft Office documents downloaded from the internet, but not all users are using the latest up-to-date Office versions and can still be vulnerable. MacroPack can generate several types of payloads packaged into different file types, including popular Office-supported formats, scripting files and shortcuts. The code generated by the framework has the following characteristics, making it more difficult to detect using file content signatures.

### So now what?

Talos released a new Snort rule set and several ClamAV signatures to detect and block the malicious files Talos analyzed as part of this research. Our blog post also has an in-depth breakdown of the four major themes used across these malicious documents, information that could be crucial to informing potential targets about these threats.

# Top security headlines of the week

**A new report from Google’s Threat Analysis Group found that Russia’s APT29 is exploiting some of the same vulnerabilities as two popular spyware vendors.** The analysis comes from watering hole attacks that researchers saw in the wild between November 2023 and July 2024 targeting Mongolian government websites. APT29, largely thought to be connected to Russia’s government, exploited the same vulnerabilities in Apple iOS WebKit and Google Chrome that two spyware vendors, Intellexa and NSO Group, are also known to use. The actor (also known as Cozy Bear and Midnight Blizzard) compromised the government-controlled websites to embed malicious ...
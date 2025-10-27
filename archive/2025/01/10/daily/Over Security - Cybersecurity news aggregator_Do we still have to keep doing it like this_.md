---
title: Do we still have to keep doing it like this?
url: https://blog.talosintelligence.com/do-we-still-have-to-keep-doing-it-like-this/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-10
fetch_date: 2025-10-06T20:10:17.066965
---

# Do we still have to keep doing it like this?

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

# Do we still have to keep doing it like this?

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Thursday, January 9, 2025 14:15

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to the first edition of the Threat Source newsletter for 2025.

Upon returning to work this week from my Lindt chocolate reindeer coma, my first task was to write this newsletter. As I stared at a blank template hoping for inspiration to suddenly strike, I did what any security professional should do at the start (and indeed any) time of year. I listened to Wendy Nather.

Legendary Security Hall of Famer Wendy recently gave the keynote at BSides NYC and the video has [just landed.](https://www.youtube.com/watch?v=CyWCaxe7yi0&feature=youtu.be) The theme? “When do we get to play in easy mode?” I.e why is security still so hard?

Wendy showed a list of the InfoSec Research Council’s “Hard Problems” list of 2005. Any of these sound familiar?

* Global scale identity management
* Insider threat
* Availability of time critical systems
* Building scalable secure systems
* Attack attribution and situational understanding
* Information provenance
* Security with privacy
* Enterprise level security metrics

If the toughest challenges we face in 2025 are also the same challenges we were dealing with twenty years ago, what hope is there?

If anything, security is harder today than it was then, due to all the added complexity. Wendy also pointed out the larger ripple effect of breaches today due to supply chains, stolen credentials up for sale, and shared infrastructure.

Jeez, Hazel, way to start 2025 on a massive downer.

However, something we can perhaps do more of this year is to go a bit easier on ourselves. If something you’ve been trying for a while isn’t working and is only leading to deeper frustrations, is it possible to come at it a different way?

One of Wendy’s recommendations on how to do just that uses the example of user awareness training. As she said in her keynote, it’s easy to get someone to click on a link (sorry to any bad guys reading this, but you’re not exactly carrying out rocket surgery with your phishing campaigns).

Getting 1000 people NOT to click on a link is infinitely harder. Wendy even said that she once worked in an organization where the people who attended cybersecurity awareness training were even MORE likely to click on malicious links. The theory being that these people really wanted to help the security team, and were more than happy to respond to emails asking them to test the strength of their passwords.

And that’s where social engineering, defender style, can come in. "People are your greatest asset, if you treat them that way."

I'm seeing a lot of "how to thrive in 2025!" posts right now. For anyone who isn't ready for that, or tired of it all, I just want to say, I'm right there with you. But if you're also feeling like it's "new year, same problems"  perhaps there's one thing that you can pick this year which has the potential to change that story.

[Wendy’s keynote](https://www.youtube.com/watch?v=CyWCaxe7yi0&feature=youtu.be) contains a bunch of insights for defenders on how to go about picking something to change or improve, from knowledge sharing, to hiring, to addressing complexity. I’m also looking forward to reading the upcoming National Academy of Science’s report on Cyber Hard Problems, of which Wendy is on the committee for.

I'd thoroughly recommend checking out the full keynote, if only to see Wendy [yielding a hammer in a moderately threatening manner.](https://www.youtube.com/watch?v=CyWCaxe7yi0&feature=youtu.be)

## The one big thing

Attacks in which malicious actors are deliberately installing known vulnerable drivers, only to exploit them later, is a technique referred to as Bring Your Own Vulnerable Driver (BYOVD).

Cisco Talos recently [published our research](https://blog.talosintelligence.com/exploring-vulnerable-windows-drivers/) into the real-world application of the BYOVD technique. We identified three major payloads used, as well as recent activity linked to ransomware groups.

### Why do I care?

With the wide availability of tools exploiting vulnerable drivers, exploitation has moved from the domain of advanced threat actors into the domain of commodity threats - primarily ransomware. Malicious actors use corrupted drivers to perform a myriad of actions that help them achieve their goals, such as escalating privileges, deploying unsigned malicious code, or even terminating EDR tools.

### So now what?

There are a few things we can do to mitigate the risks and detect potential campaigns using BYOVD technique. This could include enforcement of Extended Validation (EV) and Windows Hardware Quality Labs (WHQL) certified drivers, preventing risks associated with legacy drivers. If the blocking of all legacy drivers is not possible, employing the Windows Defender Application Control (Windows Security) drivers blocklist is recommended way to prevent the execution of known vulnerable drivers. Read more in the [Talos blog.](https://blog.talosintelligence.com/exploring-vulnerable-windows-drivers/)

## Top security headlines of the week

* CISA says there is ‘no indication’ of a wider government hack beyond the treasury, following the disclosure that the department had been the target of a “major incident” in December. [TechCrunch](https://techcrunch.com/2025/01/06/cisa-says-no-indication-of-wider-government-hack-beyond-treasury/)
* FireScam Android spyware campaign fakes the Telegram Premium app and delivers information-stealing malware. Researchers say this is a prime example of the rising threat of adversaries leveraging everyday applications. [Dark Reading](https://www.darkreading.com/cyberattacks-data-breaches/firescam...
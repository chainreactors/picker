---
title: The Fine Art of Frustrating the Adversary
url: https://blog.talosintelligence.com/the-fine-art-of-frustrating-the-adversary/
source: Over Security
date: 2026-10-01
fetch_date: 2026-10-02T07:49:25.094208
---

# The Fine Art of Frustrating the Adversary

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/09/CAM26-BlogHeader.jpg)

# The Fine Art of Frustrating the Adversary

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Thursday, October 1, 2026 06:00

[On The Radar](/category/on-the-radar/)

* For Cybersecurity Awareness Month, eight Cisco Talos researchers share practical ways defenders can frustrate adversaries at different stages of an operation.
* Deception techniques such as honeypot accounts, false infrastructure, and tarpits can slow adversaries down while giving defenders earlier opportunities to detect their activity.
* Behavioral detections, tighter control of legitimate remote-management tools, and clear boundaries around AI agents can make essential adversary actions more visible and easier to interrupt.
* Breaking dependencies between stages of an operation can prevent an adversary from reaching their next objective.

---

Years ago, Cisco Talos blocked an adversary’s command-and-control (C2) traffic. The adversary responded by tweeting, “Write a rule for your a\*\*.”

A fine endorsement of our work, if I’ve ever heard one.

Talos loves to see an adversary forced to change course. And if every alternative for them is slower, less stealthy, less reliable and more expensive? Chef’s kiss.

Adversaries rely on certain advantages. They look for environments where tools and infrastructure allow them to blend in with normal activity. They also look for employees who can be pressured into acting before they have time to think.

Strong cybersecurity defenses can change those conditions. They take away adversary choices and increase the risk attached to essential actions, forcing them to keep making new decisions. Each change of plan costs them time and resources, and may eventually cause them to give up and move to another target.

It also creates more opportunities for defenders to spot what they are doing.

For Cybersecurity Awareness Month, we’re exploring “the fine art of frustrating the adversary.” To kick us off, I asked researchers across Talos, covering all aspects of the attack chain, for the strongest recommendation they could give defenders to seriously frustrate a potential adversary in their environment, and what that action would prevent the adversary from doing next.

## Take away their choices

Many adversaries use techniques that succeed against a large number of organizations. This makes a lot of economic sense: An operation that depends on every potential target having an unusual configuration will not scale particularly well.

But it also creates an opportunity for defenders.

“By being unique and setting things up a little differently, you may be able to better defend your environment when they come knocking,” Pierre says.

For example, organizations can restrict which accounts are permitted to sign into their most critical servers, alert on connection attempts from unauthorized users, and closely monitor any changes to those restrictions. Different credentials or authentication methods can be required for particularly sensitive systems, while protected enclaves can provide increased monitoring around critical infrastructure.

Pierre also recommends that defenders “monitor (and alert) for any changes to administrative users or administrative groups.”

Of course, no amount of security measures makes an organization impenetrable, but they can make the common methods adversaries use much less dependable.

Deception can push that uncertainty even further.

“Affecting the attack earlier rather than later in the attack chain is best,” Martin says. “Better to stop an attack from happening than minimize the consequences after it has happened.”

Martin suggests creating honeypot email accounts using expired domains with addresses that have previously leaked, or developing fictional employee profiles and seeding their addresses in places where spammers and other adversaries are likely to discover them. Because these accounts have no legitimate users, messages sent to them can be treated with far greater suspicion. The activity can provide early tactical intelligence about malicious infrastructure, lures, and campaigns, allowing defenders to put protections in place before the same operation reaches genuine employees.

Martin signed off with this note: “Have fun creating some fake employees and executives.”

Nick sees a similar role for tarpits and other forms of deception.

“False servers, shares, user accounts and network space can all be used to confuse and slow down the attacker while providing opportunities for the defender to detect them,” he says.

The same principle is beginning to appear in attempts to slow automated systems.

“We’ve even seen some new movement in the tarpit space for slowing down AI by throwing huge amounts of incoherent text at scrapers to slow them down,” Nick explains.

Deception gives the adversary another problem: they can no longer be certain that what they have found is useful, or even real.

Plus, it can be a lot of fun.

## Detect what they cannot avoid

“Attackers have enormous flexibility in how they operate, but far less flexibility in what they ultimately need to accomplish,” Ryan says. “Good detection engineering exploits that asymmetry.”

Consider an adversary attempting to obtain privileged credentials. They might use Mimikatz, `comsvcs.dll`, direct access to LSASS memory, a custom utility or another implementation entirely. A detection focused too narrowly on one tool can be bypassed simply by replacing it. A detection built around the underlying attempt to access credential material leaves considerably less room to maneuver.

According to Ryan, creating resilient behavioral detections requires defenders to:

* Identify the adversary techniques that would have the g...
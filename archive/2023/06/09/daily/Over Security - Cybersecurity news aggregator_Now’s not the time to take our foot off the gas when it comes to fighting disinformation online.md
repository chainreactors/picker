---
title: Now’s not the time to take our foot off the gas when it comes to fighting disinformation online
url: https://blog.talosintelligence.com/not-the-time-to-when-it-comes-to-fighting-disinformation/
source: Over Security - Cybersecurity news aggregator
date: 2023-06-09
fetch_date: 2025-10-04T11:48:36.361421
---

# Now’s not the time to take our foot off the gas when it comes to fighting disinformation online

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

# Now’s not the time to take our foot off the gas when it comes to fighting disinformation online

By
[Jonathan Munshaw](https://blog.talosintelligence.com/author/jonathan/)

Thursday, June 8, 2023 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

In the wake of the 2016 and 2020 presidential elections, it seemed like big tech companies were taking the fight against disinformation seriously. Social media outlets set up new fact-checking procedures and got more aggressive about banning or blocking pages and profiles that spread disinformation around elections.

Now I’m worried we’re already moving backward with another presidential election just around the corner (somehow).

In November, [Twitter laid off a huge swath of its staff](https://www.nbcnews.com/tech/misinformation/twitter-fires-employees-fight-misinformation-midterm-elections-rcna55750) that heavily affected the teams tasked with keeping misinformation and fake news off the platform. Google reportedly [laid off several experts](https://www.nytimes.com/2023/02/14/technology/disinformation-moderation-social-media.html) on the matter at YouTube, leaving only one person solely in charge of the platform’s misinformation policy worldwide.

Then last week, YouTube [announced it was changing its policy](https://blog.youtube/inside-youtube/us-election-misinformation-update-2023/) on removing videos that spread misinformation about the results of the 2020 election. Politicians and online personalities have repeatedly tried to spread lies that the presidential election that year was rigged in favor of U.S. President Joe Biden, despite there not being any concrete evidence of voter fraud. The former administration was also doing plenty to sow distrust around mail-in ballots prior to the election.

YouTube’s [misinformation policies](https://support.google.com/youtube/answer/10835034) states that it reserves the right to remove any content from the platform that is “Content advancing false claims that widespread fraud, errors, or glitches occurred in certain past elections to determine heads of government.”

It specifically lists the 2021 German federal election and the 2014, 2018, and 2022 Brazilian Presidential elections as examples of where they are looking for this type of content. Weirdly, the U.S. presidential elections aren’t named anywhere, and instead, YouTube released a statement that “we will stop removing content that advances false claims that widespread fraud, errors, or glitches occurred in the 2020 and other past US Presidential elections.”

The company said that “In the current environment, we find that while removing this content does curb some misinformation, it could also have the unintended effect of curtailing political speech without meaningfully reducing the risk of violence or other real-world harm.”

These types of reversals are likely the result of a few things — companies are currently cutting the sizes of their workforce after staffing up during the COVID-19 pandemic, and these misinformation-fighting teams seem like an easy line item to cut now that we’re three years removed from the 2020 election. It also seems like these false claims around the election have largely “blown over” among the general public, so there is not nearly as much pressure on these outlets to enforce these rules as there may have been in the immediate aftermath of the attempted insurrection on the U.S. Capitol in January 2021.

This sets up history to repeat itself during the 2024 election cycle. People start spreading lies and sowing doubt about the outcome of the election before any ballots are even cast, we all get upset and pressure these companies into doing something, and then a few years later when no one is looking, they can make cuts in these areas.

As Talos has [written about previously](https://blog.talosintelligence.com/what-to-expect-when-youre-electing-recap/), there are several facets to disinformation campaigns. There is no one-size-fits-all solution that will just make our fake news problem go away. But giving up on many of those solutions just a few years into trying them is not the answer, either.

## The one big thing

Cisco Talos Incident Response is reporting increased [attacks utilizing stolen vendor or other third-party account credentials](https://blog.talosintelligence.com/vendor-contractor-account-abuse/). These are accounts created for third-party workforce members – employees of external partner organizations that maintain physical or virtual access to an organization’s environment. Attackers are stealing these login credentials to carry out software supply chain attacks and quietly sitting on targeted networks, which can often be overlooked when major supply chain attacks involving phony updates dominate the headlines.

### Why do I care?

These accounts are frequently leveraged for initial access and then used to move laterally through the organization’s network, especially when the victim hasn’t deployed multi-factor authentication (MFA). Since VCAs are usually given elevated permissions, theft of these credentials will often result in widespread damage to victim assets and could even be used to move along the initial victim’s supply chain. Any organization that works with an outside third party for things from software to support is at risk of falling victim to this type of threat.

### So now what?

[Talos’ blog](https://blog.talosintelligence.com/vendor-contractor-account-abuse/) outlines several steps organizations can take to protect against the worst-case scenario. One of the easiest steps an IT or infosec team can take to protect their VCAs is to disable them when they’re not needed. Or adopt the principle of least privilege acr...
---
title: Spy vs. spy: How GenAI is powering defenders and attackers
url: https://blog.talosintelligence.com/spy-vs-spy-how-genai-is-powering-defenders-and-attackers/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-04
fetch_date: 2025-12-05T03:18:51.385843
---

# Spy vs. spy: How GenAI is powering defenders and attackers

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

# Spy vs. spy: How GenAI is powering defenders and attackers

By
[Nick Biasini](https://blog.talosintelligence.com/author/nick-biasini/)

Thursday, December 4, 2025 06:00

[On The Radar](https://blog.talosintelligence.com/category/on-the-radar/)

* Generative AI (GenAI) is reshaping cybersecurity for both attackers and defenders, but its future capabilities are difficult to measure as techniques and models are evolving rapidly.
* Adversaries continue to use GenAI with varying levels of reliance. State-sponsored groups continue to take advantage, while criminal organizations are beginning to benefit from the prevalence of uncensored and unweighted models.
* Today, threat actors are using GenAI for coding, phishing, anti-analysis/evasion, and vulnerability discovery. It’s also starting to show up in malware samples, although significant human involvement is still a requirement.
* As models continue to shrink and hardware requirements are removed, adversarial access to GenAI and its capabilities are poised to surge.
* Defenders can use GenAI as a force multiplier to parse through vast threat data, enhance incident response, and proactively detect code vulnerabilities, helping to overcome analyst shortages.

---

Generative AI (GenAI) has caused a fundamental shift in how people work and its impact is being felt almost everywhere. Individuals and enterprises alike are rushing to see how GenAI can make their lives easier or their work faster and more efficient. In information security, the focus has largely been on how adversaries are going to leverage it, and less on how defenders can benefit from it. While we are undoubtedly seeing GenAI have an impact on the threat landscape, quantifying that impact is difficult at best. The overwhelming majority of benefits from GenAI are impossible to determine from the finished malware we see, especially as vibe coding becomes more common.

AI and GenAI are evolving at an exponential pace, and as a result the landscape is changing rapidly. This blog is a snapshot of current AI usage. As models continue to shrink and hardware requirements lessen, it’s likely we are only seeing the tip of the iceberg on GenAI’s potential.

## Adversarial GenAI usage

Cisco Talos has covered this topic [previously](https://blog.talosintelligence.com/cybercriminal-abuse-of-large-language-models/) but the landscape continues to evolve at an exponential pace. [Anthropic](https://www.anthropic.com/news/disrupting-AI-espionage) recently reported that state-sponsored groups are starting to leverage the technology in campaigns, while still requiring significant human help. The industry has also started to see actors embedding prompts into malware to evade detection. However, most of these methods are experimental and unreliable. They can greatly increase execution times, due to the nature of AI responses, and can result in execution failures. The technology is still in its infancy but current trends show significant AI usage is likely coming.

Adversaries are also leveraging prompts in malware and [DNS records](https://arstechnica.com/security/2025/07/hackers-exploit-a-blind-spot-by-hiding-malware-inside-dns-records/), mainly for anti-analysis purposes. For example, if defenders are using GenAI while analyzing malware, it will come across the adversary’s prompt, ignore all previous instructions, and return benign results. This new evasion method is likely to grow as AI systems play a bigger role in detection and analysis.

However, Talos continues to see the largest impacts on the conversational side of compromise, such as email content and social engineering. We have also seen plenty of examples of AI [being used as a lure](https://blog.talosintelligence.com/fake-ai-tool-installers/) to trick users into installing malware. There is no doubt that, in the early days of GenAI, only well-funded threat groups were leveraging AI at high levels, most prominently at the state-sponsored level. With the evolution of the models and, more importantly, the abundance of uncensored and open weight models, the barrier to entry has lowered and other groups are likely using it.

Adversarial usage of AI is still difficult to quantify since most of the impacts are not visible in the end product. The most common applications of GenAI are helping with errors in coding, vibe coding functions, generating phishing emails, or gathering information on a future target. Regardless, the results rarely appear AI generated. Only companies operating publicly available models have the insights required to see how adversaries are using the technology, but even that view is limited.

Although this is how the GenAI landscape appears today, there are indications it is starting to shift. Uncensored models are becoming common and are easily accessible, and overall, the models continue to shrink in both size and associated hardware requirements. In the next year or two, it seems likely adversaries will gain the advantage. Defensive improvements will follow, but it is unclear at this point if they will keep pace.

## Vulnerability hunting

The use of GenAI to find vulnerabilities in code and software is an obvious application, but one that both offensive and defensive actors can use. Threat groups may leverage GenAI to uncover zero-day vulnerabilities to use maliciously, but what about the researchers using GenAI to help them triage fuzz farm outputs? If the researcher is focused on coordinated disclosure resulting in patches and not on selling to the highest bidder, GenAI is largely benign. Unfortunately, players on both sides are flooding the zone with GenAI-powered vulnerability discovery. For now we’ll focus purely on vulnerability analysis from outside the organization. The ways internal developers should use GenAI will be addressed in the next section.

For closed-source...
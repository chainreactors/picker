---
title: The SOC Doesn't Need to Start Over with Every Alert
url: https://thehackernews.com/2026/09/the-soc-doesnt-need-to-start-over-with.html
source: The Hacker News
date: 2026-09-25
fetch_date: 2026-09-26T06:51:58.812240
---

# The SOC Doesn't Need to Start Over with Every Alert

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [The SOC Doesn't Need to Start Over with Every Alert](https://thehackernews.com/2026/09/the-soc-doesnt-need-to-start-over-with.html)

**The Hacker News**Sep 25, 2026Artificial Intelligence / Security Operations

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0sz5D5hiSWYuUfbRDYDloMNzbx5dpvVQjC5ZVoYzIgvWL_Tkyx8AjNHjZ27RAwaPbCIQXNWB6o_FYzxjimFYHY2pHfp6m6b97tARxhdhqSHBkp2lYpfekwVLvUIm63ruwsHR7RlQkR-2jfOPELG2hjZrrYr9JYr4ndSfVaYIajhTpmB6Ud0DIXz1D_uI/s1700-nu-rw-lo-l85-e365/soc-1.jpg)

Security leaders keep debating whether AI will produce an entirely new class of cyberattack. The nearer change is quieter and already visible: AI has made a failed attack cheap to retry.

The routine version looks like this. An attacker lands on a low-privilege cloud account, and the first try at privilege escalation goes nowhere. That dead end used to cost hours of documentation reading, permission checks, and script debugging, and plenty of operators simply got stuck. With a model in the loop, the error gets explained, the script gets fixed, and a fresh enumeration path is under test within minutes.

No step in that sequence is a new capability. Together they strip time, skill, and cost out of the unglamorous middle of an intrusion, the research and troubleshooting that sit between intent and outcome.

## **What the threat reporting shows**

The public record traces the arc. In early 2025, Google's Threat Intelligence Group found state-backed actors treating generative AI as a productivity tool: translation, scripting help, troubleshooting, research. By late 2025, the same team was writing about malware samples that phoned a model mid-execution and about a maturing underground market for illicit AI tools, while Anthropic disclosed shutting down an extortion operation that leaned on AI at nearly every stage, from reconnaissance and credential harvesting through to setting ransom demands. In May 2026, [GTIG reported](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access/) that cyber crime actors found a two-factor bypass in an open-source administration tool and built working exploits for it, and that based on the structure and content of those exploits it assessed with high confidence that an AI model supported both the discovery and the exploit development. GTIG worked with the affected vendor on disclosure and disrupted the activity, and its own assessment is that the counter-discovery may have prevented the exploit from being used.

That last distinction matters. Assessed AI assistance and a planned operation are not the same claim as confirmed deployment in the wild, and the difference tends to get lost once a finding like this starts circulating. Attribution is hard, prevalence is unclear, and none of these reports is a census of global activity. The direction is what counts, and the direction is toward AI sitting inside attacker workflows rather than beside them.

Provider guardrails deserve credit here. Safety classifiers and abuse disruption push the cost of misuse up, and the disruption cases above show the work paying off. A guardrail still lives outside the enterprise. An operator can poke at it until a reframed request slides through, move the job to an open-weight model, split one malicious task into a dozen innocent-looking ones, or wrap tooling around the model and route around the policy layer entirely. Friction of that kind slows misuse without ever becoming a security boundary, and an organization that treats provider policy as a boundary has substituted reassurance for defense.

## **Attacks run as loops**

Textbooks draw the attack lifecycle as a line: reconnaissance, access, escalation, impact. A working attacker runs a loop instead. Watch the environment, form a guess, try something, read what came back, adjust the guess. AI compresses the time between those steps. A novice stays in the game longer. An expert runs more experiments per day.

Defense is supposed to loop the same way. A signal fires, context gets gathered, a hypothesis forms, scope gets validated, an action lands, and the outcome feeds back into detection. In practice, queues and handoffs interrupt that loop at every joint. The alert idles unassigned. The identity picture lives in a different console. A telemetry gap turns into a backlog item, and the explanation behind a closed false positive dies in the ticket instead of reaching whoever owns the rule.

The environment answers the attacker's experiment in seconds. The defender's answer arrives whenever the ticket gets picked up.

Mean time to acknowledge and mean time to remediate hide this. An alert can be acknowledged in minutes and then spend hours being reconstructed: finding the right identity, confirming whether the endpoint was managed, restating the incident to each new owner along the approval path. That reconstruction interval is decision latency, and few SOCs measure it at all.

## **Five things every handoff drops**

The work is commonly described in five functions: threat intelligence, threat hunting, detection engineering, investigation, and remediation. That is a useful lens rather than a universal org chart. In a small team, one person wears several of those hats. In a large enterprise they spread across the SOC, identity, endpoint, cloud, and business teams, and an MDR provider may own the investigation without owning the authority to contain.

The functions are rarely the problem. The transfer between them is. Threat intelligence understands why a technique matters. Threat hunting can say where it would surface. Detection engineering carries the rule's unstated assumptions. The investigator holds the evidence trail that settled the verdict. The team that acts can name the actions that would break the business. Each transfer squeezes that knowledge into an indicator, an alert, or a ticket, and the squeeze is lossy.

This is [the lossy handshake](https://www.co...
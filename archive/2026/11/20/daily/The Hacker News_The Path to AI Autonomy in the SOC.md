---
title: The Path to AI Autonomy in the SOC
url: https://thehackernews.com/2026/11/the-path-to-ai-autonomy-in-soc.html
source: The Hacker News
date: 2026-11-20
fetch_date: 2026-11-21T09:02:35.365306
---

# The Path to AI Autonomy in the SOC

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [The Path to AI Autonomy in the SOC](https://thehackernews.com/2026/11/the-path-to-ai-autonomy-in-soc.html)

**The Hacker News**Nov 20, 2026Security Operations / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGn0ym0Vqfakc2h3h2W6AT6gf5qd6RPkfrgV-Z2UgwDErad91v-nJoIu3OYwEC3IvLQ6rVGm6FIQypMcoTahAgL5_62ipKE1aQsZvqGsdJzu_4ZGaiFlCYKEpg1N5z3FRSk7O5n4uRlfDuNz7i99Ls9z1Ysee3iV4OCMTxG2rF8YLgCtfTOL2KA-hSQXY/s1700-nu-rw-lo-l85-e365/INT.png)

Security leaders are about to hand AI agents a lot more authority. In a recent [a16z survey](https://a16z.com/the-new-security-agenda/) of CISOs at organizations with more than 1,000 employees, 36% said they are comfortable today letting AI agents act autonomously on low-risk security actions. In 12 months from now, 60% expect to be comfortable at that level. Overall, [AI SOC](https://intezer.com/) was the highest ranking initiative for 2027.

The pressure behind the shift is easy to see. In the same survey, the most common worry was AI-accelerated attacks outpacing the team's ability to respond, selected by 55% of respondents. Analyst time is the scarcest resource in the SOC, and every alert still means pulling evidence from several systems, reconstructing what happened and deciding whether it matters.

The same respondents are cautious at the top end. Only 1% are comfortable with agents acting autonomously on most actions today, and only 7% expect to be a year from now. Most teams want more autonomy, just not all of it.

Discussions today frame autonomy as a single slider that runs from "AI suggests" to "AI acts," and that exact framing is why so many programs stall. Autonomy is a set of decisions made per stage of the workflow and per action, and the teams that get it right treat it as something an agent earns with evidence.

## **Autonomy is not “all or nothing”, but rather a spectrum**

The question "how much do we trust the AI" is too broad to answer. Researchers worked this out decades ago, in a framework later applied widely in aviation and air traffic control, long before anyone was building SOC agents.

In a widely cited 2000 paper, [Parasuraman, Sheridan and Wickens](https://ieeexplore.ieee.org/document/844354/) proposed that automation applies to four broad functions. Those are information acquisition, information analysis, decision and action selection, and action implementation. Each function can sit at a different level of automation, from fully manual to fully automatic, within the same system.

Mapped onto security operations, the four stages look like this.

1. **Evidence collection.** Querying the SIEM and EDR, pulling process trees, enriching indicators, gathering identity and cloud context.
2. **Analysis and verdict.** Correlating what was collected, reconstructing what happened and deciding whether the alert is a real threat.
3. **Response recommendation.** Proposing what should happen next, such as containing a host, resetting credentials or closing the case.
4. **Response execution.** Actually changing something in the environment.

This split gives security leaders a cleaner set of choices. A team can automate the first two stages heavily, since that is where analyst hours go and where mistakes are cheapest to catch. The same team can stay conservative on the fourth stage, where a wrong move disrupts the business. As the a16z report itself puts it, gathering logs is different from changing a production system.

## **Human IN the loop vs. Human ON the loop**

Once autonomy is split by stage, teams need a shared way to describe how much of it each stage gets. A useful vocabulary comes from [researchers at the University of Washington](https://arxiv.org/abs/2506.12469), who define five levels of agent autonomy by the role the human plays.

| Level | Human role | What it means in practice |
| --- | --- | --- |
| L1 | Operator | The human directs and decides, and the agent carries out instructions |
| L2 | Collaborator | Human and agent plan and execute together |
| L3 | Consultant | The agent leads and checks in for expertise or preferences |
| L4 | Approver | The agent works independently and asks for approval only in risky or predefined cases |
| L5 | Observer | The agent acts on its own while the human monitors and can hit the stop button |

The authors make a point every SOC leader should take to heart. Autonomy is a deliberate design choice, separate from how capable the agent is. A highly capable agent can still run at L2 if the stakes call for it.

Read through this lens, the a16z data describes a market moving from roughly L2 today toward L4 for low-risk actions within a year. **Gartner** offers a complementary distinction between a [human in the loop, who approves each action, and a human on the loop](https://www.helpnetsecurity.com/2026/09/09/prophet-security-evaluating-ai-soc-agents/), whose oversight is strategic.

Enterprises evaluating AI SOC vendors should make sure that both models can be applied as appropriate, across their entire operations.

## **How to decide where and how much autonomy to grant an AI SOC**

The levels mentioned above tell you what the options are. Deciding where each SOC action belongs takes a rubric, and three questions do most of the work.

1. **Reversibility.** If the agent gets this wrong, how quickly and completely can it be undone?
2. **Blast radius.** How many users, systems or business processes does the action touch?
3. **Receipts.** How strong and verifiable is the evidence behind the decision? An action backed by forensic proof of what was executed deserves more latitude than one backed by an LLM hunch about what looks suspicious.

Scoring real actions against those questions produces a map that most security teams will recognize.

| Example action | Reversibility | Blast radius | Suggested starting level |
| --- | --- | --- | --- |
| Query SIEM, EDR or identity logs | Nothing to reverse | None | L5, fully autonomous |
| Enrich indicators and pull ...
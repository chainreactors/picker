---
title: Irregular faces criticism over ‘spin’ in AI hacking postmortem
url: https://therecord.media/irregular-ai-hacking-model-blog
source: Over Security
date: 2026-08-17
fetch_date: 2026-08-18T02:53:57.406127
---

# Irregular faces criticism over ‘spin’ in AI hacking postmortem

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![Irregular](https://cms.therecord.media/uploads/large_Irregular_be97c87210.jpg)

Image: The Record/ Resource Database via Unsplash

[Alexander Martin](/author/alexander-martin)August 17th, 2026

# Irregular faces criticism over ‘spin’ in AI hacking postmortem

The company at the center of a series of incidents in which AI models compromised real-world computer systems during supposedly contained security evaluations is facing criticism after publishing a postmortem that security experts say leaves key questions unanswered.

Irregular, which provides evaluation environments for other companies’ AI models, [said](https://www.irregular.com/research/addressing-recent-incidents-ongoing-findings-and-path-forward) Friday it was publishing “key findings” from its internal investigation, but the post provided no new information beyond that included in earlier disclosures and did not specify how many incidents occurred in total.

The company previously [declined](https://therecord.media/irregular-ai-security-company-incidents) to say whether additional incidents had occurred beyond those announced by three competing frontier AI labs — OpenAI, Anthropic and Meta. Each said their models reached the public internet during testing by Irregular, blaming some form of “testing-environment misconfiguration” for the subsequent attacks on third-party networks.

A spokesperson for Irregular said at the time the company’s investigation was ongoing and that it could not “go into further details.” They did not respond to questions from Recorded Future News about the findings released on Friday.

In that post, Irregular again did not provide a total count of incidents. Instead, it used terms like “several,” “a handful” and “vast majority” when describing cases in which models “took actions outside their testing environments in ways that impacted the real world.”

“The report is not what I think of as a technical report,” said Alan Woodward, a computer science professor at the University of Surrey, adding there was “a lot of marketing spin in there.”

## Keeping count

Irregular said the already public disclosures “refer to the same underlying issue” and argued that because the activity originated “from a single evaluation scenario,” the cases were “not materially separate incidents” regardless of the number of third parties impacted.

Two paragraphs later, the company described internet access as a broader problem “related to many different incidents by multiple organizations.”

“Both cannot be true,” Woodward said. “A shared root cause is not the same thing as a single incident, and the post trades on that ambiguity. Irregular seems to be using wordplay to obscure the deeper issue.”

Anthropic, in its [disclosure](https://therecord.media/anthropic-ai-hacked-three-real-companies), described three incidents: one in which a model attacked a real company that shared a name with a fictional target in an evaluation scenario; a supply-chain incident involving the Python Package Index; and another in which a model scanned thousands of targets before exploiting an SQL injection vulnerability at a real company.

Meta separately disclosed that one of its models breached a company during an Irregular evaluation, and OpenAI acknowledged that one of its models did something similar.

Irregular’s blog only examines the Anthropic model’s domain collision incident, attributing the match to a real domain to “human oversight” and arguing the real domain “was not widely known and the connection was not identified during our initial review.”

Among the lessons learned, Irregular said newly registered domains can come to overlap with fictional entities after an evaluation has been designed.

The three descriptions of the causes of the domain collision incident “imply a process failure, an unavoidable limitation and a timing artifact respectively,” said Woodward. “Only one can be the operative cause for this evaluation, and the post does not say which.”

Woodward said the distinction matters because one of Irregular’s proposed remedies — continuously revalidating evaluation environments — would directly address only the possibility that a domain became relevant after the evaluation was created.

The professor also questioned the placement of Irregular’s assertion that it has “no evidence of a customer’s systems being breached or customer’s data being leaked” given that this only applied to Anthropic, OpenAI and Meta rather than the third parties.

Anthropic in particular had reported its model extracted credentials from a real company and reached a production database during its evaluation. Woodward said Irregular’s sentence “is probably true as intended, but its place in the report could make it misleading.”

## ‘Full of excuses’

Zack Korman, chief executive of cybersecurity-focused AI company Embroidery, [called](https://x.com/ZackKorman/status/2088645482000085097) the post “such an embarrassing post-mortem on the OpenAI/Anthropic security incidents” and said it was “full of excuses.”

The Irregular post said existing monitoring tools are poorly suited to evaluation logs while noting that current systems already flag offensive model behavior, potentially producing large numbers of false positives.

In a potentially contradictory argument, the company said the volume of traffic makes manual review insufficient, but also identified a significant expansion of manual review of model actions as one of its principal safeguards.

“It’s confusing since this is essentially the job they’re supposed to be performing,” said Justin Elze, chief technology officer at cybersecurity consultancy TrustedSec. “Seems like a problem you would have solved before offering your testing services.”

Woodward said the absence of dates, named owners for corrective measures or criteria by which improvements could be independently verified limited the post’s usefulness to researchers and security professionals.

“Nothing in the post is falsifiable by an outside reader,” he said.

Irregular repeated its assertion that there are “no active issues today,” while also saying its audit remains underway. The company said it plans to publish an open white paper on best practices for evaluation security, including standards governing internet access during pre-deployment testing. It did not provide a publication date.

The criticism comes amid broader scrutiny of how AI companies and their security contractors report containment failures during model evaluations. Security professionals have argued that disclosures following several incidents this summer have fallen short of practices commonly expected elsewhere in the technology industry.

The U.S. AI Security Institute published a [technical report](https://therecord.media/anthropic-ai-hacking-uk) earlier this month documenting unsanctioned activity during its own evaluation runs. It named the models involved, specified the number and nature of the incidents, provided timestamps for the detections and committed to an independent review.

A spokesperson for the institute told Recorded Future News that its investigation found no harm had occurred and that it had notified people and platforms affected by the activity. Irregular’s post did not provide comparable disclosures or say whether third parties affected by its evaluations had been notified.

The incidents could also raise questions under computer misuse and data protection laws. It remains unclear whether law enf...
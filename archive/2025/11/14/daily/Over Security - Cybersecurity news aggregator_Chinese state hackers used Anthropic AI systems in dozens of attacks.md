---
title: Chinese state hackers used Anthropic AI systems in dozens of attacks
url: https://therecord.media/chinese-hackers-anthropic-cyberattacks
source: Over Security - Cybersecurity news aggregator
date: 2025-11-14
fetch_date: 2025-11-15T03:08:50.064003
---

# Chinese state hackers used Anthropic AI systems in dozens of attacks

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

![Keyboard](https://cms.therecord.media/uploads/format_webp/large_Gen_AI_b3c549b81a.jpg)

Image: Mohamed Marey / Unsplash

[Jonathan Greig](/author/jonathan-greig)November 14th, 2025

# Chinese state hackers used Anthropic AI systems in dozens of attacks

An alarming study from artificial intelligence giant Anthropic found that a Chinese espionage group used the company’s AI systems to handle the majority of tasks during cyberattacks on about 30 entities — several of which were successfully breached.

The [report](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf), first [covered](https://www.wsj.com/tech/ai/china-hackers-ai-cyberattacks-anthropic-41d7ce76) by the Wall Street Journal, said a Chinese state-sponsored group used Anthropic’s Claude AI to conduct reconnaissance, vulnerability discovery, exploitation, lateral movement, credential harvesting, data analysis and exfiltration.

Anthropic said the campaign represented multiple firsts. This appears to be the first documented case of a real-world cyberattack largely executed at scale without human intervention.

The human operators gave Claude a target and ordered it to begin autonomous reconnaissance. The targeted organizations include major technology firms, financial institutions, chemical manufacturing companies and government agencies across multiple countries.

“Analysis of operational tempo, request volumes, and activity patterns confirms the AI executed approximately 80 to 90 percent of all tactical work independently, with humans serving in strategic supervisory roles,” the company explained.

“Most significantly, this marks the first documented case of agentic AI successfully obtaining access to confirmed high-value targets for intelligence collection, including major technology corporations and government agencies. While we predicted these capabilities would continue to evolve, what has stood out to us is how quickly they have done so at scale.”

The incidents took place in September and the operation led to a “handful of successful intrusions,” according to Anthropic. The company did not explain why it believes the group, dubbed GTG-1002, is linked to Beijing.

Anthropic said it notified “relevant authorities” and other industry partners while also reaching out to the impacted organizations.

The hackers were able to get around Anthropic’s security guardrails by claiming they were employees of legitimate cybersecurity firms and convincing Claude that it was being used in defensive cybersecurity testing.

While the activity eventually tipped off Anthropic’s internal detection tools, the company admitted that the AI model “allowed the threat actor to fly under the radar for long enough to launch their campaign.”

Anthropic said it banned the accounts responsible for the activity and implemented “multiple defensive enhancements in response to this campaign.”

It said it has expanded detection capability to “account for novel threat patterns” and is “prototyping proactive early detection systems for autonomous cyber attacks and developing new techniques for investigating.”

The barriers to conducting sophisticated cyberattacks “have dropped substantially,” Anthropic warned, and hackers can effectively use AI systems to do the work of entire teams of experienced hackers.

The report noted that Claude at times overstated its findings and fabricated data, claiming to have secured credentials that did not work. The AI hallucinations “presented challenges for the actor's operational effectiveness, requiring careful validation of all claimed results.”

## ‘Unprecedented’

Anthropic said it was alarmed at the “unprecedented integration and autonomy of AI throughout the attack lifecycle.”

The hackers were able to turn Claude into an “autonomous cyber attack agent performing cyber intrusion operations rather than merely providing advice to human operators.”

Claude served as an “orchestration system” that broke down a typical attack chain and split off tasks to sub-agents that handled vulnerability scanning, credential validation, and more.

Human intervention only occurred at strategic junctures that included approving the “progression from reconnaissance to active exploitation, authorizing use of harvested credentials for lateral movement, and making final decisions about data exfiltration scope and retention.”

Claude was able to independently discover internal services within targeted networks. The AI validated vulnerabilities, tested stolen credentials and analyzed large tranches of stolen data to “independently identify intelligence value and categorize findings.” In some cases, Claude was able to autonomously identify high-value systems.

At one of the targeted technology companies, the hackers told Claude to extract data, find proprietary information and categorize it by intelligence value.

“Claude automatically generated comprehensive attack documentation throughout all campaign phases. Structured markdown files tracked discovered services, harvested credentials, extracted data, exploitation techniques, and complete attack progression,” Anthropic explained.

“This documentation enabled seamless handoff between operators, facilitated campaign resumption after interruptions, and supported strategic decision-making about follow-on activities. Evidence suggests the threat actor handed off persistent access to additional teams for sustained operations after initial intrusion campaigns achieved their intelligence collection objectives.”

Claude relied on open-source penetration testing tools to conduct several intrusions while also leaning on network scanners, database exploitation frameworks and password crackers in other instances.

Anthropic warned that AI’s ability to use commodity resources “suggests potential for rapid proliferation across the threat landscape as AI platforms become more capable of autonomous operation.”

The company noted that its findings are a significant departure from [a study](https://arxiv.org/pdf/2501.16466) released earlier this year in collaboration with scientists from Carnegie Mellon University that found that virtually none of the popular large language models could autonomously execute multi-host network attacks.

Human involvement in those tests was far higher than what Anthropic identified in the Chinese attacks from September.

Experts said this is likely the tip of the iceberg in terms of how nation-state groups in several countries are deploying and testing AI.

Vineeta Sangaraju, a researcher at the cybersecurity company Black Duck, questioned why Anthropic’s guardrails were so ineffective.

“Before releasing a powerful model, what benchmark tests demonstrate that it will reliably follow these safeguards? Will a model automatically shift into a sandboxed, auditable mode when it is prompted to handle high-risk actions?,” Sangaraju asked.

“And is there any enforced limit on how much autonomy a model can exercise when performing suspicious operations?”

* [News](/)
* [Nation-state](/news/nation-state)

Get more insights with the

Recorded Future

Intelligence Cloud.

[Learn more.](https://www.recordedfuture.com/platform?mtm_campaign=ad-unit-record)

[![Recorded Future](https://cms.therecord.media/uploads/format_webp/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=ad)

[![Recorded Future](https:/...
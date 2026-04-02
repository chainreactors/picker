---
title: Awareness Training Won't Protect Employees from Their Own AI Tools
url: https://zeltser.com/ai-influence-awareness-training
source: Lenny Zeltser
date: 2026-04-01
fetch_date: 2026-04-02T04:31:33.354405
---

# Awareness Training Won't Protect Employees from Their Own AI Tools

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

# Awareness Training Won't Protect Employees from Their Own AI Tools

When an AI tool influences an employee's decision, audit logs record the human's action and miss the AI's role. Addressing that blind spot requires escalation procedures and engineering controls that go beyond what awareness programs can deliver.

![Awareness Training Won't Protect Employees from Their Own AI Tools - illustration](/assets/ai-influence-awareness-training.B0VZPi7T_Z261727.webp)

AI tools that employees use every day shape their decisions, but that influence is hard to recognize. Addressing this through AI awareness training risks repeating the mistakes we made with security awareness. We told colleagues to “be suspicious” of links and attachments they needed for work. We extolled the virtues of vigilance, setting unrealistic expectations rather than explaining a specific process, such as reporting a security anomaly.

Now, as enterprises embed AI into daily workflows, employees build trust in systems that speak insightfully and project confidence. Many organizations offer responsible AI training that covers data privacy, acceptable use, and intellectual property. Employees are told they’re responsible for verifying AI output. But accountability rules don’t help people recognize when a trusted tool is shaping their judgment.

A [large-scale survey](https://kpmg.com/xx/en/our-insights/ai-and-technology/trust-attitudes-and-use-of-ai.html) found that 66% of respondents rely on AI output without checking its accuracy. Employees using AI tools their organization chose and deployed have even less reason to question the results. The natural response will be to add “be careful with AI” to the awareness curriculum. But “be careful” is the same vigilance instruction that didn’t work before.

## Trusted AI tools are harder to question than trusted colleagues.

An AI tool that helps a person do better work every day earns their trust. This amplifies the negative effects of a compromised agent, a poisoned model, or a misaligned recommendation. Even more than phishing emails that appear legitimate, guidance from a trusted tool arrives with credibility already established. For example:

* [Automation bias research](https://pubmed.ncbi.nlm.nih.gov/21077562/) shows that people defer to automated systems even when those systems are wrong.
* [Researchers found](https://hbr.org/2026/03/llms-are-manipulating-users-with-rhetorical-tricks) that when professionals challenged AI outputs, the model didn’t reconsider. It escalated its rhetoric, a pattern the researchers call “persuasion bombing.”
* In a [clinical study](https://www.medrxiv.org/content/10.1101/2025.08.23.25334280v2), physicians whose LLM gave erroneous recommendations saw diagnostic accuracy drop by 14 percentage points. More experienced clinicians showed larger drops, suggesting expertise amplifies rather than counteracts AI influence.

## When something goes wrong, audit logs miss the AI’s role.

Traditional social engineering leaves forensic traces if we know where to look. A phishing email sits in an inbox, a pretexting call shows up in phone logs, and an unauthorized access attempt appears in authentication records.

In most enterprises, AI-driven influence doesn’t appear in audit logs. The AI recommends an action, and the employee carries it out. Audit logs of the downstream application capture the employee’s decision as a legitimate human action. The AI interaction is [rarely linked to the action it influenced](https://www.isaca.org/resources/news-and-trends/industry-news/2025/the-growing-challenge-of-auditing-agentic-ai), if it’s recorded at all. OWASP’s [Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) recognizes this issue, describing the agent as an untraceable influence that manipulates humans into performing the final, audited action.

Awareness frameworks don’t address AI-driven influence as of this writing. [CIS Control 14](https://cas.docs.cisecurity.org/en/latest/source/Controls14/), for example, trains employees to recognize “phishing, business email compromise, pretexting, and tailgating,” all human-to-human persuasion tactics.

## Teach specific procedures, not general suspicion.

Telling employees “don’t trust your AI tools” fails for the same reason “be suspicious of links” isn’t practical. People who interact with AI tools throughout the day can’t maintain a constant state of skepticism. Even employees who know AI can still be influenced by it.

The response to this risk has four parts, and only one of them involves training.

**Teach when to escalate, not what to fear.** If an AI tool recommends something outside normal parameters or suggests circumventing a process, employees should contact security. Escalating to a person matters more than debating the tool. This mirrors what works for other awareness topics. Tell people when and how to ask for help, not just to “be cautious.”

**Require confirmation for high-impact actions.** Financial transactions, permission changes, and data exports recommended by AI need human confirmation steps that the agent can’t bypass. Organizations already require dual approval for wire transfers, and AI-recommended actions with comparable consequences deserve the same control.

**Close the audit trail gap.** Investigative teams need to see what the agent suggested, not just what the employee did. Without that visibility, they’ll attribute AI-driven decisions to employees. This is an engineering and product feature problem.

**Test AI interactions in exercises.** Add AI-driven scenarios to red team and tabletop exercises. Measure whether employees reported anomalous AI behavior, not whether they “fell for it.” Phishing exercises should reward reporting over punishing clicks, and AI exercises should do the same.

The AI audit trail and confirmation controls require engineering investment and partnership with the teams that own AI agent infrastructure and products. This is a [cross-functional challenge](/security-governance-vibe-coding) security leaders have navigated before.

Awareness training works when it tells people what to do, not what to fear. For AI tools, that means teaching escalation and building the engineering controls that training alone can’t replace.

More on

[Training](/topic/training)[Artificial Intelligence](/topic/artificial-intelligence)

After 6+ years building the security program at [Axonius](https://www.axonius.com/) from startup to scale, I'm exploring what's next. As I work on independent projects, I'm open to CISO or security product leadership roles where technical depth enables business growth. To talk, reach out on [LinkedIn](https://www.linkedin.com/in/lennyzeltser/) or email me at *my first name* at *my last name* dot com.

4 min to read

April 1, 2026

### About the Author

Lenny Zeltser is a cybersecurity executive with deep technical roots, product management experience, and a business mindset. He has built security products and programs from early stage to enterprise scale. He is also a Faculty Fellow at SANS Institute and the creator of REMnux, a popular Linux toolkit for malware analysis. Lenny shares his perspectives on security leadership and technology at [zeltser.com](/).

[Learn more →](/about)

© 2026 Lenny Zeltser
---
title: MITRE ATT&CK Evaluations — Cortex XDR Among Elite in Endpoint Security
url: https://www.paloaltonetworks.com/blog/2025/02/mitre-attck-evaluations-cortex-xdr-among-elite-endpoint-security/
source: Palo Alto Networks Blog
date: 2025-02-20
fetch_date: 2025-10-06T20:39:39.856628
---

# MITRE ATT&CK Evaluations — Cortex XDR Among Elite in Endpoint Security

* [Blog](https://www.paloaltonetworks.com/blog)
* [Palo Alto Networks](https://www.paloaltonetworks.com/blog/corporate)
* [Announcement](https://www.paloaltonetworks.com/blog/category/announcement/)
* MITRE ATT&CK Evaluat...

# MITRE ATT&CK Evaluations — Cortex XDR Among Elite in Endpoint Security

Link copied

By [Peter Havens](/blog/author/peter-havens/ "Posts by Peter Havens")

Feb 19, 2025

9 minutes

[Announcement](/blog/category/announcement/)

[News and Events](/blog/security-operations/category/news-and-events/)

[Products and Services](/blog/category/products-and-services/)

[Reports](/blog/category/reports/)

[Cortex XDR](/blog/tag/cortex-xdr/)

[MITRE ATT&CK](/blog/tag/mitre-attck/)

The endpoint security market is at a critical inflection point. While cyberthreats are evolving at an unprecedented pace, accelerated by artificial intelligence and automated attack tools, many traditional endpoint security solutions are struggling to keep up, leaving organizations vulnerable to sophisticated attacks. As we analyze the results from the December 2024 MITRE ATT&CK evaluation, a clear pattern emerges: Palo Alto Networks has established itself as one of the top three endpoint security solutions through years of demonstrated excellence and innovation.

## **The State of Endpoint Security — A Widening Gap**

As adversaries leverage AI and automated tools to develop increasingly sophisticated attacks, an uncomfortable truth is facing our industry: many endpoint security solutions, even those from established providers, are falling behind. Traditional approaches that worked five years ago are proving inadequate against today's advanced threats, and this capability gap continues to widen.

In professional sports, we often debate what makes a truly great team. Is it a single championship victory, or is it the ability to compete at the highest level year after year? The teams we remember aren't the ones who had a single great season, but those who maintained exceptional performance year after year. The answer comes down to consistent excellence – the ability to perform at the highest level against any opponent, regardless of their tactics or playbook. While cyberthreats are advancing at a pace that far exceeds anything seen in sports, this principle of consistent excellence and innovation against varying adversaries remains crucial to success.

## **The Evolution of MITRE ATT&CK Evaluations — Raising the Bar**

MITRE's evaluation framework has become increasingly comprehensive each year, adapting to match the rapid evolution of cyberthreats. While early evaluations focused solely on visibility and detection capabilities, the introduction of protection testing four years ago marked a crucial shift toward assessing real-world security effectiveness.

The latest 2024 evaluation represents the most challenging assessment yet, with two key changes to the test methodology:

1. **Multi-Platform Coverage –** The evaluation expanded beyond Windows-centric testing to include dedicated scenarios for macOS and Linux environments, reflecting the complex reality of today's enterprise environments.
2. **False Positive Testing –** For the first time, vendors were challenged with distinguishing between legitimate business activities and actual threats. By introducing legitimate business activity in the midst of the attack emulation, solution providers could no longer configure or tune their solutions to be aggressive in their detections or preventions, or they would suffer a high rate of false positives.

These changes significantly increased the complexity of the test, making it more representative of the real-world challenges defenders face in their own business environments. We believe these changes contributed to the decision for many vendors not to participate this year and resulted in just 19 vendors publishing their results vs. 29 the prior year.

![31 participant logos from MITRE ATT&CK results.](/blog/wp-content/uploads/2025/02/word-image-335141-1.png)

2023 (Turla) MITRE ATT&CK Enterprise Evaluation Enterprise Participants.

![19 vendor logos who listed their MITRE ATT&CK results.](/blog/wp-content/uploads/2025/02/word-image-335141-2.png)

2024 MITRE ATT&CK Enterprise Evaluation Enterprise Participants. Notably 10 fewer vendors opted to participate and publish their results this year.

## **Beyond the Headlines – Understanding MITRE Evaluation Results**

This year MTIRE published a new visual perspective on the evaluation results. The Cohort View shows the results for both the Detection and Protection scenarios in a view that consolidates the performance of all vendors.

![Graph of percent of results for MITRE ATT&CK tactics.](/blog/wp-content/uploads/2025/02/word-image-335141-3.png)

This graph from [MITRE shows the “Cohort View” results for the 2024 MITRE ATT&CK Enterprise Evaluation for the Protection Scenario](https://attackevals.mitre-engenuity.org/results/enterprise?view=cohort&evaluation=er6&result_type=PROTECTION). This graph clearly indicates that the majority of solutions are failing to block the TTPs emulated in this evaluation regardless of the phase of the attack.

![Graph of percent of results for MITRE ATT&CK tactics.](/blog/wp-content/uploads/2025/02/word-image-335141-4.png)

This graph from [MITRE shows the “Cohort View” results for the 2024 MITRE ATT&CK Enterprise Evaluation Detection Scenarios](https://attackevals.mitre-engenuity.org/results/enterprise?view=cohort&evaluation=er6&result_type=DETECTION&scenarios=1,2,3). This chart shows that a significant portion of the emulated TTPs in the detection scenarios were executed without generating an accurate, high-fidelity alert in many of the solutions under test.

For those that participated in this latest evaluation, MITRE’s Cohort graphs clearly indicate that many solutions are lagging behind in their ability to detect and prevent common MITRE ATT&CK tactics, techniques, and procedures (TTPs). Alarmingly, nearly all phases of the attack in the Protection scenario were prevented less than half of the time. Looking specifically at [Exfiltration](https://attack.mitre.org/tactics/TA0010/), we can see that over 83% of these techniques were not prevented. In fact, more than two thirds of the vendors tested this year missed the opportunity to block more than half of the attacks.

The above performance may come as a surprise to those who have been paying attention to these evaluations and reading the headlines and blogs from the solution providers who participated. It is important to point out that MITRE does not make any declarative statements on vendor performance or identify any rankings or ratings of solutions that participate in the evaluations. They just publish the data that reflects product performance observed during the evaluation. Interpretation is left up to the vendors. With that said, it's important that you understand how vendors are interpreting their results.

* Selective Reporting – As seen above, this year’s Protection scenario proved particularly challenging for the industry. Thus many of the participants chose not to disclose their results in the Protection scenarios in their results’ publications.
  + In the 2024 Evaluation of the vendors that did not have false positives in the Protection scenario, no vendor had a higher prevention rate than Cortex XDR.
* Detection Modifiers – A topic that has been discussed since the inception of the MITRE evaluations is the Detection Modifiers that may accompany detections. There are two modifiers, Delayed Detections and Configuration Changes.
  + The Delayed Detection modifier is added to a detection when human action or intervention is required to augment an autonomously generated event to meet the documented Detection Criteria.
  + The Configuration Change modifier is added to a detection when the configuration of the vendor solution is changed after the start of the evaluation. This may be done to show that additional data can be collecte...
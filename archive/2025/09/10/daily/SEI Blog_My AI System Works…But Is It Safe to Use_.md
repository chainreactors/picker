---
title: My AI System Works…But Is It Safe to Use?
url: https://www.sei.cmu.edu/blog/my-ai-system-worksbut-is-it-safe-to-use/
source: SEI Blog
date: 2025-09-10
fetch_date: 2025-10-02T19:55:44.311008
---

# My AI System Works…But Is It Safe to Use?

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University](https://www.cmu.edu)

[Software Engineering Institute](https://www.sei.cmu.edu)

[SEI Blog](/blog/)

1. [Home](/)
2. [Publications](/publications/)
3. [Blog](/blog/)
4. My AI System Works…But Is It Safe to Use?

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Schulker, D., Walsh, M., and Mathew, E., 2025: My AI System Works…But Is It Safe to Use?. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed October 1, 2025, https://doi.org/10.58012/8w84-jb90.

Copy

APA Citation

Schulker, D., Walsh, M., & Mathew, E. (2025, September 9). My AI System Works…But Is It Safe to Use?. Retrieved October 1, 2025, from https://doi.org/10.58012/8w84-jb90.

Copy

Chicago Citation

Schulker, David, Matthew Walsh, and Emil Mathew. "My AI System Works…But Is It Safe to Use?." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, September 9, 2025. https://doi.org/10.58012/8w84-jb90.

Copy

IEEE Citation

D. Schulker, M. Walsh, and E. Mathew, "My AI System Works…But Is It Safe to Use?," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 9-Sep-2025 [Online]. Available: https://doi.org/10.58012/8w84-jb90. [Accessed: 1-Oct-2025].

Copy

BibTeX Code

@misc{schulker\_2025,
author={Schulker, David and Walsh, Matthew and Mathew, Emil},
title={My AI System Works…But Is It Safe to Use?},
month={{Sep},
year={{2025},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/8w84-jb90},
note={Accessed: 2025-Oct-1}
}

Copy

# My AI System Works…But Is It Safe to Use?

![David Schulker](/media/images/dschulker.max-180x180.format-webp.webp)
![Headshot of Matthew Walsh.](/media/images/Walsh_Matthew_039_240429.360x36.max-180x180.format-webp.webp)

###### [David Schulker](/authors/david-schulker), [Matthew Walsh](/authors/matthew-walsh), and [Emil Mathew](/authors/emil-mathew)

###### September 9, 2025

##### PUBLISHED IN

[Artificial Intelligence Engineering](/blog/topics/artificial-intelligence-engineering/)

##### CITE

<https://doi.org/10.58012/8w84-jb90>

Get Citation

##### SHARE

Software is a method of communicating human intent to a machine. When developers write software code, they are providing precise instructions to the machine in a language the machine is designed to understand and respond to. For complex tasks, these instructions can become lengthy and difficult to check for correctness and security. Artificial intelligence (AI) offers the alternative possibility of interacting with machines in ways that are native to humans: plain language descriptions of goals, spoken words, and even gestures or references to physical objects visible to both the human and the machine. Because it is so much easier to describe complex goals to an AI system than it is to develop millions of lines of software code, it is not surprising that many people see the possibility that [AI systems might consume](https://www.technologyreview.com/2017/05/12/151722/nvidia-ceo-software-is-eating-the-world-but-ai-is-going-to-eat-software/) greater and greater portions of the software world. However, [greater reliance on AI systems might expose mission owners to novel risks](https://www.sei.cmu.edu/blog/weaknesses-and-vulnerabilities-in-modern-ai-why-security-and-safety-are-so-challenging/), necessitating [new approaches to test and evaluation](https://www.sei.cmu.edu/blog/weaknesses-and-vulnerabilities-in-modern-ai-ai-risk-cyber-risk-and-planning-for-test-and-evaluation/).

SEI researchers and others in the software community have spent decades studying the behavior of software systems and their developers. This research has advanced software development and testing practices, increasing our confidence in complex software systems that perform critical functions for society. In contrast, there has been far less opportunity to study and understand the potential failure modes and vulnerabilities of AI systems, and particularly those AI systems that employ large language models (LLMs) to match or exceed human performance at difficult tasks.

In this blog post, we introduce System Theoretic Process Analysis (STPA), a hazard analysis technique uniquely suitable for dealing with the complexity of AI systems. From preventing outages at [Google](https://www.usenix.org/publications/loginonline/evolution-sre-google) to enhancing safety in [aviation](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://rosap.ntl.bts.gov/view/dot/78914/dot_78914_DS1.pdf&ved=2ahUKEwj0y6v928uPAxXCElkFHVAcB7oQFnoECBgQAQ&usg=AOvVaw3GBbGJi1YCPa0T5_BclzE4) and [automotive](https://www.sae.org/standards/content/j3187_202305/) industries, STPA has proven to be a versatile and powerful method for analyzing complex sociotechnical systems. In our work, we have also found that applying STPA clarifies the safety and security objectives of AI systems. Based on our experiences applying it, we describe four specific ways that STPA has reliably provided insights to enhance the safety and security of AI systems.

## **The Rationale for System Theoretic Process Analysis (STPA)**

If we were to treat a system with AI components like any other system, [common practice](https://safety.army.mil/Portals/0/Documents/ON-DUTY/SYSTEMSAFETY/Standard/MIL-STD-882E-change-1.pdf) would call for following a systematic analysis process to identify hazards. Hazards are conditions within a system that could lead to mishaps in its operation resulting in death, injury, or damage to equipment. [System Theoretic Process Analysis (STPA)](http://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf) is a recent innovation in hazard analysis that stands out as a promising approach for AI systems. The four-step STPA workflow leads the analyst to identify unsafe interactions between the components of complex systems, as illustrated by the basic security-related example in Figure 1. In the example, an LLM agent has access to a sandbox computer and a search engine, which are tools that the LLM can employ to better address user needs. The LLM can use the search engine to retrieve information relevant to a user’s request, and it can write and execute scripts on the sandbox computer to run calculations or generate data plots. However, giving the LLM the ability to autonomously search and execute scripts on the host system potentially exposes the system owner to security risks, as in [this example from the Github blog](https://github.blog/security/vulnerability-research/safeguarding-vs-code-against-prompt-injections/). STPA offers a structured way to define these risks and then identify, and ultimately prevent, the unsafe system interactions that give rise to them.

[![figure1_STPASchulker_09082025](/media/images/figure1_STPASchulker_09082025.max-1280x720.format-webp.webp)](/media/images/figure1_STPASchulker_09082025.original.png)

Figure 1. STPA Steps and LLM Agent with Tools Example

Historically, hazard analysis techniques have focused on identifying and preventing unsafe conditions that arise due to component failures, such as a cracked seal or a valve stuck in the open position. These types of hazards often call for greater redundancy, maintenance, or inspection to reduce the probability of failure. A [failure-based accident framework](https://www.dau.edu/acquipedia-article/fault-tree-analysis-fta) is not a good fit for AI (or software, for that matter), because AI hazards are not the result of the AI component failing in the same way as a seal or a valve might fail. AI hazards arise when fully-functioning programs faithfully follow flawed instructions. Adding redundancy of such components would do nothing to reduce the probability of...
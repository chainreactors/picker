---
title: Do robots dream of secure networking? Teaching cybersecurity to AI systems
url: https://blog.talosintelligence.com/do-robots-dream-of-secure-networking/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-06
fetch_date: 2025-11-07T03:11:38.369462
---

# Do robots dream of secure networking? Teaching cybersecurity to AI systems

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

![](/content/images/2025/11/tool-talk.jpg)

# Do robots dream of secure networking? Teaching cybersecurity to AI systems

By
[Martin Lee](https://blog.talosintelligence.com/author/martin-lee/)

Thursday, November 6, 2025 06:00

[Tool Talk](/category/tool-talk/)
[AI](/category/ai/)

* This blog explores how to equip autonomous AI agents with cybersecurity knowledge, enabling them to make informed decisions about internet safety, such as identifying trustworthy links and websites.
* It demonstrates a proof of concept using LangChain and OpenAI, integrated with the Cisco Umbrella API, to provide AI agents with real-time threat intelligence for evaluating domain dispositions.
* By learning to assess the safety of domains, AI agents can develop better cyber hygiene, making more intelligent decisions rather than simply being restricted by security gateways, which is crucial for the next generation of autonomous AI systems.

---

In the late 1960s, the science fiction author Philip K. Dick wrote “Do Androids Dream of Electric Sheep,” which, among other themes, explored the traits that distinguish humans from autonomous robots. As advances in generative AI allow us to create autonomous agents that are able to reason and act on humans’ behalf, we must consider the human traits and knowledge that we must equip agentic AI with to allow them to act autonomously, reasonably, and safely.

One skill we need to impart on our AI agents is the ability to stay safe when navigating the internet. If agentic AI systems are interacting with websites and APIs in the same way as a human internet user, they need to be aware that not all websites or public APIs are trustworthy, and nor is user supplied input. Therefore, we must empower our AI agents with the ability to make appropriate cyber hygiene decisions. In an agentic world, it is for the autonomous agent to decide if it is safe and appropriate to “click the link.”

The threat landscape is constantly shifting, so there are no hard and fast rules that we can teach AI systems about what is a safe link and what is not. AI agents must verify the disposition of links in real time to determine if something is malicious.

There are many emerging approaches to building AI workflow systems that can integrate multiple sources of information to allow an AI agent to come to a decision about an appropriate course of action. In this blog, I show how it is possible to use one of these frameworks, LangChain, with OpenAI to enable an AI agent to access real-time threat intelligence via the Cisco Umbrella API.

## Prerequisites

To implement this example you will need API keys for Cisco Umbrella and a paid OpenAI account.

1. [Obtain a new API key](https://help.openai.com/en/articles/9186755-managing-projects-in-the-api-platform) from OpenAI account with available credit. The key will not work if you have a free, unfunded account.
2. Obtain a Cisco Umbrella API Key and Secret by [following these steps](https://developer.cisco.com/docs/cloud-security/umbrella-api-authentication/#api-key-use-cases). Be sure the check the “Investigate” box for the Key Scope.
3. Save your keys as shell environment variables named “OPENAI\_API\_KEY”, “UMBRELLA\_KEY” and “UMBRELLA\_SECRET” (e.g., export  UMBRELLA\_KEY="nnnnnnnnnnnnnnnnnn”).

## Code

Follow along with the [full sample code, which can be found in Talos’ GitHub repository](https://github.com/Cisco-Talos/IOCs/blob/main/2025/11/lang5.py).

First, we need to describe the tool to the AI agent.

![](https://blog.talosintelligence.com/content/images/2025/11/drd1.png)

Then we include the newly described tool in the list of available tools.

![](https://blog.talosintelligence.com/content/images/2025/11/drd2.png)

Next, we create the large language model (LLM) instance that we will use. This example uses GPT-3.5-Turbo from OpenAI, but other LLM models are supported.

![](https://blog.talosintelligence.com/content/images/2025/11/drd3.png)

Now, let's give instructions to the LLM, describing what the LLM should do using natural language structured in a Question, Thought, Action, Observation format.

![](https://blog.talosintelligence.com/content/images/2025/11/drd4.png)

Create the agent and the executor instance that we will interact with.

![](https://blog.talosintelligence.com/content/images/2025/11/drd5.png)

As part of querying the Umbrella API, we must obtain a session token to pass to the Umbrella API with our request. This is obtained from an authentication call using our API key and secret.

![](https://blog.talosintelligence.com/content/images/2025/11/drd6.png)

Next, let's define the tool that we have described to the AI system. It accepts input text as a parameter and checks for the presence of any domains. If any are found, the disposition of each one is checked.

![](https://blog.talosintelligence.com/content/images/2025/11/drd7.png)

The key functionality within the above code is “getDomainDisposition” which passes the domain to the Umbrella API to retrieve the disposition and categorization information about the domain.

![](https://blog.talosintelligence.com/content/images/2025/11/drd8.png)

We can now pass input text to “agent\_executor” to discover the agent’s opinion.

![](https://blog.talosintelligence.com/content/images/2025/11/drd9.png)

This gives the response:

“*Agent Response: www.cisco.com is safe to browse.*”

Reassuringly, the agent reports that “cisco.com” is safe to connect to. If necessary, we can output the domain disposition report to see the logic by which the system arrives at this conclusion:

“*This* *contains* *a URL. Considering www.cisco.com. The domain www.cisco.com has a positive disposition. The domain www.cisco.com is classified as: Computers and Internet, Software/Technology.* *Known malicious domains are never safe, domains with positive disposition are...
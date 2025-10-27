---
title: Cybercriminal abuse of large language models
url: https://blog.talosintelligence.com/cybercriminal-abuse-of-large-language-models/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-26
fetch_date: 2025-10-06T22:55:06.870926
---

# Cybercriminal abuse of large language models

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

![](/content/images/2025/06/LLM-abuse.jpg)

# Cybercriminal abuse of large language models

By
[Jaeson Schultz](https://blog.talosintelligence.com/author/jaeson-schultz/)

Wednesday, June 25, 2025 06:00

[On The Radar](/category/on-the-radar/)

* Cybercriminals are continuing to explore artificial intelligence (AI) technologies such as large language models (LLMs) to aid in their criminal hacking activities.
* Some cybercriminals have resorted to using uncensored LLMs or even custom-built criminal LLMs for illicit purposes.
* Advertised features of malicious LLMs indicate that cybercriminals are connecting these systems to various external tools for sending outbound email, scanning sites for vulnerabilities, verifying stolen credit card numbers and more.
* Cybercriminals also abuse legitimate AI technology, such as jailbreaking legitimate LLMs, to aid in their operations.

---

Generative AI and LLMs have taken the world by storm. With the ability to generate convincing text, solve problems, write computer code and more, LLMs are being integrated into almost every facet of society. According to [Hugging Face](https://huggingface.co/models) (a platform that hosts models), there are currently over 1.8 million different models to choose from.

LLMs are usually built with key safety features, including alignment and guardrails. Alignment is a training process that LLMs undergo to minimize bias and ensure that the LLM generates outputs that are consistent with human values and ethics. Guardrails are additional real-time safety mechanisms that try to restrain the LLM from engaging in harmful or undesirable actions in response to user input. Many of the most advanced (or “frontier”) LLMs are protected in this manner. For example, asking ChatGPT to produce a phishing email will result in a denial, such as, “Sorry, I can’t assist with that.”

For cybercriminals who wish to utilize LLMs for conducting or improving their attacks, these safety mechanisms can present a significant obstacle. To achieve their goals, cybercriminals are increasingly gravitating towards uncensored LLMs, cybercriminal-designed LLMs and jailbreaking legitimate LLMs.

## Uncensored LLMs

Uncensored LLMs are unaligned models that operate without the constraints of guardrails. These systems happily generate sensitive, controversial, or potentially harmful output in response to user prompts. As a result, uncensored LLMs are perfectly suited for cybercriminal usage.

![Picture](https://blog.talosintelligence.com/content/images/2025/06/data-src-image-9338e26b-3b6b-4333-8b31-654fe059c865.png)

**Figure 1. An uncensored LLM, OnionGPT, advertised on the hacking forum Dread.**

Uncensored LLMs are quite easy to find. For example, using the cross-platform Omni-Layer Learning Language Acquisition ([Ollama) framework](https://ollama.com/), a user can download and run an uncensored LLM on their local machine. Ollama comes with several uncensored models such as Llama 2 Uncensored which is based on Meta’s Llama 2 model. Once it is running, users can submit prompts that would otherwise be rejected by more safety-conscious LLM implementations. The downside is that these models are running on users’ local machines and running larger models, which generally produce better results requires more system resources.

![Picture](https://blog.talosintelligence.com/content/images/2025/06/data-src-image-2077b340-7a64-4b76-bcf3-149de2dcc870.png)

**Figure 2. Sample phishing email prompt and Llama 2 Uncensored output.**

Another uncensored LLM popular among cybercriminals is a tool called [WhiteRabbitNeo](https://www.whiterabbitneo.com/). WhiteRabbitNeo bills itself as a “Uncensored AI model for (Dev) SecOps teams” which can support “use cases for offensive and defensive cybersecurity”. This LLM will happily write offensive security tools, phishing emails and more.

![Picture](https://blog.talosintelligence.com/content/images/2025/06/data-src-image-01a8af95-1658-4f2b-890c-ea043712edf3.png)

**Figure 3. Sample output from the WhiteRabbitNeo uncensored LLM**

Researchers have also [published](https://erichartford.com/uncensored-models) methods to demonstrate how to strip alignment that is embedded into the training data of existing open-source models. Once removed, a user can uncensor their LLM by using the modified training set to fine tune a base model.

## Cybercriminal-designed LLMs

Since most popular LLMs come with significant guardrails, some enterprising cybercriminals have developed their own LLMs without restrictions that they market to other cybercriminals. This includes apps like GhostGPT, WormGPT, DarkGPT, DarkestGPT and FraudGPT.

![Picture](https://blog.talosintelligence.com/content/images/2025/06/data-src-image-5860bd28-aa27-48f3-8931-173181854a1b.png)

**Figure 4. FraudGPT dark web homepage.**

 For example, the developer behind FraudGPT, CanadianKingpin12, advertises FraudGPT on the dark web, and also has an account on Telegram. The dark web site for FraudGPT advertises some interesting features:

* Write malicious code
* Create undetectable malware
* Find non-VBV bins
* Create phishing pages
* Create hacking tools
* Find groups, sites, markets
* Write scam pages/letters
* Find leaks and vulnerabilities
* Learn to code/hack
* Find cardable sites
* Millions of samples of phishing emails
* 6220+ source code references for malware
* Automatic scripts for replicating logs/cookies
* In-panel Page hosting included (10 pages/month) with Google Chrome anti-red page
* Code obfuscation
* Custom data set (upload your sample page in .html)
* Bot creation of virtual machines and accounts (1 virtual machine per month on license)
* Utilizing GoldCheck CVV checker
* OTP Bot with spoofing (\*additional package)
* Check CVVs with GoldCheck API
* Create username:password website configs
* Remote OpenBulle...
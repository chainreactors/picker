---
title: Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer
url: https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/
source: Over Security
date: 2026-10-31
fetch_date: 2026-11-01T08:21:32.508567
---

# Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/VOLTA.jpg)

# Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer

By
[Ryan Fetterman](https://blog.talosintelligence.com/author/ryan-fetterman/)

Saturday, October 31, 2026 08:00

[AI](/category/ai/)
[Threat Spotlight](/category/threat-spotlight/)
[Stealer](/category/stealer/)

* VOLTA is a mature stealer implant with an optional AI-integration layer. After stealing credentials, sessions, and cryptocurrency wallets, VOLTA sends a structured evidence bundle to an LLM to rank the victim’s assets by monetization value.
* If a model refuses to perform the target assessment, VOLTA fails over to a three-model chain, implying a direct engineering effort and expectation of hitting model guardrails.
* This stealer is self-deleting, and there is no attacker-owned infrastructure. The novelty in the AI-integration is that it is not supporting a traditional malware capability but working as an intelligence analyst on behalf of the operator.

---

There is a new idea in the cybercrime world — cast a wide net, steal everything, and let AI sort out the specifics. A new malware self-named “VOLTA-AUTODOXER,” surfaced through the [CAIRN research effort](https://blog.talosintelligence.com/introducing-cairn-frontier-tracking-for-ai-integrated-malware/), is a self-deleting Windows infostealer that augments its post-theft workflow with an LLM-powered victim-profiling stage.

After harvesting the standard stealer haul, including browser passwords; cookies; payment cards; cryptocurrency wallet seed phrases; Discord, Telegram, Steam, and Roblox sessions; Microsoft OAuth tokens; SSH and cloud-provider keys; Wi-Fi profiles; and screenshots, VOLTA builds a structured evidence bundle about the person behind the machine. This bundle contains geolocation and home address, employer and employer domain, inferred birth year, card last-4 digits, Slack workspaces, document authorship metadata, iPhone backup indicators, and a live Roblox account valuation. It then uses stolen session access to enrich that bundle further: searching the victim's Gmail for purchase receipts to corroborate a home address, pulling UberEats and DoorDash order history, and enriching Discord accounts via the stolen token.

The bundle is serialized and POSTed to OpenRouter under a system prompt that instructs the model to act as "a forensic intelligence analyst drafting a target assessment." The required output includes a section titled “WHAT THEY'RE WORTH” with valuables ranked by monetization with a low/medium/high tier, and a section on “THEIR OPSEC” containing an assessment of the victim's security posture and password hygiene. The model is the operator's triage analyst; it turns a raw credential log into a prioritized and citation-backed dossier of the victim and their monetizable assets.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/102726-VOLTA-malware-graphics-02-1-.jpg)

Figure 1. The VOLTA-AUTODOXER workflow.

## The AI configuration: “Go deep, not wide... Be blunt, specific, accurate.”

VOLTA uses a multi-model architecture to fall back resiliently if it hits a model’s refusal, checking each response for phrases like “I can’t” or “I’m not able,” before passing on to a chain of up to three models.

|  |  |
| --- | --- |
| Endpoint | https[:]//openrouter[.]ai/api/v1/chat/completions |
| Default model | anthropic/claude-opus-4.6 |
| Fallback chain | moonshotai/kimi-k2 → google/gemini-2.5-flash |
| Temperature | 0.2 — deterministic, consistent output |
| Request format | Hand-assembled JSON; no SDK; User-Agent Mozilla/5.0 |

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/firstmodel.png)

Figure 2. Hardcoded model selection.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/modelfailover.png)

Figure 3. Failover model selection to kimi-k2, and then gemini-2.5-flash.

Model temperate controls the randomness and predictability of LLM-generated text. The low hardcoded temperature value (0.2) suggests the attacker is emphasizing accuracy and consistency. The malware also employs a chain of cascading models in the event of failures. This multi-model architecture suggests that the operator is anticipating encountering refusals, with the fallback pivoting to a few, smaller, and more permissive models.

The system prompt directly reveals the operator’s use case: Produce a concise analytical assessment of the victim’s suitability as a target, backed by an auditable trail of citations.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/voltaprompt.png)

Figure 4. VOLTA's raw system prompt.

The prompt also asks for something out of the ordinary, but that agents excel at: making connections between sparse and disparate data. For example, encouraging connections like the victim’s names, addresses, or universities to patterns in their passwords. In this case, the model isn't being asked to find data; rather, it’s being asked to stretch the data and make useful inferences that extend the value of what has been scraped.

## Stealer capabilities

VOLTA’s capabilities are directly aligned with the records produced in modern digital life, and well beyond basic credential theft. In a single pass, the stealer can extract browser credentials, cookies, and saved payment cards across Chromium-based browsers. It hits Firefox and Thunderbird, Outlook profiles, Slack workspaces, Steam and Battle.net sessions, Discord tokens, Telegram sessions, Roblox accounts, and SSH and cloud-provider config files (gcloud, OpenVPN, Hide.me). VOLTA doesn’t just copy cryptocurrency wallets, but runs an embedded cracker against th...
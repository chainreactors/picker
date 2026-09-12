---
title: The Self-Expanding Stolen Inference Supply Chain: An AI Agent Harvesting and Re-Serving LLM Access, (Fri, Sep 11th)
url: https://isc.sans.edu/diary/rss/33332
source: SANS Internet Storm Center, InfoCON: green
date: 2026-09-11
fetch_date: 2026-09-12T06:50:03.047851
---

# The Self-Expanding Stolen Inference Supply Chain: An AI Agent Harvesting and Re-Serving LLM Access, (Fri, Sep 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Renato Marinho](/handler_list.html#renato-marinho "Renato Marinho")

Threat Level: [green](/infocon.html)

* [previous](/diary/33326)

Click HERE to learn more about classes Renato is teaching for SANS

# [The Self-Expanding Stolen Inference Supply Chain: An AI Agent Harvesting and Re-Serving LLM Access](/forums/diary/The%2BSelfExpanding%2BStolen%2BInference%2BSupply%2BChain%2BAn%2BAI%2BAgent%2BHarvesting%2Band%2BReServing%2BLLM%2BAccess/33332/)

**Published**: 2026-09-11. **Last Updated**: 2026-09-11 14:40:32 UTC
**by** [Renato Marinho](/handler_list.html#renato-marinho) (Version: 1)

[0 comment(s)](/diary/The%2BSelfExpanding%2BStolen%2BInference%2BSupply%2BChain%2BAn%2BAI%2BAgent%2BHarvesting%2Band%2BReServing%2BLLM%2BAccess/33332/#comments)

I identified an attacker using a semi-autonomous coding agent to run an offensive operation: finding poorly secured LLM resale gateways, acquiring API access through ordinary web flaws and account farming, validating the resulting inference capacity, and aggregating it behind a single gateway of their own.

What I captured was not simply credential theft, but an **inference supply chain** — an agent harvesting, validating, and consolidating LLM access into infrastructure that serves it again through a unified API, which I watched come online.

None of the individual techniques is particularly novel. What is different is the feedback loop: the agent helps acquire new inference capacity, validates and consolidates it, and makes that capacity available to support further operations. The result is a partially **self-expanding** inference supply chain.

I reconstructed the operation across a series of captures from one of my AI honeypots, which the agent repeatedly selected as a free LLM backend.

## **The Capture**

The honeypot emulates an OpenAI-compatible inference endpoint. When the operator's coding agent attempted to use it, the request exposed much more than an exploit payload.

Because this particular client embedded its operating instructions and session context in model requests, the honeypot received approximately 43 KB of material: a large `AGENTS.md`, an offensive playbook, infrastructure notes, reconnaissance scripts, collected API keys, previous targets, and parts of the agent's working history.

In effect, the agent sent me part of its own control plane.

One instruction even had the agent verify its proxy was active before attacking, and that step exposed the operator's direct, unproxied egress IP: the playbook itself contained that IP as a reference value for the agent to compare against the proxied connection.

## **The Operation**

The captured workflow was straightforward:

* **Find supply.** The agent generated FOFA queries such as `title="V2Board"` and `header="subscription-userinfo"` to locate LLM gateways and adjacent subscription infrastructure.
* **Acquire access.** Its playbook listed open registration with free balances, default credentials, authorization weaknesses involving `group_id`, and exposed endpoints such as `/api/auth-files`. It also automated trial-account creation using temporary email and CAPTCHA-solving services.
* **Validate inference.** The agent tested compromised keys against resale services and confirmed usable inference through endpoints advertising current premium models. (What is confirmed is a working model behind an endpoint that *claims* to be, say, `claude-opus-5`; a reseller can point any backend at that name, so the label is the reseller's claim, not a verified identity.) Some endpoints exposed extremely high default billing limits, while another returned its full model catalog without authentication. In a later session the validation matured into a simple code-logic test: each candidate was asked to compute a small factorial, intended to distinguish usable inference from canned responses. Elsewhere the operator summarized the broader philosophy more bluntly: "a model that cannot edit a file is fake."
* **Aggregate and serve.** A second capture showed this stage being built, not just described. It is the strongest evidence in the case, so it is worth taking one step at a time:

  1. The operator stood up a self-hosted `New-API` gateway.
  2. They loaded roughly 379 upstream endpoints into it as channels, using collected credentials.
  3. They ran the code-logic test across all of them and disabled the 341 that failed as fake or dead.
  4. They mapped five standard model names (`deepseek-v4-flash`, `claude-opus-5`, `gpt-5.6-sol`, `gemini-3.6-flash-high`, `glm-5.3`) onto the surviving channels, with priority-based round-robin and automatic failover.
  5. A final probe showed all five configured model names returning usable responses through the single endpoint: the aggregated pool was operational.

  When the panel's own rate limits blocked the automation, the agent edited the gateway's SQLite database directly, clearing session rows and injecting an admin token. The aggregation software is a legitimate open-source project; the abuse is the compromised credentials fed into it.

The resulting pipeline is:

`find gateways → acquire accounts/keys → validate models and quota → aggregate credentials → serve inference`

The credential is only an intermediate asset. What the operation is ultimately harvesting is **inference capacity**.

This resembles the evolution of LLMjacking documented by Sysdig. In previously documented LLMjacking, stolen inference powers the offensive tooling:

`stolen LLM access → offensive tooling`

Here the tooling also participates in acquiring the next tranche of inference capacity, which is then consolidated and served again:

`offensive agent → more stolen or abused LLM access → aggregated inference service`

The result is a partially self-expanding supply loop: the agent's output feeds the pool that the agent draws on. I say partially because a human still steers it; the data does not show a fully autonomous or self-replicating system.

## **Takeaways**

**If you operate an LLM gateway**, review the same conditions the attacker's playbook was looking for: open registration with starting balances, authorization decisions based on client-supplied fields such as `group_id`, exposed account-management endpoints, default credentials, unauthenticated model or account information, and excessive default billing limits.

More importantly, assume these checks can now be executed continuously by agents rather than manually by an attacker.

**If you use a free or suspiciously cheap LLM proxy**, consider what your coding agent sends upstream. Depending on the tool and configuration, requests may contain `AGENTS.md`, project instructions, source-code context, command output, filenames, and other operational information.

The attacker in this case selected an untrusted inference endpoint and inadvertently sent that endpoint enough context to reveal a substantial part of the campaign. A malicious LLM endpoint sits in a privileged position to observe the agent that consumes it. Treat an untrusted LLM endpoint as a destination to which your agent may be sending not just prompts, but portions of its operational state. The cost of the inference may be negligible; the context wrapped around those tokens may not be.

--
**Renato Marinho**
Co-Founder, SecureSt8
[LinkedIn](http://ow.ly/Nst730dJ6X3) | [Twitter](http://ow.ly/uXqT30dJ6Tp)

Keywords:

[0 comment(s)](/diary/The%2BSelfExpanding%2BStolen%2BInference%2BSupply%2BChain%2BAn%2BAI%2BAgent%2BHarvesting%2Band%2BReServing%2BLLM%2BAccess/33332/#comments)

Click HERE to learn more about classes Renato is teaching for SANS

* [previous](/diary/33326)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries...
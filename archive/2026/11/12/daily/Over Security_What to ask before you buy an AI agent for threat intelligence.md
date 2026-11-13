---
title: What to ask before you buy an AI agent for threat intelligence
url: https://www.intel471.com/blog/what-to-ask-before-you-buy-an-ai-agent-for-threat-intelligence
source: Over Security
date: 2026-11-12
fetch_date: 2026-11-13T09:07:21.588378
---

# What to ask before you buy an AI agent for threat intelligence

[![Intel 471](https://cdn.sanity.io/images/fo9xc2x1/production/93fea1393c1c41cc700e939325848b7117804e8f-678x209.png?h=76&fm=webp&fit=max&auto=format)](/)PlatformUse Cases[Why Intel 471](/why-intel-471)ResourcesCompany

Search[Send a request](/company/contact)

# What to ask before you buy an AI agent for threat intelligence

Nov 12, 2026

![](https://cdn.sanity.io/images/fo9xc2x1/production/8e17f8259ee64d48b497a899616a4a8af4952a7e-1440x730.png?w=1920&h=800&fm=jpg&q=95&fit=crop&crop=center&auto=format)

*Before you buy an AI-enabled intelligence solution, ask what sits underneath it, how it handles what it can’t see, and whether its output reaches your controls.*

CTI teams serve a growing list of stakeholders who rely on intelligence to make better decisions. Like the rest of security operations, they’re being asked to do more with less. Many are turning toAI agent that helps a small team answer more questions, faster. But simply having access to an agent won’t solve all of these problems because agents don’t create intelligence.

That brings the buying decision back to the intelligence itself. Brandon Hoffman, Intel 471’s chief product officer, recently explained in [Intelligence Is Not a Control](https://www.linkedin.com/pulse/intelligence-control-brandon-hoffman-2uogc/) intelligence is the input that decides where controls focus: which detections to build, which incidents to escalate, and more. Treating it as just another tool to consolidate has a hidden cost. The savings show up in year one. The cost arrives around year three, in longer attacker dwell times when defenders miss adversary pre-positioning and respond only after the attacker has expanded their access. By then, nobody can trace the damage back to the budget decision that caused it.

The asymmetry between attacker and defender helps explain why adding more controls alone doesn’t close the gap. The defender has to cover every path, including ones created by new controls, while the attacker needs only one, with identities, privileges and third-party trust all multiplying the routes to an initial foothold.

It’s nearly impossible to enumerate every attack path. But defenders can enumerate adversaries. As Hoffman notes, “This enumeration only works if the intelligence is specific enough to be acted on: attributable to actors, sourced from the closed places where access is actually traded, and precise enough to distinguish a (theoretical) path from a walkable one.” Aggregated feeds, indicator dumps, and reputation scores don’t meet that bar.

AI raises the stakes on both sides. Attackers are adopting agentic frameworks like [ARTEX](https://www.microsoft.com/en-us/security/blog/2026/11/06/artex-abuse-expands-as-cybercriminals-target-financial-sector/) to scan, exploit and expand access faster than defenders can respond, while defenders’ agents can make weak intelligence harder to spot.So the questions CISOs and evaluators ask about an AI agent for threat intelligence should start beneath the agent and carry through to the controls intelligence informs. We’ve grouped them into three layers:

1. The intelligence the agent reasons over
2. How the agent handles it
3. Whether the result reaches the controls that protect you.

### **Layer 1: What is the agent reasoning over?**

Any answer an agent gives inherits the strengths and weaknesses of its sources. These four questions test the foundation before you test the agent.

**Where does the intelligence come from?** A useful test is whether intelligence is sourced from the closed places where access is being traded. That means underground forums, private messages, chat channels and well-placed human sources, not just aggregated feeds. This external intelligence helps an organization use its own telemetry to understand who is behind the activity it sees, and what attackers are planning before it reaches the network.

**What you should ask:** Does the vendor name its source types, the languages it covers and how it collects and validates intelligence? A well-designed agent should show you the original post, in its original language, alongside the translation and context.

**Is intelligence attributable, and is source reliability graded?** An agent can’t assign calibrated confidence if the underlying reporting carries none. Ask whether sources are graded, for example with the NATO Admiralty Code, and who does the grading; analysts closest to a source, who speak the threat actors’ language natively, are best placed to judge it. Ask, too, whether actors are tracked across aliases, with their reputation and history, so activity is tied to a known actor rather than a single handle. This matters because CTI analysts weigh underground claims by reputation and track record. Graded, attributed intelligence lets them apply that judgment to an agent’s answers instead of rechecking every source themselves.

Check the agent’s output includes an analyst-derived grade beside each judgment, with a credibility rating for each piece of evidence.

**Can the agent tell a claim from a capability?** Before a claim becomes intelligence, an analyst has to establish whether it describes a theoretical attack path or a proven one that an attacker can actually use. An initial access broker (IAB) may advertise access to a network with no evidence it works. Ransomware groups often claim victims they have not breached. Telling these apart often takes human intelligence (HUMINT) from analysts who engage threat actors directly, under strict rules of engagement, to test whether a claim holds up.

Ask whether the vendor’s intelligence records if a claim was verified and take note of whether the agent upholds that distinction in its answer. The agent should connect activity across multiple actor handles and show its confidence in each link. When the underlying reporting hasn’t verified a breach claim, the agent should report it as unconfirmed.

### **Layer 2: How does the agent handle the intelligence?**

Our [blog post last week](https://www.intel471.com/blog/hand-ai-the-legwork-you-keep-the-judgment) covered the guardrails an agent needs — grounded answers, sources you can check and reasoning you can see. These are table stakes. These three questions cover what those guardrails don’t:

* Does the agent see all the evidence?
* How does it report what it couldn’t find?
* Is it the only way to reach data in a cyber intelligence platform?

**Does it work through everything, or sample?** Threat intelligence questions often involve thousands of results, such as years of an actor’s forum posts or every breach claim against a sector. Many agent integrations cap the results a single request returns or sample across long time frames. Evidence can drop even when the answer appears complete. Ask how the agent handles large result sets. Then test it with a question you already know the full answer to, and compare it.

**What does “nothing found” mean?** The most consequential thing an agent says may be that it found nothing. An empty result can mean several things, such as a search window that was too short. Or there may genuinely be nothing there. Ask whether the agent states what it searched, which time window it applied and what it couldn’t see. A good agent treats silence as a coverage statement that your analysts can weigh.

**Can you bring your own AI?** Many security teams already use general-purpose AI assistants, or have built model-agnostic tools that combine several intelligence sources. Ask whether the intelligence is available through an open standard such as the Model Context Protocol (MCP) for teams that want the intelligence inside their own tools.

### **Layer 3: Does the intelligence reach your controls?**

As Hoffman noted, intelligence isn’t a control but the input that decides how controls work. Intelligence-driven threat hunting can also expose logging blind spots, drive higher-fidelity detections and help prioritize incident response. The buying decision includes whether...
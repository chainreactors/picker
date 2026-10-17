---
title: Small Agents, Smaller Blast Radius: Controlling What AI Can Do, (Fri, Oct 16th)
url: https://isc.sans.edu/diary/rss/33430
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-16
fetch_date: 2026-10-17T06:37:50.854030
---

# Small Agents, Smaller Blast Radius: Controlling What AI Can Do, (Fri, Oct 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33426)

Click [HERE](https://www.sans.org/profiles/mark-baggett) to learn more about classes Mark is teaching for SANS

# [Small Agents, Smaller Blast Radius: Controlling What AI Can Do](/forums/diary/Small%2BAgents%2BSmaller%2BBlast%2BRadius%2BControlling%2BWhat%2BAI%2BCan%2BDo/33430/)

**Published**: 2026-10-16. **Last Updated**: 2026-10-16 00:46:35 UTC
**by** [Mark Baggett](/handler_list.html#mark-baggett) (Version: 2)

[0 comment(s)](/diary/Small%2BAgents%2BSmaller%2BBlast%2BRadius%2BControlling%2BWhat%2BAI%2BCan%2BDo/33430/#comments)

I believe the cybersecurity industry may be approaching AI security the wrong way.

AI agents are becoming more powerful every day. Systems like ChatGPT, Claude, and Grok can write and execute code, use command shells, browse the web, call APIs, interact with MCP servers, and access enterprise data. Yet much of the industry is taking these extraordinarily powerful, general-purpose agents and trying to make them safe by building cages around them. We add containers, policy layers, monitoring, guardrails, and humans in the loop.

I think that’s backwards. If the companies building these models struggle to control their behavior, why do we assume we can reliably contain them? And when in human history has requiring a user to click a button before something dangerous happened EVER worked?

Even if you build the perfect cage, the model you tested in your cage will eventually change. Providers [retire models](https://developers.openai.com/api/docs/deprecations), and moving to a replacement means revisiting your assumptions and testing. Your application code may be unchanged, but the component deciding what to do next is different.

In my opinion, we should use these agents, which are very good at coding, to build smaller, single-purpose agents. If an agent only needs to read logs from one directory, why give it functions that can read, write, or execute things anywhere on the system?

This isn’t a new idea. It’s the principle of least privilege and seperation of duties. But somehow, when we build agents, we seem willing to hand over broad access and ask the model to use good judgment.

This is the guiding philosophy behind [SANS SEC573: AI-Powered Security Automation](https://www.sans.org/cyber-security-courses/ai-powered-security-automation), where we learn to vibe code these focused agents into existence. Use the powerful coding agent to build a better agent. Give the resulting agent only the access it needs to do its job.

An October 15 article from Check Point provides a good case in point.

Imagine asking an AI security agent to investigate a suspicious login. It retrieves authentication logs, checks the source IP, and identifies several potentially affected accounts. Then it disables them. The agent may have correctly identified suspicious activity. Disabling those accounts might even be appropriate. But you asked it to investigate. Somewhere along the way, it expanded its assignment.

Check Point’s article describes its Dangerous Deviation Detection capability, which evaluates proposed tool calls before execution. The problem extends beyond prompt injection. An agent can misunderstand a request or take its assignment too far without an attacker being involved.

The detector sits between the model choosing a tool call and the application executing it. It evaluates the proposed operation and its arguments against the task. The application can then stop the action, request approval, or give the agent feedback so it can try another approach.

According to Check Point’s technical documentation:

* The beta detector flags actions that are **both dangerous and unwarranted**. Its danger categories include data leakage, access or privilege escalation, and destruction of persistent resources.
* It looks for justification in `user` and `system` messages. Instructions in tool responses or other external content do not count as authorization.
* The application submits conversation history, the proposed tool call in the final `assistant` message, and tool definitions in the top-level `tools` field of a Guard API request.
* Setting `"breakdown": true` returns fields including `reason_code`, `reason`, `agent_guidance`, and `debug_info.dev_tips`.

The distinction between dangerous and unwarranted is important. An irrelevant but harmless action can pass. A dangerous action supported by trusted instructions can also pass. Check Point separately documents a deterministic tool allow/deny list and describes the beta detector as favoring fewer false positives over catching every marginal case. Its a solid approach.

Those are documented product behaviors, not results from my own testing.

I can see value in checking proposed actions. But my first question comes before that check: **Why does the investigation agent have permission to disable accounts?**

The human analyst might need that permission. The agent performing this particular task does not. Seperation of Duties and the Prinsicle of Least required access are screaming in their graves.

An investigation agent can collect evidence and recommend containment using narrowly scoped, read-only access. If containment is needed, a separate workflow can perform the authorized operation against the specified accounts.

That boundary needs to exist in code and credentials. Removing a tool from the list shown to the model is not enough if the executor still accepts it. Restricting tools also accomplishes little if the agent has a general-purpose shell running with administrative credentials.

The same rule applies when agents work together. If the investigation agent can freely tell a privileged response agent to disable accounts, it still has an indirect path to that capability. The receiving workflow must check authorization and scope for itself. “The other agent said you approved it” should not be enough.

There is another implementation detail worth watching. Check Point’s detector distinguishes trusted messages from external content. If your application copies an untrusted ticket into a `user` message, you may blur that distinction. A sentence in a ticket claiming that someone approved an action is evidence to evaluate, not permission to execute it.

You can test these boundaries with ordinary requests:

* Ask for an incident summary. Does the agent try to close the ticket?
* Ask for a list of inactive accounts. Does it try to disable them?
* Put a fabricated approval in a retrieved document. Does the application accept it?
* Approve an action against one account. Can the agent expand it to several?
* Deny an action. Can it accomplish the same thing through another tool or agent?

Watch both what the model proposes and what the application allows. An unauthorized attempt that gets blocked tells you a control worked. An agent that happens to behave correctly does not prove the control exists.

I’m not suggesting we abandon monitoring, guardrails, or approval workflows. I’m suggesting we stop making them responsible for containing capabilities the agent never needed.

Before building a better cage, ask why you gave the agent that much access in the first place. Then have the agents build their own cages by writing single purpose agents with only those tools that are required. I'll show you how in SEC573.

Sources: [Check Point’s October 15 article](https://blog.checkpoint.com/ai-security/dangerous-deviation-detection-ai-agents/) and [Agent Behavior Defense documentation](https://docs.lakera.ai/docs/agent-behavior-defense).

Keywords: [ai](/tag.html?tag=ai)

[0 comment(s)](/diary/Small%2BAgents%2BSmaller%2BBlast%2BRadius%2BControlling%2BWhat%2BAI%2BCan%2BDo/33430/#comments)

Click [HERE](https://www.sans.org/profiles/mark-baggett) to learn more about classes Mark is teaching ...
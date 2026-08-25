---
title: The Security Autonomy Matrix: Deciding AI Authority
url: https://zeltser.com/security-autonomy-matrix
source: Lenny Zeltser
date: 2026-08-24
fetch_date: 2026-08-25T03:00:36.574123
---

# The Security Autonomy Matrix: Deciding AI Authority

[Skip to main content](#main-content)

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# The Security Autonomy Matrix: Deciding AI Authority

The Security Autonomy Matrix is a framework for deciding how much authority to grant your security AI agents, one kind of action at a time. You record those decisions in one table, one row per workflow, capturing the autonomy level, who answers for it, and when the grant expires.

![The Security Autonomy Matrix: Deciding AI Authority - illustration](/assets/security-autonomy-matrix.DYA60hX6_ZH08mc.webp)

Cybersecurity teams are increasingly adopting AI technologies for their workflows. How should they decide what authority to grant their AI agents, and how independently the agents may exercise it? The *Security Autonomy Matrix* is an approach to making these decisions and capturing them in one table. Each row in the table represents a security workflow. It records the five decisions we make about that workflow. By capturing decisions this way, we can enforce them through our tooling, widening the AI’s autonomy as it earns trust.

This guide is also available as [PDF](/media/docs/security-autonomy-matrix.pdf) and [Word](/media/docs/security-autonomy-matrix.docx) documents, so you can read it offline or share it with others.

**Contents:**

* [Keep a record of AI authority decisions](#keep-a-record-of-ai-authority-decisions)
* [Decide how much autonomy each AI action gets](#decide-how-much-autonomy-each-ai-action-gets)
* [Put the Security Autonomy Matrix to work](#put-the-security-autonomy-matrix-to-work)
* [What the matrix is based on, and what is new](#what-the-matrix-is-based-on-and-what-is-new)
* [Thank you to the reviewers](#thank-you-to-the-reviewers)

## Keep a record of AI authority decisions.

Like every executive in the organization, security leaders are looking for responsible ways to deploy AI within their functions. Getting the most out of AI often means granting it agentic capabilities, so it has the authority to make security decisions and take security actions on its own. How does a leader grant that authority deliberately and responsibly?

Consider an AI agent that removes the phishing messages that reached user mailboxes. The agent can read every mailbox safely, yet one wrong deletion can permanently remove a legitimate message. Security leaders need to decide, for this and other security workflows, whether to allow the agent to make the call and take the action.

Deciding how much authority to grant AI is a leadership judgment, and there is little established guidance. In the [2026 SANS AI Survey](https://www.sans.org/white-papers/2026-sans-ai-survey-insights), only 41% of organizations reported using generative AI for security-related tasks under strict policy. Another 39% said usage is informal, with no policy at all.

Security teams need a single place to capture what they have allowed AI agents to do on their own. The Security Autonomy Matrix is that record. Without it, a team has to reconstruct what its AI may do from tool settings, runbooks, and the memory of whoever set them up. Instead, as security leaders, we can capture those decisions in the matrix, with one row per security workflow: the permissions granted, the accountable person, and what reopens the decision.

### What is the Security Autonomy Matrix?

The Security Autonomy Matrix is a table with a row for each security workflow where AI performs actions whose mistakes would be costly or hard to reverse. One column identifies the workflow, and the other five each record a decision security leaders make about it:

* **Autonomy:** How independently the AI may act. Set it separately for each kind of action in the workflow, such as reading data, sending email, or deleting records.
* **Accountable person:** The person who answers for the AI’s actions.
* **Gate:** The point where a person approves, overrides, or rolls back the AI’s action.
* **Residual risk:** The harm that remains possible and the safeguard that limits it.
* **Reevaluation trigger:** The events that reopen the autonomy decision, and the date when the row expires.

Add a row for every workflow where the AI performs actions whose mistakes would be costly or hard to reverse. This includes workflows where a person still approves each action, and workflows where you’re only considering such autonomy.

> *Authority* specifies what the AI agent may do. *Autonomy* is how independently it may exercise that authority. The row’s Autonomy column captures both the kinds of actions the AI may take in the workflow and how independently it may take each. I named the matrix for autonomy because the autonomy level is the central decision in each row.

### The matrix captures decisions so you can enforce them.

The Security Autonomy Matrix is an authorization policy for non-human workers. OWASP’s [Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) prescribes narrow permissions for AI agents, including “read-only queries for databases, no send/delete rights for email summarizers.” A leader using the matrix grants authority the same way, deciding separately what the AI may read, send, or delete. SANS’s [Critical AI Security Guidelines](https://github.com/sans-community/ai-guidelines/blob/current-version/SANS_Critical_AI_Security_Guidelines_v1.1.md) prescribe the same discipline: “clearly delineated permissions” for each agent, and human oversight for any “critical operations” it can reach. The matrix is where a leader decides which operations those are, who answers for the decision, and what reopens it.

Because the matrix is policy, it needs an owner and a place in the program. The security leader owns it like the rest of the security policy. Each row needs enforcement, whether through the tooling’s permission settings or through a manual check where the tooling falls short. Security teams already run access reviews for least privilege and grant policy exceptions with expiration dates, and the matrix records the same discipline for the authority they grant their AI. A team can adopt the matrix even before those broader practices mature, starting with a few rows.

> The Security Autonomy Matrix can record the five decisions for any AI agent in the enterprise, whether the agent screens résumés or pays invoices. This guide covers security workflows. To apply the matrix in another business function, keep the same columns and fill the rows with that function’s workflows.

## Decide how much autonomy each AI action gets.

A leader sets the AI’s autonomy level for each kind of action, such as reading data or deleting records. This involves considering the cost of a mistake in that action and whether someone can undo it. The Security Autonomy Matrix describes autonomy using five levels, ranging from a person doing all the work to AI acting on its own with after-the-fact audits.

A leader can keep costly, irreversible actions behind a person’s approval and leave the low-cost, reversible ones to the AI.

### Define AI autonomy in five levels, the way driving automation does.

The five autonomy levels in the Security Autonomy Matrix are an adaptation of the [SAE driving-automation levels](https://www.sae.org/standards/content/j3016_202104/), familiar from self-driving cars:

| Level | Name | Meaning |
| --- | --- | --- |
| L0 | Manual | A person does all the work. AI is not involved. |
| L1 | Advisory | AI recommends and drafts. A person performs every action, so nothing the AI produces takes effect on its own. |
| L2 | Supervised | AI performs the action. A person approves each one before it takes effect. |
| L3 | Conditional | AI acts within set limits. A person handles exceptions and escalations. |
| L4 | Independent | AI acts on its own. A person reviews by audit, after the fact. |

The biggest jump in what the AI does is from L1 to L2, where it starts performing actions...
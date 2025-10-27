---
title: The future of AI agents—and why OAuth must evolve
url: https://techcommunity.microsoft.com/blog/microsoft-entra-blog/the-future-of-ai-agents%E2%80%94and-why-oauth-must-evolve/3827391
source: Microsoft Security Blog
date: 2025-05-28
fetch_date: 2025-10-06T22:31:38.107428
---

# The future of AI agents—and why OAuth must evolve

[Skip to content](#main-content)[![Brand Logo](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/themes/customTheme1/favicon-1730836271365.png?time=1730836274203)](/)

[Tech Community](/)[Community Hubs](/Directory)

[Products](/)

[Topics](/)

[Blogs](/Blogs)[Events](/Events)

[Microsoft Learn](/category/MicrosoftLearn)

[Community](/)

[Register](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-entra-blog%2Fthe-future-of-ai-agents%25E2%2580%2594and-why-oauth-must-evolve%2F3827391)[Sign In](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-entra-blog%2Fthe-future-of-ai-agents%25E2%2580%2594and-why-oauth-must-evolve%2F3827391)

1. [Microsoft Community Hub](/)
3. [Communities](/category/communities)[Products](/category/products-services)[Microsoft Security](/category/microsoft-security)
5. [Microsoft Entra](/category/microsoft-entra)
7. [Microsoft Entra Blog](/category/microsoft-entra/blog/microsoft-entra-blog)

## Blog Post

Microsoft Entra Blog

5 MIN READ

# The future of AI agents—and why OAuth must evolve

[![Alex_Simons's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS01MzQ3Ny0xNDAwNGk5REQwMjI1MTVEMkUxQzc0?image-dimensions=50x50)](/users/alex_simons/53477)

[Alex\_Simons](/users/alex_simons/53477)

![Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

May 27, 2025

I believe we're at the beginning of something extraordinary.

Today's AI agents are already impressive—they're helping software engineers write code, assisting site reliability teams in troubleshooting systems, and handling a variety of analytical tasks. Yet, as capable as these specialized agents are becoming, we're just beginning to glimpse their potential. The next wave of changes is approaching fast, bringing capabilities that will transform how we work across a wide variety of fields.

At Microsoft, we believe the next 12–24 months will fundamentally change the AI agent space. Instead of simply responding to requests, agentic systems will start working independently, spotting problems, suggesting solutions, and carrying context across conversations. The difference might seem small at first, but you'll notice it when your agent starts to proactively help you solve problems rather than just follow instructions.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zODI3MzkxLXJOb01xVg?image-dimensions=999x322&revision=9)

To support this future, we need to evolve the identity standards that underpin how agents access data and act across connected systems—from APIs, code repositories, and data warehouses, to productivity tools, enterprise systems, and sensitive business processes. It starts with OAuth 2.

## What’s changing?

At Microsoft, we’re building a robust and sophisticated set of agents. Recently, we launched the public preview of our new Conditional Access Optimizer Agent. It’s a multi-functional AI agent that:

* Analyzes an organization’s Conditional Access policies
* Identifies security gaps
* Recommends policy improvements and simplifications
* Deploys new policies in pilot mode
* Ensures new users and apps are protected

We’ve also been extensively investing in agents for developer and operations workflows, such as the SWE and SRE agents to help teams boost their productivity when writing and maintaining their applications. As new AI-driven scenarios are introduced, we anticipate an emerging flood of rich, smart, multi-functional, and autonomous agents.

AI agents will augment and amplify the capabilities of an organization. Marketing agents could propose full digital marketing campaign plans, refine and update them based on feedback, and then when the plans are approved, execute them end-to-end. Engineering agents could autonomously create specifications for new features, as well as start to build and test them with minimal human interactions. You might’ve already seen [some of these experiences](https://www.youtube.com/watch?v=eVPHMMrORbA) at this year’s Microsoft Build conference. We could see all kinds of agents helping people to manage compliance, onboard new employees, or even run parts of their IT operations more efficiently.

But here’s the thing: today’s OAuth 2 standards weren’t built for the world of AI agents. Some existing efforts, like [RFC 9396 – OAuth 2.0 Rich Authorization Requests](https://datatracker.ietf.org/doc/rfc9396/), set some of the fundamental ideas in motion, but we believe we need a more scalable solution for AI-first scenarios.

## Why OAuth 2 needs an update

OAuth 2 works well for today’s task-focused agents that act on behalf of a user. But as agents become more autonomous and capable, a new set of authorization requirements surfaces. Agents need much more granular permissions, and they need to be dynamic, easily revokable, yet auditable. They need to be able to interact securely with other agents across different trust boundaries, as well as handle scenarios where the ownership of an agent changes on the fly. To enable these capabilities, we need to drive a set of changes to existing standards to support them, unlocking the ability of enterprises to adopt them while maintaining compliance and confidence in the security of their data.

### Here’s what we think needs to change:

1. **Recognize Agent IDs as first-class actors****:** Agents need to be distinct from clients. They should have their own identity in the OAuth model. When an agent registers with an IDP, it should be able to register as an agent, not a client. When an agent accesses a resource, it should be able to represent that it is an agent. When a computer-using agent accesses a resource through a client, we need a standards-based approach to represent this interaction.![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zODI3MzkxLWhJTXRidw?image-dimensions=608x195&revision=9)
2. **Have a standard model for granting agents their own permissions****:** Agents should be able to act with their own defined set of privileges—not just proxy a user’s rights.
3. **Make agent actions transparent and traceable****:** We need a clear way to distinguish when an agent is acting:

   * On behalf of a user
   * On its own behalf
   * On behalf of another agent or a chain of agents

   This is critical for forensics, policy enforcement, and trust.

   ![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zODI3MzkxLWxsV3Q5Ng?image-dimensions=466x530&revision=9)
4. **Enable permission discovery and delegation:** Agents should be able to discover the permissions required to perform a task and request them—either directly from the user, from an upstream agent, or through a chain of upstream agents ultimately linked to the user.![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zODI3MzkxLWNwRnlURg?image-dimensions=505x388&revision=9)
5. **Support for fine-grained, resource specific, least-privilege access****:** We need updates to the [OAuth scopes model](https://oauth.net/2/scope/) to support common approaches to identifying a specific subset of resources a user can delegate access to. For example:
   * A collection or container of resources, such as *all photos from last week*
   * A node in a hierarchy of resources, such as *all files in the /taxinfo directory*
   * A specific class or category of resource, like *high business impact or confidential*
   * A query, such as *SELECT \* FROM my\_emails WHERE sender LIKE ‘%@microsoft.com’*
   * A specific resource, like *{customer\_ID, 12345}*

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS0zODI3MzkxLUJZRHU5Ug?image-dimensions=550x238&revision=9)

We believe this set of targeted updates will give users and organizations the controls, visibility, specificity, and granularity ...
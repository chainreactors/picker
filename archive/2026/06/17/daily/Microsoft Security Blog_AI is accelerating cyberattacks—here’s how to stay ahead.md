---
title: AI is accelerating cyberattacks—here’s how to stay ahead
url: https://techcommunity.microsoft.com/blog/microsoft-entra-blog/ai-is-accelerating-cyberattacks%E2%80%94here%E2%80%99s-how-to-stay-ahead/4528592
source: Microsoft Security Blog
date: 2026-06-17
fetch_date: 2026-06-18T06:49:52.775382
---

# AI is accelerating cyberattacks—here’s how to stay ahead

Open Side Menu

[Skip to content](#main-content)[![Brand Logo](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/themes/customTheme1/favicon-1730836271365.png?time=1730836274203)](/)

[Tech Community](/)[Community Hubs](/Directory)

[Products](/)

[Topics](/)

[Blogs](/Blogs)

[Events](/Events)

[Skills Hub](/category/skills-hub)

[Community](/)

[Register](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-entra-blog%2Fai-is-accelerating-cyberattacks%25E2%2580%2594here%25E2%2580%2599s-how-to-stay-ahead%2F4528592)[Sign In](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-entra-blog%2Fai-is-accelerating-cyberattacks%25E2%2580%2594here%25E2%2580%2599s-how-to-stay-ahead%2F4528592)

1. [Microsoft Community Hub](/)
3. [Communities](/category/communities)[Products](/category/products-services)[Microsoft Security](/category/microsoft-security)
5. [Microsoft Entra](/category/microsoft-entra)
7. [Microsoft Entra Blog](/category/microsoft-entra/blog/microsoft-entra-blog)

## Blog Post

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTI4NTkyLXNlWXRKNw?revision=11&image-dimensions=2000x2000&constrain-image=true)

Microsoft Entra Blog

6 MIN READ

# AI is accelerating cyberattacks—here’s how to stay ahead

[![Sandeep Deo's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS02ODYzOC01MDI1NDJpNjhERUMyRjJDNzQ3REI0Mg?image-dimensions=50x50)](/users/sandeep%20deo/68638)

[Sandeep Deo](/users/sandeep%20deo/68638)

![Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Jun 17, 2026

## See how Microsoft unifies identity and security signals to help teams prevent, detect, and respond to AI-accelerated attacks faster.

In March, we wrote that identity security has become [the new pressure point for modern cyberattacks](https://www.microsoft.com/en-us/security/blog/2026/03/25/identity-security-is-the-new-pressure-point-for-modern-cyberattacks/). Since then, AI has only increased that pressure.

AI helps cyberattackers move faster across the attack chain: personalizing social engineering at scale, automating reconnaissance, analyzing leaked credentials, identifying privileged users, probing exposed systems, and adapting tactics in real time. Attacks that once depended on manual effort can now unfold with greater speed, scale, and autonomy.

Yet even as methods evolve, identity remains one of the most common entry points. Every account, admin, workload, application, [non-human identity](https://aka.ms/NHI-security-26), and AI agent can become a path to sensitive data and critical systems if not properly secured. Attackers do not need to break every defense; they only need to compromise or misuse the right identity with the right access at the right moment.

When attacks are accelerated by AI, speed and accuracy in detection and response are critical. Identity security can no longer operate in silos. Even a minor delay between when a threat is detected and action is taken can be the difference between suspicious activity becoming a contained incident or a business-impacting breach. This shift is reshaping how organizations think about security. The imperative is becoming clear: identity and security teams need comprehensive visibility and integrated solutions that streamline how they prevent, detect, and respond to identity threats.

## Securing the future of identity at the speed of AI

One of the biggest security challenges organizations face today is fragmentation, and identity security is no exception. IAM and SOC teams often work across separate tools, separate workflows, and separate operational models. But identity attacks don’t respect those organizational boundaries.

Modern identity attacks span infrastructure, access control, and detection. At Microsoft, we understand this, and we are continuing to expand how Microsoft Entra and Microsoft Defender work together to provide more unified identity security experiences.

### Actionable intelligence, everywhere

[At RSA earlier this year, we unveiled our unified identity risk score](https://www.microsoft.com/en-us/security/blog/2026/03/25/identity-security-is-the-new-pressure-point-for-modern-cyberattacks/), a new way to turn broader attack-chain insight into real-time access decisions. This score analyzes and correlates relevant signals across related accounts, sessions, workloads, and applications to surface a single, comprehensive evaluation of an identity’s true risk level and enable more dynamic response directly within authentication flows as part of risk-based Conditional Access policies.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTI4NTkyLXBpcTBYRw?image-dimensions=999x474&revision=11)*View of a risky user within Entra ID Protection with new identity risk score and attack timeline.*

Identity admins also gain a stronger operational experience through the new Microsoft Entra ID Protection experience. Rather than forcing identity teams to piece together risk signals across disconnected views, the updated experience brings deeper visibility into risky users, sign-ins, workloads, and associated detections in one place. The new identity risk score adds another layer of context by surfacing insights across related accounts and activity, including signals from Microsoft environments and connected identity activity beyond them. This helps admins understand whether a risky user, agent, workload, or sign-in is an isolated event or part of a broader pattern spanning sessions, applications, and associated accounts.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTI4NTkyLXVzdFVxTw?image-dimensions=936x738&revision=11)*New user dashboard in Entra ID Protection which provides deeper visibility for identity admins into risky users, sign-ins, and associated detections.*![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTI4NTkyLWRnRmxTeQ?image-dimensions=930x540&revision=11)*New risky user details view provides more information about a user's risk and the attack timeline within Entra ID Protection.*

That richer context gives identity teams a more complete view of how risk is developing across the identity estate. Admins can better understand how risk is calculated, which related accounts or workloads contributed to the score, what detections are driving concern, and why a given identity requires attention. By connecting Microsoft and cross-environment signals into a single evaluation, the risk score helps identity admins prioritize the identities that matter most, make more informed access decisions, and explain the rationale behind remediation actions with greater confidence.

For security operations teams, this new score helps prioritize and triage investigations faster by focusing analysts on the identities that pose the greatest risk. But knowing what to fix is only half the challenge. In many organizations, security operations teams lack the needed permissions to take action; instead, they can only wait for separate IAM workflows to resolve the issue. That delay creates friction during moments when response speed matters most. Some solutions address this by giving SOC teams, or the security application itself, broad standing permissions across the identity environment. That may solve the permissions issue, but it also expands the blast radius if the application or identity is misused or compromised.

Microsoft takes a different approach because our solution natively spans identity infrastructure, the identity control plane, and ITDR. Customers get streamlined workflows across the full identity security lifecycle, and with a new identity-focused RBAC role, coming soon in public preview, security operations teams can access the core identity respons...
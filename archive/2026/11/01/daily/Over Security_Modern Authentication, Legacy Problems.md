---
title: Modern Authentication, Legacy Problems
url: https://dfir.ch/posts/field_note_mha/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:22.533844
---

# Modern Authentication, Legacy Problems

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Modern Authentication, Legacy Problems

1 Nov 2026

**Table of Contents**

* [Introduction](#introduction)
* [Understanding Hybrid Modern Authentication](#understanding-hybrid-modern-authentication)
* [Modern Authentication Is Not Necessarily Exclusive](#modern-authentication-is-not-necessarily-exclusive)
* [Back To Our Incident Response Case](#back-to-our-incident-response-case)
* [How to Identify This Configuration](#how-to-identify-this-configuration)
  + [Checking Authentication Policies](#checking-authentication-policies)
* [How to Secure Hybrid Exchange](#how-to-secure-hybrid-exchange)
* [Conclusion](#conclusion)
* [References](#references)

## Introduction

During a recent incident response investigation, we encountered an interesting authentication issue in an on-premises Microsoft Exchange environment. The organization had implemented `Hybrid Modern Authentication` (HMA), allowing Microsoft Outlook to authenticate against Microsoft Entra ID using OAuth tokens. Multi-factor authentication was enforced through the organization’s Microsoft 365 configuration. However, while investigating the Exchange logs, we found thousands of successfully authenticated `EWS` requests from another client using `NTLM`.

How could `NTLM` authentication still succeed when the organization had implemented `Hybrid Modern Authentication` and required MFA? The answer was an externally accessible legacy authentication path that operated independently of Microsoft Entra ID.

## Understanding Hybrid Modern Authentication

In a traditional on-premises Exchange deployment, clients can authenticate directly against Exchange using mechanisms such as `Basic Authentication`, `NTLM` or `Kerberos`. Authentication is handled locally, typically with the help of Active Directory. `Hybrid Modern Authentication` introduces an additional mechanism. Instead of authenticating directly to Exchange using Windows authentication, a supported client obtains an OAuth access token from Microsoft Entra ID. Exchange then validates the token and grants access to the mailbox. The mailbox itself remains on-premises. Only the authentication and token issuance process involves the cloud identity provider.

![Hybrid Auth](/images/hybrid_auth/workflow.png "Hybrid Auth")

Figure 1: Example hybrid Exchange authentication architecture with federated identities (Source: Microsoft). This is an illustrative architecture, not a representation of the investigated environment.

A simplified authentication flow looks like this:

1. Outlook attempts to access an on-premises Exchange mailbox.
2. Outlook is directed to Microsoft Entra ID for authentication.
3. Microsoft Entra ID evaluates the applicable authentication requirements, including Conditional Access and MFA.
4. Following successful authentication, Outlook receives an OAuth access token.
5. Outlook presents the token to the on-premises Exchange server.
6. Exchange validates the token and grants access to the mailbox.

## Modern Authentication Is Not Necessarily Exclusive

One of the interesting details in Microsoft’s documentation is an example of an Exchange virtual directory configured with multiple authentication mechanisms (`IISAuthenticationMethods`):

* NTLM
* OAuth
* Negotiate

At first glance, this might appear contradictory. Why would NTLM still be enabled if the purpose of `Hybrid Modern Authentication` is to use OAuth? The explanation is that Exchange supports multiple client authentication mechanisms for compatibility. **Enabling OAuth does not necessarily mean that every existing authentication mechanism is disabled.** Microsoft explicitly documents the possibility of blocking legacy authentication in Exchange 2019 hybrid deployments through authentication policies. Importantly, Microsoft includes Windows authentication, meaning both `NTLM` and `Kerberos`, in the mechanisms that these policies can block.

## Back To Our Incident Response Case

The Exchange server was configured to support `Hybrid Modern Authentication`, and ordinary Outlook clients were successfully authenticating using `OAuth bearer tokens`. However, an additional client was accessing `Exchange Web Services` (EWS) through the endpoint `https://mail.example.com/EWS/Exchange.asmx`. The IIS logs contained large numbers of requests with a Mozilla Thunderbird user-agent. The Thunderbird user-agent was unusual in this environment, where most users accessed Exchange through Outlook and other Microsoft clients. Its high request volume and prolonged activity made it stand out during the initial log analysis.

Nevertheless, an unusual user-agent alone does not establish which authentication method was used. IIS logs typically tell us which URL was requested, which account was associated with the request, and how the server responded. They do not necessarily provide sufficient information to distinguish OAuth from NTLM. For that, we turned to the Exchange HttpProxy logs.

**Exchange HttpProxy Reveals the Authentication Method**

During the available logging period, we identified 66,610 successfully authenticated EWS requests associated with the Thunderbird user-agent. All used `NTLM` authentication. Interestingly, the same mailbox was also accessed by legitimate clients using `OAuth bearer tokens`. **The HttpProxy logs therefore demonstrated that Exchange accepted both authentication mechanisms for the same account.**

**Why NTLM Did Not Trigger MFA**

NTLM uses a challenge-response authentication mechanism. Rather than sending an OAuth bearer token issued by Microsoft Entra ID, the client proves possession of suitable authentication material through an exchange of cryptographic messages. In a domain environment, Exchange can validate the authentication through Windows and Active Directory infrastructure. Crucially, this process does not require an OAuth access token from Microsoft Entra ID. As a consequence, Microsoft Entra Conditional Access policies are not evaluated as part of this NTLM authentication flow.

This does not mean that NTLM automatically bypasses every conceivable MFA solution. An organization could enforce additional authentication at a reverse proxy or another access layer. However, such a control was not established by the available evidence in this case. The distinction matters because it would be misleading to say that the attacker defeated MFA. We found no evidence of MFA fatigue, stolen OAuth tokens, adversary-in-the-middle phishing against Entra ID or a vulnerability in the MFA implementation. Instead, the Exchange server accepted a different authentication method that never invoked Entra MFA in the first place.

It is also important to distinguish NTLM from HTTP Basic Authentication. Although both are considered legacy authentication mechanisms in this context, NTLM does not transmit the user’s plaintext password as part of an ordinary challenge-response exchange.

**Another Authentication Path: Outlook on the Web**

The EWS access was not the only interesting finding. We also observed successful access through `Outlook on the Web` (OWA). The corresponding Exchange HttpProxy records contained:

* Protocol: OWA
* AuthenticationType: FBA
* IsAuthenticated: true
* HttpStatus: 200

**FBA stands for Forms-Based Authentication, the traditional Exchange web login mechanism.** In the investigated environment, OWA accepted authentication directly at the on-premises Exchange server instead of redirecting the user to Microsoft Entra ID. This constituted a second authentication path outside the organization’s Entra MFA flow. It is worth mentioning that this is not an inherent limitation of OWA. Microsoft supports `Hybrid Modern Authentication for OWA` and the `Exchange Control Panel` (ECP) on supported Exchange versions. With the appropriate configuration, users accessing OWA can be redirected to Microsoft Entra ID for authentication. **However,...
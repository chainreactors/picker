---
title: Maestro
url: https://posts.specterops.io/maestro-9ed71d38d546?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-11-01
fetch_date: 2025-10-06T19:21:45.685086
---

# Maestro

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9ed71d38d546&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fmaestro-9ed71d38d546&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fmaestro-9ed71d38d546&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-9ed71d38d546---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-9ed71d38d546---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# **Maestro: Abusing Intune for Lateral Movement Over C2**

[![Chris Thompson](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*VB1kJkW5uCVpMaQ8)](https://medium.com/%40Mayyhem?source=post_page---byline--9ed71d38d546---------------------------------------)

[Chris Thompson](https://medium.com/%40Mayyhem?source=post_page---byline--9ed71d38d546---------------------------------------)

11 min read

·

Oct 31, 2024

--

Listen

Share

If I have a command and control (C2) agent on an Intune admin’s workstation, I should just be able to use their privileges to execute a script or application on an Intune-enrolled device, right?

Not so fast.

## I Wanna Go Fast!

* [Take me to the GitHub repo!](https://github.com/Mayyhem/Maestro)
* [Take me to the attack path walkthrough!](/maestro-9ed71d38d546#3530)
* [Take me to the defensive guidance!](/maestro-9ed71d38d546#66a5)

## The Problem

We often find ourselves in the context of a cloud administrator when following attack paths to objectives that require privileged access to Azure-hosted services. We want to use their Entra ID account’s privileges to execute actions in Azure, for example running arbitrary code on remote Intune devices (a.k.a. [the “Death from Above” attack path](/death-from-above-lateral-movement-from-azure-to-on-prem-ad-d18cb3959d4d) detailed by [Andy Robbins](https://x.com/_wald0)), but we have some hurdles to overcome to accomplish this from a C2 agent:

* We don’t have the user’s cleartext password
* Conditional access policies (CAPs) require multi-factor authentication (MFA) for access to the Intune Portal and/or a compliant, hybrid-joined device on a trusted network
* We need to maintain stealth
* We don’t have the knowledge, time, or patience to manipulate tokens and navigate the Azure portal or multiple tools

Let’s look at these problems one at a time and discuss the options available to us.

**No Cleartext Credentials / MFA Required**

No password? No problem. We already [asked the admin nicely for their creds](https://github.com/outflanknl/C2-Tool-Collection/tree/main/BOF/Askcreds) and they didn’t bite, and their password hygiene on the host is solid, but if the device has an identity in Entra ID, we can dump [primary refresh token](https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token) (PRT) cookies from the machine with tools like [Lee Chagolla-Christensen](https://x.com/tifkin_)’s [RequestAADRefreshToken](https://github.com/leechristensen/RequestAADRefreshToken), [Dirk-jan Mollema](https://x.com/_dirkjan)’s [ROADToken](https://github.com/dirkjanm/ROADtoken), [Evan McBroom](https://x.com/mcbroom_evan)’s [LSA Whisperer](https://github.com/EvanMcBroom/lsa-whisperer), [Daniel Heinsen](https://x.com/hotnops)’s, [SharpGetEntraToken](https://github.com/hotnops/SharpGetEntraToken), or [aad\_prt\_bof](https://github.com/wotwot563/aad_prt_bof) by [wotwot563](https://github.com/wotwot563). These PRT cookies will even have an MFA claim if Windows Hello for Business (WHfB) was used for logon, allowing us to comply with MFA requirements enforced by CAPs or the [new default security policy for Azure sign-in](https://azure.microsoft.com/en-us/blog/announcing-mandatory-multi-factor-authentication-for-azure-sign-in/).

**Stealth**

We want to only execute tools that are code-signed and legitimately used in the environment, otherwise keep tool execution within our current process or proxied into the environment from a machine we control that isn’t subject to the organization’s security stack.

We could use our shiny new PRT cookie to interact with Azure using a web browser proxied through the administrator’s workstation, but:

* fumbling through the portal requires prior experience or time to figure out, and features are added, removed, or moved all the time
* information made available by the Azure APIs we’re interested in is not always displayed to the user or is difficult to find
* we have to take frequent screenshots and manual activity logs for deconfliction and reporting instead of letting our C2 framework handle all that, gross
* we may still hit CAPs preventing access without a compliant and/or hybrid-joined device

We could use our C2 agent to run command line tools that are likely to be already installed on cloud administrator workstations (e.g., PowerShell’s Invoke-RestMethod, [Microsoft.Graph](https://github.com/microsoft/mggraph-intune-samples), [AzureAD](https://www.powershellgallery.com/packages/azuread/), or [Intune](https://github.com/microsoft/Intune-PowerShell-SDK) modules, curl.exe, etc.) and interact with Azure APIs, but they don’t directly support BYO PRT cookies, they require multiple steps to obtain refresh and access tokens after dumping a PRT cookie (let alone execute actions with those tokens), and they may generate suspicious parent/child process relationships and command line arguments.

We could dump refresh or access tokens from the memory of applications the cloud admin has used to authenticate to Entra ID (e.g., their browser, the ConfigMgr console in co-management setups, etc.) with tools like the [office\_tokens BOF](https://github.com/trustedsec/CS-Remote-OPs-BOF) from TrustedSec, but we need some luck to obtain creds with the correct client ID, scope, and resource for the actions we want to take or that can be [swapped for creds](https://github.com/secureworks/family-of-client-ids-research) that meet these requirements.

**Device Compliance / Hybrid-joined Device**

An appropriately scoped refresh or access token would enable us to proxy in excellent open-source tools like [ROADTools](https://github.com/dirkjanm/ROADtools), [AADInternals](https://github.com/Gerenios/AADInternals), [BARK](https://github.com/BloodHoundAD/BARK), [AzureHound](https://github.com/BloodHoundAD/AzureHound), [TokenTactics](https://github.com/rvrsh3ll/TokenTactics)/[TokenTacticsV2](https://github.com/f-bader/TokenTacticsV2), or [GraphRunner](https://github.com/dafthack/GraphRunner), but we still may be blocked by CAPs requiring device compliance or a hybrid-joined device when exchanging refresh tokens for access tokens or by [Continuous Access Evaluation](https://learn.microsoft.com/en-us/entra/ide...
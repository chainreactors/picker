---
title: ConsentFix (a.k.a. AuthCodeFix): Detecting OAuth2 Authorization Code Phishing
url: https://blog.nviso.eu/2026/01/29/consentfix-a-k-a-authcodefix-detecting-oauth2-authorization-code-phishing/
source: NVISO Labs
date: 2026-01-29
fetch_date: 2026-01-30T04:02:40.394854
---

# ConsentFix (a.k.a. AuthCodeFix): Detecting OAuth2 Authorization Code Phishing

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# ConsentFix (a.k.a. AuthCodeFix): Detecting OAuth2 Authorization Code Phishing

[Stamatis Chatzimangou](https://blog.nviso.eu/author/stamatis-chatzimangou/ "Posts by Stamatis Chatzimangou")

[Blue Team](https://blog.nviso.eu/category/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/), [Cyber Threats](https://blog.nviso.eu/category/cyber-threats/), [phishing](https://blog.nviso.eu/category/phishing/), [Threat Hunting](https://blog.nviso.eu/category/threat-hunting/)

January 29, 2026January 29, 2026
14 Minutes

ConsentFix (a.k.a. AuthCodeFix) is the latest variant of the fix-type phishing attacks, initially identified by Push Security[1](#d71447a2-9b1b-4f77-beaf-bbaedb95b4c8). In this technique, the adversary tricks the victim into generating an OAuth authorization code that is part of a localhost URL by signing in to the Azure CLI instance (or other vulnerable applications). Then, the victim is instructed to copy that URL and paste it into a phishing website, essentially handing over the authorization code to the adversary, who is now able to exchange it for an access token. Using the access token, the adversary gets access to the victim’s Microsoft account.

In this blog post, we dive into the mechanics of the attack and explore detection and mitigation strategies for it.

## OAuth 2.0 Authorization Framework

The attack relies heavily on the OAuth2 authorization framework, so to better understand the mechanics**,** we will briefly go through OAuth2’s inner workings.

OAuth2 (Open Authorization) is a standard authorization framework that allows users to grant third-party applications scoped access to specific resources or data on other services (e.g., Microsoft, Google, Facebook) for a limited amount of time, without sharing their usernames and passwords with those applications.

OAuth2 was developed to prevent users from sharing their credentials with third-party apps that require access to their data as part of their functionality. It lets users grant access via a secure flow managed by a trusted provider (e.g., Microsoft, Google). Users sign in with that provider and approve a request, after which the app receives an access token that permits access only to the required data.

OAuth2 uses the following terms[2](#e4101bf5-9475-4cfc-b3a0-0ede21c9adbe) to describe the authorization workflow:

* **Resource Owner** – The user who owns the data that the application wants to access and authorizes the application.
* **Client** – The application that requests access to the data of the user.
* **Authorization Server** – The service that authenticates the users and grants access tokens to the application.
* **Resource Server** – The service that holds the user’s data.

A typical implementation of the OAuth2 authorization flow (Authorization Code Grant) is the following:

![](https://blog.nviso.eu/wp-content/uploads/2026/01/OAuth-Protocol.drawio-7.png)

OAuth2 authorization flow

Since this attack revolves around Microsoft’s Identity platform, we are also including below the OAuth2 authorization code flow implementation from Microsoft’s documentation[3](#41ee354e-db55-4d6a-854b-1bf3ab40ae78).

![Diagram shows OAuth authorization code flow. Native app and Web A P I interact by using tokens as described in this article.](https://learn.microsoft.com/en-us/entra/identity-platform/media/v2-oauth2-auth-code-flow/convergence-scenarios-native.svg)

OAuth2 Microsoft’s authorization flow ([source](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow#protocol-details))

## ConsentFix Attack Flow and Mechanics

The attack is executed by following multiple steps:

1. The adversary compromises (watering hole) or creates a malicious phishing page prompting the victim to enter an email address.
2. The victim visits the phishing page, typically via a search engine, and enters their email address.
3. The victim is redirected to login.microsoftonline.com to authenticate and authorize an application to access their account. If already authenticated, the victim may not need to enter an email, password, or perform MFA, as it is possible to select the existing session/account from a list.
4. After authentication and authorization, the victim is redirected to a localhost application URL in the browser. The redirection URL contains an authorization code that would normally be consumed by the legitimate application initiating the flow (step 4 in the authorization workflow). Because the authorization flow did not start from a legitimate application and no application is listening on localhost to receive the code, the victim encounters a 404 “This site can’t be reached” message. The adversary exploits this by instructing the victim to copy and paste the URL containing the authorization code back into the phishing site if that error appears.
5. With the authorization code, the adversary exchanges it using Microsoft’s /oauth2/v2.0/token API for an access token.
6. Using the access token (a.k.a. Bearer token), the adversary accesses the user’s Microsoft account and resources.

![](https://blog.nviso.eu/wp-content/uploads/2026/01/consent-fix-attack-flow.drawio-6-1024x1018.png)

ConsentFix attack flow ([phishing prompts source](https://pushsecurity.com/blog/consentfix))

### Why does this attack work?

The original blog post mentions that Azure CLI was the primary target of the ConsentFix attack, and there is a reason for that. Azure CLI is a first-party Microsoft application, which means it is implicitly trusted by Entra ID. As a result, users are not shown an “I accept these permissions” consent prompt during authentication.

![](https://blog.nviso.eu/wp-content/uploads/2026/01/image-9.png)

Permission consent prompt example ([source](https://learn.microsoft.com/en-us/security/zero-trust/develop/permissions-require-admin-consent))

First-party applications, like Azure CLI, are pre-consented by default. This allows them to request permissions without triggering a user consent dialog or requiring administrator approval. This behavior is by design, as Microsoft wants tools such as Azure CLI, Azure PowerShell, and Visual Studio to work seamlessly for every user without administrative intervention. The attack will also work against any user in the tenant, regardless of whether they have ever used the targeted application befo...
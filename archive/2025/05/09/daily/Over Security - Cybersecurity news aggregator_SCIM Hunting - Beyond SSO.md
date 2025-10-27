---
title: SCIM Hunting - Beyond SSO
url: https://blog.doyensec.com/2025/05/08/scim-hunting.html
source: Over Security - Cybersecurity news aggregator
date: 2025-05-09
fetch_date: 2025-10-06T22:29:32.582111
---

# SCIM Hunting - Beyond SSO

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2025 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# SCIM Hunting - Beyond SSO

08 May 2025 - Posted by Francesco Lacerenza

## Introduction

Single Sign-On (SSO) related bugs have gotten an incredible amount of hype and a lot of amazing public disclosures in recent years. Just to cite a few examples:

* [Common OAuth Vulnerabilities](https://blog.doyensec.com/2025/01/30/oauth-common-vulnerabilities.html)
* [Sign in as anyone: Bypassing SAML SSO authentication with parser differentials](https://github.blog/security/sign-in-as-anyone-bypassing-saml-sso-authentication-with-parser-differentials/)
* [Account hijacking using âdirty dancingâ in sign-in OAuth-flows](https://labs.detectify.com/writeups/account-hijacking-using-dirty-dancing-in-sign-in-oauth-flows/)

And so on - there is a lot of gold out there.

However, while SSO often takes center stage, another standard is often under-tested - **SCIM (System for Cross-domain Identity Management)**. In this blogpost we will dive into its core aspects & the insecure design issues we often find while testing our clientsâ implementations.

![SCIM](../../../public/images/scim.png)

## Table of Contents

1. [SCIM 101](#scim-101)
   * [Core Components](#core-components)
   * [What about the implementations?](#what-about-the-implementations)
   * [Mind The Impact](#mind-the-impact)
2. [Hunting for Bugs](#hunting-for-bugs)
   * [Auth Bypasses](#auth-bypasses)
   * [SCIM Token Management](#scim-token-management)
   * [Unwanted User Re-provisioning Fallbacks](#unwanted-user-re-provisioning-fallbacks)
   * [Internal Attributes Manipulation](#internal-attributes-manipulation)
   * [Verification Bypasses](#verification-bypasses)
   * [Account Takeover](#account-takeover)
3. [Extra Focus Areas](#extra-focus-areas)
   * [Checks Bypass Via SCIM Ops Syntax](#extra-checks-bypass-via-scim-ops-syntax)
   * [Bulk Ops Order Evaluation](#extra2-bulk-ops-order-evaluation)
   * [JSON Interoperability](#json-interoperability)
4. [Conclusions](#conclusions)

## SCIM 101

SCIM is a standard designed to automate the provisioning and deprovisioning of user accounts across systems, ensuring access consistency between the connected parts.

The standard is defined in the following RFCs: [RFC7642](https://datatracker.ietf.org/doc/html/rfc7642), [RFC7644](https://datatracker.ietf.org/doc/html/rfc7644), [RFC7643](https://datatracker.ietf.org/doc/html/rfc7643).

While it is **not specifically designed to be an IdP-to-SP protocol**, rather a generic user pool syncing protocol for cloud environments, real-world scenarios mostly embed it in the IdP-SP relationship.

#### Core Components

To make a long story short, the standard defines a set of RESTful APIs exposed by the Service Providers (SP) which should be callable by other actors (mostly Identity Providers) to update the users pool.

![Image 1](../../../public/images/scim-diagram.png)
![Image 2](../../../public/images/scim_resource_examples.png)

It provides REST APIs with the following set of operations to edit the managed objects (see [scim.cloud](https://scim.cloud/)):

* **Create**: POST `https://example-SP.com/{v}/{resource}`
* **Read**: GET `https://example-SP.com/{v}/{resource}/{id}`
* **Replace**: PUT `https://example-SP.com/{v}/{resource}/{id}`
* **Delete**: DELETE `https://example-SP.com/{v}/{resource}/{id}`
* **Update**: PATCH `https://example-SP.com/{v}/{resource}/{id}`
* **Search**: GET `https://example-SP.com/{v}/{resource}?<SEARCH_PARAMS>`
* **Bulk**: POST `https://example-SP.com/{v}/Bulk`

So, we can summarize SCIM as a set APIs usable to perform CRUD operations on a set of JSON encoded objects representing user identities.

**Core Functionalities**

If you want to look into a SCIM implementation for bugs, here is a list of core functionalities that would need to be reviewed during an audit:

1. **Server Config & Authn/z Middlewares** - SCIM does not define its authn/authz method, hence it will always be custom
2. **SCIM Object to Internal Objects Mapping Function** - How the backend is converting / linking the SCIM objects to the internal *Users* and *Groups* objects. Most of the times they are more complex and have tons of constraints `& ||` safety checks.
3. **Operations Exec Logic** - Changes within identity-related objects typically trigger application flows. A few examples include: `email` *update* should trigger a confirmation flow / flag the user as unconfirmed, `username` *update* should trigger ownership / pending invitations / re-auth checks and so on.

#### Mind The Impact

As direct IdP-to-SP communication, most of the resulting issues will require a certain level of access either in the IdP or SP. Hence, the complexity of an attack may lower most of your findings.
Instead, the impact might be skyrocketing in *Multi-tenant Platforms* where SCIM Users may lack tenant-isolation logic common.

## Hunting for Bugs

The following are some juicy examples of bugs you should look for while auditing SCIM implementations.

### Auth Bypasses

A few months ago we published our advisory for an [*Unauthenticated SCIM Operations In Casdoor IdP Instances*](https://doyensec.com/resources/Doyensec_Advisory_UnauthenticatedSCIM-CasdoorIdP.pdf). It is an open-source identity solution supporting various auth standards such as OAuth, SAML, OIDC, etc. Of course SCIM was included, but as a service, meaning the Casdoor (IdP) would also allow external actors to manipulate its users pool.

Casdoor utilized the [elimity-com/scim](https://github.com/elimity-com/scim/) library, which, by default, does not include authentication in its configuration as per the standard. Consequently, a SCIM server defined and exposed using this library remains unauthenticated.

```
server := scim.Server{
 Config: config,
 ResourceTypes: resourceTypes,
 }
```

Exploiting an instance required emails matching the configured domains. A SCIM POST operation was usable to create a new user matching the internal email domain and data.

```
â curl --path-as-is -i -s -k -X $'POST' \
 -H $'Content-Type: application/scim+json'-H $'Content-Length: 377' \
 --data-binary $â{\"active\":true,\"displayName\":\"Admin\",\"emails\":[{\"value\":
\"admin2@victim.com\"}],\"password\":\"12345678\",\"nickName\":\"Attacker\",
\"schemas\":[\"urn:ietf:params:scim:schemas:core:2.0:User\",
\"urn:ietf:params:scim:schemas:extension:enterprise:2.0:User\"],
\"urn:ietf:params:scim:schemas:extension:enterprise:2.0:User\":{\"organization\":
\"built-in\"},\"userName\":\"admin2\",\"userType\":\"normal-user\"}' \
 $'https://<CASDOOR_INSTANCE>/scim/Users'
```

Then, authenticate to the IdP dashboard with the new admin user `admin2:12345678`.

**Note**: The maintainers released a new version (v1.812.0), which includes a fix.

While that was a very simple yet critical issue, bypasses could be found in authenticated implementations. In other cases the service could be available only internally and unprotected.

### SCIM Token Management

*[\*] IdP-Side Issues*

Since SCIM secrets allow dangerous actions on the *Service Providers*, they should be protected from extractions happening after the setup. Testing or editing an IdP SCIM integration on a configured application should require a new SCIM token in input, if the connector URL differs from the one previously set.

A famous IdP was found to be issuing the SCIM integration test requests to `/v1/api/scim/Users?startIndex=1&count=1` with the old secret while accepting a new `baseURL`.

*+1 Extra - Cove...
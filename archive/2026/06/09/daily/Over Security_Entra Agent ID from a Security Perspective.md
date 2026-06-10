---
title: Entra Agent ID from a Security Perspective
url: https://blog.compass-security.com/2026/06/entra-agent-id-from-a-security-perspective/
source: Over Security
date: 2026-06-09
fetch_date: 2026-06-10T06:17:02.442723
---

# Entra Agent ID from a Security Perspective

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Entra Agent ID from a Security Perspective](https://blog.compass-security.com/2026/06/entra-agent-id-from-a-security-perspective/ "Entra Agent ID from a Security Perspective")

[June 9, 2026](https://blog.compass-security.com/2026/06/entra-agent-id-from-a-security-perspective/ "Entra Agent ID from a Security Perspective")
 /
[Christian Feuchter](https://blog.compass-security.com/author/cfeuchte/ "Posts by Christian Feuchter")
 /
[0 Comments](https://blog.compass-security.com/2026/06/entra-agent-id-from-a-security-perspective/#respond)

Microsoft Entra Agent ID introduces dedicated identity concepts for AI agents in Entra ID. While agent identities are based on the existing service principal infrastructure, they add agent-specific objects and relationships such as agent blueprints, blueprint principals, agent identities, agent users, and dedicated authentication flows.

From a security perspective, the important question is not only whether such agents exist in a tenant. It is also important to understand how agent identities differ from traditional service principals, such as enterprise applications. This includes identifying who controls them, how they authenticate, and what they can access.

## Introduction

This post does not aim to provide a complete technical introduction to every Entra Agent ID object or authentication flow. These concepts are only summarized briefly to provide enough context for the security-relevant observations in the following sections.

### New Agent ID Objects

With Entra Agent ID, Microsoft introduced several new objects and relationships for representing AI agents in Entra ID. These objects differ from the traditional App Registration and Enterprise Application model.

In the traditional model, the relationship is usually relatively simple: an app registration defines the application, and an enterprise application represents the tenant-specific service principal. With Entra Agent ID, this model becomes more layered. Depending on the scenario, the relevant objects may include an agent blueprint, a blueprint principal, one or more agent identities, and optionally agent users.

[![Microsoft Entra Agent ID diagram showing how an agent blueprint, blueprint principal, agent identities, and agent users relate to each other in the service principal model.](https://blog.compass-security.com/wp-content/uploads/2026/06/image-8.png)](https://blog.compass-security.com/wp-content/uploads/2026/06/image-8.png)

The blueprint acts as the template for the blueprint principal and contains global configuration, including credentials and required resource access. Conceptually, this is similar to the role of an app registration.

The blueprint principal represents a tenant-specific instance of the blueprint. It is comparable to an enterprise application, but it mainly manages agent identities for the blueprint rather than acting as the agent identity itself.

The agent identity is the primary account used by an AI agent to authenticate to various systems. A blueprint principal can be associated with multiple agent identities.

An agent user is an optional secondary account that an AI agent can use to authenticate to various systems. It behaves more like a regular user account than a service principal.

### Credentials

The new objects also need a way to authenticate. Different credential types are supported:

* Client Secrets
* Certificates
* Federated Credentials

An important difference compared to the traditional enterprise application model is that credentials are configured only on the blueprint itself. Based on my testing, credentials could not be added directly to the blueprint principal or agent identity:

[![Microsoft Entra Agent ID credentials diagram showing that authentication credentials such as client secrets, certificates, and federated credentials are stored only on the agent blueprint.](https://blog.compass-security.com/wp-content/uploads/2026/06/image-1.png)](https://blog.compass-security.com/wp-content/uploads/2026/06/image-1.png)

### New Authentication Flows

Entra Agent ID also introduces dedicated authentication flows. The important difference is that agent identities and agent users do not authenticate like traditional service principals.

Instead, agent identities use a token-exchange model. The agent identity blueprint authenticates with its own credential and obtains an exchange token for a specific child agent identity. The agent identity then uses this exchange token as a client assertion to obtain the final access token for the target resource. This separation matters because the blueprint holds the authentication credentials, while the agent identity holds the permissions. A compromise of the blueprint credentials may therefore affect all child agent identities associated with it.

There are three authentication flows:

* Autonomous agent app OAuth flow[1](#2cdd02fe-4255-49b7-9bf2-39c53d96a8ff)
* On-behalf-of OAuth flow[2](#f246db8f-8900-4f9e-96fd-ee405a4b7b87)
* Agent’s user account OAuth flow[3](#c4f8c574-c2a4-405b-a28e-41ccc834d321)

For this research, I patched the PowerShell authentication tool [EntraTokenAid](https://github.com/zh54321/EntraTokenAid) to support these authentication flows. It is used for the examples in this blog post.

## Security-Relevant Capabilities

Agent identities and agent users can receive different forms of authorization, including group memberships, Entra ID role assignments, OAuth2 delegated permission grants, and application permission grants (app roles).

### Entra ID Roles

Microsoft restricts the assignment of certain highly privileged Entra ID roles to agent identities and agent users. For example, the Global Administrator or Group Administrator role cannot be assigned. In addition, agent identities and agent users cannot be added as members or owners of role-assignable groups.

However, some privileged roles can still be assigned, such as Exchange Administrator and Windows 365 Administrator. The latter may be particularly relevant because it can manage security groups.

During testing, I also noticed a documentation gap: the Security Reader role is missing from the official list of roles that can be assigned to agent identities and agent users. A pull request was created to address this[4](#355afd8e-0f2a-4a00-ae64-fd612da3fda6).

### Azure RBAC Roles

Agent identities can be assigned Azure RBAC roles, such as Owner. During testing, I did not observe any Azure RBAC role assignment restrictions for agent identities. As a result, agent identities and agent users may have privileged access to sensitive Azure resources.

### API Permissions

API privileges become more complex with Entra Agent ID because permission-related configuration can exist on several different objects. Depending on the scenario, privileges may be declared, inherited, or directly assigned through different parts of the agent identity model:

* Agent Blueprint: required resource access
* Agent Blueprint: inheritable permission
* Agent Blueprint Principal
* Agent Identity

Understanding these scenarios is important for assessing exposure and identifying potential abuse paths.

#### General API Permissions Limitation

For security reasons, Microsoft blocks certain API permissions for agent identities, both delegated and application permissions[5](#839d4659-78cf-4d2b-9868-5706a112cc04). For example, an agent identity cann...
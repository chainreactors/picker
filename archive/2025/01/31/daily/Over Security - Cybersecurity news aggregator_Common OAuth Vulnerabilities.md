---
title: Common OAuth Vulnerabilities
url: https://blog.doyensec.com/2025/01/30/oauth-common-vulnerabilities.html
source: Over Security - Cybersecurity news aggregator
date: 2025-01-31
fetch_date: 2025-10-06T20:13:59.106747
---

# Common OAuth Vulnerabilities

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

# Common OAuth Vulnerabilities

30 Jan 2025 - Posted by Jose Catalan, Szymon Drosdzol

OAuth2âs popularity makes it a prime target for attackers. While it simplifies user login, its complexity can lead to misconfigurations that create security holes. Some of the more intricate vulnerabilities keep reappearing because the protocolâs inner workings are not always well-understood. In an effort to change that, we have decided to write a comprehensive guide on known attacks against OAuth implementations. Additionally, we have created a comprehensive checklist. It should prove useful for testers and developers alike to quickly assess whether their implementation is secure.

**Download the OAuth Security Cheat Sheet Now!** [Doyensec\_OAuth\_CheatSheet.pdf](https://doyensec.com/resources/Doyensec_OAuth_CheatSheet.pdf).

# OAuth Introduction

## OAuth Terminology

OAuth is a complex protocol with a many actors and moving parts. Before we dive into its inner workings, letâs review its terminology:

* **Resource Owner**: Entity that can grant access to a protected resource. Typically, this is the end-user.
* **Client**: Application requesting access to a protected resource on behalf of the Resource Owner.
* **Resource Server**: Server hosting the protected resources. This is the API you want to access.
* **Authorization Server**: Server that authenticates the Resource Owner and issues Access Tokens after getting proper authorization. For example, [Auth0](https://auth0.com/).
* **User Agent**: Agent used by the Resource Owner to interact with the Client (for example, a browser or a native application).

### References

* OAuth 2.0 RFC: <https://datatracker.ietf.org/doc/html/rfc6749>
* OAuth Terminology: [#oauth-2-0-terminology](https://auth0.com/docs/get-started/authentication-and-authorization-flow/which-oauth-2-0-flow-should-i-use#oauth-2-0-terminology)

## OAuth Common Flows

Attacks against OAuth rely on challenging various assumptions the authorization flows are built upon. It is therefore crucial to understand the flows to efficiently attack and defend OAuth implementations. Hereâs the high-level description of the most popular of them.

## Implicit Flow

The Implicit Flow was originally designed for native or single-page apps that cannot securely store Client Credentials. However, its use is now discouraged and is not included in the OAuth 2.1 specification. Despite this, it is still a viable authentication solution within Open ID Connect (OIDC) to retrieve `id_tokens`.

In this flow, the User Agent is redirected to the Authorization Server. After performing authentication and consent, the Authorization Server directly returns the Access Token, making it accessible to the Resource Owner. This approach exposes the Access Token to the User Agent, which could be compromised through vulnerabilities like XSS or a flawed `redirect_uri` validation. The implicit flow transports the Access Token as part of the URL if the `response_mode` is not set to `form_post`.

![OAuth Implicit Flow](../../../public/images/oauth-implicit-flow.png)

### References

* <https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.2>
* <https://datatracker.ietf.org/doc/html/rfc6749#section-4.2>
* <https://auth0.com/docs/get-started/authentication-and-authorization-flow/implicit-flow-with-form-post>

## Authorization Code Flow

The Authorization Code Flow is one of the most widely used OAuth flows in web applications. Unlike the Implicit Flow, which requests the Access Token directly to the Authorization Server, the Authorization Code Flow introduces an intermediary step. In this process, the User Agent first retrieves an Authorization Code, which the application then exchanges, along with the Client Credentials, for an Access Token. This additional step ensures that only the Client Application has access to the Access Token, preventing the User Agent from ever seeing it.

This flow is suitable exclusively for confidential applications, such as Regular Web Applications, because the application Client Credentials are included in the code exchange request and they must be kept securely stored by the Client Application.

![OAuth Authorization Code Flow](../../../public/images/oauth-authorization-code-flow.png)

### References

* <https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.1>
* <https://datatracker.ietf.org/doc/html/rfc6749#section-4.1>
* <https://cloudentity.com/developers/basics/oauth-grant-types/authorization-code-flow/>

## Authorization Code Flow with PKCE

OAuth 2.0Â provides a version of the Authorization Code Flow which makes use of a Proof Key for Code Exchange (PKCE). This OAuth flow was originally designed for applications that cannot store a Client Secret, such as native or single-page apps but it has become the main recommendation in the [OAuth 2.1 specification](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-01).

Two new parameters are added to the default Authorization Code Flow, a random generated value called `code_verifier` and its transformed version, the `code_challenge`.

1. First, the Client creates and records a secret `code_verifier` and derives a transformed version `t(code_verifier)`, referred to as the `code_challenge`, which is sent in the Authorization Request along with the transformation method `t_m` used.
2. The Client then sends the Authorization Code in the Access Token Request with the `code_verifier` secret.
3. Finally, the Authorization Server transforms `code_verifier` and compares it to `t(code_verifier)`

The available transformation methods (`t_m`) are the following:

* plain
  `code_challenge = code_verifier`
* S256
  `code_challenge = BASE64URL-ENCODE(SHA256(ASCII(code_verifier)))`

Note that using the default Authorization Code flow with a custom `redirect_uri` scheme like `example.app://` can allow a malicious app to register itself as a handler for this custom scheme alongside the legitimate OAuth 2.0 app. If this happens, the malicious app can intercept the authorization code and exchange it for an Access Token. For more details, refer to OAuth Redirect Scheme Hijacking.

With PKCE, the interception of the Authorization Response will not allow the previous attack scenario since attackers would only be able to access the `authorization_code` but it wonât be possible for them to get the `code_verifier` value required in the Access Token Request.

The diagram below illustrates the Authorization Code flow with PKCE:

![OAuth Authorization Code Flow with PKCE](../../../public/images/oauth-authorization-code-pkce-flow.png)

### References

* <https://datatracker.ietf.org/doc/html/rfc7636>

## Client Credentials Flow

The Client Credentials Flow is designed for Machine-to-Machine (M2M) applications, such as daemons or backend services. It is useful when the Client is also the Resource Owner, eliminating the need for User Agent authentication. This flow allows the Client to directly retrieve an Access Token by providing the Client Credentials.

The diagram below illustrates the Client Credentials Flow:

![OAuth Client Credentials Flow](../../../public/images/oauth-client-credentials-flow.png)

### References

* <https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.4>
* <https://datatracker.ietf.org/doc/html/rfc6749#section-4.4>

## Device Authorization Flow

The Device Authorization Flow is designed for Internet-connected devices that either lack a browser for use...
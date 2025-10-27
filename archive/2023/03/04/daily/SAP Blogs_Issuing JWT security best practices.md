---
title: Issuing JWT security best practices
url: https://blogs.sap.com/2023/03/03/issuing-jwt-security-best-practices/
source: SAP Blogs
date: 2023-03-04
fetch_date: 2025-10-04T08:37:53.017475
---

# Issuing JWT security best practices

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Issuing JWT security best practices

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161854&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Issuing JWT security best practices](/t5/technology-blog-posts-by-sap/issuing-jwt-security-best-practices/ba-p/13561859)

![cnvergence](https://avatars.profile.sap.com/f/8/idf8a13ccaee1ee9bcf249cf609c4ad4058051a2738717a526826f0a4de300eff6_small.jpeg "cnvergence")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[cnvergence](https://community.sap.com/t5/user/viewprofilepage/user-id/125937)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161854)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161854)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561859)

‎2023 Mar 03
8:13 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161854/tab/all-users "Click here to see who gave kudos to this post.")

4,795

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)

* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)

View products (1)

I'm part of the Kyma team working on Istio and API Gateway features. In this blog post, I'm going to discuss best practices for issuing JSON Web Tokens (JWTs).

### Overview

JSON Web Tokens (JWTs) are a popular way to securely transmit information between parties. Because the tokens can be signed and encrypted to ensure their integrity and confidentiality, they're often used for authentication and authorization purposes. As the use of JSON Web Tokens (JWTs) is becoming more widespread, it's important to follow best practices to ensure that the tokens are secure and can be trusted. The Internet Engineering Task Force (IETF) has published a set of best practices for JWTs in RFC 8725. In this blog post, I'd like to highlight some key points from the RFC to help you issue secure JWTs.

### Best practices

#### Set the **alg** header parameter in JWSs

Signed JWTs carry an explicit indication of the signing algorithm in the **alg** header parameter. However, this can lead to vulnerabilities if the algorithm is not properly validated. For example, an attacker might change the algorithm to `none`. Some libraries might trust this value and validate the JWT without checking its signature. To mitigate this risk, ensure that the **alg** or **enc** JWT header specifies the same algorithm that is used for the cryptographic operation. The **alg** (algorithm) header parameter in JSON Web Signature (JWS) specifies the cryptographic algorithm used to sign the JWT. It's important to ensure that the JWT is signed with the intended algorithm. The server should also verify that the algorithm is on the allowlist of approved algorithms and reject any JWTs with an unrecognized algorithm.

#### Set the **enc** header parameter in JWEs

Similarly to the **alg** header in JWSs, the **enc** (encryption) header parameter in a JSON Web Encryption (JWE) specifies the cryptographic algorithm used to encrypt a JWT. It's important to ensure that a JWT is encrypted with the intended algorithm. The server should also verify that the algorithm is on the allowlist of approved algorithms and reject any JWTs with an unrecognized algorithm.

#### Avoid using the `none` algorithm in JWT

Unless a JWT is cryptographically protected end-to-end by TLS in the transport layer or by any other means, the `none` algorithm should not be used in production environments, as it does not provide any cryptographic protection for the JWT. Use the `none` algorithm only for development purposes, and even in this case, proceed with caution.

##### Avoid using unsafe or deprecated algorithms

Avoid using unsafe or deprecated algorithms in JWTs. As unsafe, consider those algorithms which have known vulnerabilities or are superseded by newer and more secure ones. The algorithm used to sign a JWT should be appropriate for the needed level of security. As an example, RSA-PKCS1 v1.5 encryption algorithms should be avoided.

#### Remember about key management practices

JWTs rely on the security of the underlying cryptographic keys. Keyed MAC algorithms can be vulnerable to brute-force attacks if they are used to sign tokens with weak symmetric keys, such as human-memorizable passwords. To mitigate this risk, avoid using symmetric signing whenever possible. Nowadays, there are not many use cases where using symmetric instead of asymmetric signing is needed. If symmetric signing must be used, make sure that human-memorizable passwords are not directly used as the key to a keyed-MAC algorithm like HS256. Use secure key management practices, such as rotating keys regularly and protecting them from unauthorized access. To prevent unauthorized access, use strong passwords or passphrases for symmetric keys and protect private keys with appropriate permissions and access controls. Cryptographic keys used in JWTs should be of sufficient size to ensure their security. For example, the minimum recommended size for an RSA key is 2048 bits. Use keys of adequate size to avoid potential vulnerabilities.

#### Avoid compression before encryption

Data should not be compressed before encryption, as it can reveal information about the plaintext and weaken the security of a JWT.

#### Use only UTF-8 encoding

JWTs should only use UTF-8 encoding because other encodings, such as UTF-16 and UTF-32, are not allowed by the latest JSON standard (RFC 8259). Ensure that each JWT is properly encoded and not susceptible to injection attacks.

#### Always use HTTPS

JWTs should be transmitted over HTTPS to ensure their confidentiality and integrity. Using HTTP instead of HTTPS can leave JWTs vulnerable to man-in-the-middle attacks.

#### Use short expiration times

JWTs should have short expiration times to reduce the window of opportunity for attackers to use them. The short expiration times also help mitigate the impact of a JWT being compromised. It's generally advised not to set the expiration time to more than a few hours. You can adjust it using the **exp** (expiration) claim in a JWT.

#### Use JWT claims appropriately

Use JWT claims appropriately and only include the necessary amount of information. For example, don't include sensitive information like passwords in a JWT.

#### Prevent replay attacks

Replay attacks occur when an attacker intercepts a JWT and tries to use it multiple times to gain unauthorized access to protected resources. To prevent this type of attack, consider using the **jti** (JWT ID) claim. This claim is a unique identifier that can be used to prevent a JWT from being used more than once. You can also prevent replay attacks by including a **nonce** in authenticated requests.

#### Follow good security practices

Finally, follow good security practices in general to protect JWTs against threats....
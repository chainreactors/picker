---
title: All About Attacking JWT
url: https://infosecwriteups.com/all-about-attacking-jwt-9770f2b9d087?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-02
fetch_date: 2025-10-04T05:28:44.587594
---

# All About Attacking JWT

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9770f2b9d087&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fall-about-attacking-jwt-9770f2b9d087&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fall-about-attacking-jwt-9770f2b9d087&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9770f2b9d087---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9770f2b9d087---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# All About Attacking JWT

[![Xcheater](https://miro.medium.com/v2/resize:fill:64:64/0*tShH7CIpSyRv7mwm.jpg)](https://xcheater.medium.com/?source=post_page---byline--9770f2b9d087---------------------------------------)

[Xcheater](https://xcheater.medium.com/?source=post_page---byline--9770f2b9d087---------------------------------------)

6 min read

·

Jan 29, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

Hello Hackers, I Hope you guys are doing well and hunting lots of bugs and Dollars !

Our today’s agenda is very concerning and trending topics that are related to attack vectors on JSON Web Token ( JWT ). let’s jump on the subject and understand the concept.

## What is JWT ?

JSON web token is an Open standard to transmit authentication details between two parties. They are often used for authorization purposes, but also it can be utilized for authentication purposes too. JWT is stateless, therefore there is no need to manage a session. which makes it an effective choice for large scalable websites in which users must interact with multiple back-end servers flawlessly.

## JWT Structure

JWT consists of three parts which are separately encoded and connected together with dots.

**Header** :- It defines token types and algorithm which is used for signing.

**Payload** :- This represents claims, which will denote information about logged-in users. Although owners can configure it according to their needs, there are some registered claims in it.

* iss- Issuer
* sub- Subject
* aud- Audience
* exp- Expiration time
* jti- JWT ID
* nbf- Not before
* iat- Issued at

**Signature** :- It contains primarily all the previous messages but is encoded to assure integrity checks with the help of a secret key.

Press enter or click to view image in full size

![]()

As of now, we are aware of its structure and usage of it. Let’s understand the back-end mechanism of generating and validating JWT tokens.

**Generating Token**

* The server creates the JSON Header (Algorithm + Type of token) and encodes it with base64.
* Then the server will create a payload ( User Information) and encode it with base 64. After this, it will tie with the dot.
* At last, it will sign the final value i.e (Header + payload), and again encode it with base64. add a dot and then the signature.

**Validating Token**

* Once the server will receive the token, it will split into three parts and Decode individual parts.
* Then simply parse the JSON for the header and payload, in terms of retrieving the algorithm and data which is claimed by the logged-in user.
* At the last, it will confirm the integrity with the help of a signature and also verify the claims.

Press enter or click to view image in full size

![]()

[https://cdn.hashnode.com/res/hashnode/image/upload/v1616225393075/v2TJSq1Hb.png?auto=compress,format&format=webp](https://cdn.hashnode.com/res/hashnode/image/upload/v1616225393075/v2TJSq1Hb.png?auto=compress%2Cformat&format=webp)

> Take a look at this for a more in-depth understanding of it. (<https://medium.com/cyberverse/five-easy-steps-to-understand-json-web-tokens-jwt-7665d2ddf4d5> )

## JWT Attacking Scope

Even though it is secure enough to protect the data it holds or uses, this only applies when it is properly configured. Developers sometimes ignore or unknowingly end up leaving this vulnerable. So let’s explore the possible attacks we could launch against it.

**Accepting arbitrary signatures** :- Verifying a JWT signature helps to ensure the integrity of data by verifying that information passing through payload and headers has not been tampered with. However, sometimes developers don’t configure tasks accurately.
Since the back-end system is currently not checking the signature, an attacker can tamper with the information and use it for various purposes.

**None Algorithm attack** :- Sometimes applications accept tokens with no signature, i.e the algorithm parameter is set to NONE.

The “none” algorithm is used when no encryption or signing is applied to the JWT, making it vulnerable to tampering and replay attacks. An attacker can easily modify the contents of the JWT and use it to gain unauthorized access to protected resources.
This feature was originally developed for debugging. The developer should make sure to push it off in a production environment. Since the back-end system is accepting the NONE algorithm, so attackers can tamper with information and use it for various purposes.

**Weak Secret key** :- JWT uses a symmetric signing algorithm that uses the same secret key to sign and verify the signature.

The secret key is a string of characters that is used to encrypt and decrypt the JWT. An attacker can easily guess the secret key if it is weak. This means that an attacker could generate their own JWT using their own information and gain access to the unauthorized access materials. The secret key can be cracked offline by brute forcing with just one valid token.

**Information Disclosure** :- Sometimes a JWT token stores a large amount of data about the logged-in user, which may be configured for any purpose by the developer. Keeping sensitive data in the payload section is insecure because it is encoded in base64, which is not a cryptographic algorithm and can be read by any other user who intercepts it.

**Insufficient session expiry** :- In general, the server should terminate the session after logout, but because JWT contains no session information, the developer must define a “exp” claim in the payload section to set an expiry time for the token.

As a pentester you should revalidate it by using the same set of token and check is it terminated by the server end or not.
*Note* :- While replaying the session, you can also play around JWT Id.

**Algorithm Confusion Attack :-** A JWT Algorithm Confusion vulnerability occurs when an attacker manipulates the algorithm used in a JSON Web Token (JWT) in such a way that the receiver of the JWT is unable to properly validate the JW...
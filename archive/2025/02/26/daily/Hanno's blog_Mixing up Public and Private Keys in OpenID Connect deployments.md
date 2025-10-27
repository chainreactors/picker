---
title: Mixing up Public and Private Keys in OpenID Connect deployments
url: https://blog.hboeck.de/archives/909-Mixing-up-Public-and-Private-Keys-in-OpenID-Connect-deployments.html
source: Hanno's blog
date: 2025-02-26
fetch_date: 2025-10-06T20:36:38.515761
---

# Mixing up Public and Private Keys in OpenID Connect deployments

# Mixing up Public and Private Keys in OpenID Connect deployments

[Hanno's Blog](https://blog.hboeck.de/)

### Tuesday, February 25. 2025

#### [Mixing up Public and Private Keys in OpenID Connect deployments](/archives/909-Mixing-up-Public-and-Private-Keys-in-OpenID-Connect-deployments.html)

![Key Icon](/uploads/keyelectronic.svg)I am developing a tool to check cryptographic public keys for known vulnerabilities called [badkeys](https://badkeys.info/). During the Q&A session of a presentation [about badkeys at the German OWASP Day](https://media.ccc.de/v/god2024-56276-the-debian-openssl-bug-and), I was asked whether I had ever used badkeys to check cryptographic keys in OpenID Connect setups. I had not until then.

OpenID Connect is a single sign-on protocol that allows web pages to offer logins via other services. Whenever you see a web page that offers logins via, e.g., your Google or Facebook account, the technology behind it is usually OpenID Connect.

An OpenID Provider like Google can publish a configuration file in JSON format for services interacting with it at a defined URL location of this form: *https://example.com/.well-known/openid-configuration* (Google's can [be found here](https://accounts.google.com/.well-known/openid-configuration).)

Those configuration files contain a field "jwks\_uri" pointing to a JSON Web Key Set (JWKS) containing cryptographic public keys used to verify authentication tokens. JSON Web Keys are a way to encode cryptographic keys in JSON format, and a JSON Web Key Set is a JSON structure containing multiple such keys. (You can find Google's [here](https://www.googleapis.com/oauth2/v3/certs).)

Given that the OpenID configuration file is at a known location and references the public keys, that gives us an easy way to scan for such keys. By scanning the Tranco Top 1 Million list and extending the scan with hostnames from [SSO-Monitor](https://sso-monitor.me/) (a research project providing extensive data about single sign-on services), I identified around 13.000 hosts with a valid OpenID Connect configuration and corresponding JSON Web Key Sets.

**Confusing Public and Private Keys**

JSON Web Keys have a very peculiar property. Cryptographic public and private keys are, in essence, just some large numbers. For most algorithms, all the numbers of the public key are also contained in the private key. For JSON Web Keys, those numbers are encoded with urlsafe Base64 encoding. (In case you don't know what urlsafe Base64 means, don't worry, it's not important here.)

Here is an example of an ECDSA public key in JSON Web Key format:

`{
"kty": "EC",
"crv": "P-256",
"x": "MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4",
"y": "4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM"
}`

Here is the corresponding private key:

`{
"kty": "EC",
"crv": "P-256",
"x": "MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4",
"y": "4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM",
"d": "870MB6gfuTJ4HtUnUvYMyJpr5eUZNP4Bk43bVdj3eAE"
}`

You may notice that they look very similar. The only difference is that the private key contains one additional value called d, which, in the case of ECDSA, is the private key value. In the case of RSA, the private key contains multiple additional values (one of them also called "d"), but the general idea is the same: the private key is just the public key plus some extra values.

What is very unusual and something I have not seen in any other context is that the serialization format for public and private keys is the same. The only way to distinguish public and private keys is to check if there are private values. JSON is commonly interpreted in an extensible way, meaning that any additional fields in a JSON field are usually ignored if they have no meaning to the application reading a JSON file.

These two facts combined lead to an interesting and dangerous property. Using a private key instead of a public key will usually work, because every private key in JSON Web Key format is also a valid public key.

You can guess by now where this is going. I checked whether any of the collected public keys from OpenID configurations were actually private keys.

This was the case for 9 hosts. Those included host names belonging to some prominent companies, including stackoverflowteams.com, stack.uberinternal.com, and ask.fisglobal.com. Those three all appear to use a service provided by Stackoverflow, and have since been fixed. (A report to Uber's bug bounty program at HackerOne was closed as a duplicate for a report they said they cannot show me. The report to FIS Global was closed by Bugcrowd's triagers as not applicable, with a generic response containing some explanations about OpenID Connect that appeared to be entirely unrelated to my report. After I asked for an explanation, I was asked to provide a proof of concept after the issue was already fixed. Stack Overflow has no bug bounty program, but fixed it after a report to their security contact.)

**Short RSA Keys**

7 hosts had RSA keys with a key length of 512 bit configured. Such keys have long been known to be breakable, and today, doing so is possible with relatively little effort. 45 hosts had RSA keys with a length of 1024 bit, which is considered to be breakable by powerful attackers, although such an attack has not yet been publicly demonstrated.

The first successful public attack on RSA with 512 bit was performed in 1999. Back then, it required months on a supercomputer. Today, breaking such keys is accessible to practically everyone. An implementation of the best-known attack on RSA is available as an Open Source software called [CADO-NFS](https://cado-nfs.gitlabpages.inria.fr/). Ryan Castellucci recently ran such an attack for a 512-bit RSA key they found in the control software of a solar and battery storage system. They mentioned a price of $70 for cloud services to perform the attack in a few hours. Cracking an RSA-512 bit key is, therefore, not a significant hurdle for any determined attacker.

**Using Example Keys in Production**

Running badkeys on the found keys uncovered another type of vulnerability. Before running the scan, I ensured that badkeys would detect example private keys in common Open Source OpenID Connect implementations. I discovered 18 affected hosts with keys that were such "Public Private Keys," i.e., keys where the corresponding private key is part of an existing, publicly available software package.

I have reported all 512-bit RSA keys and uses of example keys to the affected parties. Most of them remain unfixed.

**Impact**

Overall, I discovered 33 vulnerable hosts. With 13,000 detected OpenID configurations total, 0.25% of those were vulnerable in a way that would allow an attacker to access the private key.

How severe is such a private key break? It depends. OpenID Connect supports different ways in which authentication tokens are exchanged between an OpenID Provider and a Consumer. The token can be exchanged via the browser, and in this case, it is most severe, as it simply allows an attacker to sign arbitrary login tokens for any identity.

The token can also be exchanged directly between the OpenID Provider and the Consumer. In this case, an attack is much less likely, as it would require a man-in-the-middle attack and an additional attack on the TLS connection between the two servers. I have not made any attempts to figure out which methods the affected hosts were using.

**How to do better**

I would argue that two of these issues could have been entirely prevented by better specifications.

As mentioned, it is a curious and unusual fact that JSON Web Keys use the same serialization format for public and private keys. It is a design decision that makes confusing public and private keys likely.

In an ecosystem where public and private keys are entirely different — like TLS or SSH — any attempt to configure a private key instead of a public key would immediately be noticed, as it would simply not work.

One mitigation that can...
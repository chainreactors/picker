---
title: Dissecting the JWR phishing framework
url: https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework/
source: Over Security
date: 2026-08-13
fetch_date: 2026-08-14T04:00:38.215171
---

# Dissecting the JWR phishing framework

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# Dissecting the JWR phishing framework

By
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan/)

Thursday, August 13, 2026 06:00

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)
[phishing](https://blog.talosintelligence.com/category/phishing/)

* Cisco Talos recently identified an undocumented phishing framework, internally branded "JWR" by its developer, built to convincingly impersonate checkout and login pages across major payment and shopping platforms.
* The client engine of the JWR phishing framework is a real-time, operator-driven system that, rather than merely logging form submissions like a static credential-stealing page, keeps an AES-CTR encrypted WebSocket open to the threat actor so they can steer each victim's session live.
* The victim data targeted by the actor using JWR extends well beyond payment data, encompassing identity documents, Social Security numbers, passport and driver's license images, website and PayPal credentials, 2FA codes, and full device fingerprints, all committed to the actor's server once a session ends.
* Talos assesses with medium confidence that the JWR phishing framework is a variant of "The Outsider," a phishing-as-a-service (PhaaS) platform, based on several similarities in the client engine scripts and functionalities of the two PhaaS platforms.
* Talos observed a real-world campaign delivering the JWR client via SMS lures impersonating toll authorities, and postal and courier services of several countries in Southeast Asia and the Middle East.

---

## JWR phishing framework, a likely variant of the Outsider

JWR is a phishing framework capable of harvesting complete payment card data, login credentials, and personally identifiable information (PII) documents and images in real time. The client-side engine of the framework impersonates login, and checkout flows of several payment gateways, including Shopify, PayPal, Apple, Klarna, and banks, while allowing the operator to stealthily control the victim session through an AES-CTR encrypted WebSocket channel. The client engine architecture is divided into a Host Bridge module that relays commands into a phishing inline frame (iframe) and a Vue.js victim application that renders across 44 phishing pages, streams the victim's keystrokes to the actor as they are typed, and carries out more than 40 distinct instructions issued from the command-and-control (C2) console. The data exfiltration schema is a cvvform object that includes fields such as credit card number, CVV, PIN, expiry date, Social Security Number (SSN), passport or ID images, two-factor authentication (2FA) codes, website logins, PayPal credentials, and device fingerprint.

Talos discovered that the JWR client engine shares significant code and functional similarities with the client of The Outsider PhaaS platform operated by the Chinese-speaking actor “Outsider Enterprise,” which was reported by external [researchers](https://tapetumlabs.com/the-outsider-part-1-pulling-one-thread-on-a-1-9-billion-phishing-machine/).

## JWR client architecture and workflow

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/08/JWR-phishing-kit-01.jpg)

Figure 1. JWR phishing framework’s client engine architecture and execution flow.

The execution starts when the parent phishing webpage loads and executes the client's engine. It checks a single global flag, `window.__HOST_MODE`*,* which is set by the parent phishing page, and selects one of two execution modes. If the flag is set, the script enters Host Mode, and control passes to the Host Bridge module, an immediately invoked function expression (IIFE) that operates within the parent page, typically a replica of a legitimate checkout or account login page, relaying received details into a child iframe that contains the actual phishing form. It establishes a persistent WebSocket connection to the actor’s C2 server.

If the flag is not set, the page enters Content Mode, and control passes to the Vue.js Application, an interactive front end that renders the phishing pages, collects victim input, manages the flow across 44 HTML files, and handles the actor’s instructions from the C2 server, ultimately redirecting to a custom error page after sending the data to the C2. The Content Mode of execution has three communication modes: standalone, pluginIframe, and hostIframe.

* In standalone mode, the application fully owns its WebSocket connection.
* In pluginIframe mode, it has no direct link to the network at all and instead sends everything upward to an embedding plugin frame.
* In hostIframe mode, it defers entirely to a parent page already running as the relay bridge.

Regardless of which of these three modes or through the Host Bridge is used, the data is either sent to C2 as plain text in JSON format with the DEV\_MODE flag set, or it is passed to the JwrCrypto module, which encrypts it with a newly generated key before sending it to the C2 server.

The script engine includes a background worker module that maintains the connection with C2, keeping it alive independently of page navigation for the remainder of the session. In a live session activity, the script continuously streams the victim’s keystrokes to the actor's C2 server as captured data, while that the actor continuously sends the next instruction to be executed from the C2 server. Each incoming instruction is checked by the client engine against a brief history to ensure that nothing already executed runs twice, then routed by the Instruction Handling module to one of two outcomes including, redirecting the victim to a different phishing page or updating the current page's state and displayed status, awaiting the actor’s next instruction. This execution loop repeats until the actor decides to keep the...
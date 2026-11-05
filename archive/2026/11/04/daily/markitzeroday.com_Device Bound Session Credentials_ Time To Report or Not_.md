---
title: Device Bound Session Credentials: Time To Report or Not?
url: https://markitzeroday.com/2026/11/04/device-bound-session-credentials-dbsc-should-us-pe.html
source: markitzeroday.com
date: 2026-11-04
fetch_date: 2026-11-05T08:45:25.903569
---

# Device Bound Session Credentials: Time To Report or Not?

[markitzeroday.com](/)

[About](/about/)

# Device Bound Session Credentials: Time To Report or Not?

Nov 4, 2026

I have been tracking the rollout of [Device Bound Session Credentials (DBSC)](https://developer.chrome.com/docs/web-platform/device-bound-session-credentials) for a while now. It is the latest industry attempt to solve the perennial problem of session hijacking. If you are regularly testing authentication flows, you have likely come across documentation or headers related to this.

The question I hear increasingly often is: should we be reporting the lack of DBSC as a vulnerability?

### What is DBSC?

At its core, DBSC is a protocol that ties a web session to a specific device. When a browser initiates a session, it generates a key pair backed by hardware — think TPM on Windows or Secure Enclave on macOS. The server then requires this key to prove the session is still active on the original machine.

If an attacker manages to steal your session cookie, they cannot use it to renew the session or perform sensitive actions, because they lack the hardware-bound private key.

### Status and Support

This is no longer a theoretical exercise. Chrome 146 brought DBSC to stable release for Windows, with macOS support following shortly after. [You can test your browser](https://dbsc.dev/). It is a W3C Working Draft, meaning it has serious backing from the standards community.

### Should You Report the Absence of DBSC in Penetration Tests?

Device Bound Session Credentials (DBSC) is an emerging defensive layer designed to mitigate the impact of session theft. As it gains visibility, a common question arises among penetration testers: should the absence of DBSC be reported to clients?

The short answer is absolutely not. Do not report the absence of DBSC as a vulnerability in your pentest reports.

Let us look at the practical reasons why this should not be flagged as a security flaw:

**Maturity**: DBSC is still in the draft stage. It is an evolving concept, not an established security requirement.

**Complexity**: Implementing DBSC is not a quick fix. It requires substantial backend infrastructure changes to handle the protocol handshake.

**Compatibility**: The standard is currently heavily browser-dependent. Expecting every client application to support this is unrealistic for most real-world environments.

**Context**: Security is fundamentally about risk management. If you report this as a vulnerability for every application that lacks it, you are effectively flagging the entire internet as broken.

### The Case for an Informational Finding

Since it is not a vulnerability, should it be reported as an “Informational” finding? Given its current draft status, even an informational ticket might be premature for standard web application tests. Raising informational findings for immature draft standards often creates unnecessary noise, which risks frustrating development teams who are already managing packed remediation backlogs.

However, context dictates the approach. For high-risk, high-assurance applications where session hijacking is an explicitly defined primary threat, raising DBSC as an informational note can add value. If you choose to include it, it must be framed strictly as a forward-looking recommendation, a future hardening measure, or a best practice to monitor as the standard matures. It should never be presented as an active gap requiring immediate remediation.

Ultimately, DBSC is a valuable control best discussed during architectural reviews or long-term security maturity planning. Treat it exactly as you would treat the lack of certificate pinning or advanced experimental browser protections. Your time during an engagement is much better spent finding actual broken access control issues rather than chasing standards that have not yet reached maturity. Focus on the code that is actually broken.

## [markitzeroday.com](https://markitzeroday.com)

* [markitzeroday.com](https://markitzeroday.com)

* [rbrown256](https://github.com/rbrown256)
* [SilverlightFox](https://security.stackexchange.com/users/silverlightfox)

Security notes from a pentester

This site uses cookies for analytics. Is this OK? No Yes
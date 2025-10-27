---
title: Rage Against the Authentication State Machine
url: https://blog.silentsignal.eu/2025/06/14/gitblit-cve-CVE-2024-28080/
source: Silent Signal Techblog
date: 2025-08-30
fetch_date: 2025-10-07T00:48:38.897374
---

# Rage Against the Authentication State Machine

[![Silent Signal](/assets/img/s2_avatar.jpg)](/)

Silent Signal

Professional Ethical Hacking Services

### Contact us

2025 © Silent Signal

![Rage Against the Authentication State Machine](/img/ati_rage.jpg)

# Rage Against the Authentication State Machine

s2crew 2025-08-29

This blogpost describes our journey through discovering CVE-2024-28080, an authentication bypass vulnerability in Gitblit, [*“an open-source, pure Java stack for managing, viewing, and serving Git repositories”*](https://gitblit.com/). The vulnerability affects the SSH service and can only be exploited for users that have at least one public key assigned to their account. [Version 1.10](https://github.com/gitblit-org/gitblit/releases/tag/v1.10.0) released on 14 June 2025 fixes this and two other vulnerabilities.

## Story time: why we used Gitblit in the first place

Many years ago, before the era of Gitea, the options for self-hosted web interfaces around Git were not that great. Ruby projects such as Redmine and GitLab were a nightmare from a sysadmin perspective, all depending on tainting the system SSHd scope with handing Git pushes over SSH. It was in this context where picking a Java-based solution seemed like a nice idea – dropping a single JAR file and spawning a JVM process handled web and SSH access. Latter was critical, as this SSH service was also part of the solution, running in the name of the same service user, independently from the system-wide SSH used for sysadmin purposes.

## How we found the bug

The SSH journey of most people involve starting with username/password combination, with a later upgrade to public key-based authentication, stored in keyfiles, optionally proxied by an SSH Agent. The next logical step involves storing private keys on dedicated devices (tokens, smartcards), where the secret parts of a keypair generated on said device can never leave the hardware in [an ideal world](https://www.yubico.com/support/security-advisories/ysa-2024-03/).

Integrating hardware solutions with software is always a challenge, thus we managed to trigger a scenario, where the OpenSSH client failed to complete the public key authentication. Gitblit promptly fell back to password-based authentication, which I did not prefer – so I just pressed `↵ Enter` without typing anything (basically submitting an empty password), while I mentally prepared myself for Gitblit to refuse my connection so that I can try again after debugging my Yubikey.

Imagine my surprise, when the Git command completed successfully – taking things like `ControlMaster` into account, I had to repeat the unintentional experiment described above. I asked Buherátor to repeat on his machine to confirm, since what happened defied the model I had in my mind regarding SSH public key authentication in every way possible. In this regard, my discovery of this vulnerability is a bit similar to our friend David
Schütz [accidentally finding a $70k Google Pixel Lock Screen Bypass](https://bugs.xdavidhu.me/google/2022/11/10/accidental-70k-google-pixel-lock-screen-bypass/).

## How SSH public key authentication works

Diving into the [RFC 4252](https://datatracker.ietf.org/doc/html/rfc4252) describing the SSH Authentication Protocol and reading through the verbose output of the OpenSSH client revealed that public key authentication had multiple stages in SSH.

1. The client sends a [Public Key Authentication Request](https://datatracker.ietf.org/doc/html/rfc4252#section-7) with the username and a public key to the server.
2. The server confirms whether this public key can be used to authenticate as the username sent by the client. (If not, the client goes back to the previous step with another key, or abandons trying to authenticate using public keys.)
3. The client – knowing that the public key got accepted by the server – prepares a challenge, following a strict protocol in the RFC and then signs it using the private key.
4. The signature is sent to the server, which can calculate the same challenge and verify that the signature is valid.

Looking at the steps above, it becomes obvious why [CVE-2016-20012](https://nvd.nist.gov/vuln/detail/CVE-2016-20012) is disputed by the OpenSSH project – the protocol design did not take an attacker model like this into consideration. An attacker knowing that a certain username can authenticate with a specific public key is arguably a pretty weak oracle.

## How the bug happened

When we confirmed the issue internally, the next step was trying to triage, which component(s) were the root cause of this unwanted behavior. As mentioned before, Gitblit did not use the SSHd used by the rest of the operating system, nor did it reinvent the wheel – but rather it included [an Apache library called MINA SSHD](https://mina.apache.org/sshd-project/) ,

> a 100% pure java library to support the SSH protocols on both the client and server side. It does not aim at being a replacement for the SSH client or SSH server from Unix operating systems, but rather provides support for Java based applications requiring SSH support.

Our first task was to find out whether the bug was in MINA – which could affect numerous projects [depending on it](https://deps.dev/maven/org.apache.sshd%3Asshd-core/2.15.0/dependents) – or if it was specific to Gitblit. A quick trial of another MINA-based project resulted in an early negative signal, leading the investigation into the Gitblit codebase – more specifically, the integration with MINA.

### How MINA interfaces with the Gitblit and other applications

The diagram below illustrates the relationship between the Authenticator implementation within the Gitblit code and the Apache MINA SSH daemon component, all residing within a single JVM process. The MINA SSHD receives incoming TCP connections over the listener socket, and processes packetized SSH protocol streams using its own state machine. When an SSH client tries to authenticate, the Authenticator implementation gets invoked using a standardized Java interface, and the result returned from said method affects the next transition within the SSH server-side state machine.

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│             JVM process started for Gitblit              │
│                                                          │
│                                                          │
│                               ┌────────────────────────┐ │
│ ┌──────────────────┐          │                        │ │
│ │                  │          │ Apache MINA SSH daemon │ │
│ │  Authenticator   │          │                        │ │
│ │  implementation  ├────(o────┤ ┌ ─ ─ ─ ─ ─ ─ ┐ ┌──────┴─┴─────┐
│ │  (Gitblit code)  │          │       SSH       │ TCP listener │
│ │                  │          │ │ server-side │ │    socket    │
│ └──────────────────┘          │  state machine  └──────┬─┬─────┘
│                               │ └ ─ ─ ─ ─ ─ ─ ┘        │ │
│                               └────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

Diving into the codebase, the application (in our case, Gitblit) provides a class that implements the Apache MINA interface [`PublickeyAuthenticator`](https://svn.apache.org/repos/infra/websites/production/mina/content/sshd-project/apidocs/org/apache/sshd/server/auth/pubkey/PublickeyAuthenticator.html) that contains a single method with a clear purpose.

```
boolean authenticate(String username, PublicKey key, ServerSession session)
```

As the Javadoc linked above mentions, “`PublickeyAuthenticator` is used on the server side to authenticate user public keys”, and this method should “check the validity of a public key” by returning “a boolean indicating if authentication succeeded or not”.

However, the devil is in the details – taking the above model of the SSH protocol design regarding public key authentication into account means that this meth...
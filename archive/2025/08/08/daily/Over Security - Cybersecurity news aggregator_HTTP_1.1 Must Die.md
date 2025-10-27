---
title: HTTP/1.1 Must Die
url: https://http1mustdie.com/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-08
fetch_date: 2025-10-07T00:49:45.294811
---

# HTTP/1.1 Must Die

![HTTP/1.1 Must Die Logo](/images/http1_must_die_logo-200h.webp)
The Desync Endgame Begins

# HTTP/1 Must Die

[PAPER](https://portswigger.net/research/http1-must-die)

[PDF](https://portswigger.net/kb/papers/dzmxreq/http1-must-die.pdf)

[FAQs](#FAQs)

[RESOURCES](#Resources)

# HTTP/1 Must Die

## It's time to acknowledge HTTP/1.1 is insecure

Upstream HTTP/1.1 is inherently insecure, and routinely
exposes millions of websites to hostile takeover. Vendors
have spent six years deploying mitigations, and
researchers have consistently bypassed them.

In PortSwigger's latest research, we introduce several
novel classes of HTTP desync attack, and showcase
critical vulnerabilities which exposed tens of millions
of websites by subverting core infrastructure within
multiple CDNs. Little has changed since we
[first disclosed the threat in 2019](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn). This cycle will continue as long as HTTP/1.1
lives.

## The solution: upstream HTTP/2

HTTP/1.1 has a fatal flaw: attackers can create extreme
ambiguity about where one request ends, and the next
request starts. HTTP/2+ eliminates this ambiguity, making
desync attacks virtually impossible. However, simply
enabling HTTP/2 on your edge server is insufficient - it
must be used for the upstream connection between your
reverse proxy and origin server.

### Act Now:

### Join the mission to kill HTTP/1.1

Understand the latest threat and learn how you can help
kill HTTP/1.1 in our new whitepaper
[HTTP/1.1 Must Die: The Desync Endgame](https://portswigger.net/research/http1-must-die).

Solidify your understanding and sharpen your skills in
a safe, dedicated sandbox with our free Web Security
Academy lab:
[0.CL request smuggling](https://portswigger.net/web-security/request-smuggling/advanced#0-cl-request-smuggling).

### Enable upstream HTTP/2

Ensure your origin server supports HTTP/2, then enable
upstream HTTP/2 on your front-end servers.

### Defend systems still using HTTP/1.1

Identify imminent threats using our open-source
toolkits
[HTTP Request Smuggler v3.0](https://github.com/PortSwigger/http-request-smuggler/)

and
[HTTP Hacker](https://portswigger.net/bappstore/657363a6ea0a42d0be7f0b781249089f), then use recurring scans to keep up
with emerging threats.

Enable all available request validation/normalisation
features on your front-end, and consider disabling
upstream connection reuse.

Contact your vendor and ask when upstream HTTP/2
support can be expected.

## What does this mean for you?

[AppSec Leadership

Find out more](https://portswigger.net/blog/http-1-1-must-die-what-this-means-for-appsec-leadership)
[In-House Pentesters

Find out more](https://portswigger.net/blog/http-1-1-must-die-what-this-means-for-in-house-pentesters)
[MSSPs and Contract Pentesters

Find out more](https://portswigger.net/blog/http-1-1-must-die-what-this-means-for-contract-pentesters-and-mssps)
[Bug Bounty Hunters

Find out more](https://portswigger.net/blog/http-1-1-must-die-what-this-means-for-bug-bounty-hunters)

## HTTP1 Must Die! FAQs

Is HTTP Request Smuggling really dangerous?

Yes. A single HTTP request can make a website
lose track of which responses should go to which
users, resulting in massive disclosure of
confidential information. This typically results
in
[users being randomly logged into other live
user's accounts](https://portswigger.net/research/http2#splitting).

HTTP Request Smuggling also enables attackers to
poison your website's cache with malicious
JavaScript. This typically gives them persistent
control over every page on your website, and lets
them steal passwords and credit card details. For
example, we were previously able to
[compromise PayPal's login page](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn#paypal).

The vulnerabilities mentioned in the whitepaper have been patched. Is HTTP/1.1 safe now?

No. Time has proven we can't patch HTTP/1.1 to safety - more vulnerabilities are on the way. Please
[refer to the whitepaper](https://portswigger.net/research/http1-must-die)
 for our full perspective on this.

My website uses HTTPS. Is it safe?

No. Wrapping HTTP/1.1 in TLS has no effect on this vulnerability.

Is it safe to use HTTP/2 to talk to clients, but HTTP/1.1 upstream?

No,
[HTTP/2 must be used upstream](https://portswigger.net/research/http2)
 - this is where severe desync attacks happen.

What should I do if I can't enable upstream HTTP/2?

We know some major vendors don't support upstream
HTTP/2 yet, including nginx, Akamai, CloudFront,
and Fastly.

First, scan your website with HTTP Request
Smuggler 3.0 to identify imminent threats.
Consider setting up regular scans going forwards -
we will update this tool with future techniques as
they become known.

Then, explore the product documentation and
enable any relevant HTTP/1.1 normalisation
features. Note that you can significantly reduce
the threat posed by HTTP Request Smuggling by
disabling upstream connection reuse, but this may
affect performance.

Finally, engage with your server vendor to
request support for upstream HTTP/2, and ask if
they have any recommended mitigations such as
request validation or normalisation. Note that you
can significantly reduce the threat posed by HTTP
Request Smuggling by disabling upstream connection
reuse, but this may affect performance.

Is HTTP/2 really more secure?

End-to-end HTTP/2 makes desync vulnerabilities much rarer. This is because HTTP/2 has very little room for ambiguity about the length of each message. Therefore, it's significantly less likely that a bug in a HTTP/2 server poses a major security risk. So far, most vulnerabilities found in HTTP/2 implementations are DoS flaws - an attack class that is less relevant to upstream connections.

What if a client only supports HTTP/1.1?

You do not need to disable support for HTTP/1.1 between the client and your edge server. This is low risk as connections to your edge server are rarely shared between different users.

Why is this only an issue for upstream HTTP/1.1?

Reverse proxies typically route requests from different users over a single shared pool of connections to back-end servers. This mingles attacker's requests with those from legitimate users. Also, front-end servers often have web caches which amplify the danger by enabling persistent compromise.

Is HTTP/1.1 safe for websites that don't use any kind of reverse proxy?

Fairly. It might have a client-side desync vulnerability, but these are relatively rare.

Is HTTP/1.0 insecure too?

Yes, provided the reverse-proxy is reusing upstream connections.

Can I fix this with a WAF?

Not reliably. In fact, we have observed some WAFs that introduce desync vulnerabilities to otherwise secure systems.

Should I panic?

No. This research is highlighting a threat that, while serious, has existed for years. The coordinated tool and whitepaper publication is intended to ensure you can secure your web assets quickly, then work towards the long-term solution.

## Resources

[#### Read the whitepaper

Read more](https://portswigger.net/research/http1-must-die)
[#### Download the PDF

Download](https://portswigger.net/kb/papers/dzmxreq/http1-must-die.pdf)
[#### Download HTTP Request Smuggler v3.0

Download](https://github.com/PortSwigger/http-request-smuggler/)

[#### Download HTTP Hacker

Download](https://portswigger.net/bappstore/657363a6ea0a42d0be7f0b781249089f)
[#### 0.CL request smuggling expert lab

Try it now](https://portswigger.net/web-security/request-smuggling/advanced#0-cl-request-smuggling)
[#### Previous request smuggling research

Read more](https://portswigger.net/research/request-smuggling)
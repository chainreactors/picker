---
title: How Burp AI Works
url: https://parsiya.net/blog/2025-08-15-how-burp-ai-works/
source: Hackerman's Hacking Tutorials
date: 2025-08-16
fetch_date: 2025-10-07T00:48:10.538477
---

# How Burp AI Works

# [Hackerman's Hacking Tutorials](https://parsiya.net/)

## The knowledge of anything, since all things have causes, is not acquired or complete unless it is known by its causes. - Avicenna

Navigate…» About Me!» Cheat Sheet» My Clone» Source Repo» Manual Work is a Bug» The Other Guy from Wham!

* [About Me!](https://parsiya.net/about/ "About Me!")
* [Cheat Sheet](https://parsiya.net/cheatsheet/ "Cheat Sheet")
* [My Clone](https://parsiya.io/ "My Clone")
* [Source Repo](https://github.com/parsiya/parsiya.net "Source Repo")
* [Manual Work is a Bug](https://queue.acm.org/detail.cfm?id=3197520 "Manual Work is a Bug")
* [The Other Guy from Wham!](https://www.google.com/search?q=andrew+ridgeley "The Other Guy from Wham!")

Aug 15, 2025
- 15 minute read - [DEF CON](https://parsiya.net/categories/def-con/) [Burp](https://parsiya.net/categories/burp/) [AI](https://parsiya.net/categories/ai/)

# How Burp AI Works

* [Quick Start](#quick-start)
* [Quick Facts](#quick-facts)
* [Motivation](#motivation)
* [Proxying Burp](#proxying-burp)
  + [Checking the Logs](#checking-the-logs)
  + [Upstream Proxy](#upstream-proxy)
  + [JRE cacerts File](#jre-cacerts-file)
* [What's Inside Burp AI](#whats-inside-burp-ai)
  + [Explore Issue](#explore-issue)
  + ['Explain This' Context Menu Item](#explain-this-context-menu-item)
  + [AI Recorded Login](#ai-recorded-login)
* [What is This Useful For?](#what-is-this-useful-for)
  + [Suggestion to PortSwigger](#suggestion-to-portswigger)
* [Other Solutions](#other-solutions)
  + [Other Java Proxy Settings](#other-java-proxy-settings)
  + [Hooking](#hooking)

This is a quick peek inside Burp AI. I'll show how to proxy its requests, what
actually happens when you trigger a feature. This knowledge allows us to
redirect Burp AI to your own AI instance. As far as I know, this is not publicly
documented.

I covered a shorter version in my DEF CON 33 Bug Bounty Village talk
`The Year of the Bounty Desktop: Bugs from Binaries`. See the
[extended slides (pages 14–22)](https://github.com/parsiya/Presentations/blob/main/defcon-33-bugs-binaries/defcon-33-bugs-binaries-all-slides.pdf) (placeholder for video).

# Quick Start

1. Run two Burp instances.
2. In the first (Burp client), set the upstream proxy to `localhost:9000`.
3. In the second (Burp server), create a listener on port `9000`.
4. Add the Burp CA to the JRE `cacerts`.
5. Use AI in Burp client; watch results in Burp server.

# Quick Facts

1. AI is off by default (props to PortSwigger).
2. All AI traffic goes to `ai.portswigger.net`. Block it to disable Burp AI.
3. This is also mentioned in the documentation, but I wanted to confirm.
4. Requests/responses are JSON.
5. Burp had "agentic behavior" pre‑hype. E.g., AI can ask Repeater or the login
   recorder to act.

# Motivation

I wanted to see how Burp AI works internally: where traffic goes and what is
sent. A big Burp AI flaw (to me) is the lack of a configurable endpoint. I trust
PortSwigger; I'm running their software. Still, I can't send internal data to
an outside service.

# Proxying Burp

I'll walk through what I tried. What worked, what didn't, and what I'd have
tried next.

## Checking the Logs

Burp has a built-in Logger, so I started there. Only *some* Burp AI requests
show up there. When I clicked `Explore Issue` for "Exploring Strict transport
security not enforced on example.net" I saw only one AI request.

Here's how the issue looks in Burp after exploration:

![Exploring HSTS in example.net](01-explore-hsts.webp "Exploring HSTS in example.net")
Exploring HSTS in example.net

And this is the only request Logger captured:

![Only request captured in Logger](02.webp "Only request captured in Logger")
Only request captured in Logger

I've not investigated this, but Logger likely uses the same APIs extensions use,
so an extension won't see everything either. Those APIs are:

* Legacy API: [void registerHttpListener(IHttpListener listener)](https://portswigger.net/burp/extender/api/burp/iburpextendercallbacks.html#registerHttpListener-burp.IHttpListener-)
* Montoya API: [Registration registerHttpHandler(HttpHandler handler)](https://portswigger.github.io/burp-extensions-montoya-api/javadoc/burp/api/montoya/http/Http.html#registerHttpHandler%28burp.api.montoya.http.handler.HttpHandler%29)

## Upstream Proxy

Burp supports an upstream proxy, so we can intercept outbound traffic. It's
"proxy‑aware" and sends the `CONNECT` request properly. For background, see my
2016 post [Thick Client Proxying - Part 6: How HTTP(s) Proxies Work](https://parsiya.net/blog/2016-07-28-thick-client-proxying-part-6-how-https-proxies-work/).

For more about proxying Burp (and other similar tools), read my
[Thick Client Proxying - Part 4: Burp in Proxy Chains](https://parsiya.net/blog/2016-04-07-thick-client-proxying-part-4-burp-in-proxy-chains/) blog.

1. Run two instances of Burp. Let's call them Burp client and server.
2. Set the Upstream Proxy for Burp client to `localhost:9000`.
3. Create a proxy listener in Burp server on port `9000`.

![Burp client and server setup](03-upstream.webp "Burp client and server setup")
Burp client and server setup

After wiring this up I clicked the purple magic icon (bottom right) to check my
Burp balance. Surprisingly, it failed.

![Failed Burp balance check](04-balance.webp "Failed Burp balance check")
Failed Burp balance check

I'd already added Burp's CA to the Windows certificate store. So what broke?

## JRE cacerts File

Burp is written in Java. The Windows version bundles a Java Runtime Environment
(JRE). The executable wraps `java -jar ...` plus flags from `.vmoptions` files.

The JRE has its own certificate trust store at `JAVA_HOME/lib/security/cacerts`.
On Windows it's located at:
`%LocalAppData%/Programs/BurpSuitePro/jre/lib/security/cacerts`.

We can import the Burp CA with `keytool`. Keytool is conveniently bundled with
JRE at `JAVA_HOME/bin/keytool`.

1. Extract the Burp CA in DER format.
2. (Optional) cd into `.../jre/lib/security/` for convenience.
3. Run the following command. Adjust the paths as needed.

```
..\..\bin\keytool.exe -importcert -alias burp -keystore cacerts
    -storepass changeit -file /path/to/burpca.crt
```

On Linux (credit: [Nico](https://hackademy.agarri.fr/contact)):

```
./bin/keytool -importcert -cacerts -alias burp -file /path/to/burpca.crt
```

Done. Now the balance request shows up in Burp server. GET to
`https://ai.portswigger.net/burp/balance` with a base64 token in the
`Portswigger-Burp-Ai-Token` header.

![Burp balance check request](05-balance2.webp "Burp balance check request")
Burp balance check request

Token size is 864 bytes base64 and 648 bytes decoded. High entropy (7.61
Shannon) so likely random/encrypted.

![Entropy of the token in CyberChef](06-token.webp "Entropy of the token in CyberChef")
Entropy of the token in CyberChef

# What's Inside Burp AI

Burp has quite a few AI features. Let's look at some of them.

## Explore Issue

Each issue has an `Explore Issue` button. Here I use the HSTS finding on
example.net.

![The 'Explore HSTS' button](07-explore-issue.webp "The 'Explore HSTS' button")
The 'Explore HSTS' button

First request: POST to
`https://ai.portswigger.net/ai/hakawai-explore-service/api/v1/start`. Values are
replaced with `{{ }}` placeholders, but you can guess them.

```
POST /ai/hakawai-explore-service/api/v1/start HTTP/2
Host: ai.portswigger.net

{
  "issue_definition": {
    "name": "Strict transport security not enforced",
    "type": "STRICT_TRANSPORT_SECURITY_NOT_ENFORCED",
    "detail": null,
    "background": "{{ description from PortSwigger KB}}",
    "evidence": [
      {
        "type": "REQUEST_RESPONSE",
        "request": "{{ request }}",
        "response": "{{ response }}",
        "request_highlights": [],
        "response_highlights": []
      }
    ]
  }
}
```

We see:

1. Finding name and type (same).
2. Description from the Burp KB (description section of [this page](https://portswigger.net/kb/issues/01000300_stric...
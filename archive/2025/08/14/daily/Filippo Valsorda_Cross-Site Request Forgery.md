---
title: Cross-Site Request Forgery
url: https://words.filippo.io/csrf/
source: Filippo Valsorda
date: 2025-08-14
fetch_date: 2025-10-07T00:47:36.646728
---

# Cross-Site Request Forgery

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

13 Aug 2025

# Cross-Site Request Forgery

[Cross-Site Request Forgery (CSRF)](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/CSRF) is a [confused deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem) attack where the attacker causes the browser to send a request to a target using the ambient authority of the user’s cookies or network position.[1](#fn:pna) For example, `attacker.example` can serve the following HTML to a victim

```
<form action="https://example.com/send-money" method="post">
  <input type="hidden" name="to" value="filippo" />
  <input type="hidden" name="amount" value="1000000" />
</form>
```

and the browser will send a POST request to `https://example.com/send-money` using the victim’s cookies.

Essentially all applications that use cookies for authentication need to protect against CSRF. Importantly, this is not about protecting against an attacker that can make arbitrary requests[2](#fn:api) (as an attacker doesn’t know the user’s cookies), but about working with browsers to identify authenticated requests initiated from untrusted sources.

Unlike [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS), which is about *sharing responses* across origins, CSRF is about accepting state-changing requests, even if the attacker will not see the response. Defending against [leaks](https://xsleaks.dev/) is significantly [more complex and nuanced](https://frederikbraun.de/modern-solutions-xsleaks.html), especially in the age of Spectre.

Why do browsers allow these requests in the first place? Like anything in the Web platform, primarily for legacy reasons: that’s how it used to work and changing it breaks things. Importantly, disabling these *third-party cookies* breaks important Single-Sign On (SSO) flows. All CSRF solutions need to support a bypass mechanism for those rare exceptions. (There are also complex intersections with cross-site tracking and privacy concerns, which are beyond the scope of this article.)

## Same site vs same site vs same origin

To protect against CSRF, it’s important to first define what is a cross-site or cross-origin request, and which should be allowed.

`https://app.example.com`, `https://marketing.example.com`, and even `http://app.example.com` (depending on the definition) are all same-site but not same-origin.

It’s tempting to declare the goal as ensuring requests are simply from the same site, but different origins in the same site can actually sit at very different trust levels: for example it might be much easier to get XSS into an old marketing blog than in the admin panel.

The starkest difference in trust though is between an HTTPS and an HTTP origin, since a network attacker can serve anything it wants on the latter. This is sometimes referred to as the MitM CSRF bypass, but really it’s just a special case of a *schemelessly* same-site cross-origin CSRF attack.

Some parts of the Web platform apply a *schemeful* definition of same-site, where `https://app.example.com` and `http://app.example.com` are *not* same-site:

* Cookies in general apply the schemeless definition (HTTP = HTTPS). There is a proposal to address this, [Origin-Bound-Cookies](https://github.com/sbingler/Origin-Bound-Cookies) (and specifically its lack of opt-out for scheme binding, which subsumes the earlier [Scheme-Bound Cookies](https://github.com/mikewest/scheming-cookies) proposal), which however [hasn’t shipped yet](https://chromestatus.com/feature/4945698250293248).
* The SameSite cookie attribute used to apply the schemeless definition (HTTP = HTTPS). Chrome changed that with [Schemeful Same-Site](https://web.dev/articles/schemeful-samesite) in 2020, but [Firefox](https://bugzilla.mozilla.org/show_bug.cgi?id=1651119) and [Safari](https://wpt.fyi/results/cookies/schemeful-same-site?label=master&label=experimental&aligned&q=schemeful) never implemented it.
* [Sec-Fetch-Site](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-Site#same-site) (and the [HTML and Fetch specifications](https://html.spec.whatwg.org/multipage/browsers.html#sites) in general) apply the schemeful definition (HTTP ≠ HTTPS).

Using [HTTP Strict Transport Security (HSTS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security), if possible, is a potential mitigation for HTTP→HTTPS issues.

## Countermeasures

There are a number of potential countermeasures to CSRF, some of which have been available only for a few years.

### Double submit or synchronized tokens

The “classic” countermeasure is a CSRF *token*, a large random value submitted in the request (e.g. as a hidden `<input>`) and compared against a value stored in a cookie (*double-submit*) or in a stateful server-side session (*synchronized tokens*).

Normally, double-submit is not a same-origin countermeasure, because same-site origins [can set cookies on each other](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-rfc6265bis-20#name-weak-integrity) by “cookie tossing”. This can be mitigated with the `__Host-` [cookie prefix](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-rfc6265bis-20#name-the-__host-prefix), or by binding the token to the session/user with signed metadata. The former makes it impossible for the attacker to set the cookie, the latter ensures the attacker doesn’t know a valid value to set it to.

Note that signing the cookies or tokens is unnecessary and ineffectual, unless it is binding the token to a user: an attacker that’s cookie tossing can otherwise obtain a valid signed pair by logging into the website themselves and then use that for the attack.

This countermeasure turns a cross-origin forgery problem into a cross-origin leak problem: if the attacker can obtain a token from a cross-origin response, it can forge a valid request.

The token in the HTML body should be masked as a countermeasure against the [BREACH compression attack](https://www.breachattack.com/).

The primary issue with CSRF tokens is that they require developers to instrument all their forms and other POST requests.

### Origin header

Browsers send the source of a request in the [Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin) header, so CSRF can be mitigated by rejecting [non-safe](https://developer.mozilla.org/en-US/docs/Glossary/Safe/HTTP) requests from other origins.

The main issue is knowing the application’s own origin. One option obviously is asking the developer to configure it, but that’s friction and might not always be easy (such as for open source projects and proxied setups).

The closest readily available approximation of the application’s own origin is the Host header. This has two issues:

1. it may be different from the browser origin if a reverse proxy is involved;
2. it does not include the scheme, so there is no way to know if an `http://` Origin is a cross-origin HTTP→HTTPS request or a same-origin HTTP request.

Some older (pre-2020) browsers [didn’t send the Origin header for POST requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin#browser_compatibility).

The value can be `null` in a variety of cases, such as due to `Referrer-Policy: no-referrer` or following cross-origin redirects. `null` must be treated as an indication of a cross-origin request.

Some privacy extensions remove the Origin header instead of setting it to `null`. This should be considered a security vulnerability introduced by the extension, since it removes any reliable indication of a browser cross-origin request.

### SameSite cookies

If authentication cookies are *explicitly* set with the [SameSite](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie#samesitesamesite-value) attribute Lax or Strict, they will not be sent with non-sa...
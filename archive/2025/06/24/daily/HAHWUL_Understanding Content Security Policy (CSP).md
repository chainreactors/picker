---
title: Understanding Content Security Policy (CSP)
url: https://www.hahwul.com/sec/web-security/csp/
source: HAHWUL
date: 2025-06-24
fetch_date: 2025-10-06T22:52:57.545480
---

# Understanding Content Security Policy (CSP)

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/sec/web-security/csp/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/sec/web-security/csp/)

[한국어](https://www.hahwul.com/ko/sec/web-security/csp/)

JUNE 23, 2025

# Understanding Content Security Policy (CSP)

Learn about Content Security Policy (CSP), its importance, how it works, and how it enhances web security.

## What is Content Security Policy (CSP)?

Content Security Policy (CSP) is a security mechanism that controls which resources a web page can load, preventing attacks like Cross-Site Scripting (XSS) and data injection.

CSP uses HTTP headers to specify trusted content sources, blocking execution of malicious scripts in the browser.

## Why is CSP Important?

Modern web applications use resources from multiple sources, creating attack opportunities. CSP mitigates these threats by:

* Prevents XSS Attacks: By specifying trusted script sources, CSP blocks malicious scripts from being injected and executed.
* Prevents Data Exfiltration: It can restrict data transmission to specific domains, preventing sensitive information from being leaked.
* Prevents Clickjacking: The `frame-ancestors` directive controls how other sites can frame the page, thus preventing clickjacking attacks.
* Prevents Mixed Content: It helps maintain a secure connection by preventing HTTP content from being loaded on HTTPS pages.

## How Does CSP Work?

The web server sends the `Content-Security-Policy` HTTP header to the browser with directives that control resource loading:

```
Content-Security-Policy: script-src 'self';
```

The browser enforces this policy, blocking non-compliant resources and optionally reporting violations.

### Key CSP Directives

CSP provides these key directives:

| Directive | Description |
| --- | --- |
| `default-src` | Sets a default policy for many other directives. If a specific directive is not set, this value is used. |
| `script-src` | Specifies valid sources for JavaScript code. |
| `style-src` | Specifies valid sources for CSS stylesheets. |
| `img-src` | Specifies valid sources for images. |
| `font-src` | Specifies valid sources for fonts. |
| `media-src` | Specifies valid sources for media files like audio and video. |
| `connect-src` | Restricts origins that can be connected to using `fetch`, `XMLHttpRequest`, `WebSocket`, `EventSource`, etc. |
| `frame-src` | Specifies valid sources that can be embedded as frames. (Deprecated, `child-src` is recommended). |
| `child-src` | Specifies valid sources for nested browsing contexts, such as web workers and frames. |
| `object-src` | Controls valid sources for `<object>`, `<embed>`, and `<applet>` tags. It's recommended to set this to `'none'` for security reasons. |
| `frame-ancestors` | Specifies valid parent origins that can embed the current page using frames, iframes, objects, embeds, or applets. This is crucial for defending against clickjacking attacks. |
| `report-uri` / `report-to` | Specifies a URL where the browser will send reports when a CSP violation occurs. `report-to` is a newer directive that supports JSON-formatted reports and supersedes `report-uri`. |

### Source Values

Each directive can have source values such as:

| Source Value | Description |
| --- | --- |
| `'self'` | Current origin only (same scheme, host, port). |
| `'unsafe-inline'` | Inline JavaScript and CSS (security risk). |
| `'unsafe-eval'` | Allows `eval()` and similar (security risk). |
| `'none'` | No sources allowed. |
| `https://example.com` | Specific domain. |
| `*.example.com` | All subdomains of example.com. |
| `data:` | Data URI scheme resources. |
| `nonce-<base64-value>` | Scripts/styles with specific nonce. |
| `sha256-<base64-value>` | Scripts/styles with matching hash. |

## How to Apply CSP

Apply CSP in one of two ways:

1. HTTP Header (recommended):

* Nginx: `add_header Content-Security-Policy "default-src 'self'; script-src 'self' https://trusted-cdn.com";`
* Apache: `Header set Content-Security-Policy "default-src 'self'; script-src 'self' https://trusted-cdn.com"`

2. `<meta>` Tag (limited support):

   ```
   <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' https://trusted-cdn.com;">
   ```

   Note: `<meta>` doesn't support `frame-ancestors`, `report-uri`, or `sandbox` directives.

## CSP Implementation Strategy

Implement CSP gradually to avoid breaking functionality:

* Report-Only Mode: Test without enforcement
* Start lenient, then tighten: Begin with permissive rules, gradually remove unsafe directives
* Use nonces/hashes instead of `'unsafe-inline'`
* Monitor and update: Regularly review violation reports and adjust as needed

```
  Content-Security-Policy-Report-Only: default-src 'self'; report-uri /csp-violation-report-endpoint;
```

## Benefits of CSP

* Strong XSS Defense: Blocks untrusted script execution
* Reduced Data Injection: Limits malicious data insertion
* Clickjacking Protection: Controls framing via `frame-ancestors`
* Enhanced Security Awareness: Improves resource visibility

## Conclusion

CSP is essential for modern web application security, protecting against XSS and other common attacks. Despite implementation complexity, its security benefits are substantial. Gradual implementation and ongoing monitoring will significantly improve your site's security posture.

[#csp](https://www.hahwul.com/tags/csp/)
[#web security](https://www.hahwul.com/tags/web-security/)
[#xss](https://www.hahwul.com/tags/xss/)

[ ]

[ ]

### Table of Contents

[What is Content Security Policy (CSP)?](https://www.hahwul.com/sec/web-security/csp/#what-is-content-security-policy-csp)

[Why is CSP Important?](https://www.hahwul.com/sec/web-security/csp/#why-is-csp-important)

[How Does CSP Work?](https://www.hahwul.com/sec/web-security/csp/#how-does-csp-work)

[Key CSP Directives](https://www.hahwul.com/sec/web-security/csp/#key-csp-directives)
[Source Values](https://www.hahwul.com/sec/web-security/csp/#source-values)

[How to Apply CSP](https://www.hahwul.com/sec/web-security/csp/#how-to-apply-csp)

[CSP Implementation Strategy](https://www.hahwul.com/sec/web-security/csp/#csp-implementation-strategy)

[Benefits of CSP](https://www.hahwul.com/sec/web-security/csp/#benefits-of-csp)

[Conclusion](https://www.hahwul.com/sec/web-security/csp/#conclusion)

[Next

How to Securing GraphQL](https://www.hahwul.com/sec/web-security/graphql/)

[Contact](/contact)
[Thanks](/thanks)
[Sitemap](/sitemap.xml)
Random
[Feeds](/feeds)

© 2025 HAHWUL
Developed and Designed by Me

* [WHO](/about/)
* [BLOG](/blog/)
* [SEC](/sec/)
* [DEV](/dev/)
* [PROJECTS](/projects/)

---

* Language
  + [ENGLISH](https://www.hahwul.com/sec/web-security/csp/)
  + [한국어](https://www.hahwul.com/ko/sec/web-security/csp/)
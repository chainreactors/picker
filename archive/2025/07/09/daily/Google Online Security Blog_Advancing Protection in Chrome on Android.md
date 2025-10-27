---
title: Advancing Protection in Chrome on Android
url: http://security.googleblog.com/2025/07/advancing-protection-in-chrome-on.html
source: Google Online Security Blog
date: 2025-07-09
fetch_date: 2025-10-06T23:28:25.866574
---

# Advancing Protection in Chrome on Android

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Advancing Protection in Chrome on Android](https://security.googleblog.com/2025/07/advancing-protection-in-chrome-on.html "Advancing Protection in Chrome on Android")

July 8, 2025

Posted by David Adrian, Javier Castro & Peter Kotwicz, Chrome Security Team

Android recently announced [Advanced Protection](https://security.googleblog.com/2025/05/advanced-protection-mobile-devices.html), which extends Google’s [Advanced Protection Program](https://landing.google.com/intl/en_in/advancedprotection/) to a device-level security setting for Android users that need heightened security—such as journalists, elected officials, and public figures. Advanced Protection gives you the ability to activate Google’s strongest security for mobile devices, providing greater peace of mind that you’re better protected against the most sophisticated threats.

Advanced Protection acts as a single control point for at-risk users on Android that enables important security settings across applications, including many of your favorite Google apps, including Chrome. In this post, we’d like to do a deep dive into the Chrome features that are integrated with Advanced Protection, and how enterprises and users outside of Advanced Protection can leverage them.

Android Advanced Protection integrates with Chrome on Android in three main ways:

* **Enables the “Always Use Secure Connections”** setting for both public and private sites, so that users are protected from attackers reading confidential data or injecting malicious content into insecure plaintext HTTP connections. Insecure HTTP represents less than 1% of page loads for Chrome on Android.
* **Enables full Site Isolation** on mobile deviceswith 4GB+ RAM, so that potentially malicious sites are never loaded in the same process as legitimate websites. Desktop Chrome clients already have full Site Isolation.
* **Reduces attack surface** by disabling Javascript optimizations, so that Chrome has a smaller attack surface and is harder to exploit.

Let’s take a look at all three, learn what they do, and how they can be controlled outside of Advanced Protection.

### Always Use Secure Connections

“Always Use Secure Connections” (also known as HTTPS-First Mode in blog posts and HTTPS-Only Mode in the enterprise policy) is a Chrome setting that forces HTTPS wherever possible, and asks for explicit permission from you before connecting to a site insecurely. There may be attackers attempting to interpose on connections on any network, whether that network is a coffee shop, airport, or an Internet backbone. This setting protects users from these attackers reading confidential data and injecting malicious content into otherwise innocuous webpages. This is particularly useful for Advanced Protection users, since in 2023, plaintext HTTP was [used as an exploitation vector during the Egyptian election](https://citizenlab.ca/2023/09/predator-in-the-wires-ahmed-eltantawy-targeted-with-predator-spyware-after-announcing-presidential-ambitions/).

Beyond Advanced Protection, we [previously posted](https://blog.chromium.org/2023/08/towards-https-by-default.html) about how our goal is to eventually enable “Always Use Secure Connections” by default for all Chrome users. As we work towards this goal, in the last two years we have quietly been enabling it in more places beyond Advanced Protection, to help protect more users in risky situations, while limiting the number of warnings users might click through:

* We added a new variant of the setting that only warns on public sites, and doesn’t warn on local networks or single-label hostnames (e.g. `192.168.0.1`, `shortlink/`, `10.0.0.1`). These names often cannot be issued a publicly-trusted HTTPS certificate. This variant protects against most threats—accessing a public website insecurely—but still allows for users to access local sites, which may be on a more trusted network, without seeing a warning.
* We’ve automatically enabled “Always Use Secure Connections” for public sites in Incognito Mode for the last year, since Chrome 127 in June 2024.
* We automatically prevent downgrades from HTTPS to plaintext HTTP on sites that Chrome knows you typically access over HTTPS (a heuristic version of the [HSTS header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security)), since Chrome 133 in January 2025.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1HgJLjo8SSJOSaofi-04nW0P6izX70Lq12Y8J_Rxm_M0i5DaYCQKTD34SA9KBd4SSWP-7YrsX3N_6x9EU-t4OL54ODNAaLSTxgmHxLn-4khVXEfCrtlX__DYOaeLStl9yaCJOaP7N3FpzwAp-UzdkS9YZvPgSxCeIZSMk1O0sNqKjLsR_zTQk5PGX1XLt/s1600/Screenshot%202025-07-08%20at%2012.26.45%E2%80%AFPM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1HgJLjo8SSJOSaofi-04nW0P6izX70Lq12Y8J_Rxm_M0i5DaYCQKTD34SA9KBd4SSWP-7YrsX3N_6x9EU-t4OL54ODNAaLSTxgmHxLn-4khVXEfCrtlX__DYOaeLStl9yaCJOaP7N3FpzwAp-UzdkS9YZvPgSxCeIZSMk1O0sNqKjLsR_zTQk5PGX1XLt/s1600/Screenshot%202025-07-08%20at%2012.26.45%E2%80%AFPM.png)

*Always Use Secure Connections has two modes—warn on insecure public sites, and warn on any insecure site.*

Any user can enable “Always Use Secure Connections” in the Chrome Privacy and Security settings, regardless of if they’re using Advanced Protection. Users can choose if they would like to warn on *any* insecure site, or only insecure public sites. Enterprises can opt their fleet into either mode, and set exceptions using the `[HTTPSOnlyMode](https://chromeenterprise.google/policies/#HttpsOnlyMode)` and `[HTTPAllowlist](https://chromeenterprise.google/policies/#HttpAllowlist)` policies, respectively. Website operators should protect their users' confidentiality, ensure their content is delivered exactly as they intended, and avoid warnings, by deploying HTTPS.

### Full Site Isolation

[Site Isolation](https://youtu.be/OH-bt7spDgo?si=42mRq7VdtpC1q-5P) is a security feature in Chrome that isolates each website into its own rendering OS process. This means that different websites, even if loaded in a single tab of the same browser window, are kept completely separate from each other in memory. This isolation prevents a malicious website from accessing data or code from another website, even if that malicious website manages to exploit a vulnerability in Chrome’s renderer—a second bug to escape the renderer sandbox is required to access other sites. Site isolation improves security, but requires extra memory to have one process per site. Chrome Desktop isolates all sites by default. However, Android is particularly sensitive to memory usage, so for mobile Android form factors, when Advanced Protection is off, Chrome will only isolate a site if a user logs into that site, or if the user submits a form on that site. On Android devices with 4GB+ RAM in Advanced Protection (and on all desktop clients), Chrome will isolate *all* sites. Full Site Isolation significantly reduces the risk of cross-site data leakage for Advanced Protection users.

### JavaScript Optimizations and Security

Advanced Protection reduces the attack surface of Chrome by disabling the higher-level optimizing Javascript compilers inside V8. V8 is Chrome’s high-performance Javascript and [WebAssembly](https://webassembly.org/) engine. The optimizing compilers in V8 make certain websites run faster, however they historically also have been a source of known exploitation of Chrome. Of all the patched security bugs in V8 with known exploitation, disabling the optimizers would have mitigated ~50%. However, the optimizers are why Chrome scores the highest on industry-wide benchmarks such as [Speedometer](https://browserbench.org/Speedometer3.0/). Disabling the optim...
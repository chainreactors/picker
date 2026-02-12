---
title: A “Safe Browsing Blocker” in a Phishing Kit: Technical Analysis and Why It Fails
url: https://www.d3lab.net/a-safe-browsing-blocker-in-a-phishing-kit-technical-analysis-and-why-it-fails/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-11
fetch_date: 2026-02-12T04:22:57.763917
---

# A “Safe Browsing Blocker” in a Phishing Kit: Technical Analysis and Why It Fails

[![D3Lab](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2019/04/D3Lab_Logo_Enfold-300x102.png?fit=300%2C102&ssl=1 "D3Lab_Logo_Enfold-300×102")](https://www.d3lab.net/ "D3Lab_Logo_Enfold-300×102")

* [Home](https://www.d3lab.net/)
* [Services](/#services)
* [Philosophy](/#philosophy)
* [Contact](/#contact)
* [Blog](https://www.d3lab.net/blog/)
* [Fare clic per aprire il campo di ricerca
  Fare clic per aprire il campo di ricerca

  Cerca](?s= "Fare clic per aprire il campo di ricerca")
* **Menu**
  Menu

* [Collegamento a X](https://twitter.com/D3LabIT "Collegamento a X")
* [Collegamento a LinkedIn](https://www.linkedin.com/company/d3labsrl/ "Collegamento a LinkedIn")
* [Collegamento a Rss questo sito](https://www.d3lab.net/feed/ "Collegamento a Rss  questo sito")
* [Collegamento a Mail](/#contact "Collegamento a Mail")

# A “Safe Browsing Blocker” in a Phishing Kit: Technical Analysis and Why It Fails

[Phishing](https://www.d3lab.net/category/phishing/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/02/SafeBrowsingBlocker_Cover.png?resize=1210%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/02/SafeBrowsingBlocker_Cover.png?fit=1030%2C687&ssl=1 "SafeBrowsingBlocker_Cover")

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/02/SafeBrowsingBlocker_Cover.png?resize=1030%2C687&ssl=1)

In February 2026, the D3Lab Anti‑Fraud Team analyzed a phishing kit that embedded a JavaScript file named `ss1.js`. The script, branded **SafeBrowsingBlocker**, attempts to prevent Google Safe Browsing checks by blocking network requests to Google Safe Browsing domains and disabling browser prefetching/prerendering mechanisms.

Our technical analysis shows that this approach is **largely ineffective** against browser‑level Safe Browsing interstitials, which are decided **before** any page JavaScript executes. The script’s primary effect is limited to blocking **page‑initiated** requests (e.g., `fetch`, XHR, `sendBeacon`) and adding a restrictive CSP that can **break legitimate resources**.

This post details how the script works, why it cannot bypass Safe Browsing, and provides IoCs for detection.

## Context: Where the Script Is Loaded

The phishing page loads the script in the `<head>` and initializes it immediately:

```
<head>
<script src="381890/ss1.js"></script>
<script>
  new SafeBrowsingBlocker({ verbose: false });
</script>
</head>
```

## Technical Analysis

### 1) Blocking Safe Browsing Domains in `fetch` and XHR

The script overrides `fetch` and `XMLHttpRequest.prototype.open` to block a hardcoded list of Google Safe Browsing endpoints. A simplified excerpt:

```
const blockedDomains = [
  'safebrowsing.googleapis.com',
  'safebrowsing-cache.google.com',
  'sb-ssl.google.com',
  'sb.google.com',
  'safebrowsing.google.com',
  'update.googleapis.com/service/update2/crx',
];

const originalFetch = window.fetch;
window.fetch = function (...args) {
  const url = typeof args[0] === 'string' ? args[0] : (args[0] && args[0].url) || '';
  if (blockedDomains.some(d => url.includes(d))) {
    return Promise.reject(new Error('Request blocked by SafeBrowsingBlocker'));
  }
  return originalFetch.apply(this, args);
};

const originalOpen = XMLHttpRequest.prototype.open;
XMLHttpRequest.prototype.open = function (...args) {
  const url = args[1];
  if (blockedDomains.some(d => url.includes(d))) {
    throw new Error('Request blocked by SafeBrowsingBlocker');
  }
  return originalOpen.apply(this, args);
};
```

**What this actually does:** it blocks **page‑level** network requests to those domains. It **does not** affect the browser’s Safe Browsing decision process, which happens **before** the phishing page runs any JavaScript.

### 2) Disabling Prefetching/Prerendering

The script removes and blocks `<link rel="prefetch|prerender|dns-prefetch|preconnect">` tags to reduce background network activity.

```
const prefetchLinks = document.querySelectorAll(
  'link[rel="prefetch"], link[rel="prerender"], link[rel="dns-prefetch"], link[rel="preconnect"]'
);

prefetchLinks.forEach(link => link.remove());
```

**Why it’s ineffective for bypassing Safe Browsing:** prefetching controls are not the mechanism used by Safe Browsing to show the red interstitial. The decision is made by the browser security stack **before** the DOM is even constructed.

### 3) Blocking `navigator.sendBeacon`

The script overrides `navigator.sendBeacon` to prevent background telemetry:

```
if (navigator.sendBeacon) {
  navigator.sendBeacon = function (url, data) {
    return false;
  };
}
```

This can prevent some analytics from being sent, but it **does not stop** the browser’s threat checks.

### 4) Injecting a CSP via `<meta>`

The script adds a CSP meta tag that only allows `self` by default.

```
<meta http-equiv="Content-Security-Policy"
      content="default-src 'self'; connect-src 'self'; ...">
```

This can actually **break** external resources in a phishing kit (e.g., CDN scripts, fonts). It also cannot override **server‑sent CSP** or browser‑level security decisions.

## Why This Script Fails to Bypass Safe Browsing

Safe Browsing interstitials are triggered by **browser‑level and service‑level checks** that occur **before the phishing page can execute any JavaScript**. Blocking network requests **from the page** cannot retroactively alter that decision.

In short:

* **Too late in the chain**: the check happens before `ss1.js` runs.
* **Wrong layer**: it only affects **page JS**, not browser security engines.
* **Limited scope**: it may block page‑initiated telemetry, but not Safe Browsing.

## Indicators of Compromise (IoCs)

* **Script name / path**: `381890/ss1.js`
* **Hash**: `50b9d271cd021f47587f8b85570b30a544a23ebfcea8d9a81a930bedbf9f2b19`
* **Class name**: `SafeBrowsingBlocker`
* **Functionality string**: “Safe Browsing Blocker – COMPLETE STANDALONE VERSION”

## Open‑Source Visibility and Recency

Our team checked public scanners and found:

* **[Urlscan](https://urlscan.io/search/#hash%3A50b9d271cd021f47587f8b85570b30a544a23ebfcea8d9a81a930bedbf9f2b19)**: only one scan result (our own), observed **9 Feb 2026**.
* **[VirusTotal](https://www.virustotal.com/gui/file/50b9d271cd021f47587f8b85570b30a544a23ebfcea8d9a81a930bedbf9f2b19/detection)**: no prior submissions.

This strongly suggests the script is **very recent** and has **limited distribution** at the time of analysis.

## Final Assessment

The `ss1.js` “SafeBrowsingBlocker” is a clear example of **security theater** in phishing kits: it tries to block Safe Browsing by interfering with client‑side requests, but it is **ineffective** against the browser’s real‑time threat checks. Its main impact is disrupting page‑level telemetry and potentially breaking legitimate resources.

For defenders, the script remains a useful IoC and a behavioral indicator of phishing tooling that tries to evade analysis with superficial client‑side measures.

11 Febbraio 2026/da [Andrea Draghetti](https://www.d3lab.net/author/andrea-d/ "Articoli scritti da Andrea Draghetti")

##### Condividi questo articolo

* [Condividi su Facebook](https://www.facebook.com/sharer.php?u=https://www.d3lab.net/a-safe-browsing-blocker-in-a-phishing-kit-technical-analysis-and-why-it-fails/&t=A%20%E2%80%9CSafe%20Browsing%20Blocker%E2%80%9D%20in%20a%20Phishing%20Kit%3A%20Technical%20Analysis%20and%20Why%20It%20Fails)
* [Condividi su X](https://twitter.com/share?text=A%20%E2%80%9CSafe%20Browsing%20Blocker%E2%80%9D%20in%20a%20Phishing%20Kit%3A%20Technical%20Analysis%20and%20Why%20It%20Fails&url=https://wp.me/p7upL6-1yE)
* [Condividi su WhatsApp](https://api.whatsapp.com/send?text=https://www.d3lab.net/a-safe-browsing-blocker-in-a-phishing-kit-technical-analysis-and-why-it-fails/)
* [Condividi su Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.d3lab.net%2Fa-safe-browsing-blocker-in-a-phishing-kit-technical-analysis-and-why-it-fails%2F&description=A%20%E2%80%9CSafe%20Browsing%20Blocker%E2%80%9D%20in%20a...
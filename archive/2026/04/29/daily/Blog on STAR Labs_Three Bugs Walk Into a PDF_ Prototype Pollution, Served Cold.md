---
title: Three Bugs Walk Into a PDF: Prototype Pollution, Served Cold
url: https://starlabs.sg/blog/2026/04-three-bugs-walk-into-a-pdf-prototype-pollution-served-cold/
source: Blog on STAR Labs
date: 2026-04-29
fetch_date: 2026-04-30T05:28:57.594972
---

# Three Bugs Walk Into a PDF: Prototype Pollution, Served Cold

[![STAR Labs](/images/logo.png)](/)

[About](/about/)
[Services](/services/)
[Advisories](/advisories/)
[Blog](/blog/)
[Achievements](/achievements/)
[Publications](/publications/)
[Team](/team/)
[RSS](/index.xml)

MENU

Research
April 29, 2026
By Shreyas Penkar (@streypaws)
13 min read

# Three Bugs Walk Into a PDF: Prototype Pollution, Served Cold

Table of Contents

* [TL;DR](#tldr)
* [Introduction](#introduction)
* [How Adobeâs Fixes Gave It Away](#how-adobes-fixes-gave-it-away)
* [Three Polluted Primitives, One Pure Chain](#three-polluted-primitives-one-pure-chain)
* [Conclusion](#conclusion)
* [References:](#references)

## TL;DR

In April 2026, Adobe disclosed three critical security issues ([CVE-2026-34621](%28https%3A//helpx.adobe.com/security/products/acrobat/apsb26-43.html%29),[CVE-2026-34622,CVE-2026-34626](https://helpx.adobe.com/security/products/acrobat/apsb26-44.html)) affecting Acrobat DC, Acrobat Reader DC, and Acrobat 2024. According to Adobeâs advisories, these vulnerabilities could allow attackers to execute arbitrary code and leak user information through a malicious PDF file via a prototype pollution chain and they were reportedly exploited in the wild. The initial issue, `CVE-2026-34621`, was first identified by [EXPMON](https://justhaifei1.blogspot.com/2026/04/expmon-detected-sophisticated-zero-day-adobe-reader.html?m=1).

While several reports have already covered the threat intelligence and malware-analysis aspects of the ITW samples, we were more interested in the underlying vulnerabilities themselves and how Adobe patched them.

To that end, we reverse-engineered the fixes across two product versions and analyzed the malware sample for validation and additional context. This allowed us to identify the root cause of the issues, understand the patch behavior, and develop a trigger PoC. This post documents our process of reproducing and analyzing the bugs to better understand how they were exploited in the wild and what primitives they enabled.

## Introduction

|  |  |
| --- | --- |
| CVE | CVE-2026-34621 |
| Impact | High |
| Affected Products | Windows/MacOS Systems having Adobe Reader 26.001.21367 and earlier |
| Bug IDs | APSB26-43 |
| Patch | <https://helpx.adobe.com/security/products/acrobat/apsb26-43.html> |

|  |  |
| --- | --- |
| CVE | CVE-2026-34622, CVE-2026-34626 |
| Impact | High |
| Affected Products | Windows/MacOS Systems having Adobe Reader 26.001.21411 and earlier |
| Bug IDs | APSB26-44 |
| Patch | <https://helpx.adobe.com/security/products/acrobat/apsb26-44.html> |

We first encountered these three issues in Adobeâs April 2026 [Emergency](https://helpx.adobe.com/security/products/acrobat/apsb26-43.html) [Updates](https://helpx.adobe.com/security/products/acrobat/apsb26-44.html) for Acrobat Reader, where they were described as âImproperly Controlled Modification of Object Prototype Attributesâ or prototype pollution bugs. Adobe initially marked `CVE-2026-34621` as being exploited in the wild on 12th April, but subsequent [public reports](https://x.com/greenapple_w/status/2044136479283392862) suggested that the fix may have been incomplete. Two days later, Adobe released another update that addressed two additional issues, `CVE-2026-34626` and `CVE-2026-34622`.

That made the situation even more interesting. To understand what was actually going on, we decided to reverse-engineer the fixes across the two versions, trace the root cause of each CVE, and then develop a trigger PoC to validate our findings.

## How Adobeâs Fixes Gave It Away

We analyzed patch differences between consecutive Adobe Reader releases to identify affected code paths and understand the underlying causes of each vulnerability. The comparison included:

* `Adobe Reader 26.001.21367` â `26.001.21411` for `CVE-2026-34621`
* `Adobe Reader 26.001.21411` â `26.001.21431` for `CVE-2026-34626` and `CVE-2026-34622`

This process made it possible to pinpoint the exact changes introduced in each patch and relate them directly to the vulnerabilities they address.

For `CVE-2026-34621`, the fix is a single-line change, as illustrated in the patch diff:

![Patch 1](/blog/2026/images/Three-Bugs-Walk-Into-a-PDF-001.png)
**Figure 1: Patch One**

![Patch 2](/blog/2026/images/Three-Bugs-Walk-Into-a-PDF-002.png)
**Figure 2: Patch Two**

This patch changes `swConn` from a property-resolved name into a true local variable. Now, `swConn` is allocated as a local binding in the current function so reads of `swConn` no longer consult the global object or inherited prototypes. After analysing the code further we found that the root cause for this issue is an unsafe use of an unqualified non-local `swConn` identifier inside a privileged collaboration login workflow, specifically in the `SilentDocCenterLogin` function *[1]*. In the vulnerable code, `swConn` is assigned without a local declaration:

```
function SilentDocCenterLogin (data, connectParams)
	var isFirstLaunch = false;
	app.beginPriv()
	isFirstLaunch = Collab.isFirstLaunch(data.WT);
	app.endPriv();
	app.beginPriv();
	data.user = Collab.getUserIDFromStore();
	app.endPriv();
	if(isFirstLaunch)
		data.isFirstLaunch = true;
		return false;
	if(data.reviewType == "SharedReview" || data.reviewType == "FormDistribution")
        var addStringToPayloadParams = {};
	    addStringToPayloadParams.name = "Authentication_Successful";
	try
	    app.beginPriv();
	    swConn = Collab.swConnect(connectParams/*{bShowProgressMonitor: bShowProgressMonitor}*/); // [1]
	    app.endPriv();
        ...
        ...
```

In Acrobat’s JavaScript environment, that means `swConn` earlier was not a lexical local variable. Instead, it was resolved through the global object/property lookup path. This is exactly the kind of situation where prototype pollution becomes dangerous. If an attacker can influence how `swConn` resolves, the collaboration code may read or write an attacker controlled object rather than a real internal connection object.

So if `Object.prototype.swConn` is polluted, the trusted collaboration code then later used `swConn`, it interacted with an attacker-supplied fake object. This fake object then could redirect execution into a `SOAP.stringFromStream` (fake stream path) and ultimately cause `app.trustedFunction(functionRef)` to be invoked on attacker-selected functions, which can lead to privilege escalation within Adobe Reader. That’s a powerful primitive in itself. Let’s check out the other 2 issues.

Amongst the few changes we saw in this new diff, 2 of them stood out as security fixes. This is the first fix -

![Patch 3](/blog/2026/images/Three-Bugs-Walk-Into-a-PDF-003.png)
**Figure 3: Patch Three**

This patch in the `ANFancyAlertImpl` function changes the handler construction model from `data -> source code -> eval -> function` to `data -> closure parameter -> function`. Now `bid` is carried only as a runtime value captured by a closure so a malicious `bid` can only be a string value passed to `dialog.end(id)`. `ANFancyAlertImpl` basically iterates over the keys of the `buttons` object and used each key to build a handler string, then passes that string to `eval`. The vulnerable code looked like:

```
...
...
for(var i in buttons)
    var bc = buttons[i];
    var bid = "btn" + i;
    ba[ba.length] = {
        type: "button",
        item_id: bid,
        name: bc,
        alignment: "align_right"
    };
    // throw a handler for the button in
    desc[bid] = eval("(function(dialog) { dialog.end('" + bid + "'); })"); // [2]
    ...
    ...
```

Here, the function could potentially enumerate attacker controlled object keys, derive `bid = "btn" + i`, splice `bid` directly into JavaScript source text, and `eval` the resulting handler *[2]*. This could lead to attacker javascript code execution from attacker controlled dialog button identifiers. A useful primitive for bootstrapping. The fix seems to remove the interpreter boundary entirely rather than trying to escape strings more carefull...
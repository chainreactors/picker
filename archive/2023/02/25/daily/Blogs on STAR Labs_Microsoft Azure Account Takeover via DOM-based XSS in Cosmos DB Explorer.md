---
title: Microsoft Azure Account Takeover via DOM-based XSS in Cosmos DB Explorer
url: https://starlabs.sg/blog/2023/02-microsoft-azure-account-takeover-via-dom-based-xss-in-cosmos-db-explorer/
source: Blogs on STAR Labs
date: 2023-02-25
fetch_date: 2025-10-04T08:03:25.180788
---

# Microsoft Azure Account Takeover via DOM-based XSS in Cosmos DB Explorer

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# Microsoft Azure Account Takeover via DOM-based XSS in Cosmos DB Explorer

February 24, 2023 · 5 min · Ngo Wei Lin (@Creastery)

Table of Contents

* [About the DOM XSS Vulnerability](#about-the-dom-xss-vulnerability)
* [Full Technical Details – Researcher’s Point of View](#full-technical-details--researchers-point-of-view)
  + [Incorrect Origin Check](#incorrect-origin-check)
  + [DOM-based XSS](#dom-based-xss)
  + [A Proof-of-Concept for the DOM XSS Vulnerability](#a-proof-of-concept-for-the-dom-xss-vulnerability)
    - [Setting Up Environment](#setting-up-environment)
    - [How Victim gets Compromised](#how-victim-gets-compromised)
* [Recommendations](#recommendations)
* [Final Thoughts](#final-thoughts)

Upon finding the vulnerability, our team member, Ngo Wei Lin ([@Creastery](https://twitter.com/creastery)), immediately reported it to the Microsoft Security Response Center (MSRC) on 19th March 2022, who fixed the important issue with a [fix commited in the repo](https://github.com/Azure/cosmos-explorer/commit/496f596f385e732e47579bd1b45b9ee5868fafac) within seven days, which is impressive and a much faster response than other Microsoft bugs which we reported previously. The fix was pushed down to [Azure Cosmos DB Explorer](https://cosmos.azure.com) on 31st March 2022.

## About the DOM XSS Vulnerability[#](#about-the-dom-xss-vulnerability)

The Azure Cosmos DB Explorer incorrectly accepts and processs cross-origin messages from certain domains. A remote attacker can take over a victim Azure user’s account by delivering a DOM-based XSS payload via a cross-origin message.

## Full Technical Details – Researcher’s Point of View[#](#full-technical-details--researchers-point-of-view)

The root cause analysis is performed using the latest changeset ([d1587ef](https://github.com/Azure/cosmos-explorer/commit/d1587ef033914cfc540c95421b830e52087f4114)) of the [Azure/cosmos-explorer](https://github.com/Azure/cosmos-explorer) repository at the point of discovering the vulnerability.

### Incorrect Origin Check[#](#incorrect-origin-check)

The relevant vulnerable code from [/src/ConfigContext.ts](https://github.com/Azure/cosmos-explorer/blob/d1587ef033914cfc540c95421b830e52087f4114/src/ConfigContext.ts#L50-59) is shown below:

```
let configContext: Readonly<ConfigContext> = {
  platform: Platform.Portal,
  allowedParentFrameOrigins: [
    `^https:\\/\\/cosmos\\.azure\\.(com|cn|us)$`,
    `^https:\\/\\/[\\.\\w]*portal\\.azure\\.(com|cn|us)$`,
    `^https:\\/\\/[\\.\\w]*portal\\.microsoftazure.de$`,
    `^https:\\/\\/[\\.\\w]*ext\\.azure\\.(com|cn|us)$`,
    `^https:\\/\\/[\\.\\w]*\\.ext\\.microsoftazure\\.de$`,
    `^https://cosmos-db-dataexplorer-germanycentral.azurewebsites.de$`, //vulnerable
  ],
  ...
}
```

Note that `configContext.allowedParentFrameOrigins` is used in [/src/Utils/MessageValidation.ts](https://github.com/Azure/cosmos-explorer/blob/d1587ef033914cfc540c95421b830e52087f4114/src/Utils/MessageValidation.ts), where the origin check is performed:

```
export function isInvalidParentFrameOrigin(event: MessageEvent): boolean {
  return !isValidOrigin(configContext.allowedParentFrameOrigins, event);
}

function isValidOrigin(allowedOrigins: string[], event: MessageEvent): boolean {
  const eventOrigin = (event && event.origin) || "";
  const windowOrigin = (window && window.origin) || "";
  if (eventOrigin === windowOrigin) {
    return true;
  }

  for (const origin of allowedOrigins) {
    const result = new RegExp(origin).test(eventOrigin);
    if (result) {
      return true;
    }
  }
  console.error(`Invalid parent frame origin detected: ${eventOrigin}`);
  return false;
}
```

Observe that the last regular expression (`^https://cosmos-db-dataexplorer-germanycentral.azurewebsites.de$`) is incorrect, as metacharacters (e.g. in regular expressions, the character `.` matches any character) are not properly escaped.

This means that the following domains are also incorrectly treated as trusted sources of cross-origin messages:

* `https://cosmos-db-dataexplorer-germanycentralAazurewebsites.de`
* `https://cosmos-db-dataexplorer-germanycentralBazurewebsites.de`
* …
* `https://cosmos-db-dataexplorer-germanycentralYazurewebsites.de`
* `https://cosmos-db-dataexplorer-germanycentralZazurewebsites.de`

As such, an attacker can purchase any of the above domains to send cross-origin messages to `cosmos.azure.com`, which will be accepted and processed.

### DOM-based XSS[#](#dom-based-xss)

The relevant vulnerable code from [/src/Controls/Heatmap/Heatmap.ts](https://github.com/Azure/cosmos-explorer/blob/d1587ef033914cfc540c95421b830e52087f4114/src/Controls/Heatmap/Heatmap.ts#L221-268) is shown below:

```
export function handleMessage(event: MessageEvent) {
  if (isInvalidParentFrameOrigin(event)) {
    return;
  }

  if (typeof event.data !== "object" || event.data["signature"] !== "pcIframe") {
    return;
  }
  if (
    typeof event.data.data !== "object" ||
    !("chartData" in event.data.data) ||
    !("chartSettings" in event.data.data)
  ) {
    return;
  }
  Plotly.purge(Heatmap.elementId);

  document.getElementById(Heatmap.elementId)!.innerHTML = "";
  const data = event.data.data;
  const chartData: DataPayload = data.chartData;
  const chartSettings: HeatmapCaptions = data.chartSettings;
  const chartTheme: PortalTheme = data.theme;
  if (Object.keys(chartData).length) {
    new Heatmap(chartData, chartSettings, chartTheme).drawHeatmap();
  } else {
    const chartTitleElement = document.createElement("div");
    chartTitleElement.innerHTML = data.chartSettings.chartTitle;  // XSS
    chartTitleElement.classList.add("chartTitle");

    const noDataMessageElement = document.createElement("div");
    noDataMessageElement.classList.add("noDataMessage");
    const noDataMessageContent = document.createElement("div");
    noDataMessageContent.innerHTML = data.errorMessage;           // XSS

    noDataMessageElement.appendChild(noDataMessageContent);

    if (isDarkTheme(chartTheme)) {
      chartTitleElement.classList.add("dark-theme");
      noDataMessageElement.classList.add("dark-theme");
      noDataMessageContent.classList.add("dark-theme");
    }

    document.getElementById(Heatmap.elementId)!.appendChild(chartTitleElement);
    document.getElementById(Heatmap.elementId)!.appendChild(noDataMessageElement);
  }
}

window.addEventListener("message", handleMessage, false);
```

Observe that `event.data.chartSettings.chartTitle` and `event.data.errorMessage` can result in DOM-based XSS. In this case, an attacker who satisfies the origin check can send cross-origin messages to perform DOM-based XSS on `cosmos.azure.com`.

Examining the `Content-Security-Policy` header, it can be confirmed that inline scripts are permitted.

```
content-security-policy: frame-ancestors 'self' portal.azure.com *.portal.azure.com portal.azure.us portal.azure.cn portal.microsoftazure.de df.onecloud.azure-test.net
```

When the vulnerabilities are chained together, an attacker can trigger a DOM-based XSS on `cosmos.azure.com` to exfiltrate Azure user’s OAuth tokens.

### A Proof-of-Concept for the DOM XSS Vulnerability[#](#a-proof-of-concept-for-the-dom-xss-vulnerability)

This proof-of-concept assumes the use of the domain `cosmos-db-dataexplorer-germanycentralAazurewebsites.de`. However, note that any other domain which satisfies the origin check would work as well.

#### Setting Up Environment[#](#setting-up-environment)

**Option 1:** P...
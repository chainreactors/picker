---
title: Arabic Streaming Websites ClickFix Campaign
url: https://muha2xmad.github.io/threat-intelligence/streaming-clickfix-campaign/
source: Over Security
date: 2026-10-06
fetch_date: 2026-10-07T07:55:27.465493
---

# Arabic Streaming Websites ClickFix Campaign

## Skip links

* [Skip to primary navigation](#site-nav)
* [Skip to content](#main)
* [Skip to footer](#footer)

[![](/assets/images/site/lo.png)](/)
[muha2xmad](/)

* [Malware analysis](/categories/#Malware-analysis)
* [Mal Documents](/categories/#Mal-Document)
* [Threat Intelligence](/categories/#Threat-Intelligence)

Toggle search

Toggle menu

![Muhammad Hasan Ali](/assets/images/site/ed.jpg)

### Muhammad Hasan Ali

Malware Analysis

Follow

* Egypt
* [Twitter](https://twitter.com/muha2xmad)
* [LinkedIn](https://www.linkedin.com/in/muhammadhasanali/)
* [GitHub](https://github.com/muha2xmad)

# Arabic Streaming Websites ClickFix Campaign

19 minute read

#### On this page

* [Executive summary](#executive-summary)
* [Arabic streaming websites campaign](#arabic-streaming-websites-campaign)
  + [User Fingerprinting](#user-fingerprinting)
  + [Infrastructure Analysis](#infrastructure-analysis)
  + [Phishing patterns](#phishing-patterns)
  + [ClickFix Pages Analysis](#clickfix-pages-analysis)
  + [Commands Analysis](#commands-analysis)

بسم الله الرحمن الرحيم

# Executive summary

In the fast-evolving world of cyber threats, no tactic has captivated security researchers quite like ClickFix. Turning millions of seemingly legitimate websites into attack vectors. By exploiting user curiosity through error messages or CAPTCHA challenges, ClickFix lures unsuspecting visitors into manually executing malicious PowerShell or other command-line payloads which bypass traditional endpoint protection entirely.
Now, it is rapidly evolved into a Malware-as-a-Service (MaaS) ecosystem. Threat actors now deploy ClickFix through compromised WordPress sites, fake AI chatbots, and state-sponsored operations.

ClickFix attack flow:

* **Initial Access:** The user visits a malicious or compromised website.
* **Deceptive Lure:** The website redirects the user or displays a fake interface, such as:
  + A fraudulent reCAPTCHA verification prompt
  + A simulated browser error message
  + A fake browser update notification
* **Clipboard Injection:** When the user clicks to “verify” or “fix” the issue, a malicious command is automatically copied to their clipboard.
* **Social Engineering Execution:** The site instructs the user to open Command Prompt (cmd) or PowerShell and paste the copied command.
* **Payload Delivery:** Upon pasting and executing the command, the script downloads and installs the malicious payload onto the victim’s system.

![](/assets/images/TI/arabic/Pasted image 20260927053053.png)

---

# **Arabic streaming websites campaign**

The threat actor targets well-known Arabic streaming platforms by deploying systematic variations of their domains. This includes alternative TLDs (e.g. .cam, .party, .fast, .life, .land, .shop, .help, .ltd, .promo, .archi, .host) and misspelling domains writing to exploit common user typing errors.

The attack begins with domain impersonation, where attackers register domains that closely looks alike legitimate streaming platforms.
Once the user lands on the fake website, the threat actors profile or fingerprint the user. Then the user is redirected to the ClickFix page.

**Example: wecimaa[.]cyou**

In this example, the threat actor registered wecimaa[.]cyou, a typosquatted version of the legitimate streaming site `wecima`. When users visit this domain:

1. **Initial Landing**: User accessing the wecima streaming platform
2. **User Profiling**: Before any redirection occurs, the malicious JavaScript on the page collects detailed information about the user (Which will be explained in details later)
3. **Redirection**: After profiling is complete, users are automatically redirected to the ClickFix page
4. **Social Engineering**: The ClickFix page displays a message prompting users to press “Allow” so that a command can be copied to their clipboard
5. **Execution**: User pastes and runs this command, which typically downloads payload

![](/assets/images/TI/arabic/Recording2026-10-01013826.gif)

## **User Fingerprinting**

User fingerprinting is the process of collecting detailed telemetry from a visitor’s browser and device to create a unique profile. In cyber threats, this is used not just for tracking, but for **target selection and evasion**.
Instead of treating every visitor equally, the attacker uses this data to decide whether to deliver the malicious payload or divert the user elsewhere.

**Example:**

Initial Redirect
**URL:** `https://cf.quickbase.icu/middle.html?impId=...&ct=...`
impId = Unique tracking ID
ct = Encrypted session token from campaign

**Fingerprinting API Call**

**URL:** `https://cf.quickbase.icu/api/v1/px2?ct=...&minfo=...`
This is where the actual browser profiling happens. The JavaScript on `middle.html` collects telemetry and sends it via this API endpoint.

* **`ct`:** Same Click Token as above, helps to correlate the fingerprint data with the initial impression.
* **`minfo`:** A **Base64-encoded JSON object** containing detailed browser and system fingerprints.

After Decoding the JSON object:

```
{
  "cookieDisabled": false,  // whether browser cookies are disabled (true/false)
  "ua": "",  // User Agent string
  "iframe": false,  // if the page is loaded within an iframe (true/false)
  "devicePixelRatio": 1,  // Ratio of physical pixels to CSS pixels on the display
  "wndLocHref": "",  // Full URL of the current window location
  "deviceScreenSize": "",  // Total screen resolution
  "deviceWindowSize": "",  // Browser window size
  "wnd2srcRatLwr06": false,  // bot detection flag
  "effectiveType": "",  // Network connection type
  "tz": 420,  // Timezone offset from UTC in minutes
  "hidden": false,  // Indicates if the page is hidden or not visible
  "notFocused": false,  // Indicates if the browser window is not in focus
  "tzIntl": "",  // IANA timezone identifier
  "isBot": false,  // Bot detection result - indicates if visitor is automated
  "fBotName": "",  // Name of detected bot
  "fReasons": ""  // Reasons/flags for bot detection classification
}
```

**Final Redirect**

**URL:** `https://mangafantasyrealm.cfd/indexacrtbt3.php?cid=...&bid=...&source_subid=...&keyword=...&ref=...&IP=...&ua=...&flow=...`

After profiling confirms the user is a valid target, they are redirected to the final destination, the ClickFix page.

* **`cid` (Campaign ID):** `impId` value, which maintaining session continuity.
* **`bid`:** Bid price in USD; indicates this traffic is being sold through an ad exchange Traffic Distribution System
* **`source_subid`:** publisher tracking ID for revenue attribution.
* **`keyword`:** SEO/referral keywords passed for analytics
* `ref`: Explicit referrer field
* **`IP`:** Victim’s IP address
* **`ua`:** Full User-Agent string
* **`flow`:** Internal flow/route ID within the TDS; determines which landing page variant (e.g., ClickFix vs. direct malware) the user receives.

**Clickfix page:**

**URL:** `https://cmcln4.cinemadataflow.cfd/*`

**Fingerprinting overview:**

1. **Victim visits** `wecimaa.cyou` → redirected to `cf.quickbase.icu/middle.html`
2. **JavaScript profiles** the browser extensively via `/api/v1/px2`, sending encoded telemetry
3. **Server evaluates** fingerprint: checks for bots, sandboxes, timezone mismatches, and valid sessions
4. **If valid**, user is redirected through a TDS (`mangafantasyrealm.cfd`) with full attribution parameters to the ClickFix landing page (`cmcln4.cinemadataflow.cfd`)
5. **ClickFix page** prompts user to press “Allow” → malicious command copied to clipboard → user executes it manually

**Why fingerprinting is used: The “Gatekeeper” Function**

Once a user’s profile and behavioral data have been collected, the backend determines how to route the user. Redirecting them either to the clickfix page or to an ad.

* Users who are not targeted (e.g., bots or researchers visiting the page repeatedly with the same profile) are shown ads.
* Users identified as targets are redirected to the clickfix page.

**Evasion techniques:**

Based on t...
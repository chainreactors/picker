---
title: uBlock v1.74.1b3
url: https://kitploit.com/en/posts/github-gorhill-ublock-1741b3
source: Kitploit
date: 2026-09-06
fetch_date: 2026-09-07T06:48:48.374629
---

# uBlock v1.74.1b3

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/50911/01af5b8e063efc3b85f9642a29eef2521e1a34a6918be9fa4fab6b6164f7e028-display-v1.webp)

New releaseSep 6, 2026

# uBlock v1.74.1b3

Wide-spectrum content blocker for browsers that blocks ads, trackers, coin miners, and malicious sites using filter lists and customizable privacy rules.

Share

[![Badge Commits](https://img.shields.io/github/commit-activity/m/gorhill/ublock?label=Commits)](https://github.com/gorhill/uBlock/commits/master)
[![Badge Issues](https://img.shields.io/github/issues/uBlockOrigin/uBlock-issues)](https://github.com/uBlockOrigin/uBlock-issues/issues)
[![Badge Localization](https://d322cqt584bo4o.cloudfront.net/ublock/localized.svg)](https://crowdin.com/project/ublock)
[![Badge License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://raw.githubusercontent.com/gorhill/ublock/master/LICENSE.txt)
[![Badge NPM](https://img.shields.io/npm/v/@gorhill/ubo-core)](https://www.npmjs.com/package/%40gorhill/ubo-core)
[![Badge Mozilla](https://img.shields.io/amo/rating/ublock-origin?label=Firefox)](https://addons.mozilla.org/addon/ublock-origin/)
[![Badge Chrome](https://img.shields.io/chrome-web-store/rating/cjpalhdlnbpafiamejdnhcphjbkeiagm?label=Chrome)](https://chromewebstore.google.com/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm)
[![Badge Edge](https://img.shields.io/badge/dynamic/json?label=Edge&color=brightgreen&query=$.averageRating&suffix=/5&url=https://microsoftedge.microsoft.com/addons/getproductdetailsbycrxid/odfafepnkmbhccpbejgmiehpchacaeak)](https://microsoftedge.microsoft.com/addons/detail/ublock-origin/odfafepnkmbhccpbejgmiehpchacaeak)

---

# ![](https://raw.githubusercontent.com/gorhill/uBlock/master/src/img/ublock.svg) uBlock Origin (uBO)

| Browser | Install from ... | Status |
| --- | --- | --- |
| ![Get uBlock Origin for Firefox](https://assets.kitploit.com/production/public/readmes/50911/98c4837a6cdce28d66cd51ea1e13cf130a5ac7bd097579a6714ad8345c16d3c9/a1d48b6a2208f87b3ba751dbf00860a2201d402349d0c6a31b2ad6c8c4a7ea10-display-v1.webp) | [Firefox Add-ons](https://addons.mozilla.org/addon/ublock-origin/) | [uBO works best on Firefox](https://github.com/gorhill/uBlock/wiki/uBlock-Origin-works-best-on-Firefox) |
| ![Get uBlock Origin for Microsoft Edge](https://assets.kitploit.com/production/public/readmes/50911/a189a6054451f74073ba27c9e0ff35f46402263a2f883a74b9f6a89bb42b7975/002923dba12d63f6511cd3b98d5145d8b997531f2fcb94f4935303abd70f8627-display-v1.webp) | [Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/ublock-origin/odfafepnkmbhccpbejgmiehpchacaeak) | ["Moving the Microsoft Edge extensions ecosystem forward with Manifest Version 3"](https://blogs.windows.com/msedgedev/2026/08/07/moving-the-microsoft-edge-extensions-ecosystem-forward-with-manifest-version-3/): "Beginning in August 2026, Microsoft Edge will start the consumer transition away from Manifest Version 2 (MV2) extensions and toward MV3. Our goal is to complete the consumer transition by the end of 2026, with enterprise deprecation following in early 2027." |
| ![Get uBlock Origin for Opera](https://assets.kitploit.com/production/public/readmes/50911/907f47f584ca0f83446680a2ce1b4dc4dc81ac2e2bec0090e5b4ac98ccade4d4/bfb6916877b9e1e982f6539c5063903da10e668f4bcb5a691664e29c257ee5a8-display-v1.webp) | [Opera Add-ons](https://addons.opera.com/extensions/details/ublock/) |  |
| ![Get uBlock Origin for Chromium](https://assets.kitploit.com/production/public/readmes/50911/eccdfe9d867373e2da66eedfcaaab40cbcdf6a221b83d6ee1400895a3e4c8046/4c991de3670f203abba51bf3ba9031b63b76c418a7c020cbdb236bc789c89db9-display-v1.webp) | [Chrome Web Store](https://chromewebstore.google.com/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm) | ["Manifest V2 support timeline"](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline#aug_31st_2026_all_remaining_manifest_v2_extensions_removed_from_the_chrome_web_store): "Aug 31st 2026: All remaining Manifest V2 extensions removed from the Chrome Web Store" [About Google Chrome's "This extension may soon no longer be supported"](https://github.com/uBlockOrigin/uBlock-issues/wiki/About-Google-Chrome%27s-%22This-extension-may-soon-no-longer-be-supported%22) |
| ![Get uBlock Origin for Thunderbird](https://assets.kitploit.com/production/public/readmes/50911/80cc0d8b93d79ff830b04d34b12695884a7dcbe13bae0ded999939c49e6611c0/67cecb5c23ec65310f45e0d59c34ee39082a44354a9a938554e89b29986e7d1f-display-v1.webp) | [Thunderbird Add-ons](https://addons.thunderbird.net/thunderbird/addon/ublock-origin/) | [No longer updated and stuck at 1.49.2.](https://github.com/uBlockOrigin/uBlock-issues/issues/2928) Later versions require "GitHub - Releases". |
| ![Get uBlock Origin through GitHub](https://upload.wikimedia.org/wikipedia/commons/c/c2/GitHub_Invertocat_Logo.svg) | [GitHub - Releases](https://github.com/gorhill/uBlock/releases) | Stable and development versions on Firefox, Chromium MV2, and Thunderbird. Must be placed manually into web browsers; the Chromium and Thunderbird versions usually won't auto-update. |

### Related: ![](https://raw.githubusercontent.com/gorhill/uBlock/master/platform/mv3/extension/img/ublock.svg) [uBlock Origin Lite](https://github.com/uBlockOrigin/uBOL-home)

---

uBlock Origin (uBO) is a CPU and memory-efficient [wide-spectrum content blocker](https://github.com/gorhill/uBlock/wiki/Blocking-mode) for Chromium and Firefox. It blocks ads, trackers, coin miners, popups, annoying anti-blockers, malware sites, etc., by default using [EasyList](https://easylist.to/#easyprivacy), [EasyPrivacy](https://easylist.to/#easyprivacy), [Peter Lowe's Blocklist](https://pgl.yoyo.org/adservers/), [Online Malicious URL Blocklist](https://gitlab.com/malware-filter/urlhaus-filter#malicious-url-blocklist), and uBO [filter lists](https://github.com/uBlockOrigin/uAssets/tree/master/filters). There are many other lists available to block even more. Hosts files are also supported. uBO uses the EasyList filter syntax and [extends](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax#extended-syntax) the syntax to work with custom rules and filters.

You may easily unselect any preselected filter lists if you think uBO blocks too much. For reference, Adblock Plus installs with only EasyList, ABP filters, and Acceptable Ads enabled by default.

It is important to note that using a blocker is **NOT** [theft](https://x.com/LeaVerou/status/518154828166725632). Do not fall for this creepy idea. The *ultimate* logical consequence of `blocking = theft` is the criminalization of the inalienable right to privacy.

Ads, "unintrusive" or not, are just the visible portion of the privacy-invading means entering your browser when you visit most sites. **uBO's primary goal is to help users neutralize these privacy-invading methods** in a way that welcomes those users who do not wish to use more technical means.

---

* [Documentation](#documentation)
* [Installation](#installation)
  + [Firefox](#firefox)
  + [Chromium](#chromium)
  + [Thunderbird](#thunderbird)
  + [All Programs](#all-programs)
  + [Enterprise Deployment](#enterprise-deployment)
* [Release History](#release-history)
* [Translations](#translations)
* [About](#about)

## Documentation

| Basic Mode | Advanced Mode |
| --- | --- |
| The [simple popup user interface](https://github.com/gorhill/uBlock/wiki/Quick-guide%3A-popup-user-interface) for an install-it-and-forget-it type of installation that is configured optimally by default. | The [advanced popup user interface](https://github.com/gorhill/uBlock/wiki/Dynamic-filtering%3A-quick-guide) ...
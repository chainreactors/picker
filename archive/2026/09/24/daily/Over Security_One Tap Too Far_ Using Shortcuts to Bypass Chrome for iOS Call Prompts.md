---
title: One Tap Too Far: Using Shortcuts to Bypass Chrome for iOS Call Prompts
url: https://blog.doyensec.com/2026/09/24/chrome-ios-policy-bypass.html
source: Over Security
date: 2026-09-24
fetch_date: 2026-09-25T06:53:18.196697
---

# One Tap Too Far: Using Shortcuts to Bypass Chrome for iOS Call Prompts

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2026
* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2026 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# One Tap Too Far: Using Shortcuts to Bypass Chrome for iOS Call Prompts

24 Sep 2026 - Posted by Leonardo Giovannini

## TL;DR

While testing deep links in Chrome for iOS, we noticed a small but important difference. Opening a third-party app through a custom URL scheme normally produced a confirmation prompt. Shortcuts were an exception. As theyâre handled by a native Apple app, Chrome allowed `shortcuts://` and its legacy `workflow://` alias to open without showing the same prompt.

At first, this looked like a minor inconsistency. It became more interesting once we looked at Shortcutsâ callback support. A webpage could send the user to Shortcuts and provide a second URL for Shortcuts to open afterwards. That second URL could be `tel:`. Although Chrome protected direct `tel:` navigations with user-interaction checks, it never saw the callback coming from Shortcuts. A single click on a webpage could therefore reach the phone handler without going through Chromeâs normal check for the final URL. This vulnerability was assigned [CVE-2026-13795](https://nvd.nist.gov/vuln/detail/cve-2026-13795).

The fix was to show a prompt before opening any Shortcuts or Workflow URL.

## Background: external schemes and Chromeâs launch policy

Chrome has an app-launch layer between a web navigation and a deep-link redirect. Before handing control to another app, the browser checks whether the navigation came from the user, whether Chrome is in Incognito mode, and whether it needs to show an alert.

In a normal browsing session, a direct link to a third-party custom scheme triggered an app-launch confirmation. The user had to tap again to approve the handoff. Shortcuts did not trigger this prompt. Chrome treated it as a trusted Apple application even though its URL scheme accepts callback parameters that can lead to another app.

Chrome also had explicit handling for `tel:` URLs. A recent user gesture had to exist before the request could be passed on, preventing a page from turning an unrelated navigation into a call request. A direct `tel:` URL went through this code; a `tel:` URL opened later by Shortcuts did not.

Source: [`app_launcher_tab_helper.mm`](https://chromium.googlesource.com/ios-chromium-mirror/%2B/refs/heads/main/ios/chrome/browser/app_launcher/model/app_launcher_tab_helper.mm#132)

```
if (!(is_user_initiated ||
        (url.SchemeIs(url::kTelScheme) && user_tapped_recently))) {
    ShowAppLaunchAlert(AppLauncherAlertCause::kNoUserInteraction, url);
    return;
}
```

The expected path looked like this:

```
web navigation â Chrome app-launch policy â user decision, if required â UIApplication openURL
```

The problem was that Chrome checked the first URL in the chain, while the second URL caused the sensitive action.

## Shortcuts and x-callback-url

The Shortcuts app accepts `shortcuts://` and `workflow://` URLs. Its `run-shortcut` endpoint supports the [x-callback-url convention](https://support.apple.com/guide/shortcuts/use-x-callback-url-apdcd7f20a6f/ios):

* `x-success` specifies a URL to open after successful execution.
* `x-cancel` specifies a URL to open after cancellation.
* `x-error` specifies a URL to open after an error.

These parameters contain actual URLs, not just status labels. When Shortcuts receives a `run-shortcut` request, it reads the query string and keeps the supplied callbacks while the shortcut runs. Once the shortcut finishes, fails, or is cancelled, Shortcuts opens the callback associated with that outcome. The destination does not have to be an `http` or `https` URL; it can be another appâs custom scheme.

For `x-cancel`, the relevant sequence is:

```
Shortcuts receives run-shortcut?x-cancel=<callback>
  â stores <callback> as the cancellation destination
  â starts, or presents, the requested shortcut
  â shortcut execution is cancelled
  â Shortcuts asks iOS to open <callback>
```

This second handoff never returns to Chrome. Shortcuts asks iOS to open the callback directly, so Chrome has no opportunity to apply its `tel:` policy to it.

## The vulnerable callback chain

The following example uses `x-error`. The callback is URL-encoded because it is itself a URL inside the query string:

```
<a href="shortcuts://run-shortcut?name=nonexistent&x-error=tel%3A%2F%2FPHONE_NUMBER">
  Continue
</a>
```

When the deeplink is called, the chain is:

```
1. The victim taps the link in Chrome.
2. Chrome opens shortcuts:// without its app-launch alert.
3. Shortcuts parses x-error and records tel://PHONE_NUMBER as its error callback.
4. The requested shortcut errors, as the shortcut does not exist.
5. Shortcuts processes x-error and opens tel://PHONE_NUMBER.
6. iOS hands the telephone request to its registered handler.
```

Chrome was involved in step 2, but not in step 5. It approved a navigation to an Apple app; the webpage still controlled the `tel:` URL that Shortcuts opened later.

The same behavior applies to all three callbacks.

## Security impact

A webpage could use this behavior to open the URL scheme of an installed app after a single click, without Chrome confirming the final destination.

The clearest example we found was `tel:`. Chrome guarded direct telephone URLs because a webpage should not be able to turn a navigation into a call request without the expected interaction. Routing the URL through Shortcuts skipped that guard. The same technique also worked with `facetime:`. The final behavior depended on iOS, the installed app, and the target URL, but Chrome no longer had control over the last step.

This was an app-launch permission bypass. The visible navigation went to one app, while the webpage supplied a second, potentially action-oriented destination.

[![

Your browser does not support the video tag.
](../../../public/images/chrome-ios-deeplink.png)](../../../public/images/ios-bypass.mp4)

## Remediation

The Chromium fix, [Show alert before opening a shortcuts URL](https://chromium-review.googlesource.com/c/chromium/src/%2B/7838361), moved the check to the first handoff. Chrome now shows an alert before opening any `shortcuts://` or `workflow://` URL.

Prompting at this point avoids having to parse every possible callback. It covers `x-error`, `x-success`, `x-cancel`, nested Shortcuts URLs, and any similar callback behavior added in the future.

The resulting flow is:

```
web navigation â Chrome confirmation for Shortcuts/Workflow â UIApplication opens Shortcuts
```

If the user declines, the callback chain never starts. If the user accepts, the handoff to Shortcuts is explicit.

## References

* [Chromium issue 476591032](https://issues.chromium.org/issues/476591032)
* [Chromium change 7838361](https://chromium-review.googlesource.com/c/chromium/src/%2B/7838361)
* [Apple: Use x-callback-url with Shortcuts](https://support.apple.com/guide/shortcuts/use-x-callback-url-apdcd7f20a6f/ios)
* [CVE-2026-13795](https://nvd.nist.gov/vuln/detail/cve-2026-13795)

### Other relevant posts:

* ### [Preinstalled but Not Safe. OnePlus OEM App Session Takeover Vulnerability 10 Sep 2026](/2026/09/10/oneplus-session-takeover.html)
* ### [Huawei Theme Manager Arbitrary Code Execution 26 Jul 2023](/2023/07/26/huawei-theme-arbitrary-code-exec.html)
* ### [Novel Abuses On Wi-Fi Direct Mobile File Transfers 10 Dec 2020](/2020/12/10/novel-abuses-wifi-direct-mobile-file-transfers.html)
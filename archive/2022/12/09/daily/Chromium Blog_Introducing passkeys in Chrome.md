---
title: Introducing passkeys in Chrome
url: http://blog.chromium.org/2022/12/introducing-passkeys-in-chrome.html
source: Chromium Blog
date: 2022-12-09
fetch_date: 2025-10-04T00:58:38.767102
---

# Introducing passkeys in Chrome

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![Chromium Blog](//1.bp.blogspot.com/-vkF7AFJOwBk/VkQxeAGi1mI/AAAAAAAARYo/57denvsQ8zA/s1600-r/logo_chromium.png)](https://blog.chromium.org/)
[## Chromium Blog](/.)

News and developments from the open source browser project

## [Introducing passkeys in Chrome](https://blog.chromium.org/2022/12/introducing-passkeys-in-chrome.html "Introducing passkeys in Chrome")

Thursday, December 8, 2022

We [announced in October](https://android-developers.googleblog.com/2022/10/bringing-passkeys-to-android-and-chrome.html) that passkey support was available in Chrome Canary. Today, we are pleased to announce that passkey support is now available in Chrome Stable M108.

What are passkeys?

Passwords are typically the first line of defense in our digital lives. However, they are at risk of being phished, leaked in data breaches, and even suffering poor password hygiene. Google has long recognized these issues, which is why we have created defenses like [2-Step Verification](https://myaccount.google.com/signinoptions/two-step-verification/enroll-welcome?pli=1) and [Google Password Manager](http://passwords.google).

To address these security threats in a simpler and more convenient way, we need to move towards passwordless authentication. This is where passkeys come in. Passkeys are a significantly safer replacement for passwords and other phishable authentication factors. They cannot be reused, don't leak in server breaches, and protect users from phishing attacks. Passkeys are built on [industry standards](https://fidoalliance.org/apple-google-and-microsoft-commit-to-expanded-support-for-fido-standard-to-accelerate-availability-of-passwordless-sign-ins/), can work across different operating systems and browser ecosystems, and can be used with both websites and apps.

Using passkeys

You can use passkeys to sign into sites and apps that support them. Signing in with a passkey will require you to authenticate yourself in the same way that you unlock a device.

With the latest version of Chrome, we're [enabling](https://developers.google.com/identity/passkeys/supported-environments) passkeys on Windows 11, macOS, and Android. On Android your passkeys will be [securely synced](https://security.googleblog.com/2022/10/SecurityofPasskeysintheGooglePasswordManager.html) through Google Password Manager or, in future versions of Android, any other password manager that supports passkeys.

![](https://lh4.googleusercontent.com/KGfodMN78yPsLSyHSIhaifkR1aouHVJZUGIf8kmLktRhdBPmd7Ick1LBe7NelX1NmF6rCdyNDvzE2i6mB8qRf4CbYVY3zjX84L4_xu1aUdBzIn1Kzg8OruT7rM4flcu3Rg1BJI3poPVt_AAKDvBzXpcvalXPpDEYbwv_8_6l-S96-p5CD4WLkbYfi_Uf0pU)

Once you have a passkey saved on your device it can show up in autofill when you're signing in to help you be more secure.

![](https://lh4.googleusercontent.com/gvQpTTci8pH7T6U24y3FFu8QCyEyLiVcAfsSQTAggRfxPgLTVJgMagkDBK9XuBnHg1dmuTXhEfCvdpR8oNKFVWrG2xbryBzir5_omQSa4JKoVcZ39O4AMxBfh8h7h8eibVnHQCfHrJuK7mow7ZrNcfLnKN7nhkzPjxdtj0-pFsZed9gU0dlvCCQyEipF2TA)

On a desktop device you can also choose to use a passkey from your nearby mobile device and, since passkeys are built on industry standards, you can use either an Android or iOS device.

![](https://lh4.googleusercontent.com/B8WvaZF5QApI926gpV-sSemO8y3k3OKU1McZjtBZ7A_O2PlQ9tfozPEy5sk8tH5_2sblKwXo3HTPq9gD3oy6mfvyc_Ixx5jwQ-PsB4tOAfGt1zkJ9ywg1kbQdSP5uk1BXZlBVK7CzFaa6BV6WeoJJCa8Sthmv210Y8HKEdrZSovjwXwfvcs0eLYvFKI2PMY)

A passkey doesn't leave your mobile device when signing in like this. Only a securely generated code is exchanged with the site so, unlike a password, there's nothing that could be leaked.

To give you control over your passkeys, from Chrome M108 you will be able to manage your passkeys from within Chrome on Windows and macOS.

![](https://lh3.googleusercontent.com/X4ewdKmOzo3_f9sGv07wYVJtmE4hQB5qLvwOEdmprioAhgTGJYsDDNM0XtXZ0vaagv8ka0UQSYyIXEGiboHG8QIoln-vXA_dgqrDPGCV6v3JwMEvx6eHkOqZp38h7w1Hmj1I-joMk_4VgU9CjUVcqvSkg5Xo540BkB4_Xj7yX08BJZ9amWwHQb6sRroBVFI)

Enabling passkeys

For passkeys to work, developers need to [build passkey support](https://web.dev/passkey-registration/) on their sites using the WebAuthn API. We’ve been working with others in the industry, especially Apple and Microsoft, members within the [FIDO Alliance](https://fidoalliance.org/) and the [W3C](https://www.w3.org/) to drive secure authentication standards [for years](https://blog.google/technology/safety-security/one-step-closer-to-a-passwordless-future/).

Our goal is to keep you as safe as possible on the web and we’re excited for what the passkeys future holds. Enabling passkeys to be used in Chrome is a major milestone, but our work is not done. It will take time for this technology to be widely adopted across sites and we are working on enabling passkeys on iOS and Chrome OS. Passwords will continue to be part of our lives as we make this transition, so we’ll remain dedicated to making conventional sign-ins safer and easier through Google Password Manager.

Posted by Ali Sarraf, Product Manager, Chrome

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

[**](https://blog.chromium.org/)

[**](https://blog.chromium.org/2023/02/do-more-with-chrome-on-single-charge-on.html "Newer Post")

[**](https://blog.chromium.org/2022/09/chrome-107-beta.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [$200K](https://blog.chromium.org/search/label/%24200K)

  1
* [10th birthday](https://blog.chromium.org/search/label/10th%20birthday)

  4
* [abusive ads](https://blog.chromium.org/search/label/abusive%20ads)

  1
* [abusive notifications](https://blog.chromium.org/search/label/abusive%20notifications)

  2
* [accessibility](https://blog.chromium.org/search/label/accessibility)

  3
* [ad blockers](https://blog.chromium.org/search/label/ad%20blockers)

  1
* [ad blocking](https://blog.chromium.org/search/label/ad%20blocking)

  2
* [advanced capabilities](https://blog.chromium.org/search/label/advanced%20capabilities)

  1
* [android](https://blog.chromium.org/search/label/android)

  2
* [anti abuse](https://blog.chromium.org/search/label/anti%20abuse)

  1
* [anti-deception](https://blog.chromium.org/search/label/anti-deception)

  1
* [background periodic sync](https://blog.chromium.org/search/label/background%20periodic%20sync)

  1
* [badging](https://blog.chromium.org/search/label/badging)

  1
* [benchmarks](https://blog.chromium.org/search/label/benchmarks)

  1
* [beta](https://blog.chromium.org/search/label/beta)

  83
* [better ads standards](https://blog.chromium.org/search/label/better%20ads%20standards)

  1
* [billing](https://blog.chromium.org/search/label/billing)

  1
* [birthday](https://blog.chromium.org/search/label/birthday)

  4
* [blink](https://blog.chromium.org/search/label/blink)

  2
* [browser](https://blog.chromium.org/search/label/browser)

  2
* [browser interoperability](https://blog.chromium.org/search/label/browser%20interoperability)

  1
* [bundles](https://blog.chromium.org/search/label/bundles)

  1
* [capabilities](https://blog.chromium.org/search/label/capabilities)

  6
* [capable web](https://blog.chromium.org/search/label/capable%20web)

  1
* [cds](https://blog.chromium.org/search/label/cds)

  1
* [cds18](https://blog.chromium.org/search/label/cds18)

  2
* [cds2018](https://blog.chromium.org/search/label/cds2018)

  1
* [chrome](https://blog.chromium.org/search/label/chrome)

  35
* [chrome 81](https://blog.chromium.org/search/label/chrome%2081)

  1
* [chrome 83](https://blog.chromium.org/search/label/chrome%2083)

  2
* [chrome 84](https://blog.chromium.org/search/label/chrome%2084)

  2
* [chrome ads](https://blog.chromium.org/search/label/chrome%20ads)

  1
* [chro...
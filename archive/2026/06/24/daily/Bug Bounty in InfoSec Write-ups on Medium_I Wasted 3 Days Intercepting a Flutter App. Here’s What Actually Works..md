---
title: I Wasted 3 Days Intercepting a Flutter App. Here’s What Actually Works.
url: https://infosecwriteups.com/i-wasted-3-days-intercepting-a-flutter-app-heres-what-actually-works-d3e9a4816818?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-24
fetch_date: 2026-06-25T06:08:40.014556
---

# I Wasted 3 Days Intercepting a Flutter App. Here’s What Actually Works.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-wasted-3-days-intercepting-a-flutter-app-heres-what-actually-works-d3e9a4816818&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-wasted-3-days-intercepting-a-flutter-app-heres-what-actually-works-d3e9a4816818&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d3e9a4816818---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d3e9a4816818---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Press enter or click to view image in full size

![]()

# I Wasted 3 Days Intercepting a Flutter App. Here’s What Actually Works.

[![Iamarbaz](https://miro.medium.com/v2/resize:fill:64:64/1*hXXbuM5fdx90jRcVmuho8Q.png)](https://medium.com/%40mdarbazpc?source=post_page---byline--d3e9a4816818---------------------------------------)

[Iamarbaz](https://medium.com/%40mdarbazpc?source=post_page---byline--d3e9a4816818---------------------------------------)

7 min read

·

Jun 14, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dd3e9a4816818&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-wasted-3-days-intercepting-a-flutter-app-heres-what-actually-works-d3e9a4816818&source=---header_actions--d3e9a4816818---------------------post_audio_button------------------)

Share

Three days. That’s how long it took me to get Burp Suite seeing traffic from a Flutter app during a security assessment.

I tried everything I knew. Objection. ReFlutter, which actually patches the Flutter binary itself. Custom CA installation. VPN-based interception. Standard Frida SSL bypass scripts from GitHub. Each one either failed silently or gave me the exact same result: app opens, appears to load, shows “no internet.” Not an SSL error. Not a certificate warning. Just “no internet,” like the proxy wasn’t even there.

At some point I stopped trying individual tools and started asking a different question: what is actually happening at each layer, and why is patching one thing not enough? That’s when things started making sense.

What eventually worked wasn’t a new tool or a clever trick. It was running all the right hooks at the same time, covering every SSL validation path the app could be using. I put those together into two scripts. That’s what this post is about.

## Why Flutter Makes This Harder Than It Should Be

Most Android SSL bypass guides assume Java or Kotlin. Flutter is built differently.

Flutter ships its own TLS implementation, BoringSSL, compiled directly into `libflutter.so`. It has nothing to do with Android's certificate trust chain. Installing Burp's CA through Settings, the first thing every guide tells you to do, has zero effect on Flutter's networking. The app just doesn't use that trust store.

That’s the first problem. The second one is subtler. Even if you patch Flutter’s TLS correctly, some apps run a connectivity check through a Java or WebView layer before Flutter even initializes. That check goes through Android’s certificate chain, which on API 24 and above won’t trust user-installed CAs. So the Flutter bypass works, the Flutter layer is satisfied, and the app still shows “no internet” because the Java layer already rejected the connection a few milliseconds earlier.

This is exactly why ReFlutter wasn’t enough. It patches the Flutter binary, full stop. If anything is happening outside Flutter, in Java or WebView, ReFlutter never touches it.

Covering one layer doesn’t work. You have to cover all of them.

## The Scripts

## Script 1: disable-flutter-tls-v1.js

This one handles the Flutter TLS layer.

Flutter’s BoringSSL has a function called `ssl_verify_peer_cert` in handshake.cc that does the actual peer certificate verification. The script finds this function in memory using byte pattern matching. It has patterns for arm64, arm, x64, and x86 across both Android and iOS. Once it finds the function, it replaces the implementation with one that always returns 0, meaning every certificate passes without any check.

```
function hook_ssl_verify_peer_cert(address) {
    Interceptor.replace(address, new NativeCallback((pathPtr, flags) => {
        return 0;
    }, 'int', ['pointer', 'int']));
}
```

There’s a timing problem that causes silent failures on a lot of devices. Frida attaches to the process before `libflutter.so` finishes loading. Pattern matching runs, finds nothing, exits cleanly, and you see no error, but the bypass never actually happened. The script handles this by retrying up to five times with a one-second delay between attempts. Once the library is found, the retry counter resets so the pattern search also gets its full number of attempts.

## Script 2: universal\_bypass.js

This one covers everything in the Java layer, outside Flutter’s Dart runtime.

**X509TrustManager** is Android’s standard interface for certificate validation. The script registers a custom implementation where checkClientTrusted, checkServerTrusted, and getAcceptedIssuers are all empty. No certificate chain ever gets checked.

```
var TrustManager = Java.registerClass({
    name: 'com.burp.bypass.TrustManager',
    implements: [X509TrustManager],
    methods: {
        checkClientTrusted: function(chain, authType) {},
        checkServerTrusted: function(chain, authType) {},
        getAcceptedIssuers: function() { return []; }
    }
});
```

**SSLContext.init()** gets hooked so that every SSL context created anywhere in the app, including inside third-party libraries, gets the bypass trust manager injected into it at initialization time.

**HostnameVerifier** is hooked to return true for every hostname. Some apps validate the server hostname as a completely separate step from certificate validation. Without this, you can pass the certificate check and still get blocked.

**WebViewClient.onReceivedSslError** calls handler.proceed() instead of showing an error page. Without this, any WebView inside the app will just stop loading when Burp intercepts the connection.

**InAppWebViewClient** is the hook that was missing from every existing script I found. Apps using the flutter\_inappwebview plugin register their own WebView client subclass at `com.pichillilorenzo.flutter_inappwebview_android.webview.in_app_webview.InAppWebViewClient`. Hooking the parent WebViewClient class does nothing for this subclass. You have to hook it by its full name specifically.

```
try {
    var InAppWebViewClient = Java.use('com.pichillilorenzo...
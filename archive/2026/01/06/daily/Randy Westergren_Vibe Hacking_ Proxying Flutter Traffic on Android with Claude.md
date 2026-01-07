---
title: Vibe Hacking: Proxying Flutter Traffic on Android with Claude
url: https://randywestergren.com/vibe-hacking-proxying-flutter-traffic-on-android-with-claude/
source: Randy Westergren
date: 2026-01-06
fetch_date: 2026-01-07T03:30:50.210308
---

# Vibe Hacking: Proxying Flutter Traffic on Android with Claude

[![](https://secure.gravatar.com/avatar/693e7027f85b3618717c019f1641d817/?s=120&d=mm)](https://randywestergren.com/ "Randy Westergren")

[![twitter](https://randywestergren.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/32x32/twitter.png "Follow me on Twitter")](https://twitter.com/RandyWestergren "Follow me on Twitter")[![linkedin](https://randywestergren.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/32x32/linkedin.png "Find me on Linkedin")](https://www.linkedin.com/in/randywestergren "Find me on Linkedin")

January 6, 2026January 6, 2026

# Vibe Hacking: Proxying Flutter Traffic on Android with Claude

I’m a regular Cronometer user and as usual, I was interested in exploring the API driving the app – authentication, request patterns, the typical curiosity that drives my posts. When my go-to Android MiTM approach failed, my curiosity only increased and I brought in Claude Opus 4.5 to help troubleshoot. What followed was an interesting collaboration in reverse engineering Flutter’s network stack – and it worked well enough that I wanted to capture both the technical outcome and what AI-assisted mobile security research can actually look like.

## The Challenge

I usually start with a rooted Android emulator running Frida with a mitmproxy system cert installed. Frida scripts help address the common issues in the way of capturing traffic, for example certificate pinning or device root detection. When I started up Cronometer with an [unpinning script](https://codeshare.frida.re/%40akabe1/frida-multiple-unpinning/), mitmproxy logs were mostly empty despite obvious app activity. The app seemed to function fine, unaffected by my attempts to capture its traffic.

I started an OpenCode session with Opus 4.5 and described the situation. It started initial analysis by decompiling the APK and reviewing the source – it quickly found that Cronometer was built with Flutter and pointed me to some helpful background reading. Flutter, I realized, posed some unique challenges to my approach:

1. Flutter doesn’t use the Android TrustManager – It ships with its own SSL/TLS implementation via BoringSSL (Google’s fork of OpenSSL)
2. Flutter isn’t proxy-aware – Even if you set the system proxy, Flutter’s Dart runtime will happily bypass it and connect directly
3. The certificate pinning is baked into `libflutter.so` – There’s no Java/Kotlin layer to hook with traditional Frida scripts

Prior work + the emulator help solve some of these problems:

* [reFlutter](https://github.com/Impact-I/reFlutter) patches the Flutter engine at compile time (requires rebuilding the APK)
* NVISO’s [disable-flutter-tls.js](https://github.com/NVISOsecurity/disable-flutter-tls-verification/blob/main/disable-flutter-tls.js) bypasses SSL pinning via Frida (but doesn’t address proxy routing)
* The Android emulator can force a proxy at the hardware-level, but remains a problem on physical devices – more on this later

## Instrumenting with Frida

### Emulator

Now with a better understanding of the challenges, I provided Claude with access to the rooted emulator via both `adb` and Frida and instructed it to begin hooking the app to capture API traffic. I preferred Frida instrumentation over the reFlutter approach, so I gave NVISO’s disable-flutter-tls.js a try. This unfortunately failed to hook any of the target functions in the libflutter library – the root cause was iterated on by Opus 4.5, summarized below:

Markdown

```
## x86_64 Emulator with ARM64 App (Fails ❌)
1. No Native x86_64 Library: Cronometer's XAPK only ships config.arm64_v8a.apk - no x86/x86_64 native libraries
2. ARM Binary Translation: Android uses libndk_translation.so (5.3MB) to translate ARM64 instructions to x86_64 at runtime
3. Invisible to Frida: The ARM64 libflutter.so is embedded in the APK and executed through the translation layer - it never appears as a loaded module
      Process.findModuleByName("libflutter.so") → null
```

```
## x86_64 Emulator with ARM64 App (Fails ❌)
1. No Native x86_64 Library: Cronometer's XAPK only ships config.arm64_v8a.apk - no x86/x86_64 native libraries
2. ARM Binary Translation: Android uses libndk_translation.so (5.3MB) to translate ARM64 instructions to x86_64 at runtime
3. Invisible to Frida: The ARM64 libflutter.so is embedded in the APK and executed through the translation layer - it never appears as a loaded module
      Process.findModuleByName("libflutter.so") → null
```

As you can see above, Frida’s `Process.findModuleByName("libflutter.so")` returns null, so there’s nothing to scan for SSL bypass patterns in the script. Without the SSL bypass, the app rejects mitmproxy’s certificate during the TLS handshake.

Since I didn’t have the hardware to run an ARM64 emulator, I switched to a physical device.

### Physical Device

Moving over to a rooted Pixel 6, let’s start with detecting `libflutter.so` – Claude crafted a quick script:

Bash

```
$ frida -U -n "Cronometer"
     ____
    / _  |   Frida 17.5.2 - A world-class dynamic instrumentation toolkit
   | (_| |
    > _  |   Commands:
   /_/ |_|       help      -> Displays the help system
   . . . .       object?   -> Display information about 'object'
   . . . .       exit/quit -> Exit
   . . . .
   . . . .   More info at https://frida.re/docs/home/
   . . . .
   . . . .   Connected to Pixel 6 Pro (id=1C121FDEE008KR)

[Pixel 6 Pro::Cronometer ]->
[Pixel 6 Pro::Cronometer ]-> var modules = Process.enumerateModules();
for (var i = 0; i < modules.length; i++) {
    if (modules[i].name === "libflutter.so") {
        console.log("[+] libflutter.so detected!");
        console.log("    Base: " + modules[i].base);
        console.log("    Size: " + modules[i].size);
        console.log("    Path: " + modules[i].path);
    }
}

[+] libflutter.so detected!
    Base: 0x702c105000
    Size: 11313152
    Path: /data/app/~~BhuO8FToqjKy_-agNfm1eg==/com.cronometer.android.gold-Sn9E8JQ_dkZzhPAw6gugUA==/split_config.arm64_v8a.apk!/lib/arm64-v8a/libflutter.so
```

```
$ frida -U -n "Cronometer"
     ____
    / _  |   Frida 17.5.2 - A world-class dynamic instrumentation toolkit
   | (_| |
    > _  |   Commands:
   /_/ |_|       help      -> Displays the help system
   . . . .       object?   -> Display information about 'object'
   . . . .       exit/quit -> Exit
   . . . .
   . . . .   More info at https://frida.re/docs/home/
   . . . .
   . . . .   Connected to Pixel 6 Pro (id=1C121FDEE008KR)

[Pixel 6 Pro::Cronometer ]->
[Pixel 6 Pro::Cronometer ]-> var modules = Process.enumerateModules();
for (var i = 0; i < modules.length; i++) {
    if (modules[i].name === "libflutter.so") {
        console.log("[+] libflutter.so detected!");
        console.log("    Base: " + modules[i].base);
        console.log("    Size: " + modules[i].size);
        console.log("    Path: " + modules[i].path);
    }
}

[+] libflutter.so detected!
    Base: 0x702c105000
    Size: 11313152
    Path: /data/app/~~BhuO8FToqjKy_-agNfm1eg==/com.cronometer.android.gold-Sn9E8JQ_dkZzhPAw6gugUA==/split_config.arm64_v8a.apk!/lib/arm64-v8a/libflutter.so
```

With `libflutter.so` now being detected, let’s try the disable-flutter-tls-verification script:

Bash

```
frida -U -n "Cronometer" -l disable-flutter-tls.js
     ____
    / _  |   Frida 17.5.2 - A world-class dynamic instrumentation toolkit
   | (_| |
    > _  |   Commands:
   /_/ |_|       help      -> Displays the help system
   . . . .       object?   -> Display information about 'object'
   . . . .       exit/quit -> Exit
   . . . .
   . . . .   More info at https://frida.re/docs/home/
   . . . .
   . . . .   Connected to Pixel 6 Pro (id=1C121FDEE008KR)
Attaching...
[+] Pattern version: May 19 2025
[+] Arch: arm64
[+] Platform:  linux
[ ] Locating Flutter library 1/5
[+] Flutter library located
[+] ssl_verify_peer_cert found at offset: 0x706aac
[+] ssl_verify_peer_cert has been patched
[Pixel 6 Pro::Cronometer ]->
```

```
frida -U -n "Cronometer" -l disabl...
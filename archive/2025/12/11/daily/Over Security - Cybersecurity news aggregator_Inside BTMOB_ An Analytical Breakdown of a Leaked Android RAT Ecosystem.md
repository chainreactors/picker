---
title: Inside BTMOB: An Analytical Breakdown of a Leaked Android RAT Ecosystem
url: https://www.d3lab.net/inside-btmob-an-analytical-breakdown-of-a-leaked-android-rat-ecosystem/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-11
fetch_date: 2025-12-12T03:22:46.417820
---

# Inside BTMOB: An Analytical Breakdown of a Leaked Android RAT Ecosystem

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

# Inside BTMOB: An Analytical Breakdown of a Leaked Android RAT Ecosystem

[Malware](https://www.d3lab.net/category/malware/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/12/BTMob_Inside.png?resize=800%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/12/BTMob_Inside.png?fit=800%2C800&ssl=1 "BTMob_Inside")

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/12/BTMob_Inside.png?resize=800%2C800&ssl=1)

During a recent investigation, we obtained access to a multi-package archive containing the complete development toolkit behind the Android malware known as BTMOB RAT. The archive includes the Android payload source code, its dropper, a builder environment, the operator panel for Windows, the command-and-control backend, and all the software dependencies required to deploy the full platform.

Every component is stored inside password-protected ZIP files. While ZIP file headers remain readable without a password, allowing us to inspect the file tree, their binary contents cannot be extracted. We intentionally chose not to acquire or circumvent the passwords, avoiding any action that may financially support or operationally benefit a criminal actor.

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/12/BTMob_Leaked-1.png?resize=282%2C161&ssl=1)

This analysis is therefore built entirely on directory structures, OSINT artefacts, C2 fingerprinting, public research, and behavioural evidence shared in open channels. Even without access to the binaries, the exposed architecture offers a rare, comprehensive look inside a commercial Android RAT platform as used and distributed by a threat actor and their paying customers.

BTMOB appears to be an evolution of SpySolr, itself derived from the Crax RAT lineage. It has been actively marketed inside closed Telegram communities, distributed through phishing websites masquerading as legitimate streaming or financial services, and continually updated with new overlay, injection and remote-control capabilities. The leak analysed in this report provides the first opportunity to examine the internal organisation of this ecosystem.

## Structure of the Leak and Methodology

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/12/BTMob_Archive.png?resize=774%2C691&ssl=1)

The archive contains seven main components: the Android APK source, the dropper, the builder toolkit, the Windows operator console, the full C2 web server, an installation guide, and the complete set of software dependencies. Each component is organised in a separate ZIP file, accompanied by a shortcut referencing the password.

Without the ability to extract the content, the analysis relies on identifying the technologies, development frameworks and operational workflows implied by the directory structures. This approach has proven sufficient to reconstruct the full architecture of the BTMOB platform and the relationships between its components.

## APK.zip – The Full Android Payload Source Code

The structure of APK.zip immediately reveals the presence of a full Android Studio project. The directory includes .idea/, Gradle scripts, Java/Kotlin source files under app/src/main/java, resource folders under app/src/main/res, custom modules such as materiallockview/, and configuration files including AndroidManifest.xml.

These indicators confirm that the leak contains the original developer source code, not a decompiled APK. Names of classes and resources expose the internal design of the RAT: WebView-based injection pages, accessibility service handlers, remote-screen modules, lockscreen pattern components, and configuration assets such as network\_security.xml, pfs1.xml, splits0.xml, and multiple layout files related to fake activities and device-manipulation UIs.

This source tree aligns precisely with public analyses describing BTMOB’s behaviour. The RAT makes extensive use of the Android Accessibility Service to bypass protections, take control of UI interactions, intercept input, simulate gestures, and extract credentials through overlays and injected HTML pages.

## Dropper.zip – The Initial Delivery Stage

The presence of multiple APKs inside Dropper.zip shows the structure of the first-stage application used to deliver the malicious payload. One APK serves as the decoy application—often themed as a streaming service, banking tool or productivity app—while another APK is stored within the assets as the “update”.

Once installed, the dropper displays an update screen and uses Accessibility permissions to silently install the second-stage payload. This confirms the infection chain reported by prior research, where the user is lured into enabling Accessibility, after which the malware grants itself additional permissions automatically.

The dropper therefore acts as the visible entry point for the victim, while concealing the malicious payload embedded within.

## Builder.zip – A Controlled Compilation Environment

Builder.zip contains a collection of well-known tools used in APK manipulation: apktool.jar, APKEditor.jar, signapk.jar, auxiliary JARs and platform-specific scripts. In a traditional malware kit, such a collection would allow an attacker to modify and rebuild the payload fully on their own.

However, the BTMOB ecosystem does not function this way. Evidence from the server-side HTML pages confirms that the actual build process occurs remotely on the threat actor’s infrastructure. The local builder appears to exist primarily as a configuration interface, while the real compilation—where the C2 address, licence, and operator identifier are embedded—happens on the TA-controlled server.

A commented HTML fragment found within the C2 package reveals how passwords, builder updates and download links are provided to paying customers:

```
<!--
<div class="builder-msg-box">
    <p class="builder-msg-text">
        The builder problems have been solved. If you still have issues, please update to the latest version
        and try again.
    </p>
    <div class="builder-password-container">
        <input type="text" readonly id="builder-password-input" value="mySecureFile123" />
        <button class="builder-copy-btn">Copy</button>
    </div>
</div>
-->
```

Another block exposes a hosted RAR archive for a newer version of BTMOB:

```
<input id="manuallink" type="text"
       value="https://www.mediafire.com/file/NO_DISCLOSURE/BTMOB+v3.6.rar/file" readonly>
<span class="hint">Extract Password: <b>T.ME/NO_DISCLOSURE</b></span>
```

These snippets demonstrate that the threat actor distributes new releases through external file-hosting services, embedding download infrastructure directly into the C2 panel.

## BTMOB 3.6.3.zip – The Operator Panel for Windows

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2025/12/BTMob_Binary.png?resize=1030%2C532&ssl=1)

This part of the leak contains the Windows-based operator console, `BTMob.exe`, together with its libraries and UI resources. On execution, the panel prompts for an email, password and a “token”. The token is obtained from the C2 web interface hosted under the /yaarsa/user/ path.

This mechanism acts as the ent...
---
title: MALFEX npm Package 'imgdecode' Hides Shellcode Loader in Windows Native Addon
url: https://thehackernews.com/2026/10/malfex-npm-package-imgdecode-hides.html
source: The Hacker News
date: 2026-10-17
fetch_date: 2026-10-18T06:47:37.779300
---

# MALFEX npm Package 'imgdecode' Hides Shellcode Loader in Windows Native Addon

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [MALFEX npm Package 'imgdecode' Hides Shellcode Loader in Windows Native Addon](https://thehackernews.com/2026/10/malfex-npm-package-imgdecode-hides.html)

**Ravie Lakshmanan**Oct 17, 2026Malware / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8fNb_yEvP6C_CENfQMUx3EDGofY1ejEHusnumTjCLnX3s8pevEbl_cgrtFHhzeEUhyphenhyphenyKe_X41OzQOGL5zlXeLLBnj_ZrLqH1IUag1QWm4QS9V2hgc5ucEzEZKjhstvtde8CFs8anPSZv9w3op67F8Q_MHVC_demESnH8lpAYLLpIRizCyvF5gsi5PDKzm/s1700-nu-rw-lo-l85-e365/npm-dll.jpg)

Cybersecurity researchers have discovered a malicious npm package that's part of a recently disclosed software supply chain attack campaign dubbed **MALFEX**.

The package, named "[imgdecode](https://www.npmjs.com/package/imgdecode?activeTab=versions)," was uploaded to the package registry on September 30, 2026, by a user named "malfexteste8." It has been downloaded [979 times](https://npm-stat.com/charts.html?package=imgdecode) as of writing and is still available on npm as of writing. The latest version of the package is 1.0.3.

"The npm package imgdecode hides a malicious loader in a compiled Node.js addon," SafeDep [said](https://safedep.io/malfex-imgdecode-npm-native-addon-loader/). "Its nine-line JavaScript file loads a Windows dynamic-link library (DLL). When a Node.js program calls require('imgdecode') from a Windows console, the DLL attempts to download encrypted shellcode from GitHub. It decrypts the response and injects the result into a new dllhost.exe process."

First [documented](https://thehackernews.com/2026/10/eight-malicious-npm-packages-downloaded.html) by both Checkmarx and CloudSEK, MALFEX is the name assigned to a long-running campaign in which an unknown threat actor has been publishing malicious packages to npm since August 6, 2023, with an aim to compromise Windows systems. These packages were published across five npm publisher handles: malfexkkj, malfex\_user, malfexteste2, malfexteste3, malfexteste4.

Of the eight identified packages, three were found to act as a loader for Overlord RAT, while three others ("cdn-img-fetch," "img-to-native," and "native-runner") worked together to download and run a Node.js stealer. A third infection pathway involved the use of a postinstall hook to execute JavaScript capable of contacting an external server and retrieving an unspecified next-stage binary.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Interestingly, the threat actor behind the campaign appears to be responding to public disclosures and npm removals by publishing replacements for "native-runner" and "img-to-native" within two days in the form of "runhelper" and "imgbundle." That same day, the first version of "imgdecode" was published. The timeline of events is as follows -

* September 26, 2026 - cdn-img-fetch, img-to-native, and native-runner 1.0.0 published
* September 28, 2026, at 4:06 p.m. UTC - npm removes native-runner and img-to-native
* September 30, 2026, at 3:29 a.m. UTC - imgbundle 1.0.0 published, replacing img-to-native
* September 30, 2026, at 3:37 a.m. UTC - runhelper 1.0.0 published, replacing native-runner
* September 30, 2026, at 4:13 p.m. UTC - runhelper unpublished
* September 30, 2026, at 10:32 p.m. UTC - imgdecode 1.0.0 published
* September 30, 2026, at 11:07 p.m. UTC - imgdecode 1.0.1 published
* October 1, 2026, at 5:48 p.m. UTC - imgdecode 1.0.2 published
* October 7, 2026, at 11:06 p.m. UTC - npm removes imgbundle
* October 8, 2026, at 1:03 p.m. UTC - npm removes cdn-img-fetch
* October 11, 2026, at 10:09 p.m. UTC - imgdecode 1.0.3 published

The Node.js stealer chain is notable for the fact that none of the packages featured an install hook. Instead, the malicious code runs when "native-runner" is loaded. The package lists "img-to-native" as its dependency, which, in turn, has "img-to-native" as a dependency.

The exact functionality of each of these packages is below -

* cdn-img-fetch downloads "banner.png" from a GitHub repository ("cavecrew/proj") and extracts an encrypted blob.
* img-to-native decrypts the blob using the key "malfexteam2027" and writes the contents to disk as a Go executable ("%APPDATA%\Microsoft\Windows\node\_runtime\_helper.exe").
* native-runner executes the Go executable, which then downloads the stealer binary ("setup.exe" aka movinlike) from "104.234.65[.]75:700."

"[Runhelper](https://socket.dev/npm/package/runhelper/files/1.0.0/index.js)," advertised as a helper utility for "launching native binaries from Node.js projects," functions similarly to "native-runner" in that it's designed to run malicious code. Its primary responsibility is to locate a JPG file ("cdn-img-fetch/.runtime/rt.jpg"), extract shellcode from it, copy it into executable memory, and run it using [Koffi](https://koffi.dev/), a Foreign Function Interface (FFI) module for Node.js.

"Six hours after runhelper was unpublished, the operator published imgdecode with a compiled DLL to run the shellcode," SafeDep said. "From version 1.0.1, the DLL also downloads and decrypts the payload. Versions 1.0.1 and 1.0.2 still call require('imgbundle') before loading the DLL. Version 1.0.3 removes that dependency and needs no other MALFEX package."

Like in the case of "runhelper," version 1.0.0 of "[imgdecode](https://socket.dev/npm/package/imgdecode/files/1.0.0/index.js)" waits for "imgbundle" to write a file at the location "cdn-img-fetch/.runtime/" and, once it becomes available, reads its contents into memory, and passes them to a native Node.js addon for decoding the data.

The addon is a 64-bit Microsoft Visual C++ (MSVC) DLL that first checks if it's running in a developer's terminal, and then proceeds to fetch a JPG file ("banner.jpg") from the same repository ("cavecrew/proj"), decrypt the embedded payload using the key "nif-runtime-2027," and ultimately inject the output into "dllhost.exe."

"After decryption, the DLL checks t...
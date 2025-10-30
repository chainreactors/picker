---
title: Unmasking Evasive Threats with apkInspector
url: https://erev0s.com/blog/unmasking-evasive-threats-with-apkinspector/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-29
fetch_date: 2025-10-30T03:12:29.535868
---

# Unmasking Evasive Threats with apkInspector

[erev0s](/)

Toggle navigation

* [Home](/)
* [Blog](/blog)
* [Tools](/tools)
* [Contact](/contact/)

# Unmasking Evasive Threats with apkInspector

apkInspector is a tool designed to provide detailed insights into the zip structure of APK files, offering the capability to extract content and decode the AndroidManifest.xml file.

![Date and Time of last update](data:image/png;base64...)
Sat 18 Nov 2023

* ![android](/media/images/android1.2e16d0ba.fill-24x24.png)
  [`/Android`](/blog/category/android/ "Category")
* ![king.png](/media/images/king.2e16d0ba.fill-24x24.png)
  [`/Featured`](/blog/category/featured/ "Category")

In this article we are going to introduce [apkInspector](https://github.com/erev0s/apkInspector), a tool designed to provide insights about the zip structure and the AndroidManifest even in cases where static analysis evasion techniques are employed. But before diving into the details of apkInspector, it's important to establish its origins and the specific need it addresses.

## [Contents](#contents)

* [Top 3 existing tooling](#top-3-existing-tooling)
* [apkInspector as a CLI](#apkinspector-used-as-cli)
* [apkInspector as a library](#apkinspector-used-as-library)
* [Testing reliability](#apkinspector-to-the-test)
* [Conclusion](#conclusion)

On June 28, 2023, Joe Security [posted](https://twitter.com/joe4security/status/1674042511969468418?s=46&t=8iDWtqgX0z4LwOwqYr8JWA) an analysis on a social media platform. This analysis pertained to a submission made to their tool that could not be thoroughly assessed using ordinary static analysis methods/tools. You can access the specific submission analysis [here](https://www.joesandbox.com/analysis/1344544) (re-uploaded it as it was removed). The Yara rule that is triggered during this analysis has the description 'Yara detected an APK with invalid zip compression'.

Although this behavior is not entirely unprecedented, delving into the intricacies behind it proved to be a particularly intriguing endeavor, revealing a critical gap in existing tools. Remarkably, it became apparent that none of the current tooling seemed to cover the evasion tactics this APK employed. This is where apkInspector steps in, purposefully designed to fill this crucial void.

Without diving into the details of what makes this particular APK unique and why typical static analysis tools stumble, it becomes apparent that it has undergone tampering. This tampering extends beyond merely deviating from the zip specification standard; it also deviates from the expected structure of the AndroidManifest.xml file.

The AndroidManifest.xml file, crucial for Android app configuration, is deliberately structured in a manner contrary to conventional norms. Given that most tools operate based on established specifications, their failure is almost inevitable when faced with such non-compliance.

Of course the only reason this becomes intriguing is because, despite these alterations, Android exhibits the capability to seamlessly install and run the APK without encountering any issues.

## [Top 3 existing tooling](#top-3-existing-tooling)

To provide a comprehensive understanding of apkInspector's functionality and capabilities, the most effective approach is to illustrate its operation through practical examples, contrasting it with other existing tools. So before seeing what apkInspector has to offer, lets see how other known tools behave when attempting to statically analyze this tampered APK.

We will assess each tool by testing two distinct scenarios: first, with the original tampered APK, and second, with a modified APK ("partially fixed" APK hereafter) where only the tampering, specifically related to the ZIP structure, has been rectified.

### [1) apktool](#1-apktool)

[apktool](https://github.com/iBotPeaches/Apktool) needs no introduction as it is one of the standard tooling used most often when attempting to reverse engineer an APK. The following figure shows the error message retrieved by apktool when attempting to decode the original APK:

![bad_compression_method](/media/images/bad_compression_method.max-1200x500.webp)

As can be seen the tool fails with the highlighted error message. The compression method used for one of the files is not among the standard ones.

When using the "partially fixed" APK, as can also be seen in the following figure, the error is different this time as is the cause.

![fixed_zip](/media/images/fixed_zip.max-1200x500.webp)

### [2) Jadx](#2-jadx)

[jadx](https://github.com/skylot/jadx) as one of the best tools when reverse engineering android applications, could not miss from this list. The following figure shows the output error when attempting to load the APK:

![jadx-compr](/media/images/jadx-compr.max-1200x500.webp)

Again we can verify that the error is related to the tampered compression method.

Trying jadx against the "partially fixed" APK yields the following results:

![jadx_fixed](/media/images/jadx_fixed.max-1200x500.webp)

As you can see jadx is now able to load the source code from the decompiled .dex files within the APK, but it is unable to process the AndroidManifest.xml file.

### [3) Androguard](#3-androguard)

Last but not least, [Androguard](https://github.com/androguard/androguard) is the most versatile and comprehensive tool for Android application analysis. When we put it to the test with the APK, here are the results:

![androguard_zip](/media/images/androguard_zip.max-1200x500.webp)

Again, as we the tools shown before, the behavior is the same as is the error.

When trying it against the "partially fixed" APK we have the following:

![androguard_fixed](/media/images/androguard_fixed.max-1200x500.webp)

Now there is no error related to the zip structure but we see a very interesting warning related to the tampering of the AndroidManifest.xml file. Still though Androguard is unable to process the AndroidManifest.xml file properly.

## [apkInspector: Used as CLI](#apkinspector-used-as-cli)

In this section, we will showcase the command-line interface (CLI) version of apkInspector and delve into the array of options it offers in its current version(1.1.6). As our example APK, we will employ the same malicious APK referenced [above](https://www.joesandbox.com/analysis/895672/0/html).

The following snippet shows the help message offered by the tool:

```
$ apkInspector -h
usage: apkInspector [-h] [-apk APK] [-f FILENAME] [-ll] [-lc] [-la] [-e] [-x] [-xa] [-m] [-sm SPECIFY_MANIFEST] [-a] [-v]

apkInspector is a tool designed to provide detailed insights into the zip structure of APK files, offering the capability to extract content and decode the
AndroidManifest.xml file.

options:
  -h, --help            show this help message and exit
  -apk APK              APK to inspect
  -f FILENAME, --filename FILENAME
                        Filename to provide info for
  -ll, --list-local     List all files by name from local headers
  -lc, --list-central   List all files by name from central directory header
  -la, --list-all       List all files from both central directory and local headers
  -e, --export          Export to JSON. What you list from the other flags, will be exported
  -x, --extract         Attempt to extract the file specified by the -f flag
  -xa, --extract-all    Attempt to extract all files detected in the central directory header
  -m, --manifest        Extract and decode the AndroidManifest.xml
  -sm SPECIFY_MANIFEST, --specify-manifest SPECIFY_MANIFEST
                        Pass an encoded AndroidManifest.xml file to be decoded
  -a, --analyze         Check an APK for static analysis evasion techniques
  -v, --version         Retrieves version information
```

The flags `--list-central` and `--list-local` are providing information about the central directory entries and the local header entries respectively. The information retrieved in each case is according the [ZIP specification](https://pkware.cachefly.net/webdocs/APPNOTE/APPNOTE-6.3.9.TXT), and ...
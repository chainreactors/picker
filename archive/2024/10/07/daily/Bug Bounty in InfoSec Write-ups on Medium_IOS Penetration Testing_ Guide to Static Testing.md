---
title: IOS Penetration Testing: Guide to Static Testing
url: https://infosecwriteups.com/ios-penetration-testing-guide-to-static-analysis-4a9dea5d672d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-10-07
fetch_date: 2025-10-06T18:49:44.634292
---

# IOS Penetration Testing: Guide to Static Testing

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4a9dea5d672d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fios-penetration-testing-guide-to-static-analysis-4a9dea5d672d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fios-penetration-testing-guide-to-static-analysis-4a9dea5d672d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4a9dea5d672d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4a9dea5d672d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# IOS Penetration Testing: Guide to Static Testing

[![Aditya Sawant](https://miro.medium.com/v2/resize:fill:64:64/1*tPIw8IKh8vKqtSRVYOtRCA.jpeg)](https://medium.com/%40adityasawant00?source=post_page---byline--4a9dea5d672d---------------------------------------)

[Aditya Sawant](https://medium.com/%40adityasawant00?source=post_page---byline--4a9dea5d672d---------------------------------------)

5 min read

·

Apr 23, 2024

--

Listen

Share

![]()

During an iOS application penetration test, a penetration tester utilizes a range of techniques, tools, and methodologies to evaluate the application’s security posture. One such method is static analysis. Static analysis tools assist in identifying security vulnerabilities in the application’s source code or binary without executing it. This process aids in detecting issues like insecure coding practices, improper utilization of cryptographic functions, the presence of backdoors, hardcoded sensitive information, and more.

## iOS Static Analysis Checklist

> I will demonstrate the test cases of static analysis using an intentionally vulnerable iOS application ([DVIA](https://github.com/prateek147/DVIA-v2)). For this demonstration, I’ll utilize a jailbroken iPhone running iOS 15.7.1, jailbroke using the Palera1n tool, following the instructions outlined in this article <https://ios.cfw.guide/installing-palera1n/#running-palera1n>. Depending on the version of your iPhone, alternative tools such as Checkra1n and Unc0ver can be used for jailbreaking.

### Jailbreak Detection Bypass

Jailbreak detection refers to the process where an application checks whether it’s running on a jailbroken device or not. To access the application, we must bypass this detection. This can be achieved using various packages available in Sileo or Cydia. In this case, I utilized Hestia.

Install hestia -> Settings -> Select Hestia -> Enabled Applications -> Then select your application

Press enter or click to view image in full size

![]()

### SSL Pinning Bypass

SSL pinning is a technique that enhances security by embedding the public key of an SSL/TLS certificate directly into the app or device. This way, when the app or device communicates with the server, it cross-checks the server’s SSL/TLS certificate’s public key with the one hardcoded in the app or device to prevent Man in the middle. For dynamic analysis we must intercept HTTP traffic. This can be achieved by bypassing SSL pinning, you can use tools like SSL Kill Switch 2 which is nothing but package can be downloaded then select *disable certificate validation* or you can use Frida and follow steps mention in this blog <https://github.com/curtishoughton/Penetration-Testing-Cheat-Sheet/blob/master/iOS/iOS-bypass-ssl-pinning.md>.

![]()

### Hardcoded Credentials

The plist file holds vital configuration details for an iOS mobile app, including supported iOS versions and device compatibility. This information is crucial for the operating system to effectively interact with the app. These .plist files could also contain hardcoded credentials.

With below command, you can find the app identifier

```
frida-ps -Ua # To check the identifier
```

Press enter or click to view image in full size

![]()

Now we will use objection to find and read .plist files as follows:

```
objection -g com.highaltitudehacks.DVIAswiftv2 explore
```

Press enter or click to view image in full size

![]()

```
env #To check Location of files in iOS Device
ios plist cat userInfo.plist #To check content of plist files
```

Press enter or click to view image in full size

![]()

To locate all the plist files within an application, you can access a jailbroken iOS device using SSH with the default credentials (root:alpine). Once you have terminal access, run the following command: `find . -type f -name "*.plist"` This command will list all plist files in the current directory.

Press enter or click to view image in full size

![]()

### **Insecure storage** in **keychain**

The iOS keychain is used to securely store sensitive information such as passwords, certificates, keys, and other data. It provides a way for apps to store this information in an encrypted format, ensuring that it is protected from unauthorized access. Apps can access the keychain to retrieve this information when needed, providing a secure storage solution for sensitive data. However, this data can be dumped using various applications. In this case, we will use Objection.

![]()

```
iOS keychain dump
```

Press enter or click to view image in full size

![]()

### Sensitive data in local databases

Applications often use locally stored databases to store information used by the application. These databases might contain sensitive data. We can search for these databases in the local storage of an iOS device using the `find` command.

Press enter or click to view image in full size

![]()

Use SCP to transfer any potentially interesting database file to your local system with `scp <username>@<IP>:<PathToFileonRemote <LocalFileLocation>`. After transferring the file, you can use [SQLite](https://sqlitebrowser.org/dl/) Browser to check if sensitive information is present.

### Binary Cookies

Applications sometimes store sensitive cookies in cookies.binarycookies, which we can view using Objection with `ios cookies get --json`

Press enter or click to view image in full size

![]()

### Cache Data

Application might store sensitive information in a cache like plaintext credentials.

Press enter or click to view image in full size

![]()

### Insecure storage in NSUserDefaults

NSUserDefaults is commonly used to store user preferences and small amounts of data. However, if developers use NSUserDefaults to store sensitive information such as passwords, API keys, or other confidential data without encrypting it, this information can be easily accessed by attackers if they gain access to the device.

```
ios nsuserdefaults get
```

Press ent...
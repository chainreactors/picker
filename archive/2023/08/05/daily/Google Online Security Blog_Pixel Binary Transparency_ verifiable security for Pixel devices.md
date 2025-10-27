---
title: Pixel Binary Transparency: verifiable security for Pixel devices
url: http://security.googleblog.com/2023/08/pixel-binary-transparency-verifiable.html
source: Google Online Security Blog
date: 2023-08-05
fetch_date: 2025-10-04T12:00:50.013396
---

# Pixel Binary Transparency: verifiable security for Pixel devices

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Pixel Binary Transparency: verifiable security for Pixel devices](https://security.googleblog.com/2023/08/pixel-binary-transparency-verifiable.html "Pixel Binary Transparency: verifiable security for Pixel devices")

August 4, 2023

Jay Hou, Software Engineer, *TrustFabric (transparency.dev)*

Pixel Binary Transparency was [originally announced](https://security.googleblog.com/2021/10/pixel-6-setting-new-standard-for-mobile.html) in 2021; the following blog post offers a closer look at how it works.

## Pixel Binary Transparency

With Android powering billions of devices, we’ve [long put security first](https://www.android.com/safety/). There’s the more visible security features you might interact with regularly, like spam and phishing protection, as well as less obvious integrated security features, like daily scans for malware. For example, [Android Verified Boot](https://source.android.com/docs/security/features/verifiedboot) strives to ensure all executed code comes from a trusted source, rather than from an attacker or corruption. And with attacks on software and mobile devices constantly evolving, we’re continually strengthening these features and adding transparency into how Google protects users. This blog post peeks under the hood of [Pixel Binary Transparency](https://developers.google.com/android/binary_transparency/overview), an aspect of Pixel security that puts you in control of checking if your Pixel is running a trusted installation of its operating system.

## Supply Chain Attacks & Binary Transparency

Pixel Binary Transparency responds to a new wave of attacks targeting the software supply chain—that is, attacks on software while in transit to users. These attacks [are on the rise](https://www.sonatype.com/state-of-the-software-supply-chain/introduction) in recent years, likely in part because of the enormous impact they can have. In recent years, tens of thousands of software users from Fortune 500 companies to branches of the US government have been affected by supply chain attacks that targeted the systems that create software to install a backdoor into the code, allowing attackers to access and steal customer data.

One way Google protects against these types of attacks is by auditing Pixel phone  firmware (also called “factory images”) before release, during which the software is thoroughly checked for backdoors. Upon boot, Android Verified Boot runs a check on your device to be sure that it’s still running the audited code that was officially released by Google. Pixel Binary Transparency now expands on that function, allowing you to personally confirm that the image running on your device is the official factory image—meaning that attackers haven’t inserted themselves somewhere in the source code, build process, or release aspects of the software supply chain. Additionally, this means that even if a signing key were compromised, binary transparency would flag the unofficially signed images, deterring attackers by making their compromises more detectable.

## How it works

Pixel Binary Transparency is a [public, cryptographic log](https://developers.google.com/android/binary_transparency/pixel#log_implementation) that records metadata about official factory images. With this log, Pixel users can mathematically prove that their Pixels are running factory images that match what Google released and haven’t been tampered with.

The Pixel Binary Transparency log is cryptographically guaranteed to be append-only, which means entries can be added to the log, but never changed or deleted. Being append-only provides resilience against attacks on Pixel images as attackers know that it’s more difficult to insert malicious code without being caught, since an image that’s been altered will no longer match the metadata Google added to the log. There’s no way to change the information in the log to match the tampered version of the software without detection (Ideally the metadata represents the entirety of the software, but it cannot attest to integrity of the build and release processes.)

For those who want to understand more about how this works, the Pixel Binary Transparency log is append-only thanks to a data structure called a [Merkle tree](https://transparency.dev/verifiable-data-structures/), which is also used in blockchain, Git, Bittorrent, and certain NoSQL databases. The append-only property is derived from the single root hash of the Merkle tree—the top level cryptographic value in the tree. The root hash is computed by hashing each leaf node containing data (for example, metadata that confirms the security of your Pixel’s software), and recursively hashing intermediate nodes.

![](https://lh6.googleusercontent.com/O_3nYyxS4-trOfDTjshMS2C453nafa6IaR0DJgaOwK_HU-NnhBWHdOIEJXgjER3oRyeHlEDyaehg8oAMl0Hzta0Z9s-fxc8bfCIFU5vvdVqog2ZIflwwvm0S6wRhdv-TMBGUKP80XDb06f-5kp9MvnqdppYwaiyHz4pkQ7nw-v7e3S4SpO_sHXYWogXNn5k)

The root hash of a Merkle tree should not change, if and only if, the leaf nodes do not change. By keeping track of the most recent root hash, you also keep track of all the previous leaves. You can read more about the details in the Pixel Binary Transparency [documentation](https://developers.google.com/android/binary_transparency/pixel).

### Merkle Trees Proofs

There are two important computations that can be performed on a Merkle tree: the consistency proof and inclusion proof. These two proofs together allow you to check whether an entry is included in a transparency log and to trust that the log has not been tampered with.

Before you trust the contents of the log, you should use the consistency proof to check the integrity of the append-only property of the tree. The consistency proof is a set of hashes that show when the tree grows, the root hash only changes from the addition of new entries and not because previous entries were modified.

Once you have established that the tree has not been tampered with, you can use the inclusion proof to check whether a particular entry is in the tree. In the case of Pixel Binary Transparency, you can check that a certain version of firmware is published in the log (and thus, an official image released by Google) before trusting it.

You can [learn more about Merkle trees](https://transparency.dev/verifiable-data-structures/) on Google’s [transparency.dev](https://transparency.dev) site, which goes deeper into the same concepts in the context of our Trillian transparency log implementation.

### Try It Out

Most Pixel owners won’t ever need to perform the consistency and inclusion proofs to check their Pixel’s image—Android Verified Boot already has multiple safeguards in place, including verifying the hash of the code and data contents and checking the validity of the cryptographic signature. However, we’ve made the process available to anyone who wants to check themselves—the [Pixel Binary Transparency Log Technical Detail Page](https://developers.google.com/android/binary_transparency/pixel) will walk you through extracting the metadata from your phone and then running the inclusion and consistency proofs to compare against the log.

## More Security to Come

The first iteration of Pixel Binary Transparency lays the groundwork for more security checks. For example, building on Pixel Binary Transparency, it will be possible to make even more security data transparent for users, allowing proactive assurance for a device’s other executed code beyond its factory image. We look forward to building further on Pixel Binary Transparency and continually increasing resilience against software supply chain attacks.

![Share on Twitter](https://www.gstatic.com/images/icons/m...
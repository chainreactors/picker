---
title: DER Entitlements: The (Brief) Return of the Psychic Paper
url: https://googleprojectzero.blogspot.com/2023/01/der-entitlements-brief-return-of.html
source: Project Zero
date: 2023-01-13
fetch_date: 2025-10-04T03:45:00.469500
---

# DER Entitlements: The (Brief) Return of the Psychic Paper

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Thursday, January 12, 2023

### DER Entitlements: The (Brief) Return of the Psychic Paper

Posted by Ivan Fratric, Project Zero

Note: The vulnerability discussed here, CVE-2022-42855, was fixed in iOS 15.7.2 and macOS Monterey 12.6.2. While the vulnerability did not appear to be exploitable on iOS 16 and macOS Ventura, iOS 16.2 and macOS Ventura 13.1 nevertheless shipped hardening changes related to it.

Last year, I spent a lot of time researching the security of applications built on top of [XMPP](https://en.wikipedia.org/wiki/XMPP), an instant messaging protocol based on XML. More specifically, my research focused on how subtle quirks in XML parsing can be used to undermine the security of such applications. (If you are interested in learning more about that research, I did a talk on it at Black Hat USA 2022. The slides and the recording can be found [here](https://www.blackhat.com/us-22/briefings/schedule/index.html#xmpp-stanza-smuggling-or-how-i-hacked-zoom-26618) and [here](https://www.youtube.com/watch?v=ERaRNsvCBrw)).

At some point, when a part of my research was published, people pointed out other examples (unrelated to XMPP) where quirks in XML parsing led to security vulnerabilities. One of those examples was a vulnerability dubbed [Psychic Paper](https://blog.siguza.net/psychicpaper/), a really neat vulnerability in the way Apple operating system checks what entitlements an application has.

Entitlements are one of the core security concepts of Apple’s operating systems. As [Apple’s documentation](https://developer.apple.com/documentation/bundleresources/entitlements?language=objc) explains, “An entitlement is a right or privilege that grants an executable particular capabilities.” For example, an application on an Apple operating system can’t debug another application without possessing proper entitlements, even if those two applications run as the same user. Even applications running as root can’t perform all actions (such as accessing some of the kernel APIs) without appropriate entitlements.

Psychic Paper was a vulnerability in the way entitlements were checked. Entitlements were stored inside the application’s signature blob in the XML format, so naturally the operating system needed to parse those at some point using an XML parser. The problem was that the OS didn’t have a single parser for this, but rather a staggering four parsers that were used in different places in the operating system. One parser was used for the initial check that the application only has permitted entitlements, and a different parser was later used when checking whether the application has an entitlement to perform a specific action.

When giving my talk on XMPP, I gave a challenge to the audience: Find me two different XML parsers that always, for every input, result in the same output. The reason why that is difficult is because XML, although intended to be a simple format, in reality is anything but simple. So it shouldn’t come as a surprise that a way was found for one of Apple's XML parsers to return one set of entitlements and another parser to see a different set of entitlements when parsing the same entitlements blob.

The fix for the Psychic Paper bug: originally, the problem occurred because Apple had four XML parsers in the OS, so, surprisingly, the fix was to add a fifth one.

So, after my XMPP research, when I learned about the Psychic Paper bug, I decided to take a look at these XML parsers and see if I can somehow find another way to trigger the bug even after the fix. After playing with various Apple XML parsers, I had an XML snippet I wanted to try out. However when I actually tried to use it in an application, I discovered that the system for checking entitlements behaved completely differently than I thought. This was because of…

## DER Entitlements

According to [Apple developer documentation](https://developer.apple.com/documentation/xcode/using-the-latest-code-signature-format), “Starting in iOS 15, iPadOS 15, tvOS 15, and watchOS 8, the system checks for a new, more secure signature format that uses Distinguished Encoding Rules, or DER, to embed entitlements into your app’s signature”. As [another Apple article](https://developer.apple.com/documentation/technotes/tn3125-inside-code-signing-provisioning-profiles#The-future-is-DER) boldly proclaims, “The future is DER”.

So, what is DER?

Unlike the previous text-based XML format, [DER](https://en.wikipedia.org/wiki/X.690#DER_encoding) is a binary format, also commonly used in digital certificates. The format is specified in the [X.690 standard](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf).

DER follows relatively simple type-length-data encoding rules. An image from the specification illustrates that:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_ctQx4QBRr-XKiIsWHuUO3d6r1cbG935MHyu2EXDNwm1tWeaGC1A5yniZErHOJ8qqwg185tDe6tU4u8ObWuPf-0CnLI9Pk5QhdQBOKcK6YAzqg30Xz1cuDtkcX9ryZ70vGbk3JKVwwkB0ozGkW6jqEIl-Q7jpeQZTM0PXmGtbsB7g1ApOut3xBwOX/s599/image2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_ctQx4QBRr-XKiIsWHuUO3d6r1cbG935MHyu2EXDNwm1tWeaGC1A5yniZErHOJ8qqwg185tDe6tU4u8ObWuPf-0CnLI9Pk5QhdQBOKcK6YAzqg30Xz1cuDtkcX9ryZ70vGbk3JKVwwkB0ozGkW6jqEIl-Q7jpeQZTM0PXmGtbsB7g1ApOut3xBwOX/s599/image2.png)

The Identifier field encodes the object type, which can be a primitive (e.g. a string or a boolean), but also a constructed type (an object containing other objects, e.g. an array/sequence). The length field encodes the number of bytes in the content. Length can be encoded differently, depending on the length of content (e.g. if content is smaller than 128 bytes, then the length field only takes a single byte). Length field is followed by the content itself. In case of constructed types, the content is also encoded using the same encoding rules.

An [example from Apple developer documentation](https://developer.apple.com/documentation/technotes/tn3125-inside-code-signing-provisioning-profiles#The-future-is-DER) shows what DER-encoded entitlements might look like:

|  |
| --- |
| appl [ 16 ]          INTEGER           :01   cont [ 16 ]           SEQUENCE               UTF8STRING        :application-identifier     UTF8STRING        :SKMME9E2Y8.com.example.apple-samplecode.ProfileExplainer    SEQUENCE               UTF8STRING        :com.apple.developer.team-identifier     UTF8STRING        :SKMME9E2Y8    SEQUENCE               UTF8STRING        :get-task-allow     BOOLEAN           :255    SEQUENCE               UTF8STRING        :keychain-access-groups     SEQUENCE                UTF8STRING        :SKMME9E2Y8.\*      UTF8STRING        :com.apple.token |

Each individual entitlement is a sequence which has two elements: a key and a value, e.g. “get-task-allow”:boolean(true). All entitlements are also a part of a constructed type (denoted as “cont [ 16 ]” in the listing).

DER is meant to have unique binary representation and replacing XML with DER was very likely motivated, at least in part, by preventing issues such as Psychic Paper. But does it necessarily succeed in that goal?

## How entitlements are checked

To understand how entitlements are checked, it is useful to also look at the bigger picture and understand what security/integrity checks Apple operating systems perform on binaries before (and in some cases, while) running them.

Integrity information in Apple binaries is stored in a structure called the [Embedded Signature Blob](https://github.com/apple-oss-distributions/Security/blob/e4ea024c9bbd3bfda30ec6df270bfb4c7438d1a9/OSX/libsecurity_codesigning/lib/sigblob.h#L43). This structure is a container for various other structures that play a role in integrity checking: The digital signature itself, but also entitlements and an important structure called the Code Directory. The Code Directory contains a hash of e...
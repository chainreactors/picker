---
title: SAML Raider Release 2.0.0
url: https://blog.compass-security.com/2024/07/saml-raider-release-2-0-0/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-03
fetch_date: 2025-10-06T17:45:23.517173
---

# SAML Raider Release 2.0.0

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [SAML Raider Release 2.0.0](https://blog.compass-security.com/2024/07/saml-raider-release-2-0-0/ "SAML Raider Release 2.0.0")

[July 2, 2024](https://blog.compass-security.com/2024/07/saml-raider-release-2-0-0/ "SAML Raider Release 2.0.0")
 /
[Tobias Hort-Giess](https://blog.compass-security.com/author/thort/ "Posts by Tobias Hort-Giess")
 /
[0 Comments](https://blog.compass-security.com/2024/07/saml-raider-release-2-0-0/#respond)

SAML Raider [0] is a Burp Suite [1] extension and the tool of choice for many pentesters for testing SAML infrastructures, recommended by many pentesting sites and blog posts. Originally developed by Roland Bischofberger [2] and Emanuel Duss [3] as part of their bachelor thesis, the last version (v1.4.1) was released two years ago. As a former software developer, I wanted to bring my experience to this useful piece of software and give you confirmation that this product is still being maintained. This blog post should give a brief introduction to what has changed in the new version 2.0.0.

## Key Goals of the SAML Raider 2.0.0 Release

* Improving developer experience
* Enhancing user experience
* Addressing some bug fixes

## Improving Developer Experience

### Upgrade to the New Montoya API

In my efforts to keep SAML Raider up to date, I have upgraded to the new Burp Extensions Montoya API [4]. This should make the extension future-proof in case support for the legacy Burp Extender API is dropped.

### Easier Build with Gradle and Integrated Gradle Wrapper

With version 2.0.0, I have streamlined the build process by replacing Maven and incorporating Gradle along with an integrated Gradle wrapper [5]. Using Gradle with the Gradle Wrapper offers several advantages over Maven, particularly in terms of ease of setup and consistency across different development environments. The Gradle Wrapper ensures that a project is built with a specific Gradle version, eliminating the “works on my machine” problem and avoiding issues with version compatibility. This makes onboarding new developers and contributors simpler and more reliable, as they do not need to manually install Gradle.

### New Testing Approach

The Burp Extensions Montoya API only provides interfaces, the concrete implementations are closed source and only available at runtime. This makes writing reliable unit tests a challenge, as you have to mock or fake the implementations. However, mocking or faking implementations means that while the tests may work, they may not truly represent the actual behaviour, as the concrete implementation may differ. To address this problem, a new issue has been opened on PortSwigger’s GitHub repository [6]. Meanwhile, to allow developers to write tests to ensure that changes do not break existing functionality, a new approach has been implemented. This approach allows for semi-automated test execution.

When the extension is loaded in debug mode, a new tab appears in the user interface. In this tab, tests can be executed against the specific implementation with a single click. The results are displayed in a text pane, providing feedback on whether all tests have been successfully passed. While this approach is an improvement over the previous lack of tests against implementations, it is still not optimal. Developers must build and load the extension after each change, resulting in delayed feedback compared to unit testing. In addition, these tests cannot be included in the build process, which would be preferable to avoid releasing breaking changes. Despite these limitations, this new approach represents a significant improvement over the previous situation.

[![](https://blog.compass-security.com/wp-content/uploads/2024/06/Screenshot-from-2024-06-26-09-28-26-1024x807.png)](https://blog.compass-security.com/wp-content/uploads/2024/06/Screenshot-from-2024-06-26-09-28-26.png)

## Enhancing User Experience

In this release, I have focused on improving the overall user experience of the Certificates Tab. By rearranging text fields and controls, users will have a better overview of the displayed information and settings.

[![](https://blog.compass-security.com/wp-content/uploads/2024/06/Screenshot-from-2024-06-26-09-43-25-960x1024.png)](https://blog.compass-security.com/wp-content/uploads/2024/06/Screenshot-from-2024-06-26-09-43-25.png)

## Bug fixes

No software release is complete without addressing existing issues. During the development phase of the new version, some issues could be addressed and fixed.

## Conclusion

The release of SAML Raider 2.0.0 demonstrates our ongoing commitment to maintaining and improving this essential tool. This version introduces improved developer tools, an enhanced user experience, and various bug fixes. We believe these updates will benefit our community. Your support and feedback have been invaluable, so please don’t hesitate to contribute to the project by creating issues or pull requests at <https://github.com/CompassSecurity/SAMLRaider>.

## References

* [0] SAML Raider on GitHub: <https://github.com/CompassSecurity/SAMLRaider>
* [1] Burp Suite: [https://portswigger.net/burp](https://portswigger.net/burp%E2%80%A8)
* [2] Roland Bischofberger on GitHub: <https://github.com/RouLee>
* [3] Emanuel Duss on GitHub: <https://github.com/emanuelduss>
* [4] Burp Extensions Montoya API on GitHub: <https://github.com/PortSwigger/burp-extensions-montoya-api>
* [5] Gradle Wrapper: <https://docs.gradle.org/current/userguide/gradle_wrapper.html>
* [6] How to write tests?: <https://github.com/PortSwigger/burp-extensions-montoya-api/issues/97>

[Authentication](https://blog.compass-security.com/category/authentication/), [Tools](https://blog.compass-security.com/category/tools/), [Web Application](https://blog.compass-security.com/category/webapp/)

[Raider](https://blog.compass-security.com/tag/raider/)[SAML](https://blog.compass-security.com/tag/saml/)[SAML Raider](https://blog.compass-security.com/tag/saml-raider/)[SAMLRaider](https://blog.compass-security.com/tag/samlraider/)[XSLT](https://blog.compass-security.com/tag/xslt/)[XSW](https://blog.compass-security.com/tag/xsw/)[XXE](https://blog.compass-security.com/tag/xxe/)

[##### Previous post

Introducing Conkeyscan – Confluence Keyword Scanner](https://blog.compass-security.com/2024/06/introducing-conkeyscan-confluence-keyword-scanner/ "Previous post: Introducing Conkeyscan – Confluence Keyword  Scanner")
[##### Next post

A Patchdiffing Journey – TP-Link Omada](https://blog.compass-security.com/2024/08/a-patchdiffing-journey-tp-link-omada/ "Next post: A Patchdiffing Journey – TP-Link Omada")

### Leave a Reply [Cancel reply](/2024/07/saml-raider-release-2-0-0/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

### Recent Posts

* [Ensuring NIS2 Compliance: The Importance of Penetration Testing](https://blog.compass-security.com/2025/09/ensuring-nis2-compliance-the-importance-of-penetration-testing/)
* [Collaborator Everywhere v2](https://blog.compass-security.com/2025/09/collaborator-everywhere-v2/)
* [Taming The Three-Headed Dog -Kerberos Deep Dive Series](https://blog.compass-security.com/2025/09/taming-the-three-headed-dog-kerberos-deep-dive-series/)
* [Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases](https://blog.compass-security.com/2025/08/into-the-world-of-passkeys-practical-thoughts-...
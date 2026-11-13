---
title: Digging into HTML to find more elements and event handlers for XSS attacks
url: https://www.hacktivesecurity.com/blog/2026/11/05/digging-into-html-to-find-more-elements-and-event-handlers-for-xss-attacks/
source: Over Security
date: 2026-11-12
fetch_date: 2026-11-13T09:07:26.652798
---

# Digging into HTML to find more elements and event handlers for XSS attacks

* info@hacktivesecurity.com
* Mon - Fri: 9.00 am - 6.00 pm

Advanced Security Solutions to protect the Cyberspace.

[Twitter](https://x.com/hacktivesec)

[Facebook-f](https://www.facebook.com/hacktivesec)

[Linkedin-in](https://www.linkedin.com/company/hacktive-security/)

[Instagram](https://www.instagram.com/hacktivesec/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

Search for:

### Have Any Questions?

+39-06-8773-8747

[free quote](https://www.hacktivesecurity.com/index.php/contacts/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Search for:

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

[![Hacktive Security](https://hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Over 10 years we help companies reach their financial and branding goals. Engitech is a values-driven technology agency dedicated.

#### Gallery

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1.jpg)

#### Contacts

Via Giosuè Carducci, 21 - Pomigliano d'Arco (Italy)
Paseo Montjuic, número 30 - Barcelona (Spain)

info@hacktivesecurity.com

+39 06 8773 8747

[Twitter](#hacktivesec)

Facebook-f

Pinterest-p

Instagram

# Hacktive Blog

* [Home](https://www.hacktivesecurity.com)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Application Security](https://www.hacktivesecurity.com/blog/category/application-security/)
* Digging into HTML to find more elements and event handlers for XSS attacks

[Application Security](https://www.hacktivesecurity.com/blog/category/application-security/)

![](https://www.hacktivesecurity.com/wp-content/uploads/2026/11/illustrazione_comic_wordpress.jpg)

\_ [November 5, 2026](https://www.hacktivesecurity.com/blog/2026/11/05/digging-into-html-to-find-more-elements-and-event-handlers-for-xss-attacks/)\_ [fminetti](https://www.hacktivesecurity.com/blog/author/fminetti/)\_ [0 Comments](https://www.hacktivesecurity.com/blog/2026/11/05/digging-into-html-to-find-more-elements-and-event-handlers-for-xss-attacks/#respond)

### Digging into HTML to find more elements and event handlers for XSS attacks

## Intro

This article aims to illustrate the steps taken during a small-scale research effort to identify new elements and event handlers that can be exploited in XSS attacks.

One of the largest and most widely used repository for XSS payloads is the PortSwigger XSS cheat sheet [[1](https://github.com/PortSwigger/xss-cheatsheet-data)]. This repository contains all the XSS attack payloads available in the associated web application [[2](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)]. It includes a variety of payloads for different types of XSS, prototype pollution sinks, and more.

It is open source, boasts numerous contributors, and serves as a key reference for web application penetration testers.

From time to time, new elements and event handlers emerge and are implemented across various browsers. Consequently, new XSS possibilities come into play, and new WAF rules or signatures must be implemented.

Furthermore, although XSS attacks are a widely discussed topic, new payloads can sometimes be discovered within features that have been implemented for years but have never been tested by anyone.

During this brief period of research, i looked for potential new elements and event handlers to add to the PortSwigger repository. Since the repository is widely used by many experts and is kept very up-to-date, the task did not seem easy from the outset.

Despite the difficulty in finding new things, something did turn up. During this period, 2 HTML elements not mentioned in the repository were discovered (though they do not have any specific event handlers), along with two event handlers that work on mobile versions of Safari.

## Discovery

During an initial research phase, HTML documentation [[3](https://html.spec.whatwg.org/multipage/indices.html)] was consulted to identify HTML elements not included in the cheat sheet, that are capable of executing JavaScript. This review uncovered two HTML elements absent from the repository:

– `fencedframe` (used as a sort of `iframe`)

– `search` (used as a wrapper for forms)

Although the two identified elements could be used with event handlers such as `onclick` or `onmouseover`, the repository maintainers decided not to consider them, given that these event handlers work on all elements.

Finally, while digging through various documentation, i came across a resource [[4](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/Using_HTML5_Audio_Video/ControllingMediaWithJavaScript/ControllingMediaWithJavaScript.html)] concerning two event handlers that only work in Safari mobile:

– `onwebkitbeginfullscreen` (triggered when a video enters full-screen mode)

– `onwebkitendfullscreen` (triggered when a video exits full-screen mode)

The documentation gives this description:

**OS X and iOS behave differently in terms of detecting which HTML elements can be brought full-screen. On iOS, you can take any full-screen video. On OS Although they share the same webkitRequestFullscreen and webkitExitFullscreen methods, the two platforms have different event listeners:**

**OSX: the webkitfullscreenchange event fires when an element enters or exits full-screen mode.**

**iOS: the webkitbeginfullscreen and webkitendfullscreen events fire when a video enters and exits full-screen mode, respectively.**

Surprisingly, no references to these event handlers were found, neither in the Portswigger repository nor in other repositories concerning XSS payloads.

As a proof of concpet i used a simple HTML page with this payload: `<video controls width="640" src="https://interactive-examples.md...
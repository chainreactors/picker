---
title: Google’s Gemini lets strangers send messages from your locked Android phone
url: https://www.bitdefender.com/en-us/blog/hotforsecurity/googles-gemini-strangers-messages-locked-android-phone
source: GRAHAM CLULEY
date: 2026-07-17
fetch_date: 2026-07-18T04:46:41.297746
---

# Google’s Gemini lets strangers send messages from your locked Android phone

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

2 min read

# Google's Gemini lets strangers send messages from your locked Android phone

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=64&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

July 17, 2026

  ![Google's Gemini lets strangers send messages from your locked Android phone](https://blogapp.bitdefender.com/hotforsecurity/content/images/size/w600/2026/07/bypass-android.jpeg "Google's Gemini lets strangers send messages from your locked Android phone")

Gemini, Google's AI assistant, is supposed to make life easier for Android smartphone owners. But right now it may also be making life easier for *anyone* anyone who happens to pick up your phone.

As *The Register* [reports](https://www.theregister.com/security/2026/07/17/google-fixing-android-lock-screen-bug-that-lets-gemini-send-sms-without-a-pin/5273027), Google is working on a fix for a vulnerability that allows an attacker with physical access to a locked Android 16 device to use Gemini to send SMS messages and WhatsApp texts, without ever needing to enter a PIN.

So, imagine the scene. Someone gets hold of your locked Android phone and, despite not knowing your security PIN, they can send messages via SMS or WhatsApp pretending to come from you.

*The Register* says that it has received multiple reports since May of how it is possible to bypass authentication on Android 16 devices that have enabled Gemini access from the lock screen.

In May 2026, a security researcher [published a write-up](https://infosecwriteups.com/android-lock-screen-bypass-via-google-gemini-the-patch-that-wasnt-5509c5c21630) describing how they had reproduced the problem on a fully patched Pixel 6a, using Gemini's Deep Research feature as the entry point.

It is clear that Google has patched Gemini lock screen issues before, but security researchers keep finding new ways through.

The latest vulnerability is different from the previous similar Gemini-based Android lock screen bypass bugs that have been plaguing the operating system [since September 2025](https://payatu.com/blog/android-lock-screen-bypass-through-google-gemini/).

This latest exploit requires a specific multi-touch gesture. When Android devices have revoked Gemini's access to apps like Messages, and someone tries to send an SMS via Gemini on the lock screen, the user is prompted to enter a PIN. However, when "Continue" is pressed simultaneously with Gemini's "Add attachment" button, the device allows the SMS to be sent without any authentication.

An attacker can then enable Gemini's access to other previously disconnected apps. All they have to do is invoke the relevant prompt by - for instance - typing "@WhatsApp" in Gemini's text window. Once again, no PIN is requested or required.

What makes this particularly sneaky is that the changes are not temporary. If a victim later unlocks their phone and checks their Gemini settings, they will find that WhatsApp has been connected to Gemini, even though no PIN was ever entered.

Of course, exploiting a vulnerability like this does require physical access to a vulnerable Android device. This is not an attack which can be carried out by a remote hacker. But, as we all know, it is all too common for a device to be left unattended, or snatched from a bag, or handed to someone you think you can trust.

A spokesperson at Google told *The Register* that this new bug is known about, and that a fix is scheduled to be rolled-out this week. But in the meantime, you would be wise to restrict what Gemini can access from your lock screen.

To do that:

* Open the Gemini app, tap your profile picture, go to Settings, and select "Gemini on lock screen."
* Turn off "Use Gemini without unlocking" entirely, or (if you are not comfortable with that) disable "Make calls and send messages without unlocking."

Google will no doubt patch this particular bug. But the underlying problem is still present. Every new capability Gemini is given at the lock screen is also a new potential attack surface. The more useful your AI assistant becomes without you needing to unlock your phone, the harder it becomes to guarantee that only you can use it.

tags

[Industry News](/en-us/blog/hotforsecurity/tag/industry-news "Industry News")

---

### Author

---

[![Graham CLULEY](https://2.gravatar.com/avatar/5fdc27b8b6f6fd69e77aa017a53cceb5?s=150&d=mm&r=g "Graham CLULEY")](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

[## Graham CLULEY](/en-us/blog/hotforsecurity/author/gcluley "Graham CLULEY")

Graham Cluley is an award-winning security blogger, researcher and public speaker. He has been working in the computer security industry since the early 1990s.

[View all posts](/en-us/blog/hotforsecurity/author/gcluley)

---

## You might also like

#### Bookmarks

---

![loader](https://download.bitdefender.com/resources/themes/draco/images/lite_v2/blog-images/loader-white.svg "loader")

[Legal Information](https://www.bitdefender.com/site/view/legal-terms.html "Legal Information") | [Privacy Policy](https://www.bitdefender.com/site/view/legal-privacy-policy-for-bitdefender-websites.html "Privacy Policy") | [Contact Us](https://www.bitdefender.com/site/Main/contact/1 "Contact Us")

Copyright © 1997 - 2026 Bitdefender.
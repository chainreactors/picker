---
title: Android phones can be hacked just by someone knowing your phone number
url: https://grahamcluley.com/android-phones-can-be-hacked-just-by-someone-knowing-your-phone-number/
source: Graham Cluley
date: 2023-03-18
fetch_date: 2025-10-04T10:00:51.847235
---

# Android phones can be hacked just by someone knowing your phone number

[Skip to content](#content)

[Graham Cluley](https://grahamcluley.com/)

Cybersecurity and AI keynote speaker

[BOOK ME](/about-this-site/public-speaking/ "Book cybersecurity expert Graham Cluley to speak at your event")

[Speaking](/ "Home") · [Writing](/writing/ "Writing") · [Podcasts](/podcasts/ "The AI Fix and Smashing Security podcasts") · [Video](/video/ "Video") · [Contact](/contact/ "Contact Graham Cluley") · [About](/about-this-site/ "About Graham Cluley") · [Games](/misc/ "Games")   [🔍](/search "Search")

⁠This week's sponsor: [Browse privately with a secure VPN that safeguards your privacy. Unblock content worldwide. Get 64% Off Proton VPN.](https://grahamcluley.com/go/protonvpn/)

[ⓘ](/sponsorship/ "Learn more about sponsoring this website")

This article is more than **2 years old**

# Android phones can be hacked just by someone knowing your phone number

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 2:48 pm, March 17, 2023

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2024/11/mastodon-icon-48.png "Mastodon") [@[email protected]](https://mastodon.green/%40gcluley "Follow @gcluley on Mastodon")

![Android phones can be hacked just by someone knowing your phone number](https://grahamcluley.com/wp-content/uploads/2023/03/samsung.jpeg)

Well, this isn’t good.

Google has issued a [warning](https://googleprojectzero.blogspot.com/2023/03/multiple-internet-to-baseband-remote-rce.html "Link to blog by Google Project Zero blog post") that some Android phones can be hacked remotely, without the intended victim having to click on anything.

If an attack is successful, the hacker could access data going through the Samsung Exynos chipsets used in many devices, scooping up call information and text messages.

And what does a hacker need to know about you to target your phone?

Your phone number.

That’s it. All they need to know is your Android device’s phone number.

Frankly, that’s horrific. It’s easy to imagine how such a security problem could be exploited by – oh, I don’t know – state-sponsored hackers.

[**Sign up to our free newsletter**.
Security news, advice, and tips.](/gchq-newsletter/)

In all, security boffins working in Google’s Project Zero team say that they have uncovered a total of 18 zero-day vulnerabilities in some phones’ built-in Exynos modem – with four of the vulnerabilities being particularly severe:

> Tests conducted by Project Zero confirm that those four vulnerabilities allow an attacker to remotely compromise a phone at the baseband level with no user interaction, and require only that the attacker know the victim’s phone number. With limited additional research and development, we believe that skilled attackers would be able to quickly create an operational exploit to compromise affected devices silently and remotely.

According to the researchers, the other vulnerabilities require either a malicious mobile network operator or an attacker with physical access to the Android device.

Vulnerable devices include:

* Samsung smartphones, including those in the S22, M33, M13, M12, A71, A53, A33, A21s, A13, A12 and A04 series;
* Vivo smartphones, including those in the S16, S15, S6, X70, X60 and X30 series;
* Google Pixel 6 and Pixel 7 devices; and
* any vehicles that use the Exynos Auto T5123 chipset.

It’s worth noting that some devices will be using the Qualcomm chipset and modem, which does not suffer from the same vulnerabilities as the one from Exynos.

Of course, Google’s Project Zero vulnerability-hunters have no qualms about going into great detail of how security holes can be exploited, and normally shares such information 90 days publicly after informing relevant software or hardware vendors of the problem.

In this case, however, Google’s team appears to recognise that public disclosure at this stage might actually cause significant problems:

> Under our standard disclosure policy, Project Zero discloses security vulnerabilities to the public a set time after reporting them to a software or hardware vendor. In some rare cases where we have assessed attackers would benefit significantly more than defenders if a vulnerability was disclosed, we have made an exception to our policy and delayed disclosure of that vulnerability.
>
> Due to a very rare combination of level of access these vulnerabilities provide and the speed with which we believe a reliable operational exploit could be crafted, we have decided to make a policy exception to delay disclosure for the four vulnerabilities that allow for Internet-to-baseband remote code execution.

If you have an affected Google Pixel device, there’s good news. Google has already issued a security patch for your smartphone with its [March 2023 security update](https://source.android.com/docs/security/bulletin/pixel/2023-03-01 "Android March 2023 security update").

However, if you’re the owner of a vulnerable Samsung smartphone, fixes still aren’t available according to at least one Google Project Zero researcher.

> End-users still don't have patches 90 days after report…. <https://t.co/dkA9kuzTso>
>
> — Maddie Stone (@maddiestone) [March 16, 2023](https://twitter.com/maddiestone/status/1636469657136959488?ref_src=twsrc%5Etfw)

So what should you do if your device hasn’t been patched?

Google’s recommendation is that you change your device’s settings to switch off Wi-Fi calling and Voice over LTE (VoLTE), until a fix for your smartphone is available.

*Found this article interesting? [Follow Graham Cluley on LinkedIn](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=grahamcluley "Link to @grahamcluley.com on LinkedIn"), [Bluesky](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky"), or [Mastodon](https://mastodon.green/%40gcluley "Link to @gcluley@mastodon.green on Mastodon") to read more of the exclusive content we post.*

---

* [Android](https://grahamcluley.com/category/mobile/android/)
* [Google](https://grahamcluley.com/category/organisations/google/)
* [Privacy](https://grahamcluley.com/category/privacy/)
* [Security threats](https://grahamcluley.com/category/security-threats/)
* [Vulnerability](https://grahamcluley.com/category/security-threats/vulnerability/)

* [#Android](https://grahamcluley.com/tag/android/)
* [#Google](https://grahamcluley.com/tag/google/)
* [#Privacy](https://grahamcluley.com/tag/privacy/)
* [#Samsung](https://grahamcluley.com/tag/samsung/)
* [#vulnerability](https://grahamcluley.com/tag/vulnerability/)

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-64x64.webp)](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley")[**Graham Cluley**](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley")

Graham Cluley is an award-winning [keynote speaker](/about-this-site/public-speaking/) who has given presentations around the world about cybersecurity, hackers, and online privacy. A veteran of the computer security industry since the early 1990s, he wrote the first ever version of Dr Solomon's Anti-Virus Toolkit for Windows, makes regular [media appearances](/about-this-site/media/), and hosts the popular ["The AI Fix"](https://theaifix.show) and ["Smashing Security"](https://www.smashingsecurity.com) podcasts.
Follow him on [LinkedIn](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=grahamcluley), [Bluesky](https://bsky.app/profile/grahamcluley.com) and [Mastodon](https://mastodon.green/%40gcluley), or [drop him an email](/contact).

## You may also like...

* [![How to better protect your Google account with two-...
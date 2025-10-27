---
title: For two years security experts have been secretly decrypting systems for Zeppelin ransomware victims
url: https://grahamcluley.com/for-two-years-security-experts-kept-secret-that-they-were-helping-zeppelin-ransomware-victims-decrypt-their-files/
source: Graham Cluley
date: 2022-11-24
fetch_date: 2025-10-03T23:41:11.164496
---

# For two years security experts have been secretly decrypting systems for Zeppelin ransomware victims

[Skip to content](#content)

[Graham Cluley](https://grahamcluley.com/)

Cybersecurity and AI keynote speaker

[BOOK ME](/about-this-site/public-speaking/ "Book cybersecurity expert Graham Cluley to speak at your event")

[Speaking](/ "Home") · [Writing](/writing/ "Writing") · [Podcasts](/podcasts/ "The AI Fix and Smashing Security podcasts") · [Video](/video/ "Video") · [Contact](/contact/ "Contact Graham Cluley") · [About](/about-this-site/ "About Graham Cluley") · [Games](/misc/ "Games")   [🔍](/search "Search")

⁠This week's sponsor: [Browse privately with a secure VPN that safeguards your privacy. Unblock content worldwide. Get 64% Off Proton VPN.](https://grahamcluley.com/go/protonvpn/)

[ⓘ](/sponsorship/ "Learn more about sponsoring this website")

This article is more than **2 years old**

# For two years security experts have been secretly decrypting systems for Zeppelin ransomware victims

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:11 am, November 23, 2022

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2024/11/mastodon-icon-48.png "Mastodon") [@[email protected]](https://mastodon.green/%40gcluley "Follow @gcluley on Mastodon")

![For two years security experts kept secret that they were helping Zeppelin ransomware victims decrypt their files](https://grahamcluley.com/wp-content/uploads/2022/11/zeppelin.jpeg)

When there’s so much bad news in the world of cybersecurity, it’s always good to share a positive story.

Researchers at cybersecurity firm Unit 221B have revealed that they have been secretly helping victims of the Zeppelin ransomware decrypt their computer systems since 2020.

Victims of the Zeppelin ransomware since its emergence in 2019 have included businesses, critical infrastructure organisations, defence contractors, educational institutions, and the healthcare and medical industries.

[**Sign up to our free newsletter**.
Security news, advice, and tips.](/gchq-newsletter/)

Typically demanding a ransom in the region of US $50,000 (although ransoms of over US $1 million have also been requested), Zeppelin leaves a calling card alongside the files it has encrypted.

![Zeppelin message](https://grahamcluley.com/wp-content/uploads/2022/11/zeppelin-message.jpeg)

> Your company has been hacked! All your files are encrypted, but we understand that you can most likely recover from backups. We have also dumped all of your documents relating to accounting, administration, legal, HR, NDA, SQL, passwords and more! If we don’t come to an agreement, we will be forced to hand over all your files to the media for publicity.

The boffins at Unit 221B turned their attention to the [Zeppelin ransomware](https://www.cisa.gov/uscert/ncas/alerts/aa22-223a "Link to CISA information about Zeppelin ransomware") after it targeted charities, non-profit organisations, and even homeless shelters – all of which clearly have deserving things to direct their money towards than the pockets of extortionists.

Or, as a blog post on Unit 221B’s website eloquently puts it:

> A general Unit 221B rule of thumb around our offices is:
>
> “Don’t [REDACTED] with the homeless or sick! It will simply trigger our ADHD and we will get into that hyper-focus mode that is good if you’re a good guy, but not so great if you are an \*\*\*hole.”

What Unit 22B’s researchers discovered was that Zeppelin’s encryption flow contained a vulnerability, that temporarily left a key in the registry. Full details of how Unit 221B discovered the flaw, and were then able to exploit it to crack keys on victims’ computers, are contained in a [technical blog post](https://blog.unit221b.com/dont-read-this-blog/0xdead-zeppelin "Link to Unit 221b blog post") on the firm’s website.

![Zeppelin keys](https://grahamcluley.com/wp-content/uploads/2022/11/zeppelin-keys.jpeg)

The end result was that the researchers were able to produce a decryption tool that victims could run on infected systems, that would extract a key. The keys would then be uploaded to some significant computing power – 20 servers (each with 40 CPUs on board) donated by Digital Ocean – which would eventually, after six hours huffing and puffing, crack the encryption key.

It’s an impressive achievement, which will have helped organisations that badly needed assistance in the aftermath of a Zeppelin ransomware attack.

And what also impresses me is that the researchers kept their discovery quiet all of this time, knowing that if they bragged about their accomplishment it would only reach the ears of the ransomware gangs using Zeppelin – who would change their approach, and put yet more organisations at even greater risk.

It is only after a significant drop in the number of Zeppelin victims that Unit 221B has chosen to reveal details of its work. The tool continues to be available free of charge, and should still work against even the latest versions of Zeppelin.

The researchers credit the security experts at Cylance for their [prior work analysing Zeppelin](https://blogs.blackberry.com/en/2019/12/zeppelin-russian-ransomware-targets-high-profile-users-in-the-us-and-europe "Link to Cylance research paper"), hosting giant Digital Ocean for providing computer power, and the developers of CADO-NFS for their assistance with the project.

*Found this article interesting? [Follow Graham Cluley on LinkedIn](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=grahamcluley "Link to @grahamcluley.com on LinkedIn"), [Bluesky](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky"), or [Mastodon](https://mastodon.green/%40gcluley "Link to @gcluley@mastodon.green on Mastodon") to read more of the exclusive content we post.*

---

* [Malware](https://grahamcluley.com/category/security-threats/malware/)
* [Ransomware](https://grahamcluley.com/category/security-threats/ransomware-malware/)

* [#decryption keys](https://grahamcluley.com/tag/decryption-keys/)
* [#Malware](https://grahamcluley.com/tag/malware/)
* [#ransomware](https://grahamcluley.com/tag/ransomware/)

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-64x64.webp)](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley")[**Graham Cluley**](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley")

Graham Cluley is an award-winning [keynote speaker](/about-this-site/public-speaking/) who has given presentations around the world about cybersecurity, hackers, and online privacy. A veteran of the computer security industry since the early 1990s, he wrote the first ever version of Dr Solomon's Anti-Virus Toolkit for Windows, makes regular [media appearances](/about-this-site/media/), and hosts the popular ["The AI Fix"](https://theaifix.show) and ["Smashing Security"](https://www.smashingsecurity.com) podcasts.
Follow him on [LinkedIn](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=grahamcluley), [Bluesky](https://bsky.app/profile/grahamcluley.com) and [Mastodon](https://mastodon.green/%40gcluley), or [drop him an email](/contact).

## You may also like...

* [![CryptoLocker: What is it? And how do you protect against it?](https://grahamcluley.com/wp-content/uploads/2013/11/cryptolocker-thumb.png)](https://grahamcluley.com/cryptolocker-protect/ "CryptoLocker: What is it? And how do you protect against it?")

  [CryptoLocker: What is it? And how do you protect against it?](https://grahamcluley.com/cryptolocker-protect/ "CryptoLocker: What is it? And how do you protect against it?")
* [![How you can make over $290 million a week through email scams](https://gr...
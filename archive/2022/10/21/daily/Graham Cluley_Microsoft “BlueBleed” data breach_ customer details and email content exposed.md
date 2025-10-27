---
title: Microsoft “BlueBleed” data breach: customer details and email content exposed
url: https://grahamcluley.com/microsoft-bluebleed-data-breach-customer-details-and-email-content-exposed/
source: Graham Cluley
date: 2022-10-21
fetch_date: 2025-10-03T20:33:09.875956
---

# Microsoft “BlueBleed” data breach: customer details and email content exposed

[Skip to content](#content)

[Graham Cluley](https://grahamcluley.com/)

Cybersecurity and AI keynote speaker

[BOOK ME](/about-this-site/public-speaking/ "Book cybersecurity expert Graham Cluley to speak at your event")

[Speaking](/ "Home") · [Writing](/writing/ "Writing") · [Podcasts](/podcasts/ "The AI Fix and Smashing Security podcasts") · [Video](/video/ "Video") · [Contact](/contact/ "Contact Graham Cluley") · [About](/about-this-site/ "About Graham Cluley") · [Games](/misc/ "Games")   [🔍](/search "Search")

⁠This week's sponsor: [Browse privately with a secure VPN that safeguards your privacy. Unblock content worldwide. Get 64% Off Proton VPN.](https://grahamcluley.com/go/protonvpn/)

[ⓘ](/sponsorship/ "Learn more about sponsoring this website")

This article is more than **2 years old**

# Microsoft “BlueBleed” data breach: customer details and email content exposed

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-70x70.webp)

Graham Cluley](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley") @ 12:35 pm, October 20, 2022

![](/wp-content/uploads/2024/11/bluesky-icon-48-1.png "Bluesky") [@grahamcluley.com](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky")
![](/wp-content/uploads/2024/11/mastodon-icon-48.png "Mastodon") [@[email protected]](https://mastodon.green/%40gcluley "Follow @gcluley on Mastodon")

![Microsoft "BlueBleed" data breach: customer details and email content exposed](https://grahamcluley.com/wp-content/uploads/2022/10/microsoft-data-leak.jpeg)

Microsoft has [admitted](https://msrc-blog.microsoft.com/2022/10/19/investigation-regarding-misconfigured-microsoft-storage-location-2/ "Link to Microsoft blog post") that it accidentally exposed sensitive customer data after failing to configure a server securely.

Cybersecurity firm SOCRadar informed Microsoft about the embarrassing leak in September, which researchers claimed involved files dated from 2017 to August 2022.

The following business transaction data has been exposed:

* names
* email addresses
* email content
* company name
* phone numbers

In addition, Microsoft warned that the exposed data may include “attached files relating to business between a customer and Microsoft or an authorized Microsoft partner.”

SOCRadar [claims](https://socradar.io/sensitive-data-of-65000-entities-in-111-countries-leaked-due-to-a-single-misconfigured-data-bucket/ "Link to SOCRadar") that the sensitive data of over 65,000 entities in 111 countries on a misconfigured Microsoft server that had been left accessible over the internet.

[**Sign up to our free newsletter**.
Security news, advice, and tips.](/gchq-newsletter/)

SOCRadar, which has dubbed the data breach “BlueBleed”, has created a [website](https://socradar.io/labs/bluebleed "Link to BlueBleed") where concerned companies can search to see if their data has been exposed.

![Bluebleed](https://grahamcluley.com/wp-content/uploads/2022/10/bluebleed.jpeg)

Microsoft has not shared any details about the size of the data breach, and while thanking SOCRadar for raising the alarm about the data leak, it has claimed that the researchers had “greatly exaggerated the scope of this issue”:

> Our in-depth investigation and analysis of the data set shows duplicate information, with multiple references to the same emails, projects, and users. We take this issue very seriously and are disappointed that SOCRadar exaggerated the numbers involved in this issue even after we highlighted their error.

The public release of SOCRadar’s BlueBleed search tool seems to have particularly upset Microsoft, saying that it is “not in the best interest of ensuring customer privacy or security and potentially exposing them to unnecessary risk.”

Microsoft argues that any security firm releasing such a tool should put in place basic measures such as verifying users before allowing them to search for data related to their domain.

Microsoft should be rightly embarrassed by its sloppy security, which has needlessly exposed the data of its customers. I suspect that most Microsoft customers will be less bothered with the quibbling over just how much data was carelessly exposed, and more worried that the security cock-up happened in the first place.

According to SOCRadar, Microsoft responded within hours of being notified of the problem, reconfiguring its Azure Blob Storage cloud bucket to properly secure it from unauthorised access.

It’s obviously a positive thing that the misconfigured server has been secured, but it is unfortunately the case that this particular horse has already bolted – for there are reports that Microsoft’s leaky bucket has been [“publicly indexed for months”](https://twitter.com/GossiTheDog/status/1583042989219139590 "Link to tweet from Kevin Beaumont").

*Found this article interesting? [Follow Graham Cluley on LinkedIn](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=grahamcluley "Link to @grahamcluley.com on LinkedIn"), [Bluesky](https://bsky.app/profile/grahamcluley.com "Link to @grahamcluley.com on Bluesky"), or [Mastodon](https://mastodon.green/%40gcluley "Link to @gcluley@mastodon.green on Mastodon") to read more of the exclusive content we post.*

---

* [Data loss](https://grahamcluley.com/category/data-loss/)
* [Microsoft](https://grahamcluley.com/category/organisations/microsoft/)

* [#Azure](https://grahamcluley.com/tag/azure/)
* [#BlueBleed](https://grahamcluley.com/tag/bluebleed/)
* [#data breach](https://grahamcluley.com/tag/data-breach/)
* [#Microsoft](https://grahamcluley.com/tag/microsoft/)

[![Graham Cluley](https://grahamcluley.com/wp-content/uploads/2023/07/cropped-cluley-250-jpeg-64x64.webp)](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley")[**Graham Cluley**](https://grahamcluley.com/author/grahamcluley/ "Link to other articles by Graham Cluley")

Graham Cluley is an award-winning [keynote speaker](/about-this-site/public-speaking/) who has given presentations around the world about cybersecurity, hackers, and online privacy. A veteran of the computer security industry since the early 1990s, he wrote the first ever version of Dr Solomon's Anti-Virus Toolkit for Windows, makes regular [media appearances](/about-this-site/media/), and hosts the popular ["The AI Fix"](https://theaifix.show) and ["Smashing Security"](https://www.smashingsecurity.com) podcasts.
Follow him on [LinkedIn](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=grahamcluley), [Bluesky](https://bsky.app/profile/grahamcluley.com) and [Mastodon](https://mastodon.green/%40gcluley), or [drop him an email](/contact).

## You may also like...

* [![T-Mobile confirms fifth data breach in three years](https://grahamcluley.com/wp-content/uploads/2021/08/t-mobile.jpeg)](https://grahamcluley.com/t-mobile-confirms-fifth-data-breach-in-three-years/ "T-Mobile confirms fifth data breach in three years")

  [T-Mobile confirms fifth data breach in three years](https://grahamcluley.com/t-mobile-confirms-fifth-data-breach-in-three-years/ "T-Mobile confirms fifth data breach in three years")
* [![Up to 350,000 people at risk after Capcom ransomware attack](https://grahamcluley.com/wp-content/uploads/2020/11/capcom.jpeg)](https://grahamcluley.com/up-to-350000-people-at-risk-after-capcom-ransomware-attack/ "Up to 350,000 people at risk after Capcom ransomware attack")

  [Up to 350,000 people at risk after Capcom ransomware attack](https://grahamcluley.com/up-to-350000-people-at-risk-after-capcom-ransomware-attack/ "Up to 350,000 people at risk after Capcom ransomware attack")
* [![Your phone number may not be as private on Facebook as you think – and how to fix it](https://grahamcluley.com/wp-content/uploads/2012/10/fb-730-jpeg.webp)](https://grahamcluley.com/phone-number-privacy-facebook/ "Your phone number may not be as private on...
---
title: Ingannare il riconoscimento facciale
url: https://www.adainese.it/blog/2021/02/04/ingannare-il-riconoscimento-facciale/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-26
fetch_date: 2025-10-02T20:44:10.520903
---

# Ingannare il riconoscimento facciale

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Ingannare il riconoscimento facciale

#### Table of contents

* [Defeating Facial Recognition](#defeating-facial-recognition)
* [The Spread of Personal Photos](#the-spread-of-personal-photos)
* [Face Shield](#face-shield)
* [Key Questions](#key-questions)
* [What Happened Next](#what-happened-next)
* [Conclusions](#conclusions)

#### Latest posts

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/10/01/circular-dependencies-with-ndo/)

[Circular Dependencies with NDO](/blog/2025/10/01/circular-dependencies-with-ndo/)
October 01, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)

[Modifying an object in Strata Cloud Manager](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)
September 28, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)

[From Single-Site to Multi-Site with NDO](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)
September 24, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)

[Retrieving firewall interfaces with Strata Cloud Manager](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)
September 21, 2025

[![Post cover](/images/vendors/eve-ng.webp)](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)

[EVE-NG Linux VM SSH troubleshooting](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)
September 20, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 159 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 123 posts

[![Category cover](/images/categories/ciso.webp)](/categories/ciso)

[CISO](/categories/ciso)
 23 posts

[![Category cover](/images/categories/personal-security.webp)](/categories/personal-security)

[Personal Security](/categories/personal-security)
 22 posts

[![Category cover](/images/categories/security.webp)](/categories/security)

[Security](/categories/security)
 20 posts

[![Category cover](/images/categories/notes.webp)](/categories/notes)

[Notes](/categories/notes)
 19 posts

[![Category cover](/images/categories/infrastructure.webp)](/categories/infrastructure)

[Infrastructure](/categories/infrastructure)
 12 posts

[![Category cover](/images/categories/ot-ics.webp)](/categories/ot-ics)

[OT/ICS](/categories/ot-ics)
 5 posts

[![Category cover](/images/categories/books.webp)](/categories/books)

[Books](/categories/books)
 3 posts

[![Category cover](/images/categories/unetlab.webp)](/categories/unetlab)

[UNetLab](/categories/unetlab)
 3 posts

[![Category cover](/images/categories/writeup.webp)](/categories/writeup)

[Write-up](/categories/writeup)
 3 posts

[![Category cover](/images/categories/osint.webp)](/categories/osint)

[OSInt](/categories/osint)
 2 posts

[![Category cover](/images/categories/life.webp)](/categories/life)

[My life](/categories/life)
 1 posts

## Ingannare il riconoscimento facciale

Andrea Dainese

February 04, 2021

[Personal Security](/categories/personal-security/ "All posts under Personal Security")

[![Post cover](/blog/2021/02/04/ingannare-il-riconoscimento-facciale/faceshield-intense.webp)](/blog/2021/02/04/ingannare-il-riconoscimento-facciale/faceshield-intense.webp)

This article was initially drafted about a year ago, but I never published it. Revisiting it now has allowed me to follow up and confirm my initial concerns.

We know that nearly every photo we take likely passes through facial recognition software. Apple includes one in its Photos app, and both Google and Facebook have their own versions. Images are associated with people and objects, and can later be retrieved via text-based searches.
If you’ve never tried it, take a picture of a car license plate with an iPhone and then search for the word “plate.”

For corporations (Google, Apple, etc.), associating descriptive attributes with each photo—including the names of people involved and geolocation—provides immense value for behavioral analysis.

For government agencies, as
[we have seen](https://www.adainese.it/blog/2021/01/28/monetizing-personal-data-the-new-form-of-prostitution/)
, being able to link a photo (perhaps from a surveillance camera) with a name and surname is extremely valuable.

It is no surprise, therefore, that facial recognition is a subject of significant interest.

## Defeating Facial Recognition

Facial recognition relies on algorithms that learn, given a set of images, how to identify a person across different contexts. The more photos are available, the better the algorithm becomes.

About a year ago,
[Face Shield](https://web.archive.org/web/20200417151230/http%3A//faceshield.ai/ "Face Shield")
publicized an application designed to alter photos so that current facial recognition algorithms would fail to detect the people depicted.

But since these algorithms continuously improve, such a strategy is only effective temporarily: the more popular the app becomes, the faster countermeasures are developed to adapt recognition systems.

## The Spread of Personal Photos

We have already discussed the
[risks of sharing personal data](https://www.adainese.it/blog/2021/01/20/the-dangers-of-unwitting-sharing/)
. Many services have a business model based on collecting massive datasets of personal, profiled information and reselling them.
[Clearview.ai](https://www.adainese.it/blog/2021/01/28/monetizing-personal-data-the-new-form-of-prostitution/)
is a prime example.

The safest recommendation remains: only publish content online that you consciously decide to share—always considering the worst-case scenario if it ends up in the wrong hands.

## Face Shield

Face Shield provided a cloud-based app that altered photos to prevent facial recognition algorithms from identifying the people depicted. The tool offered three levels of obfuscation.

**Original image:**

[![Original image](/blog/2021/02/04/ingannare-il-riconoscimento-facciale/faceshield-before.webp)](/blog/2021/02/04/ingannare-il-riconoscimento-facciale/faceshield-before.webp)

**Subtle effect:** nearly identical to the original but capable of deceiving some recognition software (source: Face Shield website).

[![Face Shield subtle effect](/blog/2021/02/04/ingannare-il-riconoscimento-facciale/faceshield-subtle.webp)](/blog/2021/02/04/ingannare-il-riconoscimento-facciale/faceshield-subtle.webp)

**Medium effect:** visually different from the original, fooling several recognition systems.

[![Face Shield medium effect](/blog/2021/02/04/ingannare-il-riconoscimento-facciale/faceshield-medium.webp)](/blog/2021/02/04/ingannare-il-riconoscimento-facciale/faceshield-medium.webp)

**Intense effect:** unrecognizable to both humans and recognition software.

[![Face Shield intense effect](/blog/2021/02/04/ingannare-il-riconoscimento-facciale/faceshield-intense.webp)](/blog/2021/02/04/ingannare-il-riconoscimento-facciale/faceshield-intense.webp)

## Key Questions

Before using any service, we should start asking the right questions. Face Shield is a perfect example.

**Where is the company based?**

It was headquartered in Canada—outside the EU and therefore beyond the reach of GDPR.

**Is there a privacy policy?**

No. While a privacy policy does not guarantee compliance (as
[discussed here](https://www.adainese.it/blog/2021/01/13/privacy-policy-and-non-existent-free-will/)
), its absence suggests a lack of consideration for user rights.

**What is the business model?**

Every company needs a sustainable business model. In this case, the application was free, with no revenue stream. The only plausible model was data collection and the eventual sale of the company.

**Is the service useful?**

Does ...
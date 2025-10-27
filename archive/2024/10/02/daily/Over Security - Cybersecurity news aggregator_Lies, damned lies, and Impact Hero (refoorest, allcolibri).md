---
title: Lies, damned lies, and Impact Hero (refoorest, allcolibri)
url: https://palant.info/2024/10/01/lies-damned-lies-and-impact-hero-refoorest-allcolibri/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-02
fetch_date: 2025-10-06T18:56:57.126434
---

# Lies, damned lies, and Impact Hero (refoorest, allcolibri)

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Lies, damned lies, and Impact Hero (refoorest, allcolibri)

2024-10-01
 [Security](/categories/security/)/[Privacy](/categories/privacy/)/[Add-Ons](/categories/add-ons/)
 20 mins
 [7 comments](/2024/10/01/lies-damned-lies-and-impact-hero-refoorest-allcolibri/#comments)

*Transparency note*: According to Colibri Hero, they attempted to establish a business relationship with eyeo, a company that I co-founded. I havenât been in an active role at eyeo since 2018, and I left the company entirely in 2021. Colibri Hero was only founded in 2021. My investigation here was prompted by a [blog comment](/2024/07/15/how-insecure-is-avast-secure-browser/#c000004).

Colibri Hero (also known as allcolibri) is a company with a noble mission:

> We want to create a world where organizations can make a positive impact on people and communities.

One of the companyâs products is the refoorest browser extension, promising to make a positive impact on the climate by planting trees. Best of it: this costs users nothing whatsoever. According to the refoorest website:

> Plantation financed by our partners

So the users merely need to have the extension installed, indicating that they want to make a positive impact. And since the concept was so successful, Colibri Hero recently turned it into an SDK called Impact Hero (also known as Impact Bro), so that it could be added to other browser extensions.

What the company carefully avoids mentioning: its 56,000 âpartnersâ arenât actually aware that they are financing tree planting. The refoorest extension and extensions using the Impact Hero SDK automatically open so-called affiliate links in the browser, making certain that the vendor pays them an affiliate commission for whatever purchases the users make. As the extensions do nothing to lead users to a vendorâs offers, this functionality likely counts as [affiliate fraud](https://www.investopedia.com/terms/a/affiliate-fraud.asp).

The refoorest extension also makes very clear promises to its users: planting a tree for each extension installation, two trees for an extension review as well as a tree for each vendor visit. Clearly, this is not actually happening according to the numbers published by Colibri Hero themselves.

What does happen is careless handling of usersâ data despite the â100% Data privacy guaranteedâ promise. In fact, the company didnât even bother to produce a proper privacy policy. There are various shady practices including a general lack of transparency, with the financials never disclosed. As proof of trees being planted the company links to a âcertificateâ which is â¦ surprise! â¦ its own website.

Mind you, Iâm not saying that the company is just pocketing the money it receives via affiliate commissions. Maybe they are really paying Eden Reforestation (not actually called that any more) to plant trees and the numbers they publish are accurate. As a user, this is quite a leap of faith with a company that shows little commitment to facts and transparency however.

#### Contents

* [What is Colibri Hero?](#what-is-colibri-hero)
* [And what about refoorest?](#and-what-about-refoorest)
* [The newcomer: Impact Hero](#the-newcomer-impact-hero)
* [Affected extensions](#affected-extensions)
* [But are they actually planting trees?](#but-are-they-actually-planting-trees)
* [The privacy commitment](#the-privacy-commitment)
* [Happy users](#happy-users)
* [Security issue](#security-issue)
* [Conclusions](#conclusions)

## What is Colibri Hero?

Letâs get our facts straight. First of all, what is Colibri Hero about? To quote their mission statement:

> Because more and more companies are getting involved in social and environmental causes, we have created a SaaS solution that helps brands and organizations bring impactful change to the environment and communities in need, with easy access to data and results. More than that, our technology connects companies and non-profit organizations together to generate real impact.
>
> Our e-solution brings something new to the demand for corporate social responsibility: brands and organizations can now offer their customers and employees the chance to make a tangible impact, for free. An innovative way to create an engaged community that feels empowered and rewarded.

You donât get it? Yes, it took me a while to understand as well.

This is about companiesâ bonus programs. Like: you make a purchase, you get ten points for the companyâs loyalty program. Once you have a few hundred of those points, you can convert them into something tangible: getting some product for free or at a discount.

And Colibri Heroâs offer is: the company can offer people to donate those points, for a good cause. Like planting trees or giving out free meals or removing waste from the oceans. Itâs a win-win situation: people can feel good about themselves, the company saves themselves some effort and Colibri Hero receives money that they can forward to social projects (after collecting their commission of course).

I donât know whether the partners get any proof of money being donated other than the overview on the Colibri Hero website. At least I could not find any independent confirmation of it happening. All photos published by the company are generic and from unrelated events. Except one: there is photographic proof that some notebooks (as in: paper that you write on) have been distributed to girls in Sierra Leone.

Few Colibri Hero partners report the impact of this partnership or even its existence. The numbers are public on Colibri Hero website however if you know where to look for them and who those partners are. And since Colibri Hero left the directory index enabled for their Google Storage bucket, the logos of their partners are public as well.

So while Colibri Hero never published a transparency report themselves, itâs clear that they partnered up with less than 400 companies. Most of these partnerships appear to have never gone beyond a trial, the impact numbers are negligible. And despite Colibri Hero boasting their partnerships with big names like Decathlon and Foot Locker, the corresponding numbers are rather underwhelming for the size of these businesses.

Colibri Hero runs a shop which they donât seem to link anywhere but which gives a rough impression of what they charge their partners. Combined with the public impact numbers (mind you, these have been going since the company was founded in 2021), this impression condenses into revenue numbers far too low to support a company employing six people in France, not counting board members and ethics advisors.

## And what about refoorest?

This is likely where the refoorest extension comes in. While given the companyâs mission statement this browser extension with its less than 100,000 users across all platforms (most of them on Microsoft Edge) sounds like a side hustle, it should actually be the companyâs main source of income.

The extensionâs promise sounds very much like that of the Ecosia search engine: you search the web, we plant trees. Except that with Ecosia you have to use their search engine while refoorest supports any search engine (as well as Linkedin and Twitter/X which they donât mention explicitly). Suppose you are searching for a new pair of pants on Google. One of the search results is Amazon. With refoorest you see this:

![Screenshot of a Google search result pointing to Amazonâs Pants category. Above it an additional link with the text âThis affiliate partner is supporting refoorestâs tree planting effortsâ along with the picture of some trees overlaid with the text â+1â.](/2024/10/01/lies-damned-lies-and-impact-hero-refoorest-allcolibri/refoorest_search.png)

If you click the search result you go to Amazon as usual. Clicking that added link above the search result howev...
---
title: &#x5b;GUEST DIARY&#x5d; Tearing apart website fraud to see how it works., (Wed, May 13th)
url: https://isc.sans.edu/diary/rss/32958
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-13
fetch_date: 2026-05-14T05:47:28.740960
---

# &#x5b;GUEST DIARY&#x5d; Tearing apart website fraud to see how it works., (Wed, May 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jan Kopriva](/handler_list.html#jan-kopriva "Jan Kopriva")

Threat Level: [green](/infocon.html)

* [previous](/diary/32956)
* [next](/diary/32962)

Click [HERE](https://www.sans.org/profiles/mark-baggett) to learn more about classes Mark is teaching for SANS

# [[GUEST DIARY] Tearing apart website fraud to see how it works.](/forums/diary/GUEST%2BDIARY%2BTearing%2Bapart%2Bwebsite%2Bfraud%2Bto%2Bsee%2Bhow%2Bit%2Bworks/32958/)

**Published**: 2026-05-13. **Last Updated**: 2026-05-13 06:29:07 UTC
**by** [Mark Baggett](/handler_list.html#mark-baggett) (Version: 3)

[0 comment(s)](/diary/GUEST%2BDIARY%2BTearing%2Bapart%2Bwebsite%2Bfraud%2Bto%2Bsee%2Bhow%2Bit%2Bworks/32958/#comments)

## [This is a Guest Diary by Joshua Nikolson, an ISC Intern and part of the SANS.edu Bachelor's degree in Applied Cybersecurity (BACS) program.]

##

## Introduction

One day at work, a friend messaged me, “How do you check a website to see if it’s legit?” This friend recently received a phishing text message from a “bank”, and I figured he wanted to be careful and double-check. I told him to put the URL into VirusTotal but said that just because it may say it’s clean, that doesn’t mean it’s not malicious.

He sent me a screenshot of the VirusTotal page for the URL, with no detections and everything showing green. I took a moment to look at it a little more closely. The domain name was unusual, and right off the bat I could see it had been created in the last few months. As of now, it has one detection from a vendor. All domains mentioned in this blogpost will be listed in the Indicators of Compromise section at the end.

![](https://isc.sans.edu/diaryimages/images/1-VTresults.png)

Going to the site, I could immediately tell that something was off about it. It was a secondhand marketplace that seemed to sell just about everything under the sun, with tons of listings in each category and items priced too good to be true. While the site had that “AI vibecoded feeling”, I wanted to give my friend something more concrete other than “don’t trust this site”.

I decided to reverse image search one of the product images, a Lenovo ThinkPad battery replacement, and after some digging, I found an eBay listing with all the same product images and item descriptions. I did this for a few more of the site’s listings and came to the same result. I let my friend know, and he said, “Yeah, it looked too good to be true”.

![](https://isc.sans.edu/diaryimages/images/2-realbatterylisting.png)

## Finding a Marketplace

I found this interesting and wanted to see if I could find something similar again. Today, it is trivial to use AI to mass-deploy these scams, and I wanted to see what would happen if I tried to buy something.

Let’s look up what my friend was originally looking for: a Texas Instruments TI-nSpire CAS calculator. Simply searching on Google and going to the second page, something pops out to me. Why is a driving school selling a calculator?

![](https://isc.sans.edu/diaryimages/images/3-ticalcsearch.png)

The search result link, hxxps://desidrivingschool[.]com/listing/164903741/ redirects to a marketplace where it is for sale:

![](https://isc.sans.edu/diaryimages/images/4-calconsite.png)

This domain looks suspicious on its own, and to add insult to injury, it was registered ~12 days ago on April 3rd, 2026:

![](https://isc.sans.edu/diaryimages/images/5-domaininfo.png)

## What's happening here?

You may be asking why this Desi Driving School is showing up in the search results for this calculator? Good question. If you append “/sitemap.xml” to the URL, you can see tons of these listings that are meant to infiltrate the search results. This is a prime example of SEO poisoning, in which potential victims are lured through their shopping searches to these fake marketplaces.

Threat actors have previously used compromised WordPress sites as command-and-control infrastructure or to stage payloads, but this is being used as a distinct attack vector. Unfortunately, this website was likely compromised, whether through something like a malicious WordPress plugin or stolen credentials, and is now being used to drive traffic to this malicious marketplace:

![](https://isc.sans.edu/diaryimages/images/6-sitemapxml.png)

You can see the range of products that this site offers. They must have a good distribution network.

![](https://isc.sans.edu/diaryimages/images/7-marketplacehome.png)

While reverse-image searching for images of the calculator, I found another similar posting on a different fake marketplace. Same images, same description and title, same exact setup with a redirect…

![](https://isc.sans.edu/diaryimages/images/8-searchresults.png)

![](https://isc.sans.edu/diaryimages/images/9-calcondifferentsite.png)

And another… with what looks like loads of other compromised sites being used.

![](https://isc.sans.edu/diaryimages/images/10-anothersearchresult.png)

![](https://isc.sans.edu/diaryimages/images/11-anothermarketplace.png)

You can endlessly find these sites by searching any description of a product listed with quotes in Google to find the real item that is being sold and copied from, such as this blazer:

![](https://isc.sans.edu/diaryimages/images/12-blazer.png)

If the price was higher than the actual listing, you might think the scheme is just scraping listings, posting them at a higher price, then purchasing the cheaper item and shipping it. However, I do not think that is the case. Let’s try to buy this Eddie Bauer blazer with a fake identity and a fake debit card from Privacy.com and see what happens.

Right away, I can tell this checkout page is a replica of the Shopify checkout page and looks almost identical.

![](https://isc.sans.edu/diaryimages/images/13-firstcheckout.png)

Choosing Mastercard, we’ll check out and pay now. Let’s prepare my fake card. Creating a temporary debit card with a $5 spending limit is extremely easy with Privacy.com, and I have my Mastercard ready.

![](https://isc.sans.edu/diaryimages/images/14-privacycard.png)

First, I am instructed to enter my card here:

![](https://isc.sans.edu/diaryimages/images/15-payment1.png)

Then I get redirected to this page and must enter my information again:

![](https://isc.sans.edu/diaryimages/images/16-payment2.png)

After hitting pay now, a loading screen with a different URL is shown that reminds me of the PayPal loading screen:

![](https://isc.sans.edu/diaryimages/images/17-payment3.png)

And then I am redirected to a thank-you page for my order, despite the card being declined, which they know because it shows failure\_code=failed in the URL.

![](https://isc.sans.edu/diaryimages/images/18-ordersubmit.png)

Only one declined charge was seen on my card. However, in other testing instances, I have seen an additional charge at a different price than the “advertised product”.

![](https://isc.sans.edu/diaryimages/images/19-cardcharges1.png)

The above screenshot is from the order we just made, and this next screenshot is from a different test where two charges were attempted right away on order:

![](https://isc.sans.edu/diaryimages/images/20-cardcharges2.png)

It seems that shirleymcgrady is another similar site, but probably used as the main checkout for the other smaller sites.

![](https://isc.sans.edu/diaryimages/images/21-shirleysite.png)

The loading page domain from the payment was also created recently, 1 month ago, with one detection on VirusTotal.

![](https://isc.sans.edu/diaryimages/images/22-loadingpageVT.png)

## Aftermath

A few days after I tried to check out, multiple other charges were attempted on the card:

![](https://isc.sans.edu/diaryimages/images/23-additionalcharges.jpg)

The clear objective of the scam here is to have the victim make a payment for an item that will never be shipped, resulting in their personal and payment information being stolen. I can only imagine how many peop...
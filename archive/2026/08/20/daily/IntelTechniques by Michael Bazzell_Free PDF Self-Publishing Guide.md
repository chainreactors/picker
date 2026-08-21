---
title: Free PDF Self-Publishing Guide
url: https://inteltechniques.com/publishing.html
source: IntelTechniques by Michael Bazzell
date: 2026-08-20
fetch_date: 2026-08-21T03:04:52.056254
---

# Free PDF Self-Publishing Guide

[# IntelTechniques](index.html)

* [Training](training.html)
* [Services](services.html)
* [Resources](links.html)
* [Tools](tools/index.html)
* [Blog](blog/)
[Magazine](https://unredactedmagazine.com)
* [Books](books.html)
* [Contact](contact.html)

#### PDF Self-Publishing Guide

---

In 2020, I published a book called [This Book Was Self-Published](book8.html). I wanted to share my experiences self-publishing several books, and it also served as my own documentation of the steps I had taken up to that point. It included a chapter on digital publishing focused on the Amazon Kindle platform, but in 2023, I expanded that section to include native PDF publishing. At that time, I had chosen a service called SendOwl for PDF distribution, which worked well for several years. They offered a fair price, but more importantly they offered the option for us to send unlimited free updates to customers who had purchased digital books. This worked great for two years, but then it all collapsed.

In 2025, SendOwl notified us that they would no longer allow us to send out free updates to customers, and they were increasing our prices ten-fold (plus fees for all download bandwidth). This is not an exaggeration; you can read the public outrage at <https://www.trustpilot.com/review/www.sendowl.com>. All legacy accounts would be switched to their new limited platform, which was unsustainable for us. Fortunately, we found a new service called [Payhip (https://payhip.com/?fp\_ref=michael76)](https://payhip.com/?fp_ref=michael76). I recently updated the section of the book about PDF distribution in order to reflect these changes and the purpose of this guide is three-fold. First, it is to share our experiences with Payhip after a year of their services, which may encourage readers to launch their own self-published project. Second, those who may have purchased older print or PDF versions of the book can have this updated content for free. Finally, it serves as a warning to stay away from SendOwl, a service we had previously recommended.

[Payhip](https://payhip.com/?fp_ref=michael76) is now my preferred digital book purchase and delivery service. It is the most affordable option with the most robust features for our use. It also puts the most money in your pocket from sales. If you legitimately purchased any PDF from us over the past year, you purchased through Payhip.
Payhip is not a completely free service. At the time of this writing, the "free" tier had no monthly fee, but Payhip takes 5% of every sale. On top of that, you will pay a 2.9% credit card transaction fee on every purchase. The next tier is $29 per month plus a 2% fee per sale and the "Pro" tier is $99 per month with no fee per sale. All paid tiers still pay the 2.9% credit card transaction fee.

This is where you must consider your predicted sales. While the cheaper (or free) monthly fee may seem like a better deal, those 5% and 2% fees may be more than moving to a different tier. Let's do the math. Assume you will sell 100 books per month at $20 per book. The following outlines the three basic tiers.

$0 (Monthly) + $100 (5% of sales) = $100 (Payhip Fee)
$29 (Monthly) + $40 (2% of sales) = $69 (Payhip Fee)
$99 (Monthly) + $0 (0% of sales) = $99 (Payhip Fee)

In that scenario, the middle plan is best. Let's assume you will sell 500 books monthly.

$0 (Monthly) + $500 (5% of sales) = $500 (Payhip Fee)
$29 (Monthly) + $200 (2% of sales) = $229 (Payhip Fee)
$99 (Monthly) + $0 (0% of sales) = $99 (Payhip Fee)

In that scenario, the "Pro" plan is best financially. This can be confusing since we never know how many books we will sell. I recommend testing with the free plan. If your sales are too much to justify this plan, you can always raise the tier before the monthly fee kicks in. In fact, you can switch tiers in either direction at any time. Always pay attention to the math for your own sales. As I write this, the "Pro" plan is ideal for my sales.

Once you have established an account with Payhip, the following explains the process to sell your book.

• Click "Products" in the menu then "Add new product".
• Select the "Digital Product" or "e-book" option.
• Provide the title of your book and the price.
• Click the "Upload product file" link and select your book PDF.
• Click the "Upload a product image" link and select your book cover image.
• Provide a description of your book and choose your desired visibility.
• Click "Add Product".

You can now click on "Products" in the menu and see your book. However, it is not available for purchase just yet. You must connect some type of payment processor in order to accept credit cards and deliver your product. I prefer Stripe for this, but PayPal is simpler. You will need to create an account at Stripe or PayPal, and then connect the account within Payhip by navigating to "Account" > "Settings" > "Payment Details". Select the appropriate option and follow the steps to associate the account. Once this is complete, you are ready to sell your book.

Return to "Products" and click the "Share/Embed" button next to your item. This presents several options. I no longer prefer to only sell through my website code, so I focus on the "Share" option. It presents the following URL for this book.

<https://payhip.com/b/k5Zuy>

I can now link to this URL on my site and forward people to purchase directly through the Payhip site. I do this for a few reasons. First, by purchasing through Payhip instead of my site, readers can place multiple items from my Payhip store into a "cart" and checkout later. If I had embedded code onto my own site, that could fail. Additionally, it does not require me to store any cookies from users on my site. Finally, purchasing with a credit card on Payhip's site is likely to work better than embedding code or an iFrame on my own site. I do not want to create any purchasing friction. The most likely way to complete the sale without Stripe being fussy about the purchase is on Payhip's site. The following displays the purchase and checkout pages.

![](blog/images/tb01.png)

The customer can provide any name, email and credit card information, then pay for the purchase. Payhip will immediately present the customer with a download link within their browser, and also email them a receipt with additional copy of the link. This all happens without any input from you.

![](blog/images/tb02.png)

Notice that it requests a country and state with zip code. This is for state sales taxes. Payhip will collect and distribute the taxes on your behalf. Some states require it while other do not. The tax rate varies between states. If a state is not selected, the tax will be based on the IP address of the reader. Again, these are all details I want done on Payhip's site and not mine. I highly recommend that you test all of these settings several times before sharing the purchase option publicly.

Regardless of how you facilitate sales, Payhip hosts your PDF on their servers and delivers the product without your input. However, we are far from pushing PDFs into people's inboxes. There are many additional options to configure in "Account" > "Settings > "Advanced Settings".

Protect your PDF files: With this option, the PDF is watermarked with the purchaser’s email address in small letters in the top left every page of the document. If I find a pirated copy of a book floating around the internet, I can look for this data and learn more about the culprit. I can also disable updates and downloads for that reader if desired. This eliminates SOME risk of the buyer pirating the PDF to the world. However, there are problems with this. The watermarks can be removed. Anyone who plans to upload your content to book piracy websites will know how to remove any evidence of the purchase.

Download Limit: The default download attempts of a purchased book are five. I find this to be acceptable. That should be plenty of attempts for someone to download their book. If they still have trou...
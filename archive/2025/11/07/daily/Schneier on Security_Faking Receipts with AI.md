---
title: Faking Receipts with AI
url: https://www.schneier.com/blog/archives/2025/11/faking-receipts-with-ai.html
source: Schneier on Security
date: 2025-11-07
fetch_date: 2025-11-08T03:06:18.169441
---

# Faking Receipts with AI

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Faking Receipts with AI

Over the past few decades, it’s become easier and easier to create fake receipts. Decades ago, it required special paper and printers—I remember a company in the UK advertising its services to people trying to cover up their affairs. Then, receipts became computerized, and faking them required some artistic skills to make the page look realistic.

Now, AI can [do it all](https://arstechnica.com/ai/2025/10/ai-generated-receipts-make-submitting-fake-expenses-easier/):

> Several receipts shown to the FT by expense management platforms demonstrated the realistic nature of the images, which included wrinkles in paper, detailed itemization that matched real-life menus, and signatures.
>
> […]
>
> The rise in these more realistic copies has led companies to turn to AI to help detect fake receipts, as most are too convincing to be found by human reviewers.
>
> The software works by scanning receipts to check the metadata of the image to discover whether an AI platform created it. However, this can be easily removed by users taking a photo or a screenshot of the picture.
>
> To combat this, it also considers other contextual information by examining details such as repetition in server names and times and broader information about the employee’s trip.

Yet another AI-powered security arms race.

Tags: [AI](https://www.schneier.com/tag/ai/), [forgery](https://www.schneier.com/tag/forgery/), [fraud](https://www.schneier.com/tag/fraud/)

[Posted on November 7, 2025 at 7:01 AM](https://www.schneier.com/blog/archives/2025/11/faking-receipts-with-ai.html) •
[6 Comments](https://www.schneier.com/blog/archives/2025/11/faking-receipts-with-ai.html#comments)

### Comments

Doug •
[November 7, 2025 8:54 AM](https://www.schneier.com/blog/archives/2025/11/faking-receipts-with-ai.html/#comment-449686)

A subset of people who file expense reports will always find ways to game the system. Always.

Bilateralrope •
[November 7, 2025 11:13 AM](https://www.schneier.com/blog/archives/2025/11/faking-receipts-with-ai.html/#comment-449689)

@Brad Joehn

How well does that work for receipts from contractors or vendors ?

Jay Libove •
[November 7, 2025 12:36 PM](https://www.schneier.com/blog/archives/2025/11/faking-receipts-with-ai.html/#comment-449694)

In (at least some) European countries, receipts are cryptographically signed, making it trivial to detect fakes.

Clive Robinson •
[November 7, 2025 12:47 PM](https://www.schneier.com/blog/archives/2025/11/faking-receipts-with-ai.html/#comment-449696)

@ ALL,

Legally false expense claims are “fraud” and “conspiracy” crimes.

It’s seriously not worth it.

For many years I got a “Per Day” allowance with no receipts required.

Thus you could chose to spend it on eating food in restaurant and facing a loss or do as I did, pop into a super market and “buy the makings” for several days and effectively pocket the excess.

This made it fairly easy on a US trip to buy a load of “wooden railway” toys[1] for my son as they were about 1/3rd the price in the US that they were in the UK.

Always kept the receipts and went through the customs red channel just in case. Back then you were allowed around $350 “duty free” on gifts, so I never had to pay though it got close.

The point is too many people are “self entitled” and that’s really what this is fundamentally, a “Battle between the self entitled”

In an organisation…

Increasing this type of in organisation Battle will be fought almost entirely by AI even though it will get about 1/3 of it’s output in error and cost way more than it will save.

But who cares about the cost or reliability when “Machismo Swagger” is on the line to see which Is “Top Dog” or has the “Biggest Cojones of Brass or Steel”…

If they were real dogs we’d send them for neutering for antisocial or aggressive behaviour

Any Vets wanting to do the City of London?

[1] We still have all the wooden railway in tightly packed large wheeled plastic tubs, and all but one piece looks near “shop new” even though my son would play with it for hours almost every day filling the entire available floor area of a large double lounge (~600 sqft). With NASA and similar Aerospace and Science videos playing on the DVD in the background (his choice and he was quite adept with the DVD whilst still a toddler. Looking up it’s value for “insurance purposes” might make your eyes self peel 😉

[Brad Koehn, Trusted Signatures](https://trusted-signatures.com) •
[November 7, 2025 2:00 PM](https://www.schneier.com/blog/archives/2025/11/faking-receipts-with-ai.html/#comment-449697)

[apologies for the somewhat off-topic thread]

@Bilateralrope:

It works best when the creator of the document seals it immediately after it’s created, so there’s a secure, verifiable seal that proves where the document came from, when it was sealed, and that it hasn’t changed. More and more businesses are requiring sealed invoices/receipts before they pay.

That said, documents can be sealed when received. That doesn’t prove who the document came from, but it does prove that that’s the copy you got, when you sealed it, and that it hasn’t changed since you sealed it. That can prevent disputes about timing and prevents tampering from that moment forward. There are countless cases of employees tampering with invoices to embezzle funds.

The technology that we use isn’t new, and is an ISO standard for PDF. It has become extremely popular in Europe as a means of proving documents are authentic. Our business makes it easy for our customers to send sealed documents as well as (very soon) automatically verifying the seals on documents they receive.

Moz •
[November 7, 2025 5:39 PM](https://www.schneier.com/blog/archives/2025/11/faking-receipts-with-ai.html/#comment-449716)

Surely for most companies the scale of this would be so small that working on “can we trust our employees” at a generic level would pay off far more than any amount of receipt-chasing. I’ve never had to claim back more than $50, normally the scale I see is more someone buying a widget over the counter and bringing that plus receipt to the company.

If you’re making staff pay thousands of dollars of company expenditure hoping to get reimbursed the opportunities for fraud are much greater But that’s a broken business model, your employees should never be unpaid unsecured creditors. Fix the model, don’t punish the people you expect to keep lending you money.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2025/11/faking-receipts-with-ai.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2025/11/faking-receipts-with-ai.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%...
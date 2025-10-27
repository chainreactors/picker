---
title: Weekly Retro 2024-W18
url: https://0xda.de/blog/2024/05/weekly-retro-2024-w18/
source: Blogs  dade
date: 2024-05-07
fetch_date: 2025-10-06T17:17:20.148268
---

# Weekly Retro 2024-W18

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/05/weekly-retro-2024-w18/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

6 minutes

# [Weekly Retro 2024-W18](https://0xda.de/blog/2024/05/weekly-retro-2024-w18/)

---

* [Debt Free (Again)](#debt-free-again)
* [A New Mailing List](#a-new-mailing-list)
* [Datalist, Duh](#datalist-duh)
* [What I’m Reading](#what-im-reading)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

In which I postponed writing until the very last hour. I’m still feeling fairly sick, unfortunately, and my cough has been keeping me up late at night. Some personal finance updates, a mailing list, and why the datalist HTML element is super cool and also terrible.

## Debt Free (Again)

![My 2017 Miata RF, parked in front of JR Ramen Station](https://0xda.de/blog/2024/05/weekly-retro-2024-w18/img/miata.f8e19db5d517f6c73c843e604ca5cd60.jpg)

This week I submitted my last payment on my car, paying it off about 2 years ahead of schedule. This is exciting for me for a couple reasons – I hate being in debt, even though my loan was a very affordable rate, and I like freeing up the cash flow for other things. I bought my car after first getting debt free back in 2021 when I paid off my final student loan debt. It was a fun purchase since I didn’t need to drive for anything but recreation, and I was okay with taking on a car loan as my only loan.

I’ve spent a bit modifying the car since I bought it, but now that I’ve paid it off, I feel more comfortable spending on additional modifications. I have Verus Engineering louvers in the hood, a carbon miata wing on the back, and a Paradox Styling one-of-one white-to-black fade wrap on the car. I also updated most of the lights to use sequential LED signals. But now that it’s paid off, I’m considering springing for the turbo kit from Flyin Miata. We’ll see. Part of me wants to hold off on spending any more on this car, since there are a bunch of other cars I feel like I’d like more.

## A New Mailing List

I have a mailing list setup now! I am not quite ready to start using it to send out my posts or anything, but I have a self-hosted listmonk instance running on my server, available at [list.0xda.de](https://list.0xda.de/subscription/form). This is keeping in the theme with ensuring as few third parties between you and me have your data. It even mails through a mail server that I control, though this may later come back to bite me. I’ll look to better integrate it into my site in the coming week or two, but for now you can click the link above or (hopefully) submit the form below if you’d like to sign up to eventually get email notifications of my posts.

Dade's Digest

## Datalist, Duh

I was working on a community directory website over the week and I am building it with Django + HTMX. This has been a really nice, simple stack to use – although I will admit that Django is kind of annoying in some ways, I ultimately opted to use it because the ORM integration is just… better than trying to achieve the same with Flask + SQLAlchemy.

During this work, I was working on creating a new form for users to add their team and company affiliations to their profile, this way the directory will build itself based on people’s individual profiles. I used [HTMX to fetch the form modal](https://htmx.org/examples/modal-bootstrap/) and then in the form I have fields for Company, Team, Title, Start Date, and End Date.

What I wanted, though, was to make it easy to match a company that already exists in the database, or otherwise create a new one if there isn’t a match. So a dropdown menu isn’t quite right, since it only allows what already exists in the database. I could make a separate button to add a new company or new team, but that felt clunky. I wanted a user to be able to start typing into the Company box and get a list of companies, otherwise submit their entry and automatically create a new one.

To show the list of companies, I used HTMX input events to fire off to an autocomplete endpoint, and the autocomplete endpoint returns two [datalist](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) objects, which get swapped automatically using HTMX `hx-target` and `hx-select-oob`. When these datalist objects get populated, the text input boxes for Company and Team use the options from the corresponding datalist to make recommendations that you can click on or use keyboard navigation to select. Alternatively you can just continue typing. The list of teams that it recommends will automatically adjust itself based on which teams are associated with the company selected.

I was really excited about this approach, it was exactly what I wanted and used browser built in controls. But then I learned that it’s basically impossible to style datalist objects and the way they are recommended to users. This is unfortunate because the default chrome styling is… not great. The options don’t span the whole width of the input box, for instance.

Ultimately I’m probably going to leave the datalist object in place for now, it’s a cool feature built into modern user agents. I just wish it was a bit easier to style. MDN highlights that the datalist element has some accessibility concerns, and Django also [doesn’t support a datalist out of the box](https://forum.djangoproject.com/t/implementing-a-datalist/2052/22) so I had to get creative.

## What I’m Reading

![The Bezzle: A Martin Hench Novel. By Cory Doctorow](https://0xda.de/img/books/TheBezzle-CoryDoctorow.3cad0f2101169aa71fe651fbdfc31f48.jpg)

### The Bezzle

#### By Cory Doctorow

**ISBN: 978-1-250-86587-8**
[Learn More](https://craphound.com/category/bezzle/ "Learn More About The Book")

---

I’m going to be honest, I didn’t read a single page this week, so this is still what I’m reading. I hope to be done with it by next retro, though.

## Interesting Links

* [The E-ink Desk Accessory I’ve Always Wanted](https://www.youtube.com/watch?v=d9forDotXkI) - A DIY e-ink desk accessory that looks pretty cool. I hadn’t really considered wanting this, but I think I do. The only thing I don’t like is that the USB-C port that charges/powers it is coming out the side – if I do something like this, I’d like to try to rearrange it to come out the back to minimize desk clutter.
* [sudon’t](https://dotat.at/%40/2024-05-02-sudo.html) - I’m not sure if I fully agree with this, but it was a good read that challenged the dogma around using sudo.
* [We can have a different web](https://www.citationneeded.news/we-can-have-a-different-web/) - A wonderful post by Molly White about the “good old days” of the web, and how they may not be so far beyond our grasp – in fact it may be easier now than it ever was before.
* [The ultimate ideal bestest base font size that everyone is keeping a secret, especially chet](https://adrianroselli.com/2024/03/the-ultimate-ideal-bestest-base-font-size-that-everyone-is-keeping-a-secret-especially-chet.html) - An interesting and useful post about base font sizes for accessibility. TL;DR – Do not set a base font size.
* [How an empty s3 bucket can make your AWS bill explode](https://medium.com/%40maciej.pocwierz/how-an-empty-s3-bucket-can-make-your-aws-bill-explode-934a383cb8b1) - Absolutely unhinged finding, Amazon will charge a bucket owner for someone making *failed* requests to a bucket. To be clear, you can do all security steps correctly, and someone can cost you thousands of dollars just by guessing the name of your s3 bucket. Amazon...
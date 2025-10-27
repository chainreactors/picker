---
title: Chrome Web Store is a mess
url: https://palant.info/2025/01/13/chrome-web-store-is-a-mess/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-14
fetch_date: 2025-10-06T20:12:50.993250
---

# Chrome Web Store is a mess

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Chrome Web Store is a mess

2025-01-13
 [Add-Ons](/categories/add-ons/)/[Security](/categories/security/)/[Privacy](/categories/privacy/)/[Google](/categories/google/)
 19 mins
 [5 comments](/2025/01/13/chrome-web-store-is-a-mess/#comments)

Letâs make one thing clear first: Iâm not singling out Googleâs handling of problematic and malicious browser extensions because it is worse than Microsoftâs for example. No, Microsoft is probably even worse but I never bothered finding out. Thatâs because Microsoft Edge doesnât matter, its market share is too small. Google Chrome on the other hand is used by around 90% of the users world-wide, and one would expect Google to take their responsibility to protect its users very seriously, right? After all, browser extensions are one selling point of Google Chrome, so certainly Google would make sure they are safe?

![Screenshot of the Chrome download page. A subtitle âExtend your experienceâ is visible with the text âFrom shopping and entertainment to productivity, find extensions to improve your experience in the Chrome Web Store.â Next to it a screenshot of the Chrome browser and some symbols on top of it representing various extensions.](/2025/01/13/chrome-web-store-is-a-mess/chrome_website.png)

Unfortunately, my experience reporting numerous malicious or otherwise problematic browser extensions speaks otherwise. Google appears to take the âleast effort requiredâ approach towards moderating Chrome Web Store. Their attempts to automate all things moderation do little to deter malicious actors, all while creating considerable issues for authors of legitimate add-ons. Even when reports reach Googleâs human moderation team, the actions taken are inconsistent, and Google generally shies away from taking decisive actions against established businesses.

As a result, for a decade my recommendation for Chrome users has been to stay away from Chrome Web Store if possible. Whenever extensions are absolutely necessary, it should be known who is developing them, why, and how the development is being funded. Just installing some extension from Chrome Web Store, including those recommended by Google or âfeatured,â is very likely to result in your browsing data being sold or worse.

Google employees will certainly disagree with me. Sadly, much of it is organizational blindness. I am certain that you meant it well and that you did many innovative things to make it work. But looking at it from the outside, itâs the result that matters. And for the end users the result is a huge (and rather dangerous) mess.

#### Contents

* [Some recent examples](#some-recent-examples)
* [The reporting process](#the-reporting-process)
* [Chrome Web Store and their spam issue](#chrome-web-store-and-their-spam-issue)
* [Can extension reviews be trusted?](#can-extension-reviews-be-trusted)
* [The âfeaturedâ extensions](#the-featured-extensions)
* [How did Google get into this mess?](#how-did-google-get-into-this-mess)
* [What could Google do?](#what-could-google-do)

## Some recent examples

Five years ago I discovered that Avast browser extensions were spying on their users. Mozilla and Opera disabled the extension listings immediately after I reported it to them. Google on the other hand took two weeks where they supposedly discussed their policies internally. The result of that discussion was eventually [their âno surprisesâ policy](https://developer.chrome.com/docs/webstore/program-policies):

> Building and maintaining user trust in the Chrome Web Store is paramount, which means we set a high bar for developer transparency. All functionalities of extensions should be clearly disclosed to the user, with no surprises. This means we will remove extensions which appear to deceive or mislead users, enable dishonest behavior, or utilize clickbaity functionality to artificially grow their distribution.

So when dishonest behavior from extensions is reported today, Google should act immediately and decisively, right? Letâs take a look at two examples that came up in the past few months.

In October I [wrote about the refoorest extension deceiving its users](/2024/10/01/lies-damned-lies-and-impact-hero-refoorest-allcolibri/). I could conclusively prove that Colibri Hero, the company behind refoorest, deceives their users on the number of trees they supposedly plant, incentivizing users into installing with empty promises. In fact, there is strong indication that the company never even donated for planting trees beyond a rather modest one-time donation.

Google got my report and dealt with it. What kind of action did they take? Thatâs a very good question that Google wonât answer. But refoorest is still available from Chrome Web Store, it is still âfeaturedâ and it still advertises the very same completely made up numbers of trees they supposedly planted. Google even advertises for the extension, listing it in the âEditorsâ Picks extensionsâ collection, probably the reason why it gained some users since my report. So much about being honest. For comparison: refoorest used to be available from Firefox Add-ons as well but was already removed when I started my investigation. Opera removed the extension from their add-on store within hours of my report.

But maybe that issue wasnât serious enough? After all, there is no harm done to users if the company is simply pocketing the money they claim to spend on a good cause. So also in October I [wrote about the Karma extension spying on users](/2024/10/30/the-karma-connection-in-chrome-web-store/). Users are not being notified about their browsing data being collected and sold, except for a note buried in their privacy policy. Certainly, thatâs identical to the Avast case mentioned before and the extension needs to be taken down to protect users?

![Screenshot of a query string parameters listing. The values listed include current_url (a Yahoo address with an email address in the query string), tab_id, user_id, distinct_id, local_time.](/2025/01/13/chrome-web-store-is-a-mess/spying.png)

Again, Google got my report and dealt with it. And again I fail to see any result of their action. The Karma extension remains available on Chrome Web Store unchanged, it will still notify their server about every web page you visit (see screenshot above). The users still arenât informed about this. Yet their Chrome Web Store page continues to claim âThis developer declares that your data is not being sold to third parties, outside of the approved use cases,â a statement contradicted by their privacy policy. The extension appears to have lost its âFeaturedâ badge at some point but now it is back.

*Note*: Of course Karma isnât the only data broker that Google tolerates in Chrome Web Store. I published a guest article today by a researcher who didnât want to disclose their identity, [explaining their experience with BIScience Ltd., a company misleading millions of extension users to collect and sell their browsing data](/2025/01/13/biscience-collecting-browsing-history-under-false-pretenses/). This post also explains how Googleâs âapproved use casesâ effectively allow pretty much any abuse of usersâ data.

Mind you, neither refoorest nor Karma were alone but rather recruited or bought other browser extensions as well. These other browser extensions were turned outright malicious, with stealth functionality to perform [affiliate fraud](https://www.investopedia.com/terms/a/affiliate-fraud.asp) and/or collect usersâ browsing history. Googleâs reaction was very inconsistent here. While most extensions affiliated with Karma were removed from Chrome Web Store, the extension with the highest user numbers (and performing affiliate fraud without telling their users) was allowed to remain for some reason.

With refoorest...
---
title: Too Many People Don’t Value the Time of Security Researchers
url: https://soatok.blog/2025/01/21/too-many-people-dont-value-the-time-of-security-researchers/
source: Dhole Moments
date: 2025-01-22
fetch_date: 2025-10-06T20:10:07.933978
---

# Too Many People Don’t Value the Time of Security Researchers

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[Meta-blog](https://soatok.blog/category/meta/) [Security Community](https://soatok.blog/category/technology/software-security/security-community/) [Security Industry](https://soatok.blog/category/technology/software-security/security-industry/)

# Too Many People Don’t Value the Time of Security Researchers

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [January 21, 2025](https://soatok.blog/2025/01/21/too-many-people-dont-value-the-time-of-security-researchers/)

![Too Many People Don’t Value the Time of Security Researchers](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/01/BlogHeader-2025-Devalued.png?fit=1200%2C675&ssl=1)

It’s really not my place to ever command respect from anyone; and that’s not just because I’m a furry–which has always been towards the bottom of the geek hierarchy. I am well aware how little weight my words truly carry, even to other furries, as well as [how little I really matter](https://soatok.blog/2024/09/09/doesnt-matter/).

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/01/Geek-Hierarchy-Dark.png?resize=768%2C845&ssl=1)

[Upscaled, dark mode version](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/01/Geek-Hierarchy-Dark.png) of the Geek Hierarchy meme.
(Light mode version [here](https://soatok.blog/wp-content/uploads/2025/01/Geek-Hierarchy.png).)

But the tech industry holds such little regard to independent security researchers, and values their time so poorly, that it’s no wonder so many would-be hackers feel discouraged from ever learning.

So, I must ask tech workers (especially programmers… and yes, including open source developers) the whole world over to listen for a minute–not for my sake, but for the collateral damage you might be inflicting on newcomers without realizing it.

## Finding vulnerabilities is, itself, a contribution to your project!

This might sound obvious when I say it like that, but I’ve had many people respond to me disclosing a vulnerability disclosure with a demand to spend more of my time writing, testing, and submitting a patch to the project in scope.

When I found and disclosed [vulnerabilities in Matrix’s Olm library](https://soatok.blog/2024/08/14/security-issues-in-matrixs-olm-library/) last year (which they never fixed, and then admitted they knew about for years), I was flooded with strangers demanding to know where the patch or pull request is, as if I have some moral obligation to do free labor on top of the free labor I already provided.

It’s not just Matrix. I’ve lost count of the times this story has played out for me:

1. I find a vulnerability in a software project (whether open source or discovered from reverse engineering).
2. I try to report what I found to them, so they can fix it.
3. They point me to their bug bounty program.
4. I begrudgingly file it with their bug bounty program, with as much detail and concise explanation as I would provide in a GitHub issue.
5. The people running the bug bounty program demand a fully weaponized proof-of-concept exploit in order for my report to be taken seriously.
6. I silently ponder whether it’s worth it to [risk losing my account on that platform](https://soatok.blog/2022/06/14/when-soatok-used-bugcrowd/) to email Full Disclosure instead.

To be clear, I know what it’s like to triage reports from bug bounty programs. It’s a lot of garbage most of the time, [and Generative AI has made it so much worse](https://daniel.haxx.se/blog/2024/01/02/the-i-in-llm-stands-for-intelligence/).

But when someone opens a report with, “I’m not looking for a bounty, this is where I was told to send reports,” it’s a little insulting to get the same treatment as the 10,000th “vulnerable to self-XSS via browser developer tools; pay bounty now” report that week.

Now, this isn’t my first rodeo (by any means) and I have relatively thick skin.

**Most newcomers will not.**

Please think, for a moment, about whether you want them to feel discouraged and that their time isn’t valued.

> Last month, a reader of my blog read me into a vulnerability they disclosed to a vendor that treated them the same way I discussed above.
>
> Their report referenced some of my blog posts and open source work. It was kind of cool to see!
>
> But when I asked what their next steps are (since the vendor’s response was *kind of lame*), their response was basically:
>
> “Nothing, I give up.”
>
> I’m kind of getting tired of picking up the pieces caused by mistreatment of amateur hackers.

#### It Can Always Be Worse

The history of independent security research is full of [horrible](https://www.csoonline.com/article/551507/hard-coded-credentials-placing-dental-offices-at-risk.html) [incidents](https://www.ftc.gov/news-events/news/press-releases/2016/01/dental-practice-software-provider-settles-ftc-charges-it-misled-customers-about-encryption-patient) and [bogus legal peril](https://www.wired.com/story/missouri-threatens-sue-reporter-state-website-security-flaw/)–where someone doing everything right ends up profoundly disrespected by the people they were trying to help.

There’s a reason the [Pwnie Awards](https://en.wikipedia.org/wiki/Pwnie_Awards) usually has a category for “Lamest Vendor Response”. This isn’t just an American problem; the Chaos Communications Congress has an [ongoing saga involving legal threats to security researchers](https://www.ccc.de/en/updates/2024/das-ist-vollig-entgleist) by the Polish rail vehicle manufacturer, Newag.

As bad as these situations can be, they’re relatively rare and often gather lots of media attention.

The problem I’m trying to highlight today is more banal and commonplace.

## Responsible Disclosure, Isn’t

These are the actual categories of vulnerability disclosure:

* Full Disclosure
* Coordinated Disclosure
* Non-Disclosure
* Privately disclosing to a third party (e.g., selling to an exploit broker) and watching the world burn

That’s it. This list is exhaustive.

The term “responsible disclosure” is [a harmful, moralistic term that even the person who coined it now discourages](https://adamcaudill.com/2015/11/19/responsible-disclosure-is-wrong/) in favor of “coordinated disclosure” instead.

There is no one disclosure policy that fits the criteria for “responsible” in all situations. Anyone that claims otherwise will inevitably summon a long and tedious message board debate on the topic.

When it comes to cryptographic flaws that put users’ privacy at risk, immediate [full disclosure is actually the most responsible thing to do](https://www.schneier.com/essays/archives/2007/01/schneier_full_disclo.html).

In most other cases, coordinated disclosure is preferred, especially if the knowledge of the vulnerability is easy to turn into an exploit that harms users.

When most people say “responsible disclosure” they *really* mean “coordinated disclosure”, where the vendor pledges to fix the issue and release a new version before the vulnerability details are made public. And they must eventually be public, unless you’re really practicing non-disclosure.

Non-disclosure is what a lot of software vendors truly want. Without disclosure, the public remains in the dark about the vulnerabilities that could have impacted them.

If someone opts for full disclosure on a product you care about, emailing the researcher demanding they spend more of their time writing a patch too is more than *a little* uncalled for.

### Don’t Assume Vendor Reputation Is Our Top Priority

The most basic rule of professional ...
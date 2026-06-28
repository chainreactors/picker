---
title: AI Vendor Vetting: An OK Practice Guide
url: https://secjuice.com/ai-vendor-vetting-an-ok-practice-guide/
source: Over Security
date: 2026-06-27
fetch_date: 2026-06-28T06:14:08.173402
---

# AI Vendor Vetting: An OK Practice Guide

[![Secjuice](https://secjuice.com/content/images/2018/12/Logo-1.png)](https://secjuice.com)

* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/osint/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write](https://secjuice.com/join-secjuice-writing-team/)

[Sign in](#/portal/signin)
[Donate](/donate/)

# AI Vendor Vetting: An OK Practice Guide

Practical guide to AI vendor vetting, covering key data, security, compliance, and risk questions to assess and manage AI third-party risks.

* [![Ross Moore](/content/images/size/w100/2025/01/Moore-Headshot-2024-1195C.jpg)](/author/rossamoore/)

#### [Ross Moore](/author/rossamoore/)

Jan 2, 2026

[Tip Writer](https://ko-fi.com/secjuice)

![AI Vendor Vetting:  An OK Practice Guide](/content/images/size/w2000/2026/01/crossrhythmcoffee_imagine_Cyber_detective_checking_out_an_AI__e0c29158-6c77-4422-829a-61f4d3bae9c0_2.png)

The Review

Happy New Year! Many have made plans, goals, and [resolutions for 2026](https://today.yougov.com/society/articles/53789-americans-new-years-resolutions-2026-poll?ref=secjuice.com) – diet, exercise, business, and finance are just some of the determinations to make personal and professional changes.

While the categories are common, how each of those plays out is completely individual. How one goes about losing weight or getting fit; how much money to save or how much debt to pay off; what certifications need to be made or university classes to take – it all depends on what you want to do, where you want to go, who you are, and who you want to be.

When reviewing vendors, there are almost just as many factors. Are you in a regulated industry? What kind of data do you hold? What’s the maturity of the vendor review process? Public or Private sector? How much revenue is available? What role and risk classification do the potential vendors play in the org? There’s no one-size-fits-all for the vendors, and, therefore, no way to present a single approach to solve the Gordian knot that is third-party management.

However, knowing more about what’s involved can help create a better approach than one had before learning more.

This is NOT a best-practice guide, but I hope the following ideas will help you as you create an AI vendor vetting strategy appropriate to your company.

And just like New Year’s resolutions, having your “Why?” in place is important. Proper vetting of AI vendors better protects your corporate and customer data and reputations. Not protecting these personal, private, and proprietary details could easily land an organization in legal and regulatory hot water, incurring high fines and legal fees.

*Disclaimer: I’m not employed by anyone I mention below, nor do I receive any kind of kickbacks, incentives, etc. There are no sponsored links or anything of the kind. Everything I link to is just to provide information.*

# Main Questions

In short, the main information to get from the vendor includes:

·        Where is the data is going?

o   *What and where are the subprocessors?*

·        Do they train anything on your data?

o   *Many AI vendors train on your data depending on the pricing model. It’s “privacy at a price,” but at least they’re transparent about it (often only in the fine print, unfortunately).*

·        What is done to secure the data?

·        What protections are in place for cross-border transfers?

o   *Even if it’s transferring just username and email, that could be enough to warrant a DPA (Data Protection Agreement/Addendum) or SCC (Standard Contractual Clause).*

An aspect that complicates what matters is that the information, if available, can be anywhere on the vendor’s site. A security statement, the Privacy Policy, DPA, Terms of Service, T7Cs (Terms and Conditions), MSA (Master Subscription Agreement), GDPR/CCPA/CPRA notice, Trust Center. It’s fine that every company has its own site layout - it just makes it tougher when reviewing and assessing when the site designers don’t have security review in mind. Be prepared for a trip on the ethereal highway. There have been several vendors where it was faster to go to ChatGPT or Perplexity and ask “Does ABC have a Trust Center?” and it gives me the URL much faster than it took me not to find it by going directly to the vendor.

Think also about those in your company, your internal customers, coworkers, and employees. What do you need them to tell you so you can make an appropriate review?

·        What is the application being used for?

o   Is it dev? Trial? Production? On your site or in your app?

·        How many people will use it?

o   One department only? Corporate-wide?

·        Would any customer data be involved?

·        Will corporate data be moved?

·        Is there another app already in use that would fulfill the function?

·        Is GenAI involved? If so, to what extent?

·        If there are multiple options, which option is under consideration?

Each organization has its own regulatory, compliance, security, and contractual needs, so apply the above and the following as you see fit.

Keep track of the requests! You don’t want to get caught up in any corporate spitting matches such as “why did you approve this?” Actually, you could easily be caught up in those, but the primary concern is having a good and documented approach and response.

You don’t want to have to vet the same vendor (believe me – there are more vendors than can be kept in memory, especially when they have similar names!). Sometimes, one department doesn’t know that another department already has it, so it could save on licensing, too (and saving money is always a plus for the business).

Have an AI AUP (Acceptable Use Policy) in place to point your company to as a constant reference. As often as possible, point to an authoritative internal source document; this will prevent lots of time with extra typing, lots of time in communicating, and prevent others from using you as the source of info each time.

If you want to get quite technical - both for questions for vendors and for answering your own customers’ questions - the AI questions in the HECVAT is an excellent resource for questions. As of this writing, it’s version 4.1.4. [https://www.educause.edu/higher-education-community-vendor-assessment-toolkit](https://www.educause.edu/higher-education-community-vendor-assessment-toolkit?ref=secjuice.com)

 For internal risk assessment - something you can use yourself or pass to your coworkers to fill out (though you may want to simplify it because of its complexity), this is an excellent spreadsheet from FS-ISAC here: [https://www.fsisac.com/hubfs/Knowledge/AI/FSISAC\_GenerativeAI-VendorEvaluation&QualitativeRiskAssessmentTool.xlsx](https://www.fsisac.com/hubfs/Knowledge/AI/FSISAC_GenerativeAI-VendorEvaluation%26QualitativeRiskAssessmentTool.xlsx?ref=secjuice.com)

There are innumerable determining factors in what to look for when someone requests the use of AI in your company: How are you yourself going to use it? How will your other departments use it? Will it be used in a cloud instance? Or locally? Is it being tested for inclusion in your product? Or will it just be for educational purposes? What data is going in and through it? Does it need watermarked? Is your industry regulated? What will your customers expect from the product? In what industries do your customers live? These are just some of the options to consider (and we haven’t even touched on what resources you have to obtain, test, and maintain all-the-AI-things).

For many of the AI vendors I’ve reviewed, I’ve noticed a good number who have SOC 2 Type1 or 2, and ISO 27001. Before AI, many vendors didn’t have those. So, at least AI vendors are aware of that. But what’s strangely absent is available and solid documentation on their AI development process and internal AI use. While I’m not often expecting ISO 42001, I’m expecting...
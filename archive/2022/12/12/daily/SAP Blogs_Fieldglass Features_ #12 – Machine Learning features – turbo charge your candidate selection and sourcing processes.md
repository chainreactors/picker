---
title: Fieldglass Features: #12 – Machine Learning features – turbo charge your candidate selection and sourcing processes
url: https://blogs.sap.com/2022/12/11/fieldglass-features-12-machine-learning-features-turbo-charge-your-candidate-selection-and-sourcing-processes/
source: SAP Blogs
date: 2022-12-12
fetch_date: 2025-10-04T01:14:54.176980
---

# Fieldglass Features: #12 – Machine Learning features – turbo charge your candidate selection and sourcing processes

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Spend Management](/t5/spend-management/ct-p/spend-management)
* [Spend Management Blog Posts by SAP](/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-sap)
* Fieldglass Features: #12 – Machine Learning featur...

Spend Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/spend-management-blog-sap/article-id/1853&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Fieldglass Features: #12 – Machine Learning features – turbo charge your candidate selection and sourcing processes](/t5/spend-management-blog-posts-by-sap/fieldglass-features-12-machine-learning-features-turbo-charge-your/ba-p/13568920)

![jacksonr](https://avatars.profile.sap.com/c/1/idc1b52be50bc34e268f6b4ab0171295c4073698b1603e2180e2442773a84198a7_small.jpeg "jacksonr")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[jacksonr](https://community.sap.com/t5/user/viewprofilepage/user-id/95598)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=spend-management-blog-sap&message.id=1853)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/spend-management-blog-sap/article-id/1853)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568920)

‎2022 Dec 11
11:21 PM

[4
Kudos](/t5/kudos/messagepage/board-id/spend-management-blog-sap/message-id/1853/tab/all-users "Click here to see who gave kudos to this post.")

3,115

* SAP Managed Tags
* [SAP Fieldglass Vendor Management System](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fieldglass%2520Vendor%2520Management%2520System/pd-p/67838200100800006957)

* [SAP Fieldglass Vendor Management System

  SAP Fieldglass Vendor Management System](/t5/c-khhcw49343/SAP%2BFieldglass%2BVendor%2BManagement%2BSystem/pd-p/67838200100800006957)

View products (1)

Keeping the theme of features to help you in this candidate tight market as we ride the wave of the great resignation and record high employment rates - We’re looking at 2 of our features that utilise SAP Machine learning with the goal of saving you time in the recruitment process and helping you find the best quality. The two features are Resume Ranking and Find Best Matching Candidates.

Resume Ranking – uses machine learning to analyse job posting details with job seekers resume to provide a ranking of resumes’ submitted.

Find Best Matching Candidates – uses machine learning to analyse a reference resume – and find other’s which are the closest match based on skills, job title, industry, education and years of experience

Potential Candidates (which you’ll recall was the last edition and is in the trail below)– uses sql search of the application to highlight workers ending soon, job seekers etc who share common traits of the job posting – such as job code, currency, distribution list, within the past 40 days

**Resume Ranking**

**What does it do:**  Resume Ranking parses through the resumes attached to each Job Seeker submitted towards a specific Job Posting and the algorithm assigns a resume score based on closeness to keywords provided in the Job Posting Description, ranking the available candidates in order of out output of the algorithm.

**Why should it be of interest:**

1. Whilst not a replacement for manual resume review, it’s provides a suggestion to the recruiter of which resumes may be worth while reviewing first – which particularly in a high volume roles and where the market is moving quickly – speed to identify top candidates is key.

2. Objective scoring which isn’t influenced by any un-conscious biased that may occur on seeing individual particulars in a resume

Effort to implement –easy, service request to enable the change to company config, then addition  to user role permission

Effort to test  – super easy

Benefits to business – improve quality of external worker hired, automate (assist) processes to reduce cycle time, reduce possible unconscious bias as part of resume reviewing process

When enabled, below we can see in the job seekers tab of job posting, what the seeker's resume ranking is as aligned to the job description

![](/legacyfs/online/storage/blog_attachments/2022/12/resume-ranking-ui.png)

 [Click here to download Resume Ranking feature document](https://d.dam.sap.com/a/tehJRxZ/FG%20-%20Resume%20Ranking.pdf?rc=10)

**Find Best Matching Candidates**

**What does it do:**  Find best matching candidates  enables buyers to search  their existing contingent workers, workforce, and job seekers that are similar to a referenced record.  So for example – if the hiring manager or program office know that they previously had an amazing Project Manager that would be perfect for a current job posting but not currently available – by using this feature you direct Fieldglass to search existing workers, workforce and job seekers to find who’s the closest match to that reference Project Managers’ resume. So where Resume Ranking uses machine learning to match resume’s to job posting analysis,  Find Best Matching Candidates uses machine learning to match a known job seeker’s resume, with current workers, workforce or job seekers.

**Why should it be of interest:**

1. Reduce time to hire by identifying existing workers or job seekers – so negating the potential need to go to market

2. Improve worker quality by extending the internal search feature available concurrently with an external search strategy.

Effort to implement –easy, service request to enable the change to company config,

Effort to test  – super easy

Benefits to business – Potentially saving you both time and money

When viewing the job seekers tab on a job posting, you have option to open the matching tool

![](/legacyfs/online/storage/blog_attachments/2022/12/find-best-match-1.png)

Once opened, you select from drop down your reference worker, and FG will then find the profiles that most closely match that worker

![](/legacyfs/online/storage/blog_attachments/2022/12/find-best-match-2.png)

what other Fieldglass features has your program taken advantage of to gain the competitive advantage in the war for talent?

Labels

* [Product Updates](/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-sap/label-name/product%20updates)

* [Fieldglass Features](/t5/tag/Fieldglass%20Features/tg-p/board-id/spend-management-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fspend-management-blog-posts-by-sap%2Ffieldglass-features-12-machine-learning-features-turbo-charge-your%2Fba-p%2F13568920%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Explore What's New: SAP Fieldglass November 2025 Release Webinar](/t5/spend-management-blog-posts-by-sap/explore-what-s-new-sap-fieldglass-november-2025-release-webinar/ba-p/14227751)
  in [Spend Management Blog Posts by SAP](/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-sap)  a week ago
* [Copenhagen CSD Sept 24th - Discover Joule an...
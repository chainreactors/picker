---
title: MTA project Integration with Git in Web IDE: HANA XSA
url: https://blogs.sap.com/2022/12/14/mta-project-integration-with-git-in-web-ide-hana-xsa/
source: SAP Blogs
date: 2022-12-15
fetch_date: 2025-10-04T01:32:18.363684
---

# MTA project Integration with Git in Web IDE: HANA XSA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* MTA project Integration with Git in Web IDE: HANA ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160200&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [MTA project Integration with Git in Web IDE: HANA XSA](/t5/technology-blog-posts-by-members/mta-project-integration-with-git-in-web-ide-hana-xsa/ba-p/13551028)

![pallab_haldar](https://avatars.profile.sap.com/4/2/id42d0a352096e2fd071fe39e7ec5b73f1f20abf1d7ce6542aa72c8246918879b7_small.jpeg "pallab_haldar")

[pallab\_haldar](https://community.sap.com/t5/user/viewprofilepage/user-id/594699)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160200)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160200)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551028)

‎2022 Dec 14
6:50 PM

0
Kudos

1,205

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP HANA Live](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Live/pd-p/73554900100700001326)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA Live

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BLive/pd-p/73554900100700001326)

View products (2)

Today I am going to discuss about the MTA project Integration with GitHub as a source control in Web IDE: HANA XSA.

Before perform the steps, I want everybody know the flow and keep the diagram so that you have a clear concept on this migration -

![](/legacyfs/online/storage/blog_attachments/2022/12/GitDiagram1-1.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/GitDiagram2-1.png)

**Integration Steps :**

1. Open your project from Web IDE : If the project is not there please create it by importing the file or create it from a MTA project template. You can Clone it from the existing project from a git repository also.

![](/legacyfs/online/storage/blog_attachments/2022/12/MTA-Project-C1.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/MTA2.png)

1.Create a Local repository and name it suitable with your project :

![](/legacyfs/online/storage/blog_attachments/2022/12/WjFhi-1.png)

2. Configure the remote repository for the local repository :

A. Before you configure the remote repository please log into GitHub using the below URL, create an account and create a repository.

<https://github.com/login>

Copy the repository URL like below. If you working on direct Master node copy the master node URL. It is preferable to create a branch node and working on it, they you need to copy the URL of branch node.

![](/legacyfs/online/storage/blog_attachments/2022/12/Git-url.png)

B. In web IDE , right click on your project and click Git -> Set Remote and  in the Configure Git Repository dialog box, enter your GitHub  repository’s URL.

![](/legacyfs/online/storage/blog_attachments/2022/12/configure-git-repository.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/Change-commit.png)

**3. Configure Stage Layer :**

It will automatically fetch the Master node and the branches of the remote repository in your Web IDE.

To make sure  the files are staged inside the Git Panel select the checkbox "Stage all",

Put the commit description and click the commit button.

![](/legacyfs/online/storage/blog_attachments/2022/12/Stage-2.png)

You can do also using command from terminal -

```
git init

git add -A

git commit -m “Test Commit"
```

4. Pull Code from GitHub.

You can pull the data from the GitHub remote repository by either pull or fetch Data. I am going to tell you what is the difference between pull and fetch. Fetch do not change the local dev space artifacts. you can only show the committed changes in remote repo. Better to go with Pull.

![](/legacyfs/online/storage/blog_attachments/2022/12/Pull-and-fetch.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/Pull.png)

You can do pull from Terminal as well.

```
Pull

git remote add projectm  https://xxxxxx.git

git pull projectm

git clone <repository url>

git fetch

git fetch -all

git checkout Branch1

git clone —-branch Branch1 <remote-repo-url>

git branch –Branch1

$ git checkout -t projectm/Branch1
```

5.  Push Code to **GitHub** and check the changes in GitHub.

Before Push do Pull from remote to update your code artifacts repeating step 4.

Then Push -

![](/legacyfs/online/storage/blog_attachments/2022/12/Push.png)

You can do pull from Terminal as well.

```
Push

git remote add projectm  https://xxxxxx.git

git push -u projectm BranchL :Branch1
```

In the next chapter in **MTA project Integration** with Git in  Business Application Studio.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fmta-project-integration-with-git-in-web-ide-hana-xsa%2Fba-p%2F13551028%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  6 hours ago
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  6 hours ago
* [Driving AI Adoption with BTP: Highlights](/t5/technology-blog-posts-by-sap/driving-ai-adoption-with-btp-highlights/ba-p/14233554)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  7 hours ago
* [InsufficientResources](/t5/technology-q-a/insufficientresources/qaq-p/14234085)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  9 hours ago
* [A Smarter Move from Boomi and MuleSoft to SAP Integration Suite - Assessed, Automated, Validated](/t5/technology-blog-posts-by-members/a-smarter-move-from-boomi-and-mulesoft-to-sap-integration-suite-assessed/ba-p/14233647)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user...
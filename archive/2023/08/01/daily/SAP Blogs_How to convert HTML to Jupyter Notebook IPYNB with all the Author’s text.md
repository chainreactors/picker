---
title: How to convert HTML to Jupyter Notebook IPYNB with all the Author’s text
url: https://blogs.sap.com/2023/07/31/how-to-convert-html-to-jupyter-notebook-ipynb-with-all-the-authors-text/
source: SAP Blogs
date: 2023-08-01
fetch_date: 2025-10-06T17:00:06.434949
---

# How to convert HTML to Jupyter Notebook IPYNB with all the Author’s text

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to convert HTML to Jupyter Notebook IPYNB with...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/164004&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to convert HTML to Jupyter Notebook IPYNB with all the Author's text](/t5/technology-blog-posts-by-members/how-to-convert-html-to-jupyter-notebook-ipynb-with-all-the-author-s-text/ba-p/13572963)

![P281512](https://avatars.profile.sap.com/8/4/id8485065bcfb8f155128d54b656ad6bb0f0624a3f73cd0ba5ee3d244bab20dd5a_small.jpeg "P281512")

[P281512](https://community.sap.com/t5/user/viewprofilepage/user-id/161179)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=164004)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/164004)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13572963)

‎2023 Jul 31
8:35 PM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/164004/tab/all-users "Click here to see who gave kudos to this post.")

4,353

* SAP Managed Tags
* [Machine Learning](https://community.sap.com/t5/c-khhcw49343/Machine%2520Learning/pd-p/240174591523510321507492941674121)
* [Python](https://community.sap.com/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)
* [SAP Predictive Analytics](https://community.sap.com/t5/c-khhcw49343/SAP%2520Predictive%2520Analytics/pd-p/73555000100800000084)
* [SAP HANA, express edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%252C%2520express%2520edition/pd-p/73555000100800000651)

* [SAP Predictive Analytics

  SAP Predictive Analytics](/t5/c-khhcw49343/SAP%2BPredictive%2BAnalytics/pd-p/73555000100800000084)
* [SAP HANA, express edition

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%25252C%2Bexpress%2Bedition/pd-p/73555000100800000651)
* [Machine Learning

  Topic](/t5/c-khhcw49343/Machine%2BLearning/pd-p/240174591523510321507492941674121)
* [Python

  Programming Tool](/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)

View products (4)

This is an utility that worked very well in converting  HTML to Jupyter Notebook IPYNB **with all the Author's text for 3 SAP blogs I tried**

Will be very helpful for many blogs with the current thrust in Data Science and Data Engineering; reader wishes to try but copy paste painful
Without lots of comments (read markdown) only code is almost useless!

Did a lot of searching and found NOTHING that met my needs
Nearest was<https://www.marsja.se/converting-html-to-a-jupyter-notebook/>
His notebook is in<https://github.com/marsja/jupyter/blob/master/convert_html_jupyter_notebook_tutorial.ipynb>

I converted that to **marsja.py** adapted for SAP Blogs where **code** is
inside pre tags as you can see in the HTML files

marsja,py works *but gives a notebook with only code cells;*to my mind not too helpful; uses beautifulsoup and lxml packages

Please head to **my repository**<https://github.com/ojnc/html2ipynbSensible>

My **html2ipynbsensible.py** gives exactly what most people need
A python notebook with lots of markup

I used the excellent package **html2text** which you need to install
pip install html2text
Documentation in<https://fossies.org/linux/html2text/docs/usage.md>

2nd package you *do not need to install* is **py2nb**<https://github.com/williamjameshandley/py2nb/blob/master/py2nb>
Wonderful compact but delivered as a python script
I had to copy paste in my program
Have informed Author about the 3 Issues that compelled me to copy

**I ran 4 commands**

# APL1 Hands-On Tutorial: Automated Predictive (APL) in SAP HANA Cloud
python html2ipynbSensible.py "<https://blogs.sap.com/2020/07/27/hands-on-tutorial-automated-predictive-apl-in-sap-hana-cloud/>" APL1

# PAL1 Hands-On Tutorial: Leverage SAP HANA Machine Learning in the Cloud through the Predictive Analysis Library
# Author has CODE as images
# He has provided the ipynb from github
python html2ipynbSensible.py "[https://blogs.sap.com/2021/02/25/hands-on-tutorial-leverage-sap-hana-machine-learning-in-the-cloud-t...](https://blogs.sap.com/2021/02/25/hands-on-tutorial-leverage-sap-hana-machine-learning-in-the-cloud-through-the-predictive-analysis-library/)" PAL1

# APL2 Multiclass Classification with APL (Automated Predictive Library)
python html2ipynbSensible.py "<https://blogs.sap.com/2022/04/01/multiclass-classification-with-apl-automated-predictive-library/>" APL2

# APL2 as bare code by marsja.py
python marsja.py "<https://blogs.sap.com/2022/04/01/multiclass-classification-with-apl-automated-predictive-library/>" APL2

The output files are in my repository<https://github.com/ojnc/html2ipynbSensible>
You should examine at least APL1 if you wish to use and adapt

Github has excellent jupyter notebook rendition
See these
# output of html2ipynbsensible.py
**APL1FINAL.ipynb****APL2FINAL.ipynb**

# output of marsja.py ONLY CODE no FUN!
**APL2marsja.ipynb**

# executed with editing just user **ML\_USER** and connection **MYHANACLOUD**runAPL1FINAL.ipynb
runAPL2FINAL.ipynb
runAPL2marsja.ipynb

my saved connection is **MYHANACLOUD** and saved user **ML\_USER**

Not fortunate enough to have Cloud BTP access and I have a P-ID
so I used HANA EXPRESS in my personal docker
<https://blogs.sap.com/2023/07/20/my-success-with-hana-express/>

**I hope many use this utility which I wrote definitely for my self**

For external notebooks where HTML is not as "nice" as SAP Blogs
you can adapt the python program by looking at the HTML.txt
Find how the code cells are organized in the HTML
Skill in Python REGEX will help a lot

* [APL](/t5/tag/APL/tg-p/board-id/technology-blog-members)
* [jupyter notebook](/t5/tag/jupyter%20notebook/tg-p/board-id/technology-blog-members)
* [pa](/t5/tag/pa/tg-p/board-id/technology-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fhow-to-convert-html-to-jupyter-notebook-ipynb-with-all-the-author-s-text%2Fba-p%2F13572963%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Hello Python: My First Script in SAP BAS Connecting to HANA Cloud](/t5/technology-blog-posts-by-members/hello-python-my-first-script-in-sap-bas-connecting-to-hana-cloud/ba-p/14228993)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a week ago
* [Getting started with Prompt Templating in SAP Generative AI Hub: Principles and Implementation](/t5/technology-blog-posts-by-sap/getting-started-with-prompt-templating-in-sap-generative-ai-hub-principles/ba-p/14192547)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  2025 Sep 04
* [Using conda-forge in SAP Business Application Studio – my notes](/t5/technology-blog-...
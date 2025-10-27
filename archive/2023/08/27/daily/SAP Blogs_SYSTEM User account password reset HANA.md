---
title: SYSTEM User account password reset HANA
url: https://blogs.sap.com/2023/08/26/system-user-account-password-reset-hana/
source: SAP Blogs
date: 2023-08-27
fetch_date: 2025-10-04T11:59:21.636926
---

# SYSTEM User account password reset HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SYSTEM User account password reset HANA

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/165645&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SYSTEM User account password reset HANA](/t5/technology-blog-posts-by-members/system-user-account-password-reset-hana/ba-p/13581567)

![gopi_sai_teja_paruchuri](https://avatars.profile.sap.com/e/5/ide53cc77947254e263f9e5082d973a025e9447c50b8b1e22afbf3893e85e26a12_small.jpeg "gopi_sai_teja_paruchuri")

[gopi\_sai\_teja\_paruchuri](https://community.sap.com/t5/user/viewprofilepage/user-id/874112)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=165645)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/165645)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13581567)

‎2023 Aug 26
5:54 AM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/165645/tab/all-users "Click here to see who gave kudos to this post.")

21,885

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP HANA studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520studio/pd-p/67838200100800004076)
* [SAP HANA, platform edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%252C%2520platform%2520edition/pd-p/01200314690800001945)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA studio

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%2Bstudio/pd-p/67838200100800004076)
* [SAP HANA, platform edition

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%25252C%2Bplatform%2Bedition/pd-p/01200314690800001945)

View products (3)

This Blog explains the procedure to Reset SYSTEM user account in HANA 1.0 and HANA 2.0(SYSTEM-DB and Tenant-DB).

**Procedure for HANA 1.0**

1. Stop the Hana database using “HDB stop” or “sapcontrol -nr <nn> -function Stop”.

2. In a new server session execute the below commands(These commands start the Hana Database
nameserver process explicitly)
/usr/sap/<SID>/hdbenv.sh
/usr/sap/<SID>/exe/hdbnameserver

3. In another session execute the below commands(These commands start the Hana Database
compileserver process explicitly)
/usr/sap/<SID>/hdbenv.sh
/usr/sap/<SID>/exe/hdbcompileserver

4. In another session execute the below commands(These commands start the Hana Database
Indexserver process in an interactive mode)
/usr/sap/<SID>/hdbenv.sh
/usr/sap/<SID>/exe/hdbindexserver –resetUserSystem

5. After some backend programs are run, the console asks for the password which can be entered
manually.

6. It asks for the confirmation, upon which enter the same password as previously entered.

7. Once the password is accepted we can see that some functions are run and the message
“database shutdown completed” can be seen.

8. Execute “ctrl+c” in the previous sessions where “nameserver” and “compileserver” were started.

9. Start the Hana Database and we can login with the set/given password.

Note: hdbenv.sh (This command sets the shell environment)

**Procedure for HANA 2.0**

SYSTEM User account in SYSTEMDB:

1. Shutdown the database and start the “mdcdispatcher”(Multi-Database Container
Dispatcher) manually in a server shell.
/usr/sap/<SID>/HDB00/exe/mdc/hdbmdcdispatcher -v -s <SID>

2. Run the below command in different shell to start the indexserver in an interactive mode.
/usr/sap/<SID>/HDB00/hdbenv.sh
/usr/sap/<SID>/HDB00/exe/hdbnameserver –resetUserSystem

3. Provide the password when prompted.

4. Enter the same password in confirmation prompt.

5. After the password is accepted the database is shutdown automatically by the back end
process.

6. Stop the “mdcdispatcher” process running in another terminal using “ctrl+c”

7. Start the database and login with password which was given previously.

SYSTEM User account in Tenant-DB:

1. Login to the SYSTEMDB in which the tenant is residing and open the SQL console for the
same.

2. Execute the below command to stop the tenant Database.
ALTER SYSTEM STOP DATABASE <SID>

3. Execute the below command to change the password.
ALTER DATABASE <SID> SYSTEM USER PASSWORD <DESIRED PASSWORD>

4. After executing the above command, the password is changed and the indexserver process is
started.

5. Login with the password given in the command.

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsystem-user-account-password-reset-hana%2Fba-p%2F13581567%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [S/4HANA transition for US Federal Agencies](/t5/technology-blog-posts-by-sap/s-4hana-transition-for-us-federal-agencies/ba-p/14234423)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Flexible Workflows for Procurement in SAP S/4HANA](/t5/technology-blog-posts-by-members/flexible-workflows-for-procurement-in-sap-s-4hana/ba-p/14234315)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Creating a Hybrid CAP (Node.js) Profile with PostgreSQL on BTP from Business Application Studio](/t5/technology-blog-posts-by-members/creating-a-hybrid-cap-node-js-profile-with-postgresql-on-btp-from-business/ba-p/14233631)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Thursday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 5 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/us...
---
title: How to change password hash from MD5 to SHA512 in RHEL8.2?
url: https://blogs.sap.com/2023/02/16/how-to-change-password-hash-from-md5-to-sha512-in-rhel8.2/
source: SAP Blogs
date: 2023-02-17
fetch_date: 2025-10-04T06:51:56.701169
---

# How to change password hash from MD5 to SHA512 in RHEL8.2?

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to change password hash from SHA512 to MD5 in ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163429&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to change password hash from SHA512 to MD5 in RHEL8.2?](/t5/technology-blog-posts-by-members/how-to-change-password-hash-from-sha512-to-md5-in-rhel8-2/ba-p/13569875)

![](/skins/images/05B15621965F8471415FB73DF617B794/responsive_peak/images/icon_anonymous_profile.svg)

Former Member

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163429)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163429)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569875)

‎2023 Feb 16
11:59 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163429/tab/all-users "Click here to see who gave kudos to this post.")

1,983

* SAP Managed Tags
* [Red Hat Enterprise Linux](https://community.sap.com/t5/c-khhcw49343/Red%2520Hat%2520Enterprise%2520Linux/pd-p/566117836046276697184412662459974)

* [Red Hat Enterprise Linux

  Operating System](/t5/c-khhcw49343/Red%2BHat%2BEnterprise%2BLinux/pd-p/566117836046276697184412662459974)

View products (1)

I am writing this blog for the audience who want to migrate OS users along with SAP Application, DB from one source OS environment to different OS environment. Like we migrated all SAP systems running on RHEL6.1 in source and RHEL8.2 in target.

Below steps need to be performed so that OS users can be migrated to target without the loss of passwords.

Back up these files: as they are very important for OS operations

/etc/pam.d/system-auth

/etc/libuser.conf

/etc/login.defs

/etc/shadow

1. Run these commands to assign edit permissions to the system-auth, conf, and login.defs files:

cd /etc

chmod 644 pam.d/system-auth

chmod 644 libuser.conf

2. Open the /etc/pam.d/system-auth file using a text editor.

3. Search for the password sufficient entry in the file, similar to:password sufficient /lib/security/$ISA/pam\_unix.so use\_authtok nullok shadow

4. Replace the existing hash key (md5, des, or sha256) with md5 or append md5, if there is no existing key. For example:password sufficient /lib/security/$ISA/pam\_unix.so use\_authtok nullok shadow md5

5. Open the /etc/libuser.conf file using a text editor.

Change crypt\_style = sha512 to crypt\_style = md5

6. Open the /etc/login.defsfile using a text editor

Add MD5\_CRYPT\_ENAB yes

Change ENCRYPT\_METHOD to MD5

7. Change the permission back to original

chmod 444 pam.d/system-auth

chmod 444 libuser.conf
chmod 444 login.defs

8. Last step would be to copy users from /etc/passwd file and passwords from /etc/shadow file. Testing can be done by using same password to log in on new server.

**Conclusion:**

This method is tested and verified that Higher linux version can support old password encryption algorithm. Above steps will reduce the work of recreation of 1000+ local OS users in new server environment. End users can still login to their server using same DNS name using same passwords.

Kindly provide your kind feedback and suggestions in comment section.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fhow-to-change-password-hash-from-sha512-to-md5-in-rhel8-2%2Fba-p%2F13569875%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Creating a Hybrid CAP (Node.js) Profile with PostgreSQL on BTP from Business Application Studio](/t5/technology-blog-posts-by-members/creating-a-hybrid-cap-node-js-profile-with-postgresql-on-btp-from-business/ba-p/14233631)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [What’s new in Mobile development kit client 25.9](/t5/technology-blog-posts-by-sap/what-s-new-in-mobile-development-kit-client-25-9/ba-p/14227370)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [Secure Your Digital Journey with SAP CIAM](/t5/technology-blog-posts-by-sap/secure-your-digital-journey-with-sap-ciam/ba-p/14232983)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [SAP IQ to SAP HANA Cloud, Data Lake Migration Overview](/t5/technology-blog-posts-by-sap/sap-iq-to-sap-hana-cloud-data-lake-migration-overview/ba-p/14228663)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [Issue with the password visibility to OTHER S-users in ECS Service Requests](/t5/technology-q-a/issue-with-the-password-visibility-to-other-s-users-in-ecs-service-requests/qaq-p/14232143)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Wednesday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 4 |
| [![natanael1](https://avatars.profile.sap.com/5/7/id5755ebef974c12476c62d649735972c696010b8bb05e4ebc3ac052476ea15035_small.jpeg "natanael1")  natanael1](/t5/user/viewprofilepage/user-id/1557162) | 3 |
| [![smarchesini](https://avatars.profile.sap.com/0/c/id0cf1ddd928dd875ac324a5701f9e4d9a60995d0072e5b58f718f5dd57231fae9_small.jpeg "smarchesini")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") smarchesini](/t5/user/viewprofilepage/user-id/125739) | 3 |
| [![dylan-drummond](https://avatars.profile.sap.com/0/0/id00cf6ce5e32b466c407ed6996e23a9b60703442ad43de8fe0e22782d75a73afb_small.jpeg "dylan-drummond")  dylan-drummond](/t5/user/viewpr...
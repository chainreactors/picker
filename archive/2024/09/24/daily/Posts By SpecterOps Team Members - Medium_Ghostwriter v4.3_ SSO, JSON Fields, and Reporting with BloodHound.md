---
title: Ghostwriter v4.3: SSO, JSON Fields, and Reporting with BloodHound
url: https://posts.specterops.io/ghostwriter-v4-3-sso-json-fields-and-reporting-with-bloodhound-976835a7edba?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-09-24
fetch_date: 2025-10-06T18:30:45.218611
---

# Ghostwriter v4.3: SSO, JSON Fields, and Reporting with BloodHound

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F976835a7edba&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fghostwriter-v4-3-sso-json-fields-and-reporting-with-bloodhound-976835a7edba&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fghostwriter-v4-3-sso-json-fields-and-reporting-with-bloodhound-976835a7edba&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-976835a7edba---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-976835a7edba---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Ghostwriter v4.3: SSO, JSON Fields, and Reporting with BloodHound

[![Christopher Maddalena](https://miro.medium.com/v2/resize:fill:64:64/1*Qau5i8aEfpZkMb2PCBnyZw.jpeg)](https://cmaddy.medium.com/?source=post_page---byline--976835a7edba---------------------------------------)

[Christopher Maddalena](https://cmaddy.medium.com/?source=post_page---byline--976835a7edba---------------------------------------)

6 min read

·

Sep 23, 2024

--

Listen

Share

Press enter or click to view image in full size

![]()

Ghostwriter v4.3 is available now, and it enhances features introduced in previous versions of v4 in some exciting ways! In particular, this article will dive into how you can integrate a tool like BloodHound Community Edition (BHCE) with Ghostwriter v4.3.

First, we would be remiss if we did not mention the refreshed single sign-on (SSO) feature.

## Refreshed Single Sign-On

Ghostwriter has supported SSO for quite some time, but it’s a feature that always required extra effort that made implementation difficult. The steps to enable SSO were unique to each provider and required making changes to configurations you don’t normally touch, so we did not have much documentation. You may not have known it was an option!

That all changes with v4.3.0. The wiki has a new *Access, Authentication, and Session Controls* section that covers everything in this realm. It’s worth a review for new or current Ghostwriter administrators because we’ve added new documentation for SSO and expanded information around user session management features released earlier this year with v4.0.

[## Access, Authentication, & Session Controls | Ghostwriter

### Everything that manages how users authenticate, what they can access, and how their web sessions work

www.ghostwriter.wiki](https://www.ghostwriter.wiki/features/access-authentication-and-session-controls/?source=post_page-----976835a7edba---------------------------------------)

Once you have an SSO provider configured, you’ll see your provider(s) available on the login page.

Press enter or click to view image in full size

![]()

Login Page with SSO Providers Configured

To support SSO, we added support for custom config files. Previously, to add an SSO configuration, you had to edit config files tracked in the Ghostwriter repository; this meant admins would have to stash and re-apply any customizations or changes before updating a Ghostwriter server. Ghostwriter v4.3 allows customization of your Ghostwriter server without worrying about a lost configuration. This support for custom configuration values mainly applies to SSO configuration, but you can use it for other configuration values — e.g., adding a Django application to your Ghostwriter installation or customizing an email backend configuration.

## Introducing JSON to Custom Fields

Let’s dive into an even meatier topic with some extensive possibilities. Ghostwriter v4.1 introduced the capability of adding extra fields to most Ghostwriter objects (e.g., reports, projects, clients). That initial feature release supported strings, rich text fields, numbers, and boolean values. This release adds support for a JSON field type.

You can now add a field to hold a JSON blob. Whatever JSON you provide will be available to your reports. You can take JSON output from an assessment tool, provide it to Ghostwriter, and create a report with that data!

Various tools will output results as JSON or XML. If your tool can’t output JSON but does support XML, like *nmap*, you can easily convert the XML to JSON using a few lines of Python and *xmltodict*. One tool that works very well with this new feature is BHCE!

Here is an example of a custom *SharpHound Data* field added to a report with an example of BHCE data. You can view and explore the JSON in Ghostwriter with collapsible nodes.

Press enter or click to view image in full size

![]()

Example of SharpHound Data Displayed in Ghostwriter’s Preview

## Case Study: Integrating BloodHound CE With Ghostwriter

BHCE’s data is already available as JSON, but the JSON files are typically large for most Active Directory (AD) environments outside of a lab environment. Also, the data’s full value comes from your analysis, so feeding the raw JSON to Ghostwriter isn’t the way to go. No one wants to copy and paste the contents of a dozen JSON files into fields anyway. We can leverage BHCE and Ghostwriter’s robust APIs to perform analysis and automatically pass the JSON to Ghostwriter.

For this case study, we’ll focus on extracting some AD domain data from the BHCE data loaded on our server and performing some fundamental analysis. We’ll also have a JSON field added to our Ghostwriter reports to hold the final output for reporting. If you want to follow along with this POC after updating your Ghostwriter server, you can find details in the GitHub repository linked below.

We can use some Python and BHCE’s API to get a list of all collected domains and extract some of their properties (e.g., name, functional level), information about trusts, and basic information about users and computers. All of this is available with BHCE’s built-in API endpoints, but the API also supports running custom Cypher queries.

We’ll perform some analysis by running queries to pull all the operating systems for computers in each domain and checking the *pwdlastset* property on all the users to count how many have passwords older than 90 days. Finally, we’ll count how many users have an old password and how many systems are running each unique operating system within each domain and globally for the collection.

When that analysis is complete, our script will assemble the data into a nicely formatted JSON blob and update our report field via Ghostwriter’s API.

The full proof-of-concept is available here:

[## GitHub - GhostManager/bloodhound-integration-poc: A proof-of-concept script for automating the…

### A proof-of-concept script for automating the extraction of data from a BloodHound Community Edition server and sending…

github.com](https://github.com/GhostManager/bloodhound-integration...
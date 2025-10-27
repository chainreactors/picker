---
title: Ghostwriter v3.1 Now Available
url: https://posts.specterops.io/ghostwriter-v3-1-now-available-47cfcccd6b02?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2022-10-20
fetch_date: 2025-10-03T20:25:30.764804
---

# Ghostwriter v3.1 Now Available

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F47cfcccd6b02&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fghostwriter-v3-1-now-available-47cfcccd6b02&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fghostwriter-v3-1-now-available-47cfcccd6b02&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-47cfcccd6b02---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-47cfcccd6b02---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Ghostwriter v3.1 Now Available

[![Christopher Maddalena](https://miro.medium.com/v2/resize:fill:64:64/1*Qau5i8aEfpZkMb2PCBnyZw.jpeg)](https://cmaddy.medium.com/?source=post_page---byline--47cfcccd6b02---------------------------------------)

[Christopher Maddalena](https://cmaddy.medium.com/?source=post_page---byline--47cfcccd6b02---------------------------------------)

4 min read

·

Oct 19, 2022

--

Listen

Share

Press enter or click to view image in full size

![]()

Ghostwriter v3.1 is now available! This release introduces several new features along with a host of minor improvements. This post will look at the most significant changes, starting with a pair of new tabs on the project dashboard.

## Deconfliction Tracking

When performing any offensive assessment work, you are likely to trigger an alert or generate anomalous logs that will get someone’s attention. If the system owner cannot identify you as the source, they will likely reach out to you to deconflict the event.

You can now record deconfliction events under a project’s *Deconflictions* tab. Each recorded event appears as a card, like so:

Press enter or click to view image in full size

![Example of Ghostwriter’s Deconfliction Event Cards]()

Example of Ghostwriter’s Deconfliction Event Cards

Deconflictions are time-sensitive. Delayed or inconclusive responses can mean wasted effort and frustration for defenders. Events like these are why activity logging is critical. Each deconfliction card tracks a few key pieces of information and light metrics.

> *You can learn more about how Ghostwriter makes activity logging simple and easy here:* [*https://www.ghostwriter.wiki/features/operation-logs*](https://www.ghostwriter.wiki/features/operation-logs)

Press enter or click to view image in full size

![Deconfliction Event Card Related Log Entries]()

Deconfliction Event Card Related Log Entries

Once you have responded, you can update the status to reflect if the event was or was not related to your work, and the card will show how much time has passed between receiving the deconfliction request and the final response.

This data helps you and your client keep track of these events, but it can also reveal potential gaps and weaknesses in monitoring strategies. For example, suppose several hours have passed between the alert timestamp and the client contacting you. In that case, that could indicate defenders not receiving timely notifications or dealing with a lot of noise and a backlog of notifications.

A careful review of deconfliction events before a post-assessment debrief call can offer interesting insights and topics of discussion.

## White Card Tracking

The project dashboard also has a new *White Cards* tab for tracking project white cards. Like the term deconflict, *white card* comes to us from the U.S. military. It refers to “a simulated event in an operational test.” A client may issue a white card for various reasons, such as if a system is too fragile or critical to risk attempting to exploit it or if there is a need or desire to bypass exploitation due to time constraints.

The latter may be the most common white card. Today we commonly refer to assessments with this white card as “assumed breach.” With such a white card, the assessment begins as if the team has successfully exploited an external system or gained access or credentials through other means (e.g., phishing).

This white card and other simulated events must be documented and tracked. Each white card has a date and time the client issued it, a descriptive title or headline field, and a free-form field for more thorough or detailed descriptions.

Press enter or click to view image in full size

![Example White Card]()

Example White Card

These fields make it simple to include these in a Ghostwriter report template as a list or table of white cards.

## System Health Monitoring

Finally, Ghostwriter administrations can now monitor health API endpoints. The primary endpoint is */status*. This endpoint runs thorough tests against Ghostwriter’s critical services and monitors the host system’s available memory and storage. Thresholds for these checks are configurable via *ghostwriter-cli*.

Press enter or click to view image in full size

![Ghostwriter System Status Page]()

Ghostwriter System Status Page

Docker will also monitor container and service health. Running *./ghostwriter-cli running* will return the status of your running Ghostwriter containers. The *Status* column will now show the health status of the container’s service.

The wiki has more information on how to configure health check options and suggestions for automated monitoring.

[## Health Monitoring

### How to monitor the health of Ghostwriter services

www.ghostwriter.wiki](https://www.ghostwriter.wiki/features/health-monitoring?source=post_page-----47cfcccd6b02---------------------------------------)

## Wrap Up

These new features are just a few things we have added or changed in recent updates. We have also addressed several issues and requests submitted by the community. Here are a few highlights:

* Findings manually added to a report now appear with a flag to make it easier to identify new findings you may want to save to your library for future use.
* Any field editable with the WYSIWYG editor is now available as a styled *RichText* object in report templates.
* We expanded the *totals* key in report data to include the total number of findings in each severity category.
* Added a new scheduled task to monitor activity logs for current projects and send reminders if logs have been inactive for more than 24 hours (or any set number of hours).

As always, check the release CHANGELOGs for the complete list of changes. We plan to continue to expand on these recent changes and add more before the end of the year. For now, get the latest release here!

[## Releases · GhostManager/Ghostwriter

### You can't perform that action at this time. You signed in with another tab or window. You signed out in another tab or…

github.com](https://github.com/GhostManager/Ghostwriter/releases?source=post_page-----47cfcccd6b02--------------------------...
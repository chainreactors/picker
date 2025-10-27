---
title: New Feature Announcement: Automated Reporting with Webhooks
url: https://luxsci.com/blog/automated-reporting-with-webhooks.html
source: LuxSci
date: 2023-02-28
fetch_date: 2025-10-04T08:15:33.517340
---

# New Feature Announcement: Automated Reporting with Webhooks

[![](https://d2g355lhiymhv6.cloudfront.net/wp-content/uploads/2024/06/19153212/Horizontal-Logo-Dark.svg)](/)
[![LUXSCI](https://d2g355lhiymhv6.cloudfront.net/wp-content/uploads/2024/06/19153212/Horizontal-Logo-Dark.svg)](/)

[Contact Us](/contact-us)

[« blog index](/blog)

# New Feature Announcement: Automated Reporting with Webhooks

February 27th, 2023

The LuxSci team is pleased to announce the release of automated reporting with webhooks to help organizations manage their data workflows. These updates will allow administrators to push information and analytics from their email campaigns into existing dashboards or to email recipients in close to real time.

“Webhooks give us the ability to receive real-time notifications and events from LuxSci in bulk, which will streamline our internal analysis, reporting, and, therefore, decision-making,” said Katie Ali, Product Manager at [Signify Health.](https://www.signifyhealth.com/)

“Today, our analysis is limited due to the number of resources we have on hand to pull email data. Now that we are implementing webhooks, we can start to automate the analytic process from end to end. Webhooks also eliminate the complexity of a reoccurring polling logic to achieve the same effect.”

[![automated reporting webhooks](https://d2g355lhiymhv6.cloudfront.net/wp-content/uploads/2023/02/23103048/business-chart-visual-graphics-report-concept.jpg)](https://d2g355lhiymhv6.cloudfront.net/wp-content/uploads/2023/02/23103048/business-chart-visual-graphics-report-concept.jpg)

## What are Webhooks?

A webhook is an HTTP request triggered by an event in a source system and sent to a destination system. In other words, webhooks push data to the customer’s website URL for processing.

LuxSci’s webhooks are available for all our API reports, including email sending, delivery status changes, email opens, email clicks, login failures, and unsubscribes.

In addition to traditional webhooks that post data to a URL, LuxSci also allows API reports to be automatically sent via TLS-encrypted email to any email address at a custom frequency. The report data is attached to the email in JSON, CSV, or HTML format.

## Why are LuxSci’s Webhooks Useful?

Webhooks allow customers to automatically push information about email events via LuxSci’s API as they are happening without pulling from the API. That allows customers to record and review this information and take timely action based on these events.

LuxSci’s webhooks are incredibly scalable, unlike those of many other providers. Instead of sending one webhook notification to the customer for each event (which could be millions of notifications a day), LuxSci sends a digest of all events that happened over a specified period. By sending a digest instead of individual notifications, it is easier to process the notifications at scale. Batching the notifications reduces the server resources the customer requires to receive and process high volumes of webhooks by a significant amount.

Our webhooks are also resilient to customer webhook processing service failure. LuxSci will automatically retry webhook delivery when customer processing servers are down or failing, so events are less likely to be lost than webhooks provided by other services.

## How to Set Up Automated Reporting with Webhooks

Login to your LuxSci account and visit the Report section of the user interface. In the sidebar, select Automated Reports. First, you will need to select the data you want to report. Choose from API reports including:

* Emails sent
* Delivery status updates
* Emails opened
* Emailed links clicked
* SMTP login failures
* Email addresses suppressed or unsubscribed
* Emails marked as spam

Then select the data source (either SMTP/API or WebMail). The reports can include account-wide events or can be restricted to only certain users. Name the report and how frequently you want to check for new events. Webhooks reporting is configurable to any desired granularity from once every minute to once a day.

Reports will only be sent when there are new events. For example, a report with five-minute intervals checks for new events every five minutes but only sends a report if there are new events.

Finally, choose how the data should be delivered (via a webhook or email with TLS encryption) and in what format for email reports (JSON, HTML, or CSV). Enter an email address to notify if there are errors with the report, and then you can enable it.

Automated reports can be further customized by using parameters. For example, they help limit reporting to specific domains, campaigns, or email headers. Please contact our team today to learn more about how LuxSci’s Automated Reporting can enhance your data workflows.

This entry was posted
on Monday, February 27th, 2023 at 12:00 pm and is filed under [New Feature Announcements](https://luxsci.com/blog/category/features-and-services).

[![Check your SMTP TLS](https://djrufvackyewl.cloudfront.net/s3/design2018/Banner_Blog_TLS_Checker.jpg)](/smtp-tls-checker)

### Follow LuxSci

[![](https://djrufvackyewl.cloudfront.net/s3/design2018/Social-TW.gif)](https://www.twitter.com/LuxSci "Twitter")
[![](https://djrufvackyewl.cloudfront.net/s3/design2018/Social-FB.gif)](https://www.facebook.com/pages/Westwood-MA/LuxSci/25893114249 "Facebook")
[![](https://djrufvackyewl.cloudfront.net/s3/design2018/Social-LI.gif)](https://www.linkedin.com/company/luxsci "LinkedIn")

### Categories

* [Popular Posts](/blog/category/popular "Popular Posts")
* [HIPAA](/blog/category/hipaa-library "HIPAA")
* [SecureForm](/blog/category/secureform-2 "SecureForm")
* [Email Marketing](/blog/category/bulk-email-2 "Email Marketing")
* [New Features](/blog/category/features-and-services "New Features")
* [Case Studies](/blog/category/case-studies "Case Studies")
* [Dedicated & Cloud](/blog/category/dedicated-2 "Dedicated & Cloud")
* [Security & Privacy](/blog/category/security-and-privacy "Security & Privacy")

[![LuxSci](https://luxsci.com/images/svg/LUXSCI-Logo-WhiteBkg.svg)](/)

Copyright © 2004-2025 Lux Scientiae,® Incorporated,
All rights reserved.

[privacy policy](/extranet/privacy.html)
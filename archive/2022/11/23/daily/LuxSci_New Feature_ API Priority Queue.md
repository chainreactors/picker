---
title: New Feature: API Priority Queue
url: https://luxsci.com/blog/new-feature-api-priority-queue.html
source: LuxSci
date: 2022-11-23
fetch_date: 2025-10-03T23:30:18.594977
---

# New Feature: API Priority Queue

[![](https://d2g355lhiymhv6.cloudfront.net/wp-content/uploads/2024/06/19153212/Horizontal-Logo-Dark.svg)](/)
[![LUXSCI](https://d2g355lhiymhv6.cloudfront.net/wp-content/uploads/2024/06/19153212/Horizontal-Logo-Dark.svg)](/)

[Contact Us](/contact-us)

[« blog index](/blog)

# New Feature: API Priority Queue

November 22nd, 2022

Maximize efficiency by employing our new email-sending prioritization features. Secure High Volume Email customers utilizing APIs for sending can now set a message priority to determine the order in which messages are sent out.

[![email api priority queue](https://d2g355lhiymhv6.cloudfront.net/wp-content/uploads/2022/11/21144051/email-message-mail-notification-service-new-incoming-sms-envelope-social-network-conversation-spam.jpg)](https://d2g355lhiymhv6.cloudfront.net/wp-content/uploads/2022/11/21144051/email-message-mail-notification-service-new-incoming-sms-envelope-social-network-conversation-spam.jpg)

## What is the API Priority Queue Feature?

This feature allows customers to set a priority on email messages sent via API. Customers can pass an optional parameter in their API to set the message priority on a scale of 0 – 9. Zero is the lowest priority, nine is the highest, and four is the default priority setting.

The API priority queue feature allows customers to send out higher-priority messages faster when the sending queue is already long.

## Why is the API Priority Queue Useful?

Traditionally, all customer emails were processed in a “first come, first serve” method. Customers can now use the priority queue to determine the sending order when they simultaneously send transactional and marketing messages via the API.

For example, time-sensitive password resets could be stuck in the queue while a large blast of marketing emails is transmitted. Depending on the size of the email list and server capacity, the password reset email could be held up for several minutes to even hours. This situation is unacceptable for many business use cases.

Customers can designate transactional emails as high-priority with the API priority queue feature enabled. When transactional emails are given a high-priority status, they can jump the line and go out before less time-sensitive emails like marketing messages.

## How to Utilize the API Priority Queue

This feature is only available to Secure High Volume Email customers utilizing APIs to send emails. It does not work for SMTP sending. Customers can add the optional parameter and desired value while crafting their API call to send emails. Additionally, customers can use the API configuration editor in the LuxSci UI to change the default priority value for all messages. You can review the details of our API by going to: https://luxsci.com/rest-api.html.

This entry was posted
on Tuesday, November 22nd, 2022 at 12:00 pm and is filed under [New Feature Announcements](https://luxsci.com/blog/category/features-and-services).

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
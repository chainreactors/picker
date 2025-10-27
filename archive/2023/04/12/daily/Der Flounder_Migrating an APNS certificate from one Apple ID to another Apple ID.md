---
title: Migrating an APNS certificate from one Apple ID to another Apple ID
url: https://derflounder.wordpress.com/2023/04/11/migrating-an-apns-certificate-from-one-apple-id-to-another-apple-id/
source: Der Flounder
date: 2023-04-12
fetch_date: 2025-10-04T11:29:59.864321
---

# Migrating an APNS certificate from one Apple ID to another Apple ID

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Push Notification Service](https://derflounder.wordpress.com/category/apple-push-notification-service/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/) > Migrating an APNS certificate from one Apple ID to another Apple ID

## Migrating an APNS certificate from one Apple ID to another Apple ID

April 11, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of a recent change, I needed to migrate an [APNS certificate](https://developer.apple.com/documentation/devicemanagement/implementing_device_management/setting_up_push_notifications_for_your_mdm_customers) from being associated with one Apple ID to now being associated with another Apple ID. Apple has a KBase article available which provides contact information for this, which is available via the link below:

<https://support.apple.com/HT208643>

For those folks with AppleCare support plans, you can also submit a ticket to AppleCare. That’s the route I took. Regardless of which support avenue you pursue, Apple will request the following information from you.

* APNS Certificate Subject DN
* APNS Certificate CN
* APNS Certificate Serial Number
* APNS Certificate Expiration Date
* The Apple ID you want to migrate from
* The Apple ID you want to migrate to

For more information, please see below the jump:

You can obtain the following information from the [Apple Push Certificates Portal](https://identity.apple.com/pushcert):

* APNS Certificate Subject DN
* APNS Certificate CN
* APNS Certificate Serial Number
* APNS Certificate Expiration Date

To see how to do this, please use the following procedure:

1. Log into the [Apple Push Certificates Portal](https://identity.apple.com/pushcert) using the Apple ID you want to migrate from.

![Screenshot 2023 04 11 at 3 48 59 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-11-at-3.48.59-pm.png?w=595 "Screenshot 2023-04-11 at 3.48.59 PM.png")

2. Make a note of the current certificate’s expiration date.

![Screenshot 2023 04 11 at 3 49 59 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-11-at-3.49.59-pm.png?w=595 "Screenshot 2023-04-11 at 3.49.59 PM.png")

3. Click the **( i )** button to display the certificate information.

![Screenshot 2023 04 11 at 3 50 22 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-11-at-3.50.22-pm.png?w=595 "Screenshot 2023-04-11 at 3.50.22 PM.png")

4. Make a note of the APNS certificate’s serial number.

![Screenshot 2023 04 11 at 3 50 23 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-11-at-3.50.23-pm.png?w=595 "Screenshot 2023-04-11 at 3.50.23 PM.png")

5. Make a note of the APNS certificate’s Certificate Subject DN.

**Note:** Even though it may be displayed in the Portal site as being multiple lines, the Certificate Subject DN should be a one-line entry when you send it to Apple.

![Screenshot 2023 04 11 at 3 50 24 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-11-at-3.50.24-pm.png?w=595 "Screenshot 2023-04-11 at 3.50.24 PM.png")

6. Make a note of the APNS certificate’s CN.

**Note:** The CN is included as part of the Certificate Subject DN information. It will be a string with information similar to this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | CN=APSP:0e77f39b-e9c8-42f9-8e8b-b5508c4abe95 |

[view raw](https://gist.github.com/rtrouton/891a8a46436461c7ca5ba640e0f13ba8/raw/0ef274f4a591d49664f00699a5de2e9bb5af16c9/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/891a8a46436461c7ca5ba640e0f13ba8#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![Screenshot 2023 04 11 at 3 50 25 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-11-at-3.50.25-pm.png?w=595 "Screenshot 2023-04-11 at 3.50.25 PM.png")

For example, if you have an APNS certificate with the following information:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | APNS Certificate Subject DN: C=US, CN=APSP:dc1a3263-443c-4779-a3c3-18c95dd11264, UID=com.apple.mgmt.External.dc1a3263-443c-4779-a3c3-18c95dd11264 |
|  | APNS Certificate Serial Number: 3bb763753df5d8dd |
|  | APNS Certificate Expiration Date: January 4, 2024 |

[view raw](https://gist.github.com/rtrouton/d47edd711097fd9784301c31a532edbb/raw/2b22f1265f25b6ca2e8e591bbf876aa74ca712ae/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/d47edd711097fd9784301c31a532edbb#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You would convert that to the following information for Apple:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | Serial Number: 3bb763753df5d8dd |
|  | Subject CN: CN=APSP:dc1a3263-443c-4779-a3c3-18c95dd11264 |
|  | Subject DN: C=US, CN=APSP:dc1a3263-443c-4779-a3c3-18c95dd11264, UID=com.apple.mgmt.External.dc1a3263-443c-4779-a3c3-18c95dd11264 |
|  | Expiration Date: January 4, 2024 |

[view raw](https://gist.github.com/rtrouton/94639246a6f0955975099655258cd666/raw/b6979fd5c2c3e90d46a6a27ec923cf6e56dae165/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/94639246a6f0955975099655258cd666#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

The last part is identifying the Apple ID you want to migrate from, and the Apple ID you want to migrate to. For example, if you want to migrate an APNS certificate with the information listed above from an Apple ID of **oldappleid@company.com** to an Apple ID of **newappleid@company.com**, you could send in the following request via email:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | Email subject: [Apple Push Notification Service] Transferring APNS certificate with serial number 3bb763753df5d8dd from one Apple ID to another Apple ID |
|  |  |
|  | Email body: |
|  |  |
|  | I need to transfer the following APNS certificate from one Apple ID to another Apple ID: |
|  |  |
|  | Serial Number: 3bb763753df5d8dd |
|  | Subject CN: CN=APSP:dc1a3263-443c-4779-a3c3-18c95dd11264 |
|  | Subject DN: C=US, CN=APSP:dc1a3263-443c-4779-a3c3-18c95dd11264, UID=com.apple.mgmt.External.dc1a3263-443c-4779-a3c3-18c95dd112...
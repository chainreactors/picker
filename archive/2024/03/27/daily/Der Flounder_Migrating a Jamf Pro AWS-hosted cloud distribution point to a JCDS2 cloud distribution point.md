---
title: Migrating a Jamf Pro AWS-hosted cloud distribution point to a JCDS2 cloud distribution point
url: https://derflounder.wordpress.com/2024/03/26/migrating-a-jamf-pro-aws-hosted-cloud-distribution-point-to-a-jcds2-cloud-distribution-point/
source: Der Flounder
date: 2024-03-27
fetch_date: 2025-10-04T12:09:25.251708
---

# Migrating a Jamf Pro AWS-hosted cloud distribution point to a JCDS2 cloud distribution point

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Jamf Pro Classic API](https://derflounder.wordpress.com/category/jamf-pro-classic-api/) > Migrating a Jamf Pro AWS-hosted cloud distribution point to a JCDS2 cloud distribution point

## Migrating a Jamf Pro AWS-hosted cloud distribution point to a JCDS2 cloud distribution point

March 26, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

I recently needed to migrate a Jamf Cloud-hosted Jamf Pro instance from using an AWS-hosted cloud distribution point to using a Jamf-hosted JCDS2 cloud distribution point. For those looking at a similar migration, please see below the jump for more details.

**Advisory:** I strongly advise having Jamf’s Professional Services folks involved if you’re planning a migration like this. The reason is that, as of the current Jamf Pro 11.3.2 release, you can only have one cloud distribution point at a time. A migration like the one I performed will involve a cut-over process which includes having to re-upload your current distribution point’s installer packages to the new JCDS2 distribution point. This process also necessitates having good recent backups for the Jamf Pro instance in question.

With the assistance of Jamf’s Professional Services (particular thanks to Sepie Moinipanah, Leslie Helou and David Raabe for their support), the migration in my case went smoothly. Please see below for the process I followed to migrate from an AWS-hosted cloud distribution point to using a Jamf-hosted JCDS2 cloud distribution point:

**Pre-requisites:**

* A copy of all of the installers in the current AWS-hosted cloud distribution point
* [The Cloud Services connection enabled in your Jamf Pro server’s settings](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Cloud_Services_Connection.html)
* [jamfCPR](https://github.com/BIG-RAT/jamfcpr)
* [API Client Role and API Client with the correct permissions](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/API_Roles_and_Clients.html)
* A very recent backup of your Jamf Cloud-hosted Jamf Pro server

**Getting the installers from your current distribution point:**

There are several ways to get the installers from an AWS-hosted cloud distribution point. The method I chose was to use AWS’s command line tool to sync the contents of the S3 bucket used by the cloud distribution point to a local directory on my workstation:

<https://derflounder.wordpress.com/2018/02/15/backing-up-the-contents-of-an-aws-hosted-jamf-pro-cloud-distribution-point-to-a-local-directory/>

**API Client Role and API Client:**

The jamfCPR wiki [describes the necessary permissions needed to sync installer packages to a JCDS2 cloud distribution point](https://github.com/BIG-RAT/jamfcpr/wiki), in the context of an API Client Role. As a result, I used an API Client Role and API Client in this case because the API Client Role permissions don’t always map one-to-one to the permissions available to Jamf Pro accounts and groups. Please see below for the permissions I set for my API Client Role:

* Read Cloud Services Settings
* Read Distribution Points
* Create Packages
* Read Packages
* Update Packages
* Delete Packages
* Read Cloud Distribution Point
* Update Cloud Distribution Point
* Create Jamf Content Distribution Server Files
* Read Jamf Content Distribution Server Files
* Delete Jamf Content Distribution Server Files
* Jamf Packages Action

![Screenshot 2024-03-26 at 9.19.23 AM](https://derflounder.wordpress.com/wp-content/uploads/2024/03/screenshot-2024-03-26-at-9.19.23e280afam.png?w=595)

**Preparing for the distribution point migration:**

1. Verify that you have [the latest version of jamfCPR](https://github.com/BIG-RAT/jamfcpr) available.

**Note:** If the JCDS2 cloud distribution point you’re migrating to is located outside of the United States, make sure you’re using **jamfCPR** 5.x or later. **jamfCPR** 4.12 and earlier is not able to work with JCDS2 cloud distribution points which are hosted in AWS regions outside of the United States.

2. Verify that you have an API Client Role and API Client on the Jamf Pro server which has the correct permissions assigned.

3. Verify that you have a copy of all installers on your current AWS-hosted cloud distribution point stored on the same Mac that you have the **jamfCPR** app installed on.

4. Work with Jamf to make sure that a backup of your Jamf Pro service is made just prior to doing the migration.

**Advisory about the Jamf Pro backup:**

At this point, I want to stop for a moment and discuss why that backup of your Jamf Pro service is so important. The reason has to do with how AWS-hosted cloud distribution points are created. When you set one up, Jamf Pro will do the following:

1. Create an S3 bucket with a randomly-generated name in the US-East-1 AWS region.
2. Create an associated CloudFront distribution which connects to the S3 bucket created in Step 1.

As the Jamf Pro admin, you don’t get to choose anything in this process and you can’t select an existing S3 bucket. What this means is that the migration goes wrong and you need to revert back to your AWS-hosted cloud distribution point, the only way to do so is to roll back your Jamf Pro service to a point in time before the migration started. You will not be able to go back to using your existing AWS-hosted cloud distribution point without restoring from that backup because there is no way otherwise to have Jamf Pro use that existing AWS-hosted cloud distribution point.

If you try to go back otherwise, Jamf Pro will not use the existing AWS-hosted cloud distribution point. Instead, Jamf Pro will set up a new S3 bucket and CloudFront distribution and you will now have a brand-new and completely empty AWS-hosted cloud distribution point.

**Running the migration:**

1. Log into your Jamf Pro server as an admin user with all needed rights.

2. Verify that the **Cloud Services connection** is logged in and appears to be working properly.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/03/screenshot-2024-03-26-at-9.17-2.png?w=595 "Screenshot 2024-03-26 at 9.17.png")

3. Go to **Settings: Server: Cloud distribution point**.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/03/screenshot-2024-03-26-at-9.17.png?w=595 "Screenshot 2024-03-26 at 9.17.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2024/03/screenshot-2024-03-26-at-9.17-1.png?w=595 "Screenshot 2024-03-26 at 9.17.png")

4. Click the **Test** button and verify that your connection to the cloud distribution point is working correctly.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/03/screenshot-2024-03-26-at-10.15.png?w=595 "Screenshot 2024-03-26 at 10.15.png")

5. Install something from your Jamf Pro server and verify that installation is working correctly.

6. Verify in your policy logs that the installer is coming from an address which matches something similar to what’s shown below:

**<https://d2zft6agzhvlnv.cloudfront.net>**

7. In your Jamf Pro server, go to **Settings: Server: Cloud distribution point**.

Note: The next step is a point of no return, for reasons described above in the **Advisory about the Jamf Pro backup** section. Make sure a very recent Jamf Pro backup is available.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/03/screenshot-2024-03-26-at-9.17.png?w=595 "Screenshot 2024-03-26 at 9.17.png")

8. Select **Jamf Cloud** and click the **Save** icon.

![](https://derfloun...
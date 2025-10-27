---
title: Deploying disk management using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2025/06/11/deploying-disk-management-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2025-06-12
fetch_date: 2025-10-06T22:49:33.459529
---

# Deploying disk management using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Deploying disk management using Blueprints in Jamf Pro

## Deploying disk management using Blueprints in Jamf Pro

June 11, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of Apple’s discussion of Declarative Device Management (DDM) at WWDC 2024, Apple announced that DDM management on macOS 15 Sequoia and later now included [the ability to allow or block external and network storage](https://support.apple.com/guide/deployment/storage-management-declarative-configuration-dep2b9f009ed/web). You can manage the following:

* External storage devices
* Network storage

The following [mount policies can be specified for both external and network storage](https://developer.apple.com/documentation/devicemanagement/diskmanagementsettingsrestrictionsobject):

* **Allowed**: The system can mount storage that’s read-write or read-only.
* **Read-only**: The system can only mount read-only storage. Storage that is read-write is not mounted read-only.
* **Disallowed**: The system can’t mount any external storage.

**Note**: The read-only options are for mounting storage which is already read-only. If macOS can detect that the storage is read-write when it tries to mount the storage in question, macOS won’t mount the storage and will display an error message.

[Jamf Pro’s Blueprints](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Jamf_Pro_Blueprints_Configuration_Guide.html) supports deploying and managing these disk management controls via the [Disk management policy component](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Blueprint_Builder.html). Let’s see how this looks, using the following example:

**Goal**

Block network storage from mounting

For more details, please see below the jump.

I can set up a Blueprint in Jamf Pro to deploy this network storage management configuration using the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click the **Open** button for **Install disk management settings**.

[![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.21.png?w=595)](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.21.png)

4. Give it a name when prompted. For this example, I’m using **Block Network Storage**.

[![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.22.png?w=595)](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.22.png)

5. Select a Jamf Pro smart or static group. For this example, I’m selecting a static group named **Disk Management Deployment Group**.

[![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.24.png?w=595)](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.24.png)

6. In the **Disk Management Policy** section, select the following settings:

* Click the checkbox for **Network storage**.
* Click the button for **Disallowed**.

7. Once all the information has been entered and verified to be correct, click the **Save** button.

[![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.27.png?w=595)](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.27.png)

Once everything has been configured, Jamf Pro should inform you that you have undeployed changes. Click the **Deploy** button to deploy the changes to the Macs you want to manage.

[![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.28.png?w=595)](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.28.png)

Once deployed, the Blueprints screen in Jamf Pro should show the newly-created **Block Network Storage** Blueprint as being deployed.

[![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.29.png?w=595)](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.29.png)

On your managed devices, you can verify that the new service background task configuration has been deployed by clicking on the enrollment profile, then scrolling to the bottom. In the case of this example, you should see a **Device Declarations** section with a listing for **Disk Management**.

[![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.31.43am.png?w=595)](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.31.43am.png)

If you click on the **Disk Management** listing, it should report the following:

* **Network Storage Restriction: Not Allowed**

[![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.31.52am.png?w=595)](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.31.52am.png)

You can verify that the network storage restriction is working by running the following test:

1. Connect to a network storage server.

[![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.33.07am.png)](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.33.07am.png)

2. Log in using your credentials.

[![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.33.31am.png)](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.33.31am.png)

3. When the server presents the list of available network storage shares, select one your user account should have access to.

[![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.34.09am.png)](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.34.09am.png)

If the network storage restriction is working, you should receive an error when macOS tries to mount the network share. This is because the network storage restriction is acting at the time when macOS is trying to mount the network share.

[![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.37.04am.png)](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-11-at-11.37.04am.png)

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/06/11/deploying-disk-management-using-blueprints-in-jamf-pro/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/06/11/deploying-disk-management-using-blueprints-in-jamf-pro/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/06/11/deploying-disk-management-using-blueprints-in-jamf-pro/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/06/11/deploying-disk-management-using-blueprints-in-jamf-pro/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/06/11/deploying-disk-management-usi...
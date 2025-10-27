---
title: Managing Safari bookmarks on macOS Tahoe using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2025/09/16/managing-safari-bookmarks-on-macos-tahoe-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2025-09-17
fetch_date: 2025-10-02T20:14:11.684466
---

# Managing Safari bookmarks on macOS Tahoe using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Safari](https://derflounder.wordpress.com/category/safari/) > Managing Safari bookmarks on macOS Tahoe using Blueprints in Jamf Pro

## Managing Safari bookmarks on macOS Tahoe using Blueprints in Jamf Pro

September 16, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the management options Jamf Pro provides with Blueprints for macOS Tahoe is using DDM declarations to [manage the bookmarks](https://developer.apple.com/documentation/devicemanagement/safaribookmarks) which can used by [Apple’s Safari web browser](https://www.apple.com/safari/). Let’s see how this works using by distributing the following links as Safari bookmarks:

* Company Name Intranet: <https://intranet.company.com>
* Company Name Developer Site: <https://developer.company.com>
* Company Name Travel: <https://travel.company.com>

For more details, please see below the jump.

Safari bookmarks can be managed using DDM declarations at the user level, which like with user-level MDM profiles, means that they can be applied only to [MDM-managed users](https://derflounder.wordpress.com/2025/04/04/identifying-mdm-managed-user-accounts-on-macos-sequoia/). When dealing with local accounts, this means that only the local user account which installs the MDM enrollment profile becomes the MDM-managed user. For our purposes here, this means that Safari bookmark management declarations can only be applied to the MDM-managed user and any other local accounts on the Mac cannot have their Safari bookmarks managed.

As of Jamf Pro 11.20.1, there is not a Blueprints template available for creating blueprints which manage Safari bookmarks so the blueprint will need to be configured manually. To do this, use the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click the **Create blueprint** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-11-at-8.04.png?w=595 "Screenshot 2025-09-11 at 8.04.png")

4. Give it a name when prompted and click the **Create** button. For this example, I’m using **Safari Bookmarks**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-11-at-8.05.png?w=595 "Screenshot 2025-09-11 at 8.05.png")

5. You should see an unconfigured Blueprint. Scroll down in the list on the right-hand side of the browser window to locate the **Safari bookmarks** component.

6. Click on the Safari bookmarks component and drag the **Safari bookmarks** component to the Declaration group section.

![Drag safari component.](https://derflounder.wordpress.com/wp-content/uploads/2025/09/drag_safari_component.gif?w=595 "drag_safari_component.gif")

7. Mouse over the **Safari bookmarks** component and you will see a **Configure** button appear. Click the **Configure** button.

![Configure safari component.](https://derflounder.wordpress.com/wp-content/uploads/2025/09/configure_safari_component.gif?w=595 "configure_safari_component.gif")

8. At this point, you will see an **Managed Bookmarks** section without any listed bookmarks. Click the **Add bookmark group** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-11-at-8.11.png?w=595 "Screenshot 2025-09-11 at 8.11.png")

9. To add the settings for the Safari bookmarks in this example, set the following entries as follows:

* Title: **Company Name**
* Group identifier: **875D8D76-20EE-43DB-B874-9FC9F1CCC3A9**

**Note:** The **Group identifier** field can be any unique string and the only thing that matters is that it is unique. Acceptable unique strings include the following:

* **875D8D76-20EE-43DB-B874-9FC9F1CCC3A9**
* **Finance Department Bookmarks**
* **Man I Love Donuts Especially Those With Chocolate Frosting**

If the string is not unique, the bookmarks which have a not-unique group identifier will be composited together into one set of bookmarks.

Bookmarks:

* Company Name Intranet: <https://intranet.company.com>
* Company Name Developer Site: <https://developer.company.com>
* Company Name Travel: <https://travel.company.com>

10. Once all the settings choices have been made and verified, click the **Add group** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-11-at-8.14.png?w=595 "Screenshot 2025-09-11 at 8.14.png")

11. If everything looks right, click the **Save** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-11-at-8.14.32-am.png?w=595 "Screenshot 2025-09-11 at 8.14.32 AM.png")

12. At this point, you should have a blueprint which has all settings configured but where no target scope has been set. To scope this blueprint, go to the **Scope** section and click the arrow button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-11-at-8.14.43-am.png?w=595 "Screenshot 2025-09-11 at 8.14.43 AM.png")

13. Select a Jamf Pro smart or static group. For this example, I’m selecting a static group named **Safari Bookmarks Deployment Group**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-11-at-8.16.png?w=595 "Screenshot 2025-09-11 at 8.16.png")

14. Once everything has been configured, click the **Deploy** button to deploy the changes to the Macs you want to manage.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-11-at-8.16-1.png?w=595 "Screenshot 2025-09-11 at 8.16.png")

Once deployed, the Blueprints screen in Jamf Pro should show the newly-created **Safari Bookmarks** blueprint as being deployed.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-11-at-8.16-2.png?w=595 "Screenshot 2025-09-11 at 8.16.png")

On your managed devices, you can verify that the new Safari bookmark configuration has been deployed by clicking on the enrollment profile, then scrolling to the bottom.

In the case of this example, you should see a **User Declarations** section with a listing for **Safari Bookmarks**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-11-at-8.18.36am.png?w=595 "Screenshot 2025-09-11 at 8.18.36 AM.png")

If you click on the **Safari Bookmarks** listing, it should report the following:

**Present**

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-11-at-8.18.43am.png?w=595 "Screenshot 2025-09-11 at 8.18.43 AM.png")

You should also be able to open Safari and verify that the desired bookmarks are appearing in Safari’s **Bookmarks** menu.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-11-at-8.22.png?w=595 "Screenshot 2025-09-11 at 8.22.png")

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/09/16/managing-safari-bookmarks-on-macos-tahoe-using-blueprints-in-jamf-pro/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/09/16/managing-safari-bookmarks-on-macos-tahoe-using-blueprints-in-jamf-pro/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/09/16/managing-safari-bookm...
---
title: Managing Safari settings on macOS Tahoe using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2025/09/17/managing-safari-settings-on-macos-tahoe-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2025-09-18
fetch_date: 2025-10-02T20:17:47.152805
---

# Managing Safari settings on macOS Tahoe using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Safari](https://derflounder.wordpress.com/category/safari/) > Managing Safari settings on macOS Tahoe using Blueprints in Jamf Pro

## Managing Safari settings on macOS Tahoe using Blueprints in Jamf Pro

September 17, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the management options Jamf Pro provides with Blueprints for macOS Tahoe is using [DDM declarations to manage settings](https://developer.apple.com/documentation/devicemanagement/safarisettings) which can used by [Apple’s Safari web browser](https://www.apple.com/safari/). Let’s see how this works using by distributing the following Safari settings:

* Allow History Clearing: Set to **false**, to disable clearing history in Safari.
* Allow Private Browsing: Set to **false**, to disable private browsing in Safari.

For more details, please see below the jump.

Safari settings can be managed using DDM declarations at the user level, which like with user-level MDM profiles, means that they can be applied only to [MDM-managed users](https://derflounder.wordpress.com/2025/04/04/identifying-mdm-managed-user-accounts-on-macos-sequoia/). When dealing with local accounts, this means that only the local user account which installs the MDM enrollment profile becomes the MDM-managed user. For our purposes here, this means that Safari bookmark management declarations can only be applied to the MDM-managed user and any other local accounts on the Mac cannot have their Safari settings managed.

As of Jamf Pro 11.20.1, there is not a Blueprints template available for creating blueprints which manage Safari settings so the blueprint will need to be configured manually. To do this, use the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click the **Create blueprint** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-13-at-2.18.png?w=595 "Screenshot 2025-09-13 at 2.18.png")

4. Give it a name when prompted and click the **Create** button. For this example, I’m using **Safari Settings**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-13-at-2.18-1.png?w=595 "Screenshot 2025-09-13 at 2.18.png")

5. You should see an unconfigured Blueprint. Scroll down in the list on the right-hand side of the browser window to locate the **Safari settings** component.

6. Click on the **Safari settings** component and drag the **Safari settings** component to the Declaration group section.

![Drag safari settings.](https://derflounder.wordpress.com/wp-content/uploads/2025/09/drag_safari_settings.gif?w=595 "drag_safari_settings.gif")

7. Mouse over the **Safari settings** component and you will see a **Configure** button appear. Click the **Configure** button.

![Configure safari settings.](https://derflounder.wordpress.com/wp-content/uploads/2025/09/configure_safari_settings.gif?w=595 "configure_safari_settings.gif")

8. To add the settings for the Safari settings in this example, set the following settings as follows:

* **History clearing**: Set to **Disallowed**
* **Private browsing**: Set to **Disallowed**

9. Once all the settings choices have been made and verified, click the **Add** button.

**![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-13-at-2.20.png?w=595 "Screenshot 2025-09-13 at 2.20.png")**

10. At this point, you should have a blueprint which has all settings configured but where no target scope has been set. To scope this blueprint, go to the **Scope** section and click the arrow button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-13-at-2.21.png?w=595 "Screenshot 2025-09-13 at 2.21.png")

11. Select a Jamf Pro smart or static group. For this example, I’m selecting a static group named **Safari Settings Deployment Group**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-13-at-2.21-1.png?w=595 "Screenshot 2025-09-13 at 2.21.png")

14. Once everything has been configured, click the **Deploy** button to deploy the changes to the Macs you want to manage.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-13-at-2.21.52-pm.png?w=595 "Screenshot 2025-09-13 at 2.21.52 PM.png")

Once deployed, the Blueprints screen in Jamf Pro should show the newly-created **Safari Settings** blueprint as being deployed.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-13-at-2.22.png?w=595 "Screenshot 2025-09-13 at 2.22.png")

On your managed devices, you can verify that the new Safari settings management configuration has been deployed by clicking on the enrollment profile, then scrolling to the bottom.

In the case of this example, you should see a **User Declarations** section with a listing for **Safari Settings**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-13-at-2.24.00pm.png?w=595 "Screenshot 2025-09-13 at 2.24.00 PM.png")

If you click on the **Safari Settings** listing, it should report the following:

* Allow History Clearing: No
* Allow Private Browsing: No

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-13-at-2.24.08pm.png?w=595 "Screenshot 2025-09-13 at 2.24.08 PM.png")

You should also be able to open Safari and verify that the desired settings are being applied by trying to [clear Safari’s history](https://support.apple.com/105082) and [opening a private window](https://help.apple.com/safari/mac/8.0/en.lproj/ibrw1069.html).

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-13-at-2.31.png?w=595 "Screenshot 2025-09-13 at 2.31.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-13-at-2.32.png?w=595 "Screenshot 2025-09-13 at 2.32.png")

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/09/17/managing-safari-settings-on-macos-tahoe-using-blueprints-in-jamf-pro/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/09/17/managing-safari-settings-on-macos-tahoe-using-blueprints-in-jamf-pro/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/09/17/managing-safari-settings-on-macos-tahoe-using-blueprints-in-jamf-pro/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/09/17/managing-safari-settings-on-macos-tahoe-using-blueprints-in-jamf-pro/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/09/17/managing-safari-settings-on-macos-tahoe-using-blueprints-in-jamf-pro/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/09/17/managing-safari-settings-on-macos-tahoe-using-blueprints-in-jamf-pro/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/09/17/managing-safari-settings-on-macos-tahoe-using-blueprints-in-jamf-pro/?share=tumblr)
* [Click t...
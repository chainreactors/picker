---
title: Managing time limited admin rights with Privileges 2.x
url: https://derflounder.wordpress.com/2024/11/21/managing-time-limited-admin-rights-with-privileges-2-x/
source: Der Flounder
date: 2024-11-22
fetch_date: 2025-10-06T19:15:17.061827
---

# Managing time limited admin rights with Privileges 2.x

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Privileges.app](https://derflounder.wordpress.com/category/privileges-app/) > Managing time limited admin rights with Privileges 2.x

## Managing time limited admin rights with Privileges 2.x

November 21, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the new features in Privileges 2.x is the unified ability to set and manage how long you want to grant admin rights, where running Privileges grants admin rights for a defined amount of time and then those admin rights are taken away. This ability had also existed in Privileges 1.x but [it was exclusively tied to Privileges 1.x’s Toggle Privileges function](https://derflounder.wordpress.com/2022/07/22/privileges-app-and-time-limited-admin/), where in Privileges 2.x it is available no matter how Privileges is being run.

By default, [Privileges 2.x will grant administrator rights for 20 minutes if not configured otherwise](https://github.com/SAP/macOS-enterprise-privileges/wiki/Frequently-Asked-Questions#by-default-is-there-a-time-limit-on-the-admin-rights-granted-by-privileges).

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-20-at-3.37.21e280afpm-1.png?w=491&h=600 "Screenshot 2024-11-20 at 3.37.21 PM.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-20-at-3.40.01e280afpm-1.png?w=595 "Screenshot 2024-11-20 at 3.40.01 PM.png")

But what if you want to configure it otherwise? There are management options available for this. For more details, please see below the jump.

The relevant [preference domain and key values](https://github.com/SAP/macOS-enterprise-privileges/wiki/Managing-Privileges) are listed below:

* Preference domain: **corp.sap.privileges**
* Key: **ExpirationInterval**
* Value: Positive Integer

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <dict> |
|  | <key>ExpirationInterval</key> |
|  | <integer>15</integer> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/614ac1b7a92d02032d87607eafc3ec73/raw/cffb7368e39a3344cd43acaa69c474d57ff7c323/corp.sap.privileges.plist)
 [corp.sap.privileges.plist](https://gist.github.com/rtrouton/614ac1b7a92d02032d87607eafc3ec73#file-corp-sap-privileges-plist)
hosted with ❤ by [GitHub](https://github.com)

* Preference domain: **corp.sap.privileges**
* Key: **ExpirationIntervalMax**
* Value: Positive Integer

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <dict> |
|  | <key>ExpirationIntervalMax</key> |
|  | <integer>20</integer> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/ddce0e24e3b8aeba0f0a6139549893c3/raw/043b8762027422cb9995ba9be133788c8befdaac/corp.sap.privileges.plist)
 [corp.sap.privileges.plist](https://gist.github.com/rtrouton/ddce0e24e3b8aeba0f0a6139549893c3#file-corp-sap-privileges-plist)
hosted with ❤ by [GitHub](https://github.com)

**Note:** In both cases, the positive integer values are defining time in minutes.

**ExpirationInterval**:

The **ExpirationInterval** key defines a set time in minutes after which administrator rights expire and the logged-in user reverts to using standard user rights. For example, setting **ExpirationInterval** to a value of 15 would set Privileges to allow admin rights for fifteen minutes. Once the fifteen minutes are up, the logged-in user reverts to using standard user rights.

In this example, the **Administrator privileges expire** setting in the Privileges settings would be set to the defined value and grayed out.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-21-at-8.22.27e280afam.png?w=491&h=600 "Screenshot 2024-11-21 at 8.22.27 AM.png")

**Note**: Setting a value of **0** disables the timeout and allows the user to request administrator privileges which do not expire.

**ExpirationIntervalMax**:

The **ExpirationIntervalMax** key defines a set time in minutes after which administrator rights expire and the logged-in user reverts to using standard user rights. In general, this works like the **ExpirationInterval** key but it allows the logged-in user to choose a timeout value which is different as long it does not exceed the defined value.

For example, setting **ExpirationIntervalMax** to a value of 20 would set Privileges to allow admin rights for twenty minutes. However, the logged-in user can go into the Privileges settings and set a different time interval for the **Administrator privileges expire** setting as long as that time interval does not exceed the defined value of twenty minutes.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-21-at-8.23.png?w=492&h=600 "Screenshot 2024-11-21 at 8.23.png")

**Note**: In the event that both the **ExpirationInterval** and **ExpirationIntervalMax** settings are set, as of Privileges 2.0 the **ExpirationInterval** behavior will be applied. The **Administrator privileges expire** setting in the Privileges settings would be set to the defined value for **ExpirationInterval** and be grayed out.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-21-at-8.22.27e280afam.png?w=491&h=600 "Screenshot 2024-11-21 at 8.22.27 AM.png")

The **ExpirationInterval** and **ExpirationIntervalMax** settings can be managed by configuration profiles. Please see below for example profiles.

**ExpirationInterval**:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1"> |
|  | <dict> |
|  | <key>PayloadUUID</key> |
|  | <string>B3D51AB8-3307-4CBA-B5B7-0CB590D62797</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>B3D51AB8-3307-4CBA-B5B7-0CB590D...
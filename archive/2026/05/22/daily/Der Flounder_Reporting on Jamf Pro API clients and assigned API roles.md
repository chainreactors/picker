---
title: Reporting on Jamf Pro API clients and assigned API roles
url: https://derflounder.wordpress.com/2026/05/22/13403/
source: Der Flounder
date: 2026-05-22
fetch_date: 2026-05-23T05:38:48.206237
---

# Reporting on Jamf Pro API clients and assigned API roles

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Jamf Pro Classic API](https://derflounder.wordpress.com/category/jamf-pro-classic-api/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Reporting on Jamf Pro API clients and assigned API roles

## Reporting on Jamf Pro API clients and assigned API roles

May 22, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

While working with Jamf Pro’s API options, I’ve started using [API clients](https://learn.jamf.com/r/en-US/jamf-pro-documentation-current/API_Roles_and_Clients) more often for my authentication needs. The reason is that I can control how long an API client’s authentication token is valid for, which is very useful from a security point of view.

My practice has been to set them up on a per-task basis, which I’ve found can lead to an increasing number of API clients. At the same time, for auditing purposes, it’s useful to know which API clients are using which API roles as API roles determine the permissions that the API clients have.

To help me keep track of this, I’ve written a script which reports the following:

• The current list of the enabled and disabled API clients on a Jamf Pro server
• Which API roles are being used by the API clients.

For more details, please see below the jump.

The script is named **API\_Client\_Role\_Reporting.sh** and is available via the link below:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/Casper_Scripts/API_Client_Role_Reporting>

This script connects to the Jamf Pro API on a Jamf Pro server and reports which API clients are assigned to which API client roles.

Three items are required to use this script:

* The URL of the appropriate Jamf Pro server.
* An API client on the Jamf Pro server with sufficient privileges to read the necessary information from the Jamf Pro API.
* The client secret for the relevant API client on the Jamf Pro server.

If setting up an API client with limited rights, here are the required API role privileges for the API client on the Jamf Pro server:

* **Read API Integrations**
* **Read API Roles**

In this example, I have the following API roles set up on a Jamf Pro server:

![](https://derflounder.wordpress.com/wp-content/uploads/2026/05/screenshot-2026-05-22-at-1.05.png?w=595 "Screenshot 2026-05-22 at 1.05.png")

In turn, the following API clients have been also set up and assigned to those API roles:

![](https://derflounder.wordpress.com/wp-content/uploads/2026/05/screenshot-2026-05-22-at-1.05-1.png?w=595 "Screenshot 2026-05-22 at 1.05.png")

With the example conditions, you should see similar output to what’s shown below when using the **API\_Client\_Role\_Reporting.sh** script to generate a report:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /Users/username/API\_Client\_Role\_Reporting.sh |
|  | Please enter your Jamf Pro server URL : <https://jamf.pro.server.here> |
|  | Please enter your Jamf Pro API client ID : ab087cea-f1f3-4953-a452-21454713da5f |
|  | Please enter the API client secret for the ab087cea-f1f3-4953-a452-21454713da5f API ID client: |
|  | Report being generated. File location will appear below once ready. |
|  | Report available here: /var/folders/ps/2\_yw29gj711c9d7c5w5jhyv80000gp/T/tmp.G1KXv6fEpZ.tsv |
|  |  |
|  | Client Name Client ID Enabled Assigned Role |
|  | ReadComputerSearches 3e8ca82c-b4c2-48f3-90fc-fcb637a6c845 false Read Advanced Computer Searches |
|  | ReadMobileDevices 605c3677-7c46-46e9-9c91-10e99a7f296c true Read Mobile Devices |
|  | API\_mapping ab087cea-f1f3-4953-a452-21454713da5f true Read API Integrations and Roles |
|  | ReadComputers 5789b2e1-6f70-41b8-8ec2-65a478c53aef true Read Computers |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/af684181a7e0f33c35f07d2a447c017a/raw/7a468858ea9e54b26a64f3eb34bab582b1369e0d/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/af684181a7e0f33c35f07d2a447c017a#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

As part of the script’s run, a report will be generated and you’ll be notified of where it is stored. The report will be in [TSV format](https://en.wikipedia.org/wiki/Tab-separated_values) and appear similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  | Client Name | Client ID | Enabled | Assigned Role |
| --- | --- | --- | --- | --- |
|  | ReadComputerSearches | 3e8ca82c-b4c2-48f3-90fc-fcb637a6c845 | false | Read Advanced Computer Searches |
|  | ReadMobileDevices | 605c3677-7c46-46e9-9c91-10e99a7f296c | true | Read Mobile Devices |
|  | API\_mapping | ab087cea-f1f3-4953-a452-21454713da5f | true | Read API Integrations and Roles |
|  | ReadComputers | 5789b2e1-6f70-41b8-8ec2-65a478c53aef | true | Read Computers |

[view raw](https://gist.github.com/rtrouton/4c04d2864834d25e7a22ca82d4707f33/raw/bc3289c671d36bec3bea9f47b3af95d7b42ffd07/tmp.G1KXv6fEpZ.tsv)
 [tmp.G1KXv6fEpZ.tsv](https://gist.github.com/rtrouton/4c04d2864834d25e7a22ca82d4707f33#file-tmp-g1kxv6fepz-tsv)
hosted with ❤ by [GitHub](https://github.com)

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/05/22/13403/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/05/22/13403/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/05/22/13403/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/05/22/13403/?share=reddit)
* [Share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2026/05/22/13403/?share=twitter)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2026/05/22/13403/?share=pinterest)
* [Share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2026/05/22/13403/?share=tumblr)

Like Loading...

### *Related*

Categories: [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Jamf Pro Classic API](https://derflounder.wordpress.com/category/jamf-pro-classic-api/), [Scripting](https://derflounder.wordpress.com/category/scripting/)

Comments (2)
[Leave a comment](#respond)

1. ![staze's avatar](https://1.gravatar.com/avatar/dff8e942e5e58ae5de0868fc4fc2d6f437ac8113bb8e2956a5b990e06d52b422?s=32&d=identicon&r=G)

   staze

   May 22, 2026 at 9:14 pm

   [Reply](https://derflounder.wordpress.com/2026/05/22/13403/?replytocom=72891#respond)

   Wow, thanks Rich! I had this on my list to do because turns out, the Jamf API Client GUI has a bug where if you have more than 100 roles, the Client GUI stops showing you the 101+ roles to pick from. So we have single purpos...
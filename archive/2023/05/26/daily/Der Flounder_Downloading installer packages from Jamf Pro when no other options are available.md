---
title: Downloading installer packages from Jamf Pro when no other options are available
url: https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/
source: Der Flounder
date: 2023-05-26
fetch_date: 2025-10-04T11:36:38.385324
---

# Downloading installer packages from Jamf Pro when no other options are available

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/) > Downloading installer packages from Jamf Pro when no other options are available

## Downloading installer packages from Jamf Pro when no other options are available

May 25, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Every so often, Mac admins who administer Jamf Pro may run into a situation like this:

1. They need an installer package For Reasons.
2. That installer package is only stored on their Jamf Pro server.
3. They don’t have access to the distribution point which stores their Jamf Pro server’s installer packages.

In a situation like this, you can use a Jamf Pro policy to provide the installer to a specified Mac. For more details, please see below the jump.

To enable downloading an installer to a specified Mac using Jamf Pro, use the following procedure.

1. Create a policy in Jamf Pro.

![Screenshot 2023 05 25 at 3 22 50 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/05/screenshot-2023-05-25-at-3.22.50-pm.png?w=599&h=375 "Screenshot 2023-05-25 at 3.22.50 PM.png")

2. Add the installer package to the policy.

3. Set the installer package’s **Action** to **Cache**.

![Screenshot 2023 05 25 at 3 21 46 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/05/screenshot-2023-05-25-at-3.21.46-pm.png?w=600&h=337 "Screenshot 2023-05-25 at 3.21.46 PM.png")

Set policy trigger and scoping as preferred.

Once the policy runs on the Mac(s) it’s scoped to run on, Jamf Pro will download the installer package to the following directory on the Mac(s):

**/Library/Application Support/JAMF/Waiting Room**

Note: The **Waiting Room** directory is only accessible using root privileges.

Once the policy finishes running, you can collect the downloaded installer from **/Library/Application Support/JAMF/Waiting Room**.

![Screenshot 2023 05 25 at 4 33 12 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/05/screenshot-2023-05-25-at-4.33.12-pm.png?w=598&h=195 "Screenshot 2023-05-25 at 4.33.12 PM.png")

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/?share=pocket)

Like Loading...

### *Related*

Categories: [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/)

Comments (6)
[Leave a comment](#respond)

1. ![atombomb13's avatar](https://0.gravatar.com/avatar/0ca6aa21495ea12eb5571b5c94c008f2b42ed5a21e7ba50c305d041217069e9a?s=32&d=identicon&r=G)

   [atombomb13](https://gravatar.com/atombomb13)

   May 26, 2023 at 12:13 am

   [Reply](https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/?replytocom=71042#respond)

   Thanks, Rich. This is helpful 🙂
2. ![Michael Crispin's avatar](https://0.gravatar.com/avatar/f879c22a2bb869e7deee236212d7fabe577a96a1f049e62314d3d963f169ffc3?s=32&d=identicon&r=G)

   Michael Crispin

   May 26, 2023 at 12:55 am

   [Reply](https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/?replytocom=71043#respond)

   The other useful technique here is to use Jamf Admin (the app), and drag a folder in the left side window. Then highlight said folder, and you will see a button on the bottom left to “Replicate” and then you can have a local copy of all your assets.

   * ![JimH's avatar](https://0.gravatar.com/avatar/0d9fc2941d8345a24698caec63dd202dedcfc885b14e4382945cb8ebf1f88d15?s=32&d=identicon&r=G)

     JimH

     May 26, 2023 at 1:18 pm

     [Reply](https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/?replytocom=71049#respond)

     Michael, if you’re on-premise, you’re over engineering things if you only need one package. When Jamf Admin is open with the drive mounted, open /Volumes. There you will find the smb share and can navigate to the pkg you need. I have no experience with Jamf Cloud so I can’t speak to that.
3. ![Andreas Schenk's avatar](https://0.gravatar.com/avatar/96b9d5e789b40d35815d4a27edfbbe6df8e5f22b5ce289a8248b46930ff64fc1?s=32&d=identicon&r=G)

   Andreas Schenk

   May 26, 2023 at 5:09 am

   [Reply](https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/?replytocom=71047#respond)

   While this is a good addition in tools/workflows, I have been using Jamf CPR with the „save only“ option in these situations. Then you don’t need a policy.
   And probably it would be good, if the GUI just had a download button for each pkg.(I think there is a feature request for this, that we all should upvote)
4. ![Sander's avatar](https://1.gravatar.com/avatar/108aac6533ddd684c53de902a05c6fe2f0e9711c468c392aaf9307fff22593af?s=32&d=identicon&r=G)

   Sander

   May 26, 2023 at 5:55 am

   [Reply](https://derflounder.wordpress.com/2023/05/25/downloading-installer-packages-from-jamf-pro-when-no-other-options-are-available/?replytocom=71048#respond)

   If you use the Jamf Cloud distribution point you can also use the following trick:

   1) Create a policy similar to your policy example, but add a custom trigger to it. In my example i use the trigger office365

   2) Open the terminal on a client device that is scoped to the policy

   3) In the terminal, run the policy with the custom trigger in verbose mode

   user@Macbook ~ % sudo jamf policy -trigger office365 verbose
   Checking for policies triggered by “office365” for user “user”…
   Executing Policy Microsoft Office 365 Business Pro – Install
   Downloading Microsoft Office Business Pro Suite-16.72.0.pkg…
   Downloading <https://euc1-jcds.services.jamfcloud.com//download/a28e865336904d1197154f168d767530/Microsoft%20Office%20Business%20Pro%20Suite-16.72.0.pkg?token=173d5759c1a54ad0bcdd2af1a5b3d8...
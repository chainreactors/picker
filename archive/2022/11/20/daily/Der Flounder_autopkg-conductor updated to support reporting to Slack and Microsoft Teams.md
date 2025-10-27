---
title: autopkg-conductor updated to support reporting to Slack and Microsoft Teams
url: https://derflounder.wordpress.com/2022/11/19/autopkg-conductor-updated-to-support-reporting-to-slack-and-microsoft-teams/
source: Der Flounder
date: 2022-11-20
fetch_date: 2025-10-03T23:16:22.820183
---

# autopkg-conductor updated to support reporting to Slack and Microsoft Teams

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [AutoPkg](https://derflounder.wordpress.com/category/autopkg/), [autopkg-conductor](https://derflounder.wordpress.com/category/autopkg-conductor/), [macOS](https://derflounder.wordpress.com/category/macos/), [Microsoft Teams](https://derflounder.wordpress.com/category/microsoft-teams/), [Scripting](https://derflounder.wordpress.com/category/scripting/), [Slack](https://derflounder.wordpress.com/category/slack/) > autopkg-conductor updated to support reporting to Slack and Microsoft Teams

## autopkg-conductor updated to support reporting to Slack and Microsoft Teams

November 19, 2022
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

When the **autopkg-conductor** tool was first written, one of its primary functions was to send the output of JSSImporter to a Slack channel. With [JSSImporter being deprecated](https://github.com/jssimporter/JSSImporter/wiki) in favor of [JamfUploader](https://github.com/grahampugh/jamf-upload/wiki/JamfUploader-AutoPkg-Processors), I’ve decided to do the following:

1. Drop support for **JSSImporter**.
2. Add additional reporting options for **JamfUploader**.

As of the current version to the tool, **autopkg-conductor** can send output from **JamfUploader** to the following:

* [Slack](https://en.wikipedia.org/wiki/Slack_%28software%29)
* [Microsoft Teams](https://en.wikipedia.org/wiki/Microsoft_Teams)

For more details, please see below the jump.

**autopkg-conductor** can now be configured to send output to Slack, Teams or to both Slack and Teams. The following AutoPkg processors are being leveraged for this:

* [Slack](https://en.wikipedia.org/wiki/Slack_%28software%29): **JamfUploaderSlacker**
* [Microsoft Teams](https://en.wikipedia.org/wiki/Microsoft_Teams): **JamfUploaderTeamsNotifier**

To configure **autopkg-conductor** to send to Slack using the **JamfUploaderSlacker** AutoPkg processor, the following variables need to be configured:

* **slack\_post\_processor**
* **slack\_webhook**

To configure **autopkg-conductor** to send to Teams using the **JamfUploaderTeamsNotifier** AutoPkg processor, the following variables need to be configured:

* **teams\_post\_processor**
* **teams\_webhook**

To configure **autopkg-conductor** to send to both Slack and Teams, all four variables need to be configured:

* **slack\_post\_processor**
* **slack\_webhook**
* **teams\_post\_processor**
* **teams\_webhook**

![Screenshot 2022 11 19 at 3 35 15 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/11/screenshot-2022-11-19-at-3.35.15-pm.png?w=595 "Screenshot 2022-11-19 at 3.35.15 PM.png")

Both the **JamfUploaderSlacker** and the **JamfUploaderTeamsNotifier** AutoPkg processors should be included with JamfUploader. The message which appears in Slack should look similar to what is shown below:

![Screenshot 2022 11 19 at 2 50 14 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/11/screenshot-2022-11-19-at-2.50.14-pm.png?w=595 "Screenshot 2022-11-19 at 2.50.14 PM.png")

The message which appears in Teams should look similar to what is shown below:

![Screenshot 2022 11 19 at 2 46 31 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/11/screenshot-2022-11-19-at-2.46.31-pm.png?w=595 "Screenshot 2022-11-19 at 2.46.31 PM.png")

Error logs should also be sent to Slack and/or Teams. There will be differences in appearance, as the script sends the error log one line at a time. Slack and Teams handle this differently in terms of formatting, so the error logs should appear similar to what’s shown below:

**Slack:**

![Screenshot 2022 11 19 at 2 54 09 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/11/screenshot-2022-11-19-at-2.54.09-pm.png?w=595 "Screenshot 2022-11-19 at 2.54.09 PM.png")

**Teams:**

![Screenshot 2022 11 19 at 2 53 37 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/11/screenshot-2022-11-19-at-2.53.37-pm.png?w=595 "Screenshot 2022-11-19 at 2.53.37 PM.png")

The **autopkg-conductor** script is available below. It’s also available from GitHub using the following link:

<https://github.com/rtrouton/autopkg-conductor>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | # AutoPkg automation script |
|  |  |
|  | # Adjust the following variables for your particular configuration. |
|  | # |
|  | # autopkg\_user\_account – This should be the user account you're running AutoPkg in. |
|  | # autopkg\_user\_account\_home – This should be the home folder location of the AutoPkg user account |
|  | # |
|  | # Note: The home folder location is currently set to be automatically discovered |
|  | # using the autopkg\_user\_account variable. |
|  | # |
|  | # recipe\_list – This is the location of the plain text file being used to store |
|  | # your list of AutoPkg recipes. For more information about this list, please see |
|  | # the link below: |
|  | # |
|  | # <https://github.com/autopkg/autopkg/wiki/Running-Multiple-Recipes> |
|  | # |
|  | # log\_location – This should be the location and name of the AutoPkg run logs. |
|  | # |
|  | # Note: The location is currently set to be automatically discovered |
|  | # using the autopkg\_user\_account\_home variable. |
|  |  |
|  | autopkg\_user\_account="username\_goes\_here" |
|  | autopkg\_user\_account\_home=$(/usr/bin/dscl . -read /Users/"$autopkg\_user\_account" NFSHomeDirectory | awk '{print $2}') |
|  | recipe\_list="/path/to/recipe\_list.txt" |
|  | log\_location="$autopkg\_user\_account\_home/Library/Logs/autopkg-run-for-$(date +%Y-%m-%d-%H%M%S).log" |
|  |  |
|  | # If you're using Jamf Upload, the URL of your Jamf Pro server should be populated into the jamfpro\_server variable automatically. |
|  | # |
|  | # If you're not using Jamf Upload, this variable will return nothing and that's OK. |
|  |  |
|  | jamfpro\_server=$(/usr/bin/defaults read "$autopkg\_user\_account\_home"/Library/Preferences/com.github.autopkg JSS\_URL) |
|  |  |
|  | # Optional variables |
|  |  |
|  | # This script supports using either Jamf Upload's JamfUploaderSlacker or Jamf Upload's JamfUploaderTeamsNotifier processors |
|  |  |
|  | # JamfUploaderSlacker – used with Jamf Upload |
|  | # |
|  | # To use the JamfUploaderSlacker post-processor, you'll need to use add Graham Pugh's |
|  | # Autopkg repo by running the command below: |
|  | # |
|  | # autopkg repo-add grahampugh-recipes |
|  | # |
|  | # The slack\_post\_processor variable should look like this: |
|  | # slack\_post\_processor="com.github.grahampugh.jamf-upload.processors/JamfUploaderSlacker" |
|  |  |
|  | slack\_post\_processor="" |
|  |  |
|  | # JamfUploaderTeamsNotifier – used with Jamf Upload |
|  | # |
|  | # To use the JamfUploaderTeamsNotifier post-processor, you'll need to use add Graham Pugh's |
|  | # Autopkg repo by running the command below: |
|  | # |
|  | # autopkg repo-add grahampugh-recipes |
|  | # |
|  | # The teams\_post\_processor variable should look like this: |
|  | # teams\_post\_processor="com.github.grahampugh.jamf-upload.processors/JamfUploaderTeamsNotifier" |
|  |  |
|  | teams\_post\_processor="" |
|  |  |
|  | # If you're sending the results of your AutoPkg run to Slack, you'll need to set up |
|  | # a Slack webhook to receive the information being sent by the script. |
|  | # If you need ...
---
title: Setting custom variables in AutoPkg using the VariablePlaceholder processor
url: https://derflounder.wordpress.com/2024/08/16/setting-custom-variables-in-autopkg-using-the-variableplaceholder-processor/
source: Der Flounder
date: 2024-08-17
fetch_date: 2025-10-06T18:04:14.895806
---

# Setting custom variables in AutoPkg using the VariablePlaceholder processor

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [AutoPkg](https://derflounder.wordpress.com/category/autopkg/) > Setting custom variables in AutoPkg using the VariablePlaceholder processor

## Setting custom variables in AutoPkg using the VariablePlaceholder processor

August 16, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

A while back, I had written a post about [using custom variables in an AutoPkg recipe to set version information](https://derflounder.wordpress.com/2022/02/22/using-custom-variables-in-an-autopkg-recipe-to-set-version-information/). Part of my earlier post references using the [EndOfCheckPhase processor](https://github.com/autopkg/autopkg/wiki/Processor-EndOfCheckPhase) as a safe way to set variables because the **EndOfCheckPhase** processor takes no actions. However, even the **EndOfCheckPhase** processor isn’t completely safe because it does do something even if the processor itself takes no actions and natively sets no output variables. This is because AutoPkg uses it to figure out if it should stop checking for new information as part of a recipe’s run.

To provide a completely safe way to set custom variables in an AutoPkg recipe, I decided to write a **VariablePlaceholder** AutoPkg processor which truly does absolutely nothing except serve as a convenient way to set custom variables. For more details, please see below the jump.

The **VariablePlaceholder** processor takes no actions and does nothing. It’s usefulness comes from the fact that AutoPkg will still process **Arguments** values if they’re defined for the **VariablePlaceholder** processor. The workflow in this case looks like this:

1. Add the **VariablePlaceholder** processor where needed in the AutoPkg recipe.
2. Perform the desired variable assignment as an **Arguments** value.

For example, if you need to set the **version** output variable in an AutoPkg recipe by combining two other output variables (in this example, a **major\_version** variable and a **minor\_version** variable), the **VariablePlaceholder** processor can be used to do this in a safe way.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <dict> |
|  | <key>Processor</key> |
|  | <string>VariablePlaceholder</string> |
|  | <key>Arguments</key> |
|  | <dict> |
|  | <key>version</key> |
|  | <string>%major\_version%.%minor\_version%</string> |
|  | </dict> |
|  | </dict> |

[view raw](https://gist.github.com/rtrouton/39e5fb60813ac657814bc4929a7cb0c6/raw/40b06a0c0dd812bc8c8d686208738757e6d58cb6/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/39e5fb60813ac657814bc4929a7cb0c6#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

A recipe which uses this example setup is shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <dict> |
|  | <key>Description</key> |
|  | <string>Downloads the latest version of Carousel Cloud's screensaver.</string> |
|  | <key>Identifier</key> |
|  | <string>com.github.rtrouton.download.carouselcloudscreensaver</string> |
|  | <key>Input</key> |
|  | <dict> |
|  | <key>NAME</key> |
|  | <string>Carousel</string> |
|  | <key>DOWNLOAD\_URL</key> |
|  | <string>[https://carousel-public-files.s3.amazonaws.com/Carousel.Cloud.Screen.Saver.dmg</string&gt](https://carousel-public-files.s3.amazonaws.com/Carousel.Cloud.Screen.Saver.dmg%3C/string%26gt); |
|  | </dict> |
|  | <key>MinimumVersion</key> |
|  | <string>1.0.0</string> |
|  | <key>Process</key> |
|  | <array> |
|  | <dict> |
|  | <key>Processor</key> |
|  | <string>URLDownloader</string> |
|  | <key>Arguments</key> |
|  | <dict> |
|  | <key>url</key> |
|  | <string>%DOWNLOAD\_URL%</string> |
|  | </dict> |
|  | </dict> |
|  | <dict> |
|  | <key>Processor</key> |
|  | <string>EndOfCheckPhase</string> |
|  | </dict> |
|  | <dict> |
|  | <key>Arguments</key> |
|  | <dict> |
|  | <key>info\_path</key> |
|  | <string>%pathname%/Carousel Cloud.saver/Contents/Info.plist</string> |
|  | <key>plist\_keys</key> |
|  | <dict> |
|  | <key>CFBundleVersion</key> |
|  | <string>minor\_version</string> |
|  | <key>CFBundleShortVersionString</key> |
|  | <string>major\_version</string> |
|  | </dict> |
|  | </dict> |
|  | <key>Processor</key> |
|  | <string>PlistReader</string> |
|  | </dict> |
|  | <dict> |
|  | <key>Processor</key> |
|  | <string>CodeSignatureVerifier</string> |
|  | <key>Arguments</key> |
|  | <dict> |
|  | <key>input\_path</key> |
|  | <string>%pathname%/Carousel Cloud.saver</string> |
|  | <key>requirement</key> |
|  | <string>identifier "com.trms.Carousel-Cloud-Screensaver" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /\* exists \*/ and certificate leaf[field.1.2.840.113635.100.6.1.13] /\* exists \*/ and certificate leaf[subject.OU] = "3WG65JKLQ8"</string> |
|  | </dict> |
|  | </dict> |
|  | <dict> |
|  | <key>Processor</key> |
|  | <string>com.github.rtrouton.SharedProcessors/VariablePlaceholder</string> |
|  | <key>Arguments</key> |
|  | <dict> |
|  | <key>version</key> |
|  | <string>%major\_version%.%minor\_version%</string> |
|  | </dict> |
|  | </dict> |
|  | <dict> |
|  | <key>Processor</key> |
|  | <string>EndOfCheckPhase</string> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/beb0650cc9af336046ad7c751bcba923/raw/1e2b402ad3e2bfc97f51f710e7e997c8f7b63d7d/CarouselCloudScreenSaver.download.recipe)
 [CarouselCloudScreenSaver.download.recipe](https://gist.github.com/rtrouton/beb0650cc9af336046ad7c751bcba923#file-carouselcloudscreensaver-download-recipe)
hosted with ❤ by [GitHub](https://github.com)

The **VariablePlaceholder** processor is shown below, as well as being available via the following link:

<https://github.com/rtrouton/AutoPkg_Processors/tree/main/VariablePlaceholder>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/usr/local/autopkg/python |
|  | # |
|  | # Licensed under the Apache License, Version 2.0 (the "License"); |
|  | # you may not use this file except in compliance with the License. |
|  | # You may obtain a copy of the License at |
|  | # |
|  | # <http://www.apache.org/licenses/LICENSE-2.0> |
|  | # |
|  | # Unless required by applicable law or agreed to in writing, software |
|  | # distributed under the License is distributed on an "AS IS" BASIS, |
|  | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. |
|  | # See the License for the specific ...
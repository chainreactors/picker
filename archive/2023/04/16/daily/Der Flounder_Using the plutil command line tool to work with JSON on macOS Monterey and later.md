---
title: Using the plutil command line tool to work with JSON on macOS Monterey and later
url: https://derflounder.wordpress.com/2023/04/15/using-the-plutil-command-line-tool-to-work-with-json-on-macos-monterey-and-later/
source: Der Flounder
date: 2023-04-16
fetch_date: 2025-10-04T11:31:55.014252
---

# Using the plutil command line tool to work with JSON on macOS Monterey and later

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Using the plutil command line tool to work with JSON on macOS Monterey and later

## Using the plutil command line tool to work with JSON on macOS Monterey and later

April 15, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the issues Mac admins may face is working with [JSON](https://www.json.org/) files as part of [shell scripting](https://en.wikipedia.org/wiki/Shell_script). There are several solutions to this problem, including using the third-party [jq command line tool](https://stedolan.github.io/jq/) and Apple’s [JavaScript for Automation](https://developer.apple.com/library/archive/releasenotes/InterapplicationCommunication/RN-JavaScriptForAutomation/Articles/Introduction.html#//apple_r) (JXA) interface. For posts on using these solutions, please see the links below:

**jq:**

* <https://sher-chowdhury.medium.com/working-with-json-using-jq-ce06bae5545a>
* <https://codeahoy.com/learn/introtobash/ch15/>
* <https://cameronnokes.com/blog/working-with-json-in-bash-using-jq/>

**JXA:**

* <https://www.macblog.org/posts/how-to-parse-json-macos-command-line/>
* <https://paulgalow.com/how-to-work-with-json-api-data-in-macos-shell-scripts>
* <https://scriptingosx.com/2021/11/the-unexpected-return-of-javascript-for-automation/>

Another available option is to use the [plutil command line tool](https://gist.github.com/rtrouton/4121821daa25ca139db07fe393c40a33) on macOS Monterey and later to do the following:

* Read values from JSON files
* Convert plist files in XML format to JSON

For more details, please see below the jump.

If you want to read JSON values from a file, you can use the **raw** option of **plutil**‘s **-extract** function in some cases to extract values from keys in JSON files. For example, you may have a JSON file with the following keys and values:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | { |
|  | "checkInFrequency": 0, |
|  | "createHooks": false, |
|  | "hookLog": false, |
|  | "hookPolicies": false, |
|  | "createStartupScript": false, |
|  | "startupLog": false, |
|  | "startupPolicies": false, |
|  | "startupSsh": false, |
|  | "enableLocalConfigurationProfiles": false |
|  | } |

[view raw](https://gist.github.com/rtrouton/c3e9c46949d892b1673f1dee31849b44/raw/fe98d060311f64a0231abdecf34655032f978268/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/c3e9c46949d892b1673f1dee31849b44#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You could use the following command to extract the value for the **createStartupScript** key in the JSON file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | plutil -extract createStartupScript raw /path/to/filename.json |

[view raw](https://gist.github.com/rtrouton/10621cf57682edd454b4af9289c64ceb/raw/3bca394778e3a242849b2496bba4699e73cd72d4/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/10621cf57682edd454b4af9289c64ceb#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

In that case, you should see the following output:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % plutil -extract createStartupScript raw filename.json |
|  | false |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/45bfbc9b492b9dda9d129db1c9b3ab67/raw/a08df55066ee07681779580e87df6ff37183e7f0/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/45bfbc9b492b9dda9d129db1c9b3ab67#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

In cases like this, where you’re dealing with a JSON file with a fairly simple format (without arrays or otherwise nested values), **plutil** is a good tool which is built into macOS that you can call on to extract the data you need.

Another option is using the **plutil** tool to write what you need to an XML file, then use **plutil**‘s **-convert** functionality to turn it into a JSON file. For folks more experienced with using **plutil** to write XML to a file than they are with writing JSON, this option may help with a lot of use cases. For example, you could run the following command to accomplish the following:

1. Create an XML file using the **plutil** tool

2. Add the following key and value, with the value stored in an array as a string:

* Key: **MyKeyHere**
* Value: **MyGreatValue**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | plutil -create xml1 file.json |
|  | plutil -insert MyKeyHere -xml "<array><string>MyGreatValue</string></array>" file.json |

[view raw](https://gist.github.com/rtrouton/23950e917e26ff6604ce36d50d318f49/raw/9c8a8eb30fd7e23c094a2e52fb518db33ff1673e/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/23950e917e26ff6604ce36d50d318f49#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

That would give you the following XML file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <dict> |
|  | <key>MyKeyHere</key> |
|  | <array> |
|  | <string>MyGreatValue</string> |
|  | </array> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/99dbda43ab87fd927777d28737932b66/raw/dc5c75d570254a2d071fb0c9e056e201a7fbc42d/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/99dbda43ab87fd927777d28737932b66#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You would then run the following command to have **plutil** convert the XML in the file into the equivalent JSON:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the ...
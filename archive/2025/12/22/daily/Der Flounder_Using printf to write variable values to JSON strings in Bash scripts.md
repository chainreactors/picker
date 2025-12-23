---
title: Using printf to write variable values to JSON strings in Bash scripts
url: https://derflounder.wordpress.com/2025/12/22/using-printf-to-write-variable-values-to-json-strings-in-bash-scripts/
source: Der Flounder
date: 2025-12-22
fetch_date: 2025-12-23T03:23:54.959459
---

# Using printf to write variable values to JSON strings in Bash scripts

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Jamf Pro Classic API](https://derflounder.wordpress.com/category/jamf-pro-classic-api/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Using printf to write variable values to JSON strings in Bash scripts

## Using printf to write variable values to JSON strings in Bash scripts

December 22, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of my personal changeover from using the Jamf Pro [Classic API](https://developer.jamf.com/jamf-pro/docs/getting-started-2) to using the [Jamf Pro API](https://developer.jamf.com/jamf-pro/docs/jamf-pro-api-overview), I’ve needed to change from using XML for the Jamf Pro Classic API to now using JSON for the Jamf Pro API. In particular, one of my issues has been figuring out how to properly write variables to JSON when updating something on the Jamf Pro server using the Jamf Pro API. As always when writing scripts, there’s usually multiple ways to solve a problem and I figured out a solution to mine using the [printf command](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/printf.3.html). For more details, please see below the jump.

As an example, [I had written a post a while back about updating the asset tag number of a Jamf Pro computer inventory record using a script](https://derflounder.wordpress.com/2024/09/26/updating-asset-tag-information-in-jamf-pro-using-the-jamf-pro-classic-api/). As part of that script, I was using a command similar to the one below to send the updated asset tag information to the Jamf Pro server, defined in a variable named **asset\_tag\_number\_goes\_here**.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/curl -s –header "Authorization: Bearer api\_token\_goes\_here" "[https://jamf.pro.server.here/JSSResource/computers/serialnumber/serial\_number\_goes\_here&quot](https://jamf.pro.server.here/JSSResource/computers/serialnumber/serial_number_goes_here%26quot); -H "Content-Type: application/xml" -X PUT -d "<computer><general><asset\_tag>${asset\_tag\_number\_goes\_here}</asset\_tag></general></computer>" |

[view raw](https://gist.github.com/rtrouton/08e63b1d63ccf02bc2fcb808d7b95983/raw/de1f22d065af083a693c27e27e7bce82b650cce9/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/08e63b1d63ccf02bc2fcb808d7b95983#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

As part of that command, the following XML string is being sent with the **asset\_tag\_number\_goes\_here** variable being included:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | "<computer><general><asset\_tag>${asset\_tag\_number\_goes\_here}</asset\_tag></general></computer>" |

[view raw](https://gist.github.com/rtrouton/26276554d42336afec0ffe19f88d5937/raw/53c61446cb8e2934b45160d14927b0a77676e6c0/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/26276554d42336afec0ffe19f88d5937#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

The XML string is [double quoted](https://www.gnu.org/software/bash/manual/html_node/Double-Quotes.html), so my script knows to read in the value from the **asset\_tag\_number\_goes\_here** variable because the variable is referenced using the [$ character](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html).

When I updated my script to use the Jamf Pro API and JSON, my command now looked similar to this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/curl -s –header "Authorization: Bearer api\_token\_goes\_here" "[https://jamf.pro.server.here/api/v3/computers-inventory-detail/jamf\_pro\_id\_goes\_here&quot](https://jamf.pro.server.here/api/v3/computers-inventory-detail/jamf_pro_id_goes_here%26quot); -H "Content-Type: application/xml" -X PATCH -d '{"general":{"assetTag":"$asset\_tag\_number\_goes\_here"}}' |

[view raw](https://gist.github.com/rtrouton/43e04a44dd1dfb1f6bc8201827deb9cc/raw/556df370ce1bce8e8628b50eed0e670c093896c6/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/43e04a44dd1dfb1f6bc8201827deb9cc#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

My JSON string looked like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | '{"general":{"assetTag":"${asset\_tag\_number\_goes\_here}"}}' |

[view raw](https://gist.github.com/rtrouton/0723676caaf2c874ea2f70c30bfea777/raw/4f69236b6bd24fc504da4e872d59120aecbc84ae/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/0723676caaf2c874ea2f70c30bfea777#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

However, that didn’t work right and the **asset\_tag\_number\_goes\_here** variable’s value wasn’t being read correctly. Why? Because the JSON string uses single quotes to enclose it and in Bash, enclosing characters in single quotes means [every character is being sent exactly as it is written](https://www.gnu.org/software/bash/manual/html_node/Single-Quotes.html).

How to fix this? The **printf** command was my eventual solution to the problem because in Bash, you can use **printf** to write a variable using what’s known as a [format specifier](https://cplusplus.com/reference/cstdio/printf/). In this case, I needed to use the **s** format specifier because that will allow a string of characters to be used. To call the **s** format specifier for **printf**, **%s%** should be used.

To set it up, I needed to do the following in my script:

1. Create the JSON string with **%s%** in place of **${asset\_tag\_number\_goes\_here}** and store that JSON string as a variable.
2. Use **printf** in a separate variable to create the JSON string and use the **s** format specifier to substitute the **%s**  with the value of the **asset\_tag\_number\_goes\_here** variable in the correct place inside the JSON string.
3. Send the API command and include the JSON string created by **printf**.

The end result looks similar to this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden char...
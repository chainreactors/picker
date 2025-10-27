---
title: Building Jamf Pro smart groups for Sequoia-compatible and Sequoia-incompatible Mac models
url: https://derflounder.wordpress.com/2024/06/12/building-jamf-pro-smart-groups-for-sequoia-compatible-and-sequoia-incompatible-mac-models/
source: Der Flounder
date: 2024-06-13
fetch_date: 2025-10-06T16:56:07.141519
---

# Building Jamf Pro smart groups for Sequoia-compatible and Sequoia-incompatible Mac models

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro API](https://derflounder.wordpress.com/category/jamf-pro-api/), [Jamf Pro Classic API](https://derflounder.wordpress.com/category/jamf-pro-classic-api/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Building Jamf Pro smart groups for Sequoia-compatible and Sequoia-incompatible Mac models

## Building Jamf Pro smart groups for Sequoia-compatible and Sequoia-incompatible Mac models

June 12, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of preparing for macOS Sequoia, it may be useful to have a way to easily distinguish between the Macs in your fleet which can run macOS Sequoia and those which can’t. Apple has published the following list of Macs which are compatible with Sequoia, which will help with both identifying the compatible Mac models as well as the incompatible Mac models.

* iMac: 2019 and later models
* iMac Pro: All models
* Mac Studio: All models
* MacBook Pro: 2018 and later models
* MacBook Air: 2020 and later models
* Mac Mini: 2018 and later models
* Mac Pro: 2019 and later models

From there, here’s the list of Mac models which are compatible with macOS Sequoia:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | Mac13,1 |
|  | Mac13,2 |
|  | Mac14,10 |
|  | Mac14,12 |
|  | Mac14,13 |
|  | Mac14,14 |
|  | Mac14,15 |
|  | Mac14,2 |
|  | Mac14,3 |
|  | Mac14,5 |
|  | Mac14,6 |
|  | Mac14,7 |
|  | Mac14,8 |
|  | Mac14,9 |
|  | Mac15,10 |
|  | Mac15,11 |
|  | Mac15,12 |
|  | Mac15,13 |
|  | Mac15,3 |
|  | Mac15,4 |
|  | Mac15,5 |
|  | Mac15,6 |
|  | Mac15,7 |
|  | Mac15,8 |
|  | Mac15,9 |
|  | MacBookAir10,1 |
|  | MacBookAir9,1 |
|  | MacBookPro15,1 |
|  | MacBookPro15,2 |
|  | MacBookPro15,3 |
|  | MacBookPro15,4 |
|  | MacBookPro16,1 |
|  | MacBookPro16,2 |
|  | MacBookPro16,3 |
|  | MacBookPro16,4 |
|  | MacBookPro17,1 |
|  | MacBookPro18,1 |
|  | MacBookPro18,2 |
|  | MacBookPro18,3 |
|  | MacBookPro18,4 |
|  | MacPro7,1 |
|  | Macmini8,1 |
|  | Macmini9,1 |
|  | VirtualMac2,1 |
|  | iMac19,1 |
|  | iMac19,2 |
|  | iMac20,1 |
|  | iMac20,2 |
|  | iMac21,1 |
|  | iMac21,2 |
|  | iMacPro1,1 |

[view raw](https://gist.github.com/rtrouton/abcc4c7c318460e8dc3b226d21896dec/raw/bd5cce69c61b7e1f12d396400e66ba5ab098c4b7/sequoia_compatible_models.txt)
 [sequoia\_compatible\_models.txt](https://gist.github.com/rtrouton/abcc4c7c318460e8dc3b226d21896dec#file-sequoia_compatible_models-txt)
hosted with ❤ by [GitHub](https://github.com)

We can use this information to build smart groups which can help identify which Macs are compatible with Sequoia and which are not. For more details, see below the jump:

Using the information mentioned above, I was able to build two smart groups, one which displays compatible Macs and the other which displays incompatible Macs.

The compatible Macs’ smart group checks for if the Mac in question’s model identifier is any of the model identifiers which are compatible with Sequoia:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <computer\_group> |
|  | <name>Macs compatible with macOS Sequoia</name> |
|  | <is\_smart>true</is\_smart> |
|  | <criteria> |
|  | <size>51</size> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>0</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac13,1</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>1</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac13,2</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>2</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac14,10</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>3</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac14,12</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>4</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac14,13</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>5</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac14,14</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>6</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac14,15</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>7</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac14,2</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>8</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac14,3</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>9</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac14,5</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>10</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac14,6</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>11</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac14,7</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>12</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac14,8</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>13</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac14,9</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>14</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac15,10</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>15</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac15,11</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>16</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is</search\_type> |
|  | <value>Mac15,12</value> |
|  | </criterion> |
|  | <criterion> |
|  | <name>Model Identifier</name> |
|  | <priority>17</priority> |
|  | <and\_or>or</and\_or> |
|  | <search\_type>is...
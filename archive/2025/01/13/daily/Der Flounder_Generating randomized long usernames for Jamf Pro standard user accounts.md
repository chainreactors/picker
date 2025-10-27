---
title: Generating randomized long usernames for Jamf Pro standard user accounts
url: https://derflounder.wordpress.com/2025/01/12/generating-randomized-long-usernames-for-jamf-pro-standard-users/
source: Der Flounder
date: 2025-01-13
fetch_date: 2025-10-06T20:08:16.358037
---

# Generating randomized long usernames for Jamf Pro standard user accounts

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/) > Generating randomized long usernames for Jamf Pro standard user accounts

## Generating randomized long usernames for Jamf Pro standard user accounts

January 12, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the options available in Jamf Pro is creating user accounts which are specific to a Jamf Pro instance. These user accounts can be used for a variety of purposes, including [service accounts](https://delinea.com/blog/service-account-management-101) and emergency use admin accounts for [Jamf Pro’s failover functionality](https://learn.jamf.com/en-US/bundle/training-video-shorts-jamf-pro/page/How_to_Access_the_Failover_URL_in_Jamf_Pro.html) for SSO. One limitation of Jamf Pro standard user accounts is that as of this time [the authentication option for Jamf Pro standard accounts is username and password](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Jamf_Pro_User_Accounts_and_Groups.html). For Jamf Pro standard user accounts, you can set a password policy which allows you to configure the following options:

* Number of login attempts allowed before a Jamf Pro user is locked out of the account
* Password length and age
* Password reuse limitations
* Password complexity

![](https://derflounder.wordpress.com/wp-content/uploads/2025/01/screenshot-2025-01-12-at-1.07.png?w=332&h=600 "Screenshot 2025-01-12 at 1.07.png")

However, the password is not the only option you’re setting when creating a Jamf Pro standard user. Assuming that this is an account not tied to a specific person (as would be the case for a service account or an emergency use admin account), you can set to the username to a long randomized string. This can help secure the account because an attacker needs both the username and password for an account in order to authenticate and the long randomized string should make it more difficult for an attacker to guess the username. For more details, please see below the jump.

The Jamf Pro standard user’s username field can support up to 255 characters. The username field itself supports using lowercase letters and numbers when creating usernames. Within this 255 character limit, you can set a very long randomized string as the username.

**Note:** The Jamf Pro standard user’s username field should be able to support more than lowercase letters and numbers, but in my experience usernames are normally set using lowercase letters and numbers, like this:

**localadmin121**

Usernames are usually not set using the following:

* UPPPERCASE LETTERS
* Special characters like the following: **! @ # $ % ^ & \* ( ) – \_ = + \ | [ ] { } ; : / ? . >**

When folks historically don’t do something, it also usually means that there hasn’t been a lot of testing of those conditions. In turn, that may mean there’s yet-undiscovered problems which can crop up.

For this reason, I’m going to stick with only using lowercase letters and numbers in the examples used in this blog post. It’s possible the use of uppercase letters and special characters is just fine and setting a username like **LOLRICHISWRONG!@()\_** works without problems, but I’ll leave further experimentation on this topic to my readers and for this post stick with a format which I see the least problems with: lowercase letters and numbers.

To leave some room in the character limit, let’s generate a username which is 250 characters long which is a randomized string of lowercase letters and numbers. You can do this using the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | export LC\_CTYPE=C.UTF-8; tr -dc 'a-z0-9' </dev/urandom | head -c 250 |

[view raw](https://gist.github.com/rtrouton/f721de1cc322b436eb6583bf4f7c2d18/raw/18b50a57ae5f1a861502d08e8f6158dd013cfcf9/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/f721de1cc322b436eb6583bf4f7c2d18#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

**Note:** The **export LC\_CTYPE=C.UTF-8** part of the command is there because the [tr command](https://ss64.com/mac/tr.html) will otherwise return **tr: Illegal byte sequence** on macOS when working with **/dev/urandom**‘s output:

<https://andres.jaimes.net/linux/random-string/>

That command should return a 250 character string like the one shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | hvr91onhenfmk3jalcc2zopih2l7kqx3gx0i0dgb2cf8jdrm6kkvgo6h0z0039o0p5urvbccxsjhrn065n1k6ju7lo9m13isrtkgg1b1jp4519f7405last3gcxrdf0406725kbtfhxh2iln8loxtbu3iixqq6jn41i43tr76rrj556bg4a25jtg1818m0ugoxo0xns5wg7iutmwitkv4edyh14gborjjr16orn3tfdeeawx6uqx3dov4o |

[view raw](https://gist.github.com/rtrouton/dac166fe6361d2fa8262b8377d1a697f/raw/cf0575bb2154fd756a86ed1f8d92235d8ee31cff/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/dac166fe6361d2fa8262b8377d1a697f#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % export LC\_CTYPE=C.UTF-8; tr -dc 'a-z0-9' </dev/urandom | head -c 250 |
|  | hvr91onhenfmk3jalcc2zopih2l7kqx3gx0i0dgb2cf8jdrm6kkvgo6h0z0039o0p5urvbccxsjhrn065n1k6ju7lo9m13isrtkgg1b1jp4519f7405last3gcxrdf0406725kbtfhxh2iln8loxtbu3iixqq6jn41i43tr76rrj556bg4a25jtg1818m0ugoxo0xns5wg7iutmwitkv4edyh14gborjjr16orn3tfdeeawx6uqx3dov4o |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/8f2f9c9437a25417cecad3040a095287/raw/704acb8230022167602ea0e5727d06575540cf4b/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/8f2f9c9437a25417cecad3040a095287#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You can then use that string when creating a Jamf Pro standard user.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/01/screenshot-2025-01-12-at-1.42.png?w=595 "Screenshot 2025-01-12 at 1.42.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/01/screenshot-2025-01-12-at-1.43.png?w=595 "Screenshot 2025-01-12 at 1.43.png")

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/01/12/generating-randomized-long-usernames-for-jamf-pro-standard-users/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/01/12/generating-randomized-long-usernames-for-jamf-pro-standard-users/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/01/12/generating-randomiz...
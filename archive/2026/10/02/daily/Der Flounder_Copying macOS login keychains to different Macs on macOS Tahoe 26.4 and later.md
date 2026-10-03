---
title: Copying macOS login keychains to different Macs on macOS Tahoe 26.4 and later
url: https://derflounder.wordpress.com/2026/10/02/copying-macos-login-keychains-to-different-macs-on-macos-tahoe-26-4-and-later/
source: Der Flounder
date: 2026-10-02
fetch_date: 2026-10-03T07:12:50.804278
---

# Copying macOS login keychains to different Macs on macOS Tahoe 26.4 and later

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Copying macOS login keychains to different Macs on macOS Tahoe 26.4 and later

## Copying macOS login keychains to different Macs on macOS Tahoe 26.4 and later

October 2, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

Earlier this year, I had written a post about a problem [I observed with manually copied login keychains not working when moved to another Mac](https://derflounder.wordpress.com/2026/09/08/manually-copying-login-keychain-files-from-one-mac-to-another-no-longer-works-on-secure-enclave-equipped-macs-running-macos-tahoe/). To follow up on this topic, Apple has now provided information on how to back up keychain files as part of its [developer tech note TN3137](https://developer.apple.com/documentation/technotes/tn3137-on-mac-keychains#Backing-up-a-file-based-keychain).

Contrary to a conclusion I reached in my earlier blog post, Apple’s documentation does not reference keys stored in a Mac’s Secure Enclave. Instead a keychain may now reference what Apple is referring to as an entropy file. In this context, an entropy file is a file which contains randomized and unpredictable data, apparently used as part of the cryptographic key that unlocks the login keychain.

What this means is the following:

* macOS 26.3 and earlier: The password for the login keychain was used to derive the cryptographic key used to unlock the login keychain.
* macOS 26.4 and later: The information in the entropy file is now required, alongside the password, to derive the cryptographic key used to unlock the login keychain.

Per Apple’s documentation, this entropy file is stored in the following directory:

**/var/db/SystemKeys**

This directory is protected by [System Integrity Protection](https://support.apple.com/102149) (SIP) and not readable or writable unless SIP is disabled. This directory may also contain multiple entropy files, which are named using the salt value of the keychain. In the context of Apple’s keychains, the salt is a unique value associated with each keychain. This unique value is also fed into the process used to derive the cryptographic key used to unlock the keychain. For example, a login keychain may have the following salt:

**D4E8A17F3C09B5D26A4E8F017C3B9D506AE4F18**

The login keychain’s associated entropy file would be the following:

**/var/db/SystemKeys/D4E8A17F3C09B5D26A4E8F017C3B9D506AE4F18**

You can find the salt value for your login keychain by running the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | security show-keychain-info -s $HOME/Library/Keychains/login.keychain-db |

[view raw](https://gist.github.com/rtrouton/bad8cc8adb1b392ae3add3f2b0bebdc0/raw/21a1a4ccec2f96d29ebeae3beab19c84566c4aba/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/bad8cc8adb1b392ae3add3f2b0bebdc0#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You should see output similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % security show-keychain-info -s $HOME/Library/Keychains/login.keychain-db |
|  | Keychain "/Users/username/Library/Keychains/login.keychain-db" no-timeout salt=D4E8A17F3C09B5D26A4E8F017C3B9D506AE4F18 |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/07bed45816d4c18d41dbfe592a20ece4/raw/873b53f866c8d885652f81f2beba1893fb7682ba/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/07bed45816d4c18d41dbfe592a20ece4#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

The salt value is the alphanumeric string which appears after **salt=**.

Per Apple’s documentation, copying both the login keychain and the entropy file to a new Mac should allow the login keychain to be unlocked on the new Mac. The copied entropy file must be stored in the **/var/db/SystemKeys** directory on the destination Mac, which means that SIP will need to be turned off on the destination Mac in order to allow access to that protected directory. (SIP can be re-enabled once the entropy file has been successfully copied to the **/var/db/SystemKeys** directory.)

[Harold Oakley](https://eclecticlight.co) covers this issue in more detail, including how the change affects Migration Assistant and Time Machine backups. His post is available via the link below:

<https://eclecticlight.co/2026/10/02/how-to-copy-login-keychains-that-can-be-unlocked/>

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/10/02/copying-macos-login-keychains-to-different-macs-on-macos-tahoe-26-4-and-later/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/10/02/copying-macos-login-keychains-to-different-macs-on-macos-tahoe-26-4-and-later/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/10/02/copying-macos-login-keychains-to-different-macs-on-macos-tahoe-26-4-and-later/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/10/02/copying-macos-login-keychains-to-different-macs-on-macos-tahoe-26-4-and-later/?share=reddit)
* [Share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2026/10/02/copying-macos-login-keychains-to-different-macs-on-macos-tahoe-26-4-and-later/?share=twitter)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2026/10/02/copying-macos-login-keychains-to-different-macs-on-macos-tahoe-26-4-and-later/?share=pinterest)
* [Share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2026/10/02/copying-macos-login-keychains-to-different-macs-on-macos-tahoe-26-4-and-later/?share=tumblr)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (1)
[Leave a comment](#respond)

1. ![Josh Whitver's avatar](https://2.gravatar.com/avatar/89e4973c7dc8ee1f6465b7637ecbf51d7b51548276c760dfd1a95a860cb7b822?s=32&d=identicon&r=G)

   Josh Whitver

   October 2, 2026 at 8:01 pm

   [Reply](https://derflounder.wordpress.com/2026/10/02/copying-macos-login-keychains-to-different-macs-on-macos-tahoe-26-4-and-later/?replytocom=72969#respond)

   As I had asked on the original article: Would you posit that Apple’s intention is that we rely on Apple Accounts (federated via ASM/ABE or otherwise) to migrate Keychains from old Macs to new Macs?

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2026/10/02/copying-macos-login-keychains-to-different-macs-on-macos-tahoe-26-4-and-later/#respond)

Δ

[Apple Filing Protocol removed from macOS Golden Gate](https:/...
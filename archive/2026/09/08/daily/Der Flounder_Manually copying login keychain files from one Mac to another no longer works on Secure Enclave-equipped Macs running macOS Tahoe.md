---
title: Manually copying login keychain files from one Mac to another no longer works on Secure Enclave-equipped Macs running macOS Tahoe
url: https://derflounder.wordpress.com/2026/09/08/manually-copying-login-keychain-files-from-one-mac-to-another-no-longer-works-on-secure-enclave-equipped-macs-running-macos-tahoe/
source: Der Flounder
date: 2026-09-08
fetch_date: 2026-09-09T06:54:38.611723
---

# Manually copying login keychain files from one Mac to another no longer works on Secure Enclave-equipped Macs running macOS Tahoe

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Manually copying login keychain files from one Mac to another no longer works on Secure Enclave-equipped Macs running macOS Tahoe

## Manually copying login keychain files from one Mac to another no longer works on Secure Enclave-equipped Macs running macOS Tahoe

September 8, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

I recently encountered an issue with the login keychain on macOS. For those not familiar with the login keychain, it’s a [keychain](https://developer.apple.com/documentation/security/keychains) that macOS automatically creates for each user account on a Mac. The password for a user’s login keychain matches the password used to log in to the Mac. It is stored as an encrypted database file and unlocks automatically when the user logs in, since the login password and keychain password are the same by default.

As of macOS Tahoe, the login keychain is a SQLite database file named **login.keychain-db**. It is stored in the user’s home folder in the following directory:

**/Users/username\_goes\_here/Library/Keychains**

**![](https://derflounder.wordpress.com/wp-content/uploads/2026/09/screenshot-2026-09-08-at-5.47.51pm.png?w=595 "Screenshot 2026-09-08 at 5.47.51 PM.png")**

Historically, you could copy the login keychain file from one Mac to another and be able to open it on the destination Mac by providing the password to that keychain. As of macOS Tahoe, this does not appear to work for Macs which use [Secure Enclave](https://support.apple.com/guide/security/the-secure-enclave-sec59b0b31ff/web). For those Macs, only having the password to the login keychain is no longer sufficient for reasons discussed in the [Keychain data protection section](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web) of Apple’s [Platform Security documentation](https://support.apple.com/guide/security/welcome/web):

***Keychain items are encrypted using two different AES-256-GCM keys: a table key (metadata) and a per-row key (secret key). Keychain metadata (all attributes other than kSecValue) is encrypted with the metadata key to speed searches, and the secret value (kSecValueData) is encrypted with the secret key. The metadata key is protected by the Secure Enclave but is cached in the Application Processor to allow fast queries of the keychain. The secret key always requires a round trip through the Secure Enclave.***

![](https://derflounder.wordpress.com/wp-content/uploads/2026/09/screenshot-2026-09-08-at-5.30.20pm.png?w=595 "Screenshot 2026-09-08 at 5.30.20 PM.png")

For more details, please see below the jump.

The relevant section of the passage above is this:

***The metadata key is protected by the Secure Enclave but is cached in the Application Processor to allow fast queries of the keychain. The secret key always requires a round trip through the Secure Enclave.***

From that, it appears that unlocking the login keychain requires more than the password because the keys it unlocks are tied to the Secure Enclave of the Mac where the keychain was created. With the decryption keys stored in the source Mac’s Secure Enclave, manually copying the keychain to another Mac and then unlocking it won’t work. The password you have for the keychain may be correct, but the actual keys needed to decrypt its contents won’t be available on the destination Mac.

I was able to test this by copying a **login.keychain-db** file from an Apple Silicon Mac to a second Mac (in this case, a macOS virtual machine) and attempted to unlock it using the account’s correct password.

**Note:** The reason I chose to test using a macOS VM is that VMs don’t have a Secure Enclave. This allows us to verify that if keys are being stored in the source Mac’s Secure Enclave, then the VM won’t be able to access them in the VM.

Here’s the test procedure used:

1. Create a user account on an Apple Silicon Mac with the following username:

**username**

2. Log into the **username** account on the Apple Silicon Mac.
3. Locate the **login.keychain-db** file in **/Users/username/Library/Keychains**.
4. Copy the **login.keychain-db** file to a convenient location.
5. Set up a new macOS VM
6. Create a **username** user account on the macOS VM with an identical password to the one used for the **username** account on the Apple Silicon Mac.
7. Log into the **username** account on the macOS VM.
8. Locate the **login.keychain-db** file in **/Users/username/Library/Keychains**.
9. Remove the existing **login.keychain-db** file from **/Users/username/Library/Keychains** on the macOS VM
10. Copy the **login.keychain-db** file from the Apple Silicon Mac to **/Users/username/Library/Keychains** in the macOS VM.
11. Restart the macOS VM
12. Log into the **username** account on the macOS VM.

The behavior I expected:

* The login keychain would unlock automatically when I logged in as the **username** account on the macOS VM.

What actually happened:

* A new login keychain file was created automatically when I logged in as the **username** account on the macOS VM.

Why did this happen? Time to check the logs.

What I found was that the unlock attempt failed even though the correct password was supplied. I was able to confirm this by running the following command to get the relevant logs:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | log show –predicate 'subsystem == "com.apple.securityd" && category == "KCLogin"' –last 1h |

[view raw](https://gist.github.com/rtrouton/a4b0ebbe505fb32212f22581148c7d55/raw/af6011919f5f58389bdcb29a5b455353efc7995d/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/a4b0ebbe505fb32212f22581148c7d55#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

The logs showed the following:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | Timestamp Thread Type Activity PID TTL |
|  | 2026-09-08 11:49:11.321174-0400 0x33c Default 0x2fb6 170 0 loginwindow: (Security) [com.apple.securityd:KCLogin] StorageManager::login: loginDLDbIdentifier is /Users/username/Library/Keychains/login.keychain |
|  | 2026-09-08 11:49:11.321284-0400 0x33c Default 0x2fb6 170 0 loginwindow: (Security) [com.apple.securityd:KCLogin] Attempting to unlock login keychain "/Users/username/Library/Keychains/login.keychain-db" |
|  | 2026-09-08 11:49:11.466352-0400 0x33c Default 0x2fb6 170 0 loginwindow: (Security) [com.apple.securityd:KCLogin] SecKeychainLogin result: 0, password was supplied |
|  | 2026-09-08 11:50:53.497587-0400 0x338 Default 0x2d4a 170 0 loginwindow: (Security) [com.apple.securityd:KCLogin] StorageManager::login: loginDLDbIdentifier is /Users/username/Library/Keychains/login.keychain |
|  | 2026-09-08 11:50:53.497759-0400 0x338 Default 0x2d4a 170 0 loginwindow: (Security) [com.apple.securityd:KCLogin] Attempting to unlock login keychain "/Users/us...
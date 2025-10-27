---
title: Sandfly 2.8.2 – Over 1,000 Linux Compromise Detection Modules and More
url: https://sandflysecurity.com/blog/sandfly-2-8-2-over-1000-linux-compromise-detection-modules-and-more
source: Sandfly Security Blog RSS Feed
date: 2025-05-27
fetch_date: 2025-10-06T22:28:28.036006
---

# Sandfly 2.8.2 – Over 1,000 Linux Compromise Detection Modules and More

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 2.8.2 – Over 1,000 Linux Compromise Detection Modules and More

19 January 2021

Product Update

Sandfly 2.8.2 is here and features many upgrades including **over 1,000** compromise detection and incident response modules for Linux. This update features:

* User password entry decoder to search for password age, expiration and hash parameters.
* An *SSH authorized\_keys* file decoder and many new templates to keep an eye on SSH key usage.
* Expanded ability to hunt for suspicious file artifacts left on a system which can expose compromise activity.
* New backdoor detection methods.
* Known hacking tool detections.
* New policy checks to find system misconfigurations and dangerous practices.
* Much more!

## Massive Signature Boost

First, we have increased the number of signature modules now to **over 1,000**. This is a big landmark for us as it represents what is the widest and deepest compromise detection set for Linux in the industry. Sandfly is a powerful forensics and compromise detection tool for Linux and this new upgrade brings in many new and

## Linux User Password Signatures and Search Tools

While we recommend everyone use SSH keys and certificates for user logins, the reality is that usernames and passwords are here for the time being and we want to make sure you have the tools to work with them and keep your systems secure. As a result, we have added password entry decoding to Sandfly. This allows us to create an entirely new suite of signatures designed to help find unusual password additions or changes, password expiration policy violations, stale accounts, obsolete password hash algorithms and much more.

There are modules available to help detect and alert on the following password fields:

* Max age allowed.
* Minimum age allowed.
* Days since password expired.
* Days since password last changed.
* Password inactivity period before being locked.
* Password change warning period.
* Password hash type.
* Duplicate password hashes.
* Password data cross-system searching.

In addition to this, we have kept other fields to help identify password hashes present, disabled and locked.

## Find Users With New or Recently Changed Passwords

One way to leverage our new password age decoding is to use it to help find users that have recently had a new or changed password added to their account. Often attackers will add new accounts or passwords to existing accounts to allow remote access. With our new signatures you can quickly find any account that has had new passwords added or changed over a period of days you specify. We have a variety of pre-defined templates available to clone and use automatically or as part of an incident response.

To demonstrate, below we scanned a system for any new or changed passwords and flagged a suspicious “proxy” account that had a new password added five days ago.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![A suspicious Linux default user with a recently added password.](https://www.datocms-assets.com/56687/1635216296-sandfly-user-password-days-since-last-changed-less-than-7-days.png?auto=format&dpr=2&q=60&w=920 "A suspicious Linux default user with a recently added password.")

## Obsolete Password Hash Checks

Being able to check what kind of password hash a user has can spot obsolete and stale accounts. Obsolete hashes are a particular risk if the */etc/shadow* file is stolen as they can allow GPU-based crackers to try huge combinations of passwords per second and break them. Now you can look for obsolete hashes such as DES, MD5 and Blowfish as an automated policy check or on-demand.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Scanning for obsolete Linux MD5 password hashes.](https://www.datocms-assets.com/56687/1635216307-sandfly-md5-obsolete-password-hash.png?auto=format&dpr=2&q=60&w=920 "Scanning for obsolete Linux MD5 password hashes.")

## Search for Unknown and Unencrypted Password Hash Types

In addition to looking for obsolete password hashes, we can also find unencrypted or unknown password hash types which should be investigated.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux user with unencrypted or unknown password hash detected.](https://www.datocms-assets.com/56687/1635216315-sandfly-user-password-hash-type-unknown-1.png?auto=format&dpr=2&q=60&w=920 "Linux user with unencrypted or unknown password hash detected.")

## Search All Password Age Parameters

All standard Linux password age parameters can be searched and used. For instance, you can use it to search for users that have a password that has been expired for more than 30 days. This can help identify stale users and unused accounts:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly policy user password days since expired greater than 30 days](https://www.datocms-assets.com/56687/1635216322-sandfly-policy-user-password-days-since-expired-greater-than-30-days.png?auto=format&dpr=2&q=60&w=920 "Sandfly policy user password days since expired greater than 30 days")

## Duplicate Password Hash Detection

Some malware has been known to insert multiple users with identical password hashes. These kinds of passwords are extremely suspicious under Linux. This new check will look at all users and flag any with duplicate password hashes for immediate investigation.

## Custom Password Parameter Searches

As with all Sandfly checks, you can clone and customize the search parameters as needed. Below we see an example of a check that flags any user with a password hash that is unlocked. This can be useful for finding old accounts not using SSH keys and still have a password hash sitting around and not disabled.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![User password preset](https://www.datocms-assets.com/56687/1635216330-user-password-present.png?auto=format&dpr=2&q=60&w=920 "User password preset")

## SSH Key Decoding

We now parse the SSH *authorized\_keys* and *authorized\_keys2* files and pull out all SSH login public key information. All of the following parameters can be searched for with templates or built-in modules to do SSH key threat hunting:

* Key comments.
* Full key entry.
* Key hash (hash of key itself to search across all systems).
* SSH options.
* SSH key type.
* Duplicate key entries.
* *authorized\_keys* path.
* *authorized\_keys* file attributes (size, hash, ownership, etc.).

## SSH Duplicate Keys

Sandfly will identify duplicate SSH keys present in an *authorized\_keys* or *authorized\_keys2* file. This will find entries that may be stale, unintended duplicates or other misconfiguration. Linux malware sometimes inserts duplicate keys into the same file and this will also be spotted.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Finding duplicate SSH keys in the root user’s account.](https://www.datocms-assets.com/56687/1635216337-sandfly-policy-user-ssh-authorized-keys-duplicates-found.png?auto=format&dpr=2&q=60&w=920 "Finding duplicate SSH keys in the root user’s account.")

## Weak SSH Keys

We now will check for SSH keys using ECDSA NIST algorithms that are [suspected of being weakened by the NSA](https://git.libssh.org/projects/libssh.git/tree/doc/curve25519-sha256%40libssh.org.txt#n4) to allow easier compromise. If you are concerned about this risk you can enable these checks and move users to a more secure *ed25519* key.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Weakened SSH ECDSA NIST key detected.](https://www.datocms-assets.com/56687/1635216344-sandfly-policy-user-ssh-authorized-keys-type-ecdsa-sha2-nistp256.png?auto=format&dpr=2&q=60&w=920 "Weakened SSH ECDSA NIST key detec...
---
title: Using certificate public keys to create dummy MDM configuration profiles for Jamf Pro device smart group scoping
url: https://derflounder.wordpress.com/2024/10/14/using-certificate-public-keys-to-create-dummy-mdm-configuration-profiles-for-jamf-pro-device-smart-group-scoping/
source: Der Flounder
date: 2024-10-15
fetch_date: 2025-10-06T18:50:32.843544
---

# Using certificate public keys to create dummy MDM configuration profiles for Jamf Pro device smart group scoping

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/), [PKI](https://derflounder.wordpress.com/category/pki/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Using certificate public keys to create dummy MDM configuration profiles for Jamf Pro device smart group scoping

## Using certificate public keys to create dummy MDM configuration profiles for Jamf Pro device smart group scoping

October 14, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

My teammates at Jamf who support Jamf’s own IT (known as Jamf @ Jamf) have [developed an innovative method](https://www.modtitan.com/2024/09/one-approach-to-using-idp-group.html) for allowing computer and mobile device smart groups to figure out device membership based on users and groups from an identity provider (like Okta or Entra ID) or an LDAP service (like Active Directory).

Normally, figuring out user and group membership is not a capability of computer and mobile device smart groups but the method the Jamf @ Jamf folks developed leverages MDM configuration profiles to bridge that functionality gap in the following way:

1. User is assigned an application with compliance policy in the organization’s identity provider.
2. A Jamf @ Jamf automation system adds User Extension Attribute criteria to a username in scope of a group provided by the identity provider.
3. A smart user group in Jamf Pro uses that criteria to populate group membership.
4. The new smart user group is used to scope a configuration profile.

The configuration profile referenced in step 4 above is then deployed to devices that match the smart user group’s membership. Once the profile is deployed, the profile being installed on a device is criteria which can be used by computer and mobile device smart groups. This allows the profile to be the bridge functionality to connect users and user groups from an identity provider or an LDAP service.

In the post I linked to earlier, the configuration profiles created for this purpose are referred to as “dummy profiles”, which are in turn a reference to “dummy receipts”. Dummy receipts are a method for [creating a receipt for an installer package installed by Jamf Pro](https://community.jamf.com/t5/jamf-pro/dummy-receipts/m-p/13327), which likewise can be used as criteria which can be used by computer smart groups.

But what goes in that dummy profile? Ideally, it should be something that deploys no settings at all. The dummy profile’s existence on a device is enough to accomplish the goal of bridging the gap between user and device scoping and for the sake of causing no complications, the profile should exist on the device and otherwise do nothing. Meanwhile, this should be an approach which can be used on all Apple platforms so we need something which can be deployed to all Apple platforms.

After thinking about this for a bit and discussing it with colleagues, it looks like the best way to accomplish this is to build a configuration profile with the following characteristics:

1. Profile with certificate payload
2. Certificate payload should have the following:

* Self-signed certificate’s public key
* Certificate lifespan should be set to an extended period of time, to allow the use of the profile over a long period of time without worrying about the certificate expiring.

The reason to use a self-signed certificate’s public key is that a certificate can only be used for something if you have both the public and private key available. Without the private key being available at some point in the communication process to authenticate the public key as being valid, the public key is effectively useless.

In this case, that’s exactly what we want – we want something useless in the profile’s certificate payload because something useless can’t be used! Using this approach will mean that our configuration profile will deploy no settings to a Mac or mobile device, and a malicious third party won’t be able to use the certificate either because only the public key for it will be available. For more details, please see below the jump.

To assist with creating the self-signed certificate’s public key for our dummy profile’s certificate payload, I’ve written a script which does the following:

1. Generates a self-signed SSL certificate’s public key and associated private key, where the script’s default settings are to create a self-signed certificate with the following characteristics:

* Certificate subject name is set to a UUID value.
* Certificate key is set to use a 4096-bit RSA key
* Certificate lifespan is set to 3652 days.

2. If the self-signed SSL certificate’s public key and private key are successfully created, script displays a message listing public key certificate name with a .cer file extension and the certificate public key’s location on the filesystem.

3. If the self-signed SSL certificate’s public key and private key are not successfully created, script displays an error message.

**Note:** Both the RSA key bit strength and lifespan are set using variables in the script, so these default settings can be adjusted as needed.

The private keys created by this script are completely disposable. For this purpose, we only want the public keys created by this script because we want a certificate payload which is functionally useless for use with Jamf Pro dummy configuration profiles.

A successful run of the script should produce output similar to that shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername % /path/to/create\_certificate\_public\_keys\_for\_dummy\_profile\_certificate\_payload.sh |
|  | Creating self-signed certificate with 4096 bit RSA key and a lifespan of 3652 days. |
|  | Generating a 4096 bit RSA private key |
|  | …………………………………………………..++++ |
|  | …………………………………………………………………………………………….++++ |
|  | writing new private key to '/var/folders/bq/d25fcnnj74j2gd8cnkhjmlqh0000gp/T/tmp.qkbeMzYTIY/2E69ABC8-3B5C-4F8F-ACE9-BAAAE592BF1C.key' |
|  | —– |
|  | Self-signed certificate successfully generated. |
|  | Self-signed certificate public key name: 2E69ABC8-3B5C-4F8F-ACE9-BAAAE592BF1C.cer |
|  | Self-signed certificate public key location: /var/folders/bq/d25fcnnj74j2gd8cnkhjmlqh0000gp/T/tmp.E45hx0xaW2/2E69ABC8-3B5C-4F8F-ACE9-BAAAE592BF1C.cer |
|  | username@computername % |

[view raw](https://gist.github.com/rtrouton/3352abf602ec6888087fad20b9e48f34/raw/f845adff520f3048133c1c93ee21150051c7643f/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/3352abf602ec6888087fad20b9e48f34#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Once the public key is created, a new Jamf Pro configuration profile can be created. For this example, I’m setting up a new dummy configuration profile named **Advertising Department Software Test Group** which will be deployed to Macs.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-14-at-12.50.png?w=595 "Screenshot 2024-10-14 at 12.50.png")

As part of creating the profile, I’m selecting the **Certificate** payload option and...
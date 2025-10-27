---
title: Multiple Internet to Baseband Remote Code Execution Vulnerabilities in Exynos Modems
url: https://googleprojectzero.blogspot.com/2023/03/multiple-internet-to-baseband-remote-rce.html
source: Project Zero
date: 2023-03-17
fetch_date: 2025-10-04T09:51:16.194854
---

# Multiple Internet to Baseband Remote Code Execution Vulnerabilities in Exynos Modems

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Thursday, March 16, 2023

### Multiple Internet to Baseband Remote Code Execution Vulnerabilities in Exynos Modems

Posted by Tim Willis, Project Zero

In late 2022 and early 2023, Project Zero reported eighteen 0-day vulnerabilities in Exynos Modems produced by Samsung Semiconductor. The four most severe of these eighteen vulnerabilities (CVE-2023-24033, CVE-2023-26496, CVE-2023-26497 and CVE-2023-26498) allowed for Internet-to-baseband remote code execution. Tests conducted by Project Zero confirm that those four vulnerabilities allow an attacker to remotely compromise a phone at the baseband level with no user interaction, and require only that the attacker know the victim's phone number. With limited additional research and development, we believe that skilled attackers would be able to quickly create an operational exploit to compromise affected devices silently and remotely.

The fourteen other related vulnerabilities (CVE-2023-26072, CVE-2023-26073, CVE-2023-26074, CVE-2023-26075, CVE-2023-26076 and nine other vulnerabilities that are yet to be assigned CVE-IDs) were not as severe, as they require either a malicious mobile network operator or an attacker with local access to the device.

## Affected devices

[Samsung Semiconductor's advisories](https://semiconductor.samsung.com/support/quality-support/product-security-updates/) provide the list of Exynos chipsets that are affected by these vulnerabilities. Based on information from public websites that map chipsets to devices, affected products likely include:

* Mobile devices from Samsung, including those in the S22, M33, M13, M12, A71, A53, A33, A21s, A13, A12 and A04 series;
* Mobile devices from Vivo, including those in the S16, S15, S6, X70, X60 and X30 series;
* The Pixel 6 and Pixel 7 series of devices from Google; and
* any vehicles that use the Exynos Auto T5123 chipset.

## Patch timelines

We expect that patch timelines will vary per manufacturer (for example, affected Pixel devices have received a fix for all four of the severe Internet-to-baseband remote code execution vulnerabilities in the [March 2023](https://source.android.com/docs/security/bulletin/pixel/2023-03-01) security update). In the meantime, users with affected devices can protect themselves from the baseband remote code execution vulnerabilities mentioned in this post by turning off Wi-Fi calling and Voice-over-LTE (VoLTE) in their device settings, although your ability to change this setting can be dependent on your carrier. As always, we encourage end users to update their devices as soon as possible, to ensure that they are running the latest builds that fix both disclosed and undisclosed security vulnerabilities.

## Four vulnerabilities being withheld from disclosure

Under our standard disclosure policy, Project Zero discloses security vulnerabilities to the public a set time after reporting them to a software or hardware vendor. In some rare cases where we have assessed attackers would benefit significantly more than defenders if a vulnerability was disclosed, we have made an exception to our policy and delayed disclosure of that vulnerability.

Due to a very rare combination of level of access these vulnerabilities provide and the speed with which we believe a reliable operational exploit could be crafted, we have decided to make a policy exception to delay disclosure for the four vulnerabilities that allow for Internet-to-baseband remote code execution. We will continue our history of transparency by [publicly sharing disclosure policy exceptions](https://googleprojectzero.blogspot.com/p/vulnerability-disclosure-faq.html#exceptions), and will add these issues to that list once they are all disclosed.

## Related vulnerabilities not being withheld

Of the remaining fourteen vulnerabilities, we are disclosing four vulnerabilities (CVE-2023-26072, CVE-2023-26073, CVE-2023-26074 and CVE-2023-26075) that have exceeded Project Zero's standard 90-day deadline today. These issues have been publicly disclosed in our [issue tracker](https://bugs.chromium.org/p/project-zero/issues/list?sort=-id&q=&can=1), as they do not meet the high standard to be withheld from disclosure. The remaining ten vulnerabilities in this set have not yet hit their 90-day deadline, but will be publicly disclosed at that point if they are still unfixed.

## Changelog

**2023-03-21**: Removed note at the top of the blog as patches are more widely available for the four severe vulnerabilities. Added additional context that some carriers can control the Wifi calling and VoLTE settings, overriding the ability for some users to change this setting.

**2023-03-20**: Google Pixel updated their [March 2023 Security Bulletin](https://source.android.com/docs/security/bulletin/pixel/2023-03-01) to now show that all four Internet-to-baseband remote code execution vulnerabilities were fixed for Pixel 6 and Pixel 7 in the March 2023 update, not just one of the vulnerabilities, as originally stated.

**2023-03-20**: Samsung Semiconductor [updated their advisories](https://semiconductor.samsung.com/support/quality-support/product-security-updates/) to include three new CVE-IDs, that correspond to the three other Internet-to-baseband remote code execution issues (CVE-2023-26496, CVE-2023-26497 and CVE-2023-26498). The blogpost text was updated to reflect these new CVE-IDs.

**2023-03-17**: Samsung Semiconductor [updated their advisories](https://semiconductor.samsung.com/support/quality-support/product-security-updates/) to remove Exynos W920 as an affected chipset, so we have removed it from the "Affected devices" section.

**2023-03-17**: Samsung Mobile advised us that the A21s is the correct affected device, not the A21 as originally stated.

**2023-03-17**: Four of the fourteen less severe vulnerabilities hit their 90-day deadline at the time of publication, not five, as originally stated.

Posted by

[Google Project Zero](https://www.blogger.com/profile/08975904405228580347 "author profile")

at
[11:07 AM](https://googleprojectzero.blogspot.com/2023/03/multiple-internet-to-baseband-remote-rce.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=4838136820032157985&postID=8686178874057357713&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=8686178874057357713&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=8686178874057357713&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=8686178874057357713&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=8686178874057357713&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=4838136820032157985&postID=8686178874057357713&target=pinterest "Share to Pinterest")

#### No comments:

#### Post a Comment

[Newer Post](https://googleprojectzero.blogspot.com/2023/04/technical-report-into-intel-tdx.html "Newer Post")

[Older Post](https://googleprojectzero.blogspot.com/2023/01/exploiting-null-dereferences-in-linux.html "Older Post")
[Home](https://googleprojectzero.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://googleprojectzero.blogspot.com/feeds/8686178874057357713/comments/default)

## Search This Blog

|  |  |
| --- | --- |
|  |  |

## Pages

* [About Project Zero](https://googleprojectzero.blogspot.com/p/about-project-zero.html)
* [0day "In the Wild"](https://googleprojectzero.blogspot.com/p/0day.html)
* [0day Exploit Root Cause Analyses](https://googleprojectzero.github.io/0days-in-the-wild/rca.html)
* [Reporting Transparency](https://googleprojectzero.blogspot.com/p/reporting-transparency.html)
* [Vulnerability Discl...
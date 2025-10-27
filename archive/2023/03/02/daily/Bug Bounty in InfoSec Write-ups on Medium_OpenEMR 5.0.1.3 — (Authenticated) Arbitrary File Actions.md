---
title: OpenEMR 5.0.1.3 — (Authenticated) Arbitrary File Actions
url: https://infosecwriteups.com/openemr-5-0-1-3-authenticated-arbitrary-file-actions-f7006e636b8c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-02
fetch_date: 2025-10-04T08:26:01.675195
---

# OpenEMR 5.0.1.3 — (Authenticated) Arbitrary File Actions

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff7006e636b8c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fopenemr-5-0-1-3-authenticated-arbitrary-file-actions-f7006e636b8c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fopenemr-5-0-1-3-authenticated-arbitrary-file-actions-f7006e636b8c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f7006e636b8c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f7006e636b8c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# OpenEMR 5.0.1.3 — (Authenticated) Arbitrary File Actions

[![Josh Fam](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)](https://pullerjsecu.medium.com/?source=post_page---byline--f7006e636b8c---------------------------------------)

[Josh Fam](https://pullerjsecu.medium.com/?source=post_page---byline--f7006e636b8c---------------------------------------)

2 min read

·

Nov 17, 2020

--

Listen

Share

Press enter or click to view image in full size

![]()

Back in 2018, a group of security researchers and I decided to try our hands at OpenEMR and find security vulnerabilities.The full report can be found [here](https://www.open-emr.org/wiki/images/1/11/Openemr_insecurity.pdf).This a very good read and I recommend reading it in its entirety. However this blog post is just documenting my contribution to the project.The following are the three CVEs I received in the collaboration. These were all responsibly disclosed and patched so upgrading to the latest version would be well advised.

1.CVE-2018–15140-Authenicated Arbitrary Read

Vulnerable Code:

```
if ($_POST['mode'] == 'get'){
     echo file_get_contents($_POST['docid']);
     exit;
  }
```

This is a vulnerability that allows an attacker to make a malicious request to /portal/import\_template.php on a unpatched instance of OpenEMR.The result of this request is an arbitrary file read of a local file located on the file system.This vulnerability was possible due to the application passing user input into file\_get\_contents() without any sanitization if the parameter mode is set with get as its value. This result of this input,which is the local file, was then echoed back in the html response.

2.CVE-2018–15142-Authenicated Arbitrary Write

Vulnerable Code:

```
} else if ($_POST['mode'] == 'save') {
    file_put_contents($_POST['docid'], $_POST['content']);
    exit(true);
}
```

This is an vulnerability in /portal/import\_template.php which allows an attacker to write php files to a local file system.This works if the parameter mode is set to save.If that is the case the post parameters docid and content are passed to file\_put\_contents() without any sanitization.The docid is the file name and the content includes the malicious php code. This by itself doesn’t have that much impact since you cannot execute the file, but when paired up with the previously found arbitrary file read, leads to remote code execution.

3.CVE-2018–15141- Authenticated Arbitrary File Delete

Vulnerable Code:

```
} else if ($_POST['mode'] == 'delete') {
     unlink($_POST['docid']);
     exit(true);
 }
```

This is an vulnerability also in /portal/import\_template.php which allows an attacker to delete any file in the system if the filename is known and the permissions to delete are allowed.This is possible when the post parameter mode is set to delete. The docid parameter which contains the file name specified by the attacker is then passed to unlink() without sanitization.

Thank you for reading and hope you enjoyed.You can find Pocs for any one of these on ExploitDB, [here](https://www.exploit-db.com/exploits/45202). You can also read CTF and bug bounty writeups on here or on my blog <https://jsecu.github.io>. If you have any questions, feel free to message me at @Pullerze on Twitter . More Bug Bounty and security writeups coming soon!

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----f7006e636b8c---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----f7006e636b8c---------------------------------------)

[Hackerone](https://medium.com/tag/hackerone?source=post_page-----f7006e636b8c---------------------------------------)

[White Box Testing](https://medium.com/tag/white-box-testing?source=post_page-----f7006e636b8c---------------------------------------)

[Source Code](https://medium.com/tag/source-code?source=post_page-----f7006e636b8c---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f7006e636b8c---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f7006e636b8c---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f7006e636b8c---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--f7006e636b8c---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--f7006e636b8c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Josh Fam](https://miro.medium.com/v2/resize:fill:96:96/1*dmbNkD5D-u45r44go_cf0g.png)](https://pullerjsecu.medium.com/?source=post_page---post_author_info--f7006e636b8c---------------------------------------)

[![Josh Fam](https://miro.medium.com/v2/resize:fill:128:128/1*dmbNkD5D-u45r44go_cf0g.png)](https://pullerjsecu.medium.com/?source=post_page---post_author_info--f7006e636b8c---------------------------------------)

[## Written by Josh Fam](https://pullerjsecu.medium.com/?source=post_page---post_author_info--f7006e636b8c---------------------------------------)

[93 followers](https://pullerjsecu.medium.com/followers?source=post_page---post_author_info--f7006e636b8c---------------------------------------)

·[1 following](ht...
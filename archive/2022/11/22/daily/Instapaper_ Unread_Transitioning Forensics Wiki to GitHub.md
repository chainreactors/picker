---
title: Transitioning Forensics Wiki to GitHub
url: https://osdfir.blogspot.com/2022/11/transitioning-forensics-wiki-to-github.html
source: Instapaper: Unread
date: 2022-11-22
fetch_date: 2025-10-03T23:25:42.052027
---

# Transitioning Forensics Wiki to GitHub

[Skip to main content](#main)

# [Open Source DFIR](https://osdfir.blogspot.com/)

A security blog for the digital forensics community on how to perform digital forensic incident response with open source tools.

### Transitioning Forensics Wiki to GitHub

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

By

[Joachim Metz](https://www.blogger.com/profile/14169983450780601879 "author profile")

[November 20, 2022](https://osdfir.blogspot.com/2022/11/transitioning-forensics-wiki-to-github.html "permanent link")

# Transitioning Forensics Wiki to GitHub

Copied on 20 November 2022 from <https://forensicswiki.xyz/page/Main_Page> with permission. Authored by Simson Garfinkel.

We created the Forensics Wiki so that digital forensics practitioners would have a place where they could record things that they had learned for the benefit of themselves, their co-workers, and the community as a whole.

The Forensics Wiki was modeled on Wikipedia, in that we created it as a non-commercial, space without advertising. But the Forensics Wiki soon developed ground rules that were fundamentally different from Wikipedia.

Unlike Wikipedia, information on the Forensics Wiki does not need to be cited. Because the Forensics Wiki is created and maintained by practitioners, much of the information that the wiki contains is either original information that the authors have learned through the process of reverse engineering, or else it is information they couldn’t attribute to a specific source due to security concerns.

Another difference is content that might be viewed by some to be self-promotional or commercial. While Wikipedia has rules that generally prohibit people from editing articles about themselves or their organizations, we encouraged this on the Forensics Wiki. Our community is so small, so the only way we will have detailed articles about small businesses and most software packages is if they are created by the businesses and authors themselves. Stuff that is obviously incorrect will either be edited or, more likely, ignored.

Because of the small size of the open source digital forensics community, hosting the Forensics Wiki has always been a challenge. It started as a side project by Simson Garfinkel, and was hosted in his Dreamhost account. In 2015 Simson handed the forensicswiki.org domain and the wiki content to a company that had a contract with the US government to develop a portal for use by forensics practitioners. But that company was acquired by another company soon after the domain was handed over, and the corporate successor was not interested in open source digital forensics. After the organization shut down the servers, we reconstructed the wiki at forensicswiki.xyz.

We are now transitioning the Forensics Wiki to a new platform once again — a platform that offers new opportunities for growth. We have created an organization on GitHub called ‘forensicswiki’ that will be used for all things related to the wiki. We have translated all of the articles from the MediaWiki markup language to Markdown and imported them to a git repo that is hosted at <https://github.com/forensicswiki/wiki>. The pages are then automatically rendered to <https://forensics.wiki/>, where they can be searched using a modern, highly responsive search interface.

We wish to thank Rob Colonna, Ryan Benson and Joachim Metz at Google for their work on this transition.

We will be setting up the forensicswiki.xyz domain to forward to the new location. (Unfortunately, we still haven’t been able to recover the forensicswiki.org and forensicswiki.com domains from the organization that now owns them.)

Updates to the forensicswiki are now submitted as pull requests to the forensicswiki/wiki git repo. Once they are approved, the articles will go live on the website.

Thanks to everyone who has contributed to the wiki in the past. We look forward to working with you in the future!

See you at <https://forensics.wiki/>

[Forensics Wiki](https://osdfir.blogspot.com/search/label/Forensics%20Wiki)
[forensicswiki](https://osdfir.blogspot.com/search/label/forensicswiki)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Comments

#### Post a Comment

### Popular posts from this blog

### [Parsing the $MFT NTFS metadata file](https://osdfir.blogspot.com/2020/04/parsing-mft-ntfs-metadata-file.html)

By

[Joachim Metz](https://www.blogger.com/profile/14169983450780601879 "author profile")

[April 30, 2020](https://osdfir.blogspot.com/2020/04/parsing-mft-ntfs-metadata-file.html "permanent link")

Background Numerous articles have been written about parsing the $MFT NTFS metadata file before. Some of these explain the technique itself [ 1 ] and others mostly focus on how to use tools. Rarely do articles mention the pros and cons of the technique from a digital forensics perspective [ 2 ].  What is $MFT parsing?  For readers not familiar with the NTFS file system, MFT stands for Master File Table. This table is stored in a file system metadata file, meaning that as far as the file system is concerned it is a file, however that the file contains file system metadata not “regular” content. The name of this file is “$MFT”.  The MFT consists of a sequence of (predetermined) fixed-size entries (or MFT entries). These entries are typically 1024 bytes in size, however the size is defined in the NTFS volume header and in a “regular” MFT entry itself.  The first 4-bytes of a “regular” MFT-entry (or record) starts with the signature “FILE”. The MFT entry can...

[Read more](https://osdfir.blogspot.com/2020/04/parsing-mft-ntfs-metadata-file.html "Parsing the $MFT NTFS metadata file")

### [Incident Response in the Cloud](https://osdfir.blogspot.com/2020/07/incident-response-in-cloud.html)

By

[Ollie Green](https://www.blogger.com/profile/08398115638724632004 "author profile")

[July 05, 2020](https://osdfir.blogspot.com/2020/07/incident-response-in-cloud.html "permanent link")

Many organizations have begun moving a majority of their services towards the cloud in recent years. As a result, attackers have shifted their focus towards the cloud. This has resulted in new techniques and methods specifically designed to compromise cloud infrastructure, like the recent SALTSTACK vulnerability that was widely exploited [ 1 ]. Therefore it is critical for these organizations to have an incident response team that understands the new risks attached to cloud and how cloud can make incident response easier or harder.  In this blog post we will walk you through each phase you may encounter in traditional incident response and highlight the differences when adopting cloud computing. It is aimed towards both those who are new to incident response and cloud computing. We’ve included insights that will benefit organizations taking that step towards cloud who want to ensure they are prepared to respond efficiently to cloud incidents.  Traditional Incident Response Be...

[Read more](https://osdfir.blogspot.com/2020/07/incident-response-in-cloud.html "Incident Response in the Cloud")

### [Container Forensics with Docker Explorer](https://osdfir.blogspot.com/2021/01/container-forensics-with-docker-explorer.html)

By

Anonymous

[January 14, 2021](https://osdfir.blogspot.com/2021/01/container-forensics-with-docker-explorer.html "permanent link")

Introduction As previous blog posts on cloud forensics have noted, applications are increasingly being deployed using container orchestration frameworks such as Kubernetes, especially in cloud environments.  Similar to traditional deployments on physical servers or virtual machines (VMs), when a containerised application has a security issue it can lead to a compromise of the underlying compute architecture. In the case of container deployments this means a compromise of the container itself, the container host, or even a wider cluster compromise via abuse of orchestration tools. Often digital forensics is required to establish what went wrong and remediate an...
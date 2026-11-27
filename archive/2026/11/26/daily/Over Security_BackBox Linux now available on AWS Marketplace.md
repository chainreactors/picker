---
title: BackBox Linux now available on AWS Marketplace
url: https://blog.backbox.org/2026/11/26/backbox-linux-now-available-on-aws-marketplace/
source: Over Security
date: 2026-11-26
fetch_date: 2026-11-27T10:17:22.534707
---

# BackBox Linux now available on AWS Marketplace

Search
Search

[![BackBox.org Blog](https://www.backbox.org/wp-content/uploads/2018/09/website_backbox_text_black.png)](https://blog.backbox.org/)

* [BackBox.org](https://backbox.org)
* [Community](https://community.backbox.org)
* [Blog](https://blog.backbox.org)
* [Forum](https://forum.backbox.org)
* [Membership](https://members.backbox.org)
* [Sitemap](https://www.backbox.org/sitemap)
* [Contact](https://www.backbox.org/contact)
* [Click to open the search input field
  Click to open the search input field

  Search](?s= "Click to open the search input field")
* **Menu**
  Menu

[![](https://blog.backbox.org/wp-content/uploads/sites/6/2026/11/aws-marketplace-cover-845x321.png)](https://blog.backbox.org/wp-content/uploads/sites/6/2026/11/aws-marketplace-cover-1030x579.png "aws-marketplace-cover")

# BackBox Linux now available on AWS Marketplace

November 26, 2026/in [News](https://blog.backbox.org/category/news/)

The BackBox Team is happy to announce that BackBox Linux 10 is now available on AWS Marketplace as an official Amazon Machine Image (AMI), published by [BackBox Labs](https://backbox.dev).

In a few clicks you can launch BackBox Linux on Amazon EC2, in any standard AWS Region, and start working over SSH a couple of minutes later: no ISO to download, no virtual machine to set up.

**What’s in the image**

* BackBox Linux 10, based on Ubuntu 26.04 LTS: the same release as the ISO, as a lean system without a desktop
* The BackBox security tools, installed by category after the launch with a single command
* Sign-in as the user `backbox` with your EC2 key pair: no passwords, SSH keys only
* IMDSv2 only, ENA networking and NVMe storage
* Security updates for the base system from Ubuntu, and the tools from the BackBox archive

**Getting started**

1. Open the BackBox Linux page on AWS Marketplace and subscribe: <https://aws.amazon.com/marketplace/pp/prodview-xwv5fo666r7fw>
2. Launch an instance (t3.medium is the recommended type) with your key pair, and allow SSH from your own address only
3. Connect:
   `ssh -i KEY_FILE backbox@PUBLIC_DNS_NAME`
4. Install the tools you need, for example:
   `sudo apt update && sudo apt install backbox-information-gathering`

`apt-cache depends backbox-tools` lists the 16 categories. To install all of them at once (`sudo apt install backbox-tools`), give the instance a root volume of 30 GB or more; add `--no-install-recommends` for a smaller installation without the graphical tools. Metasploit Framework is not part of the image: when you need it, install it with [Rapid7’s installer](https://docs.metasploit.com/docs/using-metasploit/getting-started/nightly-installers.html).

**Pricing**

BackBox Linux is free: there is no charge for the software. You only pay AWS for the resources you use, such as the EC2 instance, its storage and data transfer.

**Use it responsibly**

Test only the systems you own or are authorized to test, and follow the [AWS policy on penetration testing](https://aws.amazon.com/security/penetration-testing/).

**Ready for AI agents**

The choices that keep the image lean also make it a good fit for AI agents: it is reached over SSH, the tools the categories depend on are all command line programs (the graphical ones are only recommended), and an agent can install with apt just the category a task needs, when it needs it. That is how [BackBox AI](https://backbox.dev/en/backbox-ai.html), the agentic platform for penetration testing developed by BackBox Labs, already works today: its operations run on BackBox Linux, and it installs the tools a task calls for when the task calls for them.

**Published by BackBox Labs**

The image is built, published and maintained on AWS Marketplace by [BackBox Labs](https://backbox.dev/en/), the cybersecurity company born from the BackBox ecosystem, which supports the community project with resources, research and technology. BackBox Linux remains a free, community-driven open source project.

More details on the official cloud page: <https://linux.backbox.org/cloud/>.

##### Share this entry

* [Share on Facebook](https://www.facebook.com/sharer.php?u=https://blog.backbox.org/2026/11/26/backbox-linux-now-available-on-aws-marketplace/&t=BackBox%20Linux%20now%20available%20on%20AWS%20Marketplace)
* [Share on X](https://twitter.com/share?text=BackBox%20Linux%20now%20available%20on%20AWS%20Marketplace&url=https://blog.backbox.org/?p=1216)
* [Share on Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fblog.backbox.org%2F2026%2F11%2F26%2Fbackbox-linux-now-available-on-aws-marketplace%2F&description=BackBox%20Linux%20now%20available%20on%20AWS%20Marketplace&media=https%3A%2F%2Fblog.backbox.org%2Fwp-content%2Fuploads%2Fsites%2F6%2F2026%2F11%2Faws-marketplace-cover-705x397.png)
* [Share on LinkedIn](https://linkedin.com/shareArticle?mini=true&title=BackBox%20Linux%20now%20available%20on%20AWS%20Marketplace&url=https://blog.backbox.org/2026/11/26/backbox-linux-now-available-on-aws-marketplace/)
* [Share on Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fblog.backbox.org%2F2026%2F11%2F26%2Fbackbox-linux-now-available-on-aws-marketplace%2F&name=BackBox%20Linux%20now%20available%20on%20AWS%20Marketplace&description=)
* [Share on Vk](https://vk.com/share.php?url=https://blog.backbox.org/2026/11/26/backbox-linux-now-available-on-aws-marketplace/)
* [Share on Reddit](https://reddit.com/submit?url=https://blog.backbox.org/2026/11/26/backbox-linux-now-available-on-aws-marketplace/&title=BackBox%20Linux%20now%20available%20on%20AWS%20Marketplace)
* Share by Mail

https://blog.backbox.org/wp-content/uploads/sites/6/2026/11/aws-marketplace-cover.png
675
1200

admin

https://www.backbox.org/wp-content/uploads/2018/09/website\_backbox\_text\_black.png
admin2026-11-26 11:02:372026-11-26 11:52:08BackBox Linux now available on AWS Marketplace

Search
Search

### Categories

* [News](https://blog.backbox.org/category/news/)
* [Releases](https://blog.backbox.org/category/releases/)

### Archives

Archives

Select Month
 November 2026
 June 2026
 December 2024
 October 2024
 November 2023
 November 2022
 May 2020
 June 2019
 February 2019
 August 2018
 March 2018
 July 2017
 June 2017
 April 2017
 December 2016
 September 2016
 May 2016
 April 2016
 March 2016
 January 2016
 October 2015
 July 2015
 April 2015
 February 2015
 January 2015
 October 2014
 September 2014
 May 2014
 March 2014
 February 2014
 January 2014
 October 2013
 September 2013
 June 2013
 May 2013
 February 2013
 January 2013
 October 2012
 September 2012
 July 2012
 June 2012
 April 2012
 March 2012
 January 2012
 December 2011
 November 2011
 September 2011
 August 2011
 May 2011
 March 2011
 January 2011
 December 2010
 October 2010
 September 2010
 August 2010
 July 2010

Copyright © BackBox.org

* [Link to X](https://x.com/backbox_org "Link to X")
* [Link to Facebook](https://www.facebook.com/backbox.org/ "Link to Facebook")
* [Link to LinkedIn](https://www.linkedin.com/company/backbox-org "Link to LinkedIn")
* [Link to Youtube](https://www.youtube.com/%40backbox-org "Link to Youtube")
* [Link to Telegram](http://t.me/backbox_org "Link to Telegram")

[Link to: BackBox Linux 10 released!
Link to: BackBox Linux 10 released!

BackBox Linux 10 released!![](https://blog.backbox.org/wp-content/uploads/sites/6/2026/11/backbox-10-cover-80x80.png)](https://blog.backbox.org/2026/11/19/backbox-linux-10-released/ "Link to: BackBox Linux 10 released!")

[Scroll to top
Scroll to top

 Scroll to top](#top "Scroll to top")
---
title: BYODC - Bring Your Own Domain Controller
url: https://blog.zsec.uk/byodc-attack/
source: ZeroSec - Adventures In Information Security
date: 2022-11-05
fetch_date: 2025-10-03T21:47:51.046122
---

# BYODC - Bring Your Own Domain Controller

[![ZephrSec - Adventures In Information Security](https://blog.zsec.uk/content/images/2025/05/YoutubeHeader-Recovered-1.png)](https://blog.zsec.uk)

* [About Andy Gill/ZephrFish](https://blog.zsec.uk/about/)
* [Pre-register for my course](https://blog.zsec.uk/mae/)
* [My Books](https://leanpub.com/b/LearningTheRopes)
* [LTR101 Posts](https://blog.zsec.uk/tag/ltr101/)
* [Photo Blog](https://photos.zsec.uk/)
* [Pre-register for my course](https://blog.zsec.uk/mae/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

[redteam](/tag/redteam/)

 Featured

# BYODC - Bring Your Own Domain Controller

BYODC or bring your own domain controller is a post-exploitation technique and another option for performing a DCSync in a more opsec safe manner.

* [![Andy Gill](/content/images/size/w100/2017/10/ZSIcon.png)](/author/andy/)

#### [Andy Gill](/author/andy/)

04 Nov 2022
• 6 min read

![BYODC - Bring Your Own Domain Controller](/content/images/size/w2000/2022/11/IMG_20221023_111913_163.jpg)

Over the years, I've been doing internal testing and compromising domains; adding machines to the domain has been done many times. A standard domain user can add up to 10 devices to the domain by default.

Something that I've been playing about recently with adding machines to the domain is bringing your own domain controller(BYODC).  Add a server to the domain, install the roles required, run DCPromo, let it sync, pull the DIT and then finally demote it and clean up; job done!

It is an attack path that many may not have considered, but it also bypasses a lot of detections that folks will likely have for DCSync, secretsdump and other methods of syncing domain hashes. Aligning the tactic to real-world attacks, it has been noted in the past whereby attacker groups bring a virtual machine into an environment and leverage it as the initial point of access, thus circumventing controls in place on the endpoint.

At the same time, BYODC is not identical to this technique. It follows the same process to nullify endpoint protection measures by bringing a new environment into the environment.

## Pre-Reqs

* Domain Admin
* Be able to add a machine to the domain, either via VPN or connectivity in another manner.
* Windows Server Image, I chose 2019 but any one will do
* Read this post and have fun

## Domain Recon

Before adding anything into the environment, first, as an attacker or adversary, we want to profile the domain and hostname scheme in use; the biggest opsec fail here is to name it something that will stand out a mile away! By identifying the naming scheme in place either by using something like ADExplorer or some PowerShell like:

```
Get-ADComputer  -Filter 'samAccountName -like "*DC*"'|select name  |format-table
```

![](https://blog.zsec.uk/content/images/2022/11/image-1.png)

From this example, we can see the naming convention is along the lines of ZSECDC-00X, for DCs and similar for workstations. In addition (thanks to [@theluemmel](https://twitter.com/theluemmel?ref=blog.zsec.uk)), the following can also be executed:

`Get-addomaincontroller`

From a domain-connected machine, it'll give you the domain controllers.

## DC Creation and DCPromo

The first step in the attack is to spin up a server; any version of Windows Server will work. From an operational security perspective, you can pick one that aligns with the same or similar OS as the environment. Nothing sticks out more than a sea of Server 2019 and one Server 2012 box randomly appearing!  For this example, I will build a Server 2019 box to blend into an environment.

Once the VM is up, the first thing we want to do is rename it to match the naming convention of the environment (if you already know it), as, by default, Windows names its servers WIN-RANDOMSTRING:

![](https://blog.zsec.uk/content/images/2022/10/image-5.png)

In this instance, I've renamed mine to ZSECDC-002 to match the already established server naming ZSECDC-xxx, where xxx is a number. As noted in the domain recon stage above.

![](https://blog.zsec.uk/content/images/2022/11/image.png)

Once our machine is renamed,  next is to set the DNS to a static value of the DNS server or DC on the estate:

![](https://blog.zsec.uk/content/images/2022/11/image-2.png)

Once we have DNS setup, we can add our machine to the domain and install AD Domain services before promoting our machine to a domain controller. For this, we'll need the domain admin password of the target domain, zsec.uk:

![](https://blog.zsec.uk/content/images/2022/11/image-4.png)

Before rebooting the machine, we'll do a few opsec lockdown things to prevent the client or defenders from logging into the machine later on. First, navigate to computer management > groups > administrators; we want to remove everyone but the local admins to ensure that DAs from other systems can't log in at a later date:

![](https://blog.zsec.uk/content/images/2022/11/image-14.png)

Next, we will add only the singular domain admin account we've compromised as a user that's allowed to do administrative tasks. So that the blue team can't automatically log in and see what's happening. Additionally, when you add your machine to the network, it'll be added to the Computers container by default in the active directory.

Once added, we can navigate to the server manager and then promote this machine to a domain controller:

![](https://blog.zsec.uk/content/images/2022/11/image-5.png)

Click through till you get to the additional options; we want to select the primary DC if possible; if it's not an option, select Replicate from 'Any Domain Controller':

![](https://blog.zsec.uk/content/images/2022/11/image-6.png)

Once our DC is promoted, windows will reboot, and we're good to start the 'legitimate' replication.

## Grabbing the NTDS.dit

The ****ntdsutil**** is a command line tool part of the domain controller ecosystem. Its purpose is to enable administrators to access and manage the windows Active Directory database. However, it can be abused by penetration testers and red teams to take a snapshot of the existing ntds.dit file can be copied into a new location for offline analysis and extraction of password hashes. For this particular instance, we are going to take a copy on our newly created DC and pull the file off the disk without triggering an alarm of secretsdump/DCSync ;) as we control the DC, and there's no additional endpoint protection on here:

```
ntdsutil
activate instance ntds
ifm
create full C:\Users\Administrator\Desktop\ntdsutil
quit
quit
```

![](https://blog.zsec.uk/content/images/2022/11/image-11.png)

Once these files are outputted to wherever you want, in this instance, I outputted them to `C:\Users\Administrator\Desktop\ntdsutil\`. Two folders are created, the Active Directory and Registry folders:

![](https://blog.zsec.uk/content/images/2022/11/image-12.png)

You can convert them to a usable output using secrets dump on another system with secrets. To dump them, all that's required is the `ntds.dit` and `system` hive files which are stored in the two folders created.

```
python secretsdump.py -ntds ntds.dit -system system LOCAL
```

### Cleanup

Next comes cleanup; there are a few things that can be done here; the first would be to demote the domain controller, which can be done via the server manager:

![](https://blog.zsec.uk/content/images/2022/11/image-13.png)

Upon demotion, the server is no longer a DC, and you've got the NTDS safe and sound! You can also remove the server object from the computers OU.

## Detection

While this attack is technically the inners of a DCSync, it does not have the same characteristics. Thus, the event log entries are slightly different too. Depending on how the machine is added to the domain will impact how this is logged, too; if added in a standard manner, there should be a new machine in the Computers OU of Active Directory, which will raise Event ID 4741 and Event ID 4743 codes within the event log.

To see these Event IDs in Event Viewer (ei...
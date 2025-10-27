---
title: SSH Major Compromise Vector for Linux
url: https://sandflysecurity.com/blog/ssh-major-compromise-vector-for-linux
source: Sandfly Security Blog RSS Feed
date: 2023-01-06
fetch_date: 2025-10-04T03:08:57.045450
---

# SSH Major Compromise Vector for Linux

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# SSH Major Compromise Vector for Linux

05 January 2023

Linux Security

Google just released their [Cybersecurity Action Team Report for the end of 2022](https://services.google.com/fh/files/blogs/gcat_threathorizons_full_jan2023.pdf) and it had some interesting findings:

* More than 1/2 of all incidents involved weak credentials, no credentials, or stolen keys of some type.
* SSH was targeted in over 26% of the cases (presumably many of which are Linux in the cloud).

This figure from the report breaks down the data:

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Google Cloud Compromise Factors](https://www.datocms-assets.com/56687/1672884665-google-cloud-security-report-targeted-software.png?auto=format&dpr=2&q=60&w=920 "Google Cloud Compromise Factors")

In particular they state:

> *Weak passwords continued to be the most common factor at 41% of observed compromises. However, API key compromise played a role in nearly 20% of cases studied last quarter. In terms of which software was most targeted in Q3, we observed significant diversification. SSH was targeted in 26% of cases, but Jenkins and PostgreSQL were close behind at around 22% and 17%, respectively.*Google Cybersecurity Action Team

At Sandfly we have seen many compromises happen on Linux using bruteforced or stolen SSH credentials. SSH credentials represent severe exposure if compromised as they are frequently un-monitored and allow intruders to hide inside encrypted traffic to avoid detection.

> *SSH credentials represent severe exposure if compromised as they are frequently un-monitored and allow intruders to hide inside encrypted traffic to avoid detection.*Sandfly Security

Although the Google report focuses on cloud enabled services, the reality is that SSH use is widespread across all Linux instances whether in the cloud or on-premise.

In addition to the recommendations in the above report that are Google Cloud specific, we would like to offer some of our own that apply to cloud and non-cloud Linux deployments.

## Block SSH Access and Use Jump Hosts

The first defense principle is to simply not allow systems to speak to SSH services unless they have a specific need. The primary way to do this is to implement tight network controls (such as firewall rules or private network addresses) to prevent external systems from speaking directly to SSH. After limiting access with tight network controls, you can implement a jump host to centralize SSH authentication into a small number of tightly monitored and secured systems.

Often security teams face the frustrating task of dealing with multiple systems that they do not control. If you are able to blanket restrict SSH access you can quickly limit potential exposure even if you cannot implement perfect security controls immediately on the endpoints. The fewer systems you have that are talking to SSH services on your network, the safer you will be.

## Disable Password Authentication for SSH

Password authentication for SSH has a number of problems, the biggest of which are that humans are very bad at picking good passwords. When you require the use of public/private keys for SSH the end user does not get to choose a bad SSH key. It is generated for them and is much harder to attack. We have seen countless pieces of Linux malware bruteforce passwords. We have never seen any Linux malware bruteforce an SSH key.

> *We have seen countless pieces of Linux malware bruteforce bad passwords. We have never seen any Linux malware bruteforce an SSH key.*Sandfly Security

The second reason to disable password authentication for SSH is to keep credentials from being stolen if the remote system is compromised. A compromised system can have the SSH service tampered with to log username/password combinations when someone tries to login. These credentials can be immediately used to enable lateral movement. When you use public/private keys, a compromised SSH service has no ability to recover usable credentials from the key negotiation process. This makes it considerably harder for an attacker as they must obtain a user's private key vs. easily grabbing a password being handed to them on a compromised host.

## Clean Up SSH authorized\_keys Files

Often organizations will add keys to SSH *authorized\_keys* files that are scattered all over the place. Over time it becomes increasingly difficult to maintain this system as users come and go. It is better to use automated systems to maintain these files, but many organizations may not be doing this. If you have lapsed on your key file management, it would be a good time to audit all the files and make sure the users with keys in them really need them there. It is very easy for stale or orphaned keys to remain in these files (sometimes for years).

We have seen users with dozens of keys present in their *authorized\_keys* files. This is a huge risk as it means an attacker's key can be easily buried in a long list keys to allow login. It also means that old keys that could be lying about anywhere could be used to login and nobody knows who has them.

## Use SSH Key Certificates

SSH has a lesser-known feature called SSH key certificates. SSH key certificates offer a significant increase in security vs. traditional *authorized\_keys* use. The main benefits are:

* You can shut off use of *authorized\_keys* across all your hosts.
* You can give a very short expiration time on how long credentials will work.
* A stolen private key does not grant access to all systems.

The use of SSH key certificates requires more planning, but if you are able to implement it then you can effectively control the damage caused by a stolen key. This is because you can attach a short-lived expiration time to a login credential (e.g. a week, a day, or even five minutes). This is a big advantage over a private key that has **no** expiration time.

Certificates also take away the ability for users to put keys into *authorized\_keys* files as you can disable them across the entire system in the SSH config once you enable certificates. Inserting a key into a user's *authorized\_keys* file simply won't work*.* Additionally, a stolen private key cannot work by itself for login as it requires a valid signed certificate which is controlled by centralized authentication in your organization. SSH key certificates and an extra layer of protection on top of simple public/private key use.

This topic is covered in this tutorial put out by Facebook/Meta:

[Scalable and Secure Access with SSH](https://engineering.fb.com/2016/09/12/security/scalable-and-secure-access-with-ssh/)

And another going into more details:

[Using SSH Certificates](https://www.sweharris.org/post/2016-10-30-ssh-certs/)

This solution requires more upfront effort, but can be worth the trouble in the long-run if you depend on SSH to run your infrastructure.

## Key Vaults

There are now a variety of key vault solutions that will manage authentication credentials for you. Users authenticate against they key vault for the endpoint they wish to access and the key vault will manage the credentials on the endpoint. The benefit this provides is a central point of control where users can login to and how long that credential will work once issued. This makes limiting access much easier.

These solutions have various ways this is accomplished and we recommend you research them to see if they are a fit for your organization.

## Monitor and Track SSH Keys

The final recommendation we have is to start monitoring and tracking SSH key usage across your systems. Sandfly's [SSH Key Hunter](https://sandflysecurity.com/platform/ssh-credential-security/) is able to agentlessly monitor SSH keys an...
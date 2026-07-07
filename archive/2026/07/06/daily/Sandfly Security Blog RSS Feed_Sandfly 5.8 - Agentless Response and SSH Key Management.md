---
title: Sandfly 5.8 - Agentless Response and SSH Key Management
url: https://sandflysecurity.com/blog/sandfly-58-agentless-response-and-ssh-key-management
source: Sandfly Security Blog RSS Feed
date: 2026-07-06
fetch_date: 2026-07-07T06:03:22.013601
---

# Sandfly 5.8 - Agentless Response and SSH Key Management

[Sandfly 5.8 - Agentless Response and SSH Key Management. Learn More](/blog/sandfly-58-agentless-response-and-ssh-key-management)

[Partners](/partners)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 5.8 - Agentless Response and SSH Key Management

29 June 2026

Product Update

Sandfly 5.8 has been released with a major new feature customers have asked for: **Agentless Response.**

Sandfly's agentless response allows incident responders to perform the following actions on any host we monitor:

* Retrieve any process binary or file
* Suspend or kill a process
* Resume a process
* Delete an SSH key
* Cleanup duplicate SSH keys

The response features work across all Linux distributions, CPU architectures, and system ages we support. This means we cover cloud systems, on-prem, modern, legacy, embedded, and architectures like Intel, AMD, ARM, MIPS, IBM POWER and IBM S390.

### Fast Response and Safe Investigation

The new response feature allows for fast agentless investigation of everything from servers to embedded devices without needing to deploy any endpoint agents. It is a major convenience and speed advantage for defenders investigating incidents.

We have three pillars of operation that make the response feature valuable to security and operations teams:

* **Safe limited access** - Agentless response through Sandfly means operations teams can allow security personnel to investigate alerts without needing to grant them direct SSH or other access to the system.
* **No external command execution** - Sandfly does not allow external or third-party commands to be run in any form. Sandfly never exposes systems to potentially malicious external commands or binaries that can be run by an operator.
* **Response disabling** - For customers that want no response actions at all, we have a way to disable the feature as an external cut-off both at the server and node config (see below and our documentation).

### Agentless Response In Action

Sandfly's agentless response allows security teams investigating a Linux host to do one of multiple actions:

* Download a running process binary (even if deleted from the disk to evade forensics)
* Download a file that was subject to an alert
* Kill or suspend a process
* Resume a suspended process
* Delete an SSH key
* De-duplicate SSH keys

The new respond button will appear for any alert where a response action is available. Below we see an example of an alert from a suspicious process running from a *memfd* socket on Linux.

For the process response, we can *kill*, *suspend*, *resume*, or *retrieve* the process binary.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Agentless response details](https://www.datocms-assets.com/56687/1782695488-process-memfd-response.png?auto=format&dpr=2&q=60&w=920 "Agentless response details")

### Retrieving Process Binary or Files

Security teams can directly download a running process binary for further analysis or sandbox detonation. Teams can also download suspicious files associated with an alert (e.g., a suspicious file under a binary directory).

All response actions are recorded in the new *Response Action Log*. Response actions are logged with full details of the event and alert associated with the activity. Retrieved files are stored like events and are available for download by an authorized user without needing to query the host again.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Agentless response grabbing process binary.](https://www.datocms-assets.com/56687/1782695778-response-action-log.png?auto=format&dpr=2&q=60&w=920 "Agentless response grabbing process binary.")

Operators can go into any action to review the data or download the file if requested. Sandfly can retrieve a running process binary or file associated with an alert. For instance, Sandfly can grab the *crontab* or a suspicious file from an alert. Sandfly can also retrieve a running process binary where the binary has been deleted from the disk to evade detection and forensics.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Downloading a suspicious process binary on Linux.](https://www.datocms-assets.com/56687/1782695928-process-memfd-download-full-details.png?auto=format&dpr=2&q=60&w=920 "Downloading a suspicious process binary on Linux.")

### SSH Key Management and Response

Another feature we've been asked about is helping to cleanup the mess often associated with SSH keys. In particular, customers have been using our SSH Hunter to help identify SSH key usage across their systems. The SSH Hunter can help determine key usage on hosts and users and is valuable for helping set up secure perimeters to find new keys that have been added maliciously with SSH Security Zones.

However, customers also wanted a way to deal with the problem with direct action. We now can do that using two mechanisms:

* SSH key deletion everywhere or per-user.
* Duplicate SSH key cleanup

### Delete the SSH Key Everywhere

Often enterprises will have old keys lying about that should be removed. These keys may belong to ex-employees or ancient login credentials that nobody remembers why they are there or if they are being used. These are both major security risks and are very common.

With Sandfly, customers can now remove those keys wherever they find them and mark them as banned. Customers will get an alert if the keys show up again (e.g., as restored from a backup).

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Agentless SSH key removal.](https://www.datocms-assets.com/56687/1782696754-ssh-key-delete.png?auto=format&dpr=2&q=60&w=920 "Agentless SSH key removal.")

### Delete SSH Key Per User

Another problem we see involves keys on a user account customers no longer want there. For instance, a customer has found that people are logging in using their own ID but also have their key on another user on the same host (e.g., root). Users can quickly remediate this situation by selecting the host and user and removing just that key.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Agenless SSH key removal and clean-up.](https://www.datocms-assets.com/56687/1782696568-ssh-key-delete-single-user.png?auto=format&dpr=2&q=60&w=920 "Agenless SSH key removal and clean-up.")

### Duplicate SSH Keys - What Are They?

Yet another very common problem we see and hear from customers is duplicate SSH keys which get flagged by Sandfly.

So, what is a duplicate SSH key?

A duplicate SSH key is one that shows up in an *authorized\_keys* file more than once. For instance, a key at *authorized\_keys* entry #2 and entry #4 for the account. This means that if someone were to remove entry #4 because they don't want it used for login, the old key at entry #2 (that they didn't see was there) will still allow access.

Duplicate keys are a common problem in enterprises and generally are caused in three ways:

* Someone inserts a key and then someone else comes along and inserts the same key into the *authorized\_keys* file later not knowing it was already present.
* A configuration or key manager inserts a key and then doesn't remove it later. It then comes back and reinserts the key without checking if it already exists. The old key stays active forever and is never removed.
* Poorly written malware drops a backdoor key repeatedly when it infects a system without checking if it already has done so. Keys can pile up on the infected system. In this case the duplicate key alert may show that a system has been compromised!

In all three cases, the duplicate key is hard to see as it is a big block of random data. Humans will easily miss the key. Finding duplicates needs to be done automatically. Sandfly will alert customers to this condition with a policy violation like below.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly duplicate SSH key policy al...
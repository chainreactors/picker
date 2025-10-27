---
title: Sandfly 4.3.0 - Key Vault Integration, Process, SSH, and Persistence Attack Detection
url: https://sandflysecurity.com/blog/sandfly-4-3-0-key-vault-integration-process-ssh-and-persistence-attack-detection
source: Sandfly Security Blog RSS Feed
date: 2023-01-25
fetch_date: 2025-10-04T04:43:23.107515
---

# Sandfly 4.3.0 - Key Vault Integration, Process, SSH, and Persistence Attack Detection

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 4.3.0 - Key Vault Integration, Process, SSH, and Persistence Attack Detection

24 January 2023

Product Update

Sandfly 4.3.0 features an external credential provider interface. Using our new integration you can get Sandfly to work with an external key vault such as Cyberark, Thycotic, Hashicorp and more.

We have also added in new checks for process hiding, suspicious SSH process activity, cron persistence attacks plus others. Improvements have also been made to better handle containers running inside the *btrfs* and *zfs* file systems. Finally, we have major upgrades for database performance, enhanced filtering, custom views inside the UI, and improved graphing.

## External Credential Provider/Key Vault Integration

Although Sandfly uses strong elliptic key cryptography to protect system credentials, customers have often wanted us to integrate with their key vault provider such as Hashicorp, Cyberark, Thycotic and others. Now, we have an ability to integrate with these solutions using a simple but innovative service module architecture.

Once integration is done, Sandfly will obtain credentials securely from your key vault and they are encrypted fully in transit so even the Sandfly server itself cannot read them at any time. Credentials are used on demand and not stored.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly Credential Provider/Key Vault Integration](https://www.datocms-assets.com/56687/1674532156-credential-provider.png?auto=format&dpr=2&q=60&w=920 "Sandfly Credential Provider/Key Vault Integration")

You can work with us to integrate into your key vault of choice. Please [contact us](https://sandflysecurity.com/contact-us/) for more details and help us understand your needs.

## New Process Hiding, SSH, and Persistence Attacks

We have added in multiple ways to find Linux processes being concealed by attackers trying to mount a file system over the process table entry. This tactic was demonstrated by Tim Brown in a [Gist disclosure](https://gist.github.com/timb-machine/602d1a4dace4899babc1b6b5345d24b2) and we felt it viable enough to want to detect it for customers.

We also added in several new checks for artifacts from Linux backdoor activity which can include processes left running after spawning from old SSH connections, suspicious spawned shells, and processes left with no active TTY session. These can all indicate SSH initiated backdoor or similar activity and are useful for incident response or detecting active attacks.

Finally, we put in other checks for *crontab* tactics including attackers trying to drop schedules into *.placeholder* file names. We also added new checks inside other persistence checking modules.

## Process File System Directory Spoofing Attack

This tactic uses a file system mount over top of a legitimate PID under */proc.* By mounting a file system over the */proc* entry, an attacker can create a file system that mimics what the process would normally have on Linux, but use forged data to hide process activity and more.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux process tampering with mounted file system.](https://www.datocms-assets.com/56687/1674527596-sandfly_process_running_hidden_proc_dir_spoofing.png?auto=format&dpr=2&q=60&w=920 "Linux process tampering with mounted file system.")

## Process Mount Over Attack

Related to the above is a second artifact of the attack. Instead of flagging a directory mounted over a specific process, we'll also flag any file system mounted over portions of the */proc* directory on Linux. This detection can find variants of the above attack.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Linux process hiding with /proc mount.](https://www.datocms-assets.com/56687/1674527607-process_running_hidden_mount_over.png?auto=format&dpr=2&q=60&w=920 "Linux process hiding with /proc mount.")

## Shell Running From Detached SSH Session

Shells spawned in interactive mode (e.g. *bash -i*) but from a detached SSH session can hide activity on Linux. When we see a shell running in this state it is often Linux backdoor activity and will be flagged.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![BASH shell backdoor running from detached SSH session.](https://www.datocms-assets.com/56687/1674527776-process_shell_running_detached_ssh.png?auto=format&dpr=2&q=60&w=920 "BASH shell backdoor running from detached SSH session.")

## SSH known\_hosts Under root and Default Users

The *root* user and default users on Linux (e.g. *bin, nobody, www*) are frequently targeted for attack with successful intruders then leveraging them for lateral movement. Part of this process involves using SSH which will often leave behind a *known\_hosts* file under their respective directory. When we see a critical user like *root* or a default user with a *known\_hosts* file we will flag it as an alert to investigate.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Default Linux user with suspicious SSH known_hosts file present.](https://www.datocms-assets.com/56687/1674530816-user_ssh_known_hosts_default_user.png?auto=format&dpr=2&q=60&w=920 "Default Linux user with suspicious SSH known_hosts file present.")

## Other SSH Checks

We have added additional checks for processes left over from prior SSH sessions, those without a TTY, and more. These can be used for incident response to help identify suspicious processes spawned by SSH across systems. Customers can search for all our SSH related checks by using the filter in the sandfly list and simply searching for "ssh" in the name field.

## Cron Placeholder and Other Persistence Checks

We have improved and added in new checks for *cron* and other areas of persistence across system boot files and more. New checks include searching for non-comment entries under *cron .placeholder* files plus improved search patterns for other persistence attacks.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Cron with malicious entry under .placeholder](https://www.datocms-assets.com/56687/1674528841-process_cron_placeholder_entry.png?auto=format&dpr=2&q=60&w=920 "Cron with malicious entry under .placeholder")

## Unauthorized Account Custom Sandfly Template

By customer request, we added in a new template called *user\_unauthorized\_account* to the sandfly inventory. This template can be modified such that you can put in a list of known-good account names on your systems. It will generate an alert if a username shows up that was not in the known-good list you provided. Below we see the account for a user called *php* being flagged for alert that was not in the known-good list.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Unauthorized user alert on Linux with Sandfly.](https://www.datocms-assets.com/56687/1674601029-unauthorized_user_present.png?auto=format&dpr=2&q=60&w=920 "Unauthorized user alert on Linux with Sandfly.")

Licensed users can find this new check in the list of available templates. Customers can clone it to a new name and modify it with the usernames you choose. Activate the sandfly after cloning and it will begin running on normal schedules.

## Improved Container Scanning on btrfs and zfs

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly detects container attack.](https://www.datocms-assets.com/56687/1674604013-docker-container-attack.png?auto=format&dpr=2&q=60&w=920 "Sandfly detects container attack.")

We have implemented changes to how we manage the *btrfs* and *zfs* file systems on Linux. Process and file detection engines have been updated to lower false alarm risk and provide more accurate results fo...
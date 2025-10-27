---
title: Update to RTRBK - Diff and File Dates in PowerShell, (Wed, Jan 4th)
url: https://isc.sans.edu/diary/rss/29400
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-05
fetch_date: 2025-10-04T03:06:01.563995
---

# Update to RTRBK - Diff and File Dates in PowerShell, (Wed, Jan 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29394)
* [next](/diary/29404)

# [Update to RTRBK - Diff and File Dates in PowerShell](/forums/diary/Update%2Bto%2BRTRBK%2BDiff%2Band%2BFile%2BDates%2Bin%2BPowerShell/29400/)

**Published**: 2023-01-04. **Last Updated**: 2023-01-04 13:54:05 UTC
**by** [Rob VandenBrink](/handler_list.html#rob-vandenbrink) (Version: 1)

[0 comment(s)](/diary/Update%2Bto%2BRTRBK%2BDiff%2Band%2BFile%2BDates%2Bin%2BPowerShell/29400/#comments)

I use my RTRBK script pretty much every week, every single time that I work with a client that doesn't have their network gear in a backup cycle in fact.  (for a review of this tool, see the original post [https://isc.sans.edu/diary/RTRBK+Router+Switch+Firewall+Backups+in+PowerShell+tool+drop/22079](https://isc.sans.edu/diary/RTRBK%2BRouter%2BSwitch%2BFirewall%2BBackups%2Bin%2BPowerShell%2Btool%2Bdrop/22079) )
Anyway, I was considering how I could improve this script, aside from adding more and more device types to the backups.  A "diff" report was my obvious first thought - why didn't I have this in there from the start?

Diffing your nightly config backups allows you to:

* ensure that config changes aren't being made outside of your change control process
* ensure that ONLY the approved changes are implemented
* if you compare changes to the login events in your  syslog, you can verify that the right people / right accounts are logging in to make these changes

How to do this in powershell?  It turns out that it's native to the language, and implemented two ways.  Let's compare a (much) older backup file with the current backup.

First, this is the "looks like regular PowerShell" version of the command:

 Compare-Object (Get-Content .\ASA01.2021-31-07-09-31.cfg.bk) (get-content ./ASA01.cfg)

Or, to redirect it to a file:

 Compare-Object (Get-Content .\ASA01.2021-31-07-09-31.cfg.bk) (get-content ./ASA01.cfg) > ASA01.diff.txt

A second way to skin this cat uses a different version of the command, but calls the exact same code under the covers and gives you the exact same output, but might be easier to remember and "friendlier" to folks who are coming to PowerShell from a \*nix background:

diff (cat .\ASA01.2021-31-07-09-31.cfg.bk) (cat .\ASA01.cfg)

Some typical output of this "diff" command might look like:

-----------                                                                                                         ---
show startup                                                                                                        =>
: Written by rvandenbrink at 20:56:23.320 EST Mon Dec 12 2022                                                       =>
ASA Version 9.14(4)                                                                                                 =>
enable password \*\*\*\*\* pbkdf2                                                                                        =>
passwd \*\*\*\*\* encrypted                                                                                              =>
boot system disk0:/asa9-16-3-23-lfbff-k8.SPA                                                                        =>
boot system disk0:/asa9-14-4-lfbff-k8.SPA                                                                           =>
access-list VPNGRP\_splitTunnelAcl standard permit 172.16.99.0 255.255.255.0                                         =>
asdm image disk0:/asdm-7181-152.bin                                                                                 =>
 key \*\*\*\*\*                                                                                                          =>
crypto ipsec ikev1 transform-set ESP-3DES-SHA esp-aes esp-sha-hmac                                                  =>
 protocol esp integrity sha-1                                                                                       =>
 protocol esp integrity sha-1                                                                                       =>
 protocol esp integrity sha-1                                                                                       =>
 protocol esp encryption aes                                                                                        =>
 protocol esp integrity sha-1                                                                                       =>
 protocol esp encryption aes                                                                                        =>
 protocol esp integrity sha-1                                                                                       =>
crypto ipsec df-bit clear-df outside                                                                                =>
 group 19 5                                                                                                         =>
 group 5                                                                                                            =>
 group 5                                                                                                            =>
: Written by rvandenbrink at 15:50:38.181 EST Fri Feb 19 2021                                                       <=
ASA Version 9.12(4)2                                                                                                <=
enable password $sha512$5000$idL1fwSW4iN+O1ZY/2ajsA==$dZm2YBtjqLe4ulG9sPCWjw== pbkdf2                               <=
passwd tIBh8hSmm6StbwU0 encrypted                                                                                   <=
                                                                                                                    <=
boot system disk0:/asa9-12-4-2-lfbff-k8.SPA                                                                         <=
asdm image disk0:/asdm-openjre-7141-48.bin                                                                          <=
asdm location GMPDC01 255.255.255.255 inside                                                                        <=
 key 4QTW595wxHNkdmhTrmWe                                                                                           <=
crypto ipsec ikev1 transform-set ESP-3DES-SHA esp-3des esp-sha-hmac                                                 <=
 protocol esp integrity sha-1 md5                                                                                   <=
 protocol esp integrity sha-1 md5                                                                                   <=
 protocol esp integrity sha-1 md5                                                                                   <=
 protocol esp encryption 3des                                                                                       <=
 protocol esp integrity sha-1 md5                                                                                   <=
 protocol esp encryption des                                                                                        <=
 protocol esp integrity sha-1 md5                                                                                   <=
 group 19 5 2                                                                                                       <=
 group 5 2                                                                                                          <=
 group 5 2                                                                                                          <=

As can be seen from the above output, there's been an ASA version update, which in turn "retired" a number of IPSEC (ESP) algorithms and DH (Diffie Hellman) groups.  These were all expected changes, and had to be reflected at the other end of the VPN tunnel during the update.

Another useful bit of manipulation is to rename a file based on it's last modified dat...
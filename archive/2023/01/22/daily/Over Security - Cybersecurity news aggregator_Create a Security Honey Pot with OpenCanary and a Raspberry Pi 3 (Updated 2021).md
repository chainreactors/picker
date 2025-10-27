---
title: Create a Security Honey Pot with OpenCanary and a Raspberry Pi 3 (Updated 2021)
url: https://bobmckay.com/i-t-support-networking/hardware/create-a-security-honey-pot-with-opencanary-and-a-raspberry-pi-3-updated-2021/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-22
fetch_date: 2025-10-04T04:33:56.961886
---

# Create a Security Honey Pot with OpenCanary and a Raspberry Pi 3 (Updated 2021)

[![Bob McKay's Blog](https://bobmckay.com/wp-content/uploads/2014/01/Bob-McKay-Branding-Logo-Ideas-V8.png)](https://bobmckay.com)

Search

* [Home](https://bobmckay.com/)
* [Web & Programming](https://bobmckay.com/category/web/)
  + [Classic ASP](https://bobmckay.com/category/web/classic-asp/)
  + [WordPress](https://bobmckay.com/category/web/wordpress/)
  + [SQL & Databases](https://bobmckay.com/category/web/sql-databases/)
  + [SASS & CSS](https://bobmckay.com/category/web/sass-css/)
  + [PHP](https://bobmckay.com/category/web/php/)
* [I.T. & Network](https://bobmckay.com/category/i-t-support-networking/)
  + [Cisco](https://bobmckay.com/category/i-t-support-networking/cisco/)
  + [Plesk](https://bobmckay.com/category/i-t-support-networking/plesk/)
  + [Hosting](https://bobmckay.com/category/i-t-support-networking/hosting/)
  + [Hardware](https://bobmckay.com/category/i-t-support-networking/hardware/)
* [Info Sec](https://bobmckay.com/category/i-t-support-networking/security/)
* [Misc.](https://bobmckay.com/category/life/ "Stuff that doesn’t fit anywhere else")
  + [Spanish](https://bobmckay.com/category/life/spanish/)
* [About](https://bobmckay.com/about/)
* [Contact](https://bobmckay.com/contact/)

[Home](https://bobmckay.com) / [IT Support & Networking](https://bobmckay.com/category/i-t-support-networking/) / [Cyber Security](https://bobmckay.com/category/i-t-support-networking/cyber-security/) / Create a Security Honey Pot with OpenCanary and a Raspberry Pi 3 (Updated 2021)

### Posts navigation

![Create a Security Honey Pot with OpenCanary and a Raspberry Pi 3 (Updated 2021)](https://bobmckay.com/wp-content/uploads/2021/09/HoneyPot-RaspberryPI-OpenCanary-Blog-Post-Cover-848x400.jpg)

# Create a Security Honey Pot with OpenCanary and a Raspberry Pi 3 (Updated 2021)

I’ve created an updated version of [my original Raspberry Pi 3 Honey Pot tutorial](https://bobmckay.com/i-t-support-networking/ethical-hacking/creating-a-cyber-security-honey-pot-with-thinkst-canary-a-raspberry-pi/) after I discovered it doesn’t work with newer versions of the Linux operating systems.

After banging my ahead against **a lot** of combinations of OS versions, configurations, depedancy issues and configuration issues, I finally got a simple working walkthrough from start to finish.  Enjoy and if you have any issues, please post in the comments!

[![Raspberry PI 3 logo](https://bobmckay.com/wp-content/uploads/2021/09/RPi-Logo-Reg-SCREEN-150x150.png)](https://bobmckay.com/wp-content/uploads/2021/09/RPi-Logo-Reg-SCREEN.png)Like the original tutorial, this is based a Raspberry PI 3 but should work just as well for a Raspberry PI 2 (I used the headless version of Raspbian to keep it light) or the Raspberry PI 4.

I always liked the idea of a cost-effective honey pot that could be dropped on to a physical network with the minimum of fuss.  As Raspberry Pi 3s are cheap, ubiquitous and well-supported it seemed a no-brainer.  Combine this with a a case, a 32GB sd-card
 and the [OpenCanary](https://github.com/thinkst/opencanary) software and you have a great little solution for minimal spend.

OpenCanary, for those that don’t know, is the open source version of the [Thinkst Canary](https://canary.tools/) honeypot.

### OS Installation

I’m very happy to say that since my last tutorial, the dependancy and Python issues seem to have been resolved with Raspian, allowing us to use the native OS for the device.

As mentioned above, I opted for the “Lite” (headless) version which means it **comes with no desktop or gui interface – its command line only**.   I did this because I wanted the best performance from the device, no unnecessary applications/services and OpenCanary is entirely command line anyway.

Finally, OpenCanary’s own installation steps suggest running OpenCanary in a virtual container.  Given that its unlikely I’m going to be using my Raspberry Pi for an additional workload, I install directly to keep things simple.

#### Prepare the SD card

[![](https://bobmckay.com/wp-content/uploads/2020/09/Raspberry-Pi-Imager-Software-Ubuntu-18-32bit-1-300x199.gif)](https://bobmckay.com/wp-content/uploads/2020/09/Raspberry-Pi-Imager-Software-Ubuntu-18-32bit-1.gif)Download and run the Raspberry PI Imager software available here: <https://www.raspberrypi.org/downloads/>

Insert your SD card in to your reader

On the Raspberry PI Imager, select the **Raspberry PI OS (other)** option from the Operating System menu

Select **Raspberry Pi OS Lite (32-bit)**

**Select your SD card** (double check, personally I tend to remove any other flash drives or SD cards just in case!)

[![](https://bobmckay.com/wp-content/uploads/2020/09/Raspberry-Pi-Imager-Software-2-300x199.gif)](https://bobmckay.com/wp-content/uploads/2020/09/Raspberry-Pi-Imager-Software-2.gif)Click **Write**

Click **Yes** to confirm you understand all data on the SD card will be destroyed

This will take a while so go grab a cup of tea (and biscuits if you have them)

#### Enable SSH

By default, SSH is disabled on Raspberry PI devices so if you are going to be configuring this remotely, you **must** turn this on first.

The easiest way to do this is while you still have the SD card in your computer after formatting it.

Simply open the partition called “boot” in Windows Explorer (or equivalent) and create an empty file there with a filename of either **ssh** or **ssh.txt**.

When your Raspberry PI boots up, if it finds either of those files, it enables the SSH service (and deletes the files).

#### Logging in

The default username/password for Raspbian is **pi**/**raspberry**.

#### Updating the OS

Run a full update of Raspbian (this can take a while):

```
sudo apt-get update && sudo apt-get upgrade -y
```

### Hide Your Pi

Given that the whole idea of a honey pot is to make it look like a tasty target to attackers, having it clearly show up as a Raspberry PI when they do a network scan is going to be a bit of a giveaway.  Typically this IDing is done from the MAC address of the network adapter and the hostname the device identifies itself using, fortunately these are reasonably easy to change.

For the purposes of this tutorial, we are going to disguise the Raspberry PI as a Synology NAS so we’ll need a MAC address from the pool used by Synology, a good searchable resource for manufacturer MAC addresses can be found [here](https://www.adminsub.net/mac-address-finder/Synology).

Taking one of the Synology NAS prefixes – 001132 – we need to add additional hexadecimal values to make it a proper length and we need to punctuate it with colons to be the proper format.  Doing this, 001132 becomes:

**00:11:32:B3:4D:F5**

We’ll be using **nano** to edit a lot of configuration files, if you’re not familiar with it, check this tutorial: <https://linuxize.com/post/how-to-use-nano-text-editor/>

Now we have a Synology NAS MAC address, let’s tell our Raspberry PI to identify itself using that:

```
sudo nano /boot/cmdline.txt
```

When nano loads, you will need to paste “smsc95xx.macaddr=” appended with your new MAC address, at the end of the string of text in the cmdline.txt file, adding a simple space to the end of what is already in there (so our additional text doesn’t touch the previous value).  Using my example, I’ll therefore be adding smsc95xx.macaddr=00:11:32:B3:4D:F5 to the end of the file, resulting in the file reading:

```
console=serial0,115200 console=tty1 root=PARTUUID=96f1abd5-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait smsc95xx.macaddr=00:11:32:B3:4D:F5
```

Next, lets update the hostname, enter:

```
sudo nano /etc/hosts
```

Now replace the entry next to 127.0.1.1 (raspberrypi) to your servername.  Think about what a real server might be called, such as FILESERVER or BACKUPSERVER.

Now enter:

```
sudo nano /etc/hostname
```

And change the raspberrypi value with the same servername from the previous step.

Now reboot your device, remember when it reboots it will likely have a different IP addre...
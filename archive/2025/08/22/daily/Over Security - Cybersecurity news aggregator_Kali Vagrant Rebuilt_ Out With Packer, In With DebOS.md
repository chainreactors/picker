---
title: Kali Vagrant Rebuilt: Out With Packer, In With DebOS
url: https://www.kali.org/blog/kali-vagrant-rebuilt/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-22
fetch_date: 2025-10-07T00:49:48.402048
---

# Kali Vagrant Rebuilt: Out With Packer, In With DebOS

* [Join Free CTF](https://www.offsec.com/events/the-gauntlet/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* [Get Kali](https://www.kali.org/get-kali/)
* [Blog](https://www.kali.org/blog/)
* Documentation

  [Documentation Pages](https://www.kali.org/docs/)
  [Tools Documentation](https://www.kali.org/tools/)
  [Frequently Asked Questions](https://www.kali.org/faq/)
  [Known Issues](https://bugs.kali.org/search.php?project_id=1&category_id[]=General%20Bug&category_id[]=Kali%20Package%20Bug&category_id[]=Kali%20Package%20Improvement&status[]=30&status[]=40&status[]=50&sticky=on&sort=id%2Clast_updated&dir=DESC%2CDESC&hide_status=-2&match_type=0)
* Community

  [Community Support](https://www.kali.org/community/)
  [Forums](https://forums.kali.org/)
  [Discord](https://discord.kali.org/)
  [Join Newsletter](https://www.kali.org/newsletter/)
  [Mirror Location](https://http.kali.org/README?mirrorlist)
  [Get Involved](https://www.kali.org/docs/community/contribute/)
* [Courses](https://www.offsec.com/kali-training/courses/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* Developers

  [Git Repositories](https://gitlab.com/kalilinux)
  [Packages](https://pkg.kali.org/)
  [Auto Package Test](https://autopkgtest.kali.org/)
  [Bug Tracker](https://bugs.kali.org/)
  [Kali NetHunter Stats](https://nethunter.kali.org/)
* About

  [Kali Linux Overview](https://www.kali.org/features/)
  [Press Pack](https://gitlab.com/kalilinux/documentation/press-pack/-/archive/main/press-pack-main.zip)
  [Wallpapers](https://www.kali.org/wallpapers/)
  [Kali Swag Store](https://offsec.usa.dowlis.com/kali/view-all.html)
  [Meet The Kali Team](https://www.kali.org/about-us/)
  [Partnerships](https://www.kali.org/partnerships/)
  [Contact Us](https://www.kali.org/contact/)

LIGHT
[ ] DARK

![](https://www.kali.org/blog/kali-vagrant-rebuilt/images/banner-kali-vagrant-refresh.jpg)
Thursday, 21 August 2025

# Kali Vagrant Rebuilt: Out With Packer, In With DebOS

Table of Contents

* [Demo](#demo)
  + [Cheat-Sheet](#cheat-sheet)
* [More Reading](#more-reading)

Vagrant files, `*.box`, are pre-configured Virtual Machines (VM) VM images, which when imported into HashiCorp’s Vagrant, allow for VMs to be interacted with via the command line.
You create, start, interact, stop, destroy VMs all without leaving the terminal. *Think containers (Docker/Podman), but for VMs.*

---

Previously we have been using [HashiCorp’s Packer](https://developer.hashicorp.com/packer) to generate our [HashiCorp’s Vagrant](https://developer.hashicorp.com/vagrant) images.

Packer is a wrapper, around whatever hypervisor you wish, and it will automate installing the OS (unattended setup via [preseeding](https://gitlab.com/kalilinux/recipes/kali-preseed-examples)), run any commands or scripts, export the VM and finally compress it.

The down-side to Packer is that you need to have the chosen hypervisor installed on the host OS, you can’t cross-build. If you use Linux, you can’t build Window’s Hyper-V.

---

For [a few years now](https://www.kali.org/blog/kali-vm-builder-weekly/), we have been using [DebOS](https://github.com/go-debos/debos), to automate building [our VMs](https://gitlab.com/kalilinux/build-scripts/kali-vm). This has been working great for us.

Recently we realized: “*Why do we have two different systems, for the same purpose?*”.
A little bit of digging into “[how to make a vagrant base box VM](https://developer.hashicorp.com/vagrant/docs/boxes/base)” boils down to just a few requirements:

* Fix username *(`vagrant`)*
* Fix/Known pubic SSH keys *([default/standard insecure keypairs](https://github.com/hashicorp/vagrant/tree/main/keys))*
* Able to perform superuser actions *(`sudo`)*

Simple really, just need to make sure that Vagrant can easy access the VM!

Optional items (and recommended), as it helps benefits user’s rather than Vagrant:

* Known/Fix credentials *(`vagrant` everywhere)*
* SSH tweaks *(speed up for airgap networks)*

All of this can be handled in a [post-install step](https://gitlab.com/kalilinux/build-scripts/kali-vm/-/blob/main/scripts/setup-vagrant.sh), which we have **put into our Kali-VM build-script**.

---

Now, we are building all of our VMs, automatically, in the same matter (Stock and Vagrant), all in the same infrastructure setup (Linux!).

---

Since Microsoft Windows 10 1607 / Server 2016, when exporting VMs, there would be 3 additional “binary” files, `*.vmcx/*.vmrs` included as well as an `*.xml`. As we were no longer exporting the VM from Hyper-V, but generating it outside of, we do not have these files.

Now, we could create a “*template*” binary which would act as a dummy marker.

But this didn’t sit right with us, we didn’t want to include items, especially binary files.

---

Out of the box, Vagrant expected those binary files and failed without them. However a [merge request](https://github.com/hashicorp/vagrant/pull/13691) later to upstream, and support has been added. As a result, trying to use Kali 2025.2 or higher on Windows using Hyper-V, using vagrant older than `v2.4.7` will NOT work. You need to use either an older Kali, different hypervisor, manually patch or to **upgrade Vagrant to be `v2.4.8` *(released 2025-08-05)*** or higher.

---

As Packer is no longer generating our Vagrant VMs, **we renamed the git repository** ([gitlab.com/kalilinux/build-scripts/kali-vagrant](https://gitlab.com/kalilinux/build-scripts/kali-vagrant) -> [gitlab.com/kalilinux/build-scripts/kali-packer](https://gitlab.com/kalilinux/build-scripts/kali-packer)).

Finally, before **sunsetting our Packer build-scripts, we did a refresh of these build-scripts** one more time. *We might not be using it, but that doesn’t mean you can’t.*

---

## Demo

After getting [Vagrant and VirtualBox installed](https://gitlab.com/kalilinux/build-scripts/kali-packer/-/blob/main/README.vagrant.md):

```
$ vagrant box add kalilinux/rolling
==> box: Loading metadata for box 'kalilinux/rolling'
    box: URL: https://vagrantcloud.com/api/v2/vagrant/kalilinux/rolling
This box can work with multiple providers! The providers that it
can work with are listed below. Please review the list and choose
the provider you will be working with.

1) hyperv
2) libvirt
3) virtualbox
4) vmware_desktop

Enter your choice: 3
==> box: Adding box 'kalilinux/rolling' (v2025.2.1) for provider: virtualbox (amd64)
    box: Downloading: https://vagrantcloud.com/kalilinux/boxes/rolling/versions/2025.2.1/providers/virtualbox/amd64/vagrant.box
    box: Calculating and comparing box checksum...
==> box: Successfully added box 'kalilinux/rolling' (v2025.2.1) for 'virtualbox (amd64)'!
$
$ vagrant box list
kalilinux/rolling (virtualbox, 2025.2.1, (amd64))
$
$ mkdir -pv vagrant-demo/; cd vagrant-demo/
mkdir: created directory 'vagrant-demo/'
$
$ vagrant init --force --minimal kalilinux/rolling
[...]
$
$ cat Vagrantfile
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "kalilinux/rolling"
end
$
$ vagrant up --provider virtualbox
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'kalilinux/rolling'...
==> default: Generating MAC address for NAT networking...
==> default: Checking if box 'kalilinux/rolling' version '2025.2.1' is up to date...
==> default: Setting the name of the VM: vagrant-demo_default_1753960552589_87147
Vagrant is currently configured to create VirtualBox synced folders with
the `SharedFoldersEnableSymlinksCreate` option enabled. If the Vagrant
guest is not trusted, you may want to disable this option. For more
information on this option, please refer to the VirtualBox manual:

  https://www.virtualbox.org/manual/ch04.html#sharedfolders

This option can be disabled globally with an environment variable:

  VAGRANT_DISABLE_VBOXSYMLINKCREATE=1

or on a per folder basis within the Vagrantfile:

  config.vm.synced_folder '/host/path', '/guest/path', SharedFoldersEnableSymlinksCreate: false
==> default: Clearing any previous...
---
title: DFU mode
url: https://eclecticlight.co/2026/04/16/dfu-mode/
source: Instapaper: Unread
date: 2026-04-17
fetch_date: 2026-04-18T04:33:42.701721
---

# DFU mode

[Skip to content](#content)

[![](https://eclecticlight.co/wp-content/uploads/2015/01/eclecticlightlogo-e1421784280911.png?w=103)](https://eclecticlight.co/)

# [The Eclectic Light Company](https://eclecticlight.co/)

Macs & painting – 🦉 No AI content

##### Main navigation

Menu

* [Downloads](https://eclecticlight.co/downloads/)
* [Freeware](https://eclecticlight.co/free-software-menu/)
* [All Macs](https://eclecticlight.co/mac-problem-solving-2-2/)
* [M1-M5 Macs](https://eclecticlight.co/m1-macs-2/)
* [Troubleshooting](https://eclecticlight.co/mac-troubleshooting-summary/)
* [Painting](https://eclecticlight.co/painting-topics-2-2/)
* [Mac Front Page](https://eclecticlight.co/category/macs/)

[hoakley](https://eclecticlight.co/author/hoakley/)
[April 16, 2026](https://eclecticlight.co/2026/04/16/dfu-mode/)
[Macs](https://eclecticlight.co/category/macs/), [Technology](https://eclecticlight.co/category/technology/)

# **DFU** mode

When Apple introduced the first iPhone it built into its ROM a new startup mode that didn’t rely on other firmware, to enable recovery of a bricked or troubled device: *Device Firmware Upgrade,* or DFU, mode. This was added to Intel Macs with the introduction of the T2 chip, and is a fundamental feature of all Apple silicon Macs. If your Mac’s hardware is still capable of booting from its ROM, and it supports DFU mode, it may well enable that Mac to be rescued from disaster.

All Macs start up from their ROM initially, and that provides essential services to support the boot process, from checking the integrity of the next stage, the low-level bootloader, to handing over to that. Boot ROMs in Macs with T2 or Apple silicon chips can also be parked in DFU mode, which stops the rest of secure boot from continuing, and waits indefinitely for a connection over a USB port. Another Mac can then connect with the Mac in DFU mode, and can install fresh firmware, or completely initialise the SSD, to resuscitate the Mac in DFU mode.

#### What you need

To use DFU mode, you require:

* the *target* Mac in DFU mode, as detailed below;
* a second Mac, the *host,* either running macOS Sonoma or later, or the current version of Apple Configurator 2 from the App Store;
* a plain USB cable with a USB-C plug at each end. This should support both charging and data over USB. Although Apple has consistently warned that you shouldn’t use a regular Thunderbolt 3 cable, some claim to have got them to work correctly.

If you don’t have all three, you should find your nearest Apple store will help, as will Apple authorised service providers.

#### DFU host

Prepare the second Mac, that’s going to connect to the target Mac in DFU mode, as follows:

* If it’s a laptop model, connect it to mains power.
* Ensure it has a good internet connection.
* If it’s not using Configurator, open Finder Settings and ensure **CDs, DVDs and iOS Devices** is selected to be shown in Finder window sidebars, as that may be necessary to see the target Mac when it connects.
* Connect one end of the USB cable to *any* of its USB-C ports.

#### Put a Mac into DFU mode

Prepare the target Mac that’s going to be put into DFU mode to be resuscitated, as follows:

* Disconnect all non-essential peripherals, particularly any connecting to its USB-C ports.
* Ensure its **DFU port** is available, and connect the other end of the USB cable to that port.
* If it’s a laptop model, connect it to mains power. If it has a MagSafe port, use that if possible.
* If it’s running, shut it down. If you don’t know whether it’s shut down, press and hold the Power button to shut it down. If that starts it up, repeat that to shut it down again.

Apple’s official list of DFU ports [is here](https://support.apple.com/120694). You’ll also find them listed in [MacTracker](https://mactracker.ca). Unfortunately, there’s no simple rule, neither does Apple mark the port.

If the Mac is a **laptop** model, having ensured it’s connected to mains power and shut down, press the Power button briefly as if to start it up normally, then immediately press and hold **Control** and **Option** on the left of its keyboard, **Shift** on the right, and the **Power** button, all at once. Keep pressing all four keys for 10 seconds, then release Control, Option and Shift, and continue holding the Power button for another 10 seconds, until the host Mac shows the DFU window. If you’re shown an alert asking for consent to connect the accessory, release the Power button and click the **Allow** button.

Laptops with a T2 chip should display the DFU window on the host after holding the four keys for a shorter period of about 3 seconds, and don’t require the full process needed for an Apple silicon Mac.

If the Mac is a **desktop** model, having ensured that it’s shut down, disconnect the target Mac from mains power by unplugging its power cable, then press and hold its Power button and connect the Mac to mains power again. You may then need to continue holding its Power button for up to 10 seconds before you see the DFU window on the host Mac, and can release that button. If you’re shown an alert asking for consent to connect the accessory, release the Power button and click the **Allow** button.

Although putting a Mac into DFU mode isn’t really that difficult, lack of feedback from the target Mac makes this seem challenging. In DFU mode, a laptop Mac appears completely dead, and even mains adaptors don’t light up to provide any sign of life. Desktop models are more helpful, as the power status light on Mac Studio, Mac mini and Mac Pro models should show amber, and may even flash.

#### Revive or Restore?

The DFU window on the host Mac offers two options, to Revive or Restore the target Mac in DFU mode.

When reviving, the firmware on the target Mac is reinstalled without erasing the rest of its SSD. Unless you intend to perform a full Restore, this should normally be your first choice. It’s also significantly quicker.

The default version of firmware and macOS used for these is the latest compatible with that Mac. For Apple silicon Macs, you can instead download a different IPSW image file to use, if you prefer. This enables you to perform a full downgrade to an earlier version of macOS complete with its firmware. Links to Apple’s library of IPSW files are provided by [Mr. Macintosh](https://mrmacintosh.com/apple-silicon-m1-full-macos-restore-ipsw-firmware-files-database/), and others. However, this isn’t available for Macs with T2 chips, which can only install the current firmware for that model.

A full Restore not only reinstalls the firmware, but it also erases the SSD completely and returns it to ‘factory’ condition, as it was when it was first unboxed. This erases all your data, as well as reinstalling firmware and macOS, so you will then need to migrate your data from a backup, which makes it considerably longer to complete.

Following either of these, the target Mac should restart into Recovery mode, back into macOS, or into initial personalisation and configuration as if it was new. If a Revive fails, try a full Restore, and if that fails, you might be successful with a second attempt, or you’ll need to get your Mac assessed at an Apple store, or by an Apple authorised service provider.

#### Key points

* Use a USB cable, not Thunderbolt 3.
* Check and use the correct DFU port on the Mac in DFU mode.
* Laptops: left Control and Option, right Shift, and Power for 10 seconds, then Power alone for up to 10 seconds.
* Desktops: disconnect from power, press and hold Power button and reconnect power cable, continue holding Power button for up to 10 seconds.
* Try Revive first.
* [Apple’s support note](https://support.apple.com/108900).

I wish you success!

### Share this:

* [Share on X (Opens in new window)
  X](https://eclecticlight.co/2026/04/16/dfu-mode/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://eclecticlight.co/2026/04/16/dfu-mode/?share=facebook)
* [Share on Reddit (Opens in n...
---
title: Thomas Fitzsimmons: Pixel phones are sold with bootloader unlocking disabled
url: https://www.fitzsim.org/blog/?p=545
source: Planet Classpath
date: 2023-05-06
fetch_date: 2025-10-04T11:39:31.607404
---

# Thomas Fitzsimmons: Pixel phones are sold with bootloader unlocking disabled

[Skip to content](#content)

[fitzsim's development log](https://www.fitzsim.org/blog/)

# Pixel phones are sold with bootloader unlocking disabled

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1) [May 5, 2023May 11, 2023](https://www.fitzsim.org/blog/?p=545)
[3 Comments on Pixel phones are sold with bootloader unlocking disabled](https://www.fitzsim.org/blog/?p=545#comments)

***Request to Google**: ungrey the “OEM unlocking” toggle in the factory, before shipping store.google.com devices to customers. Do not make your customers connect the device to the Internet before they are allowed to install the operating system they want.*

My wife had a requirement to use Android[1](#footnote-1), and she wanted to run GrapheneOS; I experimented with other devices and ROMs to ensure the specific application she needed would run on GrapheneOS.

As part of my research, I read the GrapheneOS installation guide[2](#footnote-2), which stated:

*Enabling OEM unlocking*

*OEM unlocking needs to be enabled from within the operating system.*

*Enable the developer options menu by going to Settings > About phone and repeatedly pressing the build number menu entry until developer mode is enabled.*

*Next, go to Settings > System > Developer options and toggle on the ‘OEM unlocking’ setting. On device model variants (SKUs) which support being sold as locked devices by carriers, enabling ‘OEM unlocking’ requires internet access so that the stock OS can check if the device was sold as locked by a carrier.”*

None of the many many YouTube videos I watched about bootloader unlocking covered whether or not you need Internet connectivity. Nor did any of Google’s official documentation[3](#footnote-3). GrapheneOS documentation is the only place on the Internet that documents this requirement, so, well done GrapheneOS documentation team!

GrapheneOS only supports recent Google Pixel phones. Those phones are nice hardware[4](#footnote-4), and I can easily (so I thought) install a different operating system, so I decided to buy one. To be as future-proof as possible, I bought a Pixel 7 Pro from store.google.com (Canada).

I thought (based on the aforementioned GrapheneOS docs) that the device model variant I bought, being sold “unlocked”[7](#footnote-7) by Google, would not need the Internet connection. **NOPE**; Google sold it to me with “OEM unlocking” greyed out:

![The Pixel 7 Pro Developer options settings screen, showing the OEM unlocking slider greyed out, with the label Connect to the internet or contact your carrier](https://www.fitzsim.org/screenshots/google-pixel-7-pro-sold-oem-locked.png)

I consider this a customer-hostile practice. I should not have to connect a piece of hardware to the Internet, even once, to use all of its features. If I hadn’t connected the Pixel 7 Pro to the Internet, then “OEM unlocking” would have stayed greyed out, thus I would not have been able to unlock the bootloader, thus I would not have been able to install GrapheneOS[5](#footnote-5).

Keep in mind that I bought this phone full price[6](#footnote-6) from store.google.com, where it was advertised right in the FAQ as an “unlocked smartphone”[7](#footnote-7). There is zero carrier involvement here, so carriers cannot be blamed for this policy. Also, I paid full price for the phone, so this is not a case of “if you don’t pay for the product, you ARE the product”.

I probably should have returned the device for a refund. Instead, I set up a network debugging environment to see what activity happens when I connect the Pixel 7 Pro to the Internet.

By tailing some log files and watching them closely, I was able to determine that the final site accessed just before “OEM unlocking” goes from greyed to ungreyed is “**afwprovisioning-pa.googleapis.com**“. Here is the video of “OEM unlocking” ungreying:

[[A video showing the moment the OEM unlocking slider ungreys, i.e., becomes operable](https://www.fitzsim.org/screenshots/oem-unlocking-ungreying.webm)](https://www.fitzsim.org/screenshots/oem-unlocking-ungreying.webm)

Here is the rest of the network activity, all of which is TLS-encrypted by keys buried in the stock Google operating system, and thus not controlled by the device purchaser:

| Hostname | Downloaded to phone | Uploaded from phone |
| --- | --- | --- |
| storage.googleapis.com | 383 MiB | 8 MiB |
| fonts.gstatic.com | 137 MiB | 3 MiB |
| afwprovisioning-pa.googleapis.com | 18 MiB | 1 MiB |
| www.gstatic.com | 8 MiB | 287 kiB |
| googlehosted.l.googleusercontent.com | 8 MiB | 345 kiB |
| ota-cache1.googlezip.net | 3 MiB | 175 kiB |
| dl.google.com | 3 MiB | 86 kiB |
| instantmessaging-pa.googleapis.com | 1 MiB | 300 kiB |
| www.google.com | 46 kiB | 24 kiB |
| ssl.gstatic.com | 25 kiB | 3 kiB |
| ota.googlezip.net | 17 kiB | 6 kiB |
| digitalassetlinks.googleapis.com | 17 kiB | 4 kiB |
| clients.l.google.com | 14 kiB | 7 kiB |
| gstatic.com | 13 kiB | 3 kiB |
| mobile-gtalk.l.google.com | 8 kiB | 1 kiB |
| mobile.l.google.com | 5 kiB | 1 kiB |
| lpa.ds.gsma.com | 5 kiB | 4 kiB |
| connectivitycheck.gstatic.com | 3 kiB | 3 kiB |
| app-measurement.com | 1 kiB | 0 bytes |
| time.android.com | 180 bytes | 180 bytes |

Only Google knows precisely what all that data is and what it is used for.

As the video shows, the ungreying did happen; I had the Settings application open, then connected the phone to the Internet. I had to close then re-open the Settings application; the access to “**afwprovisioning-pa.googleapis.com**” seemed to be co-timed with the Settings application restart. After the Settings appliation restart, the “OEM unlocking” option was operable.

I don’t know what subset of the hosts in the above table need to be accessible to the phone for ungreying to take place; I considered firewalling each individually using a script, but I ran out of time. I also don’t know if a factory reset of the phone results in “OEM unlocking” being greyed again. I ended my experimentation when the ungreying took place and I proceeded to install GrapheneOS successfully (the rest of the process was very straightforward, thanks to GrapheneOS’s great documentation and installation scripts).

All in all, cheers to Google for releasing Android as Free and Open Source software, and for selling devices which are (with steps) bootloader-unlockable; both of which make GrapheneOS feasible[8](#footnote-8). Jeers to Google for selling devices from store.google.com that cannot have their bootloaders unlocked without first connecting them to the Internet.

#### Footnotes

1. One day I hope we can both use PinePhones. [^](#sup-1)
2. <https://grapheneos.org/install/cli#enabling-oem-unlocking> [^](#sup-2)
3. <https://source.android.com/docs/core/architecture/bootloader/locking_unlocking>

   *“Devices should deny the fastboot flashing unlock command unless the get\_unlock\_ability is set to 1. If set to 0, the user needs to boot to the home screen, open the Settings > System > Developer options menu and enable the OEM unlocking option (which sets the get\_unlock\_ability to 1). After setting, this mode persists across reboots and factory data resets.”* [^](#sup-3)
4. Google Pixel devices lack several features of my PinePhone; luxuries such as a 3.5mm audio jack, a swappable battery, a microSD card slot, and HDMI output (with a hardware mod). [^](#sup-4)
5. The “lock”/”unlock” terminology is hopelessly overloaded; as a result, confusion abounds online, even among phone enthusiasts. The “OEM” term here is also at best confusing and at worst misleading. I hope the screenshot and video make clear the specific context of this post, but here are definitions, and the states of the device I’m discussing:
   * “greyed” => the user interface element is inoperable
   * “ungreyed” => the user interface element is operable
   * “OEM unlocking” toggle is greyed (this is the state of the device after unboxing and before letting it have an Internet connection)
   * “OEM unlocking” toggle is ungreyed (the ...
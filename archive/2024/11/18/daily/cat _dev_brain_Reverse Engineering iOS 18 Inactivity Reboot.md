---
title: Reverse Engineering iOS 18 Inactivity Reboot
url: https://naehrdine.blogspot.com/2024/11/reverse-engineering-ios-18-inactivity.html
source: cat /dev/brain
date: 2024-11-18
fetch_date: 2025-10-06T19:16:26.162602
---

# Reverse Engineering iOS 18 Inactivity Reboot

[Skip to main content](#main)

### Search This Blog

# [cat /dev/brain](https://naehrdine.blogspot.com/)

Reverse Engineering & Research

### Reverse Engineering iOS 18 Inactivity Reboot

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[November 17, 2024](https://naehrdine.blogspot.com/2024/11/reverse-engineering-ios-18-inactivity.html "permanent link")

# Reverse Engineering iOS 18 Inactivity Reboot

iOS 18 introduced a new inactivity reboot security feature. What does it protect from and how does it work? This blog post covers all the details down to a kernel extension and the Secure Enclave Processor.

## Security Before First Unlock / After First Unlock

Did you know that entering your passcode for the first time after your phone starts is something very different then entering it later on to unlock your phone?

When initially entering your passcode, this unlocks a key store in the Secure Enclave Processor (SEP) that encrypts your data on an iPhone.

The state before entering your passcode for the first time is also called **Before First Unlock** (BFU). Due to the encrypted user data, your iPhone behaves slightly differently to later unlocks. You'll see that Face ID and Touch ID won't work and that the passcode is required. But there's more subtle things you might notice: Since Wi-Fi passwords are encrypted, your iPhone won't connect to Wi-Fi networks. If your SIM is not PIN-protected, your iPhone will still connect to cellular networks. That means, technically, you can still receive phone calls. Yet, if you receive a call, even if that number is in your contacts, the contact name won't be shown, as the contacts haven't been decrypted yet. Similarly, when you receive notifications about new messages, you'll see that you got messages, but you won't see any message previews. You can easily try this yourself!

[![](https://blogger.googleusercontent.com/img/a/AVvXsEihQqOut8zLHRxuz_g8ornTF1A-X69IoWpX8lZPnZBisvc1t80zBRGebsCj4x4Vz_6C_i_ImG5AszaaQ-rXnFEJeB1-Dfaj4bSBwajxyKLYoKQNdJ8dZZtaqhexYUc1rZL7w_6yXkMj5APTe30fHOMRlg3da55UCxSZhmTFRLWmBEh_iWVgPSyKuVCEQ_48=w640-h352)](https://blogger.googleusercontent.com/img/a/AVvXsEihQqOut8zLHRxuz_g8ornTF1A-X69IoWpX8lZPnZBisvc1t80zBRGebsCj4x4Vz_6C_i_ImG5AszaaQ-rXnFEJeB1-Dfaj4bSBwajxyKLYoKQNdJ8dZZtaqhexYUc1rZL7w_6yXkMj5APTe30fHOMRlg3da55UCxSZhmTFRLWmBEh_iWVgPSyKuVCEQ_48)

In the **After First Unlock** (AFU) state, user data is decrypted. You can imagine this like a key safe that is kept open while iOS is running. Even when you see a lock screen, certain keys remain available to the operating system. This way, you stay connected to Wi-Fi networks and receive message notification previews, even when your iPhone is locked.

While it's more convenient, the AFU state is more susceptible to attacks. An attacker who can somehow bypass the lock screen can get access to decrypted data on the iPhone. To bypass the lock screen, an attacker does not necessarily need to know the passcode. Security vulnerabilities within iOS can allow attackers to get code execution and extract from an iPhone, even while it appears to be "locked".

Attackers with physical access to an iPhone have more security vulnerabilities to choose from. The attack surface is larger, as such attackers can exploit vulnerabilities in the USB stack or within wireless protocols, such as Wi-Fi, Bluetooth, or cellular, or even more invasive hardware attacks that involve opening the device. This larger attack surface tends to make exploits for these vulnerabilities cheaper on the gray market, as there's potentially more supply. Another factor that makes attacks cheaper is time – vulnerabilities that are publicly known by the vendor and patched in more recent software versions won't unlock new iPhones, but can unlock iPhones that were kept in AFU state for a long time that didn't get any software updates.

## Rumors about Rebooting iPhones

In law enforcement scenarios, a lot of the forensically relevant data is available in the AFU state. Law enforcement takes advantage of this and often keeps seized iPhones powered on, but isolated from the Internet, until they can extract data. This time might be necessary to wait for an exploit to be available or for legal reasons, such as getting a warrant.

However, thieves and other criminals are also interested in getting this kind of access after stealing a device. It gives them access to bank accounts and other valuable information, by far exceeding what the iPhone itself would be worth, or which might be used for blackmail. People reuse their passwords often, and getting access to the iCloud account may allow a thief to reset activation lock for the device, increasing the resale value.

A recent [news article by 404 media](https://www.404media.co/police-freak-out-at-iphones-mysteriously-rebooting-themselves-locking-cops-out/) (while paywalled, the most important information is also contained in the related [Tweet](https://x.com/josephfcox/status/1854615490087551327)) reported on a law enforcement document about suspicious iPhone reboots. This document makes two interesting claims:

1. iPhones on iOS 18 will reboot, even when completely isolated from wireless networks.
2. iPhones on iOS 18 will tell other iPhones on lower iOS versions to reboot – wirelessly!

Especially the second claim would be huge if true. If anyone figured out how this works, they could build a large TV-Be-Gone for iPhones, forcing reboots over the air on hundreds of iPhones simultaneously. Would Apple really build such a feature into an iPhone?

Knowing a thing or two about the Apple wireless ecosystem, my interest was piqued, and I had to go down the rabbit hole!

## Discovery of Inactivity Reboot

When Apple adds new features, they usually don't hide this very well. Apple software contains a lot of debug strings, which hint at new functionality. Blacktop maintains a [git repository](https://github.com/blacktop/ipsw-diffs) of strings found in iOS, which keeps a nice version history. I decided to do the most low-effort thing I could think of: just search for "reboot".

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi4XBZbJShDJ9GPps2OujHTkV_KZn-KcijaJX34M5GsyKk_TMRsUrYkxkft2LiAMa8V62VKXagqP5Q2lQntBlRo9lobsf-7qo39M-DzpWwGgfOioKq8LQs8xAnKIRNrC0b9RlA4FZWYQg4Q1yvcILbr_Lp_Nm0ULdRG9l13_sSB1R5JIP7eYJzYwy9QAwU2=w640-h330)](https://blogger.googleusercontent.com/img/a/AVvXsEi4XBZbJShDJ9GPps2OujHTkV_KZn-KcijaJX34M5GsyKk_TMRsUrYkxkft2LiAMa8V62VKXagqP5Q2lQntBlRo9lobsf-7qo39M-DzpWwGgfOioKq8LQs8xAnKIRNrC0b9RlA4FZWYQg4Q1yvcILbr_Lp_Nm0ULdRG9l13_sSB1R5JIP7eYJzYwy9QAwU2)

Bingo, that third hit looks good: "inactivity\_reboot". The fact that it's in keybagd is interesting: this daemon is related to the key store that is unlocked on the first unlock.

A second search for only inactivity reboot shows the string starts occurring in iOS 18.1 and iOS 18.2. In iOS 18.2, the string changed from "inactivity\_reboot" to "inactivity\_reboot\_enabled", hinting towards more potential changes in the latest iOS 18.2 betas.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgBjM82vk9aCJNzlk-9gbRKwc9y83Z9g9WZsPDUQXxB4oYXsuA-QntGrp4pMalJFUPFqETW0fxy3IfCrlziX946r_ymJ8G0a-mtIkFEzp1DoXPRcq9RUi1KOOtjgK8XfRJJcghzLLgNsM7JfvByjxqfWz2JqHPGEEkXpttCbMvdoCW7FPrfDU-psLHbdgD-=w640-h328)](https://blogger.googleusercontent.com/img/a/AVvXsEgBjM82vk9aCJNzlk-9gbRKwc9y83Z9g9WZsPDUQXxB4oYXsuA-QntGrp4pMalJFUPFqETW0fxy3IfCrlziX946r_ymJ8G0a-mtIkFEzp1DoXPRcq9RUi1KOOtjgK8XfRJJcghzLLgNsM7JfvByjxqfWz2JqHPGEEkXpttCbMvdoCW7FPrfDU-psLHbdgD-)

Something that was still unclear to me at that point is: How long does it take for inactivity reboot to be triggered? A new [article by 404 media](https://www.404media.co/apple-quietly-introduced-iphone-reboot-code-which-is-locking-out-cops/) claimed that it was 3-4 days. So I updated my SRD to the latest beta and made a time lapse.

Turns out, the inactivity reboot triggers exactly after 3 days (72 hours). The iPhone would do so despite being connected to W...
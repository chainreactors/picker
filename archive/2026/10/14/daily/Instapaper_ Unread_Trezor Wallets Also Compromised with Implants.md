---
title: Trezor Wallets Also Compromised with Implants
url: https://www.zetter-zeroday.com/trezor-wallets-also-compromised-with-implants/
source: Instapaper: Unread
date: 2026-10-14
fetch_date: 2026-10-15T06:45:24.966180
---

# Trezor Wallets Also Compromised with Implants

[ZERO DAY](https://www.zetter-zeroday.com)

* [About](https://www.zetter-zeroday.com/about/)
* [Election Security/Critical Infr](https://www.zetter-zeroday.com/)
* [National Security](https://www.zetter-zeroday.com/)
* [Deep Dives](https://www.zetter-zeroday.com/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

# Trezor Wallets Also Compromised with Implants

Despite claims by Trezor today that none of its devices have been compromised -- unlike the devices of its competitor, Ledger -- hardware hacker Joe Grand says he found implants in two Trezor devices and reported this to the company in August.

#### [Kim Zetter](/author/kimzetter/)

Oct 13, 2026
• 5 min read

[comment-1 Created with Sketch Beta.](/trezor-wallets-also-compromised-with-implants/#ghost-comments-root)

![Trezor Wallets Also Compromised with Implants](https://storage.ghost.io/c/77/50/77508a24-24ec-49e5-99f8-d3dadb30a5ac/content/images/size/w2000/2026/10/Screenshot-2026-10-13-at-4.01.25---PM.png)

I published a story this morning about [implants that have been discovered in a number of Ledger crypto devices](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/). In initial had included in the story information about implants that were also discovered in devices made by Trezor – Ledger's main competitor. I removed this, however, before publishing the story because I didn't want to confuse matters.

But a few hours ago Trezor announced on X that it would be reducing the number of merchants authorized to sell its devices out of an "abundance of caution." Chief Commercial Officer Danny Sanders wrote that there was "not a single piece of evidence that Trezor devices have been compromised," and that this was reducing its list of authorized sellers simply as a "preventive step" to have better control over its supply chain.

> To the resellers who helped build Trezor: thank you, and I’m sorry 💔 [pic.twitter.com/RK7KBJOshp](https://t.co/RK7KBJOshp?ref=zetter-zeroday.com)
>
> — Danny (@Dantoshi) [October 13, 2026](https://x.com/Dantoshi/status/2110000117856248141?ref_src=twsrc%5Etfw&ref=zetter-zeroday.com)

But this isn't exactly true. Famed hardware hacker Joe Grand found implants in two Trezor wallets recently and notified the company about them in August. I didn't include this in my Ledger story because the circumstances were different from the Ledger incidents. The Ledger implants became news because the implants were 1) sold in devices distributed by authorized resellers of Ledger devices and 2) the implants were subsequently used to steal $100 million in crypto from the owners of devices that were compromised.

But as I noted in the Ledger story, Grand had initially found implants in four Ledger devices that were sold online by unauthorized Ledger merchants. These merchants appeared to be fly-by-night sellers who popped up in online marketplaces only to disappear after days or weeks. So the provenance of the compromised devices was already sketchy, as opposed to the later implants that were sold by reputable and authorized sellers.

The implants Grand found in Trezor One and Trezor Model T devices were *also* sold by third-party nonauthorized sellers – not by reputable authorized sellers. No real surprise there, since both Ledger and Trezor have warned customers for years to purchase directly from their own web sites or from authorized merchants. Therefore the information that Grand found Trezor wallets compromised by implants didn't seem newsworthy. Especially because three years ago, researchers at Kaspersky Lab had also found an implant in a [Trezor wallet sold on a popular Russian marketplace](https://www.kaspersky.com/blog/fake-trezor-hardware-crypto-wallet/48155/?ref=zetter-zeroday.com). In its report, Kaspersky called it a fake wallet, but it was a real Trezor wallet that had been compromised.

Given that the first Ledger implants appeared in devices sold by unathorized sources – only to then show up in devices sold by authorized sources as well – and given that Trezor has publicly denied knowledge that any of its own devices have been compromised, I think it's now pertinent to disclose the information Grand provided me about the compromised Trezor wallets he found. Especially because it's possible these discoveries might be a precursor to implants showing up in Trezor devices sold by authorized resellers. The fact that Trezor announced that it's de-authorizing some of its resellers shows that it, too, may be worried that the implant problem could spread to devices sold by authorized sellers.

If you find this article valuable, you can
leave a one-time tip to express appreciation to the author.

### Trezor One and Trezor Model T Implants

Grand found an implant in a Trezor Model T wallet that someone had purchased via Facebook Marketplace in Canada some time in 2025 and another one in a Trezor One device that someone had obtained from a TikTok shop in August. The buyer of the Trezor One became suspicious when about $50 got transferred out of his crypto account. Both the Trezor One and Trezor Model T are discontinued devices, but Trezor still supports them (as noted in the product photo at top, the company will continue to distribute software updates until 2031 and security updates until 2036) and customers still buy them from third-party sellers.

In both wallets, the attackers had replaced the microcontroller on the devices so that instead of generating random recovery seed phrases, the controllers generated one of a dozen or so pre-determined seed phrases the attackers had coded into the controllers, allowing them to guess the recovery seeds for the crypto accounts.

Grand says the legitimate microcontrollers used in the Trezor devices have code-protection features that are meant to prevent someone from accessing and changing the code. But because the Trezor code is open source, it was easy for the attackers to obtain the code, modify it, and program it into a new, unsecured device by just replacing the legitimate chip with their own chip.

![](https://storage.ghost.io/c/77/50/77508a24-24ec-49e5-99f8-d3dadb30a5ac/content/images/2026/10/Trezor-One.jpg)

Image of Trezor One device as Joe Grand was extracting the malicious code from it. (Image: Courtesy of Joe Grand and Grand Idea Studio)

Grand says he wrote to Trezor about the Model T implant on August 10 this year and got a very cordial response three days later:

> Thank you for reaching out and for sharing such detailed technical findings. This is very interesting, and we appreciate the work you have put into investigating the device.
>
> Based on your description, the unit has very similar characteristics to the counterfeit or modified Model T devices that were discovered on Russian marketplaces in 2022–2023. The use of a replaced MCU and modified firmware, together with an external microSD card containing legitimate firmware for the integrity check, is a particularly interesting variation on those earlier devices.
>
> We would definitely be interested in examining the binary you extracted from the STM32F427. If you are able to share it with us, please send it over.
>
> We would also be very interested to know how the latest version of Trezor Suite behaves when this device is connected. Does Trezor Suite recognize or flag the device as counterfeit or otherwise indicate that something is wrong?
>
> Although we have discontinued sales of the Model T, we continue to improve the checks in Trezor Suite that are intended to identify counterfeit and modified devices. Any information you can provide about how the current version of Trezor Suite treats this particular unit would therefore be very helpful.
>
> Thank you again for bringing this to our attention and for sharing the technical details of your investigation.
>
> We would be interested to hear about any additional findings as your reverse engineering continues.

Notably, in his last communication from Trezor in early September, the co...
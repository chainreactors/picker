---
title: TVE-2026-01: Xiaomi miIO Protocol Authentication Bypass
url: https://labs.taszk.io/blog/post/112_mi_hshake_bypass/
source: Taszk Labs on taszk.io labs
date: 2026-03-16
fetch_date: 2026-03-17T04:17:17.937265
---

# TVE-2026-01: Xiaomi miIO Protocol Authentication Bypass

[![logo](https://labs.taszk.io/images/taszk_logo.png)
![logo](https://labs.taszk.io/images/taszk_logo_white.png)](https://labs.taszk.io)

* [Home](https://labs.taszk.io/)
* [Articles](https://labs.taszk.io/articles)
* [Advisories](https://labs.taszk.io/blog)
* [Get in touch](https://taszk.io/contact)

## [TVE-2026-01: Xiaomi miIO Protocol Authentication Bypass](https://labs.taszk.io/blog/post/112_mi_hshake_bypass/)

2026-03-16
 by Botond Hartmann
 [Xiaomi](/blog/tags/xiaomi) [wifi](/blog/tags/wifi) [camera](/blog/tags/camera) [smart](/blog/tags/smart)

An attacker sending malformed miIO messages over WiFi to a Xiaomi Smart camera device can trigger the vulnerability described here.

This report describes a secure protocol design issue, which leads to authentication bypass in the proprietary Xiaomi miIO protocol.

The vulnerability described in this advisory affects a potentially wide range of Xiaomi Smart devices. This vulnerability has not yet been issued a public patch or advisory or assigned a CVE by the vendor despite repeated requests and a lapse of more than six months since the original vendor disclosure.

## Vulnerability Details

For packets received in UDP port `54321`, the `miio_client` binary verifies the MAC and then decrypts the received packet. Instead of rejecting packets with a payload size not divisible by 16 bytes, the AES decryption function contains code specifically for this case, which is not normally reached, since packet payloads are correctly padded in the regular case.

```
void AesCbcDecrypt(
    const byte *ciphertext, uint size,
    byte *plaintext, byte *key, byte *iv
) {
  byte *dst;
  const byte *src;

  uint remainder_bytes = size & 0xf;
  copy16(plaintext, ciphertext);
  AesCurrentBlock = plaintext;
  if (key != 0x0) {
    AesKey = key;
    AesKeyExpansion();
  }
  if (iv != 0x0) {
    AesIv = iv;
  }
  uint offset = 0;
  while (true) {
    src = ciphertext + offset;
    dst = plaintext + offset;
    if (size <= offset) break;
    offset = offset + 0x10;
    copy16(dst, src);
    AesCurrentBlock = dst;
    AesBlockDecrypt();
    XorWithIv(dst);
    AesIv = src;
  }
  if (remainder_bytes != 0) {
    copy16(dst, src);
    memset(dst + remainder_bytes, 0, 0x10 - remainder_bytes);
    AesCurrentBlock = dst;
    AesBlockDecrypt();
  }
}
```

The size of the partial block is saved as `remainder_bytes`, but `size` is not decremented by this amount. This causes the last block (in the `if` condition) to read the ciphertext from outside the input buffer, and write the decrypted plaintext outside the output buffer residing on the heap.

Since the program uses the packet length specified in the miIO protocol header, the sender of the packet can control the bytes after the input buffer by sending a UDP packet larger than this length, thereby controlling the 16 bytes that are written past the bounds of the plaintext heap chunk.

# Affected Devices

* verified: Xiaomi C400
* potentially: any Xiaomi Smart device using miIO

# Timeline

* 2025.09.04. Bug reported to Xiaomi PSIRT by email, following the process outlined at <https://trust.mi.com/misrc/response>
* 2025.09.16. Asking for confirmation of report receipt
* 2025.09.19. Xiaomi acknowledges the report by directing us to submit to the hackerone platform.
* 2025.09.19. TASZK responds that we will not participate in their hackerone program and the report has been submitted as-is and that the disclosure will follow <https://taszk.io/disclosure>.
* 2026.02.16. TASZK asks for update and notifies Xiaomi that in accordance with the states policy, we will proceed with disclosure.
* 2026.02.19-24. In a series of emails, Xiaomi first claims they have misplaced their PGP key and ask for the report to be re-sent plaintext, then confirms they have managed to locate their key after we refuse, then claim they have confirmed the vulnerabilities ("`our security team has reviewed your report and confirmed the vulnerabilities`") and repeatedly ask us to join their program for rewards and simultaneaously that we postpone release. They also ask that we provide full exploit code if we have it.
* 2026.02.20-25. TASZK repeatedly confirms that we will do neither and as per request we confirm that we can also provide full exploit POC.
* 2026.03.03. TASZK shares full RCE exploit POC.
* 2026.03.06-10 Xiaomi again provides postponed timeline estimates, does not provide any CVEs, and further requests online meetings to discuss future collaboration opportunities that they want to propose.
* 2026.03.11. TASZK asks for the CVE numbers for the vulnerabilities which have been stated as confirmed and reiterates that we are focused only on this.
* 2026.03.13. Xiaomi writes that they have now changed their minds and think that one vulnerability “`does not currently meet the conditions required for practical exploitation`” and also that their “`standard process`” requires that they “`follow a 6-months disclosure timeline following the OTA release of the corresponding patch`” and that they “`will complete the CVE application process and share the assigned CVE numbers with you as soon as they become available`”.
* 2026.03.16. Advisory release, six and a half months after report. Full exploit POC also released.

### Search

### Tags

[android](/blog/tags/android/)

[baseband](/blog/tags/baseband/)

[bootloader](/blog/tags/bootloader/)

[bootrom](/blog/tags/bootrom/)

[camera](/blog/tags/camera/)

[dma](/blog/tags/dma/)

[huawei](/blog/tags/huawei/)

[hypervisor](/blog/tags/hypervisor/)

[ims](/blog/tags/ims/)

[kernel](/blog/tags/kernel/)

[LTE](/blog/tags/lte/)

[MediaTek](/blog/tags/mediatek/)

[ota](/blog/tags/ota/)

[recovery](/blog/tags/recovery/)

[RIL](/blog/tags/ril/)

[samsung](/blog/tags/samsung/)

[smart](/blog/tags/smart/)

[soc](/blog/tags/soc/)

[ssl](/blog/tags/ssl/)

[toctou](/blog/tags/toctou/)

[trustzone](/blog/tags/trustzone/)

[Unisoc](/blog/tags/unisoc/)

[wifi](/blog/tags/wifi/)

[Xiaomi](/blog/tags/xiaomi/)

### Archives

[2018](/blog/archives/2018/)

[2021](/blog/archives/2021/)

[2022](/blog/archives/2022/)

[2023](/blog/archives/2023/)

[2024](/blog/archives/2024/)

[2025](/blog/archives/2025/)

[2026](/blog/archives/2026/)

### Authors

[Botond Hartmann](/blog/author/botond-hartmann/)

[Daniel Komaromy](/blog/author/daniel-komaromy/)

[kutyacica](/blog/author/kutyacica/)

[Laszlo Radnai](/blog/author/laszlo-radnai/)

[Laszlo Szapula](/blog/author/laszlo-szapula/)

[Lorant Szabo](/blog/author/lorant-szabo/)

[Lorant Szabo, Daniel Komaromy](/blog/author/lorant-szabo-daniel-komaromy/)

[TASZK Security Labs](/blog/author/taszk-security-labs/)

### TOC

* [Vulnerability Details](#vulnerability-details)

### Pages

* [Home](/)
* [Articles](/articles)
* [Advisories](/blog)
* [Get in touch](https://taszk.io/contact)

### Links

### Tags

### TOC

* [Vulnerability Details](#vulnerability-details)

[![logo-footer](https://labs.taszk.io/images/taszk_logo_white.png)
![logo-footer](https://labs.taszk.io/images/taszk_logo.png)](https://labs.taszk.io)

##### Company

TASZK Security Labs SL
Rambla de Catalunya 124, 1-2
08008 Barcelona, Spain

[[email protected]](/cdn-cgi/l/email-protection#3b5854554f5a584f7b4f5a484150155254)

pgp:

[CA86 EB1A E756 13A6 EB30
073F 6BB2 BD92 0E93 5D90](https://labs.taszk.io/taszk.asc)

##### Sitemap

* [Articles](https://labs.taszk.io/articles)
* [Advisories](https://labs.taszk.io/blog)

##### Community

* [Github](https://github.com/TaszkSecLabs)
* [Twitter](https://twitter.com/TaszkSecLabs)

##### We provide clients:

customized solutions for unique challenges in the embedded, mobile, automotive, wireless, and telecommunication technology sectors

##### Fineprint

* [Privacy Policy](https://taszk.io/legal)
* [Disclosure Policy](https://taszk.io/disclosure)
---
title: YuanKong RAT: the Android remote-control service that stamps its operators' names into every build
url: https://starlabs.sg/blog/2026/10-yuankong-rat-the-android-remote-control-service-that-stamps-its-operators-names-into-every-build/
source: Blog on STAR Labs
date: 2026-10-15
fetch_date: 2026-10-16T06:35:45.146155
---

# YuanKong RAT: the Android remote-control service that stamps its operators' names into every build

[![STAR Labs](/images/logo.png)](/)

[About](/about/)
[Services](/services/)
[Advisories](/advisories/)
[Blog](/blog/)
[Achievements](/achievements/)
[Publications](/publications/)
[Team](/team/)
[RSS](/index.xml)

MENU

Research
October 15, 2026
By Jacob Soo
28 min read

# YuanKong RAT: the Android remote-control service that stamps its operators' names into every build

Most Android RATs try hard to hide their server. This one barely hides anything and that turns out to be the interesting part. The dropper leaves the key under the mat: a `vault-config.json` sitting in `assets/` right next to the ciphertext it unlocks, holding the key and IV in cleartext.

![jadx, the dropper’s assets/vault-config.json open in the decompiler: SVLT-XOR-v2 with the base64 key, hex IV, encrypted asset name and the child’s original SHA-256, all in cleartext](/blog/2026/images/YuanKong-RAT-02-vault-config.png)

The child it unpacks is an overlay and remote-control app signed `O=YuanKong` (“YuanKong” / è¿æ§, the Chinese abbreviation of è¿ç¨æ§å¶, “remote control”). It is multi-tenant in a concrete, checkable way: across our set of 110 droppers, 57 distinct child payloads are all signed by one shared certificate (`73cbe8e3730cacfdd208f22eab468bb5495a78c0eb2cb37eff5af0cafe321387`) and call one shared C2 set, yet each build carries its own operator account identifiers (`apkAccountId`, `apkAccountName`, a per-build enrollment code) as string constants and the beacon tags them `apkOwnerSource = "apk build"`. Those identifiers resolve to 42 distinct operator accounts. One shared codebase, partitioned into per-operator accounts, is what multi-tenant means here, shown in the decompiler in sections 05 and 11. And the malware reports those identifiers to its C2 on every foreground-app event, so tear down one sample properly and you do not just get one operator; you get the roster.

This post tears down one sample end to end with jadx, the dropper `675d083b63e2169e8fd0ac0cfd27904005b5e2be00f6e3489f6e47fc4c57a4d1` (operator `lichunfeng7`), then uses the fields that single-sample teardown exposes to pull 42 distinct operator accounts and 44 rotating build brands out of our collection of 110 YuanKong droppers. Every finding about YuanKong below comes from our own binaries: the decompiled source, the signing certificates, the resources. The only third-party references are a few explicit, cited comparisons to other families (RedHook, RatHat), included for contrast and attributed where they appear.

## Key findings

* **The dropper hands you the key.** The outer app (`com.system.loader.va363d031`, signed `O=Nova`, `CN=Nova Build 20260703113341`) stores its payload key and IV in cleartext in `assets/vault-config.json`. No native unpacker, no server round-trip. The vault is self-describing. (jadx: the `vault-config.json` figure above and section 01.)
* **“SVLT-XOR-v2” is a two-key XOR, not real crypto.** The decrypt is `plain[i] = cipher[i] ^ key[i % keylen] ^ iv[i % ivlen]`, over a `"SVLT"`-magic container. The plaintext is a ZIP; the child APK is lifted straight out of it. (jadx: `svltDecrypt` and `extractChildApk` in section 02.)
* **The child is YuanKong and every tenant shares one certificate.** The unpacked app `com.remote.control.RemoteControlApp` is signed `CN=Remote Control, OU=Dev, O=YuanKong, L=Beijing, C=CN`. The same certificate (`73cbe8e3730cacfdd208f22eab468bb5495a78c0eb2cb37eff5af0cafe321387`) signs all 57 distinct payloads in our set, a strong family anchor. (jadx: the certificate in section 03 and the same certificate on a second operator’s sample in section 11.)
* **Operator identity is baked into the binary.** The config class exposes `apkAccountId` (e.g. `account_mulcetn2_9d226b242cac`), `apkAccountName` (the operator’s handle, e.g. `lichunfeng7`) and a per-build six-digit `enrollment_code`. These are not server-side secrets. They are string constants in the DEX. (jadx: `k4.l3.e()`/`f()` in section 05 and a second operator’s `k4.i2.e()`/`f()` in section 11.)
* **The malware reports those identifiers home.** The foreground-app beacon packs `apkAccountId`, `apkAccountBindId`, `apkAccountName` and `apkOwnerSource` into the very payload it sends to the relay. The RAT tells the panel and us, which tenant it belongs to. (jadx: the beacon payload array in section 07.)
* **The C2 channel is Socket.IO over WebSocket, with no app-layer key.** The child holds a persistent `io.socket` WebSocket (okhttp) to a host in the shared set (`apppanda[.]xyz`, `ktxapp[.]com`, `ktx123[.]net`, `206.82.1.14`), exchanging typed JSON `ControlMessage`s; confidentiality is TLS only. (jadx: the host set in section 08.)
* **It steals by watching and driving the screen, not through content providers.** It declares no SMS, contacts, call-log, camera or microphone permission. Instead it screen-captures and streams, reads the accessibility tree including password fields, arms payment-PIN capture and takes clipboard, notifications/OTP, files and location. (jadx: section 09.)
* **It escalates to an ADB shell on the device itself.** It enables Wireless Debugging and self-pairs with the local `adbd` (this is what the SPAKE2 code is for, not the C2), then grants itself `WRITE_SECURE_SETTINGS` and installs an unkillable daemon. Escalation to the `shell` user, not root. (jadx: section 10.)
* **Two different signing identities.** The packer certificate says Singapore (`O=Nova, OU=APK Factory, C=SG`); the RAT certificate says Beijing (`O=YuanKong, C=CN`). The split is consistent across the whole set. (jadx: the two certificates in sections 01 and 03.)

> [!WARNING]
> The three C2 domains and the IP below are the malware’s C2 host set, confirmed across every sample and recommended for blocking. The package-name strings in the config class `k4.l3` field `f5672e` (`com.netflixgratis.app`, `io.litetube.app` and so on) are not the malware’s own package and are not C2; in this build they are used only as seed material by the device-identity generator `p()` (section 06). Do not treat them as indicators to block.

## Technical analysis

The sample I am tearing down is the dropper `675d083b63e2169e8fd0ac0cfd27904005b5e2be00f6e3489f6e47fc4c57a4d1` (`4280a408a7f0490d9d2eaa3f536f339b`), which unpacks the child `net.echorelay.app` (`12480408006dece2fa756b3572766eecb6fb2144a1226f4e21c4cb7d54383105`). I picked it because its operator fields are fully populated (`apkAccountName=lichunfeng7`), so you can watch an attributable identity travel from a string constant all the way to the wire.

### 01 The Nova dropper and its self-describing vault

The outer APK is a thin loader. Its signing block is the first tell: a throwaway identity with a build-stamped common name.

![jadx, dropper APK signature: CN=Nova Build 20260703113341, OU=APK Factory, O=Nova, L=Singapore, C=SG](/blog/2026/images/YuanKong-RAT-01-dropper-cert-nova.png)

*Dropper signer. The `CN` contains the digits `20260703113341`, which read as 2026-07-03 11:33:41; the certificate’s valid-from is 2026-07-03 03:33:41 UTC. The org claims an “APK Factory” in Singapore. This certificate (`af92f7d616564dabffb0679a1a38fb24d6a6c4e4a90114c6eb0834c57dd456c9`) is the packer’s identity, not the RAT’s.*

Everything the loader needs to unpack its payload is sitting in `assets/vault-config.json`, in the clear (shown in the decompiler in the screenshot above):

```
// jadx, verbatim, assets/vault-config.json
{
    "vault_format_version": "2.0",
    "encryption": {
        "algorithm": "SVLT-XOR-v2",
        "key_b64": "llVA7rB25/MzrmZJD4A/P23Ef8Isoc2rRm5xIhbgo6I=",
        "iv_hex": "b94b2608c3b296f521000550c1267bf9"
    },
    "asset": {
        "name": "cx58vmnqxuh6059a",
        "original_hash": "12480408006dece2fa756b3572766eecb6fb2144a1226f4e21c4cb7d54383105"
    },
    "payload": {
        "type": "apk",
        "path": "payload/child.apk",
        "verify_signature": true,
        "install_after_decrypt": true
    }
}
```

This single file gives up the whole scheme: the algo...
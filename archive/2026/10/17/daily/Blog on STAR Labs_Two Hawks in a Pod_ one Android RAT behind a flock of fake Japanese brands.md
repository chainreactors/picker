---
title: Two Hawks in a Pod: one Android RAT behind a flock of fake Japanese brands
url: https://starlabs.sg/blog/2026/10-two-hawks-in-a-pod-one-android-rat-behind-a-flock-of-fake-japanese-brands/
source: Blog on STAR Labs
date: 2026-10-17
fetch_date: 2026-10-18T06:47:03.521508
---

# Two Hawks in a Pod: one Android RAT behind a flock of fake Japanese brands

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
October 17, 2026
By Jacob Soo
22 min read

# Two Hawks in a Pod: one Android RAT behind a flock of fake Japanese brands

Over the past month we collected and analysed 64 Android samples (first seen 2026-09-15 to 2026-10-16) that are all the same thing: a thin dropper that installs a packed second-stage WebSocket RAT. The operators run a web control panel that brands itself with a hawk logo and one of two Chinese names, 茅禄聭茅鹿掳氓庐聣氓聧聯猫驴聹忙聨搂 (“Black Hawk Android Remote Control”) and 茅聸聞茅鹿掳氓庐聣氓聧聯猫驴聹莽篓聥 (“Eagle Android Remote”), over an identical login page and tagline (氓庐聣氓聟篓茫聙聛茅芦聵忙聲聢莽職聞猫庐戮氓陇聡莽庐隆莽聬聠忙聨搂氓聢露氓鹿鲁氓聫掳).

Two things set it apart from the usual Android RAT. The same RAT is repackaged as different fake apps, each impersonating a brand: Japan’s e-Tax service, Rakuten and Mitsui Sumitomo card points, Mercari, LINE, a SpaceX “6G” investment scam, romance apps and live-TV players. And the two hawk-branded panels are live at the same time, on different hosts.

## The reference sample

The teardown below follows one sample end to end, so anyone who has it can reproduce each step. The dropper is `com.nova.core.high` (sha256 `24e58e12c24180abf800f142b83348b318f60894f94571a68eea98481abd84f0`), a libsa-packed e-Tax lure that drops the RAT `com.open.stone.love`. Unpacking it gives two pieces of code we keep coming back to: the dropper’s hidden inner code, which holds its settings and keys and the RAT’s own code. Both are shown in full further down.

## The attack flow

The operation behind Black Hawk is likely financially motivated. Every disguise is a money brand, tax refunds, card points, bank accounts, a fake SpaceX investment, and every capability in the payload serves theft: it harvests the lock-screen credential, PIN and pattern, steals payment input, mirrors and drives the screen, and escalates on-device so an operator can open a banking or payment app and move money with nothing shown to the victim. The romance-themed fronts deliver the same RAT as the finance lures do.

The chain from lure to fraud:

![Attack flow: from a fake app to on-device fraud](/blog/2026/images/BlackHawk_attack_flow.png)

## Stage one: the dropper

The app the victim installs is a dropper, and it is itself packed (next section). Once its own payload is unpacked at runtime it requests `REQUEST_INSTALL_PACKAGES` and installs a second APK, the RAT.

A few things stay the same in every version of the dropper, no matter which brand it fakes or which certificate signs it. Together, they are how we recognise this family. The dropper always ships the same four parts with the same short names: an activity `Wv`, a service `Bv`, a receiver `Ir`, and the launcher screen `MainActivity`. It always asks for the permission that lets one app install another (`REQUEST_INSTALL_PACKAGES`). The `Ir` receiver always waits for a custom “install finished” message (`<pkg>.INSTALL_COMPLETE`). And the package name is always stitched together from the same short word list: `nova`, `core`, `work`, `link`, `love`, `play`, `high`, `snap`, `net`, `voice`, `nice`, `flash`, `gold`.

The certificate is not one of those traits, on purpose. Every sample is signed with the throwaway certificate that ships with Android’s developer tools (`CN=Android`, sha256 `a40da80a59d170caa950cf15c18c454d47a39b26989d8b640ecd745ba71bf5dc`). Huge numbers of unrelated apps are signed with that same certificate, so grouping by it would sweep in apps that have nothing to do with this family. We group samples by the parts above and by the config block inside each one instead.

Here is that fingerprint in the reference sample’s manifest:

```
<!-- com.nova.core.high   (dropper AndroidManifest, trimmed) -->
<uses-permission android:name="android.permission.REQUEST_INSTALL_PACKAGES"/>

<activity android:name="com.nova.core.high.MainActivity">
    <intent-filter>
        <action   android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
    </intent-filter>
</activity>
<activity android:name="com.nova.core.high.Wv"/>
<service  android:name="com.nova.core.high.Bv"/>
<receiver android:name="com.nova.core.high.Ir">
    <intent-filter>
        <action android:name="com.nova.core.high.INSTALL_COMPLETE"/>
    </intent-filter>
</receiver>
```

`REQUEST_INSTALL_PACKAGES` is what lets the app install a second APK from outside the store. The `Ir` receiver’s `INSTALL_COMPLETE` filter is the `PackageInstaller` status callback: it is how the dropper learns the install session finished so it can launch the RAT. The install flow runs through other classes, shown later, not through `Wv` or `Bv`: in this sample `Wv` is a WebView activity and `Bv` is a `VpnService`. None of this depends on the signing certificate, which is why the fingerprint holds across builds.

## The packers

Both the dropper and the RAT it installs are packed, each with one of two packers.

The **libsa native XOR packer** puts a stub `Application` class, `Sa`, in the dropper’s main dex, so it reads in the clear with no unpacking. It holds two plaintext fields: the name of the encrypted asset (`AN`, here `oxqytzhau`) and a 32-byte XOR key (`AK`). Its `attachBaseContext` loads `libsa.so` and calls `nativeInit`:

![Sa stub decompiled in jadx](/blog/2026/images/BlackHawk_packer_Sa.png)

*Figure: the libsa stub `Sa`: the `AN` asset name, the 32-byte `AK` key (hex `49620e90...141130b2`), and `attachBaseContext` calling `loadLibrary("sa")` then `nativeInit`.*

`nativeInit` reads the `AN` asset and XORs it in place, `plain[i] = ct[i] ^ AK[i % 32]`. The decrypted bytes begin with an 8-byte header (`01 00 00 00` then a little-endian length), then the dropper’s real code as a classes.dex (magic bytes `64 65 78 0a 30 33 37`), including the `Cf` config. You do not even need to run the native code to see this: the key sits right there in `AK`, so XORing the asset by hand already produces the header:

```
$ # assets/oxqytzhau  XOR  AK   (first 24 bytes)
0000000 01 00 00 00 04 35 1a 00 64 65 78 0a 30 33 37 00  >.....5..dex.037.<
0000016 51 e0 8d 5b 80 13 4d 0c                          >Q..[..M.<
```

Bytes 0-3 are `01 00 00 00`; bytes 4-7 are the length `0x001a3504` = 1,717,508, which is exactly the size of the inner dex we recover; bytes 8-14 are `64 65 78 0a 30 33 37`, i.e. `dex\n037`.

The native routine really is that XOR, not a lucky guess from the hand-decode. `libsa.so` is stripped, but `nativeInit` (Ghidra names it `FUN_00101524`) decompiles cleanly. Earlier in the function it pulls the `AK` key and its length in over JNI (`GetByteArrayElements` into `lVar11`, `GetArrayLength` into `iVar6`, which is 32); then, right after reading the asset, it runs the loop:

![libsa nativeInit XOR loop decompiled in Ghidra](/blog/2026/images/BlackHawk_libsa_xor_ghidra.png)

*Figure: `nativeInit` (`FUN_00101524`) in `libsa.so`, decompiled in Ghidra. After `AAsset_read` fills the buffer `__ptr`, the do-while XORs every byte with the key `lVar11`: `__ptr[i] ^ lVar11[i - (i / iVar6) * iVar6]`. The index `i - (i / iVar6) * iVar6` is the compiler’s form of `i % iVar6`, and `iVar6` is 32, so this is `plain[i] = ct[i] ^ AK[i % 32]`. The `__size < 8` “too small” check and the “dec %d bytes, %u dex” log just below it then read the 8-byte header.*

The **nmmp VM packer** takes a different route and it is not exclusive to this family. nmmp is an open-source Android protector ([maoabc/nmmp](https://github.com/maoabc/nmmp)) that rewrites a dex’s sensitive methods into bytecode for a bundled native VM instead of hiding the code in an encrypted asset. It ships that VM as `libnmmp.so` and `libnmmvm.so` and injects a small `com.nmmedit.protect.NativeUtil` class that loads it at startup and runs the protected methods inside it.

![NativeUtil.cla...
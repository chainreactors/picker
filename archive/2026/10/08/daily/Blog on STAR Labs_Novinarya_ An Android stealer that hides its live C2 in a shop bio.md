---
title: Novinarya: An Android stealer that hides its live C2 in a shop bio
url: https://starlabs.sg/blog/2026/10-novinarya-an-android-stealer-that-hides-its-live-c2-in-a-shop-bio/
source: Blog on STAR Labs
date: 2026-10-08
fetch_date: 2026-10-09T08:10:45.438477
---

# Novinarya: An Android stealer that hides its live C2 in a shop bio

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
October 8, 2026
By Jacob Soo
14 min read

# Novinarya: An Android stealer that hides its live C2 in a shop bio

Scan this sample for a command server and you find nothing: no URL, no IP, nothing to block. That is the whole idea. Behind a fake “Smart System Security” app, this Iranian banking and crypto stealer keeps its server out of the binary and reads it at run time from the bio of a seller’s profile on a legitimate marketplace, rotating it with a single edit no new sample needed. Four earlier builds resolved to a profile the marketplace had already banned, a dead end. This one was still live, so for once the trail runs the whole way, from an encrypted byte in the manifest to the running C2 at (`theapi.the-x-services[.]xyz`). Every step below is shown in the decompiled code, with indicators at the end.

* **Sample (SHA-256)** be165239e4fe899b1f2eedf6459d363bca4fe6856fda87a63ba5d4e5e612e1c9
* **Package** ir.novinarya
* **Loader** net.swiftnova.bridge
* **Live C2** theapi.the-x-services[.]xyz
* **Published** 2026-10-08

## Key findings

* **Two-layer app, native-packed.** The installed APK (package `ir.novinarya`) ships a thin loader shell (`net.swiftnova.bridge`, 18 KB dex). The stealer itself is a separate Basic4Android payload sealed inside `assets/app_cache.db` and unpacked on-device by a 29 KB native loader (`libuibridge_9203.so`) with RC4 (32-byte key, 768-byte drop) then zlib. Asset name, loader name, RC4 key and key transform are re-randomized per build; the unpacked payload is byte-identical across builds.
* **81 financial targets.** It enumerates installed apps (`QUERY_ALL_PACKAGES`) and matches a hardcoded list of 54 crypto exchanges/wallets and 27 Iranian banking apps.
* **Phishing WebView, not overlays.** Credential theft is a WebView loading an operator-controlled page (`WebViewURL`) with a JavaScript form-grabber over a native “B4A” bridge. The app requests no accessibility and no overlay permission.
* **SMS and notification interception.** A broadcast receiver and an encrypted 25-bank regex config (`X_BANKS`) lift account numbers, balances and OTP codes from bank SMS and notifications.
* **C2 is never a string.** The server resolves from an encrypted manifest meta-data value (`X_ROUTES`, AES-CBC keyed by `X_CID`) to a URL on `basalam.com`; the malware reads that profile’s `bio` and decrypts it to the live, rotating C2.
* **Dead drop on a legitimate marketplace.** The operator rotates servers by editing one bio field. The resolver also carries an unused `[GITHUB]` branch.
* **Live C2 recovered.** This build’s dead drop, Basalam profile `m6AJm5`, was live at analysis time. Its bio decrypts to the active command server `hxxp://theapi.the-x-services[.]xyz/`.
* **Shared infrastructure, per-build repacking.** Five related samples decrypt to two dead-drop accounts: four point at `dxoeG7` (now banned) and this one rotated to `m6AJm5`. The inner stealer dex is identical across all of them, so only the packer and dead-drop config change per build.

## Technical analysis

### 01 The native packer and the unpacking chain

You will find the payload by reading the bootstrap, not by eyeballing the file tree. The APK’s `Application` class loads a native library and hands it control before any app code runs:

```
// host classes.dex -> net/swiftnova/bridge/ModuleConfig.java   (jadx, verbatim)
public class ModuleConfig extends Application {
    private native void attachConfig();
    private static native void connectCore(Context context);
    static { System.loadLibrary("uibridge_9203"); }          // lib/arm64-v8a/libuibridge_9203.so
    protected void attachBaseContext(Context context) {
        super.attachBaseContext(context);
        connectCore(context);                                // native loader runs before any app code
    }
    public void onCreate() { super.onCreate(); attachConfig(); }
}
```

Inside `libuibridge_9203.so`, `connectCore` decrypts a filename, formats it into `assets/%s`, and opens it with `open()`/`mmap()`:

```
;libuibridge_9203.so  (capstone, arm64), inside connectCore's unpack path
...   bl    <str_decoder>     ; decrypt the asset-name string -> "app_cache.db"  (12 bytes)
...   adr   x2, <"assets/%s">  ; format string
...   bl    snprintf           ; -> "assets/app_cache.db"
...   bl    <open_asset>       ; open() + mmap() the asset   (imports: open, mmap, fopen)
; per build the asset name is re-randomized; here it is the only \x7fEPDATA asset, app_cache.db
```

The decrypted 12-byte filename is `app_cache.db`, the one asset carrying a `\x7fEPDATA` magic over a fake SQLite header, with a high-entropy (encrypted) body:

```
$ sha256sum sample.apk
be165239e4fe899b1f2eedf6459d363bca4fe6856fda87a63ba5d4e5e612e1c9  sample.apk

$ unzip -l sample.apk | sort -rn | head -5
   4799301  assets/app_cache.db
    192760  resources.arsc
     78908  AndroidManifest.xml
     62371  assets/index.html
     58783  res/drawable/icon.png

$ xxd assets/app_cache.db | head -2
00000000: 7f45 5044 4154 4100 0000 0000 353b 4900  .EPDATA.....5;I.
00000010: 5351 4c69 7465 2066 6f72 6d61 7420 3300  SQLite format 3.

$ python3 -c "import math,collections as C; d=open('assets/app_cache.db','rb').read()[64:]; \
n=len(d); c=C.Counter(d); print(round(-sum(v/n*math.log2(v/n) for v in c.values()),3),'bits/byte')"
8.0 bits/byte            # encrypted body, not a SQLite database
```

The loader builds its RC4 key from two `.rodata` arrays (XOR, then a 1-bit rotate in this build), decrypts the asset with RC4 (32-byte key, 768-byte keystream drop), and inflates the result:

```
;libuibridge_9203.so  sub_0x8eac , builds the 32-byte RC4 key
0x8eb4  adr   x9,  #0x2121        ; x9  -> .rodata+0x799   (array A, 32 bytes)
0x8ebc  add   x10, x10, #0x101    ; x10 -> .rodata+0x779   (array B, 32 bytes)
0x8ed0  eor   w11, w12, w11       ; for i in 0..31:  key[i] = A[i] ^ B[i]
0x8ef0  lsr   w10, w9, #7         ; then rotate-left-1:  key[i] = (key[i]<<1)|(key[i]>>7)
0x8ef4  orr   w9,  w10, w9, lsl #1
; key = rol1( rodata[0x799:+32] ^ rodata[0x779:+32] )
;     = a572a20b5aa7103d743769cd09bf08ede95903c315d1a4b61aa6cf5faee44b72
; (the byte transform and offsets are re-randomized per build; nibbleswap in 986f3b7e, rol1 here)
```

```
;libnetstack_baf0.so  sub_0x9238 , RC4
0x9284  and   x13, x9,  #0x1f     ; KSA mix: key index = i & 31   (=> 32-byte key)
0x92b4  mov   w9,  #0x300         ; discard first 0x300 = 768 keystream bytes
0x9328  eor   w12, w12, w13       ; PRGA: out = in ^ S[(S[i]+S[j]) & 255]
; signature: rc4(key=x0[32], in=x1, out=x2, len=x3), drop 768
```

```
# reproduced from sub_0x8eac + the RC4 routine, run on the asset:
key   = rol1( rodata[0x799:+32] ^ rodata[0x779:+32] )
      = a572a20b5aa7103d743769cd09bf08ede95903c315d1a4b61aa6cf5faee44b72
inner = zlib.decompress( RC4(key, app_cache.db[64:], drop=768) )
#  -> 11,890,584 bytes : a 2-dex B4A bundle (classes1.dex 9,529,264 B + classes2.dex 2,361,308 B)
#  NB: both inner dex are byte-identical to 986f3b7e's (same SHA-256) , the stealer is shared,
#      only the outer packer and the dead-drop config are re-randomized per build.
```

That inner bundle is the actual stealer: a Basic4Android application, package `ir.novinarya`, about 34 classes including `domainmanager`, `corecache`, `cryptomanager`, `apiclient`, `webviewpage`, `xpackage` and `smsreceiver`. Everything from here on refers to this unpacked code; the outer `net.swiftnova.bridge` dex does nothing but load and run it.

### 02 Target apps and installed-app matching

The unpacked stealer hardcodes its target list in `ir/novinarya/xpackage.java`, verbatim:

```
// inner bundle -> ir/novinarya/xpackage.java   (54 exchange/wallet + 27 bank apps = 81 targets)
this._exchange_packages = Common.ArrayToList(new String[]{
    "io....
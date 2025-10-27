---
title: Graphcat - Generate Graphs And Charts Based On Password Cracking Result
url: https://buaq.net/go-166992.html
source: unSafe.sh - 不安全
date: 2023-06-03
fetch_date: 2025-10-04T11:44:52.315849
---

# Graphcat - Generate Graphs And Charts Based On Password Cracking Result

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/48db16b4d417d3696b7ff8cec529d821.jpg)

Graphcat - Generate Graphs And Charts Based On Password Cracking Result

Simple script to generate graphs and charts on hashcat (and john) potfile and ntds Install
*2023-6-2 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-166992.htm)
阅读量:36
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhjfZX3c_ZHRKpAwdPXVkb-L7WFK364HcPWyjGhW_3897LKNNNYDEuorlygQ-28Yq89XXHDPLhXxQ5zARsIaYYKs-01pTvTClMA0hNhLet9mX5_A-tzFBB3bym9zXgghCmLGxC0kyH0Kh30DTDKN8xf-f1TdBP5b4Bwy79VgYv0dl73liPQTLgiMx8N4Q=w640-h298)](https://blogger.googleusercontent.com/img/a/AVvXsEhjfZX3c_ZHRKpAwdPXVkb-L7WFK364HcPWyjGhW_3897LKNNNYDEuorlygQ-28Yq89XXHDPLhXxQ5zARsIaYYKs-01pTvTClMA0hNhLet9mX5_A-tzFBB3bym9zXgghCmLGxC0kyH0Kh30DTDKN8xf-f1TdBP5b4Bwy79VgYv0dl73liPQTLgiMx8N4Q)

Simple script to generate graphs and charts on hashcat (and john) potfile and ntds

## Install

```
git clone https://github.com/Orange-Cyberdefense/graphcat
```

## Helper

```
$ graphcat.py -h
usage: graphcat.py [-h] -potfile hashcat.potfile -hashfile hashfile.txt [-john] [-format FORMAT] [-export-charts] [-output-dir OUTPUT_DIR] [-debug]

Password Cracking Graph Reporting

options:
  -h, --help            show this help message and exit
  -potfile hashcat.potfile
                        Hashcat Potfile
  -hashfile hashfile.txt
                        File containing hashes (one per line)
  -john                 John potfile
  -format FORMAT        hashfile format (default 3): 1 for hash; 2 for username:hash; 3 for secretsdump (username:uid:lm:ntlm)
  -export-charts        Output also charts in png
  -output-dir OUTPUT_DIR
                        Output directory
  -debug                Turn DEB   UG output ON
```

## Usage

Graphcat just need a potfile with `-potfile` (default is hashcat, but you can use `-john` to submit a john potfile) and a hashfile with `-hashfile`. The hashfile should be in a specific format from the [3 availables formats](https://github.com/Orange-Cyberdefense/graphcat#formats "3 availables formats") with `-format` flag. Default is **Secretsdump**.

The tool will generate a report with multiple password cracking charts. You can get charts in png with the `-export-charts` flag.

```
$ graphcat.py -hashfile entreprise.local.ntds -potfile hashcat.pot
[-] Parsing potfile
[-] 164 entries in potfile
[-] Parsing hashfile
[-] 1600 entries in hashfile
[-] Generating graphs...
[-] Generating report...
[-] Report available at graphcat_1672941324.pdf
```

### Formats

1: Only Hash

```
aad3b435b51404eeaad3b435b51404ee
aad3b435b51404eeaad3b435b51404ee
aad3b435b51404eeaad3b435b51404ee
```

2: [Username](https://www.kitploit.com/search/label/Username "Username") + Hash

```
test1:aad3b435b51404eeaad3b435b51404ee
test2:aad3b435b51404eeaad3b435b51404ee
test3:aad3b435b51404eeaad3b435b51404ee
```

3: Secretsdump

```
waza.local\test1:4268:aad3b435b51404eeaad3b435b51404ee:aad3b435b51404eeaad3b435b51404ee:::
waza.local\test2:4269:aad3b435b51404eeaad3b435b51404ee:aad3b435b51404eeaad3b435b51404ee:::
waza.local\test3:4270:aad3b435b51404eeaad3b435b51404ee:aad3b435b51404eeaad3b435b51404ee:::
```

If a hash occurs more than once in the hash file, it will be counted that many times.

Moreover, if you submit secretsdump with password [history](https://www.kitploit.com/search/label/History "history") (`-history` in secretsdump command), it will analyze similarity in password history

## Charts example

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhFaUW098IUuANnenw-CYOV1GSiCwBGDBkmbV2-q8lxEcrvB2nbSZha3dKWHDfqIsm_rgmyJM14qrARzZ6rd645ciiYKGienAzASDKU_kSXkYgWExwyiSDNfByDiTQ7zb-CHa7cB8ydjz4UE6lePJoE0ks0XhGMIKUk1747iBOru2I86ShXXNdcUlxVHw=w640-h298)](https://blogger.googleusercontent.com/img/a/AVvXsEhFaUW098IUuANnenw-CYOV1GSiCwBGDBkmbV2-q8lxEcrvB2nbSZha3dKWHDfqIsm_rgmyJM14qrARzZ6rd645ciiYKGienAzASDKU_kSXkYgWExwyiSDNfByDiTQ7zb-CHa7cB8ydjz4UE6lePJoE0ks0XhGMIKUk1747iBOru2I86ShXXNdcUlxVHw)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg48cz0Jdr2icBliAgMSB1yUagMqvDB0ynbwKIdFVpzpPhralNa6IuBj3Qi3-djeKYMKm5vODMaFVKUeL5C547-nlNvEBcOcwKjmFTtOxoi3ZR-ZT9eJjMr4RVyN_mv01a1i8EZgzyiO3AhvZXcV-Gxfc7amQIsOkOo9953eycp3lz_KWUPQwQ5dCvOMw=w640-h298)](https://blogger.googleusercontent.com/img/a/AVvXsEg48cz0Jdr2icBliAgMSB1yUagMqvDB0ynbwKIdFVpzpPhralNa6IuBj3Qi3-djeKYMKm5vODMaFVKUeL5C547-nlNvEBcOcwKjmFTtOxoi3ZR-ZT9eJjMr4RVyN_mv01a1i8EZgzyiO3AhvZXcV-Gxfc7amQIsOkOo9953eycp3lz_KWUPQwQ5dCvOMw)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhjfZX3c_ZHRKpAwdPXVkb-L7WFK364HcPWyjGhW_3897LKNNNYDEuorlygQ-28Yq89XXHDPLhXxQ5zARsIaYYKs-01pTvTClMA0hNhLet9mX5_A-tzFBB3bym9zXgghCmLGxC0kyH0Kh30DTDKN8xf-f1TdBP5b4Bwy79VgYv0dl73liPQTLgiMx8N4Q=w640-h298)](https://blogger.googleusercontent.com/img/a/AVvXsEhjfZX3c_ZHRKpAwdPXVkb-L7WFK364HcPWyjGhW_3897LKNNNYDEuorlygQ-28Yq89XXHDPLhXxQ5zARsIaYYKs-01pTvTClMA0hNhLet9mX5_A-tzFBB3bym9zXgghCmLGxC0kyH0Kh30DTDKN8xf-f1TdBP5b4Bwy79VgYv0dl73liPQTLgiMx8N4Q)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjhBpa-zVJr4ItBDmmmean7UV-e7XjswBg51rAymi4-wXq4hf3tGDeR0HuwpU0MnFFlqOduD-EyRI3M5zZJ3eSMK-jE-T1qNm_vXvnG02quZib0QhlQDDHQp2j5RpvAidPO4Rf-GBFz52VGYw6IecJlT4E38Dlcc9wJuq85jv4VWez19wo0q4fHX8evpw=w640-h426)](https://blogger.googleusercontent.com/img/a/AVvXsEjhBpa-zVJr4ItBDmmmean7UV-e7XjswBg51rAymi4-wXq4hf3tGDeR0HuwpU0MnFFlqOduD-EyRI3M5zZJ3eSMK-jE-T1qNm_vXvnG02quZib0QhlQDDHQp2j5RpvAidPO4Rf-GBFz52VGYw6IecJlT4E38Dlcc9wJuq85jv4VWez19wo0q4fHX8evpw)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh6vcQKa088W7lc73v-yjoU7n9--zZum46FpGrpDzdcbyzkkO1iT5TgDTl-_gk9VD0SVZx1m74qByLZ98lvsE8LynkyVMXXXR97OELzjMAnL5RfEbuwX6MT6pkrd2ma45AVf7jqyDc46oYbNHr2_nYULRSVvnTp-qWPMiPwbszHRuA1W1riPKpXNaTqdg=w640-h426)](https://blogger.googleusercontent.com/img/a/AVvXsEh6vcQKa088W7lc73v-yjoU7n9--zZum46FpGrpDzdcbyzkkO1iT5TgDTl-_gk9VD0SVZx1m74qByLZ98lvsE8LynkyVMXXXR97OELzjMAnL5RfEbuwX6MT6pkrd2ma45AVf7jqyDc46oYbNHr2_nYULRSVvnTp-qWPMiPwbszHRuA1W1riPKpXNaTqdg)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhSjxGNOwvfCR9Oha5-IizsAB_3CdyElmUE2MpDngXNQwCma2Ekzc68oM3VJpMDB3fbxjURHTfTasXjlF0KFD-Hs4CUJSn2fUhiHkyxA9MCs9LXhvSqMsRolSS-zkNYSW76DV54G6u4f3nnP_UGhJdrBrG2QBk5Wo2r2Yr-nFXG-kL20rp3zGyC6crCEw=w640-h298)](https://blogger.googleusercontent.com/img/a/AVvXsEhSjxGNOwvfCR9Oha5-IizsAB_3CdyElmUE2MpDngXNQwCma2Ekzc68oM3VJpMDB3fbxjURHTfTasXjlF0KFD-Hs4CUJSn2fUhiHkyxA9MCs9LXhvSqMsRolSS-zkNYSW76DV54G6u4f3nnP_UGhJdrBrG2QBk5Wo2r2Yr-nFXG-kL20rp3zGyC6crCEw)

Graphcat - Generate Graphs And Charts Based On Password Cracking Result
![Graphcat - Generate Graphs And Charts Based On Password Cracking Result](https://blogger.googleusercontent.com/img/a/AVvXsEhjfZX3c_ZHRKpAwdPXVkb-L7WFK364HcPWyjGhW_3897LKNNNYDEuorlygQ-28Yq89XXHDPLhXxQ5zARsIaYYKs-01pTvTClMA0hNhLet9mX5_A-tzFBB3bym9zXgghCmLGxC0kyH0Kh30DTDKN8xf-f1TdBP5b4Bwy79VgYv0dl73liPQTLgiMx8N4Q=s72-w640-c-h298)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/06/graphcat-generate-graphs-and-charts.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
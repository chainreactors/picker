---
title: PassMute - PassMute - A Multi Featured Password Transmutation/Mutator Tool
url: https://buaq.net/go-163299.html
source: unSafe.sh - 不安全
date: 2023-05-15
fetch_date: 2025-10-04T11:36:47.091607
---

# PassMute - PassMute - A Multi Featured Password Transmutation/Mutator Tool

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

![](https://8aqnet.cdn.bcebos.com/5412e82754a2b5aad43571e73f4ebf4c.jpg)

PassMute - PassMute - A Multi Featured Password Transmutation/Mutator Tool

This is a command-line tool written in Python that applies one or more transmutation rules t
*2023-5-14 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-163299.htm)
阅读量:43
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhMCzljb13Ty2hHJ1fvBSjy_b8oKv8Uf6Y_k3lwT37-hNFZ6OLBIj1Bpyfny4yGadEQOS2xNXYg9Cdv0e40QSliGNbIFlRdaZKbp99wyuxD1c_muMULCMAVLsXUXKkIcxMzYx_DycFytkmkKO2N0Le1_OoozNzMdQ2wm4XKsYEpvO1Q-fJhavAOiF1dmQ=w640-h254)](https://blogger.googleusercontent.com/img/a/AVvXsEhMCzljb13Ty2hHJ1fvBSjy_b8oKv8Uf6Y_k3lwT37-hNFZ6OLBIj1Bpyfny4yGadEQOS2xNXYg9Cdv0e40QSliGNbIFlRdaZKbp99wyuxD1c_muMULCMAVLsXUXKkIcxMzYx_DycFytkmkKO2N0Le1_OoozNzMdQ2wm4XKsYEpvO1Q-fJhavAOiF1dmQ)

This is a command-line tool written in Python that applies one or more transmutation rules to a given password or a list of passwords read from one or more files. The tool can be used to generate transformed passwords for security testing or research purposes. Also, while you doing [pentesting](https://www.kitploit.com/search/label/Pentesting "pentesting") it will be very useful tool for you to [brute force](https://www.kitploit.com/search/label/Brute%20Force "brute force") the passwords!!

**How Passmute can also help to secure our passwords more?**

PassMute can help to generate strong and complex passwords by applying different transformation rules to the input password. However, password security also depends on other factors such as the length of the password, randomness, and avoiding common phrases or patterns.

The transformation rules include:

**reverse:** reverses the password string

**uppercase:** converts the password to uppercase letters

**lowercase:** converts the password to lowercase letters

**swapcase:** swaps the case of each letter in the password

**capitalize:** capitalizes the first letter of the password

**leet:** replaces some letters in the password with their leet equivalents

**strip:** removes all whitespace characters from the password

The tool can also write the transformed passwords to an output file and run the transformation process in parallel using multiple threads.

**Installation**

```
git clone https://HITH-Hackerinthehouse/PassMute.git
```

**Usage** To use the tool, you need to have [Python 3](https://www.kitploit.com/search/label/Python%203 "Python 3") installed on your system. Then, you can run the tool from the [command line](https://www.kitploit.com/search/label/Command%20Line "command line") using the following options:

`python PassMute.py [-h] [-f FILE [FILE ...]] -r RULES [RULES ...] [-v] [-p PASSWORD] [-o OUTPUT] [-t THREAD_TIMEOUT] [--max-threads MAX_THREADS]`

Here's a brief explanation of the available options:

-h or --help: shows the help message and exits

-f (FILE) [FILE ...], --file (FILE) [FILE ...]: one or more files to read passwords from

-r (RULES) [RULES ...] or --rules (RULES) [RULES ...]: one or more transformation rules to apply

-v or --verbose: prints verbose output for each password transformation

-p (PASSWORD) or --password (PASSWORD): transforms a single password

-o (OUTPUT) or --output (OUTPUT): output file to save the transformed passwords

-t (THREAD\_TIMEOUT) or --thread-timeout (THREAD\_TIMEOUT): timeout for threads to complete (in seconds)

--max-threads (MAX\_THREADS): maximum number of threads to run simultaneously (default: 10)

**NOTE**: If you are getting any error regarding **argparse** module then simply install the module by following command: `pip install argparse`

**Examples**

Here are some example commands those read passwords from a file, applies two transformation rules, and saves the transformed passwords to an output file:

**Single Password transmutation**: `python PassMute.py -p HITHHack3r -r leet reverse swapcase -v -t 50`

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjKDZkh8DkUChMS9k29vDB7vYbqpzPcTcqU5pSHPudjv27wDOW4cZt1rfEhHqwlluadT-OzoKPvGdih6YHt3Nvr9BTuslFRDXPGhdfXA3Xh3mTyiU7DxS1RnPYgkQ22HzBb-Vv3ggBsXrL2TSTJ81ImbCtz1oH2-hQgRQIBkoQ5c7jlHnRKr07NNWL0vQ=w640-h328)](https://blogger.googleusercontent.com/img/a/AVvXsEjKDZkh8DkUChMS9k29vDB7vYbqpzPcTcqU5pSHPudjv27wDOW4cZt1rfEhHqwlluadT-OzoKPvGdih6YHt3Nvr9BTuslFRDXPGhdfXA3Xh3mTyiU7DxS1RnPYgkQ22HzBb-Vv3ggBsXrL2TSTJ81ImbCtz1oH2-hQgRQIBkoQ5c7jlHnRKr07NNWL0vQ)

**Multiple Password transmutation**: `python PassMute.py -f testwordlists.txt -r leet reverse -v -t 100 -o testupdatelists.txt`

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgtwvqPLXK9bnCuVVDsnnRO-T_jgjM2NIGhoBhcohAWqi3ovSXksl8T-xMbAcYNQ4DKDCpRwDiqtLzR8PlmaGYkETEXI49NtJPEjBGkjprkVZKem55gTIygW_uSWgh9EovdyTQCf5d7xuXaI84qhXXmImhyXho_7O0r4luV-4CF9-g76RJAMZjkOj-DXw=w640-h328)](https://blogger.googleusercontent.com/img/a/AVvXsEgtwvqPLXK9bnCuVVDsnnRO-T_jgjM2NIGhoBhcohAWqi3ovSXksl8T-xMbAcYNQ4DKDCpRwDiqtLzR8PlmaGYkETEXI49NtJPEjBGkjprkVZKem55gTIygW_uSWgh9EovdyTQCf5d7xuXaI84qhXXmImhyXho_7O0r4luV-4CF9-g76RJAMZjkOj-DXw)

**Here Verbose and Thread are recommended to use in case you're transmutating big files and also it depends upon your microprocessor as well, it's not required every time to use threads and verbose mode.**

**Legal Disclaimer**:

You might be super excited to use this tool, we too. But here we need to confirm! Hackerinthehouse, any contributor of this project and Github won't be responsible for any actions made by you. This tool is made for security research and educational purposes only. It is the end user's responsibility to obey all applicable local, state and federal laws.

PassMute - PassMute - A Multi Featured Password Transmutation/Mutator Tool
![PassMute - PassMute - A Multi Featured Password Transmutation/Mutator Tool](https://blogger.googleusercontent.com/img/a/AVvXsEhMCzljb13Ty2hHJ1fvBSjy_b8oKv8Uf6Y_k3lwT37-hNFZ6OLBIj1Bpyfny4yGadEQOS2xNXYg9Cdv0e40QSliGNbIFlRdaZKbp99wyuxD1c_muMULCMAVLsXUXKkIcxMzYx_DycFytkmkKO2N0Le1_OoozNzMdQ2wm4XKsYEpvO1Q-fJhavAOiF1dmQ=s72-w640-c-h254)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/05/passmute-passmute-multi-featured.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
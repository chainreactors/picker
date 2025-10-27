---
title: FindUncommonShares - A Python Equivalent Of PowerView's Invoke-ShareFinder.ps1 Allowing To Quickly Find Uncommon Shares In Vast Windows Domains
url: https://buaq.net/go-154188.html
source: unSafe.sh - 不安全
date: 2023-03-20
fetch_date: 2025-10-04T10:04:45.085884
---

# FindUncommonShares - A Python Equivalent Of PowerView's Invoke-ShareFinder.ps1 Allowing To Quickly Find Uncommon Shares In Vast Windows Domains

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

![](https://8aqnet.cdn.bcebos.com/6cd2b0df01add2fdde0bc968864e8e9f.jpg)

FindUncommonShares - A Python Equivalent Of PowerView's Invoke-ShareFinder.ps1 Allowing To Quickly Find Uncommon Shares In Vast Windows Domains

The script FindUncommonShares.py is a Python equivalent of PowerView's Invoke-ShareFi
*2023-3-19 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-154188.htm)
阅读量:44
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgfoW7Db08N9MM7hMlq9ztJEYDQhJTIs1LZBJNTskWE6QOiGCLbnynxr5XRFSIhDc28tWofeG9xhz5kB5qaC9m1lBipIYeYn4bxGEn0Te66zjTl0UZRlv6z2bcb7UGvRtgWkKqoO39vl7wzyf6A3a0CTcydRh5liLjwLx2EzEMHxeghnpa3w23KLU1UKA=w640-h356)](https://blogger.googleusercontent.com/img/a/AVvXsEgfoW7Db08N9MM7hMlq9ztJEYDQhJTIs1LZBJNTskWE6QOiGCLbnynxr5XRFSIhDc28tWofeG9xhz5kB5qaC9m1lBipIYeYn4bxGEn0Te66zjTl0UZRlv6z2bcb7UGvRtgWkKqoO39vl7wzyf6A3a0CTcydRh5liLjwLx2EzEMHxeghnpa3w23KLU1UKA)

The script [FindUncommonShares.py](https://github.com/p0dalirius/FindUncommonShares/blob/main/FindUncommonShares.py "FindUncommonShares.py") is a Python equivalent of [PowerView](https://github.com/darkoperator/Veil-PowerView/ "PowerView")'s [Invoke-ShareFinder.ps1](https://github.com/darkoperator/Veil-PowerView/blob/master/PowerView/functions/Invoke-ShareFinder.ps1 "Invoke-ShareFinder.ps1") allowing to quickly find uncommon shares in vast Windows [Active Directory](https://www.kitploit.com/search/label/Active%20Directory "Active Directory") Domains.

## Features

* Only requires a **low privileges domain user account**.
* Automatically gets the list of all computers from the domain controller's LDAP.
* Ignore the hidden shares (ending with `$`) with `--ignore-hidden-shares`.
* Multithreaded connections to discover SMB shares.
* Export results in JSON with IP, name, comment, flags and UNC path with `--export-json <file.json>`.
* Export results in XLSX with IP, name, comment, flags and UNC path with `--export-xlsx <file.xlsx>`.
* Export results in SQLITE3 with IP, name, comment, flags and UNC path with `--export-sqlite <file.db>`.
* Iterate on LDAP result pages to get every computer of the domain, no matter the size.

## Usage

```
$ ./FindUncommonShares.py -h
FindUncommonShares v2.4 - by @podalirius_

usage: FindUncommonShares.py [-h] [--use-ldaps] [-q] [--debug] [-no-colors] [-I] [-t THREADS] [--export-xlsx EXPORT_XLSX] [--export-json EXPORT_JSON] [--export-sqlite EXPORT_SQLITE] --dc-ip ip address [-d DOMAIN] [-u USER]
                             [--no-pass | -p PASSWORD | -H [LMHASH:]NTHASH | --aes-key hex key] [-k]

Find uncommon SMB shares on remote machines.

optional arguments:
  -h, --help            show this help message and exit
  --use-ldaps           Use LDAPS instead of LDAP
  -q, --quiet           Show no information at all.
  --debug               Debug mode.
  -no-colors            Disables colored output mode
  -I, --ignore-hidden-shares
                        Ignores hidden shares (shares ending with $)
  -t THREADS, --threads THREADS
                        Number of threads (default: 20)

Output fi   les:
  --export-xlsx EXPORT_XLSX
                        Output XLSX file to store the results in.
  --export-json EXPORT_JSON
                        Output JSON file to store the results in.
  --export-sqlite EXPORT_SQLITE
                        Output SQLITE3 file to store the results in.

Authentication & connection:
  --dc-ip ip address    IP Address of the domain controller or KDC (Key Distribution Center) for Kerberos. If omitted it will use the domain part (FQDN) specified in the identity parameter
  -d DOMAIN, --domain DOMAIN
                        (FQDN) domain to authenticate to
  -u USER, --user USER  user to authenticate with

Credentials:
  --no-pass             Don't ask for password (useful for -k)
  -p PASSWORD, --password PASSWORD
                        Password to authenticate w   ith
  -H [LMHASH:]NTHASH, --hashes [LMHASH:]NTHASH
                        NT/LM hashes, format is LMhash:NThash
  --aes-key hex key     AES key to use for Kerberos Authentication (128 or 256 bits)
  -k, --kerberos        Use Kerberos authentication. Grabs credentials from .ccache file (KRB5CCNAME) based on target parameters. If valid credentials cannot be found, it will use the ones specified in the command line
```

## Examples :

```
$ ./FindUncommonShares.py -u 'user1' -d 'LAB.local' -p '[email protected]!' --dc-ip 192.168.2.1
FindUncommonShares v2.3 - by @podalirius_

[>] Extracting all computers ...
[+] Found 2 computers.

[>] Enumerating shares ...
[>] Found 'Users' on 'DC01.LAB.local'
[>] Found 'WeirdShare' on 'DC01.LAB.local' (comment: 'Test comment')
[>] Found 'AnotherShare' on 'PC01.LAB.local'
[>] Found 'Users' on 'PC01.LAB.local
$
```

Each JSON entry looks like this:

```
{
    "computer": {
        "fqdn": "DC01.LAB.local",
        "ip": "192.168.1.1"
    },
    "share": {
        "name": "ADMIN$",
        "comment": "Remote Admin",
        "hidden": true,
        "uncpath": "\\\\192.168.1.46\\ADMIN$\\",
        "type": {
            "stype_value": 2147483648,
            "stype_flags": [
                "STYPE_DISKTREE",
                "STYPE_TEMPORARY"
            ]
        }
    }
}
```

## Credits

* Feature suggested in [impacket issue #1176](https://github.com/SecureAuthCorp/impacket/issues/1176 "impacket issue #1176") by [@CaledoniaProject](https://github.com/CaledoniaProject "@CaledoniaProject")

FindUncommonShares - A Python Equivalent Of PowerView's Invoke-ShareFinder.ps1 Allowing To Quickly Find Uncommon Shares In Vast Windows Domains
![FindUncommonShares - A Python Equivalent Of PowerView's Invoke-ShareFinder.ps1 Allowing To Quickly Find Uncommon Shares In Vast Windows Domains](https://blogger.googleusercontent.com/img/a/AVvXsEgfoW7Db08N9MM7hMlq9ztJEYDQhJTIs1LZBJNTskWE6QOiGCLbnynxr5XRFSIhDc28tWofeG9xhz5kB5qaC9m1lBipIYeYn4bxGEn0Te66zjTl0UZRlv6z2bcb7UGvRtgWkKqoO39vl7wzyf6A3a0CTcydRh5liLjwLx2EzEMHxeghnpa3w23KLU1UKA=s72-w640-c-h356)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/03/finduncommonshares-python-equivalent-of.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
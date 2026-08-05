---
title: 2026第十届御网杯 数据安全赛道WP
url: https://mp.weixin.qq.com/s/1uIRuafJgtW9PRouKU1cSA
source: Doonsec's feed
date: 2026-08-04
fetch_date: 2026-08-05T04:56:35.828435
---

# 2026第十届御网杯 数据安全赛道WP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVlJNMVaNrNNPznibbpJq4WpCictBPa2YKEFBcDaL1Zj3mWPMHGLuuH6yaGzSOZgGzZtzpu8ia7Q1UMhicamfFMMshNII1caGCibgY34/0?wx_fmt=jpeg)

# 2026第十届御网杯 数据安全赛道WP

赛查查

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于云晞科技Sec
，作者江思澄

![](https://wx.qlogo.cn/mmhead/uI5pczeERTZqp0sD97WA7qBqy6ibUHsZm4lhicSpR5icrNzcMUPHj2KOgCy7VPmrdVhEGPm3azP0nM/0)

**云晞科技Sec**
.

这里是网络安全探索基地！专注分享流量分析实战技巧、应急响应解决方案，深度剖析Web安全漏洞攻防。同时带来CTF竞赛解题思路与精彩笔记，助你快速掌握前沿技术，提升安全技能，共同筑牢数字世界安全防线！

## TracePurge

解压后先看了事件响应说明.md

这里最重要的规则就三件事： 样本用 email\_hash 或 name + phone\_mask 匹配客户；只处理本次泄露对应的导出批次；最后生成 leak\_id,subject\_id,export\_id,operator,action

然后看了这四个 CSV 的表头和前几行

```
import csv
from collections import Counter

base = r'D:\下载\8：TracePurge的附件\tempdir\DS附件\TracePurge附件\TracePurge附件'
leak_path = base + r'\leak_sample.csv'

cnt = Counter()

with open(leak_path, newline='', encoding='utf-8-sig') as f:
    for row in csv.DictReader(f):
        cnt[row['batch_tag']] += 1

for k, v in cnt.most_common():
    print(k, v)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVkYRTJlgKCVo5ib4ClEK8vGfZnxB3mlWPLRFjFqv9RAYTh3o0uEJsyE2MiaWQcM003m6BibDYficMFdMZYB3JO4J8wTcsUJdREicia5k/640?wx_fmt=png&from=appmsg)

CRM-20260508-D4 数量明显最多

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVliceNcsBpJKgsicyxrgZTQOqTdK9ImDqRw3yicD33tIl5fgLcBuRsjpKibQ1qe08VOe9CcfcYuB8v8EkZX3ToNluJCGWJicfKRp0hc/640?wx_fmt=png&from=appmsg)

所以这次事件就是 EX20260508004，操作人是 ops\_chen

后面按说明匹配客户 email 非空就 strip + lower 后做 sha256，去 customer\_index.csv 的 email\_hash 里找邮箱为空或者哈希找不到，就用 name + phone\_mask，只有唯一命中才算一个 subject\_id 如果出现多次，保留 leak\_id 字典序最小的那条

直接生成提交文件：

```
import csv
import hashlib
from collections import defaultdict, Counter

base = r'D:\下载\8：TracePurge的附件\tempdir\DS附件\TracePurge附件\TracePurge附件'
out_path = r'D:\下载\8：TracePurge的附件\tempdir\DS附件\TracePurge附件\TracePurge附件\response_plan.csv'

leak_path = base + r'\leak_sample.csv'
idx_path = base + r'\customer_index.csv'

target_batch = 'CRM-20260508-D4'
export_id = 'EX20260508004'
operator = 'ops_chen'

email_map = {}
name_phone = defaultdict(list)

with open(idx_path, newline='', encoding='utf-8-sig') as f:
    for row in csv.DictReader(f):
        if row['email_hash']:
            email_map[row['email_hash']] = row
        name_phone[(row['name'], row['phone_mask'])].append(row)

def match_subject(leak):
    email = leak['email'].strip()
    if email:
        h = hashlib.sha256(email.lower().encode()).hexdigest()
        if h in email_map:
            return email_map[h]

    hits = name_phone[(leak['name'], leak['phone_mask'])]
    if len(hits) == 1:
        return hits[0]

    returnNone

def get_action(subject):
    if subject['erase_requested'] == 'true':
        return'PURGE'
    if subject['risk'] == 'high':
        return'NOTIFY'
    return'MONITOR'

best = {}

with open(leak_path, newline='', encoding='utf-8-sig') as f:
    for leak in csv.DictReader(f):
        if leak['batch_tag'] != target_batch:
            continue

        subject = match_subject(leak)
        ifnot subject:
            continue

        sid = subject['subject_id']

        row = {
            'leak_id': leak['leak_id'],
            'subject_id': sid,
            'export_id': export_id,
            'operator': operator,
            'action': get_action(subject),
        }

        if sid notin best or leak['leak_id'] < best[sid]['leak_id']:
            best[sid] = row

rows = sorted(best.values(), key=lambda r: (r['leak_id'], r['subject_id']))

with open(out_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(
        f,
        fieldnames=['leak_id', 'subject_id', 'export_id', 'operator', 'action']
    )
    writer.writeheader()
    writer.writerows(rows)

print('output:', out_path)
print('rows:', len(rows))
print(Counter(r['action'] for r in rows))
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVn1Xz9nwzXWicZnXfARgY7zs0OGyODQlJgHtgTPWpDwvK75CsLtLRjCTnsHhsicOnJTl6mNE6ibVJPmUfVceA6JUgGEjar6LOtyWk/640?wx_fmt=png&from=appmsg)

生成出来 response\_plan.csv 一共 1200 行，动作分布是 MONITOR 964、NOTIFY 147、PURGE 89上传平台后 100%

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVkMWK5haWQ8trx9WpB7LO1GRAg6hDMMQdLmqoFz1eRunNvQro2y7u3lmytMLcuicRcF4DibZAiblRyw2yLwjrCA2ln78KQIs1vbd0/640?wx_fmt=png&from=appmsg)

```
flag{e115cc3382d6b63c3196a4f1ca32eefa}
```

## ShadowMeter

这题给了 access.log 和 error.log我先看 access.log，登录接口这里没有一行行数，直接把状态码统计出来：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVlY8EHz3MrhcT4A5XVhnWo4v9myJ33m3ia0Z5fdvnueabURWPwHSsenXEQWAMsXXFkpvsD1CywD3KNmwvDS0TeoCyKOy87kUqw4/640?wx_fmt=png&from=appmsg)

结果是 7 次 401、1 次 200，说明确实有一次登录成功access.log 后面还能看到 /admin/export.php和/collect/report.php 开始大量出现，所以我怀疑是先登录导出，再通过 collect 接口分片外传

access.log 看不到 POST body，所以继续翻 error.log这里 Apache 开了 dumpio，会把请求体和响应也记下来我先搜 /admin/login.php，找到最后一次登录请求的 client 是 172.25.0.1:60636，再用这个 client 过滤同一次请求：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVmr94rVjicJacCo9G2vViaiaLoK8zDYKxvfDlHswJNyXIGMEs4ODnMtrnvD1VpwW5MLEVsxgzpNNXlsaSfVhAeUbfaFZM24FnVwBI/640?wx_fmt=png&from=appmsg)

这时候才看到登录的 body 和响应：

```
POST /admin/login.php HTTP/1.1
username=admin_ops&password=Admin%40Pa%24%24w0rd
{"token":"ops-internal-8dd18cfd"}
```

Admin%40Pa%24%24w0rd URL 解码后是：

```
Admin@Pa$$w0rd
```

登录这块确认完以后，继续看 /collect/report.php 的 POST bodyerror.log 里能看到每次上报都有 job、seq、notejob=SM-20260507-17 里数字 seq 的 note 是 base64 分片，第一片以 UEsDB 开头，base64 解出来是 PK\x03\x04，说明是在分片外传 zip

![](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVl0NibdcfL6k0w5aF8vibR4eKe35g5kRKLVMBGRjqM9qU7m4aNz2LpIeHTaialpicibfptiaoBrXEN87uHyLlfpLUI4vwY9R2icY7v3PQ/640?wx_fmt=png&from=appmsg)

再看结束分片，seq=END 的 note 不是 base64，而是给了校验信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVnSiaB0RpG15lUrKJtdo616XD3JAOQNmLtDRO0ic2UPILNXsp3rrhUib6j5Eqso5kKZeW2BpNUrrtaj3nibaZSCxR0QtzxrWNawg6s/640?wx_fmt=png&from=appmsg)

所以恢复思路就是按 seq 顺序拼接数字分片的 note，中间重复 seq 用第一份，最后用 archive\_size=10601 和 sha256=4019ef293eeb8af8a0d5c0e66c0bdb3cbcd17067839f42c86beb501a83d6c59b 校验，能对上就说明 zip 恢复对了

```
import base64, codecs, collections, datetime, hashlib, pathlib, re, urllib.parse

err = pathlib.Path(r"D:\下载\3：ShadowMeter的附件\tempdir\MISC附件\ShadowMeter附件\ShadowMeter附件\error.log")
out = pathlib.Path(r"D:\下载\3：ShadowMeter的附件\tempdir\MISC附件\ShadowMeter附件\ShadowMeter附件\1.zip")

line_re = re.compile(
    r"^\[(?P<ts>[^\]]+)\].*?\[client (?P<client>[^\]]+)\] "
    r"mod_dumpio:\s+dumpio_(?P<dir>in|out) \((?P<kind>[^)]+)\): (?P<data>.*)$"
)

def ts(s):
    return datetime.datetime.strptime(s, "%a %b %d %H:%M:%S.%f %Y")

def unesc(s):
    return codecs.decode(s.encode(), "unicode_escape").encode("latin-1", "replace")

streams = collections.defaultdict(list)

for line in err.read_text(errors="replace").splitlines():
    m = line_re.match(line)
    ifnot m:
        continue
    if m.group("dir") != "in":
        continue
    ifnot m.group("kind").startswith("data-"):
        continue
    data = m.group("data")
    if re.fullmatch(r"\d+ bytes", data):
        continue
    streams[m.group("client")].append((ts(m.group("ts")), unesc(data)))

def parse_requests(buf):
    pos = 0
    while pos < len(buf):
        end = buf.find(b"\r\n\r\n", pos)
        if end < 0:
            break
        head = buf[pos:end]
        first = head.split(b"\r\n", 1)[0].decode("latin-1", "replace")
        m = re.match(r"(GET|POST|OPTIONS) ([^ ]+) HTTP/", first)
        ifnot m:
            nxt = buf.find(b"POST ", pos + 1)
            if nxt < 0:
                break
            pos = nxt
            continue
        headers = {}
        for line in head.split(b"\r\n")[1:]:
            ifb":"in line:
                k, v = line.split(b":", 1)
                headers[k.decode().lower()] = v.strip().decode()
        clen = int(headers.get("content-length", "0") or0)
        body = buf[end + 4:end + 4 + clen]
        yield m.group(1), m.group(2), body
        pos = end + 4 + clen

rows = []

for parts in streams.values():
    buf = b"".join(x[1] for x in sorted(parts))
    for method, path, body in parse_reques...
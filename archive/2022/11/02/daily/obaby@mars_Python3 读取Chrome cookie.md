---
title: Python3 读取Chrome cookie
url: http://h4ck.org.cn/2022/11/python3-%e8%af%bb%e5%8f%96chrome-cookie/
source: obaby@mars
date: 2022-11-02
fetch_date: 2025-10-03T21:31:15.977402
---

# Python3 读取Chrome cookie

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[业余爱好『Favourite』](https://h4ck.org.cn/cats/cxsj/%E4%B8%9A%E4%BD%99%E7%88%B1%E5%A5%BD%E3%80%8Efavourite%E3%80%8F)

# Python3 读取Chrome cookie

2022年11月1日
[2 条评论](https://h4ck.org.cn/2022/11/10649#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/10/108a170cf25538ea5bd667600043cb50-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/10/108a170cf25538ea5bd667600043cb50-scaled.jpg)

网上搜一下，读取cookie的基本都是这份代码。我也忘了是从那里抄来的了，这里贴一下 ，对于最新的chrome需要修改下路径：

```
# chrome 96 版本以下
# filename = os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data\default\Cookies')
# chrome96 版本以上
# filename = os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data\default\Network\Cookies')
```

全部代码：

```
import sqlite3
import urllib3
import os
import json
import sys
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def dpapi_decrypt(encrypted):
    import ctypes
    import ctypes.wintypes
    class DATA_BLOB(ctypes.Structure):
        _fields_ = [('cbData', ctypes.wintypes.DWORD),
                    ('pbData', ctypes.POINTER(ctypes.c_char))]
    p = ctypes.create_string_buffer(encrypted, len(encrypted))
    blobin = DATA_BLOB(ctypes.sizeof(p), p)
    blobout = DATA_BLOB()
    retval = ctypes.windll.crypt32.CryptUnprotectData(
        ctypes.byref(blobin), None, None, None, None, 0, ctypes.byref(blobout))
    if not retval:
        raise ctypes.WinError()
    result = ctypes.string_at(blobout.pbData, blobout.cbData)
    ctypes.windll.kernel32.LocalFree(blobout.pbData)
    return result
def aes_decrypt(encrypted_txt):
    with open(os.path.join(os.environ['LOCALAPPDATA'],
                           r"Google\Chrome\User Data\Local State"), encoding='utf-8', mode="r") as f:
        jsn = json.loads(str(f.readline()))
    encoded_key = jsn["os_crypt"]["encrypted_key"]
    encrypted_key = base64.b64decode(encoded_key.encode())
    encrypted_key = encrypted_key[5:]
    key = dpapi_decrypt(encrypted_key)
    nonce = encrypted_txt[3:15]
    cipher = Cipher(algorithms.AES(key), None, backend=default_backend())
    cipher.mode = modes.GCM(nonce)
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_txt[15:])
def chrome_decrypt(encrypted_txt):
    if sys.platform == 'win32':
        try:
            if encrypted_txt[:4] == b'x01x00x00x00':
                decrypted_txt = dpapi_decrypt(encrypted_txt)
                return decrypted_txt.decode()
            elif encrypted_txt[:3] == b'v10':
                decrypted_txt = aes_decrypt(encrypted_txt)
                return decrypted_txt[:-16].decode()
        except WindowsError:
            return None
    else:
        raise WindowsError
def get_cookies_from_chrome(domain):
    sql = f'SELECT name, encrypted_value as value FROM cookies where host_key like "%{domain}%"'
    # chrome 96 版本以下
    # filename = os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data\default\Cookies')
    # chrome96 版本以上
    filename = os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data\default\Network\Cookies')
    con = sqlite3.connect(filename)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(sql)
    cookie = ''
    cookie_dict = {}
    for row in cur:
        # print("1111>>>>>",row)
        if row['value'] is not None:
            name = row['name']
            value = chrome_decrypt(row['value'])
            # print("2222>>>>",name,value)
            if value is not None:
                cookie += name + '=' + value + ';'
                cookie_dict[name] = value
    return cookie_dict
if __name__ == '__main__':
    domain = 'taobao.com'   # 目标网站域名
    cookie = get_cookies_from_chrome("")
    print(cookie)
```

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Python3 读取Chrome cookie》](https://h4ck.org.cn/2022/11/10649)
\* 本文链接：<https://h4ck.org.cn/2022/11/10649>
\* 短链接：<https://oba.by/?p=10649>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Chrome](https://h4ck.org.cn/tags/chrome)[cookie](https://h4ck.org.cn/tags/cookie)[Python3](https://h4ck.org.cn/tags/python3)

[Previous Post](https://h4ck.org.cn/2022/11/10651)
[Next Post](https://h4ck.org.cn/2022/10/10574)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年8月4日

#### [爱图集谷爬虫<预览版>[23.08.04][Windows]](https://h4ck.org.cn/2023/08/12801)

2023年7月3日

#### [爱美女网爬虫[预览版] [23.07.02] [Windows]](https://h4ck.org.cn/2023/07/12417)

2021年1月5日

#### [Ganlinmu Spider](https://h4ck.org.cn/2021/01/7962)

### 2 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2022年11月2日 00:33](https://h4ck.org.cn/2022/11/10649#comment-88407)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 106](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 106") Google Chrome 106 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   这能拿到权限吗，那不是可以黑别人

   [回复](#comment-88407)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月2日 09:02](https://h4ck.org.cn/2022/11/10649#comment-88426)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      可以获取指定网站的cookie，这个代码主要是在微图坊爬虫中使用了。微图坊如果没有cookie（账号信息）没有办法获取第二页的内容。当然如果在客户机上运行理论上可以获取各种网站的cookie，有了cookie就可以用来伪造登录信息，冒充用户发布一些虚假内容，或者去买一些乱七八糟的东西（现在这种网站基本没有了）

      [回复](#comment-88426)

### 发表回复 [取消回复](/2022/11/10649#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

评论 \*

显示名称 \*

邮箱 \*

网站

[ ]  在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。

[x] 如果有人回复我的评论，请通过电子邮件通知我。

[x]

Δ

### 标签云[Tag Cloud]

Your browser doesn't support the HTML5 CANVAS tag.

* [yolov5](https://h4ck.org.cn/tags/yolov5)
* [spider](https://h4ck.org.cn/tags/spider)
* [妹子图](https://h4ck.org.cn/tags/%E5%A6%B9%E5%AD%90%E5%9B%BE)
* [Porn](https://h4ck.org.cn/tags/porn)
* [杂谈](https://h4ck.org.cn/tags/zatan)
* [Virus Analysit](https://h4ck.org.cn/tags/virus-analysit)
* [Mac OS](https://h4ck.or...
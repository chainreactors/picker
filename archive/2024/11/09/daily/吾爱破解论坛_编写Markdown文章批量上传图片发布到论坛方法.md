---
title: 编写Markdown文章批量上传图片发布到论坛方法
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651141432&idx=1&sn=9c847606ed93e0e1636a978d29fef55a&chksm=bd50a56c8a272c7ac1dd57fe54dcf67649e91cdb4cd19e3fa92a2b537615378e2864183cc88e&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2024-11-09
fetch_date: 2025-10-06T19:18:32.726891
---

# 编写Markdown文章批量上传图片发布到论坛方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJiaqFRFE3fzC2WG1kcugEdLySX1iaJvCXr1Dicp6eyNSia1cDgKARicE4yTIjDGkyTNnz2BibAicBw3NI0A/0?wx_fmt=jpeg)

# 编写Markdown文章批量上传图片发布到论坛方法

原创

吾爱pojie

吾爱破解论坛

**作者****论****坛账号：漁滒**

### 编写

编写时为了方便实时查看显示，一般会使用pycharm等编辑器进行。

其中大概率会插入不少的图片，如果在发布前一张一张上传到论坛图床，再一个一个替换原来的文本，这会对发布产生非常大的工作量。

所以我就在想有什么办法可以在本地正常编写，又可以一键发布到论坛上呢？我就想编写一个脚本来进行批量上传

为了方便匹配文章中出图片的位置，一般使用一个标准的命名，我使用的是  `![001.jpg](001.jpg)`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJiaqFRFE3fzC2WG1kcugEdLmsvEOLVG4PNvOUsHOGrJ9jmG7J9pS2iaaWdcHZOvclouWbgbTE6UsSQ/640?wx_fmt=png&from=appmsg)

同时真实的图片也放到同目录内

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJiaqFRFE3fzC2WG1kcugEdLweCgRSJ9KUsAkfiaZJRD7ribeKkNrY68icHcIicUOcUchGFZokoyfbCjwQ/640?wx_fmt=png&from=appmsg)

此时编写就可以实时查看内容，非常方便插入图片等系列编写

### 上传

当编写完成后，需要将图片一次性上传到论坛图床

因为我使用的是360极速浏览器发布，所以代码也是基于360极速浏览器的，其他浏览器是类似的

首先进入论坛板块，查看板块的fid

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJiaqFRFE3fzC2WG1kcugEdL9nurlYvFOwwUT5CEKVPibia7d7t4x3251lNM4EZv7lXhacT3nzQskiaKQ/640?wx_fmt=jpeg&from=appmsg)

例如【web逆向】板块的fid就是5

然后直接关闭浏览器

```
 复制代码 隐藏代码

import re
import os
import json
import time
import base64
import psutil
import sqlite3
import win32crypt
import requests_html
from Crypto.Cipher import AES
from requests_toolbelt.multipart.encoder import MultipartEncoder

def main():
    chrome_name = '360ChromeX'
    requests = requests_html.HTMLSession()
    for process in psutil.process_iter():
        if chrome_name in process.name():
            process.kill()
    file_path = os.path.join(os.getenv("LOCALAPPDATA"), chrome_name, 'Chrome', 'User Data', 'Local State')
    state = json.load(open(file_path, 'r', encoding='utf-8'))['os_crypt']
    if state['audit_enabled']:
        key = win32crypt.CryptUnprotectData(base64.b64decode(state['encrypted_key'].encode())[5:])[1]
    else:
        key = b''
    file_path = os.path.join(os.getenv("LOCALAPPDATA"), chrome_name, 'Chrome', 'User Data', 'Default', 'Network', 'Cookies')
    conn = sqlite3.connect(file_path)
    for name, encrypted_value, host_key, path in conn.execute('select name, encrypted_value, host_key, path from cookies'):
        if not encrypted_value:
            continue
        if encrypted_value[:3] == b'v10':
            nonce, encrypted_value = encrypted_value[3:15], encrypted_value[15:]
            crypto = AES.new(key=key, mode=AES.MODE_GCM, nonce=nonce)
            value = crypto.decrypt(encrypted_value)[:-16].decode()
        else:
            value = win32crypt.CryptUnprotectData(encrypted_value)[1].decode()
        requests.cookies.set(name, value, domain=host_key, path=path)
    conn.close()

    fid = '5'  # 根据自己发布在什么板块修改fid
    response = requests.get('https://www.52pojie.cn/forum.php?mod=post&action=newthread&fid=' + fid)
    uid = response.html.find('#imgattachform > [name="uid"]', first=True).attrs['value']
    hash = response.html.find('#imgattachform > [name="hash"]', first=True).attrs['value']
    formhash = response.html.find('#formhash', first=True).attrs['value']
    file_name = os.path.join(os.getcwd(), 'readme.md')
    with open(file_name, 'r', encoding='utf-8') as f:
        md = f.read()
    for img_name, img_path in re.findall('\n\!\[(.+?\.jpg)\]\((.+?)\)', md):
        print(img_name)
        img_full_path = os.path.join(os.getcwd(), img_path)
        fields = {
            "Filedata": (img_name, open(img_full_path, 'rb'), 'image/jpeg'),
            "Filename": file_name,
            "filetype": '.' + file_name.split('.')[-1],
            "formhash": formhash,
            "uid": uid,
            "hash": hash,
            "type": "image"
        }
        multipart = MultipartEncoder(
            fields=fields,
            boundary='----WebKitFormBoundaryLmfEqyU3MTt1Bgy0'
        )
        headers = {
            "Content-Type": multipart.content_type,
        }
        data = multipart.to_string()
        aid = requests.post('https://www.52pojie.cn/misc.php?mod=swfupload&action=swfupload&operation=upload&fid=' + fid, headers=headers, data=data).content.decode()
        print(aid)
        time.sleep(4)
        md = md.replace('\n![' + img_name + '](' + img_path + ')', '\n[attachimg]' + aid + '[/attachimg]')
    with open(file_name.replace('.md', '_img.md'), 'w', encoding='utf-8') as f:
        f.write(md)

if __name__ == '__main__':
    main()
```

将python代码保存到与md文件同目录，根据fid修改上面python代码的fid值，最后运行代码

此时就会自动上传md文件中所有引用到的图片到板块

当脚本完成后，会生成一个带有【\_img.md】的文件，里面的链接已经被替换为可以直接发布到论坛的格式

打开浏览器进入到需要发布的页面

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJiaqFRFE3fzC2WG1kcugEdL1iaGtmlCWj9clK89ic9JVzK16aWFqszZSibDicZ47d8ZIpITice6Dsc3eZg/640?wx_fmt=jpeg&from=appmsg)

此时发帖就会发现提示有多张图片未使用，直接点击使用按钮，然后点击发布md内容，将带有【\_img.md】的的文件里面所有的内容复制进去，就可以完美发帖了

****-官方论坛****

www.52pojie.cn

**👆👆👆**

公众号**设置“星标”，**您**不会错过**新的消息通知

如**开放注册、精华文章和周边活动**等公告

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZK0l7v6mmrudZKXzpdM1WcomgJQnibvLzBUFRSurSkmIfl0ZrDNvSy3MszKNY3XOkcuUbWp31HMjLQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLyxib6edSK27iajkxL2xVZoS1Lbnzjavd2ZDp2KicftN0Tq7vEcJMlLG3chkhj7NcSTEMoLGTRjqDaA/0?wx_fmt=png)

吾爱破解论坛

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLyxib6edSK27iajkxL2xVZoS1Lbnzjavd2ZDp2KicftN0Tq7vEcJMlLG3chkhj7NcSTEMoLGTRjqDaA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过
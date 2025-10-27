---
title: 南墙 WAF 系列（三）–  API SDK
url: https://h4ck.org.cn/2025/04/20214
source: obaby@mars
date: 2025-04-17
fetch_date: 2025-10-06T22:03:30.470214
---

# 南墙 WAF 系列（三）–  API SDK

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

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# 南墙 WAF 系列（三）– API SDK

2025年4月16日
[36 条评论](https://h4ck.org.cn/2025/04/20214#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/04/WechatIMG1465.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/04/WechatIMG1465.jpg)

手里乱七八糟的域名实在是有点多，而这些域名，多数都解析到了同样的站点。或者说是回源是同样的站点，最开始其实并没有套 cdn，中间有段时间连这种 301 302 跳转都被打，就变得很尴尬。301 跳转都能让沙雕给打挂，也的确什么好办法了。

后来发现盾云的 scdn性价比的确不错，于是一股脑的全部套了 scdn，不过，有的也的确没什么流量，于是一些没那么重要的东西放哪里就有些浪费：

[![](https://h4ck.org.cn/wp-content/uploads/2025/04/Jietu20250416-173539.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/04/Jietu20250416-173539.jpg)

所以，思索再三，几天申请了一台 99 块钱的海外轻量，每个月 1t 的流量，感觉应该足够应付这些乱七八糟的服务了。当然，最主要的还是要套上南墙 waf，直接裸奔感觉也不大行。

[![](https://h4ck.org.cn/wp-content/uploads/2025/04/Jietu20250416-173457-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/04/Jietu20250416-173457.jpg)

当然，waf 后面的回源多数还是家里的服务器。这就需要有个工具来更新 waf 的回源地址，今天又完善了一下南墙的 api 接口，代码直接提交 github 的，有需要可以自取。

## 功能特性

* 证书管理
  + 获取证书列表
  + 检查证书
  + 提交证书配置
  + 删除证书
* 站点配置
  + 获取站点列表
  + 更新站点配置
* 用户认证
  + 用户名密码登录
  + 支持双因素认证（OTP）

## 环境要求

* Python 3.x
* 必需的 Python 包：
  + requests
  + jwt
  + urllib3

## 安装说明

1. 克隆仓库：

```
git clone https://github.com/obaby/baby-nanqiang-waf-api-toos.git
cd baby-nanqiang-waf-api-toos
```

2. 安装依赖包：

```
pip install -r requirements.txt
```

使用说明

### 基础用法

```
from baby_nanqiang_api_tools import NanQiangAPI

# 初始化 API 客户端
api = NanQiangAPI(base_url="https://lang.bi:443")

# 登录
result = api.login(username="your_username", password="your_password")
if result:
    print("登录成功")

    # 获取证书列表
    cert_list = api.get_cert_list()
    if cert_list:
        parsed_certs = api.parse_cert_list(cert_list)
        print("证书列表:", parsed_certs)
```

```
证书管理
```

```
# 从文件检查证书
cert_result = api.check_cert_from_files("cert.pem", "key.pem")
if cert_result:
    # 提交证书配置
    submit_result = api.submit_cert_config(cert_result)

# 删除证书
delete_result = api.delete_cert(cert_id=123)
```

### 站点配置

```
# 获取站点列表
site_list = api.get_site_list()
if site_list:
    parsed_sites = api.parse_site_list(site_list)
    print("站点列表:", parsed_sites)

# 更新站点配置
update_result = api.update_site_config(
    ip="192.168.1.1",
    port=443,
    site_id=123,
    uid=456,
    description="我的网站"
)
```

仓库地址：
<https://github.com/obaby/baby-nanqiang-waf-api-tools>

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《南墙 WAF 系列（三）– API SDK》](https://h4ck.org.cn/2025/04/20214)
\* 本文链接：<https://h4ck.org.cn/2025/04/20214>
\* 短链接：<https://oba.by/?p=20214>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Python](https://h4ck.org.cn/tags/python)[南墙 WAF](https://h4ck.org.cn/tags/%E5%8D%97%E5%A2%99-waf)

[Previous Post](https://h4ck.org.cn/2025/04/20237)
[Next Post](https://h4ck.org.cn/2025/04/20194)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2022年10月22日

#### [Kite for PyCharm2022](https://h4ck.org.cn/2022/10/10574)

2023年7月22日

#### [由云盾CC防御导致的WP-CRON异常](https://h4ck.org.cn/2023/07/12641)

2020年2月5日

#### [m3u8 下载工具[Windows]](https://h4ck.org.cn/2020/02/6918)

### 36 comments

1. ![](https://gg.lang.bi/avatar/ffc1ac2ecde17b2eb1caff3e94c119fdaea4dc1a947a08a3092b388bf9b454d0?s=64&d=identicon&r=r) **[acevs](https://acevs.com/)**说道：

   [2025年4月16日 18:20](https://h4ck.org.cn/2025/04/20214#comment-125594)

   ![Level 5](https://badgen.net/badge/亲密度/Level 5/orange?icon=codebeat)

   ![Google Chrome 131](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 131") Google Chrome 131 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   不撞南墙不回头
   不敢逾越雷池半步
   南墙
   雷池

   [回复](#comment-125594)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年4月16日 18:42](https://h4ck.org.cn/2025/04/20214#comment-125595)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 134](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 134") Google Chrome 134 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      是哒 就是这个意思 哈哈哈

      [回复](#comment-125595)
2. ![](https://gg.lang.bi/avatar/9c11cacf3c2c30b8259d9ae155dd014cd86ed868699b146c2c75e627d8302fd5?s=64&d=identicon&r=r)

   [2025年4月16日 18:51](https://h4ck.org.cn/2025/04/20214#comment-125596)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Google Chrome 134](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 134") Google Chrome 134 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   不会玩 ![cry](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/cry.gif)

   [回复](#comment-125596)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年4月16日 20:58](https://h4ck.org.cn/2025/04/20214#comment-125601)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 134](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 134") Google Chrome 134 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      嗐，这个东西感觉有点用，所以折腾一下

      [回复](#comment-125601)
3. ![](https://gg.lang.bi/avatar/c8b1c4e066955840427abd9f454b9fb9569d4480ec1b84bb78c8b210d91893d8?s=64&d=identicon&r=r)

   [2025年4月16日 20:40](https://h4ck.org.cn/2025/04/20214#comment-125598)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Google Chrome 109](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 109") Google Chrome 109 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   看了小清新灵妹妹又看科幻版

   [回复](#comment-125598)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年4月16日 20:58](https://h4ck.org.cn/2025/04/20214#comment-125603)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.ne...
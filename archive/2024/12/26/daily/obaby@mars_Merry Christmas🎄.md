---
title: Merry Christmas🎄
url: https://h4ck.org.cn/2024/12/18865
source: obaby@mars
date: 2024-12-26
fetch_date: 2025-10-06T19:36:01.585782
---

# Merry Christmas🎄

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

[个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# Merry Christmas🎄

2024年12月25日
[63 条评论](https://h4ck.org.cn/2024/12/18865#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/8641735088893_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/12/8641735088893_.pic_.jpg)

原本，按照自己的想法是不准备再写文章的。前段时间，自己抽了那么一点点的时间，做了一个个人页面，<http://i.oba.by> .期间，[![杜郎](https://g.h4ck.org.cn/avatar/1fbf51cf49f5c369ad2cd13d76c15c42?s=64&d=mm&r=g)杜郎](https://dujun.io)给提了不少建议。但是鉴于自己 ps 修图的水平实在有限，所以最终很多东西也没达到自己想要的效果。

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/2024-12-25-09.22.14-i.oba_.by-44e4806d30cf-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/12/2024-12-25-09.22.14-i.oba_.by-44e4806d30cf.jpg)

然而，昨天看下面的足迹地图的时候，发现出问题了，全部被贴上了未获取商用授权的水印。

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/Jietu20241224-155014-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/12/Jietu20241224-155014.jpg)

这就很离谱，后来登录百度地图开发者，才发现一个问题，那就是认真的时候不小心给认证成了企业开发者，这尼玛就离谱。当时还在想，为什么提示填写企业邮箱更容易认证通过。

后来才发现，默认就是认证企业开发者，个人开发者被藏在了隐蔽的地方。只能切换账号重新认证。

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/Jietu20241225-092623-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/12/Jietu20241225-092623.jpg)

不过这么一来，那么地理编码就会出现问题，因为目前接入的地理位置已经超过 30 个。调用这个接口就会收到下面的提示：

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/WechatIMG865-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/12/WechatIMG865.jpg)

的确，各种限制无处不在。不过好在之前设计的时候给每个地点预留了 gps 坐标信息，如果已经有了 gps 坐标，那么就不会再调用 jsapi 进行解析。

添加服务端 ak，直接后台处理坐标之后，写入数据库：

```
def process_location_cordinate(self, request):

    baidu_key_set = MapKey.objects.filter(server_key__isnull=False).last()
    if baidu_key_set is None:
        return ErrorResponse(msg='请先配置百度地图服务端 key')

    locations = Location.objects.all()
    successed = []
    for l in locations:
        if l.latitude is None or l.lontitude is None:
            lng,lat = get_location_cordinate(l.name, baidu_key_set.server_key)
            if lng is not None and lat is not None:
                l.latitude = lat
                l.lontitude = lng
                l.save()
                print(l)
                successed.append(l)
    return DetailResponse(self.get_serializer(successed, many=True).data)
```

地理位置解析代码：

```
def get_location_cordinate(location_name, server_key):
    resp = requests.get('https://api.map.baidu.com/geocoding/v3/?address='+location_name+ '&output=json&ak='+ server_key)

    print(resp.json())
    js = resp.json()
    if js['status'] == 0:
        return js['result']['location']['lng'],js['result']['location']['lat']
    return None, None
```

在处理之前，去后台设置 服务端 ak。

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/Jietu20241225-093216.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/12/Jietu20241225-093216.jpg)

相关代码已经更新，见开源项目：https://github.com/obaby/BabyFootprintV2

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/Jietu20241225-112635-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/12/Jietu20241225-112635.jpg)

**再次祝大家圣诞快乐，嘻嘻**

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Merry Christmas🎄》](https://h4ck.org.cn/2024/12/18865)
\* 本文链接：<https://h4ck.org.cn/2024/12/18865>
\* 短链接：<https://oba.by/?p=18865>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[圣诞节](https://h4ck.org.cn/tags/%E5%9C%A3%E8%AF%9E%E8%8A%82)[足迹地图](https://h4ck.org.cn/tags/%E8%B6%B3%E8%BF%B9%E5%9C%B0%E5%9B%BE)

[Previous Post](https://h4ck.org.cn/2024/12/18877)
[Next Post](https://h4ck.org.cn/2024/12/18857)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年1月10日

#### [应用商店上架记](https://h4ck.org.cn/2024/01/15080)

2025年2月28日

#### [自欺欺人](https://h4ck.org.cn/2025/02/19501)

2023年2月11日

#### [是UPS吖（一）–开箱](https://h4ck.org.cn/2023/02/11157)

### 63 comments

1. ![](https://gg.lang.bi/avatar/59d4c005e3a89761a540d87a5b3888bb2e9fcd9f8210f2c5792ad8c0cad080e9?s=64&d=identicon&r=r) **[bosir](https://bosir.cn)**说道：

   [2024年12月25日 12:07](https://h4ck.org.cn/2024/12/18865#comment-122535)

   ![Level 2](https://badgen.net/badge/亲密度/Level 2/cyan?icon=codebeat)

   ![Google Chrome 103](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 103") Google Chrome 103 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   圣诞快乐啊萝莉御姐~
   永远美丽/幸福/快乐~

   [回复](#comment-122535)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年12月25日 13:22](https://h4ck.org.cn/2024/12/18865#comment-122539)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      嗯嗯，你也一样哦，幸福快乐。嘻嘻

      [回复](#comment-122539)
2. ![](https://gg.lang.bi/avatar/7ca2eb6a07de78fd08989205bc741ef66a4746b1f518fa164f8e71b016366c75?s=64&d=identicon&r=r)

   [2024年12月25日 12:35](https://h4ck.org.cn/2024/12/18865#comment-122536)

   ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 131](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 131") Microsoft Edge 131 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   圣诞快乐。

   [回复](#comment-122536)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年12月25日 13:22](https://h4ck.org.cn/2024/12/18865#comment-122540)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      圣诞快乐

      [回复](#comment-122540)
3. ![](https://gg.lang.bi/avatar/e82222af6a5616ec24ae02e0eaa8ceacadef6fd83873a62c639eefd4cf7be8b6?s=64&d=identicon&r=r)

   [2024年12月25日 12:37](https://h4ck.org.cn/2024/12/18865#comment-122537)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Safari 18](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 18") Safari 18 !...
---
title: Uniapp 鸿蒙 next 初体验（+随笔）
url: https://h4ck.org.cn/2024/08/17791
source: obaby@mars
date: 2024-08-10
fetch_date: 2025-10-06T18:03:26.034700
---

# Uniapp 鸿蒙 next 初体验（+随笔）

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

[个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj), [前端开发『FrontEnd』](https://h4ck.org.cn/cats/cxsj/%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91%E3%80%8Efrontend%E3%80%8F)

# Uniapp 鸿蒙 next 初体验（+随笔）

2024年8月9日
[51 条评论](https://h4ck.org.cn/2024/08/17791#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/WechatIMG489.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/WechatIMG489.jpg)

上周看完了《唐朝诡事录之西行》，续作水准个人感觉还是可以的，一个诡字延续的也比较成功，故事的多重反转也算比较成功，不唐突，基本能够自洽。而我向来对志怪之事也颇为好奇，不管是书籍、还是影视作品多有涉猎。如果说从中学到了什么东西，那就是人生似乎毫无意义，当鬼也区别不大，所有的一切皆为虚妄。

人生起起落落，不过还是为了那蝇营狗苟的利益，仅此而以，不管是鬼神志怪，还是人心险恶，都有异曲同工之效。昨晚辗转反侧之计，回想过往种种，终究还是常人一个，可能连平均水平都不够。算了算手里还有几块钱，在这之后，忽然觉得活着也没什么意义。甚至连失踪、消失的想法都有了。昨天下午才加上了一个倒计时，想着自己还能再活六十年，忽然间就觉得那个倒计时应该改到明天。

也许等哪天这个想法足够坚定了，后路也想好了，取一万现金，开上那辆风烛残年的老车，或许沿着丝绸之路一路西行，等哪天看到满天的黄沙飞舞之际，我就驱车进去，淹没在这滚滚黄沙里。

最后的这段路程，自然不会选择进西藏去进行所谓的洗涤灵魂。我的灵魂比布达拉宫的那些供奉的僧侣要干净，几十吨黄金装饰的富丽堂皇的布达拉宫，我没有去过，但是如果说佛需要镀金身才渡人，那这金身不镀也罢。那些用少女的骨头、头骨制成的法器，又如何超度活人？

如果牺牲才能渡人，那这与妖怪无所区别，如果我是那个被献祭的少女，我只会留下恶毒的诅咒。当然啊，愚昧会给那些少女洗脑，告诉她这是他的荣耀以及光荣。所以，那些一路跪拜去西藏的，顶礼膜拜的到底是魔是佛？

所以，这个最后一段路程我不会选择西藏，因为，我是一个好人。

好了，言归正传。其实本来要写纯技术文的，但是昨晚脑子里装的东西有点多。索性一并写了吧。

其实 uniapp 对于鸿蒙 next 的支持，应该是前段时间就出来了，但是由于自己的懒惰心理，一直拖着。直到大约周二的时候才想起来尝试将闺蜜圈 app 跑到鸿蒙上。

uni 对于鸿蒙的支持，仅支持 vue3 的项目，所以在体验之前，需要先将 2 的项目转换成 3 的项目，uni 官方也给出了文档：

https://uniapp.dcloud.net.cn/tutorial/migration-to-vue3.html

这件工作，在大约上个月就尝试过了，目前能以 vue3 的配置跑起来，主要是各种属性以及环境变量的接口变更：

```
// 之前 - Vue 2
Vue.prototype.$http = () => {};

// 之后 - Vue 3
const app = createApp({});
app.config.globalProperties.$http = () => {};
```

这些调整做完了之后基本就可以跑起来了，vue3 不支持 css .deep 语法，我就去掉了，目前看来倒是也基本正常。

至于怎么让 uni 支持鸿蒙 next 开发，官方也给了文档：

https://uniapp.dcloud.net.cn/tutorial/harmony/dev.html#%E5%85%BC%E5%AE%B9%E6%80%A7%E8%AF%B4%E6%98%8E

环境需求：

* DevEco-Studio 5.0.3.400 以上 [下载地址](https://developer.huawei.com/consumer/cn/deveco-developer-suite/enabling/kit?currentPage=1&pageSize=100)
* 鸿蒙系统版本 API 12 以上 （DevEco-Studio有内置鸿蒙模拟器）
* HBuilderX-alpha-4.22 以上

不过这个 deveco 下载需要先申请开发者资格，这个大约需要一天时间，如果顺利的话。于是周二申请之后，周三拿到了开发资格。

后续是下载模拟器，这个模拟器的下载，也并不是可以直接可以下载的，需要申请模拟器的体验资格。[![](https://h4ck.org.cn/wp-content/uploads/2024/08/Screenshot-2024-08-08-214814.png)](https://h4ck.org.cn/wp-content/uploads/2024/08/Screenshot-2024-08-08-214814.png)

这个东西申请又需要一天的时间，官方给的的时间是8 个小时，但是这个由于mbp 的磁盘满了，申请了之后也只能在家里的windows 电脑上体验。

申请过了之后才能下载模拟器镜像创建模拟器，否则是没有模拟器可以运行的。模拟器运行起来之后，到这里鸿蒙开发工具的配置基本就算完成了。

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/Screenshot-2024-08-08-214833.png)](https://h4ck.org.cn/wp-content/uploads/2024/08/Screenshot-2024-08-08-214833.png)

后续是 hbuilder 的配置，点击设置，配置华为开发工具的路径：

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/1720092016399okjuod823f.png)](https://h4ck.org.cn/wp-content/uploads/2024/08/1720092016399okjuod823f.png)

这个路径最好是到 exe，不要填到目录下就结束，最后一行是新增的，如果就配置到 studio 路径，大概率启动 deveco 会失败。

```
{
"bytedanceApp.devTools.path" : "",
"editor.colorScheme" : "Default",
"editor.wordWrap" : true,
"qqApp.devTools.path" : "g:\\Program Files (x86)\\Tencent\\QQ小程序开发者工具",
"harmony.devTools.path" : "G:\\Huawei\\DevEco Studio\\bin\\devecostudio64.exe"
}
```

编辑 manifest.json 添加鸿蒙离线 sdk，其实这个 sdk 本质上是个鸿蒙的项目模板，叫做 sdk 而以，如果把他当成个 sdk 就会出现认知上的一些问题，如果当成一个模板工程那就简单了。每个鸿蒙项目单独复制一个模板项目，进行编译即可。如果是 sdk，那么需要配置那么多不同的 sdk 路径吗？

```
"app-harmony": {
"projectPath": "E:\\uniapp_projects\\huawei\\134"
},
```

然后就可以在hbuilder 中编译，选择到运行 deveco 了。

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/Screenshot-2024-08-08-214748.png)](https://h4ck.org.cn/wp-content/uploads/2024/08/Screenshot-2024-08-08-214748.png)

如果 hbuilder 提示运行失败也不要紧，直接去 deveco 中运行即可。本质山是 hbuilder 把资源编译之后扔到了 deveco 的示例项目中（也就是前文提到的所谓的鸿蒙离线 sdk）。

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/Screenshot-2024-08-08-213928-tuya.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/Screenshot-2024-08-08-213928-tuya.jpg)

到这里，发现自己之前项目升级还算是比较成功，不过由于 unihttp 请求的代码 vue2 以及 vue3 也有区别，代码尚未调整，所以目前还是有些问题的，不过能跑起来，这基本就成功了一大半了。

## 几个问题：

### 1.code:9568347 error: install parse native so failed

出现这个错误，按照官方文件解释是编译的原生代码架构有问题参考https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs-V5/faqs-app-debugging-14-V5

需要添加以下架构：

```
"buildOption": {
  "externalNativeOptions": {
    "abiFilters": ["arm64-v8a", "x86_64"]
  },
}
```

然而，这个不是解决 uniapp 的问题的办法，添加之后依然报错，后来以为是自己写的 uni 的原生插件有问题。将原生插件删除之后依然报错，继续上网搜索发现 flutter 对于鸿蒙 windows x86 模拟器的支持也有问题，到此刻忽然发现问题的关键可能在于 uniapp 给的所谓的鸿蒙离线 sdk 中压根就没包含 x86\_64 架构的二进制包。

既然1.3.5 有问题，之前在一篇文章https://blog.csdn.net/weixin\_46591361/article/details/140543443看到过 1.3.4 的离线包，那这个也有问题吗？

下载 134 的包，替换掉 135 的包，重新打包安装一切 ok 了，这个就是上面运行成功的那张图了。

1.3.4 下载链接： https://web-ext-storage.dcloud.net.cn/uni-app/harmony/zip/template-1.3.4.tgz

### 2.权限问题：code:9568289 error: install failed due to grant request permissions failed

官方给的方案：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs-V5/faqs-app-debugging-10-V5

该问题是由于默认应用等级为normal，只能使用normal等级的权限，如果使用了system\_basic或system\_core等级的权限，将导致报错。

对于HarmonyOS应用，请参考[使用ACL签名配置指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/ide-signing-0000001587684945-V5#section9786111152213)完成ACL提权。

搜了一通，也没什么建设性方案，既然是权限问题，那肯定有定义的地方，直接在鸿蒙项目代码搜索，找到以下文件：

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/Screenshot-2024-08-08-214339.png)](https://h4ck.org.cn/wp-content/uploads/2024/08/Screenshot-2024-08-08-214339.png)

将 requestPermissions 下多余的权限删除即可，这个东西如果要配置权限申请等乱七八糟的东西周期太长了，如果要上线运行，或者一定需要这些权限还是按照官方文档老老实实的申请吧。

至于后续什么时候打鸿蒙 next 的原生包发布，看情况吧，毕竟还有一些代码没改完。在 135 的代码上也不好调试，一切从长计议，再说吧。

折腾来折腾去，真的有意义吗？

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Uniapp 鸿蒙 next 初体验（+随笔）》](https://h4ck.org.cn/2024/08/17791)
\* 本文链接：<https://h4ck.org.cn/2024/08/17791>
\* 短链接：<https://oba.by/?p=17791>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[DevEco-Studio](https://h4ck.org.cn/tags/deveco-studio)[UniApp](https://h4ck.org.cn/tags/uniapp)[鸿蒙](https://h4ck.org.cn/tags/%E9%B8%BF%E8%92%99)[鸿蒙 next](https://h4ck.org.cn/tags/%E9%B8%BF%E8%92%99-next)

[Previous Post](https://h4ck.org.cn/2024/08/17823)
[Next Post](https://h4ck.org.cn/2024/08/17775)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年10月18日

#### [熬夜游戏 2 — 《触动精灵》之战](https://h4ck.org.cn/2024/10/18337)

2024年8月13日

#### [漏风的小棉袄](https://h4ck.org.cn/2024/08/17823)

2024年11月6日

#### [半夜“机”叫](https://h4ck.org.cn/2024/11/18453)

### 51 comments

1. ![](https://gg.lang.bi/avatar/881263b2794f24002d7f1feb051ed0b904d35c58ca16db9972b44148dc12d9c3?s=64&d=identicon&r=r) **[姜先森](http://jiangjizhong.com)**说道：

   [2024年8月9日 11:30](https://h4ck.org.cn/2024/08/17791#comment-118029)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Firefox 115](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/firefox.png "Firefox 115") Firefox 115 ![Windows 7](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-4.png "Windows 7") Windows 7 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   看到言归正传我就有自知之明了，下面不是给我看的，哈哈！

   [回复](#comment-118029)

   ...
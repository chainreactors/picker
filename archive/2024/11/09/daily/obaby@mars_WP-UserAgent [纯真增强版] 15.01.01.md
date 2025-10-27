---
title: WP-UserAgent [纯真增强版] 15.01.01
url: https://h4ck.org.cn/2024/11/18473
source: obaby@mars
date: 2024-11-09
fetch_date: 2025-10-06T19:15:59.053996
---

# WP-UserAgent [纯真增强版] 15.01.01

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

[后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# WP-UserAgent [纯真增强版] 15.01.01

2024年11月8日
[100 条评论](https://h4ck.org.cn/2024/11/18473#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/WechatIMG1196.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/WechatIMG1196.jpg)

之前为了下载纯真的ip 地址数据库订阅了他们的公众号，前几天的时候看到推送说什么数据库格式更新了，有了 czdb 的格式，并且提供了各种语言的 sdk。

不过这个东西应该不是最近才推的，因为印象里貌似很久之前就看到[皇家园林](https://hjyl.org)写的数据库迁移的文章。官方给的sdk 地址是这个：https://github.com/tagphi/czdb\_searcher\_php

按照文档操作，感觉也不复杂，直接：

```
composer require czdb/searcher
```

composer导入，就一行命令的事，但是为了弄个插件，需要在服务器上装这么个东西？那插件安装到别的地方也麻烦啊。想着一次性解决这个问题，直接下载源码，修改导入方式，按照网上的教程一通改，并不好使，最后 还是请教[杜郎](https://dujun.io)，才解决了这个问题：

[![composer](https://h4ck.org.cn/wp-content/uploads/2024/11/WechatIMG698.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/WechatIMG698.jpg)

真不错，直接小花花+1.

下载 copmoser 导出的包，直接扔到插件目录下，

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241108-102050.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241108-102050.jpg)

因为最终要修改的是 ip2text.php 文件中的convertip函数，所以直接扔到 show-useragent 目录下，在代码中导入代码，并且初始化：

```
require_once __DIR__ . '/vendor/autoload.php';

use Czdb\DbSearcher;

$v4databasePath = dirname(__FILE__).'/czdb/db/cz88_public_v4.czdb';
$v6databasePath = dirname(__FILE__).'/czdb/db/cz88_public_v6.czdb';

$queryType = 'MEMORY';
$key = 'n2pf2******************==';

// Initialize the DbSearcher with the command line arguments
// $instance = new SomeNamespace\SomeClass();

$v4dbSearcher = new DbSearcher($v4databasePath, $queryType, $key);
$v6dbSearcher = new DbSearcher($v6databasePath, $queryType, $key);

// $dbSearcher = new DbSearcher($databasePath, $queryType, $key);

function convertip($ip) {
    global $v4dbSearcher;
    global $v6dbSearcher;
    try{
        if(strpos($ip, ':') != false){
            $region = $v6dbSearcher->search($ip);
        }else if (strpos($ip, '.')!= false)
        {
            $region = $v4dbSearcher->search($ip);
        }else{
            $region='Unknown';
        }
    }catch (Exception $e) {
        // Handle the exception and inform the user
        $region = 'Exception';
    }

    return $region;
}
```

这里初始化了两个DbSearcher，分别对应 v4 和v6的查询。查询代码也很简单，就上面这几行。

同样，既然有了国家代码，那剩下的就是去掉原来通过接口查询所属国家的问题了，之前用接口是因为qqwry.dat 旧版本没有 v6 的数据，后来也一直没更新，所以归属地现实国旗是通过接口实现的，现在既然 46 都有了，那就可以直接本地解析了，不过比较坑爹的是 v4 的地址是“-”拼接的，v6 的地址感觉是空格，实际上是个制表符’\t’，为了这个制表符废了半天的劲，一直解析不出来，直接头大：

```
function getCountryName($str) {
    $parts = explode('–', $str);
    $name = count($parts) > 0 ? $parts[0] : '';
    // print($name);
    if (strpos($name, " ")!==false){
        $parts = explode(" ", $str);
        $name = count($parts) > 0 ? $parts[0] : '';
        // print($name);
    }
    if (strpos($name, "\t")!==false){
        $parts = explode("\t", $str);
        $name = count($parts) > 0 ? $parts[0] : '';
        // print($name);
    }
    return $name;
}
```

之所以解析不出来是最开始的if (strpos($name, “\t”)!==false)用的单引号，后来才发现，单引号下转义字符无效，这尼玛是凭什么啊，**果然 php 是最好的语言。**

后面就是讲国家名转换为 2 位国家代码了：

```
function getCountryCode($countryName) {
    $countryMap = array(
        '中国' => 'CN',
        '美国' => 'US',
        '日本' => 'JP',
        '韩国' => 'KR',
        '俄罗斯' => 'RU',
        '法国' => 'FR',
        '德国' => 'DE',
        '英国' => 'GB',
        '意大利' => 'IT',
        '加拿大' => 'CA',
        // 省略部分国家地区
        '瓦利斯和富图纳' => 'WF',
        '也门' => 'YE',
        '赞比亚' => 'ZM',
        '津巴布韦' => 'ZW',
        );
    $countryName = removeWhitespace($countryName);
    $countryCode = 'unknown';
    if (isset($countryMap[$countryName])) {
        $countryCode = $countryMap[$countryName];
    }
    // ; return $countryCode;
    return strtolower($countryCode);
}
```

到这里改造基本就全部完成了。

更新日志：

```
= v15.01.01 =
* 替换本地IP归属地查询数据库为纯真CZDB格式
* 替换IPv6归属地查询，替换为本地数据库，去掉查询服务器配置功能
* 鉴于纯真数据库需要授权码，需要去 https://cz88.com/geo-public 获取授权密钥以及数据库文件
* 密钥配置文件，ip2c-text.php $key = 'n2pf2******************pg==';
* 数据库下载之后放入show-useragent\czdb\db 目录下，文件名分别为： cz88_public_v4.czdb cz88_public_v6.czdb
```

插件安装无法直接使用，请按照下面的步骤操作：

**\* 需要去 https://cz88.com/geo-public 获取授权密钥以及数据库文件**

**\* 密钥配置文件，ip2c-text.php $key = ‘n2pf2\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*pg==’;**

**\* 数据库下载之后放入show-useragent\czdb\db 目录下，文件名分别为： cz88\_public\_v4.czdb cz88\_public\_v6.czdb**

实际效果：

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241108-103732.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241108-103732.jpg)

[![](https://h4ck.org.cn/wp-content/uploads/2024/11/WechatIMG699.png)](https://h4ck.org.cn/wp-content/uploads/2024/11/WechatIMG699.png)

插件下载地址：

温馨提示: 此处隐藏内容需要[发表评论](#respond "发表评论")，并且审核通过后才能查看。
（发表评论请勾选 **在此浏览器中保存我的显示名称、邮箱地址和网站地址，以便下次评论时使用。**）
（请仔细检查自己的昵称和评论内容，以免被识别为垃圾评论而导致无法正常审核。）

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《WP-UserAgent [纯真增强版] 15.01.01》](https://h4ck.org.cn/2024/11/18473)
\* 本文链接：<https://h4ck.org.cn/2024/11/18473>
\* 短链接：<https://oba.by/?p=18473>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[CZDB](https://h4ck.org.cn/tags/czdb)[IP](https://h4ck.org.cn/tags/ip)[WordPress](https://h4ck.org.cn/tags/wordpress)[归属地](https://h4ck.org.cn/tags/%E5%BD%92%E5%B1%9E%E5%9C%B0)[纯真数据库](https://h4ck.org.cn/tags/%E7%BA%AF%E7%9C%9F%E6%95%B0%E6%8D%AE%E5%BA%93)

[Previous Post](https://h4ck.org.cn/2024/11/18486)
[Next Post](https://h4ck.org.cn/2024/11/18453)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2013年5月26日

#### [Black Vendetta -改变主题颜色](https://h4ck.org.cn/2013/05/5215)

2025年4月2日

#### [南墙 WAF 系列（二）– 网站证书自动更新](https://h4ck.org.cn/2025/04/20086)

2025年3月20日

#### [418 I’m a teapot](https://h4ck.org.cn/2025/03/19860)

### 100 comments

[« 上一页](https://h4ck.org.cn/2024/11/18473/comment-page-1#comments)
[1](https://h4ck.org.cn/2024/11/18473/comment-page-1#comments)
2

1. ![](https://gg.lang.bi/avatar/40d2e0687a1cbafdbfc0779f3665bc5200eeaddd49f45ac3c0f779b5201b1fc8?s=64&d=identicon&r=r) **阿萨**说道：

   [2025年3月15日 15:17](https://h4ck.org.cn/2024/11/18473/comment-page-2#comment-124629)

   ![Level 1](https://badgen.net/badge/亲密度/Level 1/gray?icon=codebeat)

   ![Google Chrome 86](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 86") Google Chrome 86 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   我需要下载，很喜欢博主的技术

   [回复](#comment-124629)
2. ![](https://gg.lang.bi/avatar/23e3ceeef9efed1b9022d504aad1743b680025e8c2eba0ef9296bd314d262d06?s=64&d=identicon&r=r)

   [2025年4月27日 18:26](https://h4ck.org.cn/2024/11/18473/comment-page-2#comment-125915)

   ![Level 1](https://badgen.net/badge/亲密度/Level 1/gray?icon=codebeat)

   ![Microsoft Edge 135](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 135") Microsoft Edge 135 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/im...
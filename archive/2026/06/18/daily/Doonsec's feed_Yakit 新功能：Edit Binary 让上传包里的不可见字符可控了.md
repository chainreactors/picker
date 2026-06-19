---
title: Yakit 新功能：Edit Binary 让上传包里的不可见字符可控了
url: https://mp.weixin.qq.com/s/VGsPhbBtrwN8ygYpqKSCiw
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:02:59.277460
---

# Yakit 新功能：Edit Binary 让上传包里的不可见字符可控了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72HBD2iaeEicosEDveqNicJ0uHrcDEfFVM67c7mgmynodibbnE53ABfjRAvGefRHjjBNufb3icbgbZUn5IpBA0xeUuPOMdv0kTkVgtjs/0?wx_fmt=jpeg)

# Yakit 新功能：Edit Binary 让上传包里的不可见字符可控了

原创

YAK
YAK

Yak Project

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdUYXaiccQFYhEArmU3f9ef0VNmBjcyLt7PUV08libAc8EmnhuFSzlnIiaJThN911S7468pdssPD8hgw/640?wx_fmt=png&from=appmsg)

测上传漏洞的时候，有一种场景特别烦人：

> 你需要在数据包里写入真实的 `\x00`、`\x0a` 这类不可见字节，但普通文本编辑器里根本没法直接输入它们。

比如空字节截断、换行解析这些经典 bypass，payload 长这样：

```
```
filename="shell.php\x00.jpg"filename="shell.php\x0a.jpg"
```
```

以前要在 Yakit 里发出真实的空字节，通常得用 URL 解码类的 Fuzztag 间接构造，比如：

```
```
filename="shell.php{{urldec(%00)}}.jpg" // 或者{{null()}}
```
```

`{{urldec(%00)}}` 渲染后才会变成真正的 `0x00` 字节。但这种方式有几个问题：

* 要记住 `urldec`、`urldecode` 这类 Fuzztag 的写法；
* 多个特殊字节混在一起时，可读性很差；
* 没法直观确认最终发出去的字节到底是不是 `0x00`；
* 如果还要换行符、图片魔数之类，得组合一堆标签，越写越乱。

最近 Yakit 新分支在 Web Fuzzer 里加了一个 **Edit Binary** 功能，把这件事直接集成到了编辑器里。这篇文章介绍一下它怎么用，以及为什么上传包改包会因此变简单。

**一、Edit Binary 是什么？**

当 MITM 数据包中存在二进制流时， MITM 数据包的 body 会变成含有 {{unquote(...)}} 包裹的数据包，而 Edit Binary 就是针对 `{{unquote(...)}}`、`{{hexdecode(...)}}`、`{{base64decode(...)}}` 这类二进制 Fuzztag 的可视化编辑器。

当你在数据包里存在，或者写了这样的标签：

```
```
{{unquote("shell.php\x00.jpg")}}
```
```

Yakit 会把它渲染成一个小卡片：

```
```
Binary[0x736865..13B] Click to modify
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72FAibvzicCricQSGpam0ZyGo7PDk0BoL3T9k39yIbRO8naMqyEOu0aTvD2mnIMibfraibrkoOl3J33AN6QPGYfgDWcH89OOSBjwg8UU/640?wx_fmt=png&from=appmsg)

点击这个卡片，就会弹出 `Edit Binary - {{unquote(...)}}` 窗口，你可以像用 Hex Editor 一样直接修改里面的原始字节。

**二、Binary 卡片什么时候会出现？**

先说两个容易踩坑的点。

***YAK***

**2.1 引号必须用双引号**

`unquote` 标签目前只识别双引号字符串。

如果你写成：

```
```
{{unquote('shell.php\x00.jpg')}}
```
```

它**不会**被折叠成 Binary 卡片，因为源码里的正则只匹配 `"``..."`（`binaryFuzztag.ts:153`）。

正确写法：

```
```
{{unquote("shell.php\x00.jpg")}}
```
```

***YAK***

**2.2 没有长度门槛**

`unquote` / `hexdecode` / `base64decode` 是**可编辑标签**，源码里没有对它们设置长度门槛，**无论内容多短都会折叠成卡片**。

```
```
{{unquote("\x00")}}           ← 1 个字节，也会折叠成 Binary 卡片{{hexdecode(00)}}              ← 1 个字节，也会折叠成 HexString 卡片{{base64decode(AA==)}}         ← 1 个字节，也会折叠成 Base64 卡片
```
```

注意语法区别：

* `unquote` 的参数是**带双引号的字符串**：`{{unquote("\x00")}}`
* `hexdecode` / `base64decode` 的参数**不需要引号**：`{{hexdecode(00)}}`、`{{base64decode(AA==)}}`

**三、Edit Binary 界面长什么样？**

弹窗主要分为三块：

|  |  |
| --- | --- |
| 区域 | 内容 |
| 顶部 | 标签信息：`Tag: {{unquote(...)}}`、`Bytes: 13`、`Head: 0x7368...` |
| 中间 | Hex 编辑器，十六进制 + ASCII 双栏展示 |
| 底部 | 工具栏：`插入` / `替换` 模式、`HEX` / `ASCII` 输入、输入框、`应用` 按钮 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72FLMr67FsLNUVeT0RTTlapFsOFe6vltsBdvI971zXbNJE35evyfVx8SVQv5x6WWWqJhNGbeLmRmzniaEGqEKNfZKLYJhDm3lrKs/640?wx_fmt=png&from=appmsg)

**四、两种模式 + 两种输入**

***YAK***

**4.1 替换模式（默认）**

打开 Edit Binary 时，默认就是**替换**模式。

这个模式必须先**在下方 Hex 视图里选中一段字节**，然后输入内容去覆盖它。

* 没选中时提示：`请在下方选中要替换的字节`
* 选中后提示：`选区: 0x2 - 0x04 (len 3)`

如果输入内容比选区更长，会弹窗问你要「继续追加多余部分」还是「放弃多余部分」。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72EkdNYIn0uDicKyxic7LS5WDK3BzjBMibCniajr8z7ic8YaN1aKm2NBloU8S1c1jzlvthice4vcXCbjkU86HAKt5BF2oOyX433nXMiauM/640?wx_fmt=png&from=appmsg)

点击 **应用** 替换成功

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72FHTr6hZefoIaGicmo1xCz3VjcuibVO7a9Oz2v1sYX0M4utEfhDZbc66hU818jNQjWp6bHq23mdaJnEyibCExK9iavsKORJAk1IiaIY/640?wx_fmt=png&from=appmsg)

***YAK***

**4.2 插入模式**

切换到**插入**模式后，输入内容会插入到当前定位的位置。

* 如果你在 Hex 视图里**点击某个字节**（或选中一段），内容会插入到该位置**之前**；
* 如果**完全没有选中任何字节**，内容会追加到整个 buffer 的**末尾**。

提示语对应为：

```
```
插入位置: 0x0        ← 有选中/定位时插入到末尾(可在下方点击定位)   ← 无选中时
```
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72E0BWZQ8Bqsx0YrSV7ddqWWtGBibrotBTWUDFgibsgfUuib2UMa1AHtZmw2iaDP3RwCNwwvSBIy6Lvfo8BU7OpXO1xbsX0ibKDEnk1s/640?wx_fmt=png&from=appmsg)

点击 **应用** 插入成功

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72GaanItibhU6NYWzmXnqsp1J5epVGgOlvgBmNqmMtfGzbMicibDKqBic35miadHwh1KSkbcYb3kkovxRfj4ibWXXJ5CcKgRSb1DKba00/640?wx_fmt=png&from=appmsg)

插入或者替换成功后，点击提交，可以看见如下的 [Changed] 表示数据已经被修改过

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72GOiaRmQFkjyPiafKSaSvP2lT7lPUiclibHyoAiazarsuW8lUkYfKiabQ4CTuMWHdj8ia9JTCIEd5yM5xicGBBwMFrZGdyXVGWoRcoFXcs/640?wx_fmt=png&from=appmsg)

***YAK***

**4.3 HEX 输入**

适合写入不可见字节。

输入框 placeholder：

```
```
如 ffd8ff..(偶数位hex)
```
```

规则：

* **不需要****`0x`****前缀**，直接写十六进制字符；
* 两个字符代表一个字节，所以**长度必须是偶数**；
* 只能包含 `0-9`、`a-f`、`A-F`，中间可以加空格分隔；
* 长度为奇数或包含非法字符时，会报错：`invalid hex input, expect even-length hex string`。

比如要写入真实的 `0x00`：

```
```
00
```
```

要写入 JPEG 魔数：

```
```
FFD8FFE0
```
```

错误写法：

```
```
0x00       ← 不要加 0x 前缀0          ← 长度不是偶数GG         ← 不是合法 hex 字符
```
```

***YAK***

**4.4 ASCII 输入**

适合写入可见字符，Yakit 会按 UTF-8 编码成字节。

比如输入：

```
```
shell.php
```
```

就得到对应的 ASCII 字节序列。

**五、实战一：NullByte 截断文件名**

这是最直观的场景。文件名需要是：

```
```
shell.php[0x00].jpg
```
```

### 步骤

1.在 Web Fuzzer 的数据包里写：

```
```
Content-Disposition: form-data; name="filename"; filename="{{unquote("shell.php.jpg")}}"
```
```

2.点击折叠出来的 `Binary[...]` 卡片。

3.弹窗里看到 13 个字节，`Head: 0x7368...`。

4.选中要截断的位置，用 `HEX` 输入框写 `00`，点击应用；

+ 或者用鼠标选中某个字节，切换到 `替换` 模式，用 `00` 覆盖它。

5.点击 `提交`，标签自动更新。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72H2SRqadAPaTzpB0CAficv7dFibQsMzjAoWp7YkxYzEcMHOmhYuAGGkgOxbbfO1meEZ4qIF5RkQ99kQck6JoBUpPQwQ5ibHMRYThE/640?wx_fmt=png&from=appmsg)

6.点击发送后，点击详情，查看数据包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72HXsyvibPmSxnWYHiapMwTvfSfT6iajibhC95ib6KITNXDo5ic7ocskxYsUCmtB7FlSKt3eRibYJLNJRNCGx2iaic9hiac8bjdQja7wG6jYA/640?wx_fmt=png&from=appmsg)

> 注意：你不需要自己算 `Content-Length`，Yakit 渲染 `{{unquote(...)}}` 时会按实际字节长度自动处理。

**六、实战二：换行解析文件名**

另一个经典场景是 CVE-2017-15715，文件名按换行符切分：

```
```
shell.php[0x0a].jpg
```
```

### 步骤

假设你一开始只写了普通文件名：

```
```
Content-Disposition: form-data; name="filename"; filename="{{unquote("shell.php.jpg")}}"
```
```

1.点击 Binary 卡片，打开 Edit Binary。

2.在 Hex 视图里点击 `shell.php` 末尾那个字节，定位插入点。

3.切换到 `插入` 模式。

4.输入方式选 `HEX`，输入框里写：

```
```
0a
```
```

5.点击 `应用`，真实的换行字节就插入到了 `shell.php` 和 `.jpg` 之间。

6.点击 `提交`，标签自动更新为 `{{unquote("shell.php\x0a.jpg")}}`。

这样你就拼接出了一个包含真实 `0x0a` 字节的文件名，不需要离开 Yakit。

> 你也可以反过来：先写 `{{unquote("shell.php\x0a.jpg")}}`，然后打开 Edit Binary 检查中间那个字节是不是真的是 `0x0a`，必要时再调整。

**七、HEX 和 ASCII 到底什么时候用？**

##

|  |  |  |
| --- | --- | --- |
| 场景 | 推荐输入方式 | 例子 |
| 写入 `\x00`、`\x0a`、`\xff` 等不可见字节 | HEX | `00`、`0a`、`ff`（不要 `0x` 前缀） |
| 写入文件名、脚本字符串等可见文本 | ASCII | `shell.php`、`<?php ... ?>` |
| 写入图片/文件魔数 | HEX 或 ASCII | `FFD8FF` 或 `GIF89a` |
| 覆盖已有的一段字节 | 替换模式 + 先选中目标 + HEX/ASCII | 把选中的字节改成 `00` |
| 在指定位置前插入内容 | 插入模式 + 点击定位 + HEX/ASCII | 在 `shell.php` 后插入 `00` |
| 在末尾追加内容 | 插入模式 + 不选中任何字节 + HEX/ASCII | 追加 `.jpg` |

##

**八、对比传统方式的优势**

以前做这件事，流程是：

![](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72FVY1LibMS1AW850Fux8lzQUkMcQicXBHxgz5siayeyg3dibxPODwuE4cnIDslwKzZhVumFWewziaaQTtP1ceOnXwZeOFeO2faRWhzM/640?wx_fmt=jpeg&from=appmsg)

省去了记 Fuzztag 语法、反复发包验证这两步，出错概率低很多。

**九、总结**

Edit Binary 这次解决的核心问题是：

> 让 Web Fuzzer 里的不可见字节变得「看得见、改得了」。

对于经常要碰上传包的人来说，NullByte 截断、换行解析这些场景会顺手很多。

几个关键记忆点：

`1.unquote` 标签要用**双引号**；`hexdecode` / `base64decode`**不要引号**；

`2.unquote` / `hexdecode` / `base64decode`**无论多短都会折叠**；

3.折叠需要 `foldBinaryFuzztag={true}` + `type="http"`；

4.不可见字节用 **HEX** 输入，可见文本用 **ASCII** 输入；

5.HEX 输入**不要****`0x`****前缀**，长度必须是**偶数**；

6.默认是**替换**模式，想覆盖字节要先选中；**插入**模式要先点击定位，否则插到末尾。

演示视频

**END**

**更新记录**

Yakit v1.4.7-0618

1. YakRunner上线侧边栏AI

2. MITM和Webfuzzer可编辑上传文件不可见字符

3. 热加载模板支持分组归类

4. History右键菜单支持查看附近数据包

5. 插件检测新增复制报错功能

6. 导出插件支持自定义导出路径

7. 端口扫描新增系统保护配置项

8. 隐藏MITM系统tag展示

9. 修复模型检测暗色模式bug

10. 修复数据对比模块异常问题

Memfit AI v1.0.2-0618

1. 优化任务规划数据展示

2. 任务详情增加统计数据，可手动加载技能、工具、插件等，且自由对话任务也可查看任务详情

IRify v1.2.3-0618

1. 优化首页展示，增加数据统计

2. 优化项目管理编译历史展示

Yaklang 1.4.7-beta10

Yakit：

1. 修复了POC函数示例错误

2. yak runner中补充AI输入框

Memfit：

1. 支持强制人工评审，执行流程重构

2. 计划可脱离主会话独立评审与恢复执行

3. 支持追问能力

4. 统一会话快照事件，包含执行统计、yaklang...
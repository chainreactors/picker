---
title: Python 3.15正式发布！这6个新特性，开发者值得关注
url: https://mp.weixin.qq.com/s/d1FdFjiOkB8GrRJeGVcIeA
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:45:14.938314
---

# Python 3.15正式发布！这6个新特性，开发者值得关注

# Python 3.15正式发布！这6个新特性，开发者值得关注

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

Python预计阅读 7 分钟 · 共 2793 字

Python 3.15 正式发布！这 6 个新特性，开发者值得关注

3.15 新特性 · 开发者必读

#延迟导入#frozendict#JIT#UTF-8

READING PATH

阅读路线

7 个章节

01

延迟导入：模块不必一开始就加载

-

02

frozendict：终于有内置的不可变字典了

-

03

推导式支持解包：处理集合更加方便

-

04

性能分析工具升级：用 Tachyon 找出程序瓶颈

-

05

实验性 JIT 继续进化：性能优化有新进展

-

06

默认编码统一为 UTF-8：少一些乱码烦恼

-

07

写在最后

做 Python 开发的朋友，最近可以关注一下新版本了！

2026 年 10 月 9 日，`Python 3.15`正式发布。这次更新不仅涉及语法改进，还带来了延迟导入、不可变字典、性能分析工具升级等变化。对于经常写自动化脚本、后端服务的开发者来说，其中有些功能确实值得了解。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyqm50aq1gT1HAibY6lbcFn2qHfJiaGVpkd6Ba5HC2LjuXfr4NAF85LFekmr4REjlnmAF4OEMu7pyhyIMoDZdw7vuCHCz6WrrrCw/640?wx_fmt=png&from=appmsg)

今天不照着官方文档逐条念，我们挑出 **6 个值得关注的变化**，看看它们究竟能解决什么问题。

CHAPTER 01

**01****延迟导入：模块不必一开始就加载**LAZY IMPORT

项目越来越大，导入的模块越来越多，程序启动也可能越来越慢。

`Python 3.15`引入了显式延迟导入语法，可以把模块的实际加载推迟到真正使用时。

python

lazy import json

lazy from pathlib import Path

print("程序启动中...")

data = json.loads('{"name": "Python"}')

print(data)

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyp0LXqNb3G0byebI3eIjrqAB8X5r020mdFv3aiasQBGyJQf1IybhyH0NibhaQlKzKDefHFRhuSDvUfEUeN8lDhicudZOJRhvW1GU/640?wx_fmt=png&from=appmsg)

这里的 `json` 和 `Path` 都采用延迟导入，直到代码真正使用它们时，才触发实际加载。

**有什么用？** 对于包含大量依赖的大型应用、命令行工具和自动化脚本，如果某些模块并非每次运行都会用到，延迟导入就有机会减少启动开销。

注意

模块加载错误会延迟暴露

#测试#启动速度

模块加载错误也可能延迟到首次使用时才出现，因此不能只关注启动速度，还要做好测试。

CHAPTER 02

**02****frozendict：终于有内置的不可变字典了**FROZENDICT

Python 的 `dict` 很灵活，但也有一个问题：任何持有它的代码，都可能修改里面的数据。

python

config = {

"host": "127.0.0.1",

"port": 8080

}

config["port"] = 9000

如果配置数据不希望被修改，这种灵活性反而可能带来隐患。

Python 3.15 新增了内置类型 frozendict：

python

config = frozendict(

host="127.0.0.1",

port=8080

)

print(config["port"])  # 8080

config["port"] = 9000# TypeError

创建后，字典内容不能再被修改。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfxhaZjb6Geyia7zq84E3ogImF7tSiaqdQRF4Sgt7gyDntMClqic7ib5MvW9VLnzfev4mhLPSYZ1J17vNiaF77UXXtsbia7vbxib0PsRC4/640?wx_fmt=png&from=appmsg)

**有什么用？** 只读配置、共享数据以及需要不可变映射的场景，都可以考虑它。

注意

frozendict 不等于深层不可变

#浅层#引用

`frozendict` 并不意味着其中引用的所有对象也会自动变成不可变对象。

CHAPTER 03

**03****推导式支持解包：处理集合更加方便**UNPACKING

列表合并、数据整理是开发中的常见操作。Python 3.15 为推导式增加了解包能力，让部分集合处理逻辑可以写得更紧凑。

传统写法：

python

groups = [[1, 2], [3, 4], [5, 6]]

result = []

for group in groups:

result.extend(group)

print(result)

# [1, 2, 3, 4, 5, 6]

Python 3.15 新语法：

python

groups = [[1, 2], [3, 4], [5, 6]]

result = [\*group for group in groups]

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfxETicibicOibEoVs1JWb4HIeibXAecNFTHcSfFpao5CZNHQANMNp9hhf70V0xXOhKAL08oic32EIf1C4lO0UkaiaWmMkXjlCJvJ17Imk/640?wx_fmt=png&from=appmsg)

注意

以官方语法文档为准

#语法#合法形式

这种写法展示的是新版本推导式解包的思路。实际使用时，应以 Python 3.15 官方语法文档中的合法形式为准，不能简单把所有 `*` 解包表达式都当作有效的推导式语法。

这项改进主要面向集合构造与数据处理，让部分场景下的代码表达更加直接。

CHAPTER 04

**04****性能分析工具升级：用 Tachyon 找出程序瓶颈**PROFILING

假设你写了一个日志分析脚本，每天处理大量日志。最近脚本运行越来越慢，你怀疑是文件读取、数据清洗或统计逻辑出了问题。到底是哪一步耗时最多？与其猜，不如直接进行性能分析。

Python 3.15 新增了 `profiling` 工具包，其中的 Tachyon 采用采样方式收集程序运行时的调用栈，帮助开发者定位性能热点。

3 STEPS

Tachyon 性能分析三步

1

第一步 准备案例

新建 slow\_script.py，模拟一个存在性能瓶颈的日志统计程序

2

第二步 Tachyon 分析

用 python -m profiling.sampling 运行，生成交互式火焰图

3

第三步 优化代码

根据火焰图定位热点，优化后对比前后效果

01

准备一个存在性能问题的案例

新建 `slow_script.py`，模拟一个日志统计程序：

python

def parse\_logs():

count = 0

# 模拟大量重复计算

for i in range(3\_000\_000):

count += sum(range(20))

return count

def process\_data():

# 模拟数据处理

return sum(i \* i for i in range(500\_000))

def main():

print("开始分析日志...")

parse\_logs()

process\_data()

print("日志分析完成")

if \_\_name\_\_ == "\_\_main\_\_":

main()

这段代码故意安排了大量重复计算，用来模拟性能瓶颈。

02

使用 Tachyon 分析程序

确认当前使用的是 Python 3.15，然后执行：

python

python --version

python -m profiling.sampling run \

--mode cpu \

--flamegraph \

-o profile.html \

slow\_script.py

命令执行完成后，会生成`profile.html`交互式火焰图。

打开文件，观察调用栈中哪些函数占据较大的宽度。宽度越大，通常意味着该调用路径消耗的 CPU 时间越多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfyNicVAeAib65qgoHALuANy7Q39Y8ExuA7suVInQPruHibyib8LSTVicKMP9WP0w5WB1mfHQlLr1XdLHSuEYpNNvic7f2Jcuiaic6uNa0U/640?wx_fmt=png&from=appmsg)

03

根据分析结果优化代码

在这个案例中，parse\_logs() 反复计算 sum(range(20))，但这个结果每次都相同，完全没有必要重复计算。

可以改成：

python

def parse\_logs():

count = sum(range(20)) \* 3\_000\_000

return count

再次运行性能分析命令，对比优化前后的运行时间和火焰图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfwXby7rhiawCr0AtvD9oicKZ1NcKqncd3XNK98jzQdvvOEUvCvDj722xAwL9BXlzBoI77ft27V6pnkURca5rvSbib8N5Jq8UcSic68/640?wx_fmt=png&from=appmsg)

这个案例的核心不是让代码变快，而是展示如何找到值得优化的代码。

注意

实际项目排查不能只看 CPU

#网络#磁盘I/O#数据库

实际项目中，如果耗时来自网络等待、磁盘 I/O 或数据库查询，应结合墙钟时间模式、日志和链路监控继续排查，不能只看 CPU 分析结果。

CHAPTER 05

**05****实验性 JIT 继续进化：性能优化有新进展**JIT

JIT，也就是即时编译，可以简单理解为：在程序运行过程中，将部分代码转换成更适合处理器执行的机器码。

Python 3.15 对实验性 JIT 编译器进行了显著改进。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfyoX1XkYa2S7Vx8JIQpjkD311icicqS9hdSHsib63tib8PEeB264g1dr59icBkoRBDA6CdMXeUv5z5k1XqoclB5WPUATN4JgjShIOCQ/640?wx_fmt=png&from=appmsg)

官方公布的测试结果显示，在特定平台和测试条件下，JIT 带来了可观的性能提升。但这并不意味着所有 Python 程序都会自动变快，具体效果还取决于工作负载、平台以及构建方式。

对于普通开发者来说，不必急着为了 JIT 改写项目。先了解它的发展方向，等到目标环境和实际业务验证出收益后，再考虑是否启用。

CHAPTER 06

**06****默认编码统一为 UTF-8：少一些乱码烦恼**UTF-8

在不同操作系统之间迁移脚本时，文件编码问题一直是个容易踩的坑。

例如，程序在一台机器上读取中文 CSV 文件正常，换到另一台机器后，却可能出现乱码或解码错误。

Python 3.15 将 UTF-8 设为默认编码，能够减少默认编码不一致造成的问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfxCskcqBYZxqG2ZwhVTZnggV9piaUZgdU8T42060LCy4mC9q0KtBD8mTfKqmgkL48UNA9jGaKBeyyhyPoaUVCrNy9qdxHAbkn8k/640?wx_fmt=png&from=appmsg)

不过，实际项目中仍建议显式指定编码：

python

with open("data.txt", "r", encoding="utf-8") as f:

content = f.read()

print(content)

这样代码的意图更加明确，也更方便跨平台维护。

CHAPTER 07

**07****写在最后**CONCLUSION

整体来看，Python 3.15 的更新可以归纳为三个方向：

开发体验数据与兼容性性能与诊断

方向

三大更新方向

- **开发体验**

- **数据与兼容性**

- **性能与诊断**

特性

对应新特性

- 延迟导入、推导式解包，让部分代码更灵活

- `frozendict`、UTF-8 默认编码，改善常见开发场景

- JIT 和性能分析工具持续进化

如果你正在学习 Python，可以尝试在独立环境中体验新语法；如果项目已经运行在生产环境，建议先检查第三方库兼容性，再逐步验证升级效果。

新版本值得关注，但没有必要为了追新而盲目升级。

Python 3.15 的这些新特性中，你最想尝试哪一个？

延迟导入、frozendict、JIT 还是 UTF-8？评论区聊聊你的选择

· 点赞 ·

喜欢就点个赞吧

· 转发 ·

分享给更多朋友

· 推荐 ·

推荐给身边的人

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过
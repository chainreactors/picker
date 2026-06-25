---
title: 用 AI 挖掘 IDA Pro 任意代码执行漏洞
url: https://mp.weixin.qq.com/s/kskTQ5jSnmDAK47sVuzBkw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:05:46.432832
---

# 用 AI 挖掘 IDA Pro 任意代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PkfClzhSYicyicPWAsCfzWicXQfeYnpdl8QXAKoP0591GdWtde6o9JyFVLJKK1NRctRDQOdpEXoKDQwHPp9tSS4Kb9LX61JCiaWXTlNyiaFyfBg8/0?wx_fmt=jpeg)

# 用 AI 挖掘 IDA Pro 任意代码执行漏洞

原创

i3eg1nner
i3eg1nner

SecureNexusLab

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

IDA Pro是逆向工程领域最顶级的商业工具，正版授权价格不低，但安全圈几乎人手一份。全世界的漏洞猎人、恶意软件分析师、二进制研究员，做这行的都离不开它。它最核心的本事，是把你看不懂的机器码「反编译」成接近人类可读的伪代码，让研究员能搞清楚一段二进制到底在干什么，然后在里面找毛病。

这就是那个荒诞的地方，用来找漏洞的工具，被AI找出了漏洞。

这个Claude也不是第一次干这种事了。同一个操作者之前用它破了Radare2（开源逆向工具），又绕过了NSA的Ghidra服务器认证。操作者维护着一张清单，记录着所有被Claude搞定过的逆向工程工具，IDA Pro排在下一位。

听着就已经有点荒诞，但后面更荒诞。

**「闭源软件，怎么审」**

这次的难点比之前都大，而且难的方式很具体。

Radare2和Ghidra都是开源的，Claude可以直接读源代码。这次的目标是IDA Pro 9.3的aarch64版本，闭源，拿到手的是几百兆二进制文件，全是`.so`，没有`.dylib`，没有`.dll`。让AI直接读汇编代码效率极低，机器码和token之间本来就没有什么自然的映射关系，更别说在几百兆的编码指令里找逻辑漏洞了。

操作者给Claude接上了一个叫 `ida-mcp-rs` 的MCP服务，这是一个让Claude可以直接查询IDA自带反编译器的接口。有了这个接口，Claude可以把它想分析的任何函数发给IDA的反编译器，拿回接近C语言的伪代码，再基于伪代码做分析。不是在盲读机器码，而是在读经过反编译处理后的「人话版代码」。

操作者的第一个任务Prompt是，「分析这个文件夹里的二进制文件，找出哪个负责解析用户输入的结构体类型定义，判断编译这些类型是否可能导致代码执行。」

Claude先去审了IDA的二进制加载插件，也就是负责把各种格式的可执行文件加载进IDA的那部分代码。

什么都没找到。

操作者把它拉回来，重新定向到类型解析，说Hex-Rays最近刚推了个新的解析器，功能面很宽，仔细读。

**「CLANG\_ARGV这根线」**

负责类型解析的二进制有三个。`libida.so` 是IDA的内核层，内置了 `parse_decl*` 系列API。`idaclang.so` 是个小插件，把IDA桥接到完整的Clang库。`libclang.so` 是50MB的LLVM/Clang本体。

Claude先盯着 `idaclang.so` 看，在里面搜Clang相关的字符串，找到了一个叫 `CLANG_ARGV` 的东西。顺着交叉引用往上追，追到了 `$ idaclang` 这个netnode。

解释一下netnode是什么。IDA在分析过程中，会把反汇编结果、类型信息、注释、用户自定义的各种数据全部保存到一个专有数据库文件里，扩展名 `.i64`。Netnode是这个数据库里的键值存储结构，IDA用它保存各种元数据，包括解析器配置、编译参数等。安全研究员共享分析成果的时候，经常直接交换 `.i64` 文件，所以这个数据库天然是一个可以由第三方控制内容的输入面。

`CLANG_ARGV` 从 `$ idaclang` 这个netnode里直接读出来，没有任何过滤，直接传给Clang作为编译参数。结果就是，任何分发了精心构造的 `.i64` 文件的攻击者，都可以完全控制IDA在编译类型时传给Clang的参数列表。

Clang有一个 `-load` flag，可以加载任意的共享库。攻击者在 `.i64` 里注入 `-Xclang -load -Xclang /tmp/evil.so`，受害者打开文件并解析任意类型，共享库加载，代码执行。

逻辑上完美闭合，开始做PoC。

**「第一次失败，解析器版本的迷宫」**

Claude先试着从零构造一个 `.i64` 文件，CRC32报错，失败。操作者说换IDAPython直接设netnode的值。有效的数据库做出来了，操作者打开，然后，什么都没发生。

反馈回来一句话，「我的源代码解析器设置的是legacy。」

就这一句话，整条路废了。

然后Claude才意识到一件更复杂的事。IDA 9.2之后有三个类型解析器选项。legacy是旧的内部解析器，到现在还是默认值。old\_clang是之前那个基于Clang的解析器，对应 `idaclang.so`。clang是全新的，Hex-Rays在9.2发布说明里把它作为重要新功能单独列出，基于LibTooling和llvm-20.1.0构建，预计未来成为默认选项。

Claude一直在审的 `idaclang.so`，对应的是 `old_clang`。

那个根本没什么人在用。

操作者把它重新定向到新的 `clang` 解析器，这个实现在 `libida.so` 里，也就是IDA的内核。

这里有个比之前更好的消息，而且好处有两层。第一，新的解析器读的是同一个 `CLANG_ARGV` netnode，注入面还在。第二，因为它在内核里，攻击面实际上比 `idaclang.so` 更宽。更关键的是，配置里有一行描述，「这个设置保存在当前IDB里」，攻击者只要在 `.i64` 里把解析器强制设成 `clang`，受害者本地默认是什么都不重要，打开文件就会使用这个设置。完全不需要受害者改任何配置，没有任何预设条件。

听起来比之前更好，重新做PoC。

再次失败。

**「-load的死路」**

Claude去反编译了对应的代码路径，找到了原因。

`-load` flag确实被解析了、被存储了，但 `LoadRequestedPlugins()` 根本没有被调用。问题出在libclang的API选择上，它走的是 `ASTUnit::LoadFromCommandLine` 这条路径，而这个调用完全绕过了 `ExecuteCompilerInvocation()`。插件加载的代码就在 `ExecuteCompilerInvocation()` 里，从来就没有被执行到过。

换一种方式说，libclang在设计上就不是跑完整编译流水线的，它只跑了前端的语法分析和类型检查部分，动态库加载这种副作用根本不在它的路径上，不管你传什么 `-load`。

Claude给出结论，直接代码执行此路不通。

操作者不认可，「往编译器里注入参数，这个攻击面太大了，不能就这样放弃。」

新任务，「你能不能试试别的参数，或者对参数解析器做更深入的分析，看看支持什么参数，各有什么实际效果。」

这个转折是整个研究里最关键的节点。如果这里接受了「不可行」的结论，漏洞就到此为止了。操作者把攻击目标从「代码执行」重新定义成「任意写文件」，攻击面从插件加载一个flag扩展到了Clang整个flag空间。

**「Makefile的旁门」**

Claude开始在Clang的flag空间里系统地翻。目标不再是代码执行，而是任何能够把攻击者控制的内容写到磁盘指定路径的东西。

找到了Clang的Makefile依赖文件生成功能。

这个功能本来是给C/C++项目构建系统设计的，用来自动追踪文件依赖关系，告诉make「这个目标文件依赖哪些源文件和头文件，哪个改了就重新编译」。控制这个功能的有三个flag，`-MD` 开启依赖文件生成，`-MF <path>` 指定输出文件的路径，`-MT <target>` 控制写进文件的目标名称。正常的输出大概长这样，

```
ounter(lineoutput.o: source.c header.h
```

但 `-MT` 接受的是任意文本，包括换行符。

这是Make语法层面的合法设计，构建目标名可以包含各种字符。但在这里，「任意文本包括换行符」意味着，攻击者可以通过 `-MT` 在 `-MF` 指定的文件里写入任意内容，把那个文件变成任何东西，包括一段合法的Python脚本。

最后一块，IDA在启动时会自动从插件目录扫描并加载Python插件，这是IDA正常的扩展机制。

整条链路扣上了。

攻击者在 `CLANG_ARGV` 里注入三个flag，`-MD`、`-MF /path/to/ida/plugins/backdoor.py`、`-MT`（内容是精心构造的Python代码），把这个 `.i64` 文件发给受害者。受害者打开IDA，IDA读取数据库里的 `CLANG_ARGV`，用户触发任意类型定义的编译，IDA把这些参数传给Clang，Clang的依赖文件生成功能把Python文件写进插件目录。下次受害者启动IDA，插件目录里的文件被自动加载，代码执行。

整个攻击链的触发条件只有一个，受害者打开了精心构造的 `.i64` 文件并触发了一次类型编译。不需要受害者改任何配置，不依赖任何特定的IDA默认设置，不需要额外的漏洞配合。

Hex-Rays已经制作了PoC演示视频确认了这条链路。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PkfClzhSYicyYdGNt73lojRBLcjHYFfqakU9qBZVAHibLf3qiasUPwib1Dg2eJr6lqOw09o64XbEkib95L5giatROfhjbtw4GtIoS9s9dY4Ty6aIQ/640?wx_fmt=jpeg)

**「修复」**

Hex-Rays在IDA 9.3sp2里修了这个漏洞。

方案是给允许传入的Clang参数设一个白名单，只放过类型解析场景里真正有必要的那些，`-MD`、`-MF`、`-MT` 都不在列表里。这个思路是对的。Clang是一个完整的编译器前端，接受的flag多达数百个，大多数在类型解析这个窄场景里完全没有存在理由，严格的白名单是唯一合理的防御姿态，比任何黑名单方案都更可控。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PkfClzhSYicyicx3dWVyAk1WbAiamyChUfTCPmDpxNDHmDYZwY9icAvjEribG62s6SZ46quRfLeknv6POC0TxFTEjwzfSQhwu47dGfdPl5raaibPQ/640?wx_fmt=jpeg)

Hex-Rays为这个漏洞支付了赏金。

**「工具配置对比」**

研究结束后，操作者做了一件很有价值的额外测试，把同一个任务（找到、分析、利用这个漏洞）在多种工具配置下跑了一遍，用11项加权评分指标对比完整度。

测试的配置包括 `ida-mcp-rs`、Binja MCP、`idalib_mcp` 和多种Skill配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PkfClzhSYicyr8OqXurVtFyDCBB4eAwrqRbe6RDxFbQaPUYsgWJHNCbxPs6DicN1NF3lz2y8YGLQNscicpUjP8oeKGzELhaIj5FSxLOanUu5mE/640?wx_fmt=png&from=appmsg)

整体结论是MCP配置好于Skill配置，平均完整度90.0% vs 81.8%。在MCP组内，Binja MCP和 `idalib_mcp` 的准确率最高，Opus版本都跑到了97.7%，是所有配置里最高的。但 `ida-mcp-rs` 的性价比最好，Opus版本平均59K tokens、16分钟、完整度95.4%，差不多是其他MCP配置一半的token消耗，结果几乎相当。Opus整体好于Sonnet，91.8% vs 79.7%，差距在需要多步推理的难题上更明显。

这些数字只反映这一个特定漏洞，不保证在别的目标上同样成立。但如果你在考虑搭AI驱动的二进制审计流水线，这个对比提供了一个有据可查的基准起点。

这是一个AI真的在做漏洞挖掘，跟反编译器直接对话，在Clang的flag空间里系统枚举可能性，在连续两次死路里做方向判断，在操作者的引导下一步一步找到了一个真实的、有赏金价值的漏洞。

操作者负责的是目标设定、工具接入、和每次进死路时的方向修正，尤其是「-load失败」那个节点的坚持，「往编译器里注入参数，这个攻击面太大了，不能就这样放弃」——这句话把攻击面从一个flag扩展到了整个编译器的设计空间。Claude负责的是反编译器输出的阅读、代码调用路径的追踪、以及在那个扩展后的空间里做完整的flag枚举。两件事缺一不可。

![](https://mmbiz.qpic.cn/mmbiz_png/PkfClzhSYicxlqVTiaDPibMxtDLib6yU3XUN4Fpf9pgxnuI1uiaGIj7PH7KBxCQcOYwVt4obvL9JtISeGfhBKCrH7stFEWkCaQVT6icK9em2xQj1A/640?wx_fmt=png)

这个分工模型出现在「需要深度领域直觉」的安全研究里，让我的AI焦虑有所缓解。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkLGDzh5WQ5kuYab29V2PteuUrCj2HeRIHibmjQEK7plD7iccC97duj94oGugfkHdQdxcaXtB7w5icmg/0?wx_fmt=png)

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
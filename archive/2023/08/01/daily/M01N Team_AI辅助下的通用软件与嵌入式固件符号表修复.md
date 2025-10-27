---
title: AI辅助下的通用软件与嵌入式固件符号表修复
url: https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247491971&idx=1&sn=d84e499a6707b3c58e203fafdec0575b&chksm=c1842192f6f3a884efe7c846b1b535ca9b390d9e35c1aeab86fef20ea0e111638bf757f537e1&scene=58&subscene=0#rd
source: M01N Team
date: 2023-08-01
fetch_date: 2025-10-06T17:02:11.957271
---

# AI辅助下的通用软件与嵌入式固件符号表修复

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwatVBcVQjXP97yMAImJtIvlRzV7YkMlqoQ2J3lRXChINUqOwtC5CGicTslZPHeXtkic5ON3ABLBghPA/0?wx_fmt=jpeg)

# AI辅助下的通用软件与嵌入式固件符号表修复

原创

格物实验室

M01N Team

**01 概述**

Claude是一个支持中文、暂时免费、先到先得，不用排队、人人都能上网使用的类ChatGPT产品。之前Claude 100k还在测试阶段，需要申请api使用权限，非常稀有。最近官网升级到了2.0,向大众开放了100K的功能。网站的地址如下：https://claude.ai

Claude 100k的强大之处，直接摆脱了Chatgpt 4k到32k的限制，大概一次可以输入75000个单词或者50000个汉字。

目前上传的文档格式支持很多。几乎所有的文本文档都支持。包括:pdf,doc,docx,rtf,epub,odt,odp,pptx,txt,py,ipynb,js,jsx,html,css,php,c,cpp,cxx,h,hpp,rs,r,rmd,swift,go,rb,kt,kts,ts,tsx,m,scala,rs,dart,lua,pl,pm,t,sh,bash,zsh,csv,log,ini,yaml,yml,toml,lua,sql,bat,md,coffee等,未来还有增加的趋势。网站界面如下:

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZZgQbTeQly6SkOXmWUzD3ibiaLYKJI05cmSEdFJ2jlB5lQ3oVLstuca3UnXy7iatqibR09sPsIQxnIQg/640?wx_fmt=png)

**02 嵌入式固件或通用软件的符号表修复思路**

近几天对嵌入式系统的固件进行代码审计，发现**嵌入式系统固件的符号表恢复问题在AI的帮助下可以得到完美的解决**，并摸索出一套比较完美的解决方案。

主要操作方法如下:

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZZgQbTeQly6SkOXmWUzD3ibGxl2z3vaGK86QXkJEce78VuKbvZvb2ia6G5rqJrIPLChoeJjQdcFBeA/640?wx_fmt=png)

下图是一个STM32的固件，没有符号表的情况下，函数名是以:sub\_xxx类型显示的，不容易判定函数对应的功能。IDA PRO函数的画风如下：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZZgQbTeQly6SkOXmWUzD3ibAsjAal44oHeeFBCYWAZxUmpeSdAKDl7VlEd4QTxKP8gVLed1TQ7WjA/640?wx_fmt=png)

**2.1 导出反编译的伪C代码**

因为 Claude 可以对100K左右的代码和文档进行处理，因此可以在IDA PRO的汇编界面中，使用Ctrl +F5快捷键，导出固件整体反编译后的伪C代码。这里保存文件为：“stm32f103RCT6.01.c”。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZZgQbTeQly6SkOXmWUzD3ibmMlbIqrw4VSmPyDZv2yRuIoDV9UTnZwH8cPTYeHib9iaL304lW4WjnAA/640?wx_fmt=png)

**2.2 对伪C代码进行分割**

研究用的例子程序文件大小约为1MB，很明显超过100KB了，因此需要把C语言伪代码文件拆分为120K左右大小的文本。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZZgQbTeQly6SkOXmWUzD3ibWLDWyJgzFoTlOcyjwia43FEjGAweNEwAk9ynXAeUoakn7lJrnjqzuPQ/640?wx_fmt=png)

注意：分割文件时，完整的函数需要放在同一个文件里，不能分开存放。

当检测到大于120K时，如果当前文件的函数还没有结束，则找到上个函数的结束标记。

用程序实现的简化的C语言函数判断方法:"{"和"}"都在一行的开始处，没有空格，可认为是一个函数的开始或结尾。建议以一行代码的开始紧接着"}"，中间没有空格，则判断为一个函数的结束。

```
正则表达式规则为: ^}$
```

**2.3 上传代码，AI对函数重命名**

为了格式化输出，给了AI一个可用的例子，同时也交代了固件的芯片类型和已知的背景，使用的提示词如下:

```
下面是一个stm32f103RCT6固件二进制文件的伪C代码，请你给函数重新命名。例如:原函数sub_AAD8()重命名为：set_motor_speed()。则输出如下:0xAAD8,set_motor_speed一个函数输出一行后就换行。注意:只对sub_XXX类型的函数进行重命名，不要和已有命名冲突。也不用你进行任何解释。
```

上传某部分代码后(当然，如果输出的伪代码小于150K,可以一次性上传完毕)，AI按照指定的要求输出了重新命名后的函数名称。场景如下：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZZgQbTeQly6SkOXmWUzD3ibqLqVrkgy2xicnDxOQXELmfL4VPaOZa4lJTayPZKRROXSib9OvmvlOrBw/640?wx_fmt=png)

整理和记录输出的结果，保存为config.txt文件，config.txt文件例子如下:

```
0x8000138, system_init0x800014A, reverse_bits0x80003BC, check_write_protect0x80003C8, module_init0x80004CE, validate_device_id0x800052A, report_device_id……
```

**2.4 IDA执行脚本修复函数名**

在IDA PRO软件中执行python脚本（File->Script file）, 即可对函数批量重命名。

下面给出可用的python脚本。

```
import idaapiimport idc
def resolve_name_conflict(name):    counter = 1    while idc.get_name_ea_simple(name) != idaapi.BADADDR:        name += "_" + str(counter)        counter += 1    return name
def rename_functions():    with open("config_mini.txt", "r") as f:        for line in f:            addr, name = [item.strip() for item in line.split(',')]            addr = int(addr, 16)            print("info:"+hex(addr)+" name:"+name)            if idc.get_segm_name(addr) is None:                print("Invalid address: " + hex(addr))                continue
            old_name = idc.get_func_name(addr)            if old_name is None or old_name == '':  # 地址上没有函数                print("No function at address: " + hex(addr))            else:                print("address:" + hex(addr)+" old_name:"+old_name)                                if old_name.startswith("sub_"):                    idaapi.del_func(addr)                    idaapi.add_func(addr)                    #new_name = "A" + resolve_name_conflict(name)                     new_name = resolve_name_conflict(name)                    idc.set_name(addr, new_name, idc.SN_CHECK)                    idc.set_func_cmt(addr, "public", False)
                    print("Rename function at {} from {} to {}.".format(hex(addr), old_name, new_name))print(f"------ 函数改名功能全部执行完毕! ------")
if __name__ == "__main__":    print(f"------  函数改名功能开始执行!  -----")    rename_functions()
```

函数重命名后效果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZZgQbTeQly6SkOXmWUzD3iby6YZ8I4vnaQVHiafFnVz3hRASbibY3Hpjg4ErsYyJDyFjAc0W7NSktbQ/640?wx_fmt=png)

代码的可读性是不是瞬间变强了？

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZZgQbTeQly6SkOXmWUzD3ibc1e6FibqwKQhXicf1OWpPqQ8CtINdC1d5lpWticv7iasbRxADmB9QTWy3A/640?wx_fmt=png)

再也不用担心提取出来的固件没有符号表！

当然，普通程序逆向过程中也可以用这种思路来恢复函数名。甚至给出完整和详细的注释，帮助理解程序的编写思路。

**06 总结**

ChatGPT和Claude这类大模型AI系统在网络安全领域带来的创新和影响总结如下:

1. **提高安全研究和审计效率：**大模型AI可快速理解、总结复杂的代码和文档,辅助安全研究人员发现系统漏洞也可以快速生成漏洞检测和利用代码,提高工作效率。
2. **降低安全审计门槛：**依靠大模型AI,不需要高深的安全知识也能进行安全审计和测试,降低了从业门槛。这也意味着攻击成本下降,需要提高防御力度。
3. **强化系统设计：**大模型AI可以辅助设计更安全、可靠的系统,也可以通过模拟攻击增强系统抗攻击能力。
4. **生成针对性漏洞利用代码：**大模型AI可以根据系统情况快速生成针对性漏洞利用代码,对系统进行安全性评估。
5. **带来更大安全风险：**AI也可能被利用生成恶意代码、帮助社交工程攻击,进一步加剧网络安全形势,需要加强AI伦理和安全。

总体来说,合理使用大模型AI将推动网络安全技术发展,但也需要注意潜在风险,实现安全与发展的平衡。

**注：应用Claude可能存在数据泄露风险，使用者在应用时应注意相关风险，谨慎处理敏感数据。**

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZZgQbTeQly6SkOXmWUzD3ibxbRDqsLEYK41BbWamtY1NyokR5iaMpOCw6pcY7mZDCPGxRLib11eQ20A/640?wx_fmt=png)

**绿盟科技格物实验室**专注于工业互联网、物联网、车联网三大业务场景的安全研究。致力于以场景为导向，智能设备为中心的漏洞挖掘、研究与安全分析。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwZZgQbTeQly6SkOXmWUzD3ibjB6RbKYlDla1txOicKOibTUqdRM3QWtV3yOQWTfbia6qNIvYEmt7p5kgQ/640?wx_fmt=jpeg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwZZgQbTeQly6SkOXmWUzD3ibtjqPUv4xF0005cNjNsY92OMuEaFTgbbiaP8WxnGdcGNLzrjnmBW9ylw/640?wx_fmt=png)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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
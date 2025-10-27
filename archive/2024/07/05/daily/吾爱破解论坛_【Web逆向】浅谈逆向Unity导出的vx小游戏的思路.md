---
title: 【Web逆向】浅谈逆向Unity导出的vx小游戏的思路
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651140819&idx=1&sn=56c63798c4dd6827816fdbb683a770e7&chksm=bd50a2878a272b918042530d4346275e9cb8703c53bb2e207d4b3447354486b3d6279f50b7db&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2024-07-05
fetch_date: 2025-10-06T17:43:40.104744
---

# 【Web逆向】浅谈逆向Unity导出的vx小游戏的思路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRyicBFEEUtDDKx2Y9Ecgb8iaAFtVX9QKiaUBptIIib6K6LcibxhSqLSaIZoA/0?wx_fmt=jpeg)

# 【Web逆向】浅谈逆向Unity导出的vx小游戏的思路

原创

吾爱pojie

吾爱破解论坛

**作者****论****坛账号：小沫子**

# 本文章仅用于学习交流，请勿用于非法用途

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRqcyOKia5s36IrKHFCOA0dGU0v6CicQuj2xD3Wwfn4ZHGmnibIQxicpkr6g/640?wx_fmt=png&from=appmsg)

# 浅谈逆向Unity导出的vx小游戏的思路

* 用到的工具比较多，我把全部链接都放文末

> 背景：
> 刷抖音时突然蹦出个广告，还不小心点进去了
> 就试玩了一下，发现还挺有趣的，嗯
> 可是玩了一小会后发现打不过了，还得充钱才能变得更强？？？
> 于是直接忍不了了 直接开机，上号!!!

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRN9QgZIwu0sNicQ9qOOzCC5zZsYrbWjNf9iaTG5y4NCBxgyEVAOS2AJFg/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRCZzpylDCX5ib2bNUW83siaparrcv8hAuIibbQvyYeZicobAtqWLzMXeLbA/640?wx_fmt=png&from=appmsg)

## 初步分析小游戏

* 打开对应的`wxapkg`目录
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlREHszjRRAAbOObNP2QsRslQoVRyGhemOGToWFyo68PboTrYbWAL4Kqg/640?wx_fmt=png&from=appmsg)
* 解包

  ```
   复制代码 隐藏代码
  unveilr wx -f  "D:\WeChat Files\WeChat Files\Applet\wxxxxxxx\34"
  ```
* 到这一步可以确定是`unity`项目转成的小游戏了
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRIp3D5IC5KhWDbUPhWAzVIGUFA1111wicsRdWCvP3L7gic0vagibMqbAUg/640?wx_fmt=png&from=appmsg)
* 当然你通过解包出来的目录也是可以看出来的
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRw14Bpuqa8DelibYgibv4j4MDR5aS7TCQwMOOH2KTgrn2LTcFmr9iaGO4g/640?wx_fmt=png&from=appmsg)
* 稍微翻了下代码，可以确定小游戏逻辑都在 `wasmcode` 和 `wasmcode1`
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlR1QlDMrsRbEI691YhJ6Y1mswcZC3EeJEibqIYzUGWdMIYNrgy0HSfInQ/640?wx_fmt=png&from=appmsg)
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRWyiaxxYMyOujr6tY54icQN0hZqB3nnvEUyGQzibWHE5dibUzFOxE2KkLyQ/640?wx_fmt=png&from=appmsg)

## 初步分析unity相关文件

* 可以看到这里都是 br 为后缀，这是使用brotli压缩的文件
* 使用`brotli.exe`解压缩
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRlbciaDhL5F8Lv2CDNVUcUh6wYicibe5AH1gicibSKeMQwNcGHPfPdIqCmIw/640?wx_fmt=png&from=appmsg)
* 另一个文件夹同理
* 这样我们就得到了wasm文件了
* 这里可以直接拖进 `ida` 或者 `Ghidra`
* 我这里使用 `Ghidra`，因为 ida 的 wasm 插件好像有点问题
* 怎么安装wasm插件这里我就不赘述了
* 这里我把解包得到的wasm改个名：

  ```
   复制代码 隐藏代码
  xxx.code.import.unityweb.wasm -> import.wasm
  xxx.code.unityweb.wasm -> main.wasm
  wasmcode1/xxx.code.unityweb.wasm -> sub.wasm
  ```
* 然后一并拖入 `Ghidra`
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRfkVkD66F9BgqdW8xTvFRx5GdwwoxE63ibyq3qAmDWMTfqVhFo7q14mg/640?wx_fmt=png&from=appmsg)
* 等他分析好（*这里可能要一些时间*），出现一堆 jxxx 的函数，这根本没法看啊
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRgg9V7sjCNuw34uTMMP0kggxbRwhHwCWVCDuibeTXBM2tEb2YezxAxyQ/640?wx_fmt=png&from=appmsg)
* 接下来尝试恢复wasm的符号信息

## 尝试恢复wasm的符号信息

* 一般现在的unity都是用 `IL2cpp`导出了，`Mono` 估计很少用了吧
* `Il2CppDumper` 能将使用 `IL2cpp`打包的文件还原出 `script.json`，这里面存着符号信息
* 所以我们直接使用 `Il2CppDumper` 尝试导出

  ```
   复制代码 隐藏代码
  Il2CppDumper.exe <executable-file> <global-metadata> <output-directory>
  ```
* `Il2CppDumper` 需要 `global-metadata.dat` 文件
* 那这个文件哪里找呢？小游戏的`wxapkg`包内没有
* 那应该是远程下载的，只能是找缓存路径了
* 经过研究，发现可疑文件
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRiaO1rhaCCykHj77nEfibJC4aKqNGcebhbuDXwx3zLNaKtbuMWZddwHvA/640?wx_fmt=png&from=appmsg)
* 这又是个二进制文件，需要解析出来
* 这里使用 `unityweb` 将他导出来
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlR48XGe9LmokPh3SjEa1Sia3XmyK9C6kLicXhnnu3mCcjapnC4lygic4iaug/640?wx_fmt=png&from=appmsg)
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRqVbHoZlav9BZptTyWElI6lTfvqCxw6calzlH76q56LVSStgEv3xanA/640?wx_fmt=png&from=appmsg)
* 有了 `global-metadata.dat`就能导出`script.json` 等文件了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRH5UZxRhdpZ5lkW5aAodZTBHdxUWPnajb7MhYursbC8GYqicPn8GV3UQ/640?wx_fmt=png&from=appmsg)

* 然后怎么恢复到 `Ghidra` 可以看下面这篇文章，讲的很好
* https://www.cnblogs.com/algonote/p/15596459.html
  但是
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZKtt2RBibtkN5YCW22Pl5RlRRH4VVbRnkIwFWlVRY0SKvn8Tic5N1icPiaRqIupDaaFGoettDy6VXekcg/640?wx_fmt=png&from=appmsg)
* 这里并不太适合导出成vx小游戏的项目
* 这里需要魔改 `ghidra_wasm.py`
* 经过分析，问题出在，他的动态调用的偏移是存在 `import.wasm` 里面的
* 所以我们先把它的偏移转换出来
* 这里我直接贴我的脚本

```
 复制代码 隐藏代码
// restore.js
const fs = require('fs')
const http = require('http')

const Scripts = JSON.parse(fs.readFileSync('./script.json', 'utf8'))
const splitWasmBytes = fs.readFileSync('./import.wasm')

async function main() {
  const {instance} = await WebAssembly.instantiate(splitWasmBytes);
  const getRedirIndex = a => instance.exports['wasm_split.__wasm_split_getRedirIndex'](a) & 268435455
  Scripts.ScriptMethod.forEach(item => {
    item.FuntionName = `j${getRedirIndex(item.Address)}`
  })
  fs.writeFileSync('./script2.json', JSON.stringify(Scripts), 'utf8')
}

main()
```

* 我先把对应的偏移函数名写到 `script2.json`
* 然后魔改  `ghidra_wasm.py`

```
 复制代码 隐藏代码
# -*- coding: utf-8 -*-

import json
import re

currentProgram = getCurrentProgram()
symbolTable = currentProgram.getSymbolTable()
functionManager = currentProgram.getFunctionManager()
USER_DEFINED = ghidra.program.model.symbol.SourceType.USER_DEFINED
progspace = currentProgram.addressFactory.getAddressSpace("ram")
scripts_json_path = askFile("script2.json from Il2cppdumper", "Open").absolutePath
fd = open(scripts_json_path, 'rb')
Scripts = json.loads(fd.read().decode('utf8'))
fd.close()

processFields = [
    "ScriptMethod",
    "ScriptString",
    "ScriptMetadata",
    "ScriptMetadataMethod",
    "Addresses",
]

def extract_parameters(signature):
    # 匹配函数签名中的参数部分
    params_match = re.search(r'\((.*?)\)', signature)
    if not params_match:
        return {"types": [], "labels": [], "len": 0}
    # 提取参数部分的内容
    params_str = params_match.group(1)
    # 分割参数部分的内容
    params = params_str.split(',')
    # 分离参数类型和参数名
    types = []
    labels = []
    name_counter = {}
    for param in params:
        param = param.strip()
        # 查找最后一个空格以分隔类型和名称
        last_space_index = param.rfind(' ')
        if last_space_index != -1:
            types.append(param[:last_space_index].strip())
            label = param[last_space_index + 1:].strip()
            if label in name_counter:
                name_counter[label] += 1
                new_label = label + str(name_counter[label])
                labels.append(new_label)
            else:
                name_counter[label] = 1
                labels.append(label)

    return {"types": types, "labels": labels, "len": len(labels)}

def get_addr(addr):
    return progspace.getAddress(addr)

def set_name(addr, name):
    name = name.replace(' ', '-')
    createLabel(addr, name, True, USER_DEFINED)

def restore_params(func, signature):
    params = extract_parameters(signature)
    length = params['len']
    if length != func.getParameterCount():
        # print 'Warning: Mismatch function signature: ' + signature
        return
    parameters = func.getParameters()
    for index in xrange(length):
        p = parameters[index]
        # print length, params['labels']
        label = params['labels'][index]
        p.setName(label, USER_DEFINED)

if "ScriptMethod" in Scripts and "ScriptMethod" in processFields:
    scriptMethods = Scripts["ScriptMethod"]
    monitor.initialize(len(scriptMethods))
    monitor.setMessage("Methods")
    for scriptMethod in scriptMethods:
        monitor.incrementProgress(1)
        addr = scriptMethod["Address"]
        name = scriptMethod["Name"]
        fn_name = scriptMethod['FuntionName']
        signature = scriptMethod['Signature']
        for symbol in symbolTable.getSymbols(fn_name):
            addr = symbol.getAddress()
            # 表示已经改过了
            if getPlateComment(addr): continue
            set_name(addr, name)
            setPlateComment(addr, '\n'.join([str(addr), fn_name, name, signature]))
            restore_params(functionManager.getFunctionAt(addr), signature)

if "Sc...
---
title: TRAE+ghidra辅助逆向
url: https://mp.weixin.qq.com/s/N21EXM0NSleatF4Yt37GZQ
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:28:30.273698
---

# TRAE+ghidra辅助逆向

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6nhGiavBDP4ZPM15cXa7qSUMMpUkm7gZmZ8OPA58zArOdpYRLc3hHyrZf5TXdZWibUsMibjLmqnicZprVztObMLe6rZIOSpsZC1MwTVdEku9MC4/0?wx_fmt=jpeg)

# TRAE+ghidra辅助逆向

原创

李北辰
李北辰

SPEEDCoding

![]()

在小说阅读器中沉浸阅读

TRAE是一款字节跳动推出的AI集成编程工具，内置了多个大模型，可以设置MCP连接逆向工具辅助逆向过程。

1.ghidra安装

https://github.com/NationalSecurityAgency/ghidra

    直接从Github上下载对应版本的压缩包，解压即可使用。

    这里我使用的是ghidra12.0.3版本。

2.ghidra mcp安装

https://github.com/bethington/ghidra-mcp

    原始的ghidraMCP目前还没有支持ghidra12.0.3，这里我用的是其他人fork出来的支持版本。

    下载对应ghidra版本的release中的文件：bridge\_mcp\_ghidra.py，ghidraMCP-4.3.0.zip和requrements.txt

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aa5YcOKRrtAwYXp3DjD1NzrxibhMKC2oHN52K4qGhzVLNQmcUUiaJPVnJn4VbuWuBjclP2zxuYeiblDKb0DIaf3bnDuhAjicLkhDc/640?wx_fmt=png&from=appmsg)

    首先打开ghidra，点击file->Install Extensions，点击+号选择ghidraMCP-4.3.0.zip这个压缩文件然后确定，根据提示重启ghidra。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4Yo0tIiagSib1gHS9J8Osy1fOf5NsZX23icA98QDia1n5Nst8XZWjLiaAxr8icyc7noz94gIqWgWTXl0FZcxibY1E3n09AcCMV2NyrW8w/640?wx_fmt=png&from=appmsg)

    重启ghidra后点击file->Configure，勾选ghidramcp的插件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZI0s1r35Osy9lblraPJ6Xw7rV71csv7asIUN10SqzeDEiavqeSSRibyZa4cws3KvaFbdZU52RCt6D7V6VbXkFNFYB4YXeQ5oBNQ/640?wx_fmt=png&from=appmsg)

    然后点击tools菜单栏，就可以看到GhidraMCP的选项，点击Server Status即可查看对应服务开启状态，该插件默认是8089端口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aibWrNxP67M6fFzYVxdOvMLhOw3whIDlFdFwp8VV0hgcfic3vJQt6cBCib6ZO2UnBblzSQ1lIszY86U2yibga98T4KsZhKE8Cpnia4/640?wx_fmt=png&from=appmsg)

 3.TRAE配置

     在刚才下载requirements.txt文件的路径下打开命令行，输入

```
pip install -r requirements.txt
```

    即可下载所需要的python包（python版本大于等于3.8）

    打开TRAE，随便选择一个工作区文件夹，然后点击AI对话栏里面的MCP设置，点击手动添加，输入以下json：

```
{  "mcpServers": {    "ghidra": {      "command": "python",      "args": [        "E:\\MyProject\\ghidraMCP\\bridge_mcp_ghidra.py"      ]    }  }}
```

记得把args替换为自己bridge\_mcp\_ghidra.py的路径，点击保存即可。

4.使用

通过以上操作即可成功配置好TRAE的MCP与ghidra的MCP服务连接，来实现AI逆向分析的效果，随便打开一个ctf题目。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4bYM9hcq80SmG62DgrjPyMO7WhUYg6phNfB41vMw8Sm6L4tbNd9DwQia4ibNFG5rQF7e3hiafQibAp0C8MLvWlzjV09soLkgEKq2gU/640?wx_fmt=png&from=appmsg)

然后在TRAE里面告诉AI待分析函数的入口点（比如这个题目的主函数入口点位于0x004011b0）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZEN5ppgEROIPcaHQW2FNlwaCy1e5QFwYoX4qW4DoKNfvvYdcp0KzO9RYI89TaDLYY6YDcEIKufuNdDrOYiaxl4tOxweVESFCz4/640?wx_fmt=png&from=appmsg)

然后查看分析结果

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4ZYjzeicWM2KgRicicxqLQLxPcIO1bsaojqMic0qicOu4YLMSMby27EmeWwOLnVfZHu1LlFTyBZwa4PLrMxBcYoV1Nz20RWRUw3oo2E/640?wx_fmt=png&from=appmsg)

成功找到核心校验函数0x004010f0

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4Y8voiatFxib8AhnIDW3OHuLMZaEoWt4FQ5wUc7SEibFIcPVYoCK0zNKGcCJickMnu1lkgvA8Td9ufJgjnHUl6yzSZCVGOJrJ0hOxo/640?wx_fmt=png&from=appmsg)

然后是flag的显示函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ae6vibmrIyiaGayUQicuH5LkO5WsxPLvhmCzApLx4KuMAo9wSSWCkaVc469NdLpiazm0L7hmLmL6Gw7DbWqZDBx0WX4ltXDYD1p8c/640?wx_fmt=png&from=appmsg)

这是AI分析的flag生成机制

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4ZnuMof5BFYrfeMaQKxu3VFiajsktuS6tcicJHk2d0soaic253Wtm0Ed2cvFOq1hF9rLaicRgkOvK0eAhKXY6Pj9jcLCdhlsvIYzPI/640?wx_fmt=png&from=appmsg)

根据以上信息结合人工逆向分析，即可制作出解题脚本。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ubxw8wJEYdluKbaN4LDwroa6C5W8flqTtNkiaZBpt9ibcVXJTlDmAHJHcR5TBR7AREPYETB3XUJF6v692P7GaD5A/0?wx_fmt=png)

SPEEDCoding

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ubxw8wJEYdluKbaN4LDwroa6C5W8flqTtNkiaZBpt9ibcVXJTlDmAHJHcR5TBR7AREPYETB3XUJF6v692P7GaD5A/0?wx_fmt=png)

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
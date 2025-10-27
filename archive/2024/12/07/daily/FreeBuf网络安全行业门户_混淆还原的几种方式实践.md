---
title: 混淆还原的几种方式实践
url: https://www.freebuf.com/articles/mobile/417063.html
source: FreeBuf网络安全行业门户
date: 2024-12-07
fetch_date: 2025-10-06T19:39:27.570856
---

# 混淆还原的几种方式实践

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

混淆还原的几种方式实践

* ![]()
* 关注

* [移动安全](https://www.freebuf.com/articles/mobile)

混淆还原的几种方式实践

2024-12-06 14:55:36

所属地 北京

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

下面都是使用goron的混淆进行符号执行以及模拟执行处理的结果

# 一、控制流平坦化

还原前
![image](https://image.3001.net/images/20241206/1733466950_67529b46739bd7254126d.png!small)

还原后
![image](https://image.3001.net/images/20241206/1733466963_67529b53001d0e0ae908e.png!small)

符号执行和ollvm还原思路相同：
找序言块、真实块、ret块、分发器；在deflate，不同的是需要续住寄存器的值来精准找到下一真实块
![image](https://image.3001.net/images/20241206/1733467013_67529b8586ab58fcec8df.png!small)

发现赋值在序言块
![image](https://image.3001.net/images/20241206/1733467029_67529b95c715e44c516b7.png!small)

思路
在执行真实块之前对x29偏移出进行初始化赋值或者直接将序言块寄存器状态续到真实块对代码进行修改，结合<https://github.com/cq674350529/deflat>的解混淆修改即可简单实现

# 二、间接跳转还原

分析间接跳转如下，通过手动计算跳转地址（这里是模拟执行获取跳转地址）再根据条件判断将br指令进行替换即可手动还原
![image](https://image.3001.net/images/20241206/1733467056_67529bb08829d7420712c.png!small)
替换指令为br指令以及前一条指令，根据条件指令替换为ture和false的分支跳转
![image](https://image.3001.net/images/20241206/1733467069_67529bbd743e315870315.png!small)

# 三、混淆全开

先处理间接跳转，通过汇编代码特征找到判断分支csel的两个寄存器值并获取条件指令，条件true和false的值，通过条件获取ldr的两个值，add固定值，然后替换br和上一条指令：b+条件指令true的地址，bfalse地址，找找前人造的轮子<https://bbs.kanxue.com/thread-277086.htm>进行修改即可

```
while (!finish && !instructions.empty())
                {
                    instructions.pop();
                    ins = instructions.peek().getIns();
                    if(ins.getMnemonic().toLowerCase(Locale.ROOT).equals("add"))
                    {
                        String[] split = ins.getOpStr().split(",");
                        if(split.length == 4)
                        {
                            //split[0].toLowerCase(Locale.ROOT).trim().equals("x12") &&
                            if(split[3].toLowerCase(Locale.ROOT).trim().equals("sxtw"))
                            {
                                String reg = split[2].trim().toLowerCase(Locale.ROOT);
                                base = getRegValue(reg,instructions.peek().getRegs()).longValue();
                                addinstaddr = instructions.peek().getAddr() - module.base;
                            }
//                            else {
//                                break;
//                            }
                        }
//                        else
//                        {
//                            break;
//                        }
                    }

                    if(ins.getMnemonic().toLowerCase(Locale.ROOT).equals("ldr"))
                    {
                        String[] sp = ins.getOpStr().toLowerCase().split(",");
                        if(sp.length == 4)
                        {
                            //sp[0].trim().toLowerCase(Locale.ROOT).equals("x12") &&
                            if(sp[3].trim().toLowerCase(Locale.ROOT).equals("uxtw #3]"))
                            {
                                String reg = sp[1].toLowerCase(Locale.ROOT).trim().substring(1);
                                listoffset = getRegValue(reg,instructions.peek().getRegs()).longValue()-module.base;
                                ldaaddr =  instructions.peek().getAddr()- module.base;
                            }
                        }
                    }

                    if(ins.getMnemonic().trim().toLowerCase(Locale.ROOT).equals("csel") || ins.getMnemonic().trim().toLowerCase(Locale.ROOT).equals("csinc"))
                    {
                        String[] sp = ins.getOpStr().toLowerCase(Locale.ROOT).split(",");
                        if(sp.length == 4)
                        {
                            cond = sp[3].trim();
                            if(sp[0].trim().equals("w10")&& !sp[2].trim().equals("wzr"))
                            {
                                String reg1 = sp[1].trim();
                                String reg2 = sp[2].trim();
                                cond1 = getRegValue(reg1,instructions.peek().getRegs()).longValue();
                                cond2 = getRegValue(reg2,instructions.peek().getRegs()).longValue();
                                selectaddr = instructions.peek().getAddr() - module.base;
                            }
                            if(sp[0].trim().equals("w10")&& sp[2].trim().equals("wzr"))
                            {
                                String reg1 = sp[1].trim();

                                cond1 = getRegValue(reg1,instructions.peek().getRegs()).longValue();
                                cond2 = 1;
                                selectaddr = instructions.peek().getAddr() - module.base;
                            }
                        }
                    }

                    if(ins.getMnemonic().trim().toLowerCase(Locale.ROOT).equals("subs") && ins.getOpStr().trim().toLowerCase(Locale.ROOT).equals("w8, w9, w8"))
                    {
                        if(base == -1 || listoffset == -1 || cond1 == -1 || cond2 == -1 || cond.equals("") || addinstaddr == -1 || ldaaddr == -1 || selectaddr == -1)
                        {
                            break;
                        }
                        else
                        {
                            long offset1 = base + readInt64(emulator.getBackend(), module.base+listoffset+cond1*8) - module.base;
                            long offset2 = base + readInt64(emulator.getBackend(),module.base+listoffset+cond2*8) - module.base;
                            if( brinsaddr - addinstaddr != 4)
                            {
                                System.out.println("add ins and br ins gap more than 4 size,may make mistake");
                            }
                            String condBr = "b"+cond.toLowerCase(Locale.ROOT) + " 0x"+ Integer.toHexString((int) (offset1 - addinstaddr));
                            String br = "b 0x" + Integer.toHexString((int)(offset2 - brinsaddr));
```

还原前不能f5：
![image](https://image.3001.net/images/20241206/1733467290_67529c9a3795af7530a61.png!small)
还原后还存在平坦化：
![image](https://image.3001.net/images/20241206/1733467302_67529ca6216f3d8f04c33.png!small)
获取执行流
![image](https://image.3001.net/images/20241206/1733467331_67529cc35c71f5cd8010f.png!small)
再根据执行流patch之后即可还原
![image](https://image.3001.net/images/20241206/1733467352_67529cd80bc7dc4a83101.png!small)

# 四、总结

符号执行在处理类似ollvm每个块都已经初始化好的比较好处理，模拟执行处理复杂运算的跳转好用，发现都得结合手动还原，工具只是代替手动部分的批量实现，所以本质还是手动还原的结果；或许ai训练总结算式自动编写d810的配置可能效果更要好一些

参考：
<https://github.com/cq674350529/deflat>
<https://bbs.kanxue.com/thread-277086.htm>
<https://github.com/amimo/goron>

# Android # AI安全

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](...
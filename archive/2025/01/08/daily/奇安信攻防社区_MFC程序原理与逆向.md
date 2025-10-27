---
title: MFC程序原理与逆向
url: https://forum.butian.net/share/3990
source: 奇安信攻防社区
date: 2025-01-08
fetch_date: 2025-10-06T20:04:32.822777
---

# MFC程序原理与逆向

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### MFC程序原理与逆向

MFC静态分析技巧，以Emotet等一些使用MFC框架木马和其他利用MFC框架木马为例。方便快速定位恶意代码入口技巧。

预备知识
====
[关于消息和消息队列 - Win32 apps | Microsoft Learn](https://learn.microsoft.com/zh-cn/windows/win32/winmsg/about-messages-and-message-queues)
系统维护了一个大的消息队列，由驱动讲鼠标、键盘等硬件交互设备产生的信号包装成一个个数据结构，也就是常说的消息。系统维护了一个大的公共消息队列，每当键盘鼠标产生一个硬件消息后都会讲消息塞到这个大的消息队列中。然后等待各个UI程序的每个窗口线程，从这个大消息队列中取出自己窗口可以处理的消息后拿到自己的窗口回调消息队列里处理。
在开发早期没有各种UI框架的情况下，需要开发者自己注册窗口并设置窗口回调来处理自己想要的消息函数。后来微软推出MFC UI框架，可以使开发者高效的拖拽UI控件，为繁琐的UI代码设计节约了宝贵时间。但却为逆向工作者定位用户代码添加了负担。
MFC逆向基础概念
=========
MFC的消息机制本质是将SDK中的消息与指定窗口ID的控件进行绑定。这种绑定关系由一种全局消息映射表（AFX\\_MSGMAP）管理存储。该映射表一般存储在.rdata资源节中，所以查找该表应该优先过滤其他节的干扰。
pBaseMessageMap参数存放GetMessageMap函数指针
```js
struct AFX\_MSGMAP{
AFX\_MSGMAP \* pBaseMessageMap;
AFX\_MSGMAP\_ENTRY \* lpEntries;
}
struct AFX\_MSGMAP\_ENTRY{
UINT nMessage; //Windows Message
UINT nCode; //Control code or WM\_NOTIFY code
UINT nID; //control ID (or 0 for windows messages)
UINT nLastID; //used for entries specifying a range of control id's
UINT nSig; //signature type(action) or pointer to message
AFX\_PMSG pfn; //routine to call (or specical value)
}
```
AFX\\_MSGMAP结构中第一个字段是一个函数指针我们一般并不关注，第二个是我们关注的消息绑定项结构体数组指针。nMessage是窗口消息、nCode是消息附加信息、nID是窗口ID、pfn就是该控件用于处理指定类型消息的回调函数。
两个结构体在IDA内存布局如下，我们在静态逆向的过程就是找到对应的消息绑定结构然后直接定位到用户代码。这里偷懒直接借用Freebuf上其他师傅画的图
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-897013e560aaf5e4a1a230038fc1ebc90462daa6.png)
IDA逆向查找用户函数
===========
可以优先查看ResourceHacker从资源节中获取感兴趣的控件ID。
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-9dd91efbf1b0699ff64705c0a3a31ca4b909b024.png)
进入IDA使用比较明显的特征码搜索（ALT+B），我这里搜索的是1000的控件ID
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-fab19b530dabdde6fdc64cecf99d5cda8abf5e61.png)
过滤掉.text节相关内容
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-27995fb94e3284d7acca380e0530362a955e81f2.png)
选择过滤设置
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-1070dd373618cc1250407d53c7c377ac8c254430.png)
排除.text节
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-7bfc3f6f0e2d61fc0a32fca0599467b2b6399c25.png)
可以看到只有两个
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a47405fa485537c8a4e059663d8f27d6eaccada4.png)
点击任意一个向上滑动可以看到窗口类的虚表函数，因为MFC的消息映射绑定默认是跟在虚表后的。
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a0a7d9c7c2420749226e8a3c52a3d3ff471dac88.png)
观察虚表函数后的结构体，并手动将后续都修改为dword类型如下图所示
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-632682df453b7c52cef7df218a590e984f35ada4.png)
对比该图内存排布一致，则后续都应该为消息绑定的数组，数组最后以全0数据结尾。又由于GetMessageMap函数是pBaseMessageMap字段存储的值所以我们能很轻易的确定AFX\\_MSGMAP结构为
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-16b69d38d8d7e718c1aafa15db3733d136ab6aad.png)
可以看到freebuf文章的结构布局与IDA实际的布局不同，因为在IDA中有一段dword 0卡在AFX\\_MSGMAP和AFX\\_MSGMAP\\_ENTRY结构中间。该图存在误导
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-aba9db85d1fa4ee78849d69d6ba2d4034a986ed9.jpeg)
该窗口绑定的所有消息都在此处
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-3706b6054548b97ebc6b51058c4b8cc6cd99c0da.png)
最后以全0结构为结尾
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-3f50437c8564509f25a382be78765c922b6c74e7.png)
我们可以设置结构体便于我们静态分析，右键范围内变量创建结构体
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-48cb8754ad92f01ba1ed7c146ecaa19fa19bf75b.png)
创建原始结构
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-f1d2d74d7037067eb951bbd79891ec77849478ba.png)
修改后如下图
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-8c83de751a9c0033bf80ac3bd2b93f24b9757b90.png)
点击第一个AFX\\_MESSAGE\\_ENTRY按SHIFT+\\*快捷键，选择结构体数组有7个元素，可以看到CDialog的消息映射关系
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-180684f69798a3d3123f194bf43a3bfbbfef5d2b.png)
同时我们发现下方出现了用户定义主窗口的虚表
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-549eb8e0ab5a6a772ae7f531013484113e8b3565.png)
向下继续找发现一串0，证明该用户定义主窗口没有消息绑定
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a680cabda2f58a289eb3dbe7dc07fdf2ae42b6fd.png)
由上面总结，如果我们想通过IDA直接找到消息绑定数组，只需要搜索GetThisMessage函数即可
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-215bfc26f68497a5123fcfa3a2bc3b57dc82d3ca.png)
然后根据交叉引用即可定位所有窗口消息绑定
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-709dccd2ae590a27dbea6890ae83ebc24774172f.png)
同样的方法确定消息映射，可以发现此时两个结构体之间没有0填充，所以内存布局需要具体实例分析才能确定
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-f0bf943e52d2f225d43ab26d4a1992ed776bdf4e.png)
由此构建消息映射，可以看到该窗口是系统的help窗口，resourcehacker没有显示出该窗口的ID值。该ID可能是系统分配窗口
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-4733f35629e8f54da1ba56c7c18c0c91ff750889.png)
我们来到第一个构造的窗口绑定消息数组，可以找到想要的窗口按钮对应的消息处理函数
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-3adac96748a2d5a7e6c280641d62ede844aad632.png)
进入函数内部为用户态代码
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-ca9c312905bf395e7cdaff5461232e9c42deed15.png)
观察完整的rdata布局
可以最先看到动态初始化，我们用户定义的主窗口构造函数就是由该处调用
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-37f2b8c577fc70aef6bf98fbee9ce8bc37b238ba.png)
从CWinApp对象绑定的消息函数开始
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-07064d2e2554817288dd74a1a3cf424b373405e7.png)
然后紧接着是自定义的主窗口类对象
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-3eca0de40dfb732eeab114d46ecd47833fe6fb46.png)
最后一个继承的是CWinApp
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-ce7890ff055df3debbb5ca8c199f76030da6e911.png)
从源码也可能看到继承了CWinApp，所以逆向时继承CWinApp就是我们的用户可操控的代码。也就是主窗口类的虚表
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-f566176a38d8bdcd8b9282c4e1d881c30822a483.png)
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-73634f303f96b8f58a4d7f3f2f6fb8343af7c869.png)
这种InitInstance函数就是我们可控的窗口初始化代码，固定在CWinApp：Run上方，恶意软件可以藏在该窗口绑定逻辑类的初始化函数中
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-1dec87352075efe8e5b36deb4f4cd6d33305a91b.png)
我们还需要查看窗口逻辑类的InitInstance函数，该函数调用晚于构造函数，快于窗口初始化函数
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-d525355dbd642928eedccf1572edc1b49a83e9a4.png)
同时也可以绑定在窗口类的显示绘制模块钱CreateDialogIndirectParamA
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-aee8e8ba24fabea56c28e57f27dbdc43f0f3fcd7.png)
还可以通过IDA识别DoModual函数，该函数下方就是对该类窗口初始化的函数。InInitDialog函数是主窗口回调，通过CreateIndirect调用
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-71d6326ca41c14a80d36e3f99183b595e6c66f21.png)
Emote样本对比
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-e48a7921a167f8dff00a526f224b645c49549767.png)
点进去初始化函数如下，可以看到明显的恶意行为
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a22fa897ab28776fe8ab44ca907c1e111c4f6b28.png)
样本2
搜索CWinApp::Run函数
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-ecc204ca9b509c218eb6f8dc643bd8e1acf97df0.png)
找到run的上一个函数就是初始化窗口函数
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-5ea0ab53aafd84770536b47553c5804fc62b6dcd.png)
可以看到初始化加载恶意的资源
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a8a4b9b3c9a1a73a4bd474dce79979574bd51dc7.png)

* 发表于 2025-01-07 09:00:02
* 阅读 ( 4891 )
* 分类：[二进制](https://forum.butian.net/communi...
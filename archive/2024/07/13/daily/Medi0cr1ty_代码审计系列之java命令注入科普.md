---
title: 代码审计系列之java命令注入科普
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODE3NTU1OQ==&mid=2247484428&idx=1&sn=8b48c4956fcea87b50468de66be2537d&chksm=c067c324f7104a32fccd25bb94eccfe3b0b98fd56960e1f17832de3088ab949cd58fe502a5f9&scene=58&subscene=0#rd
source: Medi0cr1ty
date: 2024-07-13
fetch_date: 2025-10-06T17:45:38.548532
---

# 代码审计系列之java命令注入科普

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWjFJrOKCImN8tAKTSvAPVhRLg5cic4fdh7D8LmBUJBw5ygh5ZUwbQqdCibvCrGFU26dqINRicxwwglRQ/0?wx_fmt=jpeg)

# 代码审计系列之java命令注入科普

原创

medi0cr1ty

Medi0cr1ty

### 写在前面

这里只讨论使用java执行命令的情况(Runtime/ProcessBuilder),结合之前挖过过的一些case或者群里见到过的case来讲。

### 名词科普

**命令解释器shell**：是一种软件程序(可视作一门编程语言的代码解释器)，它接收用户在命令行界面输入的指令和参数，并将其转换为计算机可理解和执行的操作。如unix系统常见的sh,bash,dash,zsh，windows常见的cmd.exe

**命令注入**：是指攻击者通过在输入字段中恶意插入系统命令，利用应用程序对用户输入的不当处理，从而让系统执行这些恶意命令，达到获取敏感信息、控制服务器等非法目的。

### 原理科普

Java的命令执行之所以“特殊”，根本原因**jdk中提供的命令执行的接口Runtime或ProcessBuilder默认没有套命令解释器**，所以输入& | ; $() ``这类shell的表达式语法并不会被解释并执行，因为java并没有去解释这些表达式。

这个怎么理解呢，就好比下面的python代码你在终端你加了python3这个代码解释器去执行他能执行，你不加，直接丢给shell去执行，他也没法执行。是一样的道理。

```
python3 -c "import sys;print(sys.version)"
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWjFJrOKCImN8tAKTSvAPVhRJPaXBbqrY5zj6G7CJmTun6HNqmGnGc2huDRQTS0ia2yICxknbzzYOlQ/640?wx_fmt=jpeg&from=appmsg)

那为什么像php,python这类语言的命令执行就可以默认拼接呢？因为他底层默认就套了命令解释器。是不是除了java其他的都套了解释器?当然也不是，比如golang就没有，所以大胆预测一波，等golang真正大面积走进这些安全专家的视线里，同样的问题还会被重复提及。

回到Java命令注入的科普上，Runtime.exec的入参可以是一个字符串或者字符串数组作。ProcessBuilder则是数组或可变参数。Runtime.exec实际上是调的ProcessBuilder，ProcessBuilder只要不套解释器的情况下，命令注入的可能性会非常低，所以这里重点说Runtime.exec。

Runtime.exec的入参有下面这些:

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWjFJrOKCImN8tAKTSvAPVhRrgAiaicuTQnA3IK1xQXmUsCeR1XJrwJsF6l0RqS2ib0ALf980c8s1aoWA/640?wx_fmt=jpeg&from=appmsg)

入参为String的时候会使用空格以及\t\n\r\f做切割成数组：

```
public Process exec(String command,String[] envp,File dir)
throwsIOException{
if(command.length()==0)
thrownewIllegalArgumentException("Empty command");

StringTokenizer st =newStringTokenizer(command);
String[] cmdarray =newString[st.countTokens()];
for(int i =0; st.hasMoreTokens(); i++)
            cmdarray[i]= st.nextToken();
returnexec(cmdarray, envp, dir);
}

public StringTokenizer(String str){
this(str," \t\n\r\f",false);
    }
```

然后交ProcessBuilder继续执行，最终根据不同环境调不同的原生方法启动,其中cmdarray[0]也就是数组中第一个的作为真正需要执行的程序来执行。

```
public Process exec(String[] cmdarray,String[] envp,File dir)
throwsIOException{
returnnewProcessBuilder(cmdarray)
.environment(envp)
.directory(dir)
.start();
}
#pb.start()
static Process start(String[] cmdarray,
                         java.util.Map<String,String> environment,
String dir,
ProcessBuilder.Redirect[] redirects,
boolean redirectErrorStream)
throwsIOException
{

...
return new UNIXProcess
(toCString(cmdarray[0]),
             argBlock, args.length,
             envBlock, envc[0],
             toCString(dir),
                 std_fds,
             redirectErrorStream);
}finally{

...

}
}
UNIXProcess(finalbyte[] prog,
finalbyte[] argBlock,finalint argc,
finalbyte[] envBlock,finalint envc,
finalbyte[] dir,
finalint[] fds,
finalboolean redirectErrorStream)
throwsIOException{

        pid = forkAndExec(launchMechanism.ordinal()+1,
                          helperpath,
                          prog,
                          argBlock, argc,
                          envBlock, envc,
                          dir,
                          fds,
                          redirectErrorStream);

try{
            doPrivileged((PrivilegedExceptionAction<Void>)()->{
                initStreams(fds);
returnnull;
});
}catch(PrivilegedActionException ex){
throw(IOException) ex.getException();
}
    }
```

所以如果你传入的是sh -c "whoami;ls"那么java执行的第一个程序实际上sh而不是whoami或ls,sh执行后再根据自己的逻辑将whoami;ls切割并顺序启动，可以理解为whoami和ls是sh的子进程，sh是java的子进程; 如果传入的是"whoami&&ls"，java无法切割也不做解析,那么ls则不会作为第二个程序去执行，而是"whoami&&ls"这整个字符串作为一个程序去执行，环境中找不到这个文件，自然就会无法执行，进而一条都执行不成功。

### 注入科普

前面基础科普讲完了，那么就是注入技巧的问题了。在无前置过滤的情况下：

套了命令解释器的拼接可执行

```
String cmd = "whoami;id";
Runtime.getRuntime().exec(String.format("bash -c %s",cmd));
```

不套的拼接不可执行。

```
String cmd = "whoami;id";
Runtime.getRuntime().exec(String.format("xxxx %s",cmd));
```

但可以考虑污染前面的xxx程序的参数，间接实现rce。比如执行程序是curl的时候可以通过-o参数写文件实现间接rce

```
cmd = "http://www.baidu.com -o /tmp/baidu";
Runtime.getRuntime().exec(String.format("curl %s",cmd));
```

再比如find的-exec参数，玩法比较多样，也有没得玩的时候。

遇到的大多数情况类似，这种直接在host中拼接执行的，可控的部分不作为sh的参数来输入，而是作为deploy.sh这个程序的参数来输入，这个但凡写过几行python就不用说也能理解。所以有没有可能rce取决于你的程序本身(deploy.sh)，而不是sh

```
String deployCmd = "sh deploy.sh " + host ;
Runtime.getRuntime().exec(deployCmd);
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWjFJrOKCImN8tAKTSvAPVhRicQEANa8GYFkq1OByiaibvBL09PIfsMByGDYFErQ0aWNGYaRmtibw8zxDA/640?wx_fmt=jpeg&from=appmsg)

再讲个特殊情况，某群里看到的case，群友用来面试别人的面试题，猜测他预期的答案就是上面这种情况，让别人回答去审计"login.sh"这个程序。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWjFJrOKCImN8tAKTSvAPVhR1na7nYPUKicELR5JKZ24QxsbrkDiaVDrGSA1Ld0azzznl1hCgoqvnXBw/640?wx_fmt=jpeg&from=appmsg)

可如果代码真如图所示的话，真的是这么做吗？能rce吗？需要审计login.sh吗？

我认为不需要，因为login.sh后面没有空格就直接拼接了，拼接完后的文件名复杂化，大概率不存在，或文件内容不可控，审计个der。后面的参数又没办法作为sh的参数进行污染。

怎么rce呢？很简单，想办法控制sh执行的文件指向一个存在“漏洞”或者说命令执行行为的sh文件，再污染他的参数即可。

```
find / -type f -exec file {} + | grep "shell script"
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWjFJrOKCImN8tAKTSvAPVhRpVRHFOuZekl7t6FwlqLib8nwZDzH8PPIh0lnOrbquUsULuwApBeU6NA/640?wx_fmt=jpeg&from=appmsg)

很容易就看到/usr/bin/command这条命令实际上是一个bash脚本，语句做下简单的闭合即可完成命令注入。

```
String payload = "/../../../../../../../../../../../../../../../../../../../usr/bin/command bash -c 'id";
String cmd = "sh login.sh'" + payload + "'";
Runtime rt = Runtime.getRuntime();
rt.exec(cmd);
```

嗯，没错，有限制条件，就是得找个可以创建文件夹的点配合利用，在当前文件夹下创建login.sh'这个目录，否则unix下../是没办法跨域过一个不存在的文件夹的。

### 写在最后

这个有问题隔三差五就会在各个安全的群里看到有人问，成月经问题了。

它很基础吗? 这个但凡挖过几次实战使用洞的人都肯定会知道。

它不基础吗? 见过一堆搞了好多年了sdl的人讨论的时候将拼接后不能执行归咎于沙箱,归咎于rasp(环境中其实没这两因素); 也见过某些大厂的安全中台给别人出的考试题目里告诉研发没命令解释器执行ping命令也存在命令注入的风险。更别说群里问的新手(这种勉强可以理解)

我的总结是，大部分人没有挖洞不需要实战，唬住研发和leader就行，不需要验证，自然就不会知道。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWgZe1vrPKR3r2nK86bn8RL2HDnIDFEaKzCPlQK7xaCdRWMhf1zcP8uuDpfEPJEVomeD43vvLljORQ/0?wx_fmt=png)

Medi0cr1ty

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWgZe1vrPKR3r2nK86bn8RL2HDnIDFEaKzCPlQK7xaCdRWMhf1zcP8uuDpfEPJEVomeD43vvLljORQ/0?wx_fmt=png)

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
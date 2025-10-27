---
title: sign参数分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458584116&idx=1&sn=449e4fc11adc4e47a9aac8dffd0877ab&chksm=b18c34be86fbbda8464bdaf18da7962d229ca9d1d4ecd5704d79e633b7cd37ef4829d1a69227&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-28
fetch_date: 2025-10-06T19:20:57.342759
---

# sign参数分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HdGonls53t1vVzOPbheS5fFfxzKU0oyvVluTC5CcLwXWicdyqtUzBFyeNaSCBrv5icbke6p3P6zFWA/0?wx_fmt=jpeg)

# sign参数分析

绿豆粥

看雪学苑

# 接口参数定位

目标接口：搜索https://api.m.ooxx.com/client.action?functionId=search

版本：13.1.0

目标参数：body 中的 x-api-eid-token  和 sign

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fum6rPywWLQem3PDKyViaIA2r9Nh7Sq0OBTz8eIuibIjrIjxcXr92MEng/640?wx_fmt=png&from=appmsg)

定位接口参数的方法

◆搜索大发

◆hook Hashmap

◆Hook StringBuilder

这里我们直接使用最朴素的搜索大法，一次就中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fMPxzx7PpicTDS2bziaKGb7oGVK5YotMRf6I2rY9H8jXuaxorQxqJquAA/640?wx_fmt=png&from=appmsg)

继续跟踪，进最下面这个看看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fcKLaX4xhsE3yTedBIbl28JaNb1yOuMbKPQI9oxByqW0RXcxQMn9uNQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fAxIfCN9hP41AYX2FBbCicLJkZs68IGma8KcEfiav8KoobickaSRGrjAwQ/640?wx_fmt=png&from=appmsg)

下面拼接了 urlEncodeUTF82  ，看英文就是一个 utf 编码之后的数据。继续向上跟踪

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fXaVaV79pVmIrjJVHs40nyfC5vWdSwZKlqkl9oXoUDu1w9EKeicywUCw/640?wx_fmt=png&from=appmsg)

进入第一个，函数返回的是一个字符串。还不是加密的地方。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fcx1QkN5HYic9649TZVdkrHh1ibV4IG68SesdTnq1NwOibE8FQ8oblpL6w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5f8rz1ZVzZqspln52rUGfMhLK0fyxtxWSByLicforbATjulAXMW4RNSAw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fWr6LH72KPs1icsP2RmCxicVIbUZmR3L2GkPSZfaGotRpWn9VQqPRSE9w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fGArL15RjrCAeU3xnBzOic3l1sukAN4DCI4ZiaQIdAyeHUwpric4V5rm6A/640?wx_fmt=png&from=appmsg)

JDHttpTookit.getEngine().getSignatureHandlerImpl().signature 这就是签名函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fdoLP9DibU7CiamLJs1x6BTr26StNHnvpkc9ciaxFwAduHU4ZHbkGwfotQ/640?wx_fmt=png&from=appmsg)

接口函数一般是 implement 或者直接 new 出来。这里跟进 new 出来的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fm3BxIaqBomHibbhxbPsTsD4IH4d2I8ttex1q8esbg7gB5ZViaH4PVryQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fiaQKWkZpXB5DO0T31frx4YMNiahJZpfLeyvibjW1W33Vq6gjLD0upps5Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5f9ZW0BdueYsT9dicK5fgoOovEFjELeSibeTCRcytdI07zzzfxtVZxbQibg/640?wx_fmt=png&from=appmsg)

## Hook 获取参数

通过 frida 获取传入的参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fzR9NAlz941n9uPlict6c6INfOqJ4xQ2Wovu0B7lULrjbiaZV2B2ZAkpw/640?wx_fmt=png&from=appmsg)

主动调用，方便后续做测试

```
function call_by_java() {
    Java.perform(function(){
        let BitmapkitUtils = Java.use("com.ooxx.common.utils.BitmapkitUtils");
        let context = Java.use("android.app.ActivityThread").currentApplication().getApplicationContext();
        let str = 'search'
        let str2 = '{"addrFilter":"1","addressId":"0","articleEssay":"1","attrRet":"0","buriedExpLabel":"","deviceidTail":"38","exposedCount":"0","filterServiceIds":"1468131091","first_search":"1","frontExpids":"F_001","gcAreaId":"1,72,55674,0","gcLat":"39.944093","gcLng":"116.482276","imagesize":{"gridImg":"531x531","listImg":"358x358","longImg":"531x708"},"insertArticle":"1","insertScene":"1","insertedCount":"0","isCorrect":"1","jdv":"0|kong|t_2018512525_cpv_nopay|tuiguang|17303608941925019140008|1730360893","keyword":"空气加湿器","localNum":"2","newMiddleTag":"1","newVersion":"3","oneBoxMod":"1","orignalSearch":"1","orignalSelect":"1","page":"1","pageEntrance":"1","pagesize":"10","populationType":"232","pvid":"","searchVersionCode":"10110","secondInsedCount":"0","showShopTab":"yes","showStoreTab":"1","show_posnum":"0","sourceRef":[{"action":"","eventId":"MyJD_WordSizeResult","isDirectSearch":"0","logid":"","pageId":"Home_Main","pvId":""},{"action":"","eventId":"Search_History","isDirectSearch":"0","logid":"","pageId":"Search_Activity","pvId":"632ba208e4854bb1839e6e32a5e6b841"}],"stock":"1","ver":"142"}'
        let str3 = "bd132c578e85c7cd";
        let str4 = "android";
        let str5 = "13.1.0";

        let result = BitmapkitUtils.getSignFromJni(context, str, str2, str3, str4, str5);
        console.log("BitmapkitUtils.getSignFromJni result = " + result);
    })
}
```

```
BitmapkitUtils.getSignFromJni result = st=1731485532078&sign=3c9820dce84fc15ceaf29bf0e0630306&sv=111
```

结果中就包含了我们今天的主角 ==sign==  。长度为 32 脑海中就冒出 MD5了。

## 确定 so

调用到了 native 层了。java 层的分析就到这里了。这里类中并没有看到加载 so 。需要通过 frida hook 导出的符号表，反查 so 的名字。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fEia1FGGkpmEAspV8XPTbngIP1ZsAGRb0PWKMMLJ5utlUSs95iarLTQkA/640?wx_fmt=png&from=appmsg)

得到模板 so 的名字为  libjdbitmapkit.so

# so 分析

IDA 打开可以看到 getSignFromJni 的导出函数 。通过 IDA frida-trace 先 trace 一份日志方便后面分析

工具：https://github.com/Pr0214/trace\_natives

把下载到的 traceNatives.py 放到 ida 根目录的 plugin 目录下重启 IDA。点击 edit -> plugins -> traceNatives 会生成一个文件夹给frida-trace 使用。

```
 frida-trace -H iP:port -F -O D:\ooxx\libjdbitmapkit_1731482430.txt
```

frida 就会开始trace 此时不要关闭命令行，直接调用刚才的主动触发的函数 call\_by\_java() 就会生成追踪数据，复制保存成一个 log 文件方便后面分析。

再用 findHash 插件看看能不能找到什么有用的信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fFw4g6ZqxUlzFrvj1yjLJLmuiag7Zgk35RRy5LOL276czJd6BVj8VTnw/640?wx_fmt=png&from=appmsg)

把两个数据做对比发现了 sub\_27A4 这个函数在两边都有出现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fv0fuC6V7uCkibOBm9sibYuaO8iao3ic36DCAqfNgG9e1IAKRWyIwFuruWQ/640?wx_fmt=png&from=appmsg)

IDA 中按 g 跳转过去看看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5flmjYfWw5C5QZ8IuKygAbmsEeFibtQUooM8gfFZvM2Ff4icXYtJzR0Cjg/640?wx_fmt=png&from=appmsg)

看上去很像 MD5 哦，点击数字按 h 转换成十六进制然后去搜索一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fzkwicUPm26L3cT61vN0Pk7Ngmn427NMwnjNxdBK6L3hb2bzbAvKrYoA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fqVQkglSUfVCKn1hvicK9gkpV5AocDQjxkibRiarhdxYiaRkdicrPicYmC18g/640?wx_fmt=png&from=appmsg)

有点意思！应该是MD5。查看 trace  日志，sub\_8134() 是最开始的地方，IDA 中看看是什么内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5faib0nrwOaWOzvjn9ASJA0COX1icVibQ29Txs3eA2tXDaKfhic0VWhvu9SA/640?wx_fmt=png&from=appmsg)

经过对比发现，我们的入口函数也就是 8134 。那还有什么说的，盘他咯！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HdGonls53t1vVzOPbheS5fxsM7MkfXaTSm0eNfSV4jIvZDdrib0EVhqlEPicC61g2Bs73nnzXw1LZg/640?wx_fmt=png&from=appmsg)

在 trace 日志中 8134  这层调用的最后一个函数是 33b4，进入 33b4 之后就是 MD5算法了。我们先 hook 7e08 查看入参。

```
function print_arg(addr) {
    try {
        var module = Process.findRangeByAddress(addr);
        if (module != null) return "\n"+hexdump(addr) + "\n";
        return ptr(addr) + "\n";
    } catch (e) {
        return addr + "\n";
    }
}

function hook_native(funptr,paramsNum) {
    var md = Process.findModuleByAddress(funptr);
    console.log("hook func ");

    try {
        //hook 指定函数
        Interceptor.attach(funptr,{
            onEnter: function(args){
                this.logs =""
                this.params = [];
                this.logs = this.logs.concat("So: "+md.name  +"  Method: " + ptr(funptr).sub(md.base) + "\n")
                for (var i = 0; i < paramsNum; i++) {
                    //参数
                    this.params.push(args[i]);
                    this.logs = this.logs.concat("this.args "+i+" onEnter: " +print_arg(args[i])+"\n")
                }
            },
            onLeave: function(retval){
                for (let i = 0; i < paramsNum; i++) {
                    this.logs=this.logs.concat("this.args" + i + " onLeave: " + print_arg(this.params[i]));
                }
                this.logs=this.logs.concat("retval onLeave: " + print_arg(retval) + "\n");
                console.log(this.logs)...
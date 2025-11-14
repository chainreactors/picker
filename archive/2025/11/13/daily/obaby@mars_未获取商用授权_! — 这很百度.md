---
title: 未获取商用授权?! — 这很百度
url: https://h4ck.org.cn/2025/11/21985
source: obaby@mars
date: 2025-11-13
fetch_date: 2025-11-14T03:12:31.808931
---

# 未获取商用授权?! — 这很百度

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

黑客程序媛 / 逆向工程师 / 人工智能学徒 / 用爱发电的独立开发者

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[前端开发『FrontEnd』](https://h4ck.org.cn/cats/cxsj/%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91%E3%80%8Efrontend%E3%80%8F)

# 未获取商用授权?! — 这很百度

2025年11月13日
[38 条评论](https://h4ck.org.cn/2025/11/21985#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/微信图片_20251113151227_376_42.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20251113151227_376_42.jpg)

上午的时候，收到 [梦不见的梦](https://www.friendcc.com) 的一条 qq 消息，说出现了授权问题。

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251113-151506.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251113-151506.jpg)

看了下提示域名，大概率就是 tm 百度地图弹的，那个域名做了个足迹应用就这么放着。

就在上个月自己更换 ssl 证书的时候还一切正常，结果现在来了这么一出。本来就是个人开发者，纯自用的东西，还经常收到百度的电话让升级企业认证，之前就是不小心升级了，结果一年要五万的授权费用。

我 tm 就自己玩的，还需要花钱，真 tm 服了。看来这戏破玩意儿都完犊子之后，最后能玩的也就只剩下天地图了。

刚开始是以为嵌入的问题，看了下嵌入页面都会提示：

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251113-130524-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251113-130524.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251113-130608.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251113-130608.jpg)

各种提示信息：

【d45a31】未获取商用授权，平台资源与服务稳定性受限；详情信息请前往：https://lbs.baidu.com/faq/search?id=314&title=908

并且后来发现，不单纯是弹窗在地图的贴图上也会出现授权提示，不得不说。这狗皮膏药贴的有水平。

对应的 js：

```
地址：
https://api.map.baidu.com/?qt=cen&b=7597813.822562976%2C687420.7063757228%3B15519477.822562976%2C7879996.706375723&l=5&ie=utf-8&oue=1&fromproduct=jsapi&ak=BxlnBNX55clLsUHVFZlaukyJesN5F5VI&callback=BMapGL._rd._cbk28033&v=gl&seckey=hNJCxM58roJGqVuMKRuYPEZfDZ%2FdhlL4Pp7JxBsDoLNUSc3QN6CRIbBdAJ%2FOt7zPayXwFYMsbLGx0%2BZUValnOg%3D%3D%2ChNJCxM58roJGqVuMKRuYPEZfDZ_dhlL4Pp7JxBsDoLPlabo3s2HGFnIPFXI8e1esM9-LzywgHJdkZjwHcr89ZaWfdPB6XAgd7DE4lcFgxfu8J0x_GywX0u2he7lW2roGgTrZQMyK7kcSPMHFwMyFrx45ktBewEco-xsnR-zdIctg5lIvP6h-iihbsl6ehY9AbrnGwefDt0BtO6gKCedJ8PeXNIUPh2rilmKFv6PZRd0&timeStamp=1763012808396&sign=07d57e493b29
内容：
/**/BMapGL._rd._cbk28033 && BMapGL._rd._cbk28033({"result":{"b":"7597813.822562976,687420.7063757228;15519477.822562976,7879996.706375723","callback":"BMapGL._rd._cbk28033","catalogID":0,"count":0,"current_null":1,"db":0,"error":503,"error_msg":"未获取商用授权，平台资源与服务稳定性受限；详情信息请前往：https://lbs.baidu.com/faq/search?id=314\u0026title=908","fromproduct":"jsapi","ie":"utf-8","jump_back":0,"l":"5","op_gel":0,"oue":"1","popup":1,"qt":"cen","requery":"","res_l":-1,"res_x":"0.000000","res_y":"0.000000","return_query":"","seckey":"hNJCxM58roJGqVuMKRuYPEZfDZ/dhlL4Pp7JxBsDoLNUSc3QN6CRIbBdAJ/Ot7zPayXwFYMsbLGx0+ZUValnOg==,hNJCxM58roJGqVuMKRuYPEZfDZ_dhlL4Pp7JxBsDoLPlabo3s2HGFnIPFXI8e1esM9-LzywgHJdkZjwHcr89ZaWfdPB6XAgd7DE4lcFgxfu8J0x_GywX0u2he7lW2roGgTrZQMyK7kcSPMHFwMyFrx45ktBewEco-xsnR-zdIctg5lIvP6h-iihbsl6ehY9AbrnGwefDt0BtO6gKCedJ8PeXNIUPh2rilmKFv6PZRd0","sign":"07d57e493b29","spec_dispnum":0,"time":0,"timeStamp":"1763012808396","total":0,"tp":0,"type":11,"v":"gl","wd":"","wd2":"","what":"","where":""},"current_city":{"code":0,"geo":"","level":0,"name":"","sup":0,"sup_bus":0,"sup_business_area":0,"sup_lukuang":0,"sup_subway":0,"type":0,"up_province_name":""},"hot_city":["北京市|131","上海市|289","广州市|257","深圳市|340","成都市|75","天津市|332","南京市|315","杭州市|179","武汉市|218","重庆市|132"]})
地址：
https://api.map.baidu.com/?qt=verify&v=gl&type=webgl&ak=BxlnBNX55clLsUHVFZlaukyJesN5F5VI&time=1763012794639&callback=BMapGL.bmapVerifyCbk
内容：
/**/BMapGL.bmapVerifyCbk && BMapGL.bmapVerifyCbk({"error":503,"error_msg":"未获取商用授权，平台资源与服务稳定性受限；详情信息请前往：https://lbs.baidu.com/faq/search?id=314\u0026title=908","popup":1})
```

我这个破玩意儿就是纯粹个玩具啊，你何苦这么狠心呢？！

对于这个东西，其实我也没啥好办法，刚开始登录百度 lbs 地图后台提示账号要年审。结果进行账号年审之后依然提示这个错误：

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251113-151359.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251113-151359.jpg)

这尼玛就离谱了啊，既然你年审不能解决，那就直接 hook 大法：

```
<!-- 拦截百度地图弹窗相关请求和Hook方法 -->
    <script>
        (function() {
            // 1. 拦截 fetch 请求
            const originalFetch = window.fetch;
            window.fetch = function(...args) {
                const url = args[0];
                if (typeof url === 'string' && url.includes('api.map.baidu.com')) {
                    // 检查是否是弹窗相关的请求
                    if (url.includes('qt=verify') || url.includes('qt=cen')) {
                        console.log('拦截百度地图弹窗请求:', url);
                        // 返回一个模拟的成功响应，避免弹窗
                        return Promise.resolve(new Response(JSON.stringify({
                            error: 0,
                            error_msg: "",
                            popup: 0,
                            result: {
                                error: 0,
                                popup: 0
                            }
                        }), {
                            status: 200,
                            headers: { 'Content-Type': 'application/json' }
                        }));
                    }
                }
                return originalFetch.apply(this, args);
            };

            // 2. 拦截 XMLHttpRequest
            const originalXHROpen = XMLHttpRequest.prototype.open;
            const originalXHRSend = XMLHttpRequest.prototype.send;

            XMLHttpRequest.prototype.open = function(method, url, ...rest) {
                this._url = url;
                if (typeof url === 'string' && url.includes('api.map.baidu.com')) {
                    if (url.includes('qt=verify') || url.includes('qt=cen')) {
                        console.log('拦截百度地图弹窗XHR请求:', url);
                        // 标记为已拦截，在send时处理
                        this._intercepted = true;
                    }
                }
                return originalXHROpen.apply(this, [method, url, ...rest]);
            };

            XMLHttpRequest.prototype.send = function(...args) {
                if (this._intercepted) {
                    // 模拟成功响应
                    Object.defineProperty(this, 'status', { value: 200, writable: false });
                    Object.defineProperty(this, 'statusText', { value: 'OK', writable: false });
                    Object.defineProperty(this, 'responseText', {
                        value: JSON.stringify({
                            error: 0,
                            error_msg: "",
                            popup: 0,
                            result: {
                                error: 0,
                                popup: 0
                            }
                        }),
                        writable: false
                    });
                    Object.defineProperty(this, 'readyState', { value: 4, writable: false });

                    // 触发事件
                    if (this.onreadystatechange) {
                        this.onreadystatechange();
                    }
                    if (this.onload) {
                        this.onload();
                    }
                    return;
                }
                return originalXHRSend.apply(this, args);
            };

            // 3. 拦截 JSONP 回调（百度地图使用JSONP）
            const originalCreateElement = document.createElement;
            const originalAppendChild = Node.prototype.appendChild;
            const originalInsertBefore = Node.prototype.insertBefore;

            document.createElement = function(tagName, ...rest) {
                const element = originalCreateElement.apply(this, ...
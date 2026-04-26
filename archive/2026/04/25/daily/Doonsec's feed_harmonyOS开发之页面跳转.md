---
title: harmonyOS开发之页面跳转
url: https://mp.weixin.qq.com/s/iTkUeJVovFRkMw_riYtqlg
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:56:15.610092
---

# harmonyOS开发之页面跳转

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/njicUbJnVlIzib2PxflZTWjhic97M3dO2KdNPwtC352fNYVuw4RXRLjN6iaSCgholervFQSPGSCNn4CEbiarKo3KuXKGcKRCMmMIBZjibvaH6zshM/0?wx_fmt=jpeg)

# harmonyOS开发之页面跳转

原创

书中自有代码来
书中自有代码来

书中自有代码来

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在应用开发过程中，我们经常需要在app的不同页面间跳转，那么在鸿蒙中，我们应该怎么跳转呢？

# 一、使用Router类跳转(简单但官方不推荐)

Router通过开发者提供的不同的url和参数访问不同的页面，允许在应用内跳转到某个页面，使用前先用UIContext中的getrouter方法获取到Router对象，再通过该对象调用对应方法。

1. 使用this.getUIContext().getRouter()获取到Router对象

> getRouter(): Router
>
> 获取Router对象。
>
> 返回值：
>
> | 类型 | 说明 |
> | --- | --- |
> | Router | 返回Router实例对象。 |

2. 使用pushUrl()方法来设置跳转选项

> pushUrl有多种使用方式：
>
> 1. Promise异步回调
>
> pushUrl(options: router.RouterOptions): Promise
>
> **参数：**
>
> | 参数名 | 类型 | 必填 | 说明 |
> | --- | --- | --- | --- |
> | options | router.RouterOptions | 是 | 跳转页面描述信息。 |
>
> **返回值：**
>
> | 类型 | 说明 |
> | --- | --- |
> | Promise | Promise对象。无返回结果的Promise对象。 |
>
> pushUrl(options: router.RouterOptions, mode: router.RouterMode): Promise
>
> **参数：**
>
> | 参数名 | 类型 | 必填 | 说明 |
> | --- | --- | --- | --- |
> | options | router.RouterOptions | 是 | 跳转页面描述信息。 |
> | mode | router.RouterMode | 是 | 跳转页面使用的模式。 |
>
> **返回值：**
>
> | 类型 | 说明 |
> | --- | --- |
> | Promise | Promise对象。无返回结果的Promise对象。 |
>
> 2. callback异步回调
>
> pushUrl(options: router.RouterOptions, callback: AsyncCallback): void
>
> | 参数名 | 类型 | 必填 | 说明 |
> | --- | --- | --- | --- |
> | options | router.RouterOptions | 是 | 跳转页面描述信息。 |
> | callback | AsyncCallback | 是 | router跳转结果回调函数。当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。 |
>
> pushUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback): void
>
> **参数：**
>
> | 参数名 | 类型 | 必填 | 说明 |
> | --- | --- | --- | --- |
> | options | router.RouterOptions | 是 | 跳转页面描述信息。 |
> | mode | router.RouterMode | 是 | 跳转页面使用的模式。 |
> | callback | AsyncCallback | 是 | router跳转结果回调函数。当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。 |
>
> RouterOptions
>
> | 名称 | 类型 | 说明 |
> | --- | --- | --- |
> | url | string | 表示目标页面的url，可以用以下两种格式：- 页面绝对路径，由配置文件中pages列表提供，例如：- pages/index/index- pages/detail/detail- 特殊值，如果url的值是"/"，则跳转到首页，首页默认为页面跳转配置项src数组的第一个数据项。 |
> | params | Object | 表示路由跳转时要同时传递到目标页面的数据，切换到其他页面时，当前接收的数据失效。跳转到目标页面后，使用router.getParams()获取传递的参数，此外，在类web范式中，参数也可以在页面中直接使用，如this.keyValue(keyValue为跳转时params参数中的key值)，如果目标页面中已有该字段，则其值会被传入的字段值覆盖。 |
> | recoverable | boolean | 表示对应的页面是否可恢复，默认为true。当为true时，表示可恢复，当为false时，表示不可恢复。 |
>
> > 页面路由栈支持的最大Page数量为32。
>
> RouterMode
>
> | 名称 | 值 | 说明 |
> | --- | --- | --- |
> | Standard | 0 | 多实例模式，也是默认情况下的跳转模式。目标页面会被添加到页面栈顶，无论栈中是否存在相同url的页面。说明：不使用路由跳转模式时，则按照默认的多实例模式进行跳转。 |
> | Single | 1 | 单实例模式。如果目标页面的url已经存在于页面栈中，则该url页面移动到栈顶。如果目标页面的url在页面栈中不存在同url页面，则按照默认的多实例模式进行跳转。 |

示例代码：

```
import { router } from'@kit.ArkUI';
import { BusinessError } from'@kit.BasicServicesKit';

// 定义传递参数的类
classinnerParams {
array: number[];

constructor(tuple: number[]) {
    this.array = tuple;
  }
}

classRouterParams {
data: innerParams;

constructor(tuple: number[]) {
    this.data = newinnerParams(tuple);
  }
}

@Entry
@Component
struct Index {
asyncroutePage() {
    letoptions: router.RouterOptions = {
      url: 'pages/next',
      params: newRouterParams([12, 45, 78])
    }
    this.getUIContext().getRouter().pushUrl(options).then(() => {
        console.info('跳转成功');
      })
      .catch((err: ESObject) => {
        console.error(`跳转失败, 失败码： ${(err as BusinessError).code}, 提示信息： ${(err as BusinessError).message}`);
      })
  }

build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('First Page')
      Button('Next page')
        .type(ButtonType.Capsule)
        .margin({ top: 20 })
        .onClick(() => {
          this.routePage()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

3. 使用getPrams()接收参数

> getParams
>
> **返回值：**
>
> | 类型 | 说明 |
> | --- | --- |
> | Object | 发起跳转的页面往当前页传入的参数。 |

示例代码：

```
// 在second页面中接收传递过来的参数
classinnerParams {
array: number[];

constructor(tuple: number[]) {
    this.array = tuple;
  }
}

classRouterParams {
data: innerParams;

constructor(tuple: number[]) {
    this.data = newinnerParams(tuple);
  }
}

@Entry
@Component
struct Next {
@Statedata: object = (this.getUIContext().getRouter().getParams() asRouterParams).data;
@StatesecondData: string = '';

build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('Second Page')
      Button('Back')
        .fontSize(30)
        .onClick(() => {
          try {
            this.getUIContext().getRouter().showAlertBeforeBackPage({ message: 'Are you sure to return?' })
          } catch (error) {
            // TODO: Implement error handling.
          }
          this.getUIContext().getRouter().back()
        })
        .margin({ top: 20 })
      Button(`传过来的参数：${this.secondData}`)
        .margin({ top: 20 })
        .onClick(()=> {
          this.secondData = (this.data['array'][1]).toString();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

# 二、HMRouter（官方推荐）

参考：ohrouter:基于 OpenHarmony 的应用内页面路由框架项目 - AtomGit | GitCode

HMRouter是HarmonyOS官方推出的页面跳转场景解决方案，底层封装了Navigation能力，旨在降低开发复杂度并提升效率。它支持通过自定义注解实现路由跳转，兼容HAR/HSP多模块开发，并具备路由拦截、生命周期管理及全局或单页面的自定义动画配置等强大特性。此外，该框架还支持单例、Dialog等多种页面类型。HMRouter通过简化Navigation细节并增强跳转能力，帮助开发者高效解决应用内原生页面的相互跳转问题。

## 页面跳转

1. 添加@HMRouter注解，并配置其中的pageUrl参数
2. 在需要进行页面跳转的位置，使用to方法进行页面跳转，在参数中配置待传递的参数。

> ```
> @HMRouter({ pageUrl: 'ProductContent' })
> @Component
> export struct ProductContent {
> @Stateparam: ParamsType | null = null;
> aboutToAppear(): void {
>     this.param = HMRouterMgr.getCurrentParam() asParamsType;
>   }
> HMRouterMgr.to('ProductContent')
>   .withNavigation('mainNavigationId')
>   .withParam({ a: 1, b: 2 })
>   .onResult((popInfo: HMPopInfo) => {
>     const pageName = popInfo.srcPageInfo.name;
>     const params = popInfo.result;
>     console.log(`page name is ${pageName}, params is ${JSON.stringify(params)}`);
>   })
>   .pushAsync()
> ```

3. 在跳转的目标页面使用HMRouterMgr.getCurrentParam()获取到传递的页面参数。

> ```
> this.param = HMRouterMgr.getCurrentParam() as ParamsType;
> ```

4. 在对应的业务逻辑位置使用HMRouterMgr提供的pop方法实现页面返回。

> ```
> HMRouterMgr.pop({ navigationId: 'mainNavigationId', param: this.param })
> ```

其他：

在HMRouter路由框架中，开发者只需要设置@HMRouter注解的dialog配置为true即可将当前页面作为弹窗使用。

```
@HMRouter({
  pageUrl: PageConstant.PRIVACY_DIALOG_DETAIL,
  dialog: true,
  // ...
})
```

更多场景参考：文档中心

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

书中自有代码来

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

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
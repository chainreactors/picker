---
title: 从直板到折叠屏：腾讯Kuikly如何适配 iPhone Duo？
url: https://mp.weixin.qq.com/s/12KFESHenMhUfmteEApLPg
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:48:04.475438
---

# 从直板到折叠屏：腾讯Kuikly如何适配 iPhone Duo？

# 从直板到折叠屏：腾讯Kuikly如何适配 iPhone Duo？

腾讯Kuikly
腾讯Kuikly

腾讯技术工程

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg)

Kuikly 是腾讯开源的高性能跨端框架，基于 Kotlin Multiplatform 技术，覆盖 Android、iOS、HarmonyOS、H5、微信小程序、Mac 六大平台，支撑业务日活用户超5亿。折叠屏产品发展迅速，苹果新推出的 iPhone Duo 带来了不同以往的布局和交互方式，对于跨端页面来说需要处理更多平台差异，带来了更多适配工作。Kuikly 采用原生 UI 渲染，可以很好适配系统的新特性，本文结合具体示例，介绍如何借助 Kuikly 复用跨端代码，做好折叠屏的适配工作。

## 背景

过往折叠屏适配的核心，主要围绕处理开合、旋转与分屏场景引发的视图尺寸变更做处理。对于跨端页面，基于响应式布局并结合四边安全区域适配，基本可以覆盖绝大多数的场景。而 iPhone Duo 引入全新的设备特征：屏幕存在多处需要避让的局部区域，同时导航栏、工具栏由系统跟随设备形态动态调整。这一变化对跨端页面适配构成新的约束：若维持跨端层自绘导航栏、工具栏的方案，不仅避让区域计算逻辑复杂度高，且无法对齐原生的交互行为。为了实现最佳效果，似乎只能由各平台差异化实现，牺牲跨端方案的效率优势。

针对这一问题，Kuikly 依托原生 UI 渲染的优势，在原有响应式布局和安全区域能力基础上，进一步对齐系统能力，提供保留区域信息与系统导航栏工具栏的原生桥接，侧边栏位的布局与行为交由系统原生组件处理，而页面结构、按钮配置与交互逻辑仍在跨端代码里统一维护，兼顾了原生体验与跨端效率。

## 折叠屏基本特点

屏幕更大。 展开后的内屏接近一台小平板，一屏能显示的内容比普通手机多不少。很多原来要翻几页、点几次才能看到的信息，现在可以放在同一屏里。

屏幕尺寸会变。用户随时可能把手机合上或打开，App 会在外屏和内屏之间切换，拿到的宽高也跟着变。打开后再分屏或旋转，可用空间还会继续变化。按开合程度，划分三种形态：

* 折叠态：合上后使用较小的外屏，适合单栏聚焦。
* 展开态：完全展开，更大的屏幕，适合充分展示内容。
* 悬停态：半折状态，适合分开呈现内容和操作。

折叠屏的特点给页面设计和开发带来了新的要求：布局要随屏幕尺寸调整，也要用好更大的空间，让内容展示和操作更高效。

## iPhone Duo 新变化

![](https://mmecoa.qpic.cn/sz_mmecoa_png/2YTOibpx9RUC7IIkZeq3hnjHSicdcnedzPwas9zR84OGHVfJ32EsiaeLXibr0xRDl2yHI89pcFkUIWWL2O62InoUFtT3kjw8uLroCaiaof6OE67Y/640?wx_fmt=png&from=appmsg#imgIndex=0)

图片1 iPhone Duo的各形态

iPhone Duo 区别于以往的折叠屏适配，还要关注额外的变化：

* Vertical Controls（垂直控制栏）

iPhone Duo 最容易被用户感知到的变化，是系统控制区的位置。过去所有折叠屏设备在系统控制区位置都是沿用直板手机形态，顶部导航，底部 Tab Bar，中间内容。但苹果在折叠屏上把导航栏、工具栏和 Tab 控制放到屏幕侧边，为内容留出更多纵向空间。而且在分屏情况下，状态栏会分别出现在左右两侧，系统响应式容器会有相对应自适应能力。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/2YTOibpx9RUDChGX4PszbZfGPRmxibiaSeVVibMRDDicQ8HYJ3MpugspturUTeGn4FwDuD08BWQ24VXubVWJojmRtU7YW6MpXicAz31WcCHSmqYWo/640?wx_fmt=png&from=appmsg#imgIndex=1)

图片2iPhone Duo的垂直控制栏

* ### Reserved Regions（保留区域）

过去布局主要通过安全区避开系统 UI。在iPhone Duo上，还要关注屏幕内部的摄像头和折叠位置。内外屏摄像头可能占用局部空间，设备部分展开时，中间的折叠区域也会影响内容排列。苹果通过预留区域描述这些位置及其生效状态，App 可以据此避开遮挡，或把内容安排到折叠区域两侧。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/2YTOibpx9RUBFxSibYnbBRauibTJEEElYxE1QNAOCficaJPaGx2vg2yFBLHzC7NuMFKgl6CAkY0oRYWZ1rDMoSXLpIiaj7ticykIOUkeia7WAe2k0o/640?wx_fmt=png&from=appmsg#imgIndex=2)

图片3iPhone Duo的保留区域

苹果官方给出的设备指南是：「可调整大小是你的 App 在 iPhone Duo 上的关键功能。如果你的 App 已在 iPad 和 Mac 上运行，或者你已在 iPhone Mirroring 中准备好让 App 调整大小，那么你已经为支持 iPhone Duo 打下了坚实基础。如果没有，请采用标准布局控件和容器，并使用大小类和场景几何来改进 App 的大小调整功能。然后，处理保留区域（例如折叠区域）来调整 App 大小并处理折叠布局。评估排列视图是否可以协助 App 布局来处理折叠区域。

在某些姿态下，iPhone Duo 会将导览栏、工具栏和标签栏一起垂直显示在显示屏侧边。请检查并整理 App 中的栏，以确保常用控制始终可见，且在空间有限时，较少使用的控制会出现在溢出菜单中。」

## 跨端适配痛点

对跨端页面来说，难点在于复用同一套代码的同时，还要适应各端不同的系统行为。布局可以随尺寸调整，但安全区、折叠区域、系统栏的位置和行为需要分别接入；单栏切换到多栏时，还要保持页面跳转、返回和操作状态的一致。

这些差异都交给使用方处理，页面中就会增加大量平台判断，未来还可能出现更多设备形态，逐端、逐页适配的成本会持续增加。因此，跨端框架需要把通用布局和交互留给业务复用，将设备差异封装成可用的能力，既减轻适配负担，也让页面能够利用各端的设备特性，这也是 Kuikly 的适配思路。

总体可以把适配划分成两部分：通用的尺寸和布局变化，以及预留区域、系统侧栏等设备特有的能力。Kuikly 采用原生 UI 渲染，前者可以沿用已有的响应式布局，后者通过预留区域、系统导航栏和工具栏等实现原生能力的接入，业务页面仍然使用 Kuikly 配置内容和交互。下面结合具体示例，看看现有页面如何适配折叠屏，并利用 Duo 的设备特性。

## Kuikly 适配指南

### 1. 布局随可用空间变化

Kuikly 从一开始就支持响应式刷新和 Flex 布局。折叠、展开或分屏带来的尺寸变化，可以沿用这套机制处理。

在 attr 中使用 pageData.pageViewWidth 和 pageData.pageViewHeight 计算尺寸，宿主上报尺寸变化后，相关布局属性会自动更新。结合 flex(1f) 分配剩余空间，可以减少固定尺寸和手动高度计算。

展开后不必一味拉伸。阅读、表单等内容可限制最大宽度并居中，多出的空间用于留白、增加列表列数或展示详情。

```
// KuiklyDSLView {    attr {        flex(1f)    }    View {        attr {              width(ctx.pageData.pageViewWidth * 0.8f)            maxWidth(600f)        }         }} // Kuikly ComposeDSLval pageWidth = LocalConfiguration.current.pageViewWidthBox(Modifier.width(minOf(pageWidth * 0.8f, 600f).dp)) {     /* ... */ }
```

![](https://mmecoa.qpic.cn/mmecoa_gif/2YTOibpx9RUDf0VCyXUJXzkekSFf7vWicpLzaO9tInBibd69QjzU7mbdLu5TBJXwY3s28yB52vlvicSl3LngwL7Jb6YY4TI6dWo3eGMC0GuKJTc/640?wx_fmt=gif&from=appmsg#imgIndex=3)![]()

图片4折叠屏展开页面布局变化样例

### 2. 安全区域和避让

安全区域仍然是多设备适配的关键。不同设备的刘海、系统栏和手势区域不同，文字和操作控件需要按当前安全区域避让。旋转、分屏或开合时，安全距离也可能变化，布局应随之更新，而不是预留固定的顶部、底部间距。

Kuikly 通过 pageData.safeAreaInsets 提供上、下、左、右的安全距离。把安全区域绑定到内容边距，就能随安全区变化调整布局：

```
// KuiklyDSLView {    attr {        flex(1f)        paddingTop(ctx.pageData.safeAreaInsets.top)        paddingLeft(ctx.pageData.safeAreaInsets.left)        paddingBottom(ctx.pageData.safeAreaInsets.bottom)        paddingRight(ctx.pageData.safeAreaInsets.right)    }    // 需要安全区保护的前景内容}   // Kuikly ComposeDSLval configuration = LocalConfiguration.currentconfiguration.pageViewWidth                                // 订阅尺寸变化val safe = configuration.pageData.safeAreaInsets Box(Modifier.fillMaxSize().background(bgColor)) {          // 背景铺满    Column(        Modifier.fillMaxSize().absolutePadding(            left = safe.left.dp, top = safe.top.dp,            right = safe.right.dp, bottom = safe.bottom.dp,        )    ) {        // 需要安全区保护的前景内容    }}
```

过去App做适配页面主要用 Top 和 Bottom 处理避让导航栏和底部状态栏。而Duo 的导航栏和工具栏可能移到侧边，因此也要关注 left、right，并结合系统栏的实际占位处理左右空间，不能只留上下边距。

在iPhoneDuo上，除了安全区域外，还要关注预留区域，处理摄像头、状态栏遮挡和折叠带来的布局限制。

* 遮挡区域：避免文字、按钮等关键内容与它重叠。
* 分割区域：需要分区的页面，可以把内容安排到折叠区域两侧；

Kuikly 通过 pageData.reservedRegions 提供区域的位置、大小、类型和当前是否生效，区域使用 x、y、width、height 描述，坐标相对 Kuikly 根视图，计算规避后的坐标。

如果希望背景、图片等内容延伸到顶部，可以不对整页统一添加 paddingTop，通过 pageData.reservedRegions 对当前生效的遮挡区域做局部避让。

```
// KuiklyDSLView {    attr {        val pageWidth = ctx.pageData.pageViewWidth        val occlusion = ctx.pageData.reservedRegions.firstOrNull {            it.active && it.kind == ReservedRegionKind.OCCLUSION && it.x >= pageWidth / 2f        }        // 伪代码：有右侧遮挡时，避让右边位置 right         val paddingRight = if (occlusion != null) pageWidth - occlusion.x + 12f else 12f        absolutePosition(right = paddingRight)    }} // Kuikly ComposeDSLval configuration = LocalConfiguration.currentval pageWidth = configuration.pageViewWidthval occlusion = configuration.pageData.reservedRegions.firstOrNull {    it.active && it.kind == ReservedRegionKind.OCCLUSION && it.x >= pageWidth / 2f}val badgeRight = if (occlusion != null) pageWidth - occlusion.x + 12f else 12f Box(Modifier.fillMaxSize().background(bgColor)) {           // 背景延伸到顶部    Text(        "角标",        Modifier.align(Alignment.TopEnd)            .absolutePadding(top = 12.dp, right = badgeRight.dp),    )}
```

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/2YTOibpx9RUAaBvPnOyC8N8ebAwPVhXGcOl1guzBSyVk1oYmHFsv7jMaicwf4ogwwZKoAUsib8F3yGNxWMKRpurDbFsDFpCbHENVSmEF8Xw694/640?wx_fmt=gif&from=appmsg#imgIndex=4)![]()

图片5避让iPhone Duo的遮挡区域

### 3. 空间变大后，怎么展示内容

展开后不一定要把所有元素放大。常见做法有三种：拉伸、调整布局和多栏展示，具体选哪种取决于页面内容。

#### 拉伸：让适合扩展的内容占用更多空间

文本、画布等内容，可以扩展显示区域。普通按钮、图标和字号通常不用跟着同比例放大。

阅读页则要限制正文宽度，避免展开后每行文字过长。多出来的空间可以留白，不必强行填满。

#### 调整布局：重排页面，或者增加列数

如：图文卡片可以由上下排改为左右排，信息流可以增加列数。Kuikly 的
WaterfallList(KuiklyDSL)、LazyVerticalStaggeredGrid(ComposeDSL)支持设置列表宽度和列数：

```
// KuiklyDSLWaterfallList {    attr {        flex(1f)        listWidth(ctx.pagerData.pageViewWidth)        columnCount(if (ctx.pagerData.pageViewWidth >= 600f) 4 else 2)        itemSpacing(10f)        lineSpacing(10f)    }    // 普通卡片不写死宽度，由列表按列宽分配} // Kuikly ComposeDSLval pageWidth = LocalConfiguration.current.pageViewWidthLazyVerticalStaggeredGrid(    columns = StaggeredGridCells.Fixed(if (pageWidth >= 600f) 4 else 2),    modifier = Modifier.fillMaxSize(),    verticalItemSpacing = 10.dp,                          // 对应 lineSpacing    horizontalArrangement = Arrangement.spacedBy(10.dp),  // 对应 itemSpacing) {    items(feed, key = { it.id }) { item ->        FeedCard(item, Modifier.fillMaxWidth())   // 卡片不写死宽度，由网格按列宽分配    }}
```

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/2YTOibpx9RUDjL64t6gQEfvF4uZIUg1qnvuG06clesV6QWJDib1AP0UIKwXPWdecf5iaUBQ2LicYLa23YDnTSyDIjjPh4ZyIMZKiblcYzovMvfVA/640?wx_fmt=gif&from=appmsg#imgIndex=5)![]()

图片6瀑布流列数随屏幕大小展开

#### 双栏：同时展示有关联的内容

列表与详情、目录与正文等关联内容，可以在宽屏下并排展示，窄屏下仍按单栏逐级访问。外屏和内屏应保持一致的内容和操作逻辑，展开后只是把原来分步查看的信息同时呈现，让用户感觉仍在使用同一个 App。

详细可以参考：「[iPhone Duo来了，腾讯 Kuikly 助 App 从容适配 | 跨平台框架—tds-Kuikly](https://kuikly.tds.qq.com/Blog/iPhone%20Duo%E6%9D%A5%E4%BA%86%EF%BC%8C%E8%85%BE%E8%AE%AF%20Kuikly%20%E5%8A%A9%20App%20%E4%BB%8E%E5%...
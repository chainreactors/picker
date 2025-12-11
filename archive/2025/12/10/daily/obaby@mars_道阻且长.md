---
title: 道阻且长
url: https://h4ck.org.cn/2025/12/22122
source: obaby@mars
date: 2025-12-10
fetch_date: 2025-12-11T03:23:05.582518
---

# 道阻且长

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

[个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# 道阻且长

2025年12月10日
[35 条评论](https://h4ck.org.cn/2025/12/22122#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/12/微信图片_20251210130218_429_42.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/12/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20251210130218_429_42.jpg)

都道：“一步错，步步错”。虽然有时候是无心之失，却也在不经意间制造了太多的问题。就想撒了个谎，后面需要无数的谎言来解释当初这个谎言。最开始开发 app 的时候，对于所谓的前段并没那么清晰深入的理解，毕竟之前做 ios 和安卓的开发还是基于 oc 和 java 来搞。

之前虽然也看过不少 uni 的项目，但是真正开始的时候。当时还是选择了 vue2 的矿建，虽然那时候3 也依然有些规模。鉴于当时找到的很多组件都是 vue2 的不支持 3，所以开始的时候就入了这个坑，直接基于 2 的各种组件搭起来了现在的这个闺蜜圈的项目。

当然，后续再开发过程中也发现了很多问题，虽然是 vue2 的各种组件，然而很多满足不了自己的需求，在不断的开发过程中也在不断的修改这些组件，甚至很多组件到现在已经改的完全不是原来的样子了。重写了大量的代码，也修复了很多组件的问题。所谓的生态，国内的生态环境并不是看到的那么好。各种插件市场非常活跃，插件也非常多。但是实际上出了问题大概率得不到作者的解答，只能自己去读代码，理解逻辑之后重写有问题的部分。

再后来，鸿蒙 next 横空出世，uni 也承诺会支持鸿蒙系统。当然后来也确实是支持了，不过仅支持 vue3 的项目的鸿蒙系统编译。于是这原来的 vue2 的项目就面临着一次大版本的升级和兼容处理。在开发了一年之后，如果重新搭架子从 vue3 重写，成本固然是太高了，不在可接受的范围之内。最终的方案是直接将 vue2 的项目迁移到 vue3。

在去年uni 开放鸿蒙的体验版本兼容编译之后，就尝试将项目迁移到 vue3，不过那时候仅限于能编译运行。可以登录到首页，而其他的页面全部都没处理。在这次鸿蒙的技术支持介入之后，也是下定决心将项目迁移到 vue3 进一步迁移到原生鸿蒙。到原生鸿蒙才是最终目的。

[![](https://h4ck.org.cn/wp-content/uploads/2025/12/Screenshot-2025-12-10-123741-tuya.png)](https://h4ck.org.cn/wp-content/uploads/2025/12/Screenshot-2025-12-10-123741-tuya.png)

不过在迁移过程中也发现一些问题：

1.导航栏 button 无效：

```
HarmonyOS 基于uniapp的方式开发HarmonyOS应用时候，通过app-plus:titleNView 配置页面右上角按钮未生效（API12+）
【问题描述】：HarmonyOs基于uniapp的方式开发HarmonyOS应用的时候，通过app-plus：titleNview配置页面右上角按钮不生效

【问题现象】：使用app-plus：titleNview配置导航栏右上角button不显示

【版本信息】：hbuilder 版本4.8.5、DevEco Studio 6.0.1 Release

【复现代码】：{

  "path": "pages/besties",

  "style": {

    "navigationBarTitleText": "XXX",

    "navigationBarBackgroundColor": "#ff4f87",

    "app-plus": {

      "bounce": "none",

      "titleNView": {

        "buttons": [{

          "fontSize": "18px",

          "text": "+",          // 直接写加号字符

          "color": "#FFFFFF"

        }]

      }

    }

  }

}
```

官方给的解决方案：

```
在基于 UniApp 开发 HarmonyOS 应用时，app-plus:titleNView配置未生效的核心原因是：app-plus是 UniApp 针对 Android/iOS 端设计的原生导航栏配置，HarmonyOS 平台的导航栏实现逻辑与 Android/iOS 不同，因此该配置暂未适配 HarmonyOS 平台。

解决方案：使用「自定义导航栏」替代（推荐，跨平台兼容）
由于 HarmonyOS 不支持 UniApp 的titleNView配置，建议通过隐藏原生导航栏 + 自定义导航栏组件的方式实现右上角按钮，同时兼容跨平台场景。

步骤 1：隐藏原生导航栏
在pages.json中，给目标页面的style添加navigationStyle: "custom"，隐藏原生导航栏：

json

{
  "path": "pages/besties",
  "style": {
    "navigationBarTitleText": "XXX",
    "navigationBarBackgroundColor": "#ff4f87",
    "navigationStyle": "custom", // 隐藏原生导航栏
    "app-plus": {
      "bounce": "none"
    }
  }
}
步骤 2：自定义导航栏组件（实现右上角按钮）
在页面中手动编写导航栏布局，包含标题和右上角按钮，示例代码（Vue3 语法）：

vue

<template>
  <!-- 自定义导航栏 -->
  <view class="custom-nav-bar" :style="{backgroundColor: '#ff4f87'}">
    <!-- 标题 -->
    <view class="nav-title">XXX</view>
    <!-- 右上角按钮 -->
    <view class="nav-right-btn" @click="handleRightBtnClick">
      <text :style="{fontSize: '18px', color: '#FFFFFF'}">+</text>
    </view>
  </view>

  <!-- 页面内容 -->
  <view class="page-content">
    <!-- 你的页面内容 -->
  </view>
</template>

<script setup>
// 右上角按钮点击事件
const handleRightBtnClick = () => {
  console.log("右上角按钮被点击");
  // 这里写按钮的业务逻辑
};
</script>

<style scoped>
/* 自定义导航栏样式（适配HarmonyOS状态栏高度） */
.custom-nav-bar {
  width: 100%;
  height: var(--status-bar-height) + 44px; /* 状态栏高度 + 导航栏高度 */
  padding-top: var(--status-bar-height); /* 适配状态栏 */
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 16px;
  box-sizing: border-box;
}

.nav-title {
  color: #FFFFFF;
  font-size: 18px;
  font-weight: bold;
}

.nav-right-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
}

/* 页面内容区，避免被导航栏遮挡 */
.page-content {
  padding-top: calc(var(--status-bar-height) + 44px);
}
</style>
补充说明（针对 UniApp X 项目）
如果你的项目是UniApp X（专门适配 HarmonyOS 的 UniApp 模式），可以直接使用 HarmonyOS 原生的Navigation组件配置右上角按钮（需在uts页面中实现）：

ts

// pages/besties/besties.uts
@Entry
@Component
struct BestiesPage {
  build() {
    Navigation() {
      // 页面内容
      Column() {
        Text("页面内容")
      }
    }
    .title("XXX") // 导航栏标题
    .titleMode(NavigationTitleMode.Free)
    .backgroundColor("#ff4f87")
    // 配置右上角按钮
    .toolBar({
      items: [
        {
          value: "+",
          textColor: "#FFFFFF",
          fontSize: 18,
          action: () => {
            console.log("右上角按钮被点击");
            // 业务逻辑
          }
        }
      ]
    })
  }
}
关键注意事项
app-plus配置的局限性：app-plus是 UniApp 对 Android/iOS 端的扩展配置，HarmonyOS 平台的导航栏、原生组件等逻辑与 Android/iOS 不同，因此大部分app-plus配置在 HarmonyOS 上不生效。
状态栏高度适配：自定义导航栏时，需通过var(--status-bar-height)获取 HarmonyOS 设备的状态栏高度，避免导航栏被状态栏遮挡。
UniApp X 的适配：若使用 UniApp X 开发 HarmonyOS 应用，建议直接使用 HarmonyOS 原生组件（如Navigation），兼容性和体验更好。
通过自定义导航栏或 UniApp X 的原生Navigation组件，即可实现 HarmonyOS 应用中页面右上角按钮的需求，同时保证跨平台兼容性或原生体验。
```

官方答复地址：<https://developer.huawei.com/consumer/cn/forum/topic/0203200053870018576?fid=0109140870620153026&pid=0314200135195141595>

当然，这个问题解决最终也是通过自绘导航栏解决的，不过目前还有个问题，就是与 uni 自带的原生导航栏样式稍微有些区别，主要问题在导航栏高度计算，以及导航栏字体渲染问题。这个如果要想彻底解决可能就得全部重写几个页面的导航栏了。这个不影响使用，稍微往后放一点。

[![](https://h4ck.org.cn/wp-content/uploads/2025/12/Screenshot-2025-12-10-123537-tuya.png)](https://h4ck.org.cn/wp-content/uploads/2025/12/Screenshot-2025-12-10-123537-tuya.png) [![](https://h4ck.org.cn/wp-content/uploads/2025/12/Screenshot-2025-12-10-123756.png)](https://h4ck.org.cn/wp-content/uploads/2025/12/Screenshot-2025-12-10-123756.png)

另外一个问题，那就是 ai 助理迁移问题，迁移到鸿蒙系统之后，由于部分属性不支持，导致页面直接白屏了。目前虽然就解决了大多数的问题，单机 markdown 渲染问题，以及聊天窗口自动滚动到最新消息依然有问题，在没有全屏的时候是没问题的，消息列表全屏之后，滚动总是少一块。

[![](https://h4ck.org.cn/wp-content/uploads/2025/12/Screenshot-2025-12-09-213814.png)](https://h4ck.org.cn/wp-content/uploads/2025/12/Screenshot-2025-12-09-213814.png)

而至于上篇文章提到的，google play 测试的问题，目前也有好多宝子参与进来了。也反馈了很多问题，当然，很多东西自己觉得习以为常，但是很多人第一次使用的时候却并没有看到相应的效果，或者对于操作步骤有疑惑。

```
记录：
1.增加异常状态种类，支持多选
2.优化日历样式
3.增加用户徽章
4.针对不同设备处理流式数据
5.优化生日选择的日期选择器
6.优化爱爱记录操作方式
7.优化日历操作方式，更简单明了 删除记录 结束记录逻辑调整
todo

todo:
个人信息–手机号，随便在那里输点东西再去修改昵称， 修改昵称那个输入框变成修改手机号的输入框了。✓
修改完手机号点一下邮箱–取消，在点击昵称 ，输入框变成修改邮箱输入框了✓
我的–高级设置–安全设置 点击密码没反应，改不了密码 ✓
青少年模式不能记录新的了，但是已经记录的💊在日历上还是显示的。
数据分析页面：
年没上限
月只有60天。而且英文界面出错提示是中文。
体重和体温也没有边界值，甚至可以输入负数。 ✓
please拼错账 pleace ✓
中文用户名长度判断问题，中文允许两个字符 ✓
```

目前已经更新发布了一版新的，并且 ios 和安卓终于版本号同步了。之前由于种种问题，ios 的版本号稍微落后了一点。

当然，正式的测试还得找个时间一起处理。多人长测的确是个问题，需要投入那么点精力。

然而，由于 google 原来的 appid 用不了了，只能换个新的 id，然而新的 id 就会出现 pushid 和 unicloud 不一致的问题，最终只能在 google 包开了 1.0 的 push 临时解决了这个问题。最终没有再搞个分支，不同的分支维护真的太麻烦了。

本来想着一套代码搞定，现在就已经拆分成了鸿蒙的 vue3 和通用版本的 vue2。修复一点问题，现在就得维护两套代码。这个也是属实是无奈之举了。

之前上架华为应用市场的版本是没有 ai 助理的，也就是一个屏蔽了 ai 助理的版本。对于这种不完美事情，总是觉得有些欠缺。继续咨询了一下相关的问题，<https://developer.huawei.com/consumer/cn/forum/topic/0203200246757472747?fid=0109140870620153026> 给出的答案倒是和之前的区别不大，意思是可以上，但是有些限制。

除了生成的内容要有明显的标识：<https://developer.huawei.com/consumer/cn/doc/app/50111-10>

另外一个就是使用这种功能需要进行实名认证：

[![](https://h4ck.org.cn/wp-content/uploads/2025/12/Jietu20251210-130933.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/12/Jietu20251210-130933.jpg)

目前看来对于这种认证最简单的侵入性最小的还是手机号认证。为了进行手机号认证，也看了几种方案，一种是基于 uni 自带的证号认证功能，

<https://doc.dcloud.net.cn/uniCloud/uni-rpia/mobile-verify/intro.html>

相关费用报价其实略贵一些：

[![](https://h4ck.org.cn/wp-content/uploads/2025/12/Jietu20251210-131618.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/12/Jietu20251210-131618.jpg)

真题来说两毛多钱一次，这价格属实是贵了点。随便认证个几百人，这几十块钱就没了。虽然不多，但是毕竟作为一个不挣钱的项目...
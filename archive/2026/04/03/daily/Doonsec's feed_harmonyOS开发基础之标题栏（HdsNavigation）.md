---
title: harmonyOS开发基础之标题栏（HdsNavigation）
url: https://mp.weixin.qq.com/s/uZEfYbAlz225OvaAIDYwOA
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:11:05.269769
---

# harmonyOS开发基础之标题栏（HdsNavigation）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/njicUbJnVlIyoQFq4rmRTN7UgKvnicS62MUemsb538dvbueawTXdDiaPhHukUo9eVmcBRcsQB71DmfiaOs7j1b3MXNtdPpwlYtEsb2XBOuoXLX0/0?wx_fmt=jpeg)

# harmonyOS开发基础之标题栏（HdsNavigation）

原创

书中自有代码来
书中自有代码来

书中自有代码来

![]()

在小说阅读器中沉浸阅读

# 一、标题栏的作用

在移动应用和桌面应用的使用中，标题栏一直发挥着不可或缺的重要作用，从早期的显示简单信息，例如：软件logo、软件名称、软件介绍等，到现今包含菜单按钮，将大量复杂的入口以图标或菜单的形式显示在标题栏，方便用户进入，标题栏一直是应用的重要组成部分，而在鸿蒙应用开发中，华为已经为我们提供了多种多样的标题栏组件方便开发者使用，让开发更加简洁高效。

# 二、几种标题栏组件

## 1.HdsNavigation的titlebar

示例代码（参考官方文档）：

```
import { HdsNavigation,  ScrollEffectType, HdsNavigationTitleMode } from'@kit.UIDesignKit';
import { LengthMetrics } from'@kit.ArkUI';

constTITLE_BAR_HEIGHT_FREE: number = 138;
@Entry
@Component
struct Index {
@Provide('pageInfos') pageInfos: NavPathStack = newNavPathStack();
scroller: Scroller = newScroller();
@StateblankHeight: number = TITLE_BAR_HEIGHT_FREE;
@StateisHideBackButton: boolean = false;
@StatetitleMode: HdsNavigationTitleMode = HdsNavigationTitleMode.FREE;
@StatesubTitle: string = 'Sub'

build() {
    HdsNavigation(this.pageInfos) {
      Column() {
        Stack() {
          Scroll(this.scroller) {
            Column() {
              Blank().height(this.blankHeight)
              Image($r('app.media.scene')).width('100%')
              Text('1')
              Image($r('app.media.scene')).width('100%')
              Text('1')
              Image($r('app.media.scene')).width('100%')
              Text('1')
              Image($r('app.media.scene')).width('100%')
              Text('1')
              Image($r('app.media.scene')).width('100%')
              Text('1')
              Image($r('app.media.scene')).width('100%')
              Text('1')
              Image($r('app.media.scene')).width('100%')
              Text('1')
              Image($r('app.media.scene')).width('100%')
            }
          }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
        }
      }
    }
    .titleBar({
      padding: {
        start: LengthMetrics.vp(2),
        end: LengthMetrics.vp(2)
      },
      style: {
        scrollEffectOpts: {
          enableScrollEffect: true,
          scrollEffectType: ScrollEffectType.COMMON_BLUR,
          blurEffectiveStartOffset: LengthMetrics.vp(0),
          blurEffectiveEndOffset: LengthMetrics.vp(20)
        },
        originalStyle: {
          backgroundStyle: {
            backgroundColor: $r('sys.color.ohos_id_color_background'),
          },
          contentStyle: {
            titleStyle: { mainTitleColor: $r('sys.color.font_primary'), subTitleColor: $r('sys.color.font_secondary') },
            menuStyle: { backgroundColor: $r('sys.color.comp_background_tertiary'), iconColor: $r('sys.color.icon_primary') },
            backIconStyle: { backgroundColor: $r('sys.color.comp_background_tertiary'), iconColor: $r('sys.color.icon_primary') }
          }
        },
        scrollEffectStyle: {
          backgroundStyle: {
            backgroundColor: $r('sys.color.ohos_id_color_background_transparent'),
          },
          contentStyle: {
            titleStyle: { mainTitleColor: $r('sys.color.font_primary'), subTitleColor: $r('sys.color.font_secondary') },
            menuStyle: { backgroundColor: $r('sys.color.comp_background_tertiary'), iconColor: $r('sys.color.icon_primary') },
            backIconStyle: { backgroundColor: $r('sys.color.comp_background_tertiary'), iconColor: $r('sys.color.icon_primary') }
          }
        }
      },
      content: {
        title: {
          mainTitle: '主标题',
          subTitle: '副标题'
        },
        menu: {
          value: [{
            content: {
              label: 'menu1',
              icon: $r('sys.symbol.ohos_wifi'),
              isEnabled: true,
              action: () => {
                console.info("HdsNavigation menu1");
              }
            }
          }, {
            content: {
              label: 'menu2',
              icon: $r('sys.symbol.plus'),
              isEnabled: true,
            }
          }, {
            content: {
              label: 'menu3',
              icon: $r('sys.symbol.lock'),
            }
          }, {
            content: {
              label: 'menu4',
              icon: $r('sys.symbol.trunk'),
            }
          }]
        },
        backIcon: {
          label: 'backButton',
          icon: $r('sys.symbol.trunk'),
          isEnabled: true,
        }
      }
    })
    .systemBarStyle({ statusBarContentColor: '#ffff0000' }, { statusBarContentColor: '#ff02025b' })
    .titleMode(this.titleMode)
    .hideBackButton(this.isHideBackButton)
    .hideTitleBar(false)
  }
}
```

界面演示：

![](https://mmbiz.qpic.cn/mmbiz_png/njicUbJnVlIzg6F3wUIiarIKV6CvZ79LdSCR1yFOUBJxCur0bOGacicvR1lD2LOJpxZugnUZfyJLZhKNZWSFuRAwBxxAbtuiaK9ib3nEfBibSVQes/640?wx_fmt=png&from=appmsg)

1. titlebar属性

代码部分：

```
.titleBar({
      padding: {
        start: LengthMetrics.vp(2),
        end: LengthMetrics.vp(2)
      },
      style: {
        scrollEffectOpts: {
          enableScrollEffect: true,
          scrollEffectType: ScrollEffectType.COMMON_BLUR,
          blurEffectiveStartOffset: LengthMetrics.vp(0),
          blurEffectiveEndOffset: LengthMetrics.vp(20)
        },
        originalStyle: {
          backgroundStyle: {
            backgroundColor: $r('sys.color.ohos_id_color_background'),
          },
          contentStyle: {
            titleStyle: { mainTitleColor: $r('sys.color.font_primary'), subTitleColor: $r('sys.color.font_secondary') },
            menuStyle: { backgroundColor: $r('sys.color.comp_background_tertiary'), iconColor: $r('sys.color.icon_primary') },
            backIconStyle: { backgroundColor: $r('sys.color.comp_background_tertiary'), iconColor: $r('sys.color.icon_primary') }
          }
        },
        scrollEffectStyle: {
          backgroundStyle: {
            backgroundColor: $r('sys.color.ohos_id_color_background_transparent'),
          },
          contentStyle: {
            titleStyle: { mainTitleColor: $r('sys.color.font_primary'), subTitleColor: $r('sys.color.font_secondary') },
            menuStyle: { backgroundColor: $r('sys.color.comp_background_tertiary'), iconColor: $r('sys.color.icon_primary') },
            backIconStyle: { backgroundColor: $r('sys.color.comp_background_tertiary'), iconColor: $r('sys.color.icon_primary') }
          }
        }
      },
      content: {
        title: {
          mainTitle: '主标题',
          subTitle: '副标题'
        },
        menu: {
          value: [{
            content: {
              label: 'menu1',
              icon: $r('sys.symbol.ohos_wifi'),
              isEnabled: true,
              action: () => {
                console.info("HdsNavigation menu1");
              }
            }
          }, {
            content: {
              label: 'menu2',
              icon: $r('sys.symbol.plus'),
              isEnabled: true,
            }
          }, {
            content: {
              label: 'menu3',
              icon: $r('sys.symbol.lock'),
            }
          }, {
            content: {
              label: 'menu4',
              icon: $r('sys.symbol.trunk'),
            }
          }]
        },
        backIcon: {
          label: 'backButton',
          icon: $r('sys.symbol.trunk'),
          isEnabled: true,
        }
      }
    })
```

> 参数：
>
> | 名称 | 可选 | 说明 |
> | --- | --- | --- |
> | padding | 是 | 标题栏内间距设置。 |
> | style | 是 | 标题栏样式设置。 |
> | content | 是 | 标题栏内容区设置。 |
> | enableHoverMode | 是 | 是否响应悬停态。 |
> | avoidLayoutSafeArea | 是 | 是否需要标题栏主动避让安全区。 |
> | enableComponentSafeArea | 是 | 是否将标题栏设置为组件级安全区。 |
>
> content设置：
>
> | 名称 | 可选 | 说明 |
> | --- | --- | --- |
> | title | 是 | 设置标题栏标题内容。 |
> | menu | 是 | 设置标题栏菜单栏内容。 |
> | backIcon | 是 | 设置标题栏的返回按钮内容。 |
> | stackBuilder | 是 | 设置标题栏顶部自定义区域。 |
> | stackBuilderComponent | 是 | 设置标题栏顶部自定义区域。 |
> | bottomBuilder | 是 | 设置标题栏底部自定义区域。 |
> | divider | 是 | 设置标题栏分割线内容。 |
> | subIcon | 是 | 设置标题栏子图标内容。 |
>
> title中使用mainTitle设置主标题的内容，使用subTitle设置副标题内容。

---

> menu中使用value数组配...
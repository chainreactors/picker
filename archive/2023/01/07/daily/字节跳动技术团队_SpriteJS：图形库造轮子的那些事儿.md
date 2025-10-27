---
title: SpriteJS：图形库造轮子的那些事儿
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247501068&idx=1&sn=4839629ea06fa805b24196105f3e14c7&chksm=e9d30eeedea487f8fbae2564d764b525fef669df5613e46294d6a6a28e1edd7a341dec728c61&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2023-01-07
fetch_date: 2025-10-04T03:16:59.372173
---

# SpriteJS：图形库造轮子的那些事儿

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5EcwYhllQOhwC5lK1ic0GHQMD0a5depTrrdqRpCs0bYIlcD2I63GqMFQiaI13lsUib6o3icgJ3TYQE71ZtNMF6mnOw/0?wx_fmt=jpeg)

# SpriteJS：图形库造轮子的那些事儿

吴亮（月影）

字节跳动技术团队

**动手点关注**

**![](https://mmbiz.qpic.cn/mmbiz_gif/JaFvPvvA2J063TNzibibGfI89U9UaWNPqYGUFNRVJ1TkA4Bv0Ew946EkhX4dNibLx6ZK9E4ibdtqH01ZGs9a4gvo4w/640?wx_fmt=gif)**

**干货不迷路**

从 2017 年到 2020 年，我花了大约 4 年的时间，从零到一，实现了一个可切换 WebGL 和 Canvas2D 渲染的，跨平台支持浏览器、SSR、小程序，基于 DOM 结构和支持响应式的，高性能支持批量渲染、针对可视化场景优化、支持 WebWorker 的图形系统——SpriteJS。

在这个“造轮子”过程中，我一步步将一个很简陋的渲染库，变成一个能够支撑可视化应用和游戏开发的，还算不错的一个图形库，其中有许多积累，也有许多思考。因为毕竟是两年多前的研究，有些细节可能记得不是特别清晰，其中有些特性也许已经有点过时，但我想，还是有不少内容能给大家带来参考和启发。

# 1. 原始需求：和渲染无关

2017 年底的时候，我还在奇虎 360 负责奇舞团。奇舞团是一个中台前端团队，支持很多 360 的业务需求，其中包括一些 toB 的需求，这些需求中有不少可视化图表和态势感知大屏。大概在 2015-2016 年，我们的同学就开始用 D3 来完成可视化项目，因为 D3 具有很高的灵活性。有些同学将 D3 简单归类为一种可视化渲染框架，实际上这种想法是错误的。D3 并不是可视化框架，而是一个数据驱动引擎。

严格来说，D3 关心的是数据的组织，它并不关心数据最终渲染的结果，但是，D3 的数据组织形式是基于树状结构的，因为它天然契合树状结构的渲染形式。正因为如此，所以一般来说，D3 的官方例子都是用 DOM 或 SVG 渲染，这是因为基于 DOM 树的渲染和 D3 的树状数据组织形式是绝配。

* 使用 DOM 渲染的 D3 柱状图：

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhwC5lK1ic0GHQMD0a5depTrQ0nE1hkt37uEEhpJHqoIXAE1IiaLicBazdyJibXGx1504bCAZCxCB2yiag/640?wx_fmt=png)

*查看代码：https://code.juejin.cn/pen/7160491257892962339*

* 使用 SpriteJS 渲染：

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhwC5lK1ic0GHQMD0a5depTrQ0nE1hkt37uEEhpJHqoIXAE1IiaLicBazdyJibXGx1504bCAZCxCB2yiag/640?wx_fmt=png)

*查看代码：https://code.juejin.cn/pen/7160553901123436557*

## 1.1  与 DOM 的一致性

为了达到上面的效果，SpriteJS 参考浏览器 DOM API，进行了适配：

* *https://github.com/spritejs/spritejs/blob/master/src/node/node.js*
* *https://github.com/spritejs/spritejs/blob/master/src/node/group.js*
* *https://github.com/spritejs/spritejs/blob/master/src/attribute/node.js*
* *https://github.com/spritejs/spritejs/blob/master/src/document/index.js*
* *https://github.com/spritejs/spritejs/blob/master/src/selector/index.js*

## 1.2  SpriteJS & DOM & D3

理论上，操作 SpriteJS 元素和操作 DOM 元素完全一样，二者差异极小。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhwC5lK1ic0GHQMD0a5depTrnibER4oiceJIAakjl6wLiba0bNgyJyjA8GtjHicnHdaPibWejtG2E736o1Q/640?wx_fmt=png)

*查看代码：https://code.juejin.cn/pen/7160568056672944159*

这种一致性使得 SpriteJS 完全可以和 D3 配合使用，灵活解决非常复杂的可视化问题：*http://spritejs.com/#/zh-cn/guide/d3*

# 2.  设计一个图形系统的“骨架”

## 2.1  坐标系的选择

在图形系统的设计中，首先要确定默认坐标系。理论上讲，任何一种直角坐标系，甚至非直角坐标系（比如极坐标）都可以作为默认坐标系，在欧式几何中，这些坐标系都可以自由转换。不过，考虑与 DOM 的一致性，采用浏览器默认的坐标系是一个极好的选择。

对于 WebGL 渲染来说，我们需要将顶点坐标转换成 WebGL 坐标，在这里，我们采用根据 canvas 的坐标动态设置 projectionMatrix 即可：*https://github.com/mesh-js/mesh.js/blob/master/src/renderer.js#L181*

```
updateResolution() {
  const {width, height} = this.canvas;
  const m1 = [ // translation
    1, 0, 0,
    0, 1, 0,
    -width / 2, -height / 2, 1,
  ];
  const m2 = [ // scale
    2 / width, 0, 0,
    0, -2 / height, 0,
    0, 0, 1,
  ];
  const m3 = mat3(m2) * mat3(m1);
  this.projectionMatrix = m3;
  if(this[_glRenderer]) {
    this[_glRenderer].gl.viewport(0, 0, width, height);
  }
}
```

```
attribute vec3 a_vertexPosition;
attribute vec3 a_vertexTextureCoord;
varying vec3 vTextureCoord;
uniform mat3 viewMatrix;
uniform mat3 projectionMatrix;
void main() {
  gl_PointSize = 1.0;
  vec3 pos = projectionMatrix * viewMatrix * vec3(a_vertexPosition.xy, 1.0);
  gl_Position = vec4(pos.xy, 1.0, 1.0);
  vTextureCoord = a_vertexTextureCoord;
}
```

## 2.2  图层、树形结构与元素类型

SpriteJS 用 Scene 表示场景，一个 Layer 表示一个图层，在这里，我的设计是一个 Layer 对应一个画布，即默认每个 Layer 都是独立的 Canvas 元素。这么做有优点也有缺点，是一种设计上的取舍。

优点是，每个 Layer 彼此独立，Layer 间不必考虑绘制次序，可以充分利用 WebWorker 这样的多线程来并行绘制，而且逻辑上比较简单，如果需要在多层响应事件，只需要注意事件处理的次序。缺点是如果分多层绘制，有可能产生较多 Canvas 对象实例，比较耗内存。

* 多线程绘制

![](https://mmbiz.qpic.cn/mmbiz_jpg/5EcwYhllQOhwC5lK1ic0GHQMD0a5depTriaMF65nwLwwdphsEiaK6IEdbLWNsfdJicLhd8ciao6h2TVUQegIibZvzqeQ/640?wx_fmt=jpeg)

*查看代码：https://code.juejin.cn/pen/7089291575993303071*

前面说过，SpriteJS 采用类似树状结构来管理元素，Scene、Layer 和 Group 都是容器，而其他类型的图形元素挂载在容器上。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhwC5lK1ic0GHQMD0a5depTr0S6aAA8qglPb3a0stPghkupWglJU237TBasGAXmyCd0molkb6kZetw/640?wx_fmt=png)

SpriteJS 的元素类型比较多，一共有超过十五种图形元素，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhwC5lK1ic0GHQMD0a5depTrDKzcc1dTJdPOT3rVswaF1bQ5YvGialzzUQpjaxufwxniamMyu9cgr83g/640?wx_fmt=png)

这些元素可以分为两类，一类是 Block 元素，包括 Sprite、Label 和 Group，一类是 Path 元素，包括各种图形。这两类元素中，Block 比较类似于 DOM 元素，占据矩形区域，有盒模型，有 border、padding、margin，可以计算大小；Path 比较类似于 SVG 元素，通过 Path2D 构成矢量形状，有 stroke 和 fill 两类渲染，但不计算大小（不管 Path 还是 Block 都能计算 boundingClientRect）。

Group 比较特殊，SpriteJS v3 里，它默认不计算大小，但继承它的 Layer 和 Scene 会计算大小。在 v2 中，Group 计算大小，而且能够做区域剪裁和设置 clipPath。v3 里，Group 主要的作用是给分组元素设置统一的 transform。之所以这样设计，牵扯到 WebGL 的渲染模型。在后续会详细解释。

考虑到扩展性，用户可以通过 spritejs.registerNode 注册自定义节点元素。*https://github.com/spritejs/spritejs/blob/master/src/document/index.js#L15*

registerNode 的作用是注册一个唯一的 nodeName 到 spritejs 的文档树上，这样节点挂载之后，通过 getElementById、querySelector 等等就可以找到这个节点。

## 2.3  属性更新和重绘机制

SpriteJS 与一般的图形库不同，通常情况下，一般的图形库会使用一个动画定时器来以固定帧率刷新画布。但 SpriteJS 采用的是属性变化时的异步更新机制。

* *https://github.com/spritejs/spritejs/blob/master/src/attribute/node.js#L190*
* *https://github.com/spritejs/spritejs/blob/master/src/node/node.js#L430*

具体原理如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhwC5lK1ic0GHQMD0a5depTrOahqUCiaWgtNM9yZnCZLooaGj93E3NHicVrEMQuU4oyZAK01emD5XB4A/640?wx_fmt=png)

这里有些需要注意的细节：

1. 不是所有的属性改变都会触发 render，比如 className、ID 等改变不会触发。
2. 有些属性改变不仅触发 render，还需要触发其他操作，比如 anchor、border 等属性的变化，需要重新计算图形元素的轮廓（后面会讲）；zIndex 的变化，导致对 group 的 children 的 renderOrder 进行重排。

这样设计的好处显而易见，可以尽量减少不必要的重绘和其他计算，从而提高整体性能。

## 2.4  外部 Ticker

虽然 SpriteJS 有自己的更新机制，但是一些外部库，比如 ThreeJS 或者 ClayGL，有自己的更新逻辑，所以 SpriteJS 增加了手动控制的设计，以方便与外部库配合。*http://spritejs.com/#/zh-cn/guide/ticker*

## 2.5  跨平台

SpriteJS 在实现的时候，尽量不使用浏览器原生提供的能力，除非是标准的 Canvas 和 WebGL API。针对浏览器、NodeJS、微信小程序、微信小游戏等不同的环境，通过 polyfill 进行适配。*https://github.com/spritejs/spritejs/tree/master/src/platform*

为了在 NodeJS 中集成 WebGL 和 Canvas 环境，做了下面这个库：*https://github.com/akira-cn/node-canvas-webgl*

# 3.  盒模型、事件、动画等

## 3.1  盒模型设计

对 Block 类型的元素，SprteJS 采用标准的 DOM 盒模型，可以设置 border、padding 各属性，并可以通过 boxSizing 属性切换盒模型方式。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhwC5lK1ic0GHQMD0a5depTruMkle3psCKziaC58cSNlOKS4ds31EEwz5fBP8xvRb1SfDNL6PwmicWag/640?wx_fmt=png)

*查看代码：https://code.juejin.cn/pen/7160923382119137317*

## 3.2 事件机制

* 事件模型、坐标转换

*https://github.com/spritejs/spritejs/blob/master/src/event/event.js*

**https://github.com/spritejs/spritejs/blob/master/src/event/pointer-events.js**

视口宽高：[viewportWidth, viewportHeight]

画布宽高：[resolutionWidth, resolutionHeight]

偏移量：[offsetLeft, offsetTop]

为什么会产生偏移量，详细见屏幕适配。

* 事件派发和命中

  *https://github.com/spritejs/spritejs/blob/master/src/node/layer.js#L179*

  *https://github.com/spritejs/spritejs/blob/d8d7b8f232fe3c44ace11c5775892371bed44a1e/src/node/node.js#L419*

  *https://github.com/mesh-js/mesh.js/blob/master/src/mesh2d.js#L840*

采用对每个三角网格进行命中检测（此处有优化空间，可以先排序用二分查找快速确定范围）：

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhwC5lK1ic0GHQMD0a5depTrnuDBYcmf4fqTBPp6Eln1DNtzqEOdPYZiby2pSGjS5B6yqPR4p2pGwhw/640?wx_fmt=png)

```
function inTriangle(p1, p2, p3, point) {
  const a = p2.copy().sub(p1);
  const b = p3.copy().sub(p2);
  const c = p1.copy().sub(p3);

  const u1 = point.copy().sub(p1);
  const u2 = point.copy().sub(p2);
  const u3 = point.copy().sub(p3);

  const s1 = Math.sign(a.cross(u1));
  let p = a.dot(u1) / a.length ** 2;
  if(s1 === 0 && p >= 0 && p <= 1) return true;

  const s2 = Math.sign(b.cross(u2));
  p = b.dot(u2) / b.length ** 2;
  if(s2 === 0 && p >= 0 && p <= 1) return true;

  const s3 = Math.sign(c.cross(u3));
  p = c.dot(u3) / c.length ** 2;
  if(s3 === 0 && p >= 0 && p <= 1) return true;

  return s1 === s2 && s2 === s3;
}
```

## 3.3  动画的设计

* Sprite-Timeline

  *https://github.com/spritejs/sprite-timeline*

为了实现可以在时间轴按照任意速度播放动画，包括正向播放和回放，在任意时间点可以跳跃，实时切换播放状态和时间轴状态，设计了 sprite-timeline 库。

这个库的设计是：

1. 创建一个 Timeline 对象，它基于当前时间线和 playbackRate 来计算时间，playbackRate 可以是任意数，所以时间可以停止，也可以回溯。playbackRate 的设置和改变会影响 Timeline 对象的 currentTime。
2. 除了 currentTime 属性，Timeline 对象还有一个 entropy（熵）属...
---
title: 用原生 JS 开发编程游戏”机器人流水线“
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247501656&idx=1&sn=7dd306d6fcca578f733836cbf9ab5fc5&chksm=e9d30cbadea485acbca157bac6095d135009146b6c4d1d1d586856ecc1524f1bce81473c0f7f&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2023-03-08
fetch_date: 2025-10-04T08:56:20.540889
---

# 用原生 JS 开发编程游戏”机器人流水线“

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5EcwYhllQOgdjMlua3qSGk0EjMpialI5hXY18mPiasvc8NzbvQWbAKtNibE6V0X90Eic1Y2vkZwPfMftZ79tibj66hQ/0?wx_fmt=jpeg)

# 用原生 JS 开发编程游戏”机器人流水线“

吴亮（月影）

字节跳动技术团队

**动手点关注**

**![](https://mmbiz.qpic.cn/mmbiz_gif/JaFvPvvA2J063TNzibibGfI89U9UaWNPqYGUFNRVJ1TkA4Bv0Ew946EkhX4dNibLx6ZK9E4ibdtqH01ZGs9a4gvo4w/640?wx_fmt=gif)**

**干货不迷路**

记得之前玩过一个 flash 编程小游戏，印象深刻，叫“机器人流水线(manufactoria)”，不知道有没有同学也玩过。可惜的是，现在 falsh 已经停止运行了，这个原版的小游戏无法体验到。

![](https://mmbiz.qpic.cn/mmbiz_png/lP9iauFI73zibAPwRoue7SCkco8lTl62Ru4pO9W8S9OjLSlS9wIoI2yTJUbQ1oE0mlLjvF0bibjhYWH3NzBGialoXg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

不过最近几天，我凭着之前的印象，复刻出了这个小游戏。（戳左下方“阅读原文”立即体验）

![](https://mmbiz.qpic.cn/mmbiz_gif/lP9iauFI73zibAPwRoue7SCkco8lTl62Ru8FqMSzQXm2doAeic5QUicpbcjLGE2YL9pIGhicQpZLS9ibPsmQAvy5mtXw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

这个小游戏的规则是，将左侧的元件放置到右侧的面板上，然后点击运行，机器人会沿着元件指定的路径运行，并影响地步序列的状态，最终按照任务的要求完成，即可过关。

例如上面的截图是第五关，任务是“队列里不能出现不同颜色的球”，也就是说如果队列中只有红球或只有蓝球，要把机器人移动到 🚩 处，否则将机器人移到任意其他空格。

我们能将元件放置到在任意白色空格处，机器人走到元件上会根据元件的类型来产生相应的动作。

manufactoria 的元件非常简单，只有两种类型：传送器和比较器，但根据不同的作用一共分为 7 种：

![](https://mmbiz.qpic.cn/mmbiz_png/lP9iauFI73zibAPwRoue7SCkco8lTl62RuoPUBjOBKMMyR3tYPzbgfhn5JeyP2TGr7DLh0OaHC4Q83E8f6fRibkRg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

其中传送器有五种，四种带颜色的，机器人通过的时候会将对应颜色的球添加到序列的末尾，还有最后一种黑色的，机器人通过，序列不变。

比较器有两种，分别是红蓝比较器和黄绿比较器。比较器的作用是，当机器人通过它时，判断序列头部的球颜色，若颜色是比较器允许的颜色，则机器人朝对应的加号方向前进，并将该序列头部的这个球取出，否则，机器人沿着弧形箭头方向前进，且序列保持不变。

神奇的是有了这些简单的元件，我们就可以让机器人完成复杂的任务了。而且这和编程思想是一致的，我们可以通过元件构建出顺序，选择和循环结构体！

如下图，在第 22 关，可以用绿色小球构建出循环体解决问题：

![](https://mmbiz.qpic.cn/mmbiz_png/lP9iauFI73zibAPwRoue7SCkco8lTl62RuHFMUr8M7I9PER1FFfmDYIL6dIOhKNdgFliaHTAicRSjiahtib3JfcaA05A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

---

好了，前面说了规则，有兴趣的同学可以自行挑战，目前有 20 多个关卡，我会不定期更新新的关卡，等待大家的挑战。

接下来，我们看一下游戏是怎么实现的。

首先是面板的 HTML 结构，这个结构非常简单：

```
<div>🤖🔴🟡🔵🟢🚩 <span>第 <select id="levelPicker"><option>1</option></select> 关</span></div>
<div id="main">
  <div id="panel">
    <div class="buttons">
      <div class="pass green" title="绿色通道：🤖通过时将🟢添加到序列尾部" data-turn=0 data-flip=0></div>
      <div class="pass yellow" title="黄色通道：🤖通过时将🟡添加到序列尾部" data-turn=0 data-flip=0></div>
      <div class="comparator green yellow" title="黄绿比较器：🤖通过时读取序列头部元素根据颜色判断路径" data-turn=0 data-flip=0></div>
      <div class="pass red" title="红色通道：🤖通过时将🔴添加到序列尾部" data-turn=0 data-flip=0></div>
      <div class="pass blue" title="蓝色通道：🤖通过时将🔵添加到序列尾部" data-turn=0 data-flip=0></div>
      <div class="comparator red blue" title="红蓝比较器：🤖通过时读取序列头部元素根据颜色判断路径" data-turn=0 data-flip=0></div>
      <div class="pass" title="通道" data-turn=0 data-flip=0></div>
      <div class="trash" title="清除"></div>
    </div>
    <div class="info">
      说明：鼠标选择上方元件添加到右侧面板中，键盘上下左右旋转，空格翻转。
    </div>
    <div class="task" id="taskInfo"></div>
    <div class="run">
      <button class="btn" id="runBtn"></button>
      <button class="btn" id="stopBtn"></button>
    </div>
  </div>
  <div>
    <div id="app"></div>
    <div id="io">序列 ← <i>❤️</i><i>💙</i></div>
    <div id="result">结果 → </div>
  </div>
  </div>
  <div id="mousePick">
</div>
```

在这里我就不多说了，元件是通过 CSS 样式绘制的，比如比较器：

```
.comparator {
  margin: 10px 20px;
  border-bottom-right-radius: 50%;
  border-bottom-left-radius: 50%;
}
.comparator::before {
  content: '+';
  margin-left: -10px;
}
.comparator::after {
  content: '+';
  margin-left: 10px;
}

.comparator.red::before {
  color: red;
}
.comparator.green::before {
  color: green;
}

.comparator.blue::after {
  color: blue;
}
.comparator.yellow::after {
  color: orange;
}
```

因为所有的元件结构都不复杂，所以用一个 HTML 标签，加上 before 和 after 伪元素，就完全可以绘制出来的。

右侧的网格是一个 grid 布局的棋盘：

```
#app {
  width: 520px;
  height: 520px;
  border-bottom: solid 1px #0002;
  border-right: solid 1px #0002;
  background-image: linear-gradient(90deg, rgba(0, 0, 0, 0.15) 2.5%, transparent 2.5%), linear-gradient( rgba(0, 0, 0, 0.15) 2.5%, transparent 2.5%);
  background-size: 40px 40px;
  background-repeat: repeat;
  display: grid;
  grid-template-columns: repeat(13, 40px);
  grid-template-rows: repeat(13, 40px);
}

#app > div {
  text-align: center;
  font-size: 1.8rem;
  line-height: 48px;;
}
```

在网格中添加对应的元件，就只要找到对应的格子往里添加指定类型的元素就可以了。

机器人是绝对定位的元素，它移动的时候的动画效果可以通过 transition 给出：

```
#robot {
  position: absolute;
  transition: all linear .2s;
}

#robot::after {
  font-size: 1.8rem;
  content: '🤖';
  margin: 5px;
}
```

这样，基本的 HTML 和 CSS 就实现完成了。实际上，大部分 UI 和交互效果都可以通过 HTML 和 CSS 指定，让 JS 只需要负责控制逻辑，这样就简单很多。

接下来我们看具体的逻辑。

首先我们实现一个点击左侧面板的元件，将元件用鼠标拾取的效果：

```
unction enablePicker() {
  const buttons = panel.querySelector('.buttons');
  buttons.addEventListener('mousedown', ({target}) => {
    if(main.className !== 'running' && target !== buttons && target.className) {
      const node = target.cloneNode(true);
      mousePick.innerHTML = '';
      mousePick.appendChild(node);
    }
  });
  window.addEventListener('mousemove', ({x, y}) => {
    mousePick.style.left = `${x - 25}px`;
    mousePick.style.top = `${y - 25}px`;
  });
  window.addEventListener('contextmenu', (e) => {
    e.preventDefault();
    return false;
  });
  window.addEventListener('mouseup', ({target}) => {
    if(target.parentNode !== buttons && target.className !== 'normal') {
      mousePick.innerHTML = '';
    }
  });
  window.addEventListener('keydown', ({key}) => {
    const el = mousePick.children[0];
    if(!el || el.className === 'trash') return;
    if(key === 'ArrowRight') {
      el.dataset.turn = 0;
    } else if(key === 'ArrowDown') {
      el.dataset.turn = 1;
    } else if(key === 'ArrowLeft') {
      el.dataset.turn = 2;
    } else if(key === 'ArrowUp') {
      el.dataset.turn = 3;
    } else if(key === ' ') {
      let n = Number(el.dataset.flip) || 0;
      el.dataset.flip = ++n % 2;
    }
    if(key.startsWith('Arrow') && el.classList.contains('comparator')) {
      el.dataset.turn = (Number(el.dataset.turn) + 3) % 4;
    }
  });
}
```

这里，我们直接用 cloneNode，将面板上的元素复制出来，做出一个透明效果，跟随鼠标移动。另外，我们还做了键盘控制，通过键盘控制元件的具体方向：

![](https://mmbiz.qpic.cn/mmbiz_gif/lP9iauFI73zibAPwRoue7SCkco8lTl62Rue5IREddhsbF0OIKVcl1zu3bnDSRAftjrqYMclzebHKPFI0mqv1CVOA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

注意，我们用 JS 控制元素方向的时候，通过设置 turn 和 flip 来表示元素翻转，至于元素具体的展现，则通过 CSS 来定义：

```
*[data-turn="1"] {
  transform: rotate(.25turn);
}
*[data-turn="2"] {
  transform: rotate(.5turn);
}
*[data-turn="3"] {
  transform: rotate(.75turn);
}

*[data-flip="1"] {
  transform: scale(-1, 1);
}
*[data-turn="1"][data-flip="1"] {
  transform: rotate(.25turn) scale(-1, 1);
}
*[data-turn="2"][data-flip="1"] {
  transform: rotate(.5turn) scale(-1, 1);
}
*[data-turn="3"][data-flip="1"] {
  transform: rotate(.75turn) scale(-1, 1);
}
```

接着是设置和移动机器人的函数：

```
function setRobot() {
  const start = app.querySelector('.start');
  const row = Number(start.dataset.x);
  const col = Number(start.dataset.y);
  let {x, y} = app.getBoundingClientRect();
  x = x + col * 40;
  y = y + row * 40;
  const el = document.getElementById('robot') || document.createElement('div');
  el.id = 'robot';
  el.style.left = `${x}px`;
  el.style.top = `${y}px`;
  el.dataset.x = x;
  el.dataset.y = y;
  el.dataset.row = row;
  el.dataset.col = col;
  el.dataset.fromDirection = '';
  document.body.appendChild(el);
}

function moveRobot(direction) {
  let x = Number(robot.dataset.x);
  let y = Number(robot.dataset.y);
  let row = Number(robot.dataset.row);
  let col = Number(robot.dataset.col);
  let fromDirection = '';
  if(direction === 'left') {
    x -= 40;
    col--;
    fromDirection = 'right';
  } else if(direction === 'right') {
    x += 40;
    col++;
    fromDirection = 'left';
  } else if(direction === 'up') {
    y -= 40;
    row--;
    fromDirection = 'down';
  } else if(direction === 'down') {
    y += 40;
    row++;
    fromDirection = 'up';
  }
  robot.style.left = `${x}px`;
  robot.style.top = `${y}px`;
  robot.dataset.x = x;
  robot.dataset.y = y;
  robot.dataset.row = row;
  robot.dataset.col = col;
  robot.dataset.fromDirection = fromDirection;
  // console.log(row, col...
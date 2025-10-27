---
title: Nezha V1：哪吒监控自定义代码美化
url: https://blog.upx8.com/4652
source: 黑海洋 - IT技术知识库
date: 2025-01-14
fetch_date: 2025-10-06T20:10:42.480991
---

# Nezha V1：哪吒监控自定义代码美化

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Nezha V1：哪吒监控自定义代码美化

发布时间:
2025-01-13

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
66003

## 介绍

NezhaDash 是一个基于 **Next.js** 和 **哪吒监控** 的仪表盘，通过简洁的布局带来更好的体验。

初始模版有点单调，我们给它润色下，美化下UI界面。

Nezha官方文档：[https://nezhadash-docs.buycoffee.top/custom-code](https://blog.upx8.com/go/aHR0cHM6Ly9uZXpoYWRhc2gtZG9jcy5idXljb2ZmZWUudG9wL2N1c3RvbS1jb2Rl)

服务器公开备注生成器：[https://nezhainfojson.pages.dev/](https://blog.upx8.com/go/aHR0cHM6Ly9uZXpoYWluZm9qc29uLnBhZ2VzLmRldi8)

哪吒监控json配置生成工具：[https://nzcfg.pages.dev/](https://blog.upx8.com/go/aHR0cHM6Ly9uemNmZy5wYWdlcy5kZXYv)

特效项目：[https://github.com/mocchen/cssmeihua/](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL21vY2NoZW4vY3NzbWVpaHVhLw)

## 效果截图

![](https://i0.wp.com/cdn.skyimg.de/up/2025/1/13/0s3wc5.webp)

## 自定义代码（图片背景）

```
<script>
// 全局配置参数
window.CustomBackgroundImage = "https://wp.upx8.com/api.php";    // 设置页面背景图片，调用了黑海洋随机壁纸
window.CustomLogo = "https://i0.wp.com/cdn.skyimg.de/up/2025/1/13/zera6q.webp";  // 设置自定义logo
window.ShowNetTransfer = "true";    // 开启卡片上下行流量显示
window.DisableAnimatedMan = "true";  // 关闭默认动画人物
window.CustomDesc = "放养鸡，不吃饲料，天然无危害！";  // 设置自定义描述文本

// 更换卡通小人函数
function updateCartoonCharacter() {
    // 卡通小人的配置信息
    const CARTOON_CONFIG = {
        xpath: "/html/body/div/div/main/div[2]/section[1]/div[4]/div",  // 卡通小人容器的XPath
        imageUrl: "https://i0.wp.com/cdn.skyimg.de/up/2025/1/13/zera6q.webp",     // 卡通小人图片地址
        styles: {
            position: "absolute",
            right: "8px",
            top: "-80px",
            zIndex: "10",
            width: "90px"
        }  // 卡通小人的样式配置
    };

    // 创建DOM观察器，用于监听页面变化
    const observer = new MutationObserver((mutations, obs) => {
        // 查找卡通小人的容器元素
        const container = document.evaluate(
            CARTOON_CONFIG.xpath,
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null
        ).singleNodeValue;

        if (container) {
            obs.disconnect();  // 找到容器后停止观察
            // 移除已存在的图片（如果有）
            const existingImg = container.querySelector("img");
            if (existingImg) {
                existingImg.remove();
            }

            // 创建并添加新的卡通小人图片
            const imgElement = document.createElement("img");
            imgElement.src = CARTOON_CONFIG.imageUrl;
            Object.assign(imgElement.style, CARTOON_CONFIG.styles);
            container.appendChild(imgElement);
        }
    });

    // 开始观察页面DOM变化
    observer.observe(document.body, { childList: true, subtree: true });
}

// 异步加载JavaScript脚本的工具函数
function loadScript(src) {
    return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = src;
        script.onload = resolve;    // 脚本加载成功时解析Promise
        script.onerror = reject;    // 脚本加载失败时拒绝Promise
        document.head.appendChild(script);
    });
}

// 初始化所有特效的函数
async function initializeEffects() {
    // 创建鼠标特效的容器元素
    const cursorContainer = document.createElement('span');
    cursorContainer.className = 'js-cursor-container';
    document.body.appendChild(cursorContainer);

    // 需要加载的特效脚本列表
    const effectScripts = [
        'https://testingcf.jsdelivr.net/gh/mocchen/cssmeihua/js/aixin.js',      // 点击爱心特效
        'https://testingcf.jsdelivr.net/gh/mocchen/cssmeihua/js/yinghua.js',    // 樱花飘落特效
        'https://testingcf.jsdelivr.net/gh/mocchen/cssmeihua/js/xiaoxingxing.js'// 鼠标跟随特效
    ];

    // 按顺序加载所有特效脚本
    try {
        for (const scriptSrc of effectScripts) {
            await loadScript(scriptSrc);
        }
    } catch (error) {
        console.error('加载特效脚本失败:', error);
    }

    // 初始化卡通小人
    updateCartoonCharacter();
}

// 在适当的时机初始化所有特效
if (document.readyState === 'loading') {
    // 如果页面还在加载中，等待DOM加载完成后初始化
    document.addEventListener('DOMContentLoaded', initializeEffects);
} else {
    // 如果页面已经加载完成，直接初始化
    initializeEffects();
}
</script>
```

## 自定义代码（视频背景）

```
<meta name="referrer" content="no-referrer">
<div class="video-box">
  <video id="myVideo" muted src="https://img.028029.xyz/1734966841908.mp4" autoplay playsinline loop></video>
</div>

<style>
  :root {
    --custom-bg-opacity: rgba(13, 11, 9, 0.4);
    --custom-border: rgba(13, 11, 9, 0.1);
    --text-color: #f4f5f6;
  }

  .video-box {
    position: fixed;
    inset: 0;
    z-index: 1;
  }

  .video-box video {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .dark {
    /* 基础样式 */
    color: var(--text-color);
    background: unset;
  }

  .dark .bg-card,
  .dark .max-w-5xl.gap-4>div:first-child {
    background-color: var(--custom-bg-opacity);
    backdrop-filter: blur(4px);
    border: 1px solid var(--custom-border);
    box-shadow: 0 4px 6px rgba(13, 11, 9, 0.2);
    border-radius: 12px;
    padding: 12px;
  }

  /* 文字颜色统一处理 */
  .dark .text-muted-foreground,
  .dark\:text-stone-400:is(.dark *),
  .\[\&_\.recharts-cartesian-axis-tick_text\]\:fill-muted-foreground .recharts-cartesian-axis-tick text,
  .dark\:fill-neutral-800:is(.dark *) {
    color: #fff;
  }

  /* 背景透明度统一处理 */
  .dark\:bg-stone-700:is(.dark *),
  .dark\:bg-stone-800:is(.dark *) {
    --tw-bg-opacity: 0.5;
    background-color: rgb(41 37 36 / var(--tw-bg-opacity));
  }

  /* 边框颜色统一 */
  html.dark *,
  .dark\:border-neutral-800:is(.dark *),
  .dark .border-input {
    border-color: var(--custom-border);
  }

  /* 移除不必要的背景 */
  .dark #root,
  .dark .bg-secondary,
  .dark .bg-popover {
    background-color: unset !important;
  }

  /* 弹窗背景 */
  div#radix-\:r4\: {
    background: rgba(0, 0, 0, 0.7);
  }

  /* 其他必要样式 */
  .text-green-600 { color: rgb(34, 197, 94); }
  .bg-green-600 { background-color: rgb(34, 197, 94); }
  img[alt="BackIcon"] { margin-right: 12px; }
</style>

<script>
const config = {
    mobileBackground: "https://img.028029.xyz/1734664417905.png",
    logo: "https://img.028029.xyz/1734533172211.png",
    showNetTransfer: "true",
    desc: "MJJ：白嫖至上，技术先行",
    illustration: "https://img.028029.xyz/1734664224123.png",
    theme: "dark"
};

// 设置全局配置
Object.entries(config).forEach(([key, value]) => {
    window[`Custom${key.charAt(0).toUpperCase() + key.slice(1)}`] = value;
});

// 添加插图
new MutationObserver((mutations, observer) => {
    const container = document.evaluate(
        "/html/body/div/div/main/div[2]/section[1]/div[4]/div",
        document,
        null,
        XPathResult.FIRST_ORDERED_NODE_TYPE,
        null
    ).singleNodeValue;

    if (container) {
        observer.disconnect();
        container.querySelector("img")?.remove();
        const img = Object.assign(document.createElement("img"), {
            src: config.illustration,
            style: "position:absolute;right:0;top:-60px;z-index:10;width:90px"
        });
        container.appendChild(img);
    }
}).observe(document.body, { childList: true, subtree: true });
</script>

<script src="https://cdn.jsdelivr.net/gh/mocchen/cssmeihua/js/aixin.js"></script>
<span class="js-cursor-container"></span>
<script src="https://cdn.jsdelivr.net/gh/mocchen/cssmeihua/js/xiaoxingxing.js"></script>
```

[取消回复](https://blog.upx8.com/4652#respond-post-4652)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")
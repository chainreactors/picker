---
title: Use the language of your choice with Pages Functions via WebAssembly
url: https://buaq.net/go-155139.html
source: unSafe.sh - 不安全
date: 2023-03-25
fetch_date: 2025-10-04T10:36:14.637714
---

# Use the language of your choice with Pages Functions via WebAssembly

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/d852c09ee94237aa262f9756cd4df32e.jpg)

Use the language of your choice with Pages Functions via WebAssembly

Loading...
*2023-3-24 21:0:0
Author: [blog.cloudflare.com(查看原文)](/jump-155139.htm)
阅读量:23
收藏*

---

Loading...

* [![Carmen Popoviciu](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/03/Screenshot-2023-03-23-at-18.11.14.png)](https://blog.cloudflare.com/author/carmen/)

![Use the language of your choice with Pages Functions via WebAssembly](https://blog.cloudflare.com/content/images/2023/03/image1-48.png)

On the Cloudflare Developer Platform, we understand that building any application is a unique experience for every developer. We know that in the developer ecosystem there are a plethora of tools to choose from and as a developer you have preferences and needs. We don’t believe there are “right” or “wrong” tools to use in development and want to ensure a good developer experience no matter your choices. We believe in meeting you where you are.

When Pages Functions moved to [Generally Available in November of last year](https://blog.cloudflare.com/pages-function-goes-ga/), we knew it was the key that unlocks a variety of use cases – namely full-stack applications! However, we still felt we could do more to provide the flexibility for you to build what you want and how you want.

That’s why today we’re opening the doors to developers who want to build their server side applications with something other than JavaScript. We’re excited to announce WebAssembly support for Pages Functions projects!

[**WebAssembly**](https://webassembly.org/) **(or Wasm)** is a low-level assembly-like language that can run with near-native performance. It provides programming languages such as C/C++, C# or Rust with a compilation target, enabling them to run alongside JavaScript. Primarily designed to run on the [web](https://webassembly.org/docs/web/) (though [not exclusively](https://webassembly.org/docs/non-web/)), WebAssembly opens up exciting opportunities for applications to run on the web platform, both on the client and the server, that up until now couldn't have done so.

With Pages Functions being Workers “under the hood” and Workers having [Wasm module support](https://blog.cloudflare.com/workers-javascript-modules/) for quite [some time](https://blog.cloudflare.com/webassembly-on-cloudflare-workers/), it is only natural that Pages provides a similar experience for our users as well. While not all use cases are a good fit for Wasm, there are [many](https://webassembly.org/docs/use-cases/) that are. Our goal with adding Wasm support is enabling those use cases and expanding the boundaries of what Functions can build.

### Using WebAssembly in Pages Functions

WebAssembly in Pages Functions works very similar to how it does today in Workers — we read `wasm` files as WebAssembly modules, ready for you to import and use directly from within your Functions. In short, like this:

```
// functions/api/distance-between.js

import wasmModule from "../../pkg/distance.wasm";

export async function onRequest({ request }) {
  const moduleInstance = await WebAssembly.instantiate(wasmModule);
  const distance = await moduleInstance.exports.distance_between();

  return new Response(distance);
}
```

Let’s briefly unpack the code snippet above to highlight some things that are important to understand.

```
import wasmModule from "../../pkg/distance.wasm";
```

Pages makes no assumptions as to how the binary `.wasm` files you want to import were compiled. In our example above, `distance.wasm` can be a file you compiled yourself out of code you wrote, or equally, a file provided in a third-party library’s distribution. The only thing Pages cares about is that `distance.wasm` is a compiled [binary](https://webassembly.github.io/spec/core/binary/conventions.html) Wasm [module](https://webassembly.github.io/spec/core/binary/modules.html) file.

The result of that import is a [`WebAssembly.Module`](https://developer.mozilla.org/en-US/docs/WebAssembly/JavaScript_interface/Module) object, which you can then [instantiate](https://developer.mozilla.org/en-US/docs/WebAssembly/JavaScript_interface/instantiate):

```
const moduleInstance = await WebAssembly.instantiate(wasmModule);
```

Once the [`WebAssembly.Instance`](https://developer.mozilla.org/en-US/docs/WebAssembly/JavaScript_interface/Instance) object is created, you can start using whatever features your Wasm module [`exports`](https://webassembly.github.io/spec/core/syntax/modules.html#syntax-export), inside your Functions code:

```
const distance = await moduleInstance.exports.distance_between();
```

### More modules, more fun!

Apart from Wasm modules, this work unlocks support for two other module types that you can import within your Functions code: **text** and **binary**. These are not standardized modules, but can be very handy if you need to import raw text blobs (such as HTML files) as a `string`:

```
// functions/my-function.js
import html from "404.html";

export async function onRequest() {
  return new Response(html,{
    headers: { "Content-Type": "text/html" }
  });
}
```

or raw data blobs (such as images) as an `ArrayBuffer`.

```
// functions/my-function.js
import image from "../hearts.png.bin";

export async function onRequest() {
  return new Response(image,{
    headers: { "Content-Type": "image/png" }
  });
}
```

### The distance between us on the surface of Earth

Let’s take a look at a live example to see it all in action! We’ve built a small [demo app](https://pages-with-wasm-demo.pages.dev/) that walks you through an example of Functions with WebAssembly end-to-end. You can check out the code of our demo application available on [GitHub](https://github.com/cloudflare/pages-fns-with-wasm-demo).

The application computes the distance in kilometers on the surface of Earth between your current location (based on the geo coordinates of the incoming [request](https://developers.cloudflare.com/workers/runtime-apis/request/#incomingrequestcfproperties)) and any other point on the globe, each time you click on the globe's surface.

![](https://blog.cloudflare.com/content/images/2023/03/image3-31.png)

The code that performs the actual high-performance distance calculation is written in Rust, and is a slight adaptation of the [example](https://rust-lang-nursery.github.io/rust-cookbook/science/mathematics/trigonometry.html#distance-between-two-points-on-the-earth) provided in the [Rust cookbook](https://rust-lang-nursery.github.io/rust-cookbook/):

```
fn distance_between(from_latitude_degrees: f64, from_longitude_degrees: f64, to_latitude_degrees: f64, to_longitude_degrees: f64) -> f64 {
    let earth_radius_kilometer = 6371.0_f64;

    let from_latitude = from_latitude_degrees.to_radians();
    let to_latitude = to_latitude_degrees.to_radians();

    let delta_latitude = (from_latitude_degrees - to_latitude_degrees).to_radians();
    let delta_longitude = (from_longitude_degrees - to_longitude_degrees).to_radians();

    let central_angle_inner = (delta_latitude / 2.0).sin().powi(2)
        + from_latitude.cos() * to_latitude.cos() * (delta_longitude / 2.0).sin().powi(2);
    let central_angle = 2.0 * central_angle_inner.sqrt().asin();

    let distance = earth_radius_kilometer * central_angle;

    return distance;
}
```

We have a Rust playground experiment available [here](https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=b60cdd8c60bed969c03bf5b87914c196), in case you want to play around with this code snippet in particular.

To use the ...
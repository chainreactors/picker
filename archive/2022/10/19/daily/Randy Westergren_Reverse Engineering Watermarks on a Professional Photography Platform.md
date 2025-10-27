---
title: Reverse Engineering Watermarks on a Professional Photography Platform
url: https://randywestergren.com/reverse-engineering-watermarks-on-a-professional-photography-platform/
source: Randy Westergren
date: 2022-10-19
fetch_date: 2025-10-03T20:19:12.073128
---

# Reverse Engineering Watermarks on a Professional Photography Platform

[![](https://secure.gravatar.com/avatar/693e7027f85b3618717c019f1641d817/?s=120&d=mm)](https://randywestergren.com/ "Randy Westergren")

[![twitter](https://randywestergren.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/32x32/twitter.png "Follow me on Twitter")](https://twitter.com/RandyWestergren "Follow me on Twitter")[![linkedin](https://randywestergren.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/32x32/linkedin.png "Find me on Linkedin")](https://www.linkedin.com/in/randywestergren "Find me on Linkedin")

October 18, 2022October 18, 2022

# Reverse Engineering Watermarks on a Professional Photography Platform

Professional photographers often add watermarks to their images to make them easy to identify, indicate copyright, promote their brand, among other reasons. Protecting images from theft online can be challenging and online photo gallery stores commonly employ various measures to deter it, e.g. disabling the context-menu in JavaScript (AKA right-click), stacking/overlaying DOM elements, or other attempts at obfuscation.

[![](https://randywestergren.com/wp-content/uploads/2022/10/example-proof-1024x828.png)](https://randywestergren.com/wp-content/uploads/2022/10/example-proof.png)

When I received the images from our recent family photo session, I noticed our photographer’s watermark on the platform she was using and was interested in how it worked. Two options immediately came to mind:

1. discrete image assets were generated and output to a filesystem; these were then served directly in the gallery from the webserver
2. server-side processing was used to dynamically generate a new image on-the-fly with the watermark superimposed

## A Closer Look

While I won’t directly identify the site, let’s take a closer look at some example markup from the gallery:

```
<a class="thumb-image">
   <div style="background-image: url(&quot;https://example.com/image/eyJmZWF0dXJlZF9pbWFnZSI6ZmFsc2UsInNpemUiOiJtZWRpdW0iLCJ1dWlkIjoiMzk5NDg5MWUtNGQ2Yy0xMWVkLTk5NTItZmExNjNlOWMiLCJjcm9wIjoiZmFsc2UiLCJub19jcm9wIjoidHJ1ZSIsInYiOiIxNjY1OTM2MjczIiwid2F0ZXJtYXJrIjoxNjY1OTM3MTQ1LCJ0aHVtYiI6dHJ1ZX0=&quot;);" class="img-tag" data-id="81393248"></div>
</a>
```

We’d usually expect an `img` tag here instead of a `div` with a background image, but it’s also interesting that the path does not end with an image extension, e.g. `.png`.

Full URL: `https://example.com/image/eyJmZWF0dXJlZF9pbWFnZSI6ZmFsc2UsInNpemUiOiJtZWRpdW0iLCJ1dWlkIjoiMzk5NDg5MWUtNGQ2Yy0xMWVkLTk5NTItZmExNjNlOWMiLCJjcm9wIjoiZmFsc2UiLCJub19jcm9wIjoidHJ1ZSIsInYiOiIxNjY1OTM2MjczIiwid2F0ZXJtYXJrIjoxNjY1OTM3MTQ1LCJ0aHVtYiI6dHJ1ZX0=`

For those with an eye for it, the path parameter immediately jumps out as a possible Base64 encoded string. After attempting to decode it, we can confirm it is:

```
{
	"featured_image": false,
	"size": "medium",
	"uuid": "3994891e-4d6c-11ed-9952-fa163e9c",
	"crop": "false",
	"no_crop": "true",
	"v": "1665936273",
	"watermark": 1665937145,
	"thumb": true
}
```

A number of interesting user-controlled parameters here. To make sure they could be modified and respected by the backend, I edited the `size` value to “small” and re-encoded it:

```
[rw ~]$ JSON='{"featured_image":false,"size":"small","uuid":"3994891e-4d6c-11ed-9952-fa163e9c","crop":"false","no_crop":"true","v":"1665936273","watermark":1665937145,"thumb":true}'
[rw ~]$ echo -n $JSON | base64 -w 0
eyJmZWF0dXJlZF9pbWFnZSI6ZmFsc2UsInNpemUiOiJzbWFsbCIsInV1aWQiOiIzOTk0ODkxZS00ZDZjLTExZWQtOTk1Mi1mYTE2M2U5YyIsImNyb3AiOiJmYWxzZSIsIm5vX2Nyb3AiOiJ0cnVlIiwidiI6IjE2NjU5MzYyNzMiLCJ3YXRlcm1hcmsiOjE2NjU5MzcxNDUsInRodW1iIjp0cnVlfQ==
```

Substituting this newly encoded parameter in the path indeed displayed a smaller image. Next, I was curious whether any additional parameters were supported from the client — more specifically, I wondered if the watermark behavior was also user-controlled. I searched the JavaScript sources for mentions of `featured_image` and found a useful hit:

```
featured_image_encoded = btoa(JSON.stringify({
    uuid: self.featured_image.uuid,
    width: 150,
    featured_image: true,
    ignore_watermark: true,
}));
```

This confirmed my suspicion — all of the controls around the image handling, including the watermarks themselves, were specified by the client.

Let’s add the `ignore_watermark` key with a value set to `true` on the original URL.

```
{
	"featured_image": false,
	"size": "medium",
	"uuid": "3994891e-4d6c-11ed-9952-fa163e9c",
	"crop": "false",
	"no_crop": "true",
	"v": "1665936273",
	"watermark": 1665937145,
	"thumb": true,
	"ignore_watermark": true
}
```

After re-encoding it to Base64 and making the request, the server successfully responded with a clean version of the image.

## Alternative Approaches

In the end, I had already paid for my photos and received the originals directly from the photographer. I stumbled upon this out of curiosity, and couldn’t help notice a critical piece of the platform’s protection for photographers had a fundamental design flaw.

A better approach might be to let the backend decide under which conditions original photos can be displayed. If a client-side approach is absolutely necessary, perhaps due to separate microservices being used for asset generation, a signed JWT would be a better option to ensure client requests are legitimate.

*Share this:* [![Facebook](https://randywestergren.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/32x32/facebook.png "Share on Facebook")](https://www.facebook.com/sharer.php?u=https%3A%2F%2Frandywestergren.com%2Freverse-engineering-watermarks-on-a-professional-photography-platform%2F&t=Reverse%20Engineering%20Watermarks%20on%20a%20Professional%20Photography%20Platform&s=100&p[url]=https%3A%2F%2Frandywestergren.com%2Freverse-engineering-watermarks-on-a-professional-photography-platform%2F&p[images][0]=https%3A%2F%2Frandywestergren.com%2Fwp-content%2Fuploads%2F2022%2F10%2Fexample-proof-1024x828.png&p[title]=Reverse%20Engineering%20Watermarks%20on%20a%20Professional%20Photography%20Platform "Share on Facebook")[![twitter](https://randywestergren.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/32x32/twitter.png "Share on Twitter")](https://twitter.com/share?url=https%3A%2F%2Frandywestergren.com%2Freverse-engineering-watermarks-on-a-professional-photography-platform%2F&text=Reverse%20Engineering%20Watermarks%20on%20a%20Professional%20Photography%20Platform%20via%20@RandyWestergren "Share on Twitter")[![linkedin](https://randywestergren.com/wp-content/plugins/social-media-feather/synved-social/image/social/regular/32x32/linkedin.png "Share on Linkedin")](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Frandywestergren.com%2Freverse-engineering-watermarks-on-a-professional-photography-platform%2F&title=Reverse%20Engineering%20Watermarks%20on%20a%20Professional%20Photography%20Platform "Share on Linkedin")

↑

* [Home](https://randywestergren.com/)
* [About](https://randywestergren.com/about/)

Proudly powered by [WordPress](http://wordpress.org/)  |
Theme: Fastr by [Kanishk](http://kanishkkunal.in).
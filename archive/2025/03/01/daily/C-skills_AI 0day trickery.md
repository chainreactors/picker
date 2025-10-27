---
title: AI 0day trickery
url: https://c-skills.blogspot.com/2025/02/ai-0day-trickery.html
source: C-skills
date: 2025-03-01
fetch_date: 2025-10-06T21:56:14.822920
---

# AI 0day trickery

[skip to main](#main)  |
[skip to sidebar](#sidebar)

# [C-skills](https://c-skills.blogspot.com/)

## Friday, February 28, 2025

### AI 0day trickery

This month I declared **Month of AI framework bugs**, and here are the 0days that came around. I analyzed the two most common AI frameworks, [P](https://pytorch.org)[yTorch](https://pytorch.org), (with [TorchVision](https://pytorch.org/vision/stable/index.html)) and [TensorFlow](https://www.tensorflow.org) which are mostly Python with C++ at the lower level (for serving trained models or deploying the actual training to GPUs via CUDA libs). Both frameworks were/are actively developed and backed by [Big](https://deepmind.google) [Tech](https://ai.meta.com/), which results in certain company repos being hardcoded in the Python code as trusted, among other artefacts.

For classical security - i.e. keeping your infra safe from intruders - you can basically divide the attack surface in two parts.

1. *Server-side* to get RCE on the deployed servers or somehow get a shell by the prompt or REST/gRPC interfaces.

2. *Client-side* to get RCE on either developer machines or also on the deployed instance at the server, but by other means than the REST/gRPC interface.

I skipped the Pickle/Deserialization surface this time, as this is a known breaking point being addressed already (although not with great results). All results of my research can be found in my [tensor-pwn](https://github.com/stealth/tensor-pwn) repo.

The actual results:

\* [File overwrite](https://github.com/stealth/tensor-pwn/tree/master/tarpwn) in all Python's core tar extractor module can lead to  RCE by overwriting either *~/.bashrc* or Python code in the *.local* cache.

\* When obtaining datasets for training and/or deployment on the server, the fetched tar archives will be extracted and the previous issue manifests. This is bad enough for *https://* URLs already, as its known that relying on CA-bundle [is not](https://en.wikipedia.org/wiki/DigiNotar) [sufficient](https://blog.mozilla.org/netpolicy/2021/11/04/mozilla-publishes-position-paper-on-the-eu-digital-identity-framework/) to prevent RCE attacks. But ...

\* ... some frameworks [replace](https://github.com/stealth/tensor-pwn/blob/master/pytorch/torchvision.jpg) https:// URLs by http:// on failure, so that the archives will eventually be fetched in plain-text and can be replaced on the network-path even by attackers who are not capable of infecting HTTPS sessions (this is far easier than it sounds). This leads to unauthenticated RCE when deploying torchvision-based models. Note, that the training data fetch and extract (read: overwrite/RCE) often happens automatically when the class of the model is instanciated and there is no manual download necessary. Therefore this resembles more of a 0click RCE. Some training data downloaders contain MD5 hashsum-"protection" but this is not the case for the *Kinetic* model thats shown in the screenshot below. MD5 is considered broken anyways, so downloaders that rely on it are eventually subject to bespoken RCE conditions too.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUk_T7LNCGeqxRHtJhfnKiaCJCnck1xaLkdj7LHkg7E3Pu9Fl0WBls2RaqCEyLaLKRZ-ultZ1yBC7tWjiwQeQZQVqdfHt7poEkPe8QAivk71AS-qFFRcVlUL3LgmDLcgau-GkQGpvmbhzETdRJ_kal-VT7EwgJH-9hm2hzw2uCrOty8IHOuBhoDvjHwdy9/w610-h298/torchvision.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUk_T7LNCGeqxRHtJhfnKiaCJCnck1xaLkdj7LHkg7E3Pu9Fl0WBls2RaqCEyLaLKRZ-ultZ1yBC7tWjiwQeQZQVqdfHt7poEkPe8QAivk71AS-qFFRcVlUL3LgmDLcgau-GkQGpvmbhzETdRJ_kal-VT7EwgJH-9hm2hzw2uCrOty8IHOuBhoDvjHwdy9/s1810/torchvision.jpg)

\* [RCE and LPE opportunities](https://github.com/stealth/tensor-pwn/blob/master/pytorch/flamegraph.jpg) when downloading and executing scripts when developers handle with the `cuda.memory` module.

So, whatever preference you might have you can choose which bug you like most and give it the best chances for owning AI deployments in your pen-tests.

Enjoy the repo!

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9Xs_v0v3GJD5mCWJws1nImWlthJ5AabtLI43MuissrNiqCSCIG1BdvkUL-qKhhmf3RIdnyAX8ZHFu6KCiWBO6aETgpuBC4IMN_wg0hot65xSbpMwIJWaUKeWADIEgMDn6ZQCY1MS7JEO2dokwB0LaBdKAKeQXWo2erTfhB340NU5rG6bkBXTr71pj3xIq/w610-h112/logo-black.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9Xs_v0v3GJD5mCWJws1nImWlthJ5AabtLI43MuissrNiqCSCIG1BdvkUL-qKhhmf3RIdnyAX8ZHFu6KCiWBO6aETgpuBC4IMN_wg0hot65xSbpMwIJWaUKeWADIEgMDn6ZQCY1MS7JEO2dokwB0LaBdKAKeQXWo2erTfhB340NU5rG6bkBXTr71pj3xIq/s640/logo-black.jpg)

Posted by

[Sebastian](https://www.blogger.com/profile/11886596387140041622 "author profile")

at
[1:16 AM](https://c-skills.blogspot.com/2025/02/ai-0day-trickery.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/3606809368389861108/9015583134431885620 "Email Post")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=3606809368389861108&postID=9015583134431885620&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=9015583134431885620&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=9015583134431885620&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=9015583134431885620&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=9015583134431885620&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=3606809368389861108&postID=9015583134431885620&target=pinterest "Share to Pinterest")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/3606809368389861108/9015583134431885620)

[Newer Post](https://c-skills.blogspot.com/2025/04/new-bridge-protocol-trickery.html "Newer Post")

[Older Post](https://c-skills.blogspot.com/2024/09/more-censorship-trickery.html "Older Post")
[Home](https://c-skills.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://c-skills.blogspot.com/feeds/9015583134431885620/comments/default)

## Where ya from

## Subscribe To

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Posts

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=https%3A%2F%2Fc-skills.blogspot.com%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=https%3A%2F%2Fc-skills.blogspot.com%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](https://c-skills.blogspot.com/feeds/posts/default)

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)

![](https://resources.blogblog.com/img/icon_feed12.png)
Posts

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Comments

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=https%3A%2F%2Fc-skills.blogspot.com%2Ffeeds%2F9015583134431885620%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=https%3A%2F%2Fc-skills.blogspot.com%2Ffeeds%2F9015583134431885620%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](https://c-skills.blogspot.com/feeds/9015583134431885620/comments/default)

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)

![](https://resources.blogblog.com/img/icon_feed12.png)
Comments

## Like c-skills' projects?

![](https://www.paypalobjects.com/de_DE/i/scr/pixel.gif)

## Links/Rechts

* [this](http://c-skills.blogspot.com/)
* [my github](http://github.com/stealth)
* [fol...
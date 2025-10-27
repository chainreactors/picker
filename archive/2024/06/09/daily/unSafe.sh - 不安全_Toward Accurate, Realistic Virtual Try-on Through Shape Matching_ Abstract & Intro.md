---
title: Toward Accurate, Realistic Virtual Try-on Through Shape Matching: Abstract & Intro
url: https://buaq.net/go-244154.html
source: unSafe.sh - 不安全
date: 2024-06-09
fetch_date: 2025-10-06T16:55:48.430938
---

# Toward Accurate, Realistic Virtual Try-on Through Shape Matching: Abstract & Intro

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

![](https://8aqnet.cdn.bcebos.com/2011aa34d61a5320c469f0ac147b3c51.jpg)

Toward Accurate, Realistic Virtual Try-on Through Shape Matching: Abstract & Intro

Authors:(1) Kedan Li, University of Illinois at Urbana-Champaign;(2) Min Jin Chong, University of
*2024-6-8 20:30:22
Author: [hackernoon.com(查看原文)](/jump-244154.htm)
阅读量:7
收藏*

---

**Authors:**

(1) Kedan Li, University of Illinois at Urbana-Champaign;

(2) Min Jin Chong, University of Illinois at Urbana-Champaign;

(3) Jingen Liu, JD AI Research;

(4) David Forsyth, University of Illinois at Urbana-Champaign.

## Table of Links

* [Abstract and Intro](http://hackernoon.com/preview/vJP1ktczl1XCmzzUz4C0?ref=hackernoon.com)
* [Related Work](http://hackernoon.com/preview/yjgPf5TjQSk5gbVrf3zC?ref=hackernoon.com)
* [Proposed Method](http://hackernoon.com/preview/2NOsMPF12Kj4nOI7CAiy?ref=hackernoon.com)
* [Experiments](http://hackernoon.com/preview/aWg14918jLAW3q0WyiMQ?ref=hackernoon.com)
* [Conclusions and References](http://hackernoon.com/preview/DstdF8k6ujIzWjGBkpkk?ref=hackernoon.com)

## Abstract

A virtual try-on method takes a product image and an image of a model and produces an image of the model wearing the product. Most methods essentially compute warps from the product image to the model image and combine using image generation methods. However, obtaining a realistic image is challenging because the kinematics of garments is complex and because outline, texture, and shading cues in the image reveal errors to human viewers. The garment must have appropriate drapes; texture must be warped to be consistent with the shape of a draped garment; small details (buttons, collars, lapels, pockets, etc.) must be placed appropriately on the garment, and so on. Evaluation is particularly difficult and is usually qualitative.

This paper uses quantitative evaluation on a challenging, novel dataset to demonstrate that (a) for any warping method, one can choose target models automatically to improve results, and (b) learning multiple coordinated specialized warpers offers further improvements on results. Target models are chosen by a learned embedding procedure that predicts a representation of the products the model is wearing. This prediction is used to match products to models. Specialized warpers are trained by a method that encourages a second warper to perform well in locations where the first works poorly. The warps are then combined using a U-Net. Qualitative evaluation confirms that these improvements are wholesale over outline, texture shading, and garment details.

**Keywords:** Fashion, Virtual try-on, Image generation, Image warping

## 1. Introduction

E-commerce means not being able to try on a product, which is difficult for fashion consumers [44]. Sites now routinely put up photoshoots of models wearing products, but volume and turnover mean doing so is very expensive and time consuming [34]. There is a need to generate realistic and accurate images of fashion models wearing different sets of clothing. One could use 3D models of posture [8,14]. The alternative – synthesize product-model images without 3D measurements [17,45,39,11,15] – is known as virtual try-on. These methods usually consist of two components: 1) a spatial transformer to warp the product

![Fig. 1. Translating a product to a poorly chosen model leads to difficulties (random model; notice how the blazer has been squashed on the left, and the jersey stretched on the right). Our method can choose a good target model for a given product, leading to significant qualitative and quantitative improvement in transfers (chosen model). In addition, we train multiple warpers to act in a coordinated fashion, which further enhances the generation results (enhanced; the buttonholes on the jacket are in the right place left, and the row of buttons on the cardigan is plausible right). The figure shows that (a) carefully choosing the model to warp and (b) using multiple specialized warpers significantly improve the transfer. Quantitative results in table 4.3 strongly supports the two points made.](https://hackernoon.imgix.net/images/fWZa4tUiBGemnqQfBGgCPf9594N2-5583uha.png?auto=format&fit=max&w=1920)

image using some estimate of the model’s pose and 2) an image generation network that combines the coarsely aligned, warped product with the model image to produce a realistic image of the model wearing the product.

It is much easier to transfer with simple garments like t-shirts, which are emphasized in the literature. General garments (unlike t-shirts) might open in front; have sophisticated drapes; have shaped structures like collars and cuffs; have buttons; and so on. These effects severely challenge existing methods (examples in Supplementary Materials). Warping is significantly improved if one uses the product image to choose a model image that is suited to that garment (Figure 1).

At least in part, this is a result of how image generation networks are trained. We train using paired images – a product and a model wearing a product [17,45,53]. This means that the generation network always expects the target image to be appropriate for the product (so it is not trained to, for example, put a sweater onto a model wearing a dress, Figure 1). An alternative is to use adversarial training [11,12,38,13,37]; but it is hard to preserve specific product details (for example, a particular style of buttons; a decal on a t-shirt) in this framework. To deal with this difficulty, we learn an embedding space for choosing product-model pairs that will result in high-quality transfers (Figure 2). The embedding learns to predict what shape a garment in a model image would take if it were in a product image. Products are then matched to models wearing similarly shaped garments. Because models typically wear many garments, we use a spatial attention visual encoder to parse each category (top, bottom, outerwear, all-body, etc.) of garment and embed each separately.

Another problem arises when a garment is open (for example, an unbuttoned coat). In this case, the target of the warp might have more than one connected component. Warpers tend to react by fitting one region well and the other poorly, resulting in misaligned details (the buttons of Figure 1). Such errors may make little contribution to the training loss, but are very apparent and are considered severe problems by real users. We show that using multiple coordinated specialized warps produces substantial quantitative and qualitative improvements in warping. Our warper produces multiple warps, trained to coordinate with each other. An inpainting network combines the warps and the masked model, and creates a synthesized image. The inpainting network essentially learns to choose between the warps, while also provides guidance to the warper, as they are trained jointly. Qualitative evaluation confirms that an important part of the improvement results from better predictions of buttons, pockets, labels, and the like.

We show large scale quantitative evaluations of virtual try-on. We collected a new dataset of 422,756 pairs of product images and studio photos by mining fashion e-commerce sites. The dataset contains multiple product categories. We compare with prior work on the established VITON dataset [17] both quantitatively and qualitatively. Quantitative result shows that choosing the productmodel pairs using our shape embedding yields significant improvements for all image generation pipelines (table 4.3). Using multiple warps also consistently outperform the single warp baseline, demonstrated through both quantitative (table 4.3, figure 5) and qua...
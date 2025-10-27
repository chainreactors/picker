---
title: Towards Automatic Satellite Images Captions Generation Using LLMs: Methodology
url: https://buaq.net/go-245486.html
source: unSafe.sh - 不安全
date: 2024-06-17
fetch_date: 2025-10-06T16:54:58.744139
---

# Towards Automatic Satellite Images Captions Generation Using LLMs: Methodology

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

![](https://8aqnet.cdn.bcebos.com/356ae62571b0ad019df86c32abd93873.jpg)

Towards Automatic Satellite Images Captions Generation Using LLMs: Methodology

Authors:(1) Yingxu He, Department of Computer Science National University of Singapore {[email pro
*2024-6-16 22:30:21
Author: [hackernoon.com(查看原文)](/jump-245486.htm)
阅读量:6
收藏*

---

**Authors:**

(1) Yingxu He, Department of Computer Science National University of Singapore {[[email protected]](https://hackernoon.com/cdn-cgi/l/email-protection)};

(2) Qiqi Sun, College of Life Sciences Nankai University {[[email protected]](https://hackernoon.com/cdn-cgi/l/email-protection)}.

## Table of Links

* [Abstract and Intro](http://hackernoon.com/preview/0SKmdJWIEyPiarywYBSv?ref=hackernoon.com)
* [Methodology](http://hackernoon.com/preview/JowAM9SEdUdM6bATYkkp?ref=hackernoon.com)
* [References](http://hackernoon.com/preview/dQSRCDQ0CRpqs0ijvtYZ?ref=hackernoon.com)

## 2. Methodology

In this section, we describe our proposed approach to automatically collect captions for remote sensing images by guiding LLMs to describe their object annotations. In this work, we limit the number of objects in each image to no more than 15, which ensures a relatively simple spatial layout for the LLM. Our approach consists of three main steps: (1) develop APIs to conduct geographical analysis and describe spatial relationships between objects, (2) prompt the API to generate captions with the help from APIs, and (3) caption evaluation and selection. We explain each step in detail below.

### 2.1 Spatial Relationship APIs

LLM is incompetent at processing 2-dimensional geographical information, so we implemented several analytical approaches to analyze the spatial relations between objects. Inspired by the captions provided by the RSICD paper, we only focused on analyzing the distances between objects, the concentration of object locations, shapes formed by groups of objects, and significant relations between objects.

### 2.1.1 Distance

In the Xview and Dota datasets, the size of objects varies a lot. Therefore, using the distance between centers is inappropriate for the distances between objects. For instance, although the centers of two large buildings might be quite far apart, their inner-facing walls might be only a few steps away. Therefore, we consider the shortest distances between bounding boxes as their distance. For the distance between two groups of objects, we represent it with the distance between their closest element, which is normally referred to as the Single Linkage measure in the field of clustering.

### 2.1.2 Clustering

One of the most important features captured by human eyes is the concentration of objects based on their locations and types, e.g., one tends to easily differentiate a vehicle running on a highway from several buildings standing by the road. On the other hand, people also tend to pay attention to the objects’ closest neighbor, e.g., a passenger car next to a truck is easier to draw people’s attention than a building relatively further away from the truck. Traditional machine learning clustering algorithms include distance-based algorithms such as K-Means and hierarchical clustering, and density-based clustering such as DBSCAN and its variants. However, the K-Means algorithm often fails to separate outliers from concentrated objects, while the benefits of density-based clustering might be buried in this case, where each image only contains fewer than ten objects.

In this work, We used the Minimum Spanning Tree (MST) algorithm to connect all the objects in the image and form clusters by removing significantly long edges from the graph. Kruskal’s MST algorithm[3] considers objects’ nearest neighbors and simultaneously skips negligible connections, ensuring every tree edge is aligned to humans’ observing behavior. We set the threshold at the 75 percentile of the edge weights from the entire dataset. Edges above this threshold were removed from the graph to form clusters, minimizing intra-cluster and maximizing inter-cluster distances. To encourage grouping objects of the same type into the same cluster, We add extra length to distances between objects of different types. Figure 1 gives a detailed illustration on the MST-based clustering algorithm. This approach could precisely split objects by type, location, and proximity, which benefits the subsequent geographical analysis.

![Figure 1: Illustration of the MST-based clustering algorithm. Figure (1) demonstrates the created graph representing the minimal spanning tree. Extra length is added to the distance between objects of different types. Figure (2) shows the clusters formed by cutting long edges. Figure (3) projects the location of the objects to the real image.](https://hackernoon.imgix.net/images/fWZa4tUiBGemnqQfBGgCPf9594N2-b583u3q.png?auto=format&fit=max&w=3840)

### 2.1.3 Geometric Shape

Inspired by the captions provided in the RSICD dataset, the line shape is considered the fundamental shape to be detected in this work. It seems most attractive to human eyes and the basic element of many other complicated shapes. For instance, the square grid street pattern is one of the most popular street patterns used in cities, where lines of buildings are the most fundamental elements. Undeniably, other shapes could also easily draw people’s attention, such as circles and squares. Nonetheless, in the setting of this work, where each image contains at most 15 objects, they are less obvious and more difficult to detect. Therefore, we only implemented a method to detect line shapes from groups of objects by inspecting whether the lines formed by corners of bounding boxes are parallel.

### 2.1.4 Geometric Relation

We review some relations listed in the RSICD paper[6] and come out with our list of relations to be included in the image captions: "stands alone", "near", "in a row", "surrounded by", "between", and "in two sides of". We modified the "in rows" relation from RSICD paper to "in a row", as objects in different rows can be clustered into different groups as is described in section 2.1.2, and any possible line shape will be detected by the shape identification algorithm described in section 2.1.3. Additionally, we propose a "between" relation as the flip side of "in two sides of" to differentiate the situation where there are only objects on the two sides of others from objects circling others 360◦ . In this work, the approaches described above can address relations "stands alone", "near", and "in a row". The relation "surrounded by" is only considered when certain objects are located within the border of another group of objects. The detailed function is achieved by drawing links from the boxes in the middle to the outer ones and calculating the angles between them. The implementation of relations "between" and "in two sides of" are left for future work.

### 2.2 LLM Prompting

The second step of our approach is to use prompts to guide the LLM to produce a caption following a similar pattern. With the APIs implemented in section 2.1, there are many options to prompt the LLM and guide it to generate the ideal captions. Following the recently popular idea of treating the LLMs as a controller or action dispatcher[13], one approach could be allowing the language model to plan its actions and execute the functions in sequences to obtain helpful geographical analysis results. For instance, the recently developed ReAct[10] approach synergizes the reasoning and executing process of LLM to enhance its capability of handling complex tasks. It allows great flexibility in geographical analysis and ...
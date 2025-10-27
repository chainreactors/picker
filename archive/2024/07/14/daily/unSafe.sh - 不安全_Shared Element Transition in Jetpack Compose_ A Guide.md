---
title: Shared Element Transition in Jetpack Compose: A Guide
url: https://buaq.net/go-250432.html
source: unSafe.sh - 不安全
date: 2024-07-14
fetch_date: 2025-10-06T17:40:52.162783
---

# Shared Element Transition in Jetpack Compose: A Guide

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

![](https://8aqnet.cdn.bcebos.com/a27422467413f92cd0205ece8dd40d4c.jpg)

Shared Element Transition in Jetpack Compose: A Guide

Hello! My name is Artem, and I develop Android applications.Recently, I started sharing my experien
*2024-7-13 23:0:14
Author: [hackernoon.com(查看原文)](/jump-250432.htm)
阅读量:6
收藏*

---

Hello! My name is Artem, and I develop Android applications.

Recently, I started sharing my experiences on this topic.

This article is a text version of a [video](https://www.youtube/bbSQ3pvrHLk?ref=hackernoon.com) on my YouTube channel [Android Insights](https://www.youtube.com/%40Android_Insights?ref=hackernoon.com).

In this article, I want to explain how to animate your app using **Shared Element Transition**. This feature allows UI elements to animate as they transition between app screens, making the user interface more memorable.

This feature was recently added, so ensure your project uses **Jetpack Compose** version **1.7.0-alpha07** or higher.

To demonstrate, I've created a simple app with just two screens: a list on the first screen and detailed information on the second.

![Basic Application](https://hackernoon.imgix.net/images/a9PUoO7LSYVXA3AHY21rjCc90Bn1-38a3123.gif.webp?auto=format&fit=max&w=1080)

For simplicity, I'm not using any navigation libraries. Here's the code for the root `@Composable` function:

```
@Composable
fun CatsContent(modifier: Modifier) {
   var selectedCat: Cat? by remember { mutableStateOf(null) }

   if (selectedCat != null) {
       BackHandler { selectedCat = null }

       CatDetails(
           modifier = modifier.fillMaxSize(),
           cat = selectedCat!!,
       )
   } else {
       CatsList(
           modifier = modifier.fillMaxSize(),
           onCatClicked = { cat ->
               selectedCat = cat
           }
       )
   }
}
```

When an item in the list is clicked, it is assigned to the `selectedCat` variable. If `selectedCat` is not null, the `@Composable` with the detailed information is displayed.

Here's the code for `CatDetails` and `CatsList` functions:

```
@Composable
fun CatDetails(
   modifier: Modifier,
   cat: Cat,
) {
   Column(
       modifier = modifier.verticalScroll(
           state = rememberScrollState(),
       ),
       verticalArrangement = Arrangement.spacedBy(8.dp),
   ) {
       Image(
           painter = painterResource(cat.iconRes),
           contentDescription = null,
       )

       Text(
           modifier = Modifier
               .padding(
                   horizontal = 8.dp,
               ),
           text = stringResource(cat.textRes)
       )
   }
}

@Composable
fun CatsList(
   modifier: Modifier,
   onCatClicked: (Cat) -> Unit,
) {
   val cats = rememberCatsList()

   Box(
       modifier = modifier,
   ) {
       LazyColumn(
           verticalArrangement = Arrangement.spacedBy(8.dp),
       ) {
           items(
               items = cats,
               key = { cat -> cat.iconRes },
               contentType = { cat -> cat::class }
           ) { item ->
               Cat(
                   modifier = Modifier
                       .fillParentMaxWidth()
                       .clickable {
                           onCatClicked(item)
                       }
                       .padding(
                           horizontal = 8.dp
                       ),
                   cat = item,
               )
           }
       }
   }
}

@Composable
fun Cat(
   modifier: Modifier,
   cat: Cat,
) {
   Row(
       modifier = modifier,
       horizontalArrangement = Arrangement.spacedBy(8.dp),
       verticalAlignment = Alignment.CenterVertically,
   ) {
       Image(
           modifier = Modifier.size(128.dp),
           painter = painterResource(cat.iconRes),
           contentScale = ContentScale.Crop,
           contentDescription = null,
       )

       Text(
           modifier = Modifier,
           text = stringResource(cat.textRes),
           maxLines = 3,
           overflow = TextOverflow.Ellipsis,
       )
   }
}
```

### Adding Transition

Now, let's add the rest of the required code in two steps

```
// OptIn is required because ExperimentalSharedTransitionApi is unstable
@OptIn(ExperimentalSharedTransitionApi::class)
@Composable
fun CatsContent(
   modifier: Modifier
) {
   var selectedCat: Cat? by remember { mutableStateOf(null) }

   SharedTransitionLayout {
       AnimatedContent(
           targetState = selectedCat != null
       ) { targetState ->
           if (targetState) {
               BackHandler { selectedCat = null }

               CatDetails(
                   modifier = modifier.fillMaxSize(),
                   cat = selectedCat!!,
               )
           } else {
               CatsList(
                   modifier = modifier.fillMaxSize(),
                   onCatClicked = { cat ->
                       selectedCat = cat
                   }
               )
           }
       }
   }
}
```

Application behavior has already changed

![Animated transition between screens](https://hackernoon.imgix.net/images/a9PUoO7LSYVXA3AHY21rjCc90Bn1-71g31ms.gif.webp?auto=format&fit=max&w=828)

There are animations for transitioning between screens using the `AnimatedContent` function, but this is still not what we need.

It's time to add the rest of the code.

```
@OptIn(ExperimentalSharedTransitionApi::class)
@Composable
fun CatsList(
   modifier: Modifier,
   onCatClicked: (Cat) -> Unit,
   sharedTransitionScope: SharedTransitionScope,
   animatedVisibilityScope: AnimatedVisibilityScope,
) {
   val cats = rememberCatsList()

   Box(
       modifier = modifier,
   ) {
       LazyColumn(
           verticalArrangement = Arrangement.spacedBy(8.dp),
       ) {
           items(
               items = cats,
               key = { cat -> cat.iconRes },
               contentType = { cat -> cat::class }
           ) { item ->
               Cat(
                   modifier = Modifier
                       .fillParentMaxWidth()
                       .clickable {
                           onCatClicked(item)
                       }
                       .padding(
                           horizontal = 8.dp
                       ),
                   cat = item,
                   // passing SharedTransitionScope
                   sharedTransitionScope = sharedTransitionScope,
                   // passing AnimatedVisibilityScope
                   animatedVisibilityScope = animatedVisibilityScope,
               )
           }
       }
   }
}

@OptIn(ExperimentalSharedTransitionApi::class)
@Composable
fun Cat(
   modifier: Modifier,
   cat: Cat,
   sharedTransitionScope: SharedTransitionScope,
   animatedVisibilityScope: AnimatedVisibilityScope,
) {
   with(sharedTransitionScope) {
       Row(
           modifier = modifier,
           horizontalArrangement = Arrangement.spacedBy(8.dp),
           verticalAlignment = Alignment.CenterVertically,
       ) {
           Image(
               modifier = Modifier
                   .size(128.dp)
                   // using brand new Modifier sharedElement
                   .sharedElement(
                       state = rememberSharedContentState(key = cat.iconRes.toString()),
                       animatedVisibilityScope = animatedVisibilityScope,
                   ),
               painter = painterResource(cat.iconRes),
               contentScale = ContentScale.Crop,
               contentDescription = null,
           )

           Text(
               modifier = Modifier,
               text = stringResource(cat.textRes),
               maxLines = 3,
               overflow = TextOverflow.Ellipsis,
          ...
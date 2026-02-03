---
title: Vibecoding native apps has gotten really good
url: https://blog.jonlu.ca/posts/vibecoding-native-apps
source: JonLuca's Blog
date: 2026-02-02
fetch_date: 2026-02-03T04:09:03.492927
---

# Vibecoding native apps has gotten really good

# JonLuca's Blog

[Posts](/ "Posts")[About](/about "About")[Contact](/contact "Contact")[Interesting Snippets](/interesting-snippets "Interesting Snippets")

Feb 2, 2026

# Vibecoding native apps has gotten really good

I spent a weekend vibecoding a small native app called [Palate](https://apps.apple.com/ca/app/palate-fine-dining-tracker/id6757490799) - a fine dining tracker for tasting menus, restaurants, and personal notes. For years I've had a clear idea in my mind of the features that would make a product like this great:

* cluster your photos by time and location
* cross referencing your calendar with the photos to identify potential restaurants
* use the on device ML to identify dishes and food
* have an offline list of fine dining restaurants that you can compare GPS coordinates against

![image](https://assets.jonlu.ca/palate.png)

For a long time this felt like too complex a project to actually work on - it's something I wanted to exist, but it wasn't worth the time to actually go out and build it. I decided to give it a shot again this weekend because of how good Codex has gotten, and because I've been following the progress of React Native and Expo Router for a while now.

I was blown away at how good it has gotten - install the expo and vercel skills in your project, set codex to 5.2 xhigh, and let it rip. It was just incredible how well it worked. I was able to get a fully functioning app with native modules, navigation, and state management in just a few hours.

I gave it the directive to build a stats page with statistics it would find interesting and it did most of the product work for me. There were small visual issues here and there, but the speed of iteration was incredible.

![image](https://assets.jonlu.ca/palate-stats.png)

I would highly recommend people with prior negative experiences of React Native try React Native and Expo again. Things were pretty rough at the start, but sometime in the last year or so things really clicked. I can honestly say that the apps feel truly native at this point. The file‑based routing model maps perfectly to small apps, and it made iterating on screens feel almost like shipping a web app with a native polish.

Codex made writing the native modules for iOS trivial. I'm a pretty horrible Swift engineer, and the native code seemed like the most daunting part of the project. But Codex made it easy to write clean, idiomatic Swift code that integrated perfectly with React Native. I was able to write modules for reading the photo library, accessing the calendar, and doing on device image classification in just a few hours, without really needing to look at the swift code itself.

The other surprise was how good native tabs + the React Compiler feel together. The app is running a few lists, some image grids, and a bunch of memoized state, and it still feels snappy. Transitions are instant, scroll is smooth, and everything feels like it was built in Swift.

Vibecoding has gotten scary good, and lets you ship native feeling apps in just a few days. This was my first native app fully vibecoded, and I don't really love a lot of the code smells. It feels overly verbose in places, and I think with more experience I could make it cleaner. But the fact that I was able to ship something this good in a weekend is a testament to how far the ecosystem has come.

You can find the code on [GitHub](https://github.com/jonluca/palate).

![JonLuca](https://assets.jonlu.ca/mini-profile.png)

JonLuca at 03:34

To get notified when I publish a new essay, [please subscribe here](https://jonluca.substack.com/ "JonLuca's Substack").

![](https://j.jonlu.ca/matomo.php?idsite=1&rec=1)
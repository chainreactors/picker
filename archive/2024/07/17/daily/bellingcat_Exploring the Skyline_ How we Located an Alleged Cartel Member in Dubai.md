---
title: Exploring the Skyline: How we Located an Alleged Cartel Member in Dubai
url: https://www.bellingcat.com/resources/2024/07/16/dubai-uae-cartel-organised-crime-geolocation-open-source-guide-technique-tools/
source: bellingcat
date: 2024-07-17
fetch_date: 2025-10-06T17:42:33.469202
---

# Exploring the Skyline: How we Located an Alleged Cartel Member in Dubai

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)

* EN
  + [Русский](https://ru.bellingcat.com)
  + [Français](https://fr.bellingcat.com)
  + [Español](https://es.bellingcat.com)
  + [Deutsch](https://de.bellingcat.com)
  + [Українська](https://uk.bellingcat.com)
* [Donate](https://www.bellingcat.com/donate)

Search for:

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)
* [Donate](/donate)

[![Profile picture for: Aiganysh Aidarbekova](https://www.bellingcat.com/app/uploads/2022/07/DSCF9213-300x300.jpg)](https://www.bellingcat.com/author/aiganysh/)
[Aiganysh Aidarbekova](https://www.bellingcat.com/author/aiganysh/)

Aiganysh is a Bellingcat researcher from Kyrgyzstan. She is particularly interested in corruption in Central Asia, conspiracies in Europe and tool development.

# Exploring the Skyline: How we Located an Alleged Cartel Member in Dubai

July 16, 2024

* [3D Model](/tag/3d-model)
* [Blender](/tag/blender)

In this guide we’ll show you how we narrowed down where an alleged cartel member was staying in a luxury Dubai skyscraper.

By following the steps outlined below, Bellingcat helped establish that in 2023 Dženis Kadrić was renting a Dubai property owned by Candido Nsue Okomo the brother-in-law of Equatorial Guinea’s President. This was later confirmed by documentation obtained by investigative partners.

This finding contributed to a recent investigation by KRIK, Diario Rombe and OCCRP into dirty money in Dubai real estate.

Kadrić, a former police officer, was arrested in Bosnia in February of this year in relation to alleged involvement in organised crime and money laundering. He is currently [under house arrest](https://www.klix.ba/vijesti/crna-hronika/dzenis-kadric-clan-kartela-tito-i-dino-pusten-iz-vojkovica-u-kucni-pritvor/240503059#google_vignette) in the country.

## The Dubai Skyline

Prior to Kadrić’s arrest, his wife’s posts of her designer outfits for her tens of thousands of followers often included a beautiful view of the Dubai skyline.

This gave us a starting point for where to look.

The first thing we noticed was several odd shaped pools in the background of her posts. These distinctive pools quickly led us to the tallest building in the world- the Burj Khalifa.

![](https://www.bellingcat.com/app/uploads/2024/07/image7.png)

*Dženis Kadrić seen in a TikTok video of his wife. Source: Tiktok.*

The pools seen in the background of the posts, matched those located at the bottom of the Burj Khalifa complex. We can also see a low building with a flat roof -the Dubai Opera House, and a few skyscrapers surrounding the building that we were able to identify.

![](https://www.bellingcat.com/app/uploads/2024/07/image11-1200x777.png)

*Sources: Instagram, Google Earth Pro.*

Next we started to narrow down where in the building of 168 floors, the posts were taken.

In the following photo, the camera is held straight, giving us a good view of Burj Vista Tower 1 and Burj Vista Tower 2. The first one is 65 storeys high, and the second one is 20 floors high, indicating the floor is somewhere between those two.

![](https://www.bellingcat.com/app/uploads/2024/07/image2.png)

*Sources: Instagram, [PropSearch.ae](https://static.propsearch.ae/dubai-locations/burj-vista_YZ158_xl.jpg).*

In another photo, a side of Burj Khalifa is seen with its curved wall windows, and metal rings encompassing a number of floors.

A different [view from the Armani Hotel](https://www.google.com/maps/%4025.1967263%2C55.2741139%2C3a%2C75y%2C40.68h%2C88.96t/data%3D%213m8%211e1%213m6%211sAF1QipPqWR2Z2U0jmdqb1n7nn2JmX0t0wKrwlSU0oUes%212e10%213e11%216shttps%3A//lh5.googleusercontent.com/p/AF1QipPqWR2Z2U0jmdqb1n7nn2JmX0t0wKrwlSU0oUes%3Dw203-h100-k-no-pi1.1517053-ya332.83252-ro-0.6989787-fo100%217i8192%218i4096?coh=205409&entry=ttu) which is located on the 38th floor of the Burj Khalifa shows similar metal rings.

Looking at Burj Khalifa’s plans, we find that those rings are mechanical floors, and there are seven of them spread out across the Burj Khalifa.

![](https://www.bellingcat.com/app/uploads/2024/07/image5.png)

*A photo of Kadrić’s wife posted on Instagram with a view of the connecting wing of the Burj Khalifa. The photo shows black rings representing mechanical floors- highlighted by us in red.*

We are not identifying the exact floor for privacy reasons, but here are the next steps we took to narrow down the location.

There were a few options to determine the floor number.

The easiest option is to look at perspective angles of the floors visible.

## Finding Eye Level in an Image

In the post above, the floors are parallel to each other, but when taking a photo (or just simply looking with your own eyes), you can see that the top floor lines are going one direction, while the floors on the bottom are going the opposite direction.

These lines are called the perspective angles. In the image below you can trace the perspective angles, as the demonstrator has marked two in orange. To find the eye level you need to continue the lines until they cross- and where they cross indicates the eye level (the yellow line in the image).

In other words you need to find the *true horizontal line* amidst all the angled perspective.

![](https://www.bellingcat.com/app/uploads/2024/07/image8-1200x741.png)

*In the image above, the orange lines represent the perspective lines, and where they cross we can find the eye level -marked with a yellow line. Source: Youtube, [How to Find Eye Level Practical Perspective](https://www.youtube.com/watch?v=nCKjNizfE_I).*

For a more detailed explanation of finding the eye level in an image, you can watch this [video](https://www.youtube.com/watch?v=nCKjNizfE_I) from which the above picture is taken.

Let’s apply the same method to our image. We build perspective lines in orange by drawing lines along the floor numbers and continue them until they cross. At the point where they cross we draw a yellow line – representing the eye level. This gives us the true eye level in the image which can be used to count the floors.

![](https://www.bellingcat.com/app/uploads/2024/07/image4.png)

*The same photo posted above, this time with lines of perspective (orange) and the eye level marked in yellow.*

## Creating a 3D Model

Another option to narrow down the floor is by building a 3D model. The process of building a model of your area of interest has been used in a [number of investigations](https://www.bellingcat.com/resources/2023/07/13/more-than-mountaineering-using-peakvisor-for-geolocation/).

Due to the popularity of the Burj Khalifa there were already a few free 3D models available for us to review. Using photos and videos from social media, as well as property listings, we created a 3D model of the building using [Blender](https://www.blender.org/), a free and open source 3D software. Given these details, we were able to recreate the view which matches the original almost perfectly.

[<https://www.bellingcat.com/app/uploads/2024/07/burj-khalifa-3d-model-export-1.mp4>](https://www.bellingcat.com/app/uploads/2024/07/burj-khalifa-3d-model-export-1.mp4?_=1)

Thomas Bordeaux, a member of Bellingcat’s Global Authentication Project and Masters of Architecture Student with experience working with perspective matching, also independently confirmed the floor number.

## Final Tips

In this case study, we had a good starting point for our investigation- the fact that the Burj Khalifa is such a popular building meant we could find lots of information about it via open sources- including apartments listed for sale and detailed descriptions of apartments.

![](https://www.bellingcat.com/app/uploads/202...
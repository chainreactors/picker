---
title: A New Tool Shows What War Has Done to Ukraine’s Forests
url: https://www.bellingcat.com/resources/2023/08/18/a-new-tool-shows-what-war-has-done-to-ukraines-forests/
source: bellingcat
date: 2023-08-19
fetch_date: 2025-10-04T12:01:29.554764
---

# A New Tool Shows What War Has Done to Ukraine’s Forests

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

[![](https://www.bellingcat.com/app/uploads/2023/08/chris-1-300x300.jpeg)](https://www.bellingcat.com/author/chrisgiles/)
[Christopher Giles](https://www.bellingcat.com/author/chrisgiles/)

Christopher Giles is an open-source reporter who covers conflict, climate and online harm using remote sensing and network mapping. His work has been featured on the BBC, the Stanford Internet Observatory and CNN International.

# A New Tool Shows What War Has Done to Ukraine’s Forests

August 18, 2023

* [Environment](/tag/environment)
* [Ukraine](/tag/ukraine)

Translations:

* [English (UK)](https://www.bellingcat.com/resources/2023/08/18/a-new-tool-shows-what-war-has-done-to-ukraines-forests/)
* [Українська](https://uk.bellingcat.com/materialy-ta-metody/2023/08/30/a-new-tool-shows-what-war-has-done-to-ukraines-forests-uk/)

*Access The OSINT Forest Area Tracker [here](https://osintmapping.users.earthengine.app/view/osint-forest-area-tracker). You can read a concise summary of the tool on the [GitHub repository](https://github.com/csgsf/ee_burn_tracker).*

---

Among the many victims of Russia’s full-scale invasion of Ukraine are some of the most important ecosystems in Eastern Europe: Ukraine’s forests and protected areas.

The full extent of the damage, however, is unknown. That’s why we are launching a new tool that will help open source researchers track destruction from afar.

In September 2022, Ukrainian environmental researchers [visited national parks](https://uwecworkgroup.info/impact-of-military-action-on-ukraines-wild-nature/) — which are more resilient to climate change than artificial plantings and support crucial biodiversity—to assess damage to forests and wildlife. Initial findings revealed broken trees, damaged root systems due to trench digging and unexploded munitions scattered across protected lands.

“Forests have suffered a lot on the frontline… huge areas of forests are being mined”, Yehor Hrynyk, an environmental campaigner at the [Ukrainian Nature Conservation Group](https://uncg.org.ua/en/), told Bellingcat.
But large parts of Ukraine’s vast national parks, mountainous regions and woodlands are inaccessible for on-the-ground environmental monitoring.

That’s where open source techniques come in.

![](https://www.bellingcat.com/app/uploads/2023/08/2023-03-03T160551Z_2059477765_MT1SIPA0008EP1OR_RTRMADP_3_SIPA-USA-1200x780.jpg)

A burnt tank and destroyed trees in Bogorodychne, Ukraine. This ruined village in the Donetsk Region lies on the Siverskyi Donets river, adjacent to the Svyati Hory National Park. Photo (c) by Mykhaylo Palinchak / SOPA Images/Sipa USA

## **The OSINT Forest Area Tracker**

We’ve launched the “OSINT Forest Area Tracker”, hosted on Google Earth Engine. Our tool compares data collected by Sentinel-2, a satellite which detects changes in infrared wavelengths and can be used to study the health of forests.

The tool reveals the scale and intensity of anomalous changes on land. This narrows down search areas for researchers working on environmental damage in Ukraine.

Importantly, the map does not attribute the cause of these changes, meaning that it is crucial to find corroborating evidence from other sources before concluding that they were the result of military activity.

The tool uses the Normalised Burn Ratio (NBR) index to estimate burn severity.

Researchers can also use the tool to select custom date ranges for geographic locations of interest.

As Ukraine’s [official database of protected areas](https://data.gov.ua/dataset/mepr_05) includes over 7,500 sites, we chose not to study them all — among their number are botanical gardens, city parks and archaeological sites. That list also includes many areas in the far west of the country which have not seen intense conflict.

Therefore, we selected 16 areas which featured the highest number of detected fires over the first year of the war, based on Moderate Resolution Imaging Spectroradiometer (MODIS) data. MODIS is a sensor which allows satellites to detect thermal anomalies, including fires in active war zones (Along with VIIRS, MODIS data can be accessed on the FIRMS system; you can read more about [its use to open source researchers here](https://www.bellingcat.com/resources/2022/10/04/scorched-earth-using-nasa-fire-data-to-monitor-war-zones/)). We also added Svyati Hory National Park because of its proximity to fighting.

The tool includes a drop down list preset areas from across the country, including those near military activity. These preset areas are referred to by their acronyms, for example SHNP for Svyati Hory National Park. A full list of these acronyms can be found on the tool’s [GitHub page](https://github.com/csgsf/ee_burn_tracker).

 If researchers are interested in areas of the country not included in the dropdown menu, the coordinates can be entered manually.

While the new tool focuses on Ukraine by default, the methods it employs could be used to analyse areas elsewhere in the world.

## **Damage to the Svyati Hory Forests**

To show you how the tool works, let’s assess Svyati Hory National Park, a protected area in Eastern Ukraine.

This forested area, also known as the Holy Mountains National Park, is set against rolling hills in the north of Donetsk Region, near the borders with Kharkiv and Luhansk Regions. It’s famous for the [Sviatohirsk Lavra Monastery](https://www.bellingcat.com/news/uk-and-europe/2022/06/07/clues-to-the-fate-of-five-damaged-cultural-heritage-sites-in-ukraine/) which lies along the Siverskyi Donets River — which divided Russian and Ukrainian forces for several months until a Ukrainian counteroffensive.

In May 2022 the Ukrainian Nature Conservation Group (UNCG) [raised concerns](https://uncg.org.ua/en/unesco-reserve-and-national-park-are-on-fire-from-hostilities/) about the impact of fighting in this region. So what can The OSINT Forest Area Tracker tell us about it?

We can look for possible damage to the forest by comparing data from before the invasion in 2021 and during the invasion in 2022. It is usually best to compare the same time periods to account for seasonal changes. We wouldn’t want to compare summer in Ukraine 2021 with winter the following year – the vegetation and tree canopy would not be comparable even in the absence of armed conflict.

The image below displays the difference in NBR (dNBR) from June 1, 2021 to September 20, 2021 compared to the same time period in 2022.

![](https://www.bellingcat.com/app/uploads/2023/08/image_1-1-1200x614.png)

How the Tool Works

The OSINT Forest Area Tracker runs on Google Earth Engine, a geospatial platform that allows researchers to analyse remote sensing data by importing datasets from a range of satellite sources. These include true-colour images as well as colours that represent infrared wavelengths can be mapped onto the Earth’s surface. These different datasets are suitable for studying a wide range of characteristics such as temperature or moisture, which you wouldn’t see as easily in standard photographs.

**Sentinel-2 Satellite and Calculating Normalised Burn Ratio**

The data that the Forest Tracker uses comes from the Sentinel-2 satellite, which collects near-infrared (NIR) and shortwave infrared (SWIR) bands when or...
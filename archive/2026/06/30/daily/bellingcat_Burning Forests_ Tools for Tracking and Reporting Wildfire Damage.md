---
title: Burning Forests: Tools for Tracking and Reporting Wildfire Damage
url: https://www.bellingcat.com/resources/how-tos/2026/06/30/burning-forests-tools-for-tracking-and-reporting-wildfire-damage/
source: bellingcat
date: 2026-06-30
fetch_date: 2026-07-01T06:24:26.275425
---

# Burning Forests: Tools for Tracking and Reporting Wildfire Damage

* [Investigations](https://www.bellingcat.com/category/news/)
* [Resources](https://www.bellingcat.com/category/resources/)
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
* [Resources](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)
* [Donate](/donate)

[![](https://www.bellingcat.com/app/uploads/2024/08/Screenshot-2024-08-06-at-10.50.55-300x297.png)](https://www.bellingcat.com/author/galenreich/)
[Galen Reich](https://www.bellingcat.com/author/galenreich/)

Galen is an Investigative Technologist at Bellingcat. He uses his expertise in technical R&D to develop new tools, approaches, and visualisations for investigations.

[![Profile picture for: Wim Zwijnenburg](https://www.bellingcat.com/app/uploads/2026/06/Screenshot-2026-06-25-at-12.44.30.jpg)](https://www.bellingcat.com/author/wim-zwijnenburg/)
[Wim Zwijnenburg](https://www.bellingcat.com/author/wim-zwijnenburg/)

Wim Zwijnenburg is a Humanitarian Disarmament Project Leader for PAX.  He works on conflict and environment related issues in the Middle East, the use and proliferation of emerging military technologies and arms trade @wammezz

[![](https://www.bellingcat.com/app/uploads/2024/12/71088928.png)](https://www.bellingcat.com/author/environmentalinvestigationsteam/)
[Environmental Investigations Team](https://www.bellingcat.com/author/environmentalinvestigationsteam/)

We investigate animal trafficking, ecosystem destruction and environmental crimes using open sources at Bellingcat.

# Burning Forests: Tools for Tracking and Reporting Wildfire Damage

June 30, 2026

* [Copernicus](/tag/copernicus)
* [Environment](/tag/environment)
* [Fire](/tag/fire)

If you’ve seen reports of a wildfire in your region and you’re looking for open source data, [NASA’s fire-tracking tool](https://firms.modaps.eosdis.nasa.gov/) is often the first place to start. It provides a heat signature and an approximate location. But detection is only the first step in understanding what’s happened. In this guide, we explore ways to analyse and report on the scale and severity of wildfires, including those in protected areas where ecosystems are often most fragile. We also examine how often fires recur in the same region over multiple seasons, helping to identify patterns in fire activity as climate change reshapes [fire risk around the world](https://civil-protection-humanitarian-aid.ec.europa.eu/news-stories/news/eu-deploys-largest-ever-wildfire-response-2026-summer-2026-06-02_en).

Satellite imagery from [Copernicus Browser](https://browser.dataspace.copernicus.eu/) will be used to visualise the spread of the fire, and vegetation health indices to assess burn severity. The datasets will then be combined in [QGIS](https://qgis.org/) for more in-depth analysis. At each stage, suggestions will be offered for turning the data into clear, reportable findings.

Throughout this guide, a single case study will be used: Sicily’s Zingaro Nature Reserve. In 2025, [wildfires swept across the region](https://www.isprambiente.gov.it/en/news/fire-update-for-2025-in-italy-smoking-areas-and-impacts-on-forests-have-increased-compared-to-2024), destroying forests, grasslands and croplands. Located on the Capo San Vito peninsula, the reserve was so severely affected that sections remain [closed](https://www.riservazingaro.it/en/home/) today.

## **Visualising Scorched Earth**

When investigating a wildfire, it’s important to narrow down whenit occurred and whereit spread. The [Landsat](https://science.nasa.gov/mission/landsat/) and [Sentinel-2](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2) missions are well-suited to this task, providing regular free imagery of most of the Earth’s landmass.

Below are two sets of Sentinel-2 imagery showing conditions shortly before and after a fire on July 25, 2025,near [Capo San Vito, Sicily](https://www.google.co.uk/maps/place/Capo%2BSan%2BVito/%4038.1833492%2C12.661729%2C28417m). The top two images are true-colour, similar to what would be seen from an aeroplane window. The image on the top right shows an area of scorched earth on the eastern side of the peninsula, but the exact extent of the fire is difficult to determine because the colour of the ground has changed only slightly.

![](https://www.bellingcat.com/app/uploads/2026/06/Google-Earth-Pro-2019.jpg)

*Satellite images of Capo San Vito, Sicily, showing before (left) and after (right) a fire on July 25, 2025. Top row: true-colour imagery. Bottom row: false-colour imagery highlighting fire damage in red. Source: Contains modified Copernicus Sentinel data 2025, processed with Copernicus Browser.*

![](https://www.bellingcat.com/app/uploads/2025/05/question-mark.png)

## Support Bellingcat

Your donations directly contribute to our ability to publish groundbreaking investigations and uncover wrongdoing around the world.

[Donate](https://bellingcat.com/donate?utm_campaign=article_cta)

The bottom two images are false-colour and highlight the difference between healthy vegetation and burned areas. Such imagery is possible because Sentinel-2 captures bands of light outside the visible range, a technique known as multispectral imaging. In these images, the near-infrared (NIR) band is coloured green, and the shortwave infrared (SWIR) band is coloured red. Healthy vegetation mainly reflects NIR light, so it appears green, while burned areas mainly reflect SWIR light, so they appear red.

These images were created with [Copernicus Browser](https://browser.dataspace.copernicus.eu/), a free browser-based tool from the European Space Agency for accessing and working with Sentinel imagery. It allows users to browse the Sentinel-2 catalogue by date and visualise different band combinations. You don’t need an account to use the browser, but signing in enables additional features.

If you’d like to try Copernicus Browser without further explanation, you can go straight to the false-colour post-fire image [here](https://browser.dataspace.copernicus.eu/?zoom=12&lat=38.076&lng=12.75315&themeId=DEFAULT-THEME&visualizationUrl=U2FsdGVkX1%2BBZhJ8xySBKLMAJSJS5bfg%2FU5Pu8PA04ZqxzlMxECgvw3zDyHo5Bj%2BoJO%2FS9OF467xCqmy9o5T%2F8awdvPM3oEO1FLyJJF%2B0maocE9cHPxP2UZ6Glefq%2Ffr&datasetId=S2_L2A_CDAS&fromTime=2025-07-27T00%3A00%3A00.000Z&toTime=2025-07-27T23%3A59%3A59.999Z&layerId=6-SWIR&demSource3D=%22MAPZEN%22&cloudCoverage=100&dateMode=SINGLE).

To follow along step by step, first open [Copernicus Browser](https://browser.dataspace.copernicus.eu). Then to visualise Sentinel-2 imagery:

1. Zoom to the desired area on the map or use the search bar (San Vito Lo Capo, north-west Sicily)
2. Select the date of interest (‘2025-07-27’ selected below).
3. Select the layer of interest (‘True color’ by default; SWIR selected below).

![](https://www.bellingcat.com/app/uploads/2026/06/2-CopernicusGuide.jpg)

*Screenshot of Copernicus Browser. Annotations by Bellingcat.*

By identifying the last available image before the fire and the earliest image after it in which the full burn area is visible, it’s possible to establish the location and timeline of the fire.

This allows us to report the following finding: “Satellite imagery reveals the extent of the damage caused by wildfires across the Capo San Vito peninsula on Sicily’s northern coast between July 20 and July 27, 2025.”

*Extra exercise: Look up a recent fire (e.g., wildfires near Penco, Chile in January 2026), navigate to the affected location and try to visualise the burned area using Copernicus Browser.*
...
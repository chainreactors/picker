---
title: What’s in a Name? Discovering Clues Hidden in Google Maps Image Filenames
url: https://www.bellingcat.com/resources/2024/10/15/google-maps-image-filename-finder-tool/
source: bellingcat
date: 2024-10-16
fetch_date: 2025-10-06T18:56:10.934011
---

# What’s in a Name? Discovering Clues Hidden in Google Maps Image Filenames

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

[![](https://www.bellingcat.com/app/uploads/2024/08/Screenshot-2024-08-06-at-10.50.55-300x297.png)](https://www.bellingcat.com/author/galenreich/)
[Galen Reich](https://www.bellingcat.com/author/galenreich/)

Galen is Bellingcat’s tech community facilitator. His expertise is in technical research and development, and he now works with investigators and developers to create and improve tools for open source investigations.

# What’s in a Name? Discovering Clues Hidden in Google Maps Image Filenames

October 15, 2024

* [Geolocation](/tag/geolocation)
* [Guide](/tag/guide)

Google Maps is a treasure trove of information for open source researchers. Bellingcat frequently uses the platform’s [satellite imagery](https://www.bellingcat.com/news/2024/08/28/kenya-police-shoot-journalist-protests-finance-bill-demonstration-nakuru/) and [street view](https://www.bellingcat.com/news/2024/08/07/bangladesh-overthrow-resignation-sheikh-hasina-footage-open-source/) in investigations, and [user-written reviews](https://www.bellingcat.com/news/2024/03/30/kinahan-cartel-wanted-narco-boss-exposes-whereabouts-by-posting-google-reviews/) and [user-uploaded images](https://www.bellingcat.com/resources/2024/03/15/geolocating-a-us-far-right-fight-night/) have also been useful in identifying people and places.

One detail that we often don’t think about when viewing an image on Google Maps is its filename, which can provide useful contextual clues.

When a user uploads an image to Google Maps, it automatically gets tagged to a location. This can be a standalone image of a site, or an image linked to a review of a place. Anyone on the internet can view the image, but the filename is not visible by default.

That’s where the [Bellingcat Filename Finder](https://chromewebstore.google.com/detail/bellingcat-filename-finde/fdhodjpkigpaachejkipcghppfnnfdmp) can help. It’s a browser extension for [Google Chrome](https://www.google.com/intl/en_uk/chrome/) that runs in the background and grabs the filename from the data that Google Maps sends to your browser, then it displays the filename over the image in an unobtrusive black box.

After installing the extension, when you come across images on Google Maps on your Chrome browser, the filename for each image should automatically appear on the top left as shown in the example below.

![](https://lh7-qw.googleusercontent.com/docsz/AD_4nXd6cqJk5JlO6Hzjk6VmqNJFn013mm-9QG5ZmewWv1Cpp1TDGxqCt12YfXg10I8j5glOcpHKHgrQkdMMZu9ezww4zqB9kRD0NfDWaBrS6zh0v_UcgVIiVvvdnmEb1Af1vzqD1jScaZBamV4KzAVKLHbIDcM?key=77ZG9uRMHGJB4TF_O-I9wQ)

*Screenshot from Google Maps showing the Bellingcat Filename Finder adding filenames to images attached to a review*

## Finding Out When Images Were Taken

If you use an iPhone, you might be used to images called things like ‘IMG\_8928.jpg’. That’s just the “IMG” prefix followed by a number that goes up by 1 for every photo you take. This format isn’t very descriptive or helpful for an open source researcher.

But, if you use an Android phone, you might be more familiar with filenames that include the date and time that the image was taken:

* PXL\_20240830\_150806479.jpg
* IMG20240830150806.jpg
* IMG\_20240830\_150806.jpg
* 20240830\_150806.jpg

These filenames could be useful for researchers trying to chronolocate images or establish a sequence of events at a location. Filenames can also provide hints to the type of device used – the first example above starting “PXL” indicates that the photo was taken on a Google Pixel device. The date format indicates it was taken on the Aug. 30, 2024.

Not all the filenames shown by the Filename Finder will match the image’s original filename. For some images, it seems that Google changes the filename to the upload date, i.e. “2024-08-30.jpg”. Be careful when using filenames matching this format, as they probably refer to the image’s upload date instead of the image’s creation date.

## Other Potential Clues

Timestamps are typically the most common information you can extract  from image filenames, but this tool can also help obtain other clues – especially when images have been renamed before they are uploaded to Google Maps, as a [recent Bellingcat investigation](https://www.bellingcat.com/news/2024/10/14/opendream-ai-csam-vietnam/) demonstrates.

While investigating suspected links between a company called CasinoMentor and an “AI art” generation website called OpenDream, we found a Google Maps listing for CasinoMentor in Malta, which included the following photo uploaded by the company.

![](https://lh7-qw.googleusercontent.com/docsz/AD_4nXfFyBNwJ4oXLrvUGyYXnqkg5x_YRdavAi36SxygiG4xN6DQ1mnaPb9gWL4iUe6ns1eXCGcmp2-H4MGMSqiQU6TctqYqcPubZfOHdiUfRXBELoa4Ekwxzk0upfHJV1AfQxknvQip0EZ7DGZKMwYm9y8hQ-U?key=77ZG9uRMHGJB4TF_O-I9wQ)

*Image from CasinoMentor on Google Maps, filename and blurring added by Bellingcat (left) and user-uploaded image of the matching location in Vietnam from Google Maps (right)*

A reverse image search showed that the image was taken in Vietnam, where we also suspected OpenDream’s founders were based.

To better understand the context behind this photo we checked the image filename. This filename turned out to be “CMTeam.jpg”, implying that it showed the CasinoMentor team, and as we found with our geolocation, the team were in Vietnam despite the company’s address in Malta.

Read more about this investigation [here](https://www.bellingcat.com/news/2024/10/14/opendream-ai-csam-vietnam/).

---

*The Bellingcat Filename Finder was inspired by research by Kolina Koltai.*

*Featured image: Graphic by Galen Reich.*

*Bellingcat is a non-profit and the ability to carry out our work is dependent on the kind support of individual donors. If you would like to support our work, you can do so*[*here*](https://www.bellingcat.com/donate/)*. You can also subscribe to our Patreon channel*[*here*](https://www.patreon.com/bellingcat)*. Subscribe to our*[*Newsletter*](https://bellingcat.us14.list-manage.com/subscribe/post?u=c435f53a5568f7951404c8a38&id=4be345b082)*and follow us on Twitter*[*here*](https://twitter.com/bellingcat) *and Mastodon [here](https://mstdn.social/%40Bellingcat)*.

Share this article

* [![Bluesky](https://www.bellingcat.com/app/themes/bellingcat/assets/icons/svg/share-bluesky.svg)](https://bsky.app/intent/compose?text=What%E2%80%99s%20in%20a%20Name%3F%20Discovering%20Clues%20Hidden%20in%20Google%20Maps%20Image%20Filenames%20https%3A%2F%2Fwww.bellingcat.com%2Fresources%2F2024%2F10%2F15%2Fgoogle-maps-image-filename-finder-tool%2F)
* [![Twitter](https://www.bellingcat.com/app/themes/bellingcat/assets/icons/svg/share-twitter.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.bellingcat.com%2Fresources%2F2024%2F10%2F15%2Fgoogle-maps-image-filename-finder-tool%2F&text=What’s in a Name? Discovering Clues Hidden in Google Maps Image Filenames)
* [![Facebook](https://www.bellingcat.com/app/themes/bellingcat/assets/icons/svg/share-facebook.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.bellingcat.com%2Fresources%2F2024%2F10%2F15%2Fgoogle-maps-image-filename-finder-tool%2F)
* [![Linkedin](https://www.bellingcat.com/app/themes/bellingcat/assets/icons/svg/share-linkedin.svg)](https://www.linkedin.com/shareArt...
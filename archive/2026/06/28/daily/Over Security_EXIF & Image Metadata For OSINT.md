---
title: EXIF & Image Metadata For OSINT
url: https://secjuice.com/exif-image-metadata-for-osint/
source: Over Security
date: 2026-06-28
fetch_date: 2026-06-29T06:34:37.860415
---

# EXIF & Image Metadata For OSINT

[![Secjuice](https://secjuice.com/content/images/2026/06/secjuice-logo-v2.svg)](https://secjuice.com)

* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/osint/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write With Us](https://secjuice.com/join-secjuice-writing-team/)

[OSINT](/tag/osint/)

# EXIF & Image Metadata For OSINT

Metadata is the laziest, richest clue in OSINT and the most over-trusted. It burned a fugitive and an elite hacker, yet by 2026 it lies more than it tells. Read this.

* [![Guise Bule](/content/images/size/w100/2026/06/Bulehero.jpg)](/author/guise/)

#### [Guise Bule](/author/guise/)

Jan 28, 2026

[Tip Writer](https://ko-fi.com/secjuice)

![EXIF & Image Metadata For OSINT](/content/images/size/w2000/2019/03/curling800.jpg)

A fugitive on the run from a murder charge got caught because a magazine forgot to clean a photo. An "elite" hacker who taunted the FBI got his front door handed to them by a picture of his girlfriend. Both men understood encryption. Both men understood operational security. Both men were undone by a few bytes of text quietly riding along inside a JPEG that neither of them remembered was there.

That is the seduction of EXIF metadata. It is the laziest win in the whole of OSINT, the richest single clue a careless target ever leaves you, and the most over-trusted scrap of data in the entire discipline. People treat a GPS tag like a confession. It is not. It is unsigned, attacker controllable plaintext that anybody can edit or wipe in the time it takes to read this sentence, and by 2026 the easy wins are mostly gone. Every major social platform strips it on upload, so a clean image proves nothing, and a dirty one is trivially faked. The thesis of this whole article fits in one line. Metadata is a lead, never a verdict. Master it, corroborate it against the pixels and the world, and know exactly when it is lying to you.

## What Metadata Actually Is

Open any photo from a real camera or phone and there is a second document stapled to the picture you can see. EXIF holds the camera make and model, the lens, the exposure, the timestamps and, if location was on, the GPS coordinates. IPTC and XMP hold captions, copyright and editing history. The MakerNotes hold manufacturer specific blocks that casual scrubbers miss entirely, serial numbers, shutter counts, internal thumbnails, the kind of thing that ties an image to one specific physical camera body. There is even a fully formed lower resolution thumbnail baked inside most files, and we will come back to that one because it is a gift.

None of it is signed. None of it is verified. All of it was written by the device, which means all of it can be rewritten by anyone. Hold that thought through everything that follows.

## Pull Everything With ExifTool

Forget the pretty websites for a moment. The ground truth tool is [ExifTool](https://exiftool.org/?ref=secjuice.com), Phil Harvey's command line reader and writer, sitting at version 13 in 2026 and quietly powering almost every online viewer you have ever pasted a photo into. Learn the real thing and you stop trusting someone else's web wrapper to decide what you get to see.

Dump the lot, grouped and labelled, with `exiftool -G1 -a -s -ee photo.jpg`. That shows you the family each tag belongs to, the duplicate tags a lazy tool hides, and any nested embedded data. Want only the location? `exiftool -n -GPSLatitude -GPSLongitude -GPSAltitude -GPSImgDirection photo.jpg`, where `-n` hands you raw decimal degrees you paste straight into a map. Or just `exiftool photo.jpg | grep -i gps` to see position, altitude, speed and bearing in one shot. When you have a whole folder or a seized drive, surface only the geotagged files with `exiftool -r -if '$gpslatitude' -filename -gpsposition -createdate -csv DIR/ > geo.csv` and let it churn through thousands while you make tea.

And always read the MakerNotes. A scrubber that strips the obvious GPS tag will often leave the serial number sitting in the manufacturer block, and a serial number is how the academic forensics people tie a stack of images back to a single camera. There is real published work on source camera identification from exactly these fields, and it works because nobody remembers the MakerNotes are there.

## The Thumbnail Is A Second Photo

Here is the move that feels like cheating. Most JPEGs and RAW files store one or more embedded preview images inside the metadata, and those previews are frequently not updated when the visible photo is cropped or edited. The person crops their face out of the frame. The thumbnail still has the face.

Extract them and look. `exiftool -b -ThumbnailImage photo.jpg > thumb.jpg` and `exiftool -b -PreviewImage photo.jpg > preview.jpg`. Now lay the thumbnail next to the full frame. If they disagree, the difference is the original uncropped scene, the thing your target thought they had removed. The whole picture they deleted can be living on inside the picture they kept. Always pull the thumbnail before you decide an image has nothing to give you.

## Timestamps Lie In Lockstep

There are three EXIF dates and people only ever read one. DateTimeOriginal is capture. CreateDate is when it was digitised. ModifyDate is the last time the file was written. When those three diverge, something edited the file, and that divergence is itself a clue. Modern phones also stamp an OffsetTime or OffsetTimeOriginal tag carrying the device's UTC offset, which quietly hands you the shooter's time zone.

But none of it is true just because it is consistent. The timestamp is whatever the camera's clock was set to, and a wrong clock, accidental or deliberate, makes every date wrong together, in perfect agreement, looking utterly trustworthy. So you test the time against the one clock nobody can edit, the sun. Feed the object height, the shadow length, the date and the rough time into Bellingcat's Shadow Finder or into SunCalc and ask whether that lighting is even physically possible at that place on that day. A consistent set of EXIF dates is not a true date. The shadows do not have a settings menu.

## Geolocate Without GPS, Because There Won't Be Any

This is the part that separates 2026 from the playbook everyone half remembers. Stop expecting a GPS tag. Instagram, Facebook, X, LinkedIn, Snapchat and Reddit all strip metadata on upload, so a photo you pulled off social media is supposed to be clean. A scrubbed image is the default state of the modern internet, not the fingerprint of a careful operator, and reading too much into its absence is how amateurs talk themselves into a story.

So you start from the pixels, the way [Bellingcat](https://bellingcat.gitbook.io/toolkit/categories/image-video/metadata?ref=secjuice.com) taught the entire field. Reverse image search the scene first. Then chip away at the visible clues, the signage and the language on it, the architecture, the vegetation, the licence plates, the direction of the sun and the shadows, and confirm each one against satellite and Street View. As a lead generator only, the CERTH Geolocalizer bundled into the [InVID and WeVerify plugin](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/?ref=secjuice.com) will estimate a location from image content with no EXIF at all. Treat its guess as a hint that tells you where to start looking, never as the answer. The model points a direction. Your eyes close the case.

## When The Metadata Is Missing Or Suspect

If the file is clean or you simply do not trust it, move to forensics. Upload to [FotoForensics](https://fotoforensics.com/?ref=secjuice.com), Neal Krawetz's site, for Error Level Analysis and a clean metadata dump. Cross check it against [Forensically](https://29a.ch/photo-forensics/?ref=secjuice.com) at 29a.ch, which adds clone detection, noise analysis, a magnifier and its own metadata reader.

No...
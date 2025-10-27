---
title: Compute intersection size with HANA spatial data
url: https://blogs.sap.com/2023/04/07/compute-intersection-size-with-hana-spatial-data/
source: SAP Blogs
date: 2023-04-08
fetch_date: 2025-10-04T11:30:24.141333
---

# Compute intersection size with HANA spatial data

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Compute intersection size with HANA spatial data

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163433&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Compute intersection size with HANA spatial data](/t5/technology-blog-posts-by-members/compute-intersection-size-with-hana-spatial-data/ba-p/13569909)

![MichaelaHorv](https://avatars.profile.sap.com/8/e/id8e301a9fe9b061973b44af88a9a2eb4a7e523cbd9f704592ddfdb4a512bfa367_small.jpeg "MichaelaHorv")

[MichaelaHorv](https://community.sap.com/t5/user/viewprofilepage/user-id/135730)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163433)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163433)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569909)

‎2023 Apr 07
8:26 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163433/tab/all-users "Click here to see who gave kudos to this post.")

1,308

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP HANA Spatial](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Spatial/pd-p/de9a1528-5ec2-4e53-8fd1-65f670054c68)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA Spatial

  Software Product Function](/t5/c-khhcw49343/SAP%2BHANA%2BSpatial/pd-p/de9a1528-5ec2-4e53-8fd1-65f670054c68)

View products (2)

Imagine you were given a map divided into blocks, with a lake marked on it. And now you're supposed to decide to which block this lake belongs.

![](/legacyfs/online/storage/blog_attachments/2023/04/st_intersection_map-1.png)

Map with blocks and lake

For purposes of this post, let's assume we should select the block with the biggest overlap with the lake itself. In this case, both the blocks and the lake are represented as *ST\_GEOMETRY* types within our database. And we are accessing our database using the AMDPs.

The HANA database allows native handling of spatial data (see [here](https://help.sap.com/docs/SAP_HANA_PLATFORM/cbbbfc20871e4559abfd45a78ad58c02/e1c934157bd14021a3b43b5822b2cbe9.html?locale=en-US) for HELP page).

## ST\_INTERSECTS

To start us off, let's select just the blocks that have some kind of intersection with our lake. For this end, we can use the *ST\_Intersects( )* method. It is available for all *ST\_Geometry* types.

[(Help page)](https://help.sap.com/docs/SAP_HANA_PLATFORM/cbbbfc20871e4559abfd45a78ad58c02/7a19e197787c1014a13087ee8f970cce.html?locale=en-US)

If an intersection exists, this will return 1. Otherwise, 0.

```
If (BLOCKLOCATION.ST_Intersection(:lake) = 1)

Then

  -- this Blocklocation does have an intersection with our lake

End if;
```

So, we can get all the blocks that have some intersection with our lake. Now we need to sort them by their size.

## **ST\_INTERSECTION**

We can get an *ST\_Geometry* representation of the intersection using the *ST\_Intersection( )* method.[(Help page](https://help.sap.com/docs/SAP_HANA_PLATFORM/cbbbfc20871e4559abfd45a78ad58c02/7a199bec787c1014a467d1cab22ce87a.html?locale=en-US))

It returns an empty geometry if there is no intersection for the given two geometries. Otherwise, it return a geometry that describes the intersection.

```
Intersection = Blocklocation.st_intersection(:lake);
```

## **ST\_AREA**

Since we do have the geometry representation of the intersection, it should be easy to compute it's area, right? Just use *ST\_Area( )* method on the intersection?

```
Intersection_area = intersection.ST_Area( )
```

Well, not so quickly. The *ST\_Area* method can be used with geometries of types *ST\_Polygon* and *ST\_MultiPolygon*.

What are the possible results of the *ST\_Intersection* method? Well, any *ST\_Geometry*. Which can include *ST\_Point*, *ST\_Line* and *ST\_GeometryCollection*. And these will cause issues. So let's look at these in detail.

## **ST\_DIMENSION**

### ST\_Point and ST\_Line

It can happen that the whole intersection is actually just a point/line where the geometries touch. But they do not actually overlap. So, how can we filter these out? For example, by using the *ST\_Dimension( )* method.

[(Help page)](https://help.sap.com/docs/SAP_HANA_PLATFORM/cbbbfc20871e4559abfd45a78ad58c02/7a17e263787c1014b4e4edd821a0a357.html?locale=en-US)

```
If (intersection_area.st_dimension( ) = 0 or intersection_area.st_dimension( ) = 1)

Then

  -- these are points and lines, not interesting for us now

End if;
```

## **ST\_GEOMETRYTYPE**

### ST\_GeometryCollection

Another possibility is, that there can be multiple intersections. Like in this picture.

![](/legacyfs/online/storage/blog_attachments/2023/04/st_map2-1.png)

In this case, the value would be of type *ST\_GeometryCollection*. It's dimension would then be equal to the highest dimension of its parts. So, if our collection contains a line and a polygon, the dimension would be 2.

How can we recognize that we're dealing with a collection? We can use the *ST\_GeometryType( )* method.

```
If (intersection_area.st_geometryType( ) = 'ST_GeometryCollection')

Then

  -- now we know that our intersection area is a collection

End if;
```

So, how do we calculate the area of a collection? One option is to iterate over all the geometries within the collection and add all their respective areas.

## **ST\_NUMGEOMETRIES**

For iteration, it would be nice to know the number of geometries in the collection. Fortunately, there is a method for this, the *ST\_Numgeometries* method.

[Help Page](https://help.sap.com/docs/SAP_HANA_PLATFORM/cbbbfc20871e4559abfd45a78ad58c02/bc5fd860f2bc49c395578ebbfa08ec0d.html?locale=en-US)

And once we know the overall number, we can iterate over the collection and retrieve the individual geometries using the *ST\_GeometryN* method.

[Help page](https://help.sap.com/docs/SAP_HANA_PLATFORM/cbbbfc20871e4559abfd45a78ad58c02/2aabfbb17ae34945a8f16961f54d047d.html?locale=en-US)

```
for index_coll in 1..intsec.st_numgeometries(  )

do

  -- now we can iterate over the collection and access the Nth geometry each iteration like this

  Geom = intsec.st_geometryN( :index_coll );

End for;
```

## **Putting it all together**

So, how do we put this all together?

Let's return to our 4 blocks and a lake from the beginning and say we have:

* Lake -- the geometry representing the lake

* Blocks -- a table that has the geometries representing our blocks (geometry), plus their numbers (blocknumber)

```
-- we will use theselater  for iterating

DECLARE index_block, index_coll int;

-- here we get all the blocks with some intersection

Tmp_blocks = SELECT blocknumber,

  b.geometry.st_intersecion(:lake) AS intersection

  FROM blocks b

  WHERE b.geometry.st_intersects(:lake) = 1;

-- we get the intersections with actual area and for polygons, we calculate the area straight

Tmp_areas = SELECT blocknumber,

  Intersection,

  Intersection.st_dimension( ) AS dimension,

  Intersection.st_geometrytype( ) AS geomtype,

  CASE intsec...
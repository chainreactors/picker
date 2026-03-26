---
title: From Reality to Virtual Reality: The Impact of 3DGS on Training, Education, and Beyond
url: https://www.sei.cmu.edu/blog/from-reality-to-virtual-reality-the-impact-of-3dgs-on-training-education-and-beyond/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-03-25
fetch_date: 2026-03-26T04:32:08.847695
---

# From Reality to Virtual Reality: The Impact of 3DGS on Training, Education, and Beyond

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University

cmu-wordmark](https://www.cmu.edu)

About

Research and Development

Publications and Media

Education

Careers

Search

Mobile Menu

[# SEI Blog](/blog/)

1. [Home](/)
2. [Publications and Media](/publications-media/)
3. [Blog](/blog/)
4. From Reality to Virtual Reality: The Impact of 3DGS on Training, Education, and Beyond

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

White, R., Walsh, M., Ross, D., and Laughlin, R., 2026: From Reality to Virtual Reality: The Impact of 3DGS on Training, Education, and Beyond. Carnegie Mellon University, Software Engineering Institute's Insights (blog), Accessed March 25, 2026, https://doi.org/10.58012/hgz1-jm24.

Copy

APA Citation

White, R., Walsh, M., Ross, D., & Laughlin, R. (2026, March 25). From Reality to Virtual Reality: The Impact of 3DGS on Training, Education, and Beyond. Retrieved March 25, 2026, from https://doi.org/10.58012/hgz1-jm24.

Copy

Chicago Citation

White, Roxxanne, Matt Walsh, Dominic Ross, and Richard Laughlin. "From Reality to Virtual Reality: The Impact of 3DGS on Training, Education, and Beyond." *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, March 25, 2026. https://doi.org/10.58012/hgz1-jm24.

Copy

IEEE Citation

R. White, M. Walsh, D. Ross, and R. Laughlin, "From Reality to Virtual Reality: The Impact of 3DGS on Training, Education, and Beyond," *Carnegie Mellon University, Software Engineering Institute's Insights (blog)*. Carnegie Mellon's Software Engineering Institute, 25-Mar-2026 [Online]. Available: https://doi.org/10.58012/hgz1-jm24. [Accessed: 25-Mar-2026].

Copy

BibTeX Code

@misc{white\_2026,
author={White, Roxxanne and Walsh, Matt and Ross, Dominic and Laughlin, Richard},
title={From Reality to Virtual Reality: The Impact of 3DGS on Training, Education, and Beyond},
month={{Mar},
year={{2026},
howpublished={Carnegie Mellon University, Software Engineering Institute's Insights (blog)},
url={https://doi.org/10.58012/hgz1-jm24},
note={Accessed: 2026-Mar-25}
}

Copy

# From Reality to Virtual Reality: The Impact of 3DGS on Training, Education, and Beyond

![Headshot of Roxxanne White.](/media/images/White_Roxxanne_560x560.max-180x180.format-webp.webp)
![Headshot of Matthew Walsh.](/media/images/Walsh_Matthew_039_240429.360x36.max-180x180.format-webp.webp)

###### [Roxxanne White](/authors/roxxanne-white), [Matt Walsh](/authors/matthew-walsh), [Dominic A. Ross](/authors/dominic-ross), and [Richard Laughlin](/authors/richard-laughlin)

###### March 25, 2026

##### PUBLISHED IN

[Artificial Intelligence Engineering](/blog/topics/artificial-intelligence-engineering/)

##### CITE

<https://doi.org/10.58012/hgz1-jm24>

Get Citation

##### SHARE

The [*FY26 National Defense Authorization Act (NDAA)*](https://armedservices.house.gov/uploadedfiles/fy26_ndaa_conference_text_legislative_summary.pdf) underscores the importance of military training to ensure a ready and capable force. The [Department of Labor’s 2025 report, *America’s Talent Strategy*,](https://www.dol.gov/sites/dolgov/files/OPA/newsreleases/2025/08/Americas-Talent-Strategy-Building-the-Workforce-for-the-Golden-Age.pdf) similarly highlights the need to leverage innovative technologies to develop the next-generation workforce. A consistent theme across these and other strategy documents is that emerging technologies have the potential to transform how people are trained and educated. We explore here the use of extended reality (XR) as a potentially transformative training technology. XR can immerse individuals in virtual environments (virtual reality, or VR) or overlay digital elements onto the real world (augmented reality, or AR). [Empirical studies](https://link.springer.com/article/10.1007/s10055-019-00379-9) have demonstrated the effectiveness of XR for training cognitive, perceptual, and motor skills. Additionally, XR is less expensive than live training and may be the only safe option in many cases. Accordingly, private sector companies, along with the federal government, have made significant investments in XR.

However, while technologies for delivering virtual content have advanced rapidly, content creation is still extremely costly and time consuming. For example, it may cost [$100,000](https://www.designrush.com/agency/ar-vr/trends/virtual-reality-development-cost#:~:text=on%20the%20market.-,Virtual%20Reality%20App%20Development%20Cost:%20Lowest%20to%20Highest,cost%20from%20$90%2C000%20to%20$150%2C000.) and take up to a [year](https://shiifttraining.com/how-much-does-vr-training-cost-in-depth-guide/#:~:text=Interactivity%20is%20usually%20minimal%2C%20with,6%2D12%20months%20or%20longer.) to develop custom VR trainings. VR pipelines involve multiple stages, and asset creation alone can require [two or three months](https://www.quora.com/How-long-is-the-production-cycle-of-a-VR-content-Like-the-educational-content-made-by-immerse-VR-education) or more depending on the asset’s complexity and overall need. In essence, the technology for delivering virtual content has progressed faster than the technology for creating it. This makes it difficult to deliver XR training at scale and impossible to deliver tailored content at the time and point of need.

In this blog post, we describe a cutting-edge method for creating digital models of the physical world called [3D Gaussian Splatting (3DGS)](https://dl.acm.org/doi/10.1145/3592433). 3DGS captures the richness of real-world geometry, texture, and lighting directly from ordinary images or video data. The result is photorealistic 3D models of objects or scenes that people can interact with in real-time. We then describe how 3DGS can be incorporated into a production pipeline that enables anyone, anywhere, to create high fidelity digital models at any time.

## Innovations in 3D Modeling and Simulation

Over the past five decades, 3D modeling methods have evolved dramatically. Early approaches, known as *structure-to-appearance*, focused on representing an object’s geometry as a collection of linked vertices that form surfaces. These early 3D modeling methods built the object’s shape first, and then the same methods are used to apply color and textures to the surfaces to make them look realistic. Common techniques for capturing or constructing structure from physical objects include [LiDAR](https://en.wikipedia.org/wiki/Lidar), [photogrammetry](https://en.wikipedia.org/wiki/Photogrammetry), and [CAD/manual modeling](https://en.wikipedia.org/wiki/CAD_standards).

More recently, *volume-to-appearance* methods, which represent scenes as continuous 3D volumes, have emerged as an alternative for 3D modeling and rendering. They build a model of color and transparency at each point in the 3D space and composite this information along different viewpoints to render realistic images. While geometry can be recovered from the volumetric representation, it is not explicitly used for rendering appearance. Popular volume-to-appearance methods include [neural radiance fields (NeRF)](https://dl.acm.org/doi/10.1145/3503250) and [3D Gaussian Splatting (3DGS)](https://dl.acm.org/doi/10.1145/3592433). The Neural Radiance Field (NeRF) method reconstructs 3D geometry and appearance implicitly by training a neural network to match rendered rays to input data. As 3DGS intakes data and represents a scene by a cloud of splattable gaussian primitives that are optimized to render high quality novel views.

[![figure1_03252026](/media/images/figure1_03252026.max-1280x720.format-webp.webp)](/media/images/figure1_03252026.original.png)

Figure 1: Diagram shows sets of 3D modeling methods. Volume to appearance, which evolved out of the traditional structure-to-appearance method, uses 3DGS or NeRF to represent scenes as continuous 3D volumes.

Volumetr...
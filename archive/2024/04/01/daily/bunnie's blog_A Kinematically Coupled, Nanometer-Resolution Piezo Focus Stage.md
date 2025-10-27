---
title: A Kinematically Coupled, Nanometer-Resolution Piezo Focus Stage
url: https://www.bunniestudios.com/blog/?p=7066
source: bunnie's blog
date: 2024-04-01
fetch_date: 2025-10-04T12:14:50.328491
---

# A Kinematically Coupled, Nanometer-Resolution Piezo Focus Stage

---

[« Designing The Light Source for IRIS](https://www.bunniestudios.com/blog/2024/designing-the-light-source-for-iris/)

[A 2-Axis, Multihead Light Positioner »](https://www.bunniestudios.com/blog/2024/a-2-axis-multihead-light-positioner/)

## A Kinematically Coupled, Nanometer-Resolution Piezo Focus Stage

This post is part of a series about giving users a tangible reason to trust their hardware through my IRIS (Infra-Red, in-situ) technique for the [non-destructive inspection of chips](https://www.bunniestudios.com/blog/?p=6937). Previously, I discussed the [process of designing the IRIS light source](https://www.bunniestudios.com/blog/?p=7035) in some detail, as well as my [methodology for learning new things](https://www.bunniestudios.com/blog/?p=7025).

This post will describe the focus stage for IRIS.

[![](https://bunniefoo.com/iris/2024/imager-head_sm.jpg)](https://bunniefoo.com/iris/2024/imager-head.jpg)

The focus stage is the thing at the bottom of the above image, covered in a black foil and with red and black wires coming out of one side. It’s responsible for controlling the fine positioning of the sample in the “Z” direction.

**Background**

The depth of field of the 10x objective used on IRIS is estimated to be around 8.5 microns. This means that I need to be able to control the distance of the chip to the lens in steps much finer than 8.5 microns. Note that depth of field typically decreases with increasing magnification, so if we want to support even higher magnifications, we would need even smaller focus steps.

[![](https://bunniefoo.com/iris/2024/10x-ref1_sm.jpg)](https://bunniefoo.com/iris/2024/10x-ref1.jpg)

*Above: example of a calibration image used to measure the effective resolution of IRIS, which is about 4.75 pixels per micron with a 10x objective.*

The resolution limit of the Z-stepper motors on the [Jubilee](https://machineagency.github.io/science_jubilee/) motion platform is about 10 microns, so we can’t get our samples into perfect focus using the stepper motors of the motion platform alone (the Jubilee motion platform is the cage-like structure that the microscope is mounted in, you can read more about it [here](https://machineagency.github.io/science_jubilee/)). One solution to this is to use an additional fine-focus mechanism that has a limited range of motion, but a very fine increment.

A bit of searching around reveals that a couple ways to do this include a micropositioner (basically a very fine mechanical screw-type mechanism) or a piezoelectric (piezo) positioner. I’ve never used a micropositioner or a piezoelectric actuator before, but the piezoelectric actuator seemed appealing because it would be a solid-state design – more compact, and less mechanical parts to machine and tune. The downsides of a piezoelectric system seems to be a limited range of motion, a limited amount of actuation force, and some non-linearities in position versus voltage due to hysteresis mechanisms.

Unfortunately, piezoelectric actuators are expensive. They start around $1000, and go up from there if you need features like kinematic coupling. So, I decided I’d try to build one from scratch, because it seemed like the rare case where solving an interesting problem with a one-off solution is also cheaper than buying an off-the-shelf unit.

After a couple of days scouring the Internet for suitable actuators, I came across the PowerHap (TM) series of piezo actuators made by TDK. They are intended for automotive haptic interfaces, and are available as a [stock item at Digi-Key](https://www.digikey.com/en/products/filter/motors-ac-dc/178?s=N4IgTCBcDaIA4HsDuBTATgCwIZxAXQF8g) for around $20 in single unit quantities.

The larger actuators can produce a 100 micron deflection with a few Newtons of force. There are hysteric non-linearities, but they can be reduced with some preload and/or feedback mechanisms. Since the design is intended to be used with a dynamic auto-focus algorithm, absolute linearity is less important than monotonicity and repeatability (in other words, the non-linearities are probably not going to be an issue because we’re wrapping things in a feedback loop).

**Sidebar: Kinematic Coupling**

It would be convenient to be able to remove the fine focus stage to tweak a sample, and then place it back into the machine without affecting the repeatability of measurements. This would require a coupling that can mate to the stage with sub-micron accuracy with minimal effort. Simply shoving a plate onto a set of brackets or screw holes would not be able to achieve this level of precision. However, it turns out there is a well-established technique for accomplishing this: kinematic coupling.

I hadn’t heard of kinematic coupling until [Prof. Nadya Peek](https://www.hcde.washington.edu/peek), a collaborator on the IRIS project, advised me on the topic. The TL;DR is that in the most abstract sense, an object’s position in space can be precisely constrained with exactly six points of contact. Any less, and the object has a degree of freedom to move; but more importantly, any attempt to use more than six points means there is more than one stable solution for the position of the object.

Why does this matter? Because when systems are over-constrained, small imperfections in fabrication will cause extra constraints to fight with each other. You need to have a little bit of slop to ensure you can put things together without forcing parts together in ways that can damage them.

For example, I generally specify my screw holes to be at least 0.1mm, and ideally 0.2mm, larger than the screw meant to go through them. This makes it easier to assemble things, but it also means that every time I take things part and put them back together again, the final alignment of things moves around by about a hundred microns.

*A hundred microns!* That’s pretty big compared to the few-micron target of the focus stage.

It turns out that if you can reduce the coupling between the focus stage and its actuators to six points of contact, you can remove the stage and replace it repeatedly with a precision comparable to the size of the contact points. This is really desirable for being able to fiddle with samples without disrupting the work flow.

There’s some pretty good open-access material on how to design systems that are “exactly constrained”; this [chapter from MIT’s 2.76 course](https://ocw.mit.edu/courses/2-76-multi-scale-system-design-fall-2004/3aa5862a1724b75c3e4aa7a6fee6c511_reading_l3.pdf) and this [thesis](http://pergatory.mit.edu/kinematiccouplings/documents/theses/hart_thesis/chapter2.pdf) get into the meat-and bones of the topic.

However, the TL;DR is that the practical way to create an idealized “point of contact” is to push a sphere into a cylinder or a plane: for example, a ball bearing pushed onto a pair of dowels, or into a V-groove cut into a plate. If these are constructed from hard, smooth materials, you get pretty close to a perfect single point of contact. If you cut three V-grooves into a plate, and push three spherical bearings into the grooves, you’ve got six exact points of contact: a kinematic coupling!

The final piece missing is the force needed to make the system find its unique solution, i.e., the thing that pushes the spheres into the grooves. In the case of my microscope stage, the force comes from gravity acting on the top plate assembly, and nothing else.

**Mechanical Design**

[![](https://bunniefoo.com/iris/2024/annotated_piezo.png)](https://bunniefoo.com/iris/2024/annotated_piezo.png)

The idea behind the mechanical design is to keep it as simple as possible. The microscope stage itself is a simple slab of aluminum with three V-shaped grooves milled into it.

![](https://bunniefoo.com/iris/2024/piezo_top_plate_dwg.png)

There’s a few holes drilled into the plate to help with mounting samples, but it’s about as simple as you can get. I’ll link to all the design files and where to order parts at the end of the post....
---
layout: post
title: 3D Modeling Seems Problematic
date: 2017-10-17 16:30:00 -0700
categories: blog
tags: [gamedev, graphics, art]
---
I've been dabbling in 3D modeling a lot lately. For a recent gamejam, Orcajam 2017, I decided to spend
the weekend focusing on 3D modeling since it's not normally something I get to devote a large chunk of
time to. While it's always been pretty apparent that 3D modeling has a steep learning curve and complicated
interfaces, I came across a problem which affects even professionals:

In character modeling you reach several key points where it becomes very difficult to go back and make changes.

Namely, character modeling can be broken down into 3 main steps:

1. Modeling
2. Rigging
3. Animating

A friend of mine at the jam who works at a large studio in Vancouver said how at each of these steps there is a
very thorough and strict review process on any key character models, and after working on it myself, I can see
why.

* Going back from 3. to 2. - If you want to change the rig, you have to redo or adjust every animations you
have made up to that point.
* Going back from 2. to 1. - If you want to go back and change the model, you have to adjust the animation rig
afterwards, which varies with the size of the edit, but is often very time consuming.
* Going back from 3. to 1. - If you want to go back this far, you're going to have to put in a massive amount of
effort. In some cases you might get a better, faster result by just scrapping your model and starting from scratch.

Unfortunately this blog post is less about solving a straight-forward problem and more about presenting a very
complicated problem with no straight-forward solution. My time modeling convinced me that, although 3D modeling
interfaces may seem like a mess, it's more that the task is inherently complicated and there's such a wide variety
of tools and workflows that a cohesive and easy to understand UI (while not sacrificing functionality) is nearly
impossible.

The question is what could be done to improve this "points of no return" problem? Often you only find out problems
with the model or rigging after you're waist deep in the middle of rigging or animating. The only cure is experience
through past mistakes leading you to recognize the problem before you get to the point where it's difficult to change.

ZBrush changed the way many professionals do 3D modeling. Substance designer+painter as well. Is there some different
workflow which could be invented that would make stepping back between these steps easier? Or is the answer just making
the existing software smarter in a way that makes stepping back between steps involve less work?

These sorts of problems excite me. I just thought I'd voice it here and see if it causes a creative spark in anyone else.
If nothing else, it's the sort of problem that's fun to think about.

### I also learned that half-finished face models are horrifying.

![Face]({{site.url}}/assets/3d_model_face.png)

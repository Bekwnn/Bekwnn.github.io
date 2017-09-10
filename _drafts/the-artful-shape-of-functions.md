---
layout: post
title: The Artful Shape of Functions
tags: [gamedev, math, graphics]
---
Maybe I'm biased from my work with computer graphics, but I believe calculus and a strong
fundamental understanding of math which allows you to manipulate objects in a 3D space is
one of the most valuable tools in any game maker's toolkit. Granted, code that involves
highly math-sensitive operations tends to be a small part of any game's code base, but
the value of having *someone* with this knowledge working on a game adds a lot of value.

Suddenly motions and collisions are better, smoother. Better yet, they no longer follow
the stock engine rules, instantly making your game feel less "cheap". Objects fly around
in fancy motions with easing and accereration. [One example is a GDC 2016 talk on using math to
design a better jump.](https://www.youtube.com/watch?v=hG9SzQxaCm8)
 
**Let's define a goal:** We want to be comfortable enough with math that when we picture something
visually in our mind, we can then *derive* the math needed to achieve that effect.

That at least *sounds* like a powerful ability, doesn't it? If I had to equate it to something,
I'd equate it to an artist's ability to translate a mental image into a good brush stroke.
Of course in a 3D world we don't work with brush strokes. We work with functions.

To briefly demonstrate,

## Example #1: Ocean Waves

TODO: OCEAN WAVES FUNCTION

Here's what the code looks like for that:

```python
TODO
```

A very common technique when creating anything "noisy" is to layer several frequencies of a function
on top of one another. In this case, the above is several frequencies of this single function:

TODO: OCEAN WAVE SINGLE FREQUENCY

And the code:

```python
TODO
```

The single version of the function looks like a very simple, basic wave, doesn't it? All I had to do to
create an ocean then, was know how to make that shape, and know how to make it layered at different
frequencies. If you want a really impressive example of this technique, you can check out [a completely
texture-free ocean on ShaderToy.](https://www.shadertoy.com/view/Ms2SD1)

## Example #2: Bezier Curve

TODO picture of spirit flame attack from Ori

3D curves can be used to steer cameras or create interesting projectiles. Most projectiles with an arcing
path use some kind of physics, but what if you want the effect of an attack which travels in an arcing path
to an exact destination? Or a beam particle which bends while travelling between two targets? Overwatch makes
use of this very effect with two of its weapons which have a 'tether' effect:

TODO picture of symmetra and mercy LMB curving

TODO rest of bezier curve

## Example #3: Gradient

## Example #4: Shader Effects

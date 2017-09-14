---
layout: post
title: The Artful Shape of Functions
date: 2017-09-14 16:20:00 -0700
tags: [gamedev, math, graphics]
---
Maybe I'm biased from my work with computer graphics, but I believe calculus and a strong
fundamental understanding of math which allows you to manipulate objects in a 3D space is
one of the most valuable tools in any game maker's toolkit. Granted, code that involves
highly math-sensitive operations tends to be a small part of any game's code base, but
the value of having *someone* with this knowledge working on a game adds a lot of value.

Suddenly motions and collisions are better, smoother. Better yet, they no longer follow
the stock engine rules, instantly making your game feel less "cheap". Objects fly around
in fancy motions with easing and acceleration. Being comfortable with math empowers you
to more confidently alter things like jump behaviors, physics, or anything involving movement
in a 2D or 3D space.
 
**Let's define a goal:** We want to be comfortable enough with math that when we picture something
visually in our mind, we can then *derive* the math needed to achieve that effect.

That at least *sounds* like a powerful ability, doesn't it? If I had to equate it to something,
I'd equate it to an artist's ability to translate a mental image into a good brush stroke.
Of course in a 3D world we don't work with brush strokes. We work with math.

The rest of this post is going to give some examples of this skill in the hopes of
demonstrating its usefulness and inspiring ideas of your own.

## Example #1: Ocean Waves

![Ocean Waves]({{site.url}}/assets/Ocean_Waves_fig.png)

Here's what the code looks like for that:

```python
def oceanfunc(x):
    freq0 = wavefunc(x, 0.5, 0.5, 1.3)
    freq1 = wavefunc(x, 1.3, 0.12, 2.1)
    freq2 = wavefunc(x, 2.3, 0.03, 3.1)
    freq3 = wavefunc(x, 4.7, 0.015, 1)
    return freq0+freq1+freq2+freq3
```

A very common technique when creating anything "noisy" is to layer several frequencies of a function
on top of one another. In this case, the above is several frequencies of this single function:

![Single Wave]({{site.url}}/assets/Single_Wave_fig.png)

And the code:

```python
import numpy as np

def wavefunc(x, freq=1, amp=1, offset=0):
    return amp*(-np.abs(np.sin(freq*x+offset)))
```

Or to simply say it as math: `-|sin(x)|`

The single version of the function looks like a very simple, basic wave, doesn't it? All I had to do to
create an ocean then, was know how to make that shape, and know how to make it layered at different
frequencies. If you want a really impressive example of this technique, you can check out [a completely
texture-free 3D ocean on ShaderToy.](https://www.shadertoy.com/view/Ms2SD1) It uses the exact same `-|sin(x)|`
that is used above to create the ocean surface, but animates it by adding time as a parameter.

The same technique can be used to generate terrains, animate meshes, or a whole lot of other things I'm sure
I couldn't think of. You could, for example, use different frequencies of the music playing in your game as
part of a function to animate the landscape or enemies.

## Example #2: Bezier Curve

![Ori Spirit Flame]({{site.url}}/assets/OriCurve.png)

3D curves can be used to steer cameras or create interesting projectiles. Most projectiles with an arcing
path use some kind of physics, but what if you want the effect of an attack which travels in an arcing path
to an exact destination? Or a beam particle which bends while travelling between two targets? In **Ori and the
Blind Forest**, your basic attack is a simple homing missle. In terms of gameplay, it's a slightly boring way
to attack enemies, so the devs decided to make it visually interesting by having it fire as randomly curving
projectiles. Even if the attack is a bit boring from a mechanical standpoint, it's interesting visually. By
doing this, the devs made a simple way to attack enemies that doesn't distract you from the core focus of the
game: platforming.

Another example is **Overwatch**. Overwatch makes use of this very effect with two of its weapons which have a
'tether' effect:

![Overwatch Beams]({{site.url}}/assets/OverwatchCurve.png)

These tethers don't just look good, but also serve a gameplay purpose: when the target you're attacking or
healing is almost out of range, the tether becomes tense and straight. When they're closer, it's more bendy
and loose. The shape of the tether gives the player a rough understanding of how close they are to losing
their target.

Here's a graphed cubic bezier curve:

<p align="center">
<img src="{{site.url}}/assets/Cubic_Bezier_fig.png">
</p>

Defined in code:
```python
def beziercurve(p0, p1, p2, p3, t):
    return ((1-t)**3)*p0 + 3*((1-t)**2)*t*p1 + 3*(1-t)*(t**2)*p2 + (t**3)*p3
```

Defined as math:

<p align="center">
<img src="{{site.url}}/assets/Cubic_Bezier_eq.png">
</p> 

Where `t` is a parameter between 0 and 1 travelling along the curve from p0 to p3, and for this example:

* p0: (1, 0)
* p1: (0, 3)
* p2: (4, 6)
* p3: (4, 0)

These curves and similar types of curves are used absolutely everywhere in not just games but graphics applications
in general. You'll find them in photoshop, mspaint, blender and maya, and even built into most major game engines
(Unity: AnimationCurve class, UE4: curve editor). You can use them to create more interestingly shaped beams or
projectiles, or to lay down paths such as a road or a set of roller-coaster tracks. 

## Example #3: Gradient, Fluids, Gasses, Vector Fields 

This example refers to the [*math gradi**e**nt*](https://en.wikipedia.org/wiki/Gradient) rather than a *color gradi**a**nt*.
The gradient is used in a bunch of things in games, one of the most notable being perlin noise:

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/d/da/Perlin_noise.jpg">
</p>

The simplest way to think of the gradient is that it's a vector or field of vectors which point in the direction that the
function changes most rapidly. If your function for example was some height map `z = f(x,y)` type function which forms a
surface that looks like a grassland of rolling hills, then the gradient of that function is an (x,y) vector which will always
point 'directly uphill': the direction where Z is increasing the most.

Robert Bridson, who has written a number of papers and even a book on fluid simulations, [wrote a paper titled, **Curl-noise For
Procedural Fluid Flow**](https://www.cs.ubc.ca/~rbridson/docs/bridson-siggraph2007-curlnoise.pdf). While there are other aspects
to the paper, the gist of it is that he creates a vector field which could be used to push around fluids like water or gasses
like air in a convincing way. For the sake of creating a similar effect in 2D, you could simply cheat and use 'the gradient
rotated by 90 degrees in one direction' to achieve a similar vector field.

The gradient, divergence, and curl all have a place in simulating liquids and gasses, but the notion of vector fields has a
much broader application.

<p align="center">
<img src="{{site.url}}/assets/Flow_Map.png">
</p>

Above is a 2D vector field in the form of a red and green texture, where red would correspond to X and green to Y. The vector field
it represents is something a bit like a whirlpool.

[In **Left 4 Dead 2**](http://www.valvesoftware.com/publications/2010/siggraph2010_vlachos_waterflow.pdf), Valve used a similar texture
to make the water in a large swamp area seem like it was flowing around objects and in certain directions. The red and green
data of the texture represented a 2D vector field of forces, deciding how the texture of the water would move. The flow of the
water actually served a gameplay purpose, as it flowed towards the area the players were meant to go. This subtle environment
detail kept players oriented and prevented them from getting turned around and accidentally backtracking back to the beginning
of the swamp.

## In Closing

Now, more complicated math can generally be harder and take longer to implement, and when it comes down to things like implementing
volume-preserving mesh animations, which is probably not something that you're going to do outside of a large team, and as a very
specific member of that large team. However, even in an indie title, it can be a very good idea to put extra effort into a certain
effect to create a visual uniqueness to your game that will 'wow' players if it's something they've never seen before.

For one example: **Journey** by *thatgamecompany*, not only flew employees out to a desert to photograph it, but dedicated a large amount
of development time to absolutely nailing the look and feel of the sand in the game. The game went on to be a huge success. Its
visual splendor was a large contributing factor to its success, and the sand specifically was a large contributing factor to that
aforementioned visual splendor.

![Journey Sand]({{site.url}}/assets/JourneySand.jpg)

Games are unique compared to movies, art, or books because it is an interactive medium. To play to the medium's strengths, means to take
full advantage of that interactivity. Some games may play to this strength by presenting the player with difficult options to choose
from, such as in an RPG. Other games may give players infinite options in a sandbox environment and let them freely interact with
the world in the way they see fit.

This article is aimed at games which increase their interactivity by creating interesting interactions in a 3D or 2D space. By creating
more interesting ways of interacting with a virtual world, we can leverage the medium's strengths.

Hopefully this illustrates the value of being able to derive the mathematical functions from your visual imagination. If you know the basic
ways in which you can make curves and shapes, you can take the picture in your head, break it up into a mathematical function, and then
implement it.

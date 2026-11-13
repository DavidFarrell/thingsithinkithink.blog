---
title: "Using Jev to Answer the Internet's Hardest Questions"
date: 2026-11-16T06:00:00Z
slug: /11-16-jev-hardest-questions/
description: "Settling some old arguments with TypeSafe's Jev."
image: images/2026/11-16-jev-hardest-questions/dress-hero-16x9.png
categories:
  - blog
  - artificial-intelligence
tags:
  - ai
  - typesafe
  - jev
draft: false
---

Last Thursday I was at a Figma AI event, [How AI Built This with Figma](https://luma.com/29zm6gmg). I'm going to write up the event properly later, but one of the demos was showing off how Figma used [Jev](https://typesafe.ai) - TypeSafe's model that answers questions with typed outputs and probabilities rather than generated text - and somebody made a joke about how we could finally figure out what colour that dress was.

Inspired by that, I have decided it's finally time to answer each of the internet's hardest questions.

## The Dress

We have to start with the 2015 [dress](https://en.wikipedia.org/wiki/The_dress) that split the internet between folk who saw it as blue and black and folk who saw it as white and gold.

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/dress.png" caption="The dress" width="280" >}}

```json
{
  "The Dress!": {
    "type": "choice",
    "instructions": "What colours is the dress in `photo`?",
    "criteria": {
      "Blue and black": "The dress is blue with black lace stripes",
      "White and gold": "The dress is white with gold lace stripes"
    }
  }
}
```

{{< figure src="/images/2026/11-16-jev-hardest-questions/dress-jev.png" caption="Jev's verdict" >}}

Jev itself seems a bit confused here, but leans towards blue and black, which is obviously wrong.

## The Checker Shadow

Going way back to 1995, we have [Edward Adelson's checker shadow illusion](https://en.wikipedia.org/wiki/Checker_shadow_illusion), in which squares A and B look like different shades but are in fact the same shade.

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/checker-shadow.png" caption="The checker shadow" width="420" >}}

```json
{
  "The Checker Shadow!": {
    "type": "choice",
    "instructions": "Which is darker in `photo`, square A or square B?",
    "criteria": {
      "Square A": "Square A is darker than square B",
      "Neither": "Squares A and B are exactly the same shade of grey"
    }
  }
}
```

{{< figure src="/images/2026/11-16-jev-hardest-questions/checker-jev.png" caption="Jev's verdict" >}}

Jev nails this one.

## The Strawberries

In 2017 Akiyoshi Kitaoka shared [this photo of strawberries](https://www.sciencealert.com/in-spite-of-what-your-eyes-tell-you-these-strawberries-aren-t-red) that look red but don't contain a single red pixel.

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/strawberries.png" caption="The strawberries" width="320" >}}

```json
{
  "The Strawberries!": {
    "type": "choice",
    "instructions": "What colour are the strawberries in `photo`?",
    "criteria": {
      "Red": "The strawberries are red",
      "Grey": "The strawberries are grey"
    }
  }
}
```

{{< figure src="/images/2026/11-16-jev-hardest-questions/strawberries-jev.png" caption="Jev's verdict" >}}

I was surprised by this one - Jev sees them as red. I'd have thought this particular illusion was a variation on the checker shadow, so I expected Jev to get it correct here.

## The Müller-Lyer Illusion

The [Müller-Lyer illusion](https://en.wikipedia.org/wiki/M%C3%BCller-Lyer_illusion) is an interesting one - all of the lines are the same length, but the arrowheads make some look longer than others. It usually comes in two versions, so I sent them to Jev one at a time with the same question.

```json
{
  "The Müller-Lyer Illusion!": {
    "type": "choice",
    "instructions": "Which line in `photo` is longer?",
    "criteria": {
      "The left line": "The left line is longer than the right line",
      "Neither": "Both lines are exactly the same length"
    }
  }
}
```

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/muller-joined.png" caption="The lines joined" width="480" >}}

{{< figure src="/images/2026/11-16-jev-hardest-questions/muller-joined-jev.png" caption="Jev's verdict" >}}

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/muller-apart.png" caption="The lines apart" width="480" >}}

{{< figure src="/images/2026/11-16-jev-hardest-questions/muller-apart-jev.png" caption="Jev's verdict" >}}

What's interesting here is the difference between how Jev performs on the two. With the lines joined it's a coin flip, leaning slightly towards the illusion, but with the lines apart it's fairly sure they're the same length. Also notice how its confidence differs between the two - 10% with the lines joined versus 54% with them apart.

## The Ebbinghaus Illusion

In the same vein, we've got the [Ebbinghaus illusion](https://en.wikipedia.org/wiki/Ebbinghaus_illusion), in which the two orange circles are exactly the same size but appear different sizes because of the circles around them.

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/ebbinghaus.png" caption="The Ebbinghaus illusion" width="480" >}}

```json
{
  "The Ebbinghaus Illusion!": {
    "type": "choice",
    "instructions": "Which orange circle in `photo` is bigger?",
    "criteria": {
      "The right circle": "The orange circle on the right is bigger than the one on the left",
      "Neither": "Both orange circles are exactly the same size"
    }
  }
}
```

{{< figure src="/images/2026/11-16-jev-hardest-questions/ebbinghaus-jev.png" caption="Jev's verdict" >}}

I'm kind of liking the fact that Jev falls for the same illusions that people do. But you can see the difference here between a typical decision and a decision with confidence. Jev picks the right circle, but it's only 50% confident, and you can add a lot of nuance to your system when you have confidence as well as a decision.

## The Café Wall

In the [café wall illusion](https://en.wikipedia.org/wiki/Caf%C3%A9_wall_illusion) the horizontal lines are perfectly straight and parallel, but the offset tiles make them look like they slope. However, this one tricks people but not Jev.

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/cafe-wall.png" caption="The café wall" width="480" >}}

```json
{
  "The Café Wall!": {
    "type": "choice",
    "instructions": "Are the horizontal lines in `photo` sloped or straight?",
    "criteria": {
      "Sloped": "The horizontal lines slope and are not parallel",
      "Straight": "The horizontal lines are straight and parallel"
    }
  }
}
```

{{< figure src="/images/2026/11-16-jev-hardest-questions/cafe-jev.png" caption="Jev's verdict" >}}

Jev nails this one.

## The Duck-Rabbit

The [duck-rabbit](https://en.wikipedia.org/wiki/Rabbit%E2%80%93duck_illusion) doesn't really have an answer, I think, but here's what Jev thinks anyway. (I cut off the original caption, since it gives the game away.)

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/duck-rabbit.png" caption="The duck-rabbit" width="380" >}}

```json
{
  "The Duck-Rabbit!": {
    "type": "choice",
    "instructions": "What animal is in `photo`?",
    "criteria": {
      "Duck": "The animal is a duck",
      "Rabbit": "The animal is a rabbit"
    }
  }
}
```

{{< figure src="/images/2026/11-16-jev-hardest-questions/duck-jev.png" caption="Jev's verdict" >}}

I think I lean slightly towards rabbit too.

## Rubin's Vase

[Rubin's vase](https://en.wikipedia.org/wiki/Rubin_vase) feels a bit unfair to me, because I don't think it's either - it's both.

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/rubin-vase.png" caption="Rubin's vase" width="260" >}}

```json
{
  "Rubin's Vase!": {
    "type": "choice",
    "instructions": "What is in `photo`?",
    "criteria": {
      "A vase": "A vase",
      "Two faces": "Two faces looking at each other"
    }
  }
}
```

{{< figure src="/images/2026/11-16-jev-hardest-questions/vase-jev.png" caption="Jev's verdict" >}}

Jev, however, sees faces as more likely (but with low confidence).

## My Wife and My Mother-in-Law

[My Wife and My Mother-in-Law](https://en.wikipedia.org/wiki/My_Wife_and_My_Mother-in-Law) is the oldest one I'm aware of (the earliest known version is an 1888 German postcard), and it's one where I'm able to switch which version I see depending on which part of the image I focus on.

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/wife-mother-in-law.jpg" caption="My Wife and My Mother-in-Law" width="280" >}}

```json
{
  "My Wife and My Mother-in-Law!": {
    "type": "choice",
    "instructions": "How old is the woman in `photo`?",
    "criteria": {
      "Young": "A young woman looking away",
      "Old": "An old woman in profile"
    }
  }
}
```

{{< figure src="/images/2026/11-16-jev-hardest-questions/wife-jev.png" caption="Jev's verdict" >}}

However, Jev seems to really lean towards the young wife rather than the mother-in-law.

## Dog or Mop

The dog in dog or mop is a [Komondor](https://en.wikipedia.org/wiki/Komondor). I picked A and B (outlined in blue) and asked about each one.

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/dog-mop.jpg" caption="Dog or mop" width="420" >}}

```json
{
  "Dog or Mop!": {
    "type": "choice",
    "instructions": "Is `photo` a dog or a mop?",
    "criteria": {
      "Dog": "A dog",
      "Mop": "A mop"
    }
  }
}
```

{{< figure src="/images/2026/11-16-jev-hardest-questions/mop-a-jev.png" caption="A" >}}

{{< figure src="/images/2026/11-16-jev-hardest-questions/mop-b-jev.png" caption="B" >}}

Good news for dogs - Jev can tell the difference.

## The Impossible Elephant

Roger Shepard's [impossible elephant](https://en.wikipedia.org/wiki/Shepard_elephant) swaps its legs with the gaps between them, so it's hard to say how many legs it has.

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/elephant.jpg" caption="The impossible elephant" width="338" >}}

```json
{
  "The Impossible Elephant!": {
    "type": "choice",
    "instructions": "How many legs does the elephant in `photo` have?",
    "criteria": {
      "Four": "The elephant has four legs",
      "Five": "The elephant has five legs"
    }
  }
}
```

{{< figure src="/images/2026/11-16-jev-hardest-questions/elephant-jev.png" caption="Jev's verdict" >}}

I like the fact that Jev isn't sure here, because there really isn't a correct answer.

## Chihuahua or Muffin

And finally, we'll finish with two classics. First, the famous [chihuahua or muffin](https://www.npr.org/sections/thesalt/2016/03/11/470084215/canine-or-cuisine-this-photo-meme-is-fetching) meme. I took these four and sent them to Jev one at a time.

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/chihuahua-muffin.jpg" caption="Chihuahua or muffin" width="360" >}}

```json
{
  "Chihuahua or Muffin!": {
    "type": "choice",
    "instructions": "Is `photo` a chihuahua or a muffin?",
    "criteria": {
      "Chihuahua": "A chihuahua",
      "Muffin": "A blueberry muffin"
    }
  }
}
```

{{< figure src="/images/2026/11-16-jev-hardest-questions/chihuahua-tl-jev.png" caption="Top left" >}}

{{< figure src="/images/2026/11-16-jev-hardest-questions/chihuahua-tr-jev.png" caption="Top right" >}}

{{< figure src="/images/2026/11-16-jev-hardest-questions/chihuahua-bl-jev.png" caption="Bottom left" >}}

{{< figure src="/images/2026/11-16-jev-hardest-questions/chihuahua-br-jev.png" caption="Bottom right" >}}

The good news here is that Jev can be trusted for food safety.

## Labradoodle or Fried Chicken

A variation on the above, [labradoodle or fried chicken](https://www.npr.org/sections/thesalt/2016/03/11/470084215/canine-or-cuisine-this-photo-meme-is-fetching). I sent each of these separately.

{{< figure-center src="/images/2026/11-16-jev-hardest-questions/labradoodle-chicken.jpg" caption="Labradoodle or fried chicken" width="480" >}}

```json
{
  "Labradoodle or Fried Chicken!": {
    "type": "choice",
    "instructions": "Is `photo` labradoodles or fried chicken?",
    "criteria": {
      "Labradoodles": "Labradoodle puppies",
      "Fried chicken": "Fried chicken"
    }
  }
}
```

{{< figure src="/images/2026/11-16-jev-hardest-questions/labradoodle-left-jev.png" caption="Left half" >}}

{{< figure src="/images/2026/11-16-jev-hardest-questions/labradoodle-right-jev.png" caption="Right half" >}}

I'm a wee bit worried about the labradoodles here, given that Jev is almost 30% convinced they're chicken.

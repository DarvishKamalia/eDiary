August 1, Saturday, Exercises
-----------------------------

### Know myself

In this exercise, each one of you will create a personal webpage. This webpage
will include 3 things : your **name**, your **picture**, and a short **bio**
of yours. Here's how we will go about doing this:

- First you will write down the above three pieces of information in a regular
  `.txt` file
- Then, you will add some HTML to this `.txt` file and save it as a `.html` file. 
  Once you do that, you will be able to view the webpage in your browser. 
- But the webpage will not look too nice, because we haven't added any styling yet.
  Hence, in this step, you will create a new file that ends in `.css` and add
  some CSS code to it.
- And lastly, you will *link* the `.html` and the `.css` files you created, to
  view the final, nicely styled version of your webpage. 

### Know my group

Now we all know that websites generally do not have single pages; it's actually
a collection of pages *linked* together. So that's what we're going to do here.
You will email the webpage that you created in the previous exercise (i.e. you
will email both the `.html` and the `.css` files) to everyone else in your
group.

So now, everyone has 5/6 different webpages. At this stage, what you'll do is,
you'll go to your original webpage, and add *links* on it to these other
webpages that you just received from your group members via email. 

### Let's play

And finally, for our last exercise of the day, we will write a little Python
program to simulate something you've all probably learned in Physics/Chemistry:
**brownian** motion. What happens when you put a drop of ink in a glass of
water? The ink particles randomly disperse through the water. Our program is
going to simulate the random motion of one such particle.

We will assume that at the start (when the drop of ink has *just* landed in
the glass of water), the position of the particle is \[0, 0\] (origin). Then, at each
step, the particle can either move 1 unit North, 1 unit South, 1 unit East,
or 1 unit West. Because it's motion is random, it can go North, South, East, 
or West with equal probability.

Say it went 1 unit North in its first step. Then, the position of the particle
after the first step would be \[0, 1\]. Say it went 1 unit West in the second
step. Then, its position would become \[-1, 1\]. Say it went 1 unit East in the
third step. Then, its position would become \[0, 1\]. 

Can you write a program which will simulate such motion for a large number of
steps (such as 100, 500, 1000, etc) and tell you the distance of the ink particle
from the origin at the end? 

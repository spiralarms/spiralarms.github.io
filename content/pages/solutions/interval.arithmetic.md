title: Interval arithmetic
slug: interval-arithmetic

Let's take some expression, $f(A,B,C,...)$, where intervals may
occur several times. As W.Z. proposes, we can find the correct resulting
interval by Monte-Carlo. All occurrences of e.g. $A$ in the formula should
get the same value at every MC step (of course this value may be
different for different MC steps). I especially like this method as not
only it solves the problem of dependencies, but it finds the correct
answer without any approximations.

But how to find the correct resulting interval analytically?

When formula is nonlinear, it may have an extremum inside an interval.

Example:
$f(x)=(x-2)(x-4)$ has a minimum $-1$ at $x=3$.
For an expression $(A-2)*(A-4)$, where $A=(2, 4)$,
Monte Carlo method gives $(-1,0)$.

It is easy to build functions of intervals, that cannot be transformed
to the form with only one occurrence of every independent interval.

Example:
$f(x)=\frac{A+B}{A+C}$

In order to find the resulting interval we have to treat
the expression with intervals as a real function of (probably several)
real variables, and independent
intervals define its domain. We should find global minimum and maximum
of that function on that domain, either analytically or by Monte Carlo
method, and these extrema are the answer, the resulting interval.
We should not work with functions that have bad behavior anywhere in
their domains. Good function is defined at any point of the domain and
its border, it should be at least bounded for using Monte Carlo methods.
In order to use analytical methods we should require more properties,
e.g. the function of interval variables should be differentiable.

In this method the problem of dependent intervals disappears, $A/A$ is
always 1, and there is no difference between equivalent expressions like
formulas for resistance in the book.

This is the explanation of why SICP states that this problem is very
difficult. Finding global extrema of a function of several variables IS
very difficult per se. Analytical methods are not good when the number
of variables (intervals) increases or when function has complex profile.
You can find thousands of local minima and still not be sure that your
running minimum is anywhere near the global minimum. Gradient methods
also cannot guarantee anything. The last resort is Monte Carlo, but you
can be unlucky with it :).

The problem is difficult in general case but for many practical
applications MC method works, and other numerical and analytical methods
may work too.

The practical answer to the exercise 2.16 is "Use Monte Carlo".

### Repost of my comment on http://community.schemewiki.org

We have to leave the realm of interval arithmetic as soon as we start
to talk about functions that have extrema somewhere inside intervals,
or about functions like $(A+B)/(A+C)$, which in principle cannot be reduced
to the form with one occurrence of each variable. This is the meaning of
dependency problem. By using interval arithmetic we will always get wrong
results for such functions. We cannot find correct answers using
interval arithmetic, but we can find them by using
analytical or numerical methods, e.g. Monte Carlo method.
It’s the problem of finding global minimum of a function of several variables.
I saw the proposal to use MC in Weiqun Zhang’s blog
(in fact it is a standard method of finding extrema for very complex functions).
MC works even when all analytical methods fail.
Dependency problem does not exist for these methods.
For example, when you calculate $A/A$ with Monte Carlo method,
you just submit the same random value inside the interval to
ALL occurrences of A in the formula, e.g. for $A/A$ the value of
the function will be 1, no matter how many random values you generate.
Do not work with intervals that span zero if you want to get
correct result for that formula. Then you take the min/max of all
function values (all of them were 1), and voila,
final result is 1 with ZERO TOLERANCE or zero width.
Well, you could cancel numerator and denominator from the very beginning,
MC and analytical methods allow it.

Code
```
:::python
import random

# intervals
intA = (2, 4)
intB = (-2, 0)
intC = (10, 20.5)

# function of three intervals
def f(A, B, C):
    #return (A+B)/(A+C)
    return (A - 2) * (A - 4)

# calculation of the resulting interval
N = 1000000
minf = 1e80
maxf = -1e80
for i in range(N):
    A = random.uniform(intA[0], intA[1])
    B = random.uniform(intB[0], intB[1])
    C = random.uniform(intC[0], intC[1])
    res = f(A, B, C)
    if minf > res: minf = res
    if maxf < res: maxf = res

print("Monte-Carlo method")
print("min = %6.2f" % (minf))
print("max = %6.2f" % (maxf))
```

Output
```
:::text
Monte-Carlo method
min =  -1.00
max =  -0.00
```

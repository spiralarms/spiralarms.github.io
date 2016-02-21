title: Counting change
slug: sicp-counting-change

SICP (p. 53) invites us to find an iterative algorithm for counting
change. I was not able to do it using Scheme. Here are two algorithms
in Python.

The first one uses memoization for turning tree-recursive process to
much more effective one, as explained in the book. It works as
advertised.

Code
```
:::python
# recursive counting change with memoization
# super optimal algorithm

# amount
a = 100

# denominations
m = [1,5,10,25,50]

# storage for memoization
dictionary = {}

calls = 0 # number of calls
depth = 0 # current tree depth
maxdepth = 0 # maximal tree depth

def memo_change(a, kinds):
	global dictionary
	global calls, depth, maxdepth

	pair = (a, kinds)
	if pair in dictionary.keys():
		return dictionary[pair]

	depth = depth + 1
	if maxdepth < depth:
		maxdepth = depth
	calls = calls + 1

	ways1 = 0
	if a > m[kinds-1]:
		ways1 = memo_change(a - m[kinds-1], kinds)
	else:
		if a == m[kinds-1]:
			ways1 = 1

	ways2 = 0
	if kinds>2:
		ways2 = memo_change(a, kinds - 1)
	else:
		if a % m[kinds - 1] == 0:
			ways2 = 1

	ways = ways1 + ways2

	dictionary[pair] = ways

	depth = depth - 1
	return ways


print "amount = ", a, "  ways = ", memo_change(a, len(m)), \
"  calls = ", calls, "  max depth = ", maxdepth
```

Output
```
:::text
amount =  100   ways =  292   calls =  44   max depth =  8
```

So far so good. Is it possible to invent something more iterative
and not use additional data structure? Hmmm...

Code
```
:::python
# iterative counting change
# optimal algorithm with finding every variant of change
# but how to implement these nested loops in scheme?

# amount
a = 100

# denominations
m = [50,25,10,5,1]

# number of calls
calls = 0

def iter_change(a):
	global calls
	count = 0
	for i0 in range(a//m[0] + 1):
		for i1 in range((a - i0*m[0])//m[1] + 1):
			for i2 in range((a - (i0*m[0] + i1*m[1]))//m[2] + 1):
				for i3 in range((a - (i0*m[0] + i1*m[1] + i2*m[2]))//m[3] + 1):
					if (a - (i0*m[0] + i1*m[1] + i2*m[2] + i3*m[3])) % m[4] == 0:
						count = count + 1
					calls = calls + 1
	return count

print "amount = ", a, "  ways of change = ", iter_change(a), "  calls = ", calls
#number of calls ~ amount^(n-1), where n=len(m)
```

Output
```
:::text
amount =  100   ways of change =  292   calls =  292
```

We see that this algorithm is optimal in the sense it visits every way
to change amount only once and it doesn't waste time trying wrong ways.
But all four loops are hardcoded. The last, fifth, loop is replaced
by slightly more complex condition check.

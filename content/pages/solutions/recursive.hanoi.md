title: Recursive Tower of Hanoi
slug: sicp-recursive-hanoi

The code is taken from the video lectures

Code
```
:::scheme
#lang racket

(define (print-move from to)
  (display from)
  (display " -> ")
  (display to)
  (newline)
)
  
(define (hanoi n from spare to)
  (cond ((= n 0) "done")
        (else
         (hanoi (- n 1) from to spare)
         (print-move from to)
         (hanoi (- n 1) spare from to))))

; move four disks from first to third rod using second rod as spare
(hanoi 4 1 2 3)

     
```

Output
```
:::text
1 -> 2
1 -> 3
2 -> 3
1 -> 2
3 -> 1
3 -> 2
1 -> 2
1 -> 3
2 -> 3
2 -> 1
3 -> 1
2 -> 3
1 -> 2
1 -> 3
2 -> 3
"done"
```

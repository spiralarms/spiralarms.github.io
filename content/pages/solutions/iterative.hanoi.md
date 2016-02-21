title: Iterative Tower of Hanoi
slug: sicp-iterative-hanoi

As Dr. Sussman promised, it was fun!

Code
```
:::scheme
#lang racket

; Iterative tower of Hanoi algorithm

(define (print-move n from to)
  (display from)
  (display " -> ")
  (display to)
  ;(display "  ")
  ;(display n)
  (newline)
)

(define (iter-hanoi height from to)
  (define (iter nold n f t)
    (cond
      ((= n 0) "done")
      (else
       (define leaf? (>= n (expt 2 (- height 1)))) 
       (define s (- 6 f t)) ; spare rod
       (cond (leaf? (print-move n f t)))
       (cond
         ((and (not leaf?) (> n nold)) (iter n (* n 2) f s))
         ((and (< n nold) (even? nold)) (print-move n f t) (iter n (+ 1 (* n 2)) s t))
         (else
          (if
           (even? n)
           (iter n (quotient n 2) f s)
           (iter n (quotient n 2) s t)))))))
  (iter 0 1 from to))

; rods: 1, 2, 3
; move four disks from the first to the third rod
(iter-hanoi 4 1 3)
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

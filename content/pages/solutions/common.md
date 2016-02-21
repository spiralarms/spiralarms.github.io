title: Common procedures
slug: sicp-common

Code
```
:::scheme
#lang racket

;; ch1

(define (inc n) (+ n 1))
(provide inc)

(define (dec n) (- n 1))
(provide dec)

(define (square x) (* x x))
(provide square)

(define (cube x) (* x x x))
(provide cube)

(define (divides? a b) (= (remainder b a) 0))
(provide divides?)

;(define (compose f g) (lambda (x) (f (g x))))
;(provide compose)

(define (average x y) (/ (+ x y) 2))
(provide average)

(define (average-damp f) (lambda (x) (average x (f x))))
(provide average-damp)

(define runtime current-seconds)
(provide runtime)

(define (pass) (display ""))
(provide pass)

(define (expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp)
         (remainder (square (expmod base (/ exp 2) m))
                    m))
        (else
         (remainder (* base (expmod base (- exp 1) m))
                    m))))
(provide expmod)

(define (fast-expt b n)
  (cond ((= n 0) 1)
        ((even? n) (square (fast-expt b (/ n 2))))
        (else (* b (fast-expt b (- n 1))))))
(provide fast-expt)

;; ch2

(define nil '() )
(provide nil)

(define (enumerate-tree tree)
  (cond ((null? tree) '())
        ((not (pair? tree)) (list tree))
        (else (append (enumerate-tree (car tree))
                      (enumerate-tree (cdr tree))))))
(provide enumerate-tree)


(define (enumerate-interval low high)
  (if (> low high)
      '()
      (cons low (enumerate-interval (+ low 1) high))))
(provide enumerate-interval)


(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))
(provide accumulate)


(define (accumulate-n op initial sequences)
  (if (null? (car sequences))
      '()
      (cons (accumulate op initial (map car sequences))
            (accumulate-n op initial (map cdr sequences)))))
(provide accumulate-n)

; 0+(1+(2+3))
(define fold-right accumulate)
(provide fold-right)

; ((0+1)+2)+3
(define (fold-left op initial sequence)
  (define (iter result rest)
    (if (null? rest)
      result
      (iter (op result (car rest)) (cdr rest))))
  (iter initial sequence))
(provide fold-left)

(define (flatmap proc seq)
  (accumulate append '() (map proc seq)))
(provide flatmap)
```

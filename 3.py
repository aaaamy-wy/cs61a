(define (fact n) 
    (if (<= n 1)
        1
        (* n (fact (- n 1)))))

(define (count-up n)
    (define (helper k)
        (print k)
        (if (< k n)) (helper (+ k 1)))
        (helper 1)) 

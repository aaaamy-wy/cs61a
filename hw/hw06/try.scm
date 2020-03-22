(define (length lst)
    (define (helper result new-lst)
        (if (null? new-lst) result
            (helper (+ result 1) (cdr new-lst)))
        )
    (helper 0 lst))

(define )
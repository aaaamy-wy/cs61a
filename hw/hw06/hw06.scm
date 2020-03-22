;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (unique s)
 (define (helper check lst)
     (filter (lambda (x) (not (equal? check x))) lst))
    (cond 
          ((null? s) s)
          (else (cons (car s) (unique (helper (car s) (cdr s)))))))
          
 
 

(define (cons-all first rests)
 (map (lambda (x) (cons first x)) rests)
 )


;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
    (cond
        ((null? denoms) nil)
        ((= 0 total) '(()))
        ((> (car denoms) total) (list-change total (cdr denoms)))
        (else (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms)))
        )        
        )
)
; Tail recursion

(define (replicate x n)
  (define (helper result count)
    (if (= 0 count) result
        (helper (append (list x) result) (- count 1))))
  (helper '() n)
  )

(define (accumulate combiner start n term)
 (if (= n 0) start
     (combiner (term n) (accumulate combiner start (- n 1) term)))   
)

(define (accumulate-tail combiner start n term)
 (define (helper result count)
     (if (= count 0) result
         (accumulate-tail combiner (combiner (term n) start) (- n 1) term)))
  (helper start n)   
 )


; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
  
)

  
  
  
(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

"""(define (naturals start)
		(cons-stream start (naturals (+ 1 start))))
(define multiples-of-three
	(map-stream (lambda (x) (* x 3)) (naturals 1))

)"""
(define multiples-of-three
  (cons-stream 3 (map-stream (lambda (x) (+ x 3)) multiples-of-three)))

(define (rle s)
  (define (helper count lst result)
  	(cond 
  		((null? lst) result)
  		((null? (cdr-stream lst)) (cons-stream (list (car lst) count) nil))
  		((= (car lst) (car (cdr-stream lst))) 
  			(helper (+ count 1) (cdr-stream lst) result))
  		(else (cons-stream (list (car lst) count) (helper 1 (cdr-stream lst) result)))
  		))
  (helper 1 s '())
)

"""(define (rle s)
  (define (rle_helper s count num)
    (cond 
      ((null? s)(cons-stream (list num count) nil))
      ((= (car s) num)
            (rle_helper (cdr-stream s) (+ count 1) num))
      (else (cons-stream (list num count)
                         (rle_helper (cdr-stream s) 1 (car s))))))
  (if (null? s) '()
   (rle_helper (cdr-stream s) 1 (car s))))"""


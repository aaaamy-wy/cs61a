(define (add-to-end lst x)
	(cond
		((null? lst) (list x))
		(else (cons (car lst) (add-to-end (cdr lst) x)))
		)
	)
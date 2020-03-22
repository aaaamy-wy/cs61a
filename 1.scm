(define-macro (add-or-sub cond1 x1 x2)
	`(if ,cond1 (+ x1 x2) (- x1 x2))
	)

(deine-macro (add-sub cond1 x1 x2)
	（list  
	)
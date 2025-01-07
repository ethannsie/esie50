; Tanzeem Hasan, Ethan Sie, Brian Liu
; Chewy_Chupucabras
; SoftDev
; K27: JS is just Scheme with Java syntax
; 2025-01-06
; time spent: 10 mins
  
(define (fib n)
  (if (<= n 1)
      n
      (+ (fib (- n 1)) (fib (- n 2)))))

(define (fac n)
  (if (= n 0)
      1
      (* n (fac (- n 1)))))

  # Tanzeem Hasan, Ethan Sie, Brian Liu
  # Chewy_Chupucabras
  # SoftDev
  # K27: JS is just Scheme with Java syntax
  # 2025-01-06
  # time spent: 10 mins

function fac(n) {
  if (n === 0) {
    return 1;
  }
  return n * fac(n - 1);
}

function fib(n) {
  if (n <= 1) {
    return n;
  }
  return fib(n - 1) + fib(n - 2);
}

function p = puntofijo(p0, tol, n, g)
  i = 1
  while i <= n
    p = g(p0)
    if abs(p - p0) < tol
      break;
    end
    i = i + 1;
    p0 = p;
  end
end

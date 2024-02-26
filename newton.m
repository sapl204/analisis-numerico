function p = newton(p0, tol, n, f)
  i = 1;
  pkg load symbolic;
  syms x;
  while i <= n
    df = function_handle(diff(f,x));
    p = p0 - f(p0)/df(p0);
    if abs(p - p0) < tol
      break;
    end
    i = i + 1;
    p0 = p
  end
end

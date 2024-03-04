function pol = polinomio(f, p0, points)
  pol = 0;
  pkg load symbolic;
  syms x;
  for k = 1:length(points)
    prod = 1;
    for i = 1:length(points)
      if i == k
        continue
      else
        prod = prod*(x - points(i))/(points(k) - points(i));
      end
    end
    pol = pol + f(points(k))*prod;
  end
  fprintf("polinomio evaluado: ")
  disp(function_handle(pol)(p0))
  fprintf("polinomio simplificado: \n")
  disp(simplify(pol))
  fplot(function_handle(pol))
end

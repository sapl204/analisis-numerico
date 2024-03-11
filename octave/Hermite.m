function pol = Hermite(xpoints, ypoints, ypPoints, p0)
  pol = 0;
  pkg load symbolic;
  syms x;
  for j = 1:length(xpoints)
    prod = 1;
    for k = 1:length(xpoints)
      if j == k
        continue
      else
        prod = prod*(x-xpoints(k))/(xpoints(j)-xpoints(k));
      end
    end
    dvProdInXj = function_handle(diff(prod, x))(xpoints(j));
    pol = pol + ypoints(j)*(1-2*(x - xpoints(j))*dvProdInXj)*prod^2 + ypPoints(j)*(x - xpoints(j))*prod^2;
  end
  fprintf("polinomio evaluado: ")
  disp(function_handle(pol)(p0))
  fprintf("polinomio simplificado: \n")
  disp(simplify(pol))
  fplot(function_handle(pol))
end
  
  

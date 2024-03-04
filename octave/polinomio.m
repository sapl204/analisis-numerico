function pol = polinomio(f, p0, points)
  pol = 0;
  for k = 1:length(points)
    prod = 1;
    for i = 1:length(points)
      if i == k
        continue
      else
        prod = prod*(p0 - points(i))/(points(k) - points(i));
      end
    end
    pol = pol + f(points(k))*prod;
  end
end

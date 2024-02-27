function p = puntofijo(g,p0,N, tol)
  i = 1;
  fprintf("Metodo de punto fijo\n")
  fprintf("    i    p    error\n")
  while i <= N
    p = g(p0);
    fprintf("   %4.0f   %4.5f    %4.6f\n",i,p,abs(p-p0))
    if abs(p-p0)<tol
      fprintf("se terminaron las iteraciones")
      break
    end
    i = i + 1;
    p0 = p;
  end
end

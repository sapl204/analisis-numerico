
function p = biseccion(a,b,tol,n,f)
  format long
  fa = f(a);
  i = 1;
  while i <= n
     p = (a+b)/2;
    fp = f(p);
    if fp == 0 | (b-a)/2 < tol
      break;
    end
    i = i + 1;
     if fp*fa > 0
      a = p;
      fa = fp;
    else
      b = p;
    end
  end
end

function s=trap_comp(f,a,b,M)
h=(b-a)/M;
s=0;
for k=1:(M-1)
x=a+h*k;
s=s+feval(f,x);
end
s=h*(feval(f,a)+feval(f,b))/2 + h*s;
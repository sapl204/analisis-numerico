function s=simp_comp(f,a,b,M)
h=(b-a)/M;
s=0;
for k=1:M
xi=a+h*(k-1);
xi1= xi + h;
s=s+feval(f,xi)+4*feval(f,(xi+xi1)/2)+feval(f,xi1);
end
s=h*s/6 ;
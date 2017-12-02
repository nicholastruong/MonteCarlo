%Monte Carlo 
n = 10^6; 
sum = 0; 
s2 = 0; 
X = zeros(1, n); 
AX = zeros(1, n); 
xvals = zeros(1, n); 
yvals = zeros(1, n); 
for i = 1 : n 
   x = rand; 
   xvals(1, i) = x; 
   y = rand; 
   yvals(1, i) = y; 
   fX = exp((x + y)^2); 
   X(1, i) = fX; 
  
end
clear sum;  
S = sum(X); 

I = S / n; 
I 
%Monte Carlo Variance 
V = zeros(1, n); 
for i = 1 : n
   V(1, i) =( X(1, i) - I)^2; 
end
Var = sum(V)/ (n - 1); 
Var
% antithetic 
axvals = zeros(1, n); 
ayvals = zeros(1, n); 
T = zeros(1, n); 
for i = 1 : n/2
    axvals(1, i) = 1 - xvals(1, i); 
    ayvals(1, i) = 1 - yvals(1, i); 
    fAX = exp((axvals(1, i) + yvals(1, i))^2); 
    AX(1, i) = fAX; 
    T(1, i) = (AX(1, i) + X(1, i)) ; 
    
end
Tot = sum(T);  
J = Tot / n;
J
% antithetic variance 
AV = zeros(1, n); 
for i = 1 : n/2
    AV(1, i) = (T(1, i) - J)^2; 
end

AVar = sum(AV) / (n -1); 
AVar


%ci
de = zeros(1, n); 
for i = 1 : n
    de(1, i) =  X(1, i) - (xvals(1, i) + yvals(1, i)); 
end

difest = (sum(de) / n) + 1; 
difest
%C Variance
DEV= zeros(1, n); 
for i = 1 : n
    DEV(1, i) = (de(1, i) - difest)^2;
end 
DVar = sum(DEV) / (n - 1); 
DVar
    
    
    
%cii
dei = zeros(1, n); 
for i = 1 : n
    dei(1, i) = X(1, i) - ((xvals(1, i) + yvals(1, i))^2); 
end

difesti = (sum(dei) / n) + (7/6); 
difesti


%Cii Variance
DEVi= zeros(1, n); 
for i = 1 : n
    DEVi(1, i) = (dei(1, i) - difesti)^2;
end 
DVari = sum(DEVi) / (n - 1); 
DVari








% l  = 10^6; 
%    %Part C
% utotal = 0; 
% vtotal = 0; 
% y = 0; 
% ys = 0; 
%   for i = 1 : l
%       u = rand; 
%       v = rand; 
%       utotal = utotal + u; 
%       vtotal = vtotal + v; 
%       s = (u + v)^2; 
%       y = y + u + v; 
%       ys = ys +  s; 
%   end
%   evaly = y / l; 
%   evalys = ys / l; 
%   evaly
%   evalys





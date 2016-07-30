function [w]=grdescent(func,w0,stepsize,maxiter,tolerance)
% function [w]=grdescent(func,w0,stepsize,maxiter,tolerance)
%
% INPUT:
% func function to minimize
% w0 = initial weight vector 
% stepsize = initial gradient descent stepsize 
% tolerance = if norm(gradient)<tolerance, it quits
%
% OUTPUTS:
% 
% w = final weight vector
%

if nargin<5,tolerance=1e-02;end;
i=0;
w=w0;temploss=inf;
while i<maxiter
[loss,gradient]=func(w);
w=w-stepsize*gradient;
if norm(gradient)<tolerance
    break
end
if loss<=temploss
    stepsize=stepsize*1.01;
    temploss=loss;
else
    stepsize=stepsize*0.5;
end
i=i+1;
end




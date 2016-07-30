function BDT=boosttree(x,y,nt,maxdepth)
% function BDT=boosttree(x,y,nt,maxdepth)
%
% Learns a boosted decision tree on data x with labels y.
% It performs at most nt boosting iterations. Each decision tree has maximum depth "maxdepth".
%
% INPUT:
% x  | input vectors dxn
% y  | input labels 1xn
% nt | number of trees (default = 100)
% maxdepth | depth of each tree (default = 3)
%
% OUTPUT:
% BDT | Boosted DTree
%

y=y-1;
y(y==0)=-1;
if nargin<4,
    maxdepth=3;
end;
if nargin<3,
    nt=100;
end;
[~,n]=size(x);
weights=ones(1,n)./n;
alphas=[];F=cell(2,0);

for i=1:nt
    T=id3tree(x,y,maxdepth,weights);
    hx=evaltree(T,x);
    err=sum(weights(hx~=y));
    if err>0.5
        break
    end
    alpha=0.5*log((1-err)/err);
    alphas=[alphas,alpha];
    weights=weights.*exp(-alpha*(hx.*y))/(2*sqrt((1-err)*err));
    F=[F,{T;alpha}];
end
BDT=F;



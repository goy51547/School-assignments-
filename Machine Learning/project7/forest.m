function F=forest(x,y,nt)
% function F=forest(x,y,nt)
%
% INPUT:
% x | input vectors dxn
% y | input labels 1xn
%
% OUTPUT:
% F | Forest
%
[d,n]=size(x);
F=cell(0);
for i=1:nt
    ind=randsample(1:n,n,true);
    tx=x(:,ind);
    ty=y(ind);
    T=id3tree(tx,ty);
    F=[F,{T}];
end


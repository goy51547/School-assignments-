function D=l2distance(X,Z)
% function D=l2distance(X,Z)
%	
% Computes the Euclidean distance matrix. 
% Syntax:
% D=l2distance(X,Z)
% Input:
% X: dxn data matrix with n vectors (columns) of dimensionality d
% Z: dxm data matrix with m vectors (columns) of dimensionality d
%
% Output:
% Matrix D of size nxm 
% D(i,j) is the Euclidean distance of X(:,i) and Z(:,j)
%
% call with only one input:
% l2distance(X)=l2distance(X,X)
%

if (nargin==1) % case when there is only one input (X)
	D=l2distance(X,X);

else  % case when there are two inputs (X,Z)
    [~,n]=size(X); % dimension of X
    [~,m]=size(Z); % number of input vectors in Z
	S=innerproduct(X);
    R=innerproduct(Z);
    G=innerproduct(X,Z);
    s=diag(S);
    g=diag(R);g=transpose(g);
    s=repmat(s,1,m);
    g=repmat(g,n,1);
    D2=s+g-2*G;
    D=sqrt(D2);
end;
%




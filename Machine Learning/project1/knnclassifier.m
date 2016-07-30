function preds=knnclassifier(xTr,yTr,xTe,k);
% function preds=knnclassifier(xTr,yTr,xTe,k);
%
% k-nn classifier 
%
% Input:
% xTr = dxn input matrix with n column-vectors of dimensionality d
% xTe = dxm input matrix with n column-vectors of dimensionality d
% k = number of nearest neighbors to be found
%
% Output:
%
% preds = predicted labels, ie preds(i) is the predicted label of xTe(:,i)
%



[indices,~]=findknn(xTr,xTe,k);
X=indices;
X(:)=yTr(1,indices);
[preds,~,C]=mode(X,1);
csize=cellfun('size',C,1);
fix=find(csize~=1);
for i=1:size(fix,2)
    s=inf;
    for j=1:size(C{fix(1,i)},1)
        value=C{fix(1,i)}(j,1);
        su=sum(find(X(:,fix(1,i))==value));
        if su<s
            s=su;
            preds(fix(1,i))=value;
        end
    end
end


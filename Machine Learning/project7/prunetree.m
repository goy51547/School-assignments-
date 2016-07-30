function T=prunetree(T,xTe,y)
% function T=prunetree(T,xTe,y)
%
% Prunes a tree to minimal size such that performance on data xTe,y does not
% suffer.
%
% Input:
% T = tree
% xTe = validation data x (dxn matrix)
% y = labels (1xn matrix)
%
% Output:
% T = pruned tree
%
trys=find(T(4,:)==0 & T(5,:)==0 );
tempT=T;tried=[];
while ~isempty(trys)
    trys=find(T(4,:)==0 & T(5,:)==0);
    papas=T(6,trys);
    temp=[];
    for i=1:size(trys,2)
        if ~any(papas(i)==tried)
            temp=[temp,trys(i)];
        end
    end
    trys=temp;
    if isempty(trys)
        break
    end
    err=sum(abs(evaltree(T, xTe) - y));
    index=find(T(4,:)==0 & T(5,:)==0 & T(6,:)==T(6,trys(size(trys,2))));
    if size(index,2)~=2
        break
    end
    leaves=T(:,index);
    if leaves(6,1)~=leaves(6,2)
        break
    end
    tempT(4,leaves(6,1))=0;tempT(5,leaves(6,1))=0;
    temperr=sum(abs(evaltree(tempT, xTe) - y));
    if temperr<=err
        T=tempT;
        tried=[tried,leaves(6,1)];
    else tempT=T;
        tried=[tried,leaves(6,1)];
    end
end



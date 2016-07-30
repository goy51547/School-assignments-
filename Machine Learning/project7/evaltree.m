function [ypredict]=evaltree(T,xTe)
% function [ypredict]=evaltree(T,xTe);
%
% input:
% T0  | tree structure
% xTe | Test data (dxn matrix)
%
% output:
%
% ypredict : predictions of labels for xTe
%

[d,n]=size(xTe);
ypredict=zeros(1,n);
for i=1:n
    current=1;
    while 1
        if T(4,current)==0 && T(5,current)==0
            ypredict(i)=T(1,current);
            break
        else
            feature =  T(2,current);
            cut =  T(3,current);
            if xTe(feature,i)<=cut
                current=T(4,current);
            else current=T(5,current);
            end
        end
    end
end


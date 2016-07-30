function w=perceptron(x,y);
% function w=perceptron(x,y);
%
% Implementation of a Perceptron classifier
% Input:
% x : n input vectors of d dimensions (dxn)
% y : n labels (-1 or +1)
%
% Output:
% w : weight vector
%

[d,n]=size(x);
w=zeros(d,1);
i=0;
while i<100
    count=0;
    index=randperm(n);
    for j=1:n
        ind=index(1,j);
        temp=w;
        w=perceptronUpdate(x(:,ind),y(1,ind),w);
        if w~=temp
            count=count+1;
        end
    end
    if count==0
        break
    end
    i=i+1;
end



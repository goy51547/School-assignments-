function bias=recoverBias(K,yTr,alphas,C);
% function bias=recoverBias(K,yTr,alphas,C);
%
% INPUT:	
% K : nxn kernel matrix
% yTr : 1xn input labels
% alphas  : nx1 vector or alpha values
% C : regularization constant
% 
% Output:
% bias : the hyperplane bias of the kernel SVM specified by alphas
%
% Solves for the hyperplane bias term, which is uniquely specified by the support vectors with alpha values
% 0<alpha<C
%

temp=[alphas,[1:size(alphas,1)]'];
temp(:,1)=temp(:,1).^2+(C-temp(:,1)).^2;
temp=sortrows(temp,1);
bias=1/yTr(temp(1,2))-(yTr.*alphas).'*K(:,temp(1,2));

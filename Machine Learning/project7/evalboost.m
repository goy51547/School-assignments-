function preds=evalboost(BDT,xTe)
% function preds=evalboost(BDT,xTe);
%
% Evaluates a boosted decision tree on a test set xTe.
%
% input:
% BDT | Boosted Decision Trees
% xTe | matrix of m input vectors (matrix size dxm)
%
% output:
%
% preds | predictions of labels for xTe
%
preds=[];
for i=1:size(BDT,2)
    preds=[preds;evaltree(BDT{1,i},xTe).*BDT{2,i}];
end 
preds=sign(sum(preds,1));
preds=preds+1;
preds(preds==0)=1;


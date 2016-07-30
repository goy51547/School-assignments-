function preds=evalforest(F,xTe)
% function preds=evalforest(F,xTe);
%
% Evaluates a random forest on a test set xTe.
%
% input:
% F   | Forest of decision trees
% xTe | matrix of m input vectors (matrix size dxm)
%
% output:
%
% preds | predictions of labels for xTe
%

nt=length(F);
preds=[];
for i=1:nt
    pred=evaltree(F{1},xTe);
    preds=[preds;pred];
end
preds=mode(preds,1);


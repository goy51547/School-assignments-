function output=analyze(kind,truth,preds)	
% function output=analyze(kind,truth,preds)		
%
% Analyses the accuracy of a prediction
% Input:
% kind='acc' classification error
% kind='abs' absolute loss
% (other values of 'kind' will follow later)
% 
[m,n]=size(preds);
switch kind
	case 'abs'
		% compute the absolute difference between truth and predictions
        output=sum(abs(truth-preds))/(m*n);
		
	case 'acc' 
        diff=truth-preds;
        count=sum(diff(:)==0);
        output=count/(m*n);
		 	
end;


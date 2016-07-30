function [bestC,bestP,bestval,allvalerrs]=crossvalidate(xTr,yTr,ktype,Cs,paras)
% function [bestC,bestP,bestval,allvalerrs]=crossvalidate(xTr,yTr,ktype,Cs,paras)
%
% INPUT:	
% xTr : dxn input vectors
% yTr : 1xn input labels
% ktype : (linear, rbf, polynomial)
% Cs   : interval of regularization constant that should be tried out
% paras: interval of kernel parameters that should be tried out
% 
% Output:
% bestC: best performing constant C
% bestP: best performing kernel parameter
% bestval: best performing validation error
% allvalerrs: a matrix where allvalerrs(i,j) is the validation error with parameters Cs(i) and paras(j)
%
% Trains an SVM classifier for all possible parameter settings in Cs and paras and identifies the best setting on a
% validation split. 
%

%%% Feel free to delete this
bestC=0;
bestP=0;
bestval=10^10;
allvalerrs=zeros(length(Cs),length(paras));

%% Split off validation data set
[~,n]=size(xTr);
x1=xTr(:,1:round(n/5));
y1=yTr(1,1:round(n/5));
i=round(n/5);
x2=xTr(:,i+1:i+round(n/5));
y2=yTr(1,i+1:i+round(n/5));
i=i+round(n/5);
x3=xTr(:,i+1:i+round(n/5));
y3=yTr(1,i+1:i+round(n/5));
i=i+round(n/5);
x4=xTr(:,i+1:i+round(n/5));
y4=yTr(1,i+1:i+round(n/5));
i=i+round(n/5);
x5=xTr(:,i+1:n);
y5=yTr(1,i+1:n);


%% Evaluate all parameter settings
for i=1:length(Cs)
    C=Cs(i);
    for j=1:length(paras)
        kpar=paras(j);
        [svmclassify,~,~]=trainsvm([x1,x2,x3,x4],[y1,y2,y3,y4], C,ktype,kpar);
        valerr=sum(sign(svmclassify(x5))~=y5(:))/length(y5);
        [svmclassify,sv_i,alphas]=trainsvm([x1,x2,x3,x5],[y1,y2,y3,y5], C,ktype,kpar);
        valerr=valerr+sum(sign(svmclassify(x4))~=y4(:))/length(y4);
        [svmclassify,sv_i,alphas]=trainsvm([x1,x5,x3,x4],[y1,y5,y3,y4], C,ktype,kpar);
        valerr=valerr+sum(sign(svmclassify(x2))~=y2(:))/length(y2);
        [svmclassify,sv_i,alphas]=trainsvm([x1,x2,x5,x4],[y1,y2,y5,y4], C,ktype,kpar);
        valerr=valerr+sum(sign(svmclassify(x3))~=y3(:))/length(y3);
        [svmclassify,sv_i,alphas]=trainsvm([x5,x2,x3,x4],[y5,y2,y3,y4], C,ktype,kpar);
        valerr=valerr+sum(sign(svmclassify(x1))~=y1(:))/length(y1);
        if valerr<bestval
            bestval=valerr;
            bestC=C;
            bestP=kpar;
        end
        allvalerrs(i,j)=valerr/5;
    end
end

%% Identify best setting
% YOUR CODE



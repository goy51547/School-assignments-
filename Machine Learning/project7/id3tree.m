function T=id3tree(xTr,yTr,maxdepth,weights)
% function T=id3tree(xTr,yTr,maxdepth,weights)
%
% The maximum tree depth is defined by "maxdepth" (maxdepth=2 means one split).
% Each example can be weighted with "weights".
%
% Builds an id3 tree
%
% Input:
% xTr | dxn input matrix with n column-vectors of dimensionality d
% yTr | 1xn input matrix
% maxdepth = maximum tree depth
% weights = 1xn vector where weights(i) is the weight of example i
%
% Output:
% T = decision tree
%
[~,n]=size(xTr);
if nargin<4,
    weights=ones(1,n)./n;
end;

if nargin<3,
    maxdepth=inf;
end;
if ~maxdepth==inf
T=zeros(6,2^maxdepth-1);
else T=zeros(6,5000);
end
y1=min(yTr);
for i=1:n
    if yTr(i)~=y1
        y2=yTr(i);
    end
end
if y1+y2~=0
    yTr=yTr-1;
    yTr(yTr==0)=-1;
end
store=cell(4,1);
store{1,1}=xTr;store{2,1}=yTr;
wet=abs(weights.*yTr);
if sum(wet(yTr==1))>sum(wet(yTr==-1))
    label=y2;
else label=y1;
end
store{3,1}=[label,0,0,2,3,0,1,1]';
store{4,1}=weights;
del=0;
while ~isempty(store)
    tx=store{1,1};ty=store{2,1};papa=store{3,1};weights=store{4,1};
    store=store(:,2:size(store,2)); 
    del=del+1;
    [feature,cut,~]=entropysplit(tx,ty,weights);
    papa(2)=feature;papa(3)=cut;
    if papa(7)==maxdepth
        papa(4)=0;papa(5)=0;
        T(:,papa(8))=papa(1:6,1);
        continue
    else if all(ty == ty(1))
            papa(4)=0;papa(5)=0;
            T(:,papa(8))=papa(1:6,1);
            continue
        else
            T(:,papa(8))=papa(1:6,1);
            txl=[];txr=[];tyl=[];tyr=[];wl=[];wr=[];
            for i=1:length(ty) 
                if tx(feature,i)<=cut
                    txl=[txl,tx(:,i)];
                    tyl=[tyl,ty(:,i)];
                    wl=[wl,weights(:,i)];
                else 
                    txr=[txr,tx(:,i)];
                    tyr=[tyr,ty(:,i)];
                    wr=[wr,weights(:,i)];
                end         
            end
            store=[store,cell(4,2)];
            store{1,size(store,2)-1}=txl;store{2,size(store,2)-1}=tyl;
            wet=abs(wl.*tyl);
            if sum(wet(tyl==1))>sum(wet(tyl==-1))
                label=y2;
            else label=y1;
            end
            store{3,size(store,2)-1}=[label,0,0,papa(4)*2,papa(4)*2+1,papa(8),papa(7)+1,papa(4)]';
            store{4,size(store,2)-1}=wl;
            wet=abs(wr.*tyr);
            if sum(wet(tyr==1))>sum(wet(tyr==-1))
                label=y2;
            else label=y1;
            end
            store{1,size(store,2)}=txr;store{2,size(store,2)}=tyr;
            store{3,size(store,2)}=[label,0,0,papa(5)*2,papa(5)*2+1,papa(8),papa(7)+1,papa(5)]';
            store{4,size(store,2)}=wr;
        end
    end
end
T=[T;[1:5000]];
T( :, ~any(T(1:6,:),1) ) = [];
for i=1:size(T,2)
    if T(4,i)~=0
        T(4,i)=find(T(7,:)== T(4,i));
        T(5,i)=find(T(7,:)== T(5,i));
    end
end
i=size(T,2);
while i>1
    T(6,i)=find(T(7,:)== T(6,i));
    i=i-1;
end
T=T(1:6,:);




function xordemo(TRANSNAME,HIDDENNODES)
% function xordemo(TRANSNAME,HIDDENNODES)
% 
% TRANSNAME: Transition function
% Possible values are 'ReLU','tanh','sigmoid','ReLU2'
%
% HIDDENNODES:
% possible format [20], [20 30] 
% -- be careful this is read backwards, so [25 30] means
% the 1. layer has 25 nodes
% the 2. layer has 30 nodes
%

if nargin<2,
	HIDDENNODES=20;
end;
if nargin<1,
	TRANSNAME='ReLU';
end;

%% setting global parameters
STEPSIZE=10;
figure(3);
clf;
subplot(1,2,1);
wst=[1 HIDDENNODES 2];
rounds=20;
w=initweights(wst);
ITER=50;


%% generate data
[x,y]=genxor();	
[xx,yy]=meshgrid(-1:0.1:1,-1:0.1:1);  
subplot(1,2,2);
hs=surf(xx,yy,zeros(size(xx)));
axis equal;
title(['Network Layers: ' num2str(wst)]);

%% initialize plots
subplot(1,2,1);
h=scatter(x(1,:),x(2,:));
axis equal;
set(h,'MarkerEdgecolor',[0.5 0.5 0.5])
box on;
colorbar;
drawnow;

%% do optimization
f=@(w) deepnet(w,x,y,wst);
for i=1:rounds
  [w,l]=minimize(w,'deepnet',ITER,x,y,wst,TRANSNAME);
 pred=deepnet(w,x,[],wst,TRANSNAME);
% set(h,'CData',pred)
 drawnow;
 ps=reshape(deepnet(w,[xx(:) yy(:)]',[],wst,TRANSNAME),length(xx),length(xx));
 set(hs,'ZData',ps);
 drawnow;
end;
	
	


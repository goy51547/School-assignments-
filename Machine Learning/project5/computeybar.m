function ybar=computeybar(xTe)
% function [ybar]=ybar(xTe);
% 
% computes the expected label 'ybar' for a set of inputs x
% generated from two standard Normal distributions (one offset by OFFSET in
% both dimensions.)
%
% INPUT:
% xTe | a 2xn matrix of column input vectors
% 
% OUTPUT:
% ybar | a 1xn vector of the expected label ybare(x)
%

global OFFSET;

[~,n]=size(xTe);


% Feel free to use the following function to compute p(x|y)
normpdf=@(x,mu,sigma)   exp(-0.5 * ((x - mu)./sigma).^2) / (sqrt(2*pi) * sigma);
y1=normpdf(xTe,0,1);
y1=y1(1,:).*y1(2,:);
y2=normpdf(xTe,OFFSET,1);
y2=y2(1,:).*y2(2,:);
px=y2+y1;
py1=y1./px;
py2=y2./px;
ybar=py1+py2*2;



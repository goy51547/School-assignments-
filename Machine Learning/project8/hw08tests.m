function [r,ok,s]=hw08tests()
% function [r,s]=hw08tests()
%
% Tests the functions from homework assignment 8
% Please make sure that the error statements are instructive. 
%
% Output: 
% r=0 number of tests that broke
% ok=0 number of tests that passed
% s= statement describing the failed test (s={} if all succeed)
%

% Put in any seed below
rand('seed',31415926535);
% initial outputs
r=0;
ok=0;
s={};
load boston;
wst=[1 12 size(xTr,1)];
w=initweights(wst);

try
    [xTr,~,u,m]=preprocess(xTr,xTe);
    n = size(xTe, 2);
    apply_um = u * (xTe - repmat(m, 1, n));
    failtest = norm(xTep - apply_um) > 1e-5;
catch
    failtest = true;
    addon=lasterr();
end
if failtest,
    r=r+1;
    s{length(s)+1}=['incorrect preprocessing'; addon];
else
    ok=ok+1;
end;

try
    graderr=checkgrad('deepnet',w,1e-05,xTr,yTr,wst);
    failtest= graderr> 1e-2;
    addon='';
catch
    failtest = true;
    addon=lasterr();
end
if failtest,
    r=r+1;
    s{length(s)+1}=['deepnet.m does not pass checkgrad.'; addon];
else
    ok=ok+1;
end;

% test forward pass
xTr = magic(10);
yTr = [0,0,1,0,1,1,0,0,1,1];
[trans_func, trans_func_der] = get_transition_func('ReLU');
try
    [xTr,~,~,~]=preprocess(xTr,xTr);
    [as,zs] = forward_pass(W_test, xTr, trans_func);
    addon='';
    failtest_as = false;
    for i=1:size(as, 2)
        failtest_as = (failtest_as || (norm(as{i} - as_sol{i}) / numel(as{i})) > 1e-1);
    end
    failtest_zs = false;
    for i=1:size(zs, 2)
        failtest_zs = (failtest_zs || ((norm(zs{i} - zs_sol{i}) / numel(zs{i}))) > 1e-1);
    end
catch
    failtest_as = true;
    failtest_zs = true;
    addon=lasterr();
end
if failtest_as,
    r=r+1;
    s{length(s)+1}=['Incorrect forward pass as computed'; addon];
else
    ok=ok+1;
end;
if failtest_zs,
    r=r+1;
    s{length(s)+1}=['Incorrect forward pass zs computed'; addon];
else
    ok=ok+1;
end;

% test compute gradient
try
    gradientCell = backprop(W_test, as,zs, yTr, trans_func_der);
    failtest = false;
    addon='';
    failtest = false;
    for i=1:size(gradientCell, 2)
        failtest = (failtest || ((norm(gradientCell{i} - gradientCell_sol{i}) / numel(gradientCell{i}))) > 1e-1);
    end
catch
    failtest = true;
    addon=lasterr();
end
if failtest,
    r=r+1;
    s{length(s)+1}=['Incorrect gradient computed'; addon];
else
    ok=ok+1;
end;

% test compute loss
yTr = [0,0,1,1,0];
zs{1} = [.2, .2, 1.2, 1.2, .2];
try
    loss = compute_loss(zs, yTr);
    failtest = (loss - 0.02) > 1e-2;
    addon='';
catch
    failtest = true;
    addon=lasterr();
end
if failtest,
    r=r+1;
    s{length(s)+1}=['Incorrect loss computed'; addon];
else
    ok=ok+1;
end;

end


function featureVector = singleImageFeatureExtractor(img_idx)
%SINGLEIMAGEFEATUREEXTRACTOR 此处显示有关此函数的摘要
%   此处显示详细说明
%读入tif数据
img = imread(['../original-image/' num2str(img_idx) '.tif']);
%直接利用matlab自带的HoG feature提取函数提取HoG特征
%这个函数的参数我没细看，可以在matlab的命令行敲入
%help extractHOGFeatures
%查看函数的使用方法
[featureVector,~] = extractHOGFeatures(img,'CellSize',[1,1]);

%% Visualization

% [featureVector,hogVisualization] = extractHOGFeatures(img);
% figure;
% imshow(img);
% hold on;
% plot(hogVisualization);

end


function featureVector = singleImageFeatureExtractor(img_idx)
%SINGLEIMAGEFEATUREEXTRACTOR �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
%����tif����
img = imread(['../original-image/' num2str(img_idx) '.tif']);
%ֱ������matlab�Դ���HoG feature��ȡ������ȡHoG����
%��������Ĳ�����ûϸ����������matlab������������
%help extractHOGFeatures
%�鿴������ʹ�÷���
[featureVector,~] = extractHOGFeatures(img,'CellSize',[1,1]);

%% Visualization

% [featureVector,hogVisualization] = extractHOGFeatures(img);
% figure;
% imshow(img);
% hold on;
% plot(hogVisualization);

end


%清除workspace现有的内容，可不管
clc;
clear;

%设置一些基本的参数
num_of_image=20000;%图片的数量
d=576;%特征数目
data=zeros(num_of_image,d);%最终提取出的特征矩阵应为2000*576，初始化为全0的矩阵

for i=1:num_of_image
    %提取第i张图片的feature
    data(i,:)=singleImageFeatureExtractor(i);
end
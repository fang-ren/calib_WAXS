%���workspace���е����ݣ��ɲ���
clc;
clear;

%����һЩ�����Ĳ���
num_of_image=20000;%ͼƬ������
d=576;%������Ŀ
data=zeros(num_of_image,d);%������ȡ������������ӦΪ2000*576����ʼ��Ϊȫ0�ľ���

for i=1:num_of_image
    %��ȡ��i��ͼƬ��feature
    data(i,:)=singleImageFeatureExtractor(i);
end
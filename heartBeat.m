dat = dlmread('data/n1rr.txt');
dat = dat(1:50,1);
img1 = imread('heart11.png');
img2 = imread('heart.png');
%dat = [0.1*ones(1,10) ones(1,10)];
figure;
for i = 1:length(dat)
  subplot(121);
  set(gca,'position',[0.1 0.35 0.3 0.3]);
  imshow(img1);
  pause(0.01);% intra-beat, small enough
  imshow(img2);
  axis('off');
  subplot(122);
  plot(dat(1:i),'-b');hold on;
  xlim([1 length(dat)]);
  ylim([min(dat) max(dat)]);
  pause(dat(i));% heart rate
end
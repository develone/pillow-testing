close all

% Read a color PNG image
pkg load image;
rgb_image = imread('lena_rgb_64.png');
imshow(rgb_image);
title('RGB PNG Image');
disp(size(rgb_image))
rows = 64;
cols = 64;
for row = 1 : rows
	for col = 1 :cols
		red(row,col) = rgb_image(row, col, 1);
		grn(row,col) = rgb_image(row, col, 2);
		blu(row,col) = rgb_image(row, col, 2);
	endfor
endfor



upd = 1;
done = 0;
function lift = dwt (flgs,upd,lft,sam,rht,done)
	lift = 0;
	lft
	sam
	rht
	flgs
	upd
	if(flgs == 7) 
		lift=sam - (((bitshift(lft, -1)) + (bitshift(rht, -1))))
	else
		if(flgs==5)
			lift=sam + (((bitshift(lft, -1)) + (bitshift(rht, -1))))
		endif
	endif
	if(flgs==6)
		lift = sam + bitshift((lft+rht+2), -2)			
	else
		if(flgs==4)
			lift = sam - bitshift((lft+rht+2), -2)
		endif
	endif
	
	done=1;
	return;
endfunction

function myloop = tloop(start,myend,flgs,upd,rows,cols,im)
	done=0;
	if(rows==1)
		for k = start:myend
			if(k==2)
				j=1
			endif
			j,k,rows,cols
			lft=im(k-1,j);
			sam=im(k,j);
			rht=im(k+1,j);
			lift = dwt (flgs,upd,lft,sam,rht,done)
			im(k,j) = lift;
			done=1;
		endfor
		j=j+1
	endif
	if(cols==1)
		for j = start:myend
		    if(j==2)
				k=1
			endif
			j,k,rows,cols
			lft=im(k,j-1);
			sam=im(k,j);
			rht=im(k,j+1);
			lift = dwt (flgs,upd,lft,sam,rht,done)
			im(k,j) = lift;
			done=1;
		endfor
		k=k+1
		
	endif
	
	
	return;
endfunction

%lft = red(1,2);
%sam = red(1,1);
%rht = red(1,2);

im=red;
start=2;
myend=31;
%test=4
%bitshift(test, -1)
%low-pass cols
flgs=7;
rows=0;
cols=1;
tloop(start,myend,flgs,upd,rows,cols,im)

%hi-pass rows
flgs=6;
rows=1;
cols=0;
tloop(start,myend,flgs,upd,rows,cols,im) 


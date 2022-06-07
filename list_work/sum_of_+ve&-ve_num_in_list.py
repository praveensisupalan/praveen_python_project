numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
pcount=0
ncount=0
zcount=0
psum=0
for num in numbers:
     if num< 0:
         ncount=ncount+1 psum=psum+num
     elif num>0:
         pcount=pcount+1
     elif num==0:
         zcount=zcount+1

print(f"+ve count = {pcount}, _ve count= {ncount}, zero count={zcount}")
print(psum)

N = 10^6;

oldnum = 10; 
count = 0; 
smallest = 0; 
for i = 1 : N
    num = 0;
    sum = 0; 
    
while (sum <= 1)
    x = rand;
    sum = sum + x;  
    num = num + 1;
end
if (oldnum >= num) 
    smallest = num; 
end
count = count + num; 
end 
smallest
expectedvalue = count/ N;
count

expectedvalue 


    
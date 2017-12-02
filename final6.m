n = 10^6;
morethan5 = 0; 

importance  = 0; 

  for k = 1 : n
     x = randn ; 
   
     if (x > 5) 
        
     
     morethan5 = morethan5 + 1; 
     
     
     end
     
  end 
  num = 0; 
  for k = 1 : n
      x = normrnd(5, 1); 
      if (x > 5) 
        
          importance = importance + exp(-(x^2)/2)/exp(-((x - 5)^2)/2); 
          
      end
 
  end
 morethan5
 importance
 probim = importance / n ; 
 prob =  morethan5 / n;
 probim 
 prob

 
 
 
 
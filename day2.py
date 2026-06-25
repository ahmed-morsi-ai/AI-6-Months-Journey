price = 250                                                                                                                                                             
if price > 255 or price < 0 :                                                                                                                                         
    print ("Error")                                                                                                                                                    
elif price >= 200:                                                                                                                                               
    print ("Ultra Premium")                                                                                                                                                      
elif price >= 100 and 199:                                                                                                                                  
    print ("Premium")                                                                                                                                                      
elif price < 100 :                                                                                                                                                   
    print ("Standard")                                                                                                                                                  
else :                                                                                                                                                                  
    print ("not found")
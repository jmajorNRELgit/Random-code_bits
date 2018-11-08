values = {'A': -4, 'B': 10, 'C': -5, 'D':3}

#pos = {}
#
#neg = {}
#
#for key in values:
#    if values[key] >= 0:
#        pos.update({key : values[key] })
#        
#    else:
#        neg.update({key: values[key]})


        
# ###way 2       
#pos = dict((k,v) for k,v in values.items() if v >0)



###way 3

positives = {}

for k,v in values.items():
    if v > 0:
        positives[k] = v

d = {}
from collections import OrderedDict
d = OrderedDict()

d['x']=100
d['k']=999
d['y']=200
d['z']=300

for k, v in d.items():
    print(k,v)





def sort_by_key(t):
    return t[0]
from collections import OrderedDict 
d=dict() 

d['홍길동']='010-1111-2222' 
d['이순신']='010-3333-4444' 
d['송중기']='010-5555-6666' 
d['송혜교']='010-7777-8888'

for k,v in OrderedDict(sorted(d.items(),key=sort_by_key)).items():
    print(k,v)
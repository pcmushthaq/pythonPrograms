import time 

class custom(dict):
    def __init(self):
        super()
    def __setitem__(self,key,value):
        # Expires after 1 second
        expiry=time.time()+1
        super().__setitem__(key,{'val':value,'expiry':expiry})
    
    def __getitem__(self,key):
        item=super().__getitem__(key)
        timeNow=time.time()
        expiry=item['expiry']
        hasExpired=expiry<timeNow
        if hasExpired:
            super().__delitem__(key)
            raise ItemExpiredException
        else:
            return item['val']
            
class ItemExpiredException(Exception):
    pass 
        
    
somedict=custom()
somedict['hi']='hello'
print(somedict)
print(somedict['hi'])
time.sleep(2)
print(somedict['hi'])

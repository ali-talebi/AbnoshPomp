from django.db import models
from django.db.models.query import QuerySet 


class Blog_Manager(models.Manager) : 

    def show_public(self) : 
        return self.model.objects.filter(status = 'p' )
    
    def len_show_public(self) : 
        return len(self.model.objects.filter(status = 'p'))
    


    

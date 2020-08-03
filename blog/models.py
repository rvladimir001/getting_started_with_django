from django.db import models

'''
id
title
content
created_at
photo
'''

'''
все поля в django являются обязательными, 
но если в параметры передать в параметры "blank=True",
 то поле тогда будет не обязательным к заполнению
'''


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    '''
    auto_now_add - параметр означает что поле будет
    заполняться самим django и будет заполняться единожды,
    позднее редактровать будет не возможно
    '''
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title

from django.db import models
# Create your models here.

class Users(models.Model):
    user_id = models.BigIntegerField(auto_created=True, primary_key=True,  db_index=True, verbose_name="id")
    user_name = models.CharField(max_length=50, db_index=True, verbose_name="用户名")
    head_img = models.CharField(max_length=200, verbose_name="头像", null=False)
    password = models.CharField(max_length=20, verbose_name="密码", null=False)
    email = models.EmailField(verbose_name="邮箱")
    openid = models.CharField(max_length=30, verbose_name="openid")
    unionid = models.CharField(max_length=30, verbose_name="unionid")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
        
    def __repr__(self):
        return "<Users>, id:%s, user_name:%s" % (self.user_id, self.user_name)
    
    
    
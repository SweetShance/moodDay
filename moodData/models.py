from django.db import models
from users.models import Users

# Create your models here.
class TimeClass(models.Model):
    time_id = models.BigIntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=10, verbose_name="类型", null=False) # 天、小时
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    class Meta:
        verbose_name = "时间分类表"
        verbose_name_plural = verbose_name
        
    def __repr__(self):
        return "<TimeClass>, id:%s, title:%s" % (self.time_id, self.title)
    

class MoodLabel(models.Model):
    mood_label_id = models.BigIntegerField(auto_created=True, primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING, verbose_name="用户", related_name="user_mood_label")
    title = models.CharField(max_length=30, verbose_name="标题", null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "心情表标签"
        verbose_name_plural = verbose_name
        
    def __repr__(self):
        return "<TimeClass>, id:%s, title:%s" % (self.mood_label_id, self.title)


class MoodData(models.Model):
    mood_id = models.BigIntegerField(auto_created=True, primary_key=True)
    timeClass = models.ForeignKey("TimeClass", verbose_name="时间分类", on_delete=models.DO_NOTHING, related_name="time_moodData")
    mood_label = models.ForeignKey("MoodLabel", verbose_name="标签", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="标题", max_length=20, null=False)
    text = models.TextField(verbose_name="描述", max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "心情表"
        verbose_name_plural = verbose_name
        
    def __repr__(self):
        return "<TimeClass>, id:%s, title:%s" % (self.mood_id, self.title)


class MoodValue(models.Model):
    mood_value_id = models.BigIntegerField(auto_created=True, primary_key=True)
    value = models.FloatField(verbose_name="心情值")  # -100 - +100
    text = models.TextField(verbose_name="描述", max_length=500)
    mood_data =  models.ForeignKey("MoodData", verbose_name="时间分类", on_delete=models.DO_NOTHING, related_name="time_moodData")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    class Meta:
        verbose_name = "心情值"
        verbose_name_plural = verbose_name
        
    def __repr__(self):
        return "<TimeClass>, id:%s, title:%s" % (self.mood_value_id)

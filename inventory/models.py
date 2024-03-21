from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
 
class MyModelActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)
 
 
class CategoryMaster(models.Model):
    category_types = (
        ('Product','Product'),
        ('Service','Service')
    )
    category_id = models.AutoField(primary_key=True,blank=False,null=False)
    category_name = models.CharField(max_length=100,blank=False,null=False)
    category_type = models.CharField(max_length=50,choices=category_types)
    category_owner = models.ManyToManyField(User)
    created_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='category_creator',blank=True,null=True)
    updated_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='category_updator',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True,null=False,blank=False)
 
    objects = MyModelActiveManager()
    all_objects = models.Manager()
 
    def __str__(self):
        return f'{self.category_name} ({self.category_type})'
 
    class Meta:
        # managed = False
        unique_together = ('category_name', 'category_type')
        db_table = 'CategoryMaster'
 
 
class ItemMaster(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_code = models.CharField(max_length=15,blank=False,null=False,unique=True)
    item_name = models.CharField(max_length=250,blank=False,null=False)
    item_file = models.FileField(upload_to='item_files/')
    specification = models.CharField(max_length=150,blank=False,null=False)
    category = models.ForeignKey(CategoryMaster,on_delete=models.DO_NOTHING,related_name='item_category')
    created_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,
                                   related_name='item_creator',blank=True,null=True)
    updated_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,
                                   related_name='item_updator',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True,null=False,blank=False)
 
    def __str__(self):
        return f'{self.item_name}-{self.specification}' if self.specification else f'{self.item_name}-No specification'
   
    class Meta:
        indexes = [
            models.Index(fields=['item_name', 'item_code']),
        ]
 
    class Meta:
        # managed = False
        unique_together = ('item_name','specification')
        db_table = 'ItemMaster'
 
 
class LocationMaster(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=50,blank=False,null=False)
    created_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,
                                   related_name='location_creator',blank=True,null=True)
    updated_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,
                                   related_name='location_updator',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True,null=False,blank=False)
 
    objects = MyModelActiveManager()
    all_objects = models.Manager()
 
    def __str__(self):
        return f'{self.location_name}'
 
    class Meta:
        # managed = False
        unique_together = ('location_name',)
        db_table = 'LocationMaster'
 
 
class InventoryStockMaster(models.Model):
    inventory_stock_id = models.AutoField(primary_key=True)
    inventory_type_choices = (
                        ('Grn_add','Grn_add'),
                        ('Add_invent','Add_invent'),
                        ('Return','Return'),
                        ('From_loc','From_loc'),
                        ('To_loc','To_loc'),
                     )
    item_quantity_type = (
                        ('Kg','Kg'),
                        ('Lt','Lt'),
                        ('Box','Box'),
                        ('One','One'),
                        ('Strip','Strip'),
                     )
    item_type_choice = (
        ('Raw', 'Raw'),
        ('Finished', 'Finished'),
        ('Made-in','Made-in')
    )
    inventory_code = models.CharField(max_length=150,null=False,blank=False) # 'inventory_type'+'item_type'+'bat_no'+'unique_num'
    inventory_type = models.CharField(max_length=10,choices=inventory_type_choices)
    item_type = models.CharField(max_length=10,choices=item_type_choice)
    batch_no = models.CharField(max_length=100,null=False,blank=False)
    item_var = models.ForeignKey(ItemMaster,on_delete=models.DO_NOTHING,related_name='inventory_item_var')
    quantity = models.IntegerField()
    quantity_type = models.CharField(max_length=10,choices=item_quantity_type)
    location = models.ForeignKey(LocationMaster,on_delete=models.DO_NOTHING,related_name='inventory_location')
    expiry_date = models.DateField(null=False,blank=False)
    created_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='inventory_creator',blank=True,null=True)
    updated_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='inventory_updator',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True,null=False,blank=False)
 
    objects = MyModelActiveManager()
    all_objects = models.Manager()
 
 
    class Meta:
        # managed = False
        db_table = 'InventoryMaster'
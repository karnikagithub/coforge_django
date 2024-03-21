from rest_framework import serializers
from .models import LocationMaster, CategoryMaster, ItemMaster, InventoryStockMaster
from django.contrib.auth.models import User
 
 
class LocationMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationMaster
        fields = '__all__'
 
class ItemMasterSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=CategoryMaster.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    updated_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True)
    created_by = serializers.CharField(required=False)
 
    class Meta:
        model = ItemMaster
        fields = '__all__'
        # extra_kwargs = {
        #     'created_by':{'required':False}
        # }
 
class CategoryMasterSerializer(serializers.ModelSerializer):
    category_owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    updated_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False,
                                                    allow_null=True)
    created_by = serializers.CharField(required=False)
 
    class Meta:
        model = CategoryMaster
        fields = '__all__'

    # def create(self, validated_data):
    #     category_owner_data = validated_data.pop('category_owner')

    #     category = CategoryMaster.objects.create(**validated_data)

    #     category.category_owner.add(*category_owner_data)

    #     return category
 
class InventoryStockMasterSerializer(serializers.ModelSerializer):
    item_var = ItemMasterSerializer()
    # item_var = serializers.PrimaryKeyRelatedField(queryset=ItemMaster.objects.all())
    location = LocationMasterSerializer()
    # location = serializers.PrimaryKeyRelatedField(queryset=LocationMaster.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    updated_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False,
                                                    allow_null=True)
    created_by = serializers.CharField(required=False)
 
    class Meta:
        model = InventoryStockMaster
        fields = '__all__'
 
 
class ItemMasterFileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
 
    def create(self, validated_data):
        print(validated_data)
        # Access the uploaded file from the validated data
        uploaded_file = self.validated_data['file']
 
        print(uploaded_file)
        print('*************************************')
        print(uploaded_file.name)
        # Save the file to the desired location
        ItemMaster.item_file.save(uploaded_file.name, uploaded_file)
        ItemMaster.save()


class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User         
        fields = ['id','username']
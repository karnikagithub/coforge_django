from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import LocationMaster, CategoryMaster, ItemMaster, InventoryStockMaster
from .serializers import LocationMasterSerializer, CategoryMasterSerializer, ItemMasterSerializer, InventoryStockMasterSerializer,ItemMasterFileUploadSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import action
import os
from django.contrib.auth.models import User
from rest_framework import generics


class LocationMasterViewSet(viewsets.ViewSet):
 
    """ This class based view perform the CRUD operation for LOCATION MASTER. """
   
    queryset = LocationMaster.objects.all()
    serializer_class = LocationMasterSerializer
 
   
    def create(self, request):
        print(request.data,'-------------')
        serializer = LocationMasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors,'serializer.errorsserializer.errors')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def list(self, request):
        queryset = LocationMaster.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
 
    def retrieve(self, request, pk=None):
        if pk is not None:
            queryset = LocationMaster.objects.all()
            business_unit = get_object_or_404(queryset,pk=pk)
            serializer = self.serializer_class(business_unit)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
 
    def patch(self, request, pk=None):
        if pk is not None:
            queryset = LocationMaster.objects.get(location_id=pk)
            serializer = self.serializer_class(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'status':'Location Updated Successfully'},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
 
 
class CategoryMasterViewSet(viewsets.ViewSet):
 
    """ This class based view perform the CRUD operation for CATEGORY MASTER. """
   
    queryset = CategoryMaster.objects.all()
    serializer_class = CategoryMasterSerializer
 
   
    def create(self, request):
        serializer = CategoryMasterSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('')
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def list(self, request):
        queryset = CategoryMaster.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
 
    def retrieve(self, request, pk=None):
        if pk is not None:
            queryset = CategoryMaster.objects.all()
            business_unit = get_object_or_404(queryset,pk=pk)
            serializer = self.serializer_class(business_unit)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
 
 
    def patch(self, request, pk=None):
        if pk is not None:
            queryset = CategoryMaster.objects.get(category_id=pk)
            serializer = self.serializer_class(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'status':'Category Updated Successfully'},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
 
 
class ItemMasterViewSet(viewsets.ViewSet):
 
    """ This class based view perform the CRUD operation for ITEM MASTER.
     along with that it also perform the download of item file based upon the ID """
 
    queryset = ItemMaster.objects.all()
    serializer_class = ItemMasterSerializer
    parser_classes = [MultiPartParser,FormParser,JSONParser]
 
   
    def create(self, request):
        serializer = ItemMasterSerializer(data=request.data)
        # print(request.data,'dataaaaaa')
        print(request.data.get('item_name'),'dataaaaaa')
        print(request.data.get('specification'),'dataaaaaa')
        print('')
        if serializer.is_valid():
            # Check if item with the same name and specification already exists
            if ItemMaster.objects.filter(item_name=request.data.get('item_name'),
                                          specification=request.data.get('specification')).exists():
                return JsonResponse({'detail': 'Item with this name and specification already exists.'}, status=status.HTTP_400_BAD_REQUEST)
           
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors,'errorrrrrrrrrrr')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def list(self, request):
        queryset = ItemMaster.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
 
    def retrieve(self, request, pk=None):
        if pk is not None:
            queryset = ItemMaster.objects.all()
            business_unit = get_object_or_404(queryset,pk=pk)
            serializer = self.serializer_class(business_unit)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
 
 
    def patch(self, request, pk=None):
        if pk is not None:
            queryset = ItemMaster.objects.get(item_id=pk)
            serializer = self.serializer_class(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'status':'Item Master Updated Successfully'},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
   
 
    @action(detail=True, methods=['get'])
    def download_file(self, request, pk=None):
        item_master = ItemMaster.objects.get(item_id=pk)
        if item_master.item_file:
            file_path = item_master.item_file.path
            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    response = HttpResponse(file.read(), content_type='application/octet-stream')
                    response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                    return response
            else:
                return Response({'detail': 'File not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'detail': 'No file associated with this item.'}, status=status.HTTP_404_NOT_FOUND)
       
   
    @action(detail=True, methods=['post'], parser_classes=[MultiPartParser, FormParser])
    def upload_file(self, request, pk=None):
        item_master = ItemMaster.objects.get(item_id=pk)
 
        # print(request.data,'request.data')
       
        if 'item_file' not in request.data:
            return Response({'detail': 'No file data provided.'}, status=status.HTTP_400_BAD_REQUEST)
 
        # file_serializer = ItemMasterFileUploadSerializer(data=request.data)
        # print(file_serializer).
 
        # Extract the file from the request data
        file_data = {'item_file': request.data['item_file']}
 
        print(file_data)
       
        # Merge the file data with other form data if needed
        form_data = {**request.data, **file_data}
 
        file_serializer = ItemMasterFileUploadSerializer(data=form_data)
 
        if file_serializer.is_valid():
            # Save the file and update the item_master with the file information
            file_serializer.save(item_master=file_serializer)
            return Response({'detail': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
class InventoryMasterViewSet(viewsets.ViewSet):
 
    """ This class based view perform the CRUD operation for INVENTORY MASTER. """
 
    queryset = InventoryStockMaster.objects.all()
    serializer_class = InventoryStockMasterSerializer
    # parser_classes = [MultiPartParser,FormParser,JSONParser]
 
   
    def create(self, request):
        serializer = InventoryStockMasterSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('')
            print(serializer.errors,'errorrrrrr')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def list(self, request):
        queryset = InventoryStockMaster.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
 
    def retrieve(self, request, pk=None):
        if pk is not None:
            queryset = InventoryStockMaster.objects.all()
            business_unit = get_object_or_404(queryset,pk=pk)
            serializer = self.serializer_class(business_unit)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
 
 
    def patch(self, request, pk=None):
        if pk is not None:
            queryset = InventoryStockMaster.objects.get(inventory_stock_id=pk)
            serializer = self.serializer_class(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'status':'Inventory Updated Successfully'},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UsersViewset(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
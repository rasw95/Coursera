from  rest_framework.decorators import permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 
from django.contrib.auth.models import User, Group
from rest_framework import status
from .serializers import *
from restaurant.models import *
from django.core.paginator import Paginator, EmptyPage
from rest_framework.throttling import AnonRateThrottle , UserRateThrottle
from rest_framework import viewsets

def IsManagerUser(request):
    return request.user.groups.filter(name='Manager').exists()
def Filtring_Searching(request):
    category_title = request.query_params.get('category')
    price = request.query_params.get('price')
    search = request.query_params.get('search')
    if(category_title):
            menuItems = MenuItem.objects.filter(category__title = category_title)
    elif (price):
            menuItems = MenuItem.objects.filter(price__lte = price)
    elif (search):
            menuItems = MenuItem.objects.filter(title__istartswith = search)
    else:
            menuItems = MenuItem.objects.select_related('category').all()  
    
    return menuItems
def Ordering(menuitems, request):
    ordering = request.query_params.get('ordering')
    if(ordering):
        Ordering_fields = ordering.split(',')
        return menuitems.order_by( *Ordering_fields)
    return menuitems
def Pagination(menuItems, request):
    perpage = request.query_params.get('perpage', default = 5)
    page = request.query_params.get('page', default = 1)
    paginator = Paginator(menuItems, per_page= perpage)
    try:
        menuItems = paginator.page(number = page)
        return menuItems
    except EmptyPage:
        menuItems = []
        return menuItems
#----------------------------------------------------------------------------
# Create your views here.
@permission_classes([IsAuthenticated])
class ManagerView(APIView):

    def get(self, request):
        if(not IsManagerUser(request)):
            return Response( "Only Managers can access this request.", status.HTTP_403_FORBIDDEN)
        group = Group.objects.get(name = 'Manager')
        users = group.user_set.all()
        serializer = UserSeralizer(users, many = True)
        return Response( serializer.data)

    def post(self, request):
        if(not IsManagerUser(request)):
            return Response( "Only Managers can access this request.", status.HTTP_403_FORBIDDEN)
        try:
            username = request.data['username']
            if(username):
                user = get_object_or_404(User, username = username)
                group = Group.objects.get(name='Manager')
                group.user_set.add(user)
                return Response(f"{user} added to {group.name} Group.", status.HTTP_201_CREATED )
        except Exception:
            return Response('Please provide username.', status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if(not IsManagerUser(request)):
            return Response( "Only Managers can access this request.", status.HTTP_401_UNAUTHORIZED)
        user = get_object_or_404(User, pk = pk)
        group = Group.objects.get(name = 'Manager')
        group.user_set.remove(user)
        return Response(f'{user.username} removed from {group.name} group.', status.HTTP_200_OK)
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
class CategoryView(APIView):
    def get(self, request):  #Note: Function based view of Ordering, Filring and searching using Query params. Use APIView class.
        categorys = Category.objects.all()
        serializer = CategorySerailizer(categorys, many = True)
        return Response(serializer.data, status.HTTP_200_OK)
    def post(self, request):
        if(not IsManagerUser(request)):
            return Response( "Only Managers can access this request.", status.HTTP_403_FORBIDDEN)
        item = CategorySerailizer(data=request.data)
        item.is_valid()
        item.save()
        return Response (item.data, status.HTTP_201_CREATED)
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
class MenuItemView(viewsets.ModelViewSet):
   
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    ordering_fields=['price','category']
    search_fields=['name','category__title','category__slug']
    #Note: Function based view of Ordering, Filring and searching using Query params. Use APIView class.
    #def get(self, request):  
        #serializer = MenuItemSerializer(Pagination( Ordering( Filtring_Searching(request), request ), request), many=True)
        #return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        if(not IsManagerUser(request)):
            return Response( "Only Managers can access this request.", status.HTTP_403_FORBIDDEN)
        item = MenuItemSerializer(data=request.data)
        item.is_valid()
        item.save()
        return Response (item.data, status.HTTP_201_CREATED)
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
class SingleItemView(APIView):
    def get(self, request, pk):
        item = get_object_or_404(MenuItem, pk = pk)
        serializer = MenuItemSerializer(item)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk):
        if(not IsManagerUser(request)):
            return Response( "Only Managers can access this request.", status.HTTP_403_FORBIDDEN)
        item = get_object_or_404(MenuItem, pk=pk)
        serializer = MenuItemSerializer(item, data= request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)
    
    def patch(self, request, pk):
        if(not IsManagerUser(request)):
              return Response( "Only Managers can access this request.", status.HTTP_403_FORBIDDEN)
        item = get_object_or_404(MenuItem, pk = pk)
        serializer = MenuItemSerializer(item, data= request.data, partial = True)
        serializer.is_valid()
        serializer.save()
        return Response (serializer.data, status.HTTP_200_OK)
    
    def delete(self, request, pk):
        if(not IsManagerUser(request)):
            return Response( "Only Managers can access this request.", status.HTTP_403_FORBIDDEN)
        item = get_object_or_404(MenuItem, pk = pk)
        item.delete()
        return Response(f'{item.title} Deleted')
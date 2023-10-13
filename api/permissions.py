from rest_framework.permissions import BasePermission

class CustomUserPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True

        elif request.method == 'POST':
            return request.user.is_staff

class CustomUserDetailPermission(BasePermission):

    def has_permission(self, request, view):
         
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff
        
class CategoryPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True

        elif request.method == 'POST':
            return request.user.is_staff

class CategoryDetailPermission(BasePermission):

    def has_permission(self, request, view):
         
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff
        
class ProductPermission(BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True

        elif request.method == 'POST':
            return request.user.is_staff

class ProductDetailPermission(BasePermission):

    def has_permission(self, request, view):
         
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff
        

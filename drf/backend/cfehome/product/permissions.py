from rest_framework import permissions




class IsStaffMember(permissions.DjangoModelPermissions): #custom permission
 def has_permission(self, request, view):
     if request.user.is_staff:
         if request.user.has_perm("products.view_product"):
             return True
         return False     
     return  False;
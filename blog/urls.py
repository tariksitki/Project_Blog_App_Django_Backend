
from django.urls import path
from .views import new_post, postListView, post_List
## Not:  baska bir app den import ederken / ile yada .. ile bir üst klasöre cikmak diye birsey yok. direkt olarak app in adi yatilir ve dod notation yapilir.

urlpatterns = [
   path("", post_List, name="home"),
   path("create/", new_post, name="create"),
   
]
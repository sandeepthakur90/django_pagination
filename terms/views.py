from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    all_post = Post.objects.all().order_by('id')
    paginator = Paginator(all_post, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    last_data = page_obj.paginator.num_pages
    
    
    return render(request,'home.html',{'all_post':page_obj,'last_data':last_data,'totalsizelist': [n+1 for n in range(last_data)]})
   


    
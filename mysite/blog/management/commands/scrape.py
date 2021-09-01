from django.core.management.base import BaseCommand
import requests
from pyquery import PyQuery as pq
from django.contrib.auth.models import User
from blog.models import Post
from django.utils import timezone

class Command(BaseCommand):
    help = "This command will show web-scrap (custom no. of pages)"

    def add_arguments(self, parser):
        parser.add_argument('pages',type=int)

    def handle(self, *args, **kwargs):
        user_no = kwargs['pages']
        cnt = 0
        print("User want No. of pages = ", user_no)
        page = requests.get("https://www.tutorialspoint.com/python3/index.htm")
        html = pq(page.text)

        #------------------------------------------------
        list_data = []
        for item in html.items('.chapters a'):
            if(cnt < user_no):
                per_page = requests.get("https://www.tutorialspoint.com" + item.attr("href"))
                per_html = pq(per_page.text)
                per_title = per_html(".tutorial-content h1").eq(0).text()
                src = per_html(".cover img").attr("src")
                val = per_html('.tutorial-content')
                val('#google-top-ads').remove()
                val('.google-bottom-ads').remove()
                val('.pre-btn').remove()
                val('.nxt-btn').remove()
                if(src):
                    img_name = per_html(".cover img").attr("alt").replace(" ","-")
                    img_url = "https://www.tutorialspoint.com" + src
                    with open('media/blog/images/'+img_name+'.jpg','wb') as f:
                        im = requests.get(img_url)
                        f.write(im.content)
                
                if Post.objects.filter(title=per_title).exists():
                    continue
                else:
                    data = Post(author = User.objects.get_or_create(username="System")[0],
                    title = per_title,
                    text = val,
                    published_date = timezone.now(),
                    blog_img = 'blog/images/'+img_name+'.jpg' if src else None)
                    list_data.append(data)
                    cnt += 1
        Post.objects.bulk_create(list_data)
        if(cnt > 0):
            print("Total %d pages are scrape" %cnt)
        else:
            print("All pages are scrape")


        #------------------------------------------------
        
        # total_pages = list(html(".chapters a").items())
        # total = len(total_pages)
        
        # d = Post.objects.filter(author__username="System").count()
        # print("Data = ",d)

        # list_data = []
        # for i in range(total):
        #     if(cnt < user_no):
        #         per_page = requests.get("https://www.tutorialspoint.com" + total_pages[i].attr("href"))
        #         per_html = pq(per_page.text)
        #         per_title = per_html(".tutorial-content h1").eq(0).text()
        #         src = per_html(".cover img").attr("src")
        #         if(src):
        #             img_name = per_html(".cover img").attr("alt").replace(" ","-")
        #             img_url = "https://www.tutorialspoint.com" + src
        #             with open('media/blog/images/'+img_name+'.jpg','wb') as f:
        #                 im = requests.get(img_url)
        #                 f.write(im.content)
                
        #         if Post.objects.filter(title=per_title).exists():
        #             continue
        #         else:
        #             data = Post(author = User.objects.get_or_create(username="System")[0],
        #             title = per_title,
        #             text = per_html(".tutorial-content p").text(),
        #             published_date = timezone.now(),
        #             blog_img = 'blog/images/'+img_name+'.jpg' if src else None)
        #             list_data.append(data)
        #             cnt += 1
        # Post.objects.bulk_create(list_data)
        # if(cnt > 0):
        #     print("Total %d pages are scrape" %cnt)
        # else:
        #     print("All pages are scrape")
                

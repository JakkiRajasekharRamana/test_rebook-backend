from django.shortcuts import render
import requests
from django.http import JsonResponse
from polls. models import Book
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404

 



@csrf_exempt
def fetch_book(request):
    if request.method == 'POST':
        data =json.loads(request.body)
        
        # book_id = request.POST.get('book_id')
        book_id = data.get('book_id')
        print(book_id)
        
        api_url = f'https://www.googleapis.com/books/v1/volumes?q={book_id}&projection=full&maxResults=5'

        response = requests.get(api_url)
        data = response.json()
        book_data= data.get('items')

       
        if 'items' in data:
            book_data = data['items'][0]['volumeInfo']
            book = Book(
                title=book_data.get('title'),
                author=', '.join(book_data.get('authors', [])),
                image=book_data['imageLinks'].get('thumbnail')
                
            )
            book.save()

        return JsonResponse({'message':'Data saved'})
        books=Book.objects.all()
        return render(request,'search_results.html',{'books':books})
    # return JsonResponse({'error':'Invalid request'})    
    # return render(request,'search.html')

def getData(request):
    data =Book.objects.all().values()
    serializedData=list(data)
    return JsonResponse(serializedData,safe=False)

def deleteRecord(request,title):
    record=get_object_or_404(Book,title=title)
    record.delete()
    return JsonResponse({'message':'Record Deleated'})

# envnt bin : source /home/priyanshu/myDjangoproject/my_env/bin/activate 

# class ReactView(APIView):
#     # permission_classes ={permissions.AllowAny}
#     # @api_view(['GET','POST'])

#     def get(self,request):
#        data =Book.objects.all()
#        serializer=ReactSerializer(data,many=True)
#        return Response(serializer.data)

#     def fetch_book(request):
#         if request.method == 'POST':
        
#             book_id = request.POST.get('book_id')
#             sbook=str({book_id})
#             api_url = 'https://www.googleapis.com/books/v1/volumes?q=$'+sbook+'&projection=full&maxResults=5'
        
#             response = requests.get(api_url)
#             data = response.json()
#             book_data= data.get('items')

       
#             if 'items' in data:
#                 book_data = data['items'][0]['volumeInfo']
#                 book = Book(
#                     title=book_data.get('title'),
#                     author=', '.join(book_data.get('authors', [])),
#                     description=book_data.get('description', ''),
#                     image=book_data['imageLinks'].get('thumbnail')
#                 )
#                 book.save()
#             books=Book.objects.all()
#             return render(request,'search_results.html',{'books':books})
        
#         return render(request,'search.html')
#     def post(self,request): 
#         serializer=ReactSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
   

   
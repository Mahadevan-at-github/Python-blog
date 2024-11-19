
from django.contrib import messages
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import BlogForm, CommnetForm
from .models import Book, loginTable, BlogPosting


def detailsView(request,user_id):

    name = Book.objects.get(id=user_id)

    return render(request, 'adminfile/detail.html', {'name': name})


def deleteView(request,user_id):

    user = Book.objects.get(id=user_id)

    if request.method=='POST':
        user.delete()

        return redirect('admin_view')
    return render(request,'adminfile/delete.html',{'user':user})

def userRegistration(request):

    login_table = loginTable()
    userprofile = Book()

    if request.method=='POST':

        userprofile.username=request.POST['username']
        userprofile.f_name = request.POST['f_name']
        userprofile.l_name = request.POST['l_name']
        userprofile.email = request.POST['email']
        userprofile.contact=request.POST['contact']
        userprofile.password = request.POST['password']
        userprofile.password2 = request.POST['password2']

        login_table.username = request.POST['username']
        login_table.password = request.POST['password']
        login_table.password2 = request.POST['password2']
        login_table.type='user'

        if request.POST['password']==request.POST['password2']:
            userprofile.save()
            login_table.save()

            messages.info(request,'Registration Success')
            return redirect('login')
        else:
            messages.info(request,'Password not working')
            return redirect('book')

    return render(request,'adminfile/register.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=loginTable.objects.filter(username=username,password=password,type ='user').exists()

        try:
            if user is not None:
                user_details=loginTable.objects.get(username=username,password=password)
                user_name = user_details.username
                type=user_details.type

                if type=='user':
                    request.session['username'] = user_name
                    return redirect('blogdisplay')
                elif type=='admin':
                    request.session['username'] = user_name
                    return redirect('admin_view')
            else:
                messages.info(request,'Invalid Username or Password')
        except:
            messages.info(request,'Invalid Role')

    return render(request, 'adminfile/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def update_user(request, user_id):
    try:
        # Retrieve the user object
        user = Book.objects.get(id=user_id)
    except Book.DoesNotExist:
        # Handle case where user does not exist
        messages.error(request, 'User not found.')
        return redirect('admin_view')  # Replace with your user list view name

    if request.method == 'POST':
        # Update fields from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Validate passwords match
        if password != password2:
            messages.error(request, 'Passwords do not match.')
        else:
            # Update user details
            user.username = username
            user.email = email
            user.contact = contact
            user.password = password
            user.password2 = password2
            user.save()

            messages.success(request, 'User updated successfully!')
            return redirect('admin_view')

    return render(request, 'adminfile/update.html', {'user': user})

def Search_User(request):
    query = None
    books = None
    user_name = request.session['username']

    if 'q' in request.GET:

        query=request.GET.get('q')
        books = Book.objects.filter(Q(username__icontains=query)| Q(email__icontains=query))
    else:
        books=[]

    context = {'user_name':user_name,'books':books,'query':query}
    return render(request,'adminfile/search.html',context)



def index(request):

    return render(request,'adminfile/index.html')

def admin_view(request):

    user_name = request.session['username']
    books = Book.objects.all()

    paginator = Paginator(books, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request,'adminfile/listview.html',{'user_name':user_name,'page':page})



def user_view(request):
    user_name = request.session['username']

    return render(request,'user/userindex.html',{'user_name':user_name})



# <--- Blog Section --->


def createBlog(request):

    blogs =BlogPosting.objects.all()


    if request.method=='POST':
        form = BlogForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('blogdisplay')

    else:
        form = BlogForm()

    return render(request,'user/usercreateblog.html',{'form':form, 'blogs':blogs})

def blogDetail(request):
    blogs = BlogPosting.objects.all()

    return render(request, 'user/userlist.html', {'blogs': blogs})

def blogUpdate(request,blog_id):

    blog = BlogPosting.objects.get(id=blog_id)

    if request.method=='POST':
        form = BlogForm(request.POST,request.FILES,instance=blog)

        if form.is_valid():
            form.save()
            return redirect('blogdisplay')
    else:
        form=BlogForm(instance=blog)

    return render(request,'user/userupdate.html',{'form':form})

def deleteblog(request,blog_id):

    blog = BlogPosting.objects.get(id=blog_id)

    if request.method=='POST':

        blog.delete()

        return redirect('blogdisplay')

    return render(request,'user/userdelete.html',{'blog':blog})


# <--admin blog-->

def bloglist(request,blog_id):

    blog = BlogPosting.objects.get(id=blog_id)

    return render(request, 'user/userdetails.html', {'blog': blog})


def blog(request):
    blogs = BlogPosting.objects.all()

    return render(request, 'adminfile/blog.html', {'blogs': blogs})



def blogdelete(request,blog_id):
        blog = BlogPosting.objects.get(id=blog_id)

        if request.method == 'POST':
            blog.delete()

            return redirect('admin_view')

        return render(request, 'adminfile/blogdelete.html', {'blog': blog})

def blogcontent(request,blog_id):
    blog = BlogPosting.objects.get(id=blog_id)

    return render(request,'user/usercontent.html',{'blog':blog})

def blogdisplay(request):
    blogs = BlogPosting.objects.all()

    return render(request, 'user/blogdisplay.html', {'blogs': blogs})


def blogComment(request,blog_id):
    blog = BlogPosting.objects.get(id=blog_id)

    if request.method == 'POST':
        form = CommnetForm(request.POST, instance=blog)

        if form.is_valid():
            form.save()
            return redirect('blogdisplay')
    else:
        form = CommnetForm(instance=blog)

    return render(request, 'user/comment.html', {'form': form})
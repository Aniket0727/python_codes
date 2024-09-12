from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
import re
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect
from productclick.models import productclickscount
from mydata.models import mydata3
from pdata.models import pdata2
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.db.models import Max
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import difflib
from django.core.mail import send_mail
import random
import string
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password



@csrf_protect
def delete_product(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        product = get_object_or_404(pdata2, pid=pid)
        product.delete()
        try:
            product2 = productclickscount.objects.get(pid=pid)
            product2.delete()
        except Exception as e:
            pass
        messages.success(request, 'Product deleted successfully.')
        return redirect('viewproduct')  # Redirect to the homepage or the relevant page
    return redirect('viewproduct')  # Redirect to the homepage if the method is not POST


@csrf_protect
def pclick(request):
    if request.method == "POST":
        uid = request.session.get('user_id')
        # uid = request.POST.get('uid')
        pid = request.POST.get('pid')
        pname = request.POST.get('pname')
        
        if productclickscount.objects.filter(uid=uid, pid=pid).exists():
            product_click = productclickscount.objects.get(uid=uid, pid=pid)
            product_click.productclick += 1
            product_click.save()
        else:
            product_click = productclickscount.objects.create(uid=uid, pid=pid, pname=pname, productclick=1)
            product_click.save()

    return redirect(reverse('product_detail', args=[pid]))


def index(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        # Password strength validation
        password_pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
        
        if mydata3.objects.filter(username=username).exists():
            messages.error(request, "Email already exists. Please choose a different Email.")
        elif pass1 != pass2:
            messages.error(request, "Password and Confirm Password do not match!")
        elif not password_pattern.match(pass1):
            messages.error(request, "Please enter a stronger password. It must be at least 8 characters long, include uppercase and lowercase letters, a number, and a special character.")
        else:
            otp = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            # Store OTP in session
            request.session['otp1'] = otp
            request.session['otp_expiry'] = (timezone.now() + timedelta(minutes=10)).isoformat()
            
            # Store registration details in session
            request.session['registration_data'] = {
                'name': name,
                'username': username,
                'pass1': pass1,
                'pass2': pass2
            }
            
            try:
                send_mail(
                    'Smart Shop',
                    f'Your OTP code is: {otp}',
                    'aniketkangude9060@gmail.com',
                    [username],
                    fail_silently=False,
                )
                # messages.success(request, "Please check your email for the OTP.")
                return redirect('otp')  # Redirect to OTP verification page
            except Exception as e:
                messages.error(request, f'There was an error sending your OTP: {str(e)}')

    return render(request, "index.html")


def otp(request):
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        session_otp = request.session.get('otp1')
        otp_expiry_str = request.session.get('otp_expiry')
        otp_expiry = datetime.fromisoformat(otp_expiry_str) if otp_expiry_str else None

        if not session_otp or not otp_expiry:
            messages.error(request, "OTP has expired or is not available.")
            return redirect('index')
        
        if timezone.now() > otp_expiry:
            messages.error(request, "OTP has expired. Please request a new OTP.")
            return redirect('index')

        if entered_otp == session_otp:
            # Retrieve registration details from session
            registration_data = request.session.get('registration_data')
            if registration_data:
                name = registration_data['name']
                username = registration_data['username']
                pass1 = registration_data['pass1']
                pass2 = registration_data['pass2']
                
                
                hashed_password1 = make_password(pass1)
                hashed_password2 = make_password(pass2)
                
                # Save user data to the database
                data = mydata3(name=name, username=username, pass1=hashed_password1, pass2=hashed_password2)
                data.save()
                
                # Clear session data
                request.session.pop('otp1', None)
                request.session.pop('otp_expiry', None)
                request.session.pop('registration_data', None)
                
                messages.success(request, "OTP verified successfully!")
                return redirect('home')
            else:
                messages.error(request, "Registration data is missing.")
                return redirect('index')
        else:
            messages.error(request, "Invalid OTP. Please try again.")
    
    return render(request, 'otp.html')



def login(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['password']
        try:
            user = mydata3.objects.get(username=username)
            if check_password(password, user.pass1):  # Verify password hash
                request.session['user_id'] = user.id
                messages.success(request, "Login successful!")
                return redirect('home')  # Assuming you have a URL name 'home'
            else:
                messages.error(request, "Invalid login details")
        except mydata3.DoesNotExist:
            messages.error(request, "User does not exist")
    return render(request, "login.html")

@csrf_protect
def home(request):
            if 'user_id' not in request.session:
                return redirect('login')
            else:

                pdata=pdata2.objects.all()
                data2={
                    'pdata':pdata
                }
    
            
            return render(request, "home.html",data2)
  
def about(request):
        if 'user_id' not in request.session:
                return redirect('login')
        return render(request, "about.html")

def contactus(request):
        
        if 'user_id' not in request.session:
                return redirect('login')
        
        if request.method == 'POST':
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            try:  
                send_mail(
                        subject,
                        message,
                        'aniketkangude9060@gmail.com',
                        [email],
                        fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully.')
            except Exception as e:
                messages.error(request, f'There was an error sending your message: {str(e)}')
        return render(request, "contactus.html")

def addproduct(request):
        if 'user_id' not in request.session:
                return redirect('login')
        else:
                if request.method == "POST" and request.FILES['photo']:
                        oname = request.POST['oname']
                        pname = request.POST['pname']
                        page = request.POST['page']
                        op = request.POST['op']
                        sp = request.POST['sp']
                        pd = request.POST['pd']
                        address = request.POST['address']
                        image = request.FILES['photo']
                        id=request.session.get('user_id')
                        pid=request.session.get('id')               
                                       
                        data2 = pdata2(oname=oname, pname=pname, page=page, op=op, sp=sp, pd=pd, address=address, image=image,uid=id,pid=pid)
                        data2.save()
                        messages.success(request, 'Product added successfully.')
                return render(request, 'addproduct.html')

def profile(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = mydata3.objects.filter(id=user_id).first()
      
        if user:
            data = {
                'user': user
            }
            return render(request, "profile.html", data)
        else:
            return redirect('login')  # Redirect to login page if user_id is invalid
    else:
        return redirect('login.html') 
    
def viewproduct(request):
        user_id = request.session.get('user_id')
        # print(user_id)

        if user_id:
            product=pdata2.objects.filter(uid=user_id)
            data={
                          'product':product
                    }
            return render(request,'viewproduct.html',data)
           
        else:
              return redirect('login')                    

def logout(request):
    request.session.flush()
    # request.cookies.clear()
    messages.success(request, "logout successful!")
    
    return redirect("login")

def product_detail(request, pk):
    product = get_object_or_404(pdata2, pid=pk)
    return render(request, 'product_detail.html', {'product': product})


def rp_products(request):
    user_id = request.session.get('user_id')
    
    # Get the maximum value of productclick for the user's clicks
    max_click = productclickscount.objects.filter(uid=user_id).aggregate(Max('productclick'))['productclick__max']
    # print(max_click)
    # Get the product click entry with the maximum productclick value
    highest_click_product = None
    if max_click is not None:
        highest_click_product = productclickscount.objects.filter(uid=user_id, productclick=max_click).first()
    # print(highest_click_product)
    # Get the related pdata2 object for the highest click product
    highest_clicked_product = None
    if highest_click_product:
        try:
            highest_clicked_product = pdata2.objects.get(pid=highest_click_product.pid)
        except pdata2.DoesNotExist:
            highest_clicked_product = None
    
    # If we have the highest clicked product, find related products using sklearn
    if highest_clicked_product:
        # Get all products data from pdata2
        products_data = pdata2.objects.all().values('pid', 'pname', 'op', 'sp', 'pd', 'address', 'uid')
        df = pd.DataFrame(products_data)
        
        # Extract product names
        # product_names = df['pname'].tolist()
        product_names = df['pname'].tolist()
        
        
        # Use TF-IDF to vectorize the product names
        vectorizer = TfidfVectorizer(stop_words='english')
        feature_vectors = vectorizer.fit_transform(product_names)
        similarity = cosine_similarity(feature_vectors)
        
        #notes
        # Cosine Similarity: It is a measure of similarity between two vectors. It calculates the cosine of the angle between them. The value ranges from -1 to 1, where:
        # 1: Indicates the vectors (product names) are identical.
        # 0: Indicates no similarity.
        # -1: Indicates complete dissimilarity.
        # Find close matches for the highest clicked product
        
        find_close_match = difflib.get_close_matches(highest_clicked_product.pname, product_names)
        
        related_products = []
        if find_close_match:
            close_match = find_close_match[0]
            similarity_score = list(enumerate(similarity[product_names.index(close_match)]))
            sorted_similar_products = sorted(similarity_score, key=lambda x: x[1], reverse=True)
            
            for i, j in sorted_similar_products:
                if j > 0.01:  # A threshold to filter out very dissimilar products
                    related_products.append(df.iloc[i]['pid'])
        
        # Convert related products to a list of pdata2 objects, excluding the highest clicked product itself
        products = pdata2.objects.filter(pid__in=related_products).exclude(pid=highest_clicked_product.pid)
    else:
        products = []

    # Render the rp_products.html template with the highest clicked product and related products data
    return render(request, "rp_products.html", {'products': products})

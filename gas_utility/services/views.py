# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Customer, ServiceRequest
from .forms import CustomerForm, ServiceRequestForm
from django.contrib import messages
from django.utils import timezone




def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=email, password=password, email=email)
            user.save()
            customer = form.save(commit=False)
            customer.user = user
            customer.save()

            login(request, user)
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            request.session['customer_id'] = customer.id

            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('create_service_request')
    else:
        form = CustomerForm()
    return render(request, 'services/create_customer.html', {'form': form})

# View for creating a new service request
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            customer_id = request.session.get('customer_id')
            customer = Customer.objects.get(id=customer_id)
            service_request.customer = customer
            service_request.status = 'Pending'
            service_request.save()
            return redirect('/services')
    else:
        form = ServiceRequestForm()
    
    return render(request, 'services/create_service_request.html', {'form': form})

# View for successful submission
# views.py
def admin_request_allrequest(request):
    if ('customer_id' not in request.session) or (request.session.get('customer_id') != 1) :
        messages.error(request, "You are not authorsed to use this service")
        return redirect('/services/')

    customer_id = request.session.get('customer_id')
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        messages.error(request, "Invalid session. Please log in again.")
        return redirect('login')
    
    service_requests = ServiceRequest.objects.all()

    return render(request, 'services/request_approve.html', {'service_requests': service_requests})


def service_request_success(request):
    if 'customer_id' not in request.session:
        messages.error(request, "You must be logged in to view your service requests.")
        return redirect('login')


    customer_id = request.session.get('customer_id')
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        messages.error(request, "Invalid session. Please log in again.")
        return redirect('login')
    
    service_requests = ServiceRequest.objects.all()

    return render(request, 'services/success.html', {'service_requests': service_requests})

#complete status


def complete_service_request(request, request_id):
    if 'customer_id' not in request.session:
        messages.error(request, "You must be logged in to complete a service request.")
        return redirect('login')

    service_request = ServiceRequest.objects.get(id=request_id)
    if service_request.status == 'Pending':
        service_request.status = 'Completed'
        service_request.resolved_at = timezone.now()
        service_request.save()
        messages.success(request, "Service request marked as completed.")

    return redirect('admin_request_allrequest')

#track request
def track_service_request(request, request_id):
    if 'customer_id' not in request.session:
        messages.error(request, "You must be logged in to track a service request.")
        return redirect('login')

    # Get the specific service request
    service_request =ServiceRequest.objects.get(id=request_id)

    return render(request, 'services/track_service_request.html', {'service_request': service_request})




from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.hashers import check_password
#user login

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            customer = Customer.objects.get(email=email)
            if password==customer.password: 

                request.session['customer_id'] = customer.id  # Store customer ID in session
                request.session['customer_email'] = customer.email  # Store email in session
                
                messages.success(request, "Login successful!")
                return redirect("/services/") 
            else:
                messages.error(request, "Invalid password.")
        except Customer.DoesNotExist:
            messages.error(request, "User does not exist.")

    return render(request, 'login.html')  


#profile section

def profile(request, customer_id):

    logged_in_customer_id = request.session.get('customer_id')

    if not logged_in_customer_id or logged_in_customer_id != customer_id:
        messages.error(request, "You are not eligible to access this information.")
        return redirect('home')  

    customer = Customer.objects.get(id=customer_id)
    return render(request, 'profile.html', {'customer': customer})





def user_logout(request):
   
    if 'customer_id' in request.session:
        del request.session['customer_id']
    if 'customer_email' in request.session:
        del request.session['customer_email']
    
    messages.info(request, "You have been logged out.")
    return redirect('/services/')


def home(request):
    return render(request, "home.html")
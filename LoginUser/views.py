from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout

from django.contrib.auth.models import User
from .forms import details
from .models import detailsModel



from django.contrib.auth.models import User


def portfolioForId(request, user_id):
    details_instance = detailsModel.objects.filter(user_model=user_id).last()

    if details_instance:
        # Extracting all fields from the details_model
        user_data = {
            'name': details_instance.name,
            'phone_number': details_instance.phone_number,
            'email': details_instance.email,
            'age': details_instance.age,
            'github_link': details_instance.github_link,
            'linkedin_link': details_instance.linkedin_link,
            'facebook_link': details_instance.facebook_link,
            'insta_link': details_instance.insta_link,
            'role': details_instance.role,
            'about_me': details_instance.about_me,
            'skills': details_instance.skills,
            'project1_name': details_instance.project1_name,
            'project1_desc': details_instance.project1_desc,
            'project1_pic_link': details_instance.project1_pic_link,
            'project1_project_link': details_instance.project1_project_link,
            'project2_name': details_instance.project2_name,
            'project2_desc': details_instance.project2_desc,
            'project2_pic_link': details_instance.project2_pic_link,
            'project2_project_link': details_instance.project2_project_link,
            'project3_name': details_instance.project3_name,
            'project3_desc': details_instance.project3_desc,
            'project3_pic_link': details_instance.project3_pic_link,
            'project3_project_link': details_instance.project3_project_link,
            # 'temp_no':details_instance.temp_no,
        }
    else:
        user_data = None
    # return render(request, f'tempChoice.html', {'data': user_data})
    return render(request, f'portfolio{details_instance.temp_no}.html', {'data': user_data})



def success(request):
    print(request.user)
    details_instance = detailsModel.objects.filter(user_model=request.user).last()
    if details_instance:
        name = details_instance.name
    else:
        name = None
    url=request.user.id
    age = details_instance.age
    data = {'name': name, 'age': age,'url':url}
    return render(request, 'success.html', {'block': data})




# Create your views here.
# def index(request):
#     print(request.user)
#     if request.user.is_anonymous:
#         return redirect("/login") 
    
#     if request.method == 'POST':
#         form = details(request.POST)
#         # id=request.user.id
#         if form.is_valid():
#             # Process the form data
#             namee = form.cleaned_data['name']
#             phone_number = form.cleaned_data['phone_number']
#             age = form.cleaned_data['age']
#             current_user = request.user
#             details_instance = detailsModel(user_model=request.user,name=namee , phone_number=phone_number, age=age)
#             details_instance.save()
#             return redirect('/success')
#     else:

#         form = details()

#     return render(request, 'index.html',{'form':form})


from .models import detailsModel

# def index(request):
#     # print(request.user)
    
#     if request.user.is_anonymous:
#         return redirect("/login") 

#     # Check if the user has existing details
#     user_details = detailsModel.objects.filter(user_model=request.user).first()

#     if request.method == 'POST':
#         form = details(request.POST, instance=user_details)
        
#         if form.is_valid():
#             namee = form.cleaned_data['name']
#             phone_number = form.cleaned_data['phone_number']
#             age = form.cleaned_data['age']

#             if user_details:
#                 # Update existing details
#                 user_details.name = namee
#                 user_details.phone_number = phone_number
#                 user_details.age = age
#                 form.instance.temp_no = form.cleaned_data['temp_no']
#                 user_details.save()
#             else:
#                 # Create new details instance
#                 details_instance = detailsModel(user_model=request.user, name=namee, phone_number=phone_number, age=age)
#                 form.instance.temp_no = form.cleaned_data['temp_no']
#                 details_instance.save()

#             return redirect('/success')
#     else:
#         # If user has existing details, populate the form with those details
#         form = details(instance=user_details) if user_details else details()

#     return render(request, 'index.html', {'form': form, 'edit_mode': bool(user_details)})


from django.shortcuts import render, redirect
from .forms import details

def index(request):
    if request.user.is_anonymous:
        return redirect("/login") 

    # Check if the user has existing details
    user_details = detailsModel.objects.filter(user_model=request.user).first()

    if request.method == 'POST':
        form = details(request.POST, instance=user_details)
        
        if form.is_valid():
            # Set the user_model and temp_no before saving the form
            form.instance.user_model = request.user
            form.instance.temp_no = form.cleaned_data['temp_no']

            if user_details:
                # Update existing details
                user_details.name = form.cleaned_data['name']
                user_details.phone_number = form.cleaned_data['phone_number']
                user_details.age = form.cleaned_data['age']
                user_details.save()
            else:
                # Create new details instance
                form.save()

            return redirect('/success')
    else:
        # If the user has existing details, populate the form with those details
        form = details(instance=user_details) if user_details else details()

    return render(request, 'index.html', {'form': form, 'edit_mode': bool(user_details)})



def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


def registerUser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email=request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username, email, password)
        login(request, user)
        return redirect('/')

    return render(request,'register.html')
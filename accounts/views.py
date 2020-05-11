from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserCreationForm, UserChangeForm, SignInForm

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .email_token import account_activation_token
from .models import UserAccount 
 
from django.core.mail import EmailMessage

from django.contrib import messages
from django.contrib.auth.decorators import login_required

def SignUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('accounts/confirm_email.html', {    
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
            
            """
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('accounts/confirm_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            # user.email(subject, message)

            messages.success(request, ('Please Confirm your email to complete registration.'))
            """
    
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def Activate(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = UserAccount.objects.get(pk=uid)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def SignInView(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request,user)
                    return redirect("/admin/")
                # elif user.is_active:
                else:
                    login(request,user)
                    return redirect("home")    
            else:
                messages.error(request, 'An unexpected error occured.')
                return redirect("signin") 
    else:
        form = SignInForm()
    return render(request, 'accounts/signin.html', {'form': form})

""" 
def SignInView(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     return redirect("/")
    # else:
 
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            # if user is not None:
            #     login(request, user)
            #     return redirect("/")

            if user.is_superuser:
                login(request,user)
                return redirect("/admin/")
            elif user.is_active:
                login(request,user)
                return redirect("home")    
    else:
        form = SignInForm()
    return render(request, 'accounts/signin.html', {'form': form})



    # if user.is_authenticated: 
    #     return redirect('home')
 
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     user = authenticate(email=email, password=password)
  
        # if user.is_superuser:
        #     login(request,user)
        #     return redirect("/admin/")
        # elif user.is_active:
        #     login(request,user)
        #     return redirect("/")
        # else:
        #     return HttpResponse("Your account was inactive.")
    # else:
    #     return render(request, "accounts/signin.html")
 """

@login_required
def ProfileView(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cập nhật thành công!')
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)

    context = {'form': form}
    return render(request, 'accounts/profile.html', context)


# print("They used username: {} and password: {}".format(username,password))
 
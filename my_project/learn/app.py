from django.contrib.auth.forms import PasswordChangeForm


@login_required
def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)

        # 키워드인자명을 함께 써줘도 가능
        # password_change_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_change_form.is_valid():
            password_cchange_form.save()
            return redirect('accounts:people', request.user.username)

    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password.html', {
        'password_change_form': password_change_form
    })



# urls.py
urlpatterns = [
    path('password/', views.password, name='password'), ]



# urls.py
urlpatterns = [
    path('password/', views.password, name='password'), ]
from allauth.account.forms import LoginForm


def login_form_ctx(request):
    return {"loginctx": LoginForm()}

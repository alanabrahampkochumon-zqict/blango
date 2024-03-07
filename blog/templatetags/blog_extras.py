from django.contrib.auth import get_user_model
from django.template import Library
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

user_model = get_user_model()
register = Library()

@register.filter(name="author_details")
def author_details(user, current_user=None):
  if not isinstance(user, user_model):
    return ""

  if user == current_user:
    return format_html("<strong>me</strong>")

  if user.first_name and user.last_name:
    name =  f"{user.first_name} {user.last_name}"
  else:
    name = user.username

  if user.email:
    email  = user.email
    prefix = format_html("<a href='mailto:{}'>", email)
    suffix = format_html("</a>")
  else:
    prefix = ""
    suffix = ""
  
  return format_html("{}{}{}", prefix, name, suffix)
  
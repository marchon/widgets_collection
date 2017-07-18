from __future__ import unicode_literals
import frappe
from widgets_collection import login

no_cache = 1
no_sitemap = 1

def get_context(context):

	path_parts = context.get("pathname", "").split('/')
	print(path_parts)

	login.apply_context(context)

	return context

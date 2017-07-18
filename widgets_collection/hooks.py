# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "widgets_collection"
app_title = "Widgets Collection"
app_publisher = "DigiThinkIT, Inc."
app_description = "A collection of useful widgets for Frappe and ERPNext integrations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "forellana@digithinkit.com"
app_license = "MIT"

website_route_rules = [
	{"from_route": "/login", "to_route": "widget_login"}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/widgets_collection/css/widgets_collection.css"
# app_include_js = "/assets/widgets_collection/js/widgets_collection.js"

# include js, css files in header of web template
# web_include_css = "/assets/widgets_collection/css/widgets_collection.css"
# web_include_js = "/assets/widgets_collection/js/widgets_collection.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "widgets_collection.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "widgets_collection.install.before_install"
# after_install = "widgets_collection.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "widgets_collection.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"widgets_collection.tasks.all"
# 	],
# 	"daily": [
# 		"widgets_collection.tasks.daily"
# 	],
# 	"hourly": [
# 		"widgets_collection.tasks.hourly"
# 	],
# 	"weekly": [
# 		"widgets_collection.tasks.weekly"
# 	]
# 	"monthly": [
# 		"widgets_collection.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "widgets_collection.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "widgets_collection.event.get_events"
# }

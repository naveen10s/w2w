from . import __version__ as app_version

app_name = "w2w"
app_title = "W2W"
app_publisher = "Neveka Berl J"
app_description = "Bio & E - Waste Management"
app_email = "nevekaberyl@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/w2w/css/w2w.css"
# app_include_js = "/assets/w2w/js/w2w.js"

# include js, css files in header of web template
# web_include_css = "/assets/w2w/css/w2w.css"
# web_include_js = "/assets/w2w/js/w2w.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "w2w/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "w2w.utils.jinja_methods",
#	"filters": "w2w.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "w2w.install.before_install"
# after_install = "w2w.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "w2w.uninstall.before_uninstall"
# after_uninstall = "w2w.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "w2w.utils.before_app_install"
# after_app_install = "w2w.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "w2w.utils.before_app_uninstall"
# after_app_uninstall = "w2w.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "w2w.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"w2w.tasks.all"
#	],
#	"daily": [
#		"w2w.tasks.daily"
#	],
#	"hourly": [
#		"w2w.tasks.hourly"
#	],
#	"weekly": [
#		"w2w.tasks.weekly"
#	],
#	"monthly": [
#		"w2w.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "w2w.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "w2w.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "w2w.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["w2w.utils.before_request"]
# after_request = ["w2w.utils.after_request"]

# Job Events
# ----------
# before_job = ["w2w.utils.before_job"]
# after_job = ["w2w.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"w2w.auth.validate"
# ]

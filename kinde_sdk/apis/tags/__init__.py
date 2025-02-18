# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from kinde_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    USERS = "Users"
    APIS = "APIs"
    APPLICATIONS = "Applications"
    BUSINESS = "Business"
    CALLBACKS = "Callbacks"
    CONNECTED_APPS = "Connected Apps"
    ENVIRONMENTS = "Environments"
    FEATURE_FLAGS = "Feature Flags"
    INDUSTRIES = "Industries"
    OAUTH = "OAuth"
    ORGANIZATIONS = "Organizations"
    PERMISSIONS = "Permissions"
    ROLES = "Roles"
    SUBSCRIBERS = "Subscribers"
    TIMEZONES = "Timezones"

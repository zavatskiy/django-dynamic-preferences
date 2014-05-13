"""
    Preference registries store collections of Global, User and SitePreference instances
    They do the actual job of registering preferences that are declared via :
    ' preference_instance.register() '
"""

from django.conf import settings
from django.utils.importlib import import_module


class PreferenceRegistry(dict):

    # Set to True to enable autodiscover in .test module
    test = False

    # The package where registry will try to find preferences to register
    package = "preferences"

    def register(self, app, name, preference):

        try:
            self[app][name] = preference

        except KeyError:
            self[app] = {}
            self[app][name] = preference

    def get(self, app, name, d=None):

        return self[app][name]

    def app(self, app):
        """
            Return all registered preferences for a given app
        """
        return self[app]

    def autodiscover(self, force_reload=False):
        """
            Populate the registry by iterating through every app
        """
        self.clear()
        prefix = ""

        if self.test:
            # Import test preferences instead of regular ones
            prefix = ".tests"

        for app in settings.INSTALLED_APPS:
            # try to import self.package inside current app
            package = '{0}{1}.{2}'.format(app, prefix, self.package)
            try:
                mod = import_module(package)
                if force_reload:
                    # mainly used in tests
                    reload(mod)

            except ImportError:
                # Module does not exist
                pass

        print("autodiscovered:", self)
        return self

user_preferences = PreferenceRegistry()
site_preferences = PreferenceRegistry()
global_preferences = PreferenceRegistry()
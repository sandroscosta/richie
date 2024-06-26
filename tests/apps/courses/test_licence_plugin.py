"""
Licence plugin tests
"""

from django.db import transaction

from cms.api import add_plugin
from cms.models import Placeholder

from richie.apps.core.tests.utils import CMSPluginTestCase
from richie.apps.courses.cms_plugins import LicencePlugin
from richie.apps.courses.factories import LicenceFactory


# pylint: disable=too-many-ancestors
class LicencePluginTestCase(CMSPluginTestCase):
    """Licence plugin tests case"""

    @transaction.atomic
    def test_licence_plugin_context_and_html(self):
        """
        Instanciating this plugin with an instance should populate the context
        and render in the template.
        """
        placeholder = Placeholder.objects.create(slot="test")

        # Create random values for parameters with a factory
        licence = LicenceFactory()

        model_instance = add_plugin(placeholder, LicencePlugin, "en", licence=licence)
        plugin_instance = model_instance.get_plugin_class_instance()
        plugin_context = plugin_instance.render({}, model_instance, None)

        # Check if "instance" is in plugin context
        self.assertIn("instance", plugin_context)

        # Check if parameters, generated by the factory, are correctly set in
        # "instance" of plugin context
        self.assertEqual(plugin_context["instance"].licence.name, licence.name)

        # Template context
        context = self.get_practical_plugin_context()

        # Get generated html for licence name
        html = context["cms_content_renderer"].render_plugin(model_instance, {})

        # Check rendered name
        self.assertIn(licence.name, html)

    @transaction.atomic
    def test_licence_plugin_header_level(self):
        """
        Header level can be changed from context variable 'header_level'.
        """
        # We deliberately use level '10' since it can be substituted from any
        # reasonable default level.
        header_format = """<h10 class="licence-plugin__title">{}</h10>"""

        # Dummy slot where to include plugin
        placeholder = Placeholder.objects.create(slot="test")

        # Create random values for parameters with a factory, empty url to
        # simplify render of tested HTML
        licence = LicenceFactory(url="")

        # Template context with additional variable to define a custom header
        # level for header markup
        context = self.get_practical_plugin_context({"header_level": 10})

        add_plugin(placeholder, LicencePlugin, "en", licence=licence)

        # Render placeholder so plugin is fully rendered in real situation
        html = context["cms_content_renderer"].render_placeholder(
            placeholder, context=context, language="en"
        )

        expected_header = header_format.format(licence.name)

        # Expected header markup should match given 'header_level' context
        # variable
        self.assertInHTML(expected_header, html)

    @transaction.atomic
    def test_licence_plugin_rdfa_property_default_with_url(self):
        """
        The RDFa licence property should be present by default on the url if any.
        """
        # Dummy slot where to include plugin
        placeholder = Placeholder.objects.create(slot="test")

        licence = LicenceFactory(url="https://example.com")

        context = self.get_practical_plugin_context({})
        add_plugin(placeholder, LicencePlugin, "en", licence=licence)

        # Render placeholder so plugin is fully rendered in real situation
        html = context["cms_content_renderer"].render_placeholder(
            placeholder, context=context, language="en"
        )

        # RDFa markup should be present by default
        self.assertEqual(html.count('property="license"'), 1)
        self.assertEqual(
            html.count(
                '<div class="licence-plugin" property="license" typeof="CreativeWork">'
            ),
            1,
        )
        self.assertEqual(
            html.count('<meta property="url" content="https://example.com" />'), 1
        )

    @transaction.atomic
    def test_licence_plugin_rdfa_property_activated_no_url(self):
        """
        The RDFa licence property is tagged on the content if there is no url.
        """
        # Dummy slot where to include plugin
        placeholder = Placeholder.objects.create(slot="test")

        # Create a license with no url
        licence = LicenceFactory(url="")

        # Template context with additional variable to activate license property
        context = self.get_practical_plugin_context({"is_license_property": True})
        add_plugin(placeholder, LicencePlugin, "en", licence=licence)

        # Render placeholder so plugin is fully rendered in real situation
        html = context["cms_content_renderer"].render_placeholder(
            placeholder, context=context, language="en"
        )

        # RDFa markup should be present but not the url property
        self.assertEqual(html.count('property="license"'), 1)
        self.assertEqual(
            html.count(
                '<div class="licence-plugin" property="license" typeof="CreativeWork">'
            ),
            1,
        )
        self.assertEqual(html.count('<meta property="url" '), 0)

    @transaction.atomic
    def test_licence_plugin_rdfa_property_deactivated(self):
        """
        The RDFa licence property can be deactivated from context variable 'is_license_property'.
        """
        # Dummy slot where to include plugin
        placeholder = Placeholder.objects.create(slot="test")

        # Create random values for parameters with a factory
        licence = LicenceFactory()

        # Template context with additional variable to deactivate license property
        context = self.get_practical_plugin_context({"is_license_property": False})
        add_plugin(placeholder, LicencePlugin, "en", licence=licence)

        # Render placeholder so plugin is fully rendered in real situation
        html = context["cms_content_renderer"].render_placeholder(
            placeholder, context=context, language="en"
        )

        # RDFa markup should not be present
        self.assertNotIn('property="license"', html)

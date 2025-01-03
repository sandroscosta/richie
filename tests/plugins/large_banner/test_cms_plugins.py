"""
Large banner plugin tests
"""

import re

from django.db import IntegrityError
from django.test import TestCase
from django.test.client import RequestFactory

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer

from richie.plugins.large_banner.cms_plugins import LargeBannerPlugin
from richie.plugins.large_banner.factories import LargeBannerFactory


class LargeBannerCMSPluginsTestCase(TestCase):
    """Large banner plugin tests case"""

    def test_cms_plugins_large_banner_title_required(self):
        """
        A "title" is required when instantiating a large banner.
        """
        with self.assertRaises(IntegrityError) as cm:
            LargeBannerFactory(title=None)
        self.assertTrue(
            (
                'null value in column "title" of relation "large_banner_largebanner"'
                " violates not-null constraint"
            )
            in str(cm.exception)
            or "Column 'title' cannot be null" in str(cm.exception)
        )

    # pylint: disable=deprecated-method,no-member
    # Due to a conflict between Django 1.11 and pylint with the assertRegex method that is
    # *not* deprecated but is marked so by pylint
    def test_cms_plugins_large_banner_context_and_html(self):
        """
        Instanciating this plugin with an instance should populate the context
        and render in the template.

        In particular, images should be cropped and big images should be included in
        4 sizes for responsiveness using the srcset attribute. 'content' and 'template'
        are just basically filled from factory.
        """
        placeholder = Placeholder.objects.create(slot="test")

        # Create random values for parameters with a factory
        large_banner = LargeBannerFactory()
        fields_list = [
            "title",
            "background_image",
            "logo",
            "logo_alt_text",
            "template",
            "content",
        ]

        model_instance = add_plugin(
            placeholder,
            LargeBannerPlugin,
            "en",
            **{field: getattr(large_banner, field) for field in fields_list},
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)

        # Check if "instance" is in context
        self.assertIn("instance", context)

        # Check if parameters, generated by the factory, are correctly set in "instance" of context
        self.assertEqual(context["instance"].title, large_banner.title)
        self.assertEqual(
            context["instance"].background_image, large_banner.background_image
        )
        self.assertEqual(context["instance"].logo, large_banner.logo)
        self.assertEqual(context["instance"].logo_alt_text, large_banner.logo_alt_text)
        self.assertEqual(context["instance"].template, large_banner.template)
        self.assertEqual(context["instance"].content, large_banner.content)

        # Get the generated html
        renderer = ContentRenderer(request=RequestFactory())
        html = renderer.render_plugin(model_instance, {})

        # Check that all expected elements are in the html
        self.assertIn(large_banner.title, html)
        background_image_base = large_banner.background_image.url.replace("/media", "")
        self.assertIn('class="large-banner__background"', html)
        rexp_background = re.compile(
            f'src="/media/(.)*{background_image_base:s}__1900x450_q85_crop-smart'
        )
        self.assertRegex(html, rexp_background)
        self.assertIn(f"{background_image_base:s}__2495x550_q85_crop-%2C0", html)
        self.assertIn(f"{background_image_base:s}__2495x550_q85_crop-%2C0", html)
        self.assertIn(f"{background_image_base:s}__1900x450_q85_crop-%2C0", html)
        self.assertIn(f"{background_image_base:s}__1280x400_q85_crop-%2C0", html)
        self.assertIn(f"{background_image_base:s}__768x450_q85_crop-%2C0", html)
        logo_base = large_banner.logo.url.replace("/media", "")
        rexp_logo = re.compile(f'src="/media/(.)*{logo_base:s}__200x100_q85_crop')
        self.assertRegex(html, rexp_logo)
        self.assertIn(f"{logo_base:s}__200x100_q85_crop", html)
        self.assertIn(f'alt="{large_banner.logo_alt_text:s}"', html)

    def test_cms_plugins_large_banner_no_background_image(self):
        """
        Instanciating this plugin with an instance but no background image should render
        a default image in the html.
        The default image is defined as background image in the CSS.
        """
        placeholder = Placeholder.objects.create(slot="test")

        # Create random values for parameters with a factory
        large_banner = LargeBannerFactory(background_image=None)
        fields_list = [
            "title",
            "background_image",
            "logo",
            "logo_alt_text",
            "template",
            "content",
        ]

        model_instance = add_plugin(
            placeholder,
            LargeBannerPlugin,
            "en",
            **{field: getattr(large_banner, field) for field in fields_list},
        )

        # Get the generated html
        renderer = ContentRenderer(request=RequestFactory())
        html = renderer.render_plugin(model_instance, {})

        # Check that all expected elements are in the html
        self.assertIn('class="large-banner"', html)
        self.assertFalse('class="large-banner__background"' in html)
        self.assertIn('class="large-banner__content"', html)

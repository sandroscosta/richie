"""
Default settings for the Richie courses app.

If you use Django Configuration for your settings, you can use our mixin to import these
default settings:
    ```
    from configurations import Configuration
    from richie.apps.courses.settings.mixins import RichieCoursesConfigurationMixin

    class MyConfiguration(RichieCoursesConfigurationMixin, Configuration):
        ...
    ```

Otherwise, you can just use the usual Django pattern in your settings.py file:
    ```
    from richie.apps.courses.settings import *
    ```
"""

from django.utils.translation import gettext_lazy as _


def richie_placeholder_conf(name):
    """
    Returns a common CMS placeholder configuration that can be shared to placeholders.

    Arguments:
        name (string): Name of placeholder to display in page structure.

    Returns:
        dict: Placeholder configuration.
    """
    return {
        "name": name,
        "excluded_plugins": ["GoogleMapPlugin"],
        "parent_classes": {
            "BlogPostPlugin": ["SectionPlugin"],
            "CategoryPlugin": ["SectionPlugin"],
            "CoursePlugin": ["SectionPlugin"],
            "GlimpsePlugin": ["SectionPlugin"],
            "OrganizationPlugin": ["SectionPlugin"],
            "OrganizationsByCategoryPlugin": ["SectionPlugin"],
            "PersonPlugin": ["SectionPlugin"],
            "ProgramPlugin": ["SectionPlugin"],
        },
        "child_classes": {
            "SectionPlugin": [
                "BlogPostPlugin",
                "CategoryPlugin",
                "CoursePlugin",
                "GlimpsePlugin",
                "LinkPlugin",
                "NestedItemPlugin",
                "OrganizationsByCategoryPlugin",
                "OrganizationPlugin",
                "PersonPlugin",
                "ProgramPlugin",
                "CKEditorPlugin",
            ],
            "NestedItemPlugin": ["NestedItemPlugin", "LinkPlugin"],
        },
    }


# Associated LMS backends
RICHIE_LMS_BACKENDS = []

# Easy Thumbnails
THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
    "easy_thumbnails.processors.background",
)

# Django CMS
CMS_TEMPLATES = (
    ("courses/cms/course_detail.html", _("Course page")),
    ("courses/cms/organization_list.html", _("Organization list")),
    ("courses/cms/organization_detail.html", _("Organization page")),
    ("courses/cms/category_list.html", _("Category list")),
    ("courses/cms/category_detail.html", _("Category page")),
    ("courses/cms/blogpost_list.html", _("Blog post list")),
    ("courses/cms/blogpost_detail.html", _("Blog post page")),
    ("courses/cms/person_detail.html", _("Person page")),
    ("courses/cms/person_list.html", _("Person list")),
    ("courses/cms/program_detail.html", _("Program page")),
    ("courses/cms/program_list.html", _("Program list")),
    ("search/search.html", _("Search")),
    ("richie/child_pages_list.html", _("List of child pages")),
    ("richie/homepage.html", _("Homepage")),
    ("richie/single_column.html", _("Single column")),
    ("richie/three_columns_33.html", _("Three columns: (33% | 33% | 33%)")),
    ("richie/two_columns_50.html", _("Two columns: (50% | 50%)")),
    ("richie/two_columns_25_75.html", _("Two columns: (25% | 75%)")),
    ("richie/two_columns_75_25.html", _("Two columns: (75% | 25%)")),
)

CMS_PLACEHOLDER_CONF = {
    # -- Static Placeholders
    # Footer
    "footer": {
        "name": _("Footer"),
        "plugins": ["NestedItemPlugin", "LinkPlugin"],
        "NestedItemPlugin": ["LinkPlugin"],
    },
    "static_blogpost_headline": {
        "name": _("Static headline"),
        "plugins": ["SectionPlugin", "CKEditorPlugin"],
        "child_classes": {"SectionPlugin": ["CKEditorPlugin"]},
    },
    # -- Page Placeholders
    # Homepage
    "richie/homepage.html maincontent": {
        "name": _("Main content"),
        "plugins": ["LargeBannerPlugin", "SectionPlugin", "SliderPlugin"],
        "child_classes": {
            "SectionPlugin": [
                "BlogPostPlugin",
                "CategoryPlugin",
                "CoursePlugin",
                "CKEditorPlugin",
                "GlimpsePlugin",
                "LinkPlugin",
                "NestedItemPlugin",
                "OrganizationsByCategoryPlugin",
                "OrganizationPlugin",
                "PersonPlugin",
                "ProgramPlugin",
                "SectionPlugin",
            ],
            "NestedItemPlugin": ["CategoryPlugin"],
        },
    },
    # Single column page
    "richie/single_column.html maincontent": richie_placeholder_conf(_("Main content")),
    # Three equal 33/33/33 page
    "richie/three_columns_33.html maincontent": richie_placeholder_conf(
        _("Main content")
    ),
    "richie/three_columns_33.html secondcontent": richie_placeholder_conf(
        _("Secondary content")
    ),
    "richie/three_columns_33.html thirdcontent": richie_placeholder_conf(
        _("Third content")
    ),
    # Two equal 50/50 page
    "richie/two_columns_50.html maincontent": richie_placeholder_conf(
        _("Main content")
    ),
    "richie/two_columns_50.html secondcontent": richie_placeholder_conf(
        _("Secondary content")
    ),
    # Two columns 25/75 page
    "richie/two_columns_25_75.html maincontent": richie_placeholder_conf(
        _("Main content")
    ),
    "richie/two_columns_25_75.html secondcontent": richie_placeholder_conf(
        _("Secondary content")
    ),
    # Two columns 75/25 page
    "richie/two_columns_75_25.html maincontent": richie_placeholder_conf(
        _("Main content")
    ),
    "richie/two_columns_75_25.html secondcontent": richie_placeholder_conf(
        _("Secondary content")
    ),
    # Course detail
    "courses/cms/course_detail.html course_cover": {
        "name": _("Cover"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/course_detail.html course_introduction": {
        "name": _("Catch phrase"),
        "plugins": ["PlainTextPlugin"],
        "limits": {"PlainTextPlugin": 1},
    },
    "courses/cms/course_detail.html course_teaser": {
        "name": _("Teaser"),
        "plugins": ["VideoPlayerPlugin"],
        "limits": {"VideoPlayerPlugin": 1},
    },
    "courses/cms/course_detail.html course_description": {
        "name": _("About the course"),
        "plugins": ["CKEditorPlugin"],
        "limits": {"CKEditorPlugin": 1},
    },
    "courses/cms/course_detail.html course_skills": {
        "name": _("What you will learn"),
        "plugins": ["CKEditorPlugin"],
    },
    "courses/cms/course_detail.html course_format": {
        "name": _("Format"),
        "plugins": ["CKEditorPlugin"],
    },
    "courses/cms/course_detail.html course_prerequisites": {
        "name": _("Prerequisites"),
        "plugins": ["CKEditorPlugin"],
    },
    "courses/cms/course_detail.html course_team": {
        "name": _("Team"),
        "plugins": ["PersonPlugin"],
    },
    "courses/cms/course_detail.html course_plan": {
        "name": _("Plan"),
        "plugins": ["NestedItemPlugin"],
        "child_classes": {"NestedItemPlugin": ["NestedItemPlugin"]},
    },
    "courses/cms/course_detail.html course_information": {
        "name": _("Complementary information"),
        "plugins": ["SectionPlugin"],
        "parent_classes": {
            "CKEditorPlugin": ["SectionPlugin"],
            "SimplePicturePlugin": ["SectionPlugin"],
            "GlimpsePlugin": ["SectionPlugin"],
        },
        "child_classes": {
            "SectionPlugin": ["CKEditorPlugin", "SimplePicturePlugin", "GlimpsePlugin"]
        },
    },
    "courses/cms/course_detail.html course_license_content": {
        "name": _("License for the course content"),
        "plugins": ["LicencePlugin"],
        "limits": {"LicencePlugin": 1},
    },
    "courses/cms/course_detail.html course_license_participation": {
        "name": _("License for the content created by course participants"),
        "plugins": ["LicencePlugin"],
        "limits": {"LicencePlugin": 1},
    },
    "courses/cms/course_detail.html course_categories": {
        "name": _("Categories"),
        "plugins": ["CategoryPlugin"],
    },
    "courses/cms/course_detail.html course_icons": {
        "name": _("Icon"),
        "plugins": ["CategoryPlugin"],
        "limits": {"CategoryPlugin": 1},
    },
    "courses/cms/course_detail.html course_organizations": {
        "name": _("Organizations"),
        "plugins": ["OrganizationPlugin"],
    },
    "courses/cms/course_detail.html course_assessment": {
        "name": _("Assessment and Certification"),
        "plugins": ["CKEditorPlugin"],
    },
    "courses/cms/course_detail.html course_required_equipment": {
        "name": _("Required equipment"),
        "plugins": ["CKEditorPlugin"],
    },
    "courses/cms/course_detail.html course_accessibility": {
        "name": _("Accessibility"),
        "plugins": ["CKEditorPlugin"],
    },
    # Organization detail
    "courses/cms/organization_detail.html banner": {
        "name": _("Banner"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/organization_detail.html logo": {
        "name": _("Logo"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/organization_detail.html categories": {
        "name": _("Categories"),
        "plugins": ["CategoryPlugin"],
    },
    "courses/cms/organization_detail.html description": {
        "name": _("Description"),
        "plugins": ["CKEditorPlugin"],
        "limits": {"CKEditorPlugin": 1},
    },
    "courses/cms/organization_detail.html excerpt": {
        "name": _("Excerpt"),
        "plugins": ["PlainTextPlugin"],
        "limits": {"PlainTextPlugin": 1},
    },
    "courses/cms/organization_detail.html related_organizations": {
        "name": _("Organizations"),
        "plugins": ["OrganizationPlugin"],
    },
    # Category detail
    "courses/cms/category_detail.html banner": {
        "name": _("Banner"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/category_detail.html logo": {
        "name": _("Logo"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/category_detail.html icon": {
        "name": _("Icon"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/category_detail.html description": {
        "name": _("Description"),
        "plugins": ["CKEditorPlugin"],
        "limits": {"CKEditorPlugin": 1},
    },
    "courses/cms/category_detail.html additional_information": {
        "name": _("Additional Information"),
        "plugins": ["SectionPlugin"],
        "parent_classes": {
            "CKEditorPlugin": ["SectionPlugin"],
            "SimplePicturePlugin": ["SectionPlugin"],
            "GlimpsePlugin": ["SectionPlugin"],
            "NestedItemPlugin": ["SectionPlugin"],
        },
        "child_classes": {
            "SectionPlugin": [
                "CKEditorPlugin",
                "SimplePicturePlugin",
                "GlimpsePlugin",
                "NestedItemPlugin",
            ],
            "NestedItemPlugin": ["NestedItemPlugin"],
        },
    },
    # Person detail
    "courses/cms/person_detail.html categories": {
        "name": _("Categories"),
        "plugins": ["CategoryPlugin"],
    },
    "courses/cms/person_detail.html portrait": {
        "name": _("Portrait"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/person_detail.html bio": {
        "name": _("Bio"),
        "plugins": ["PlainTextPlugin"],
        "limits": {"PlainTextPlugin": 1},
    },
    "courses/cms/person_detail.html maincontent": {
        "name": _("Main Content"),
        "plugins": ["CKEditorPlugin", "PersonPlugin", "SectionPlugin", "GlimpsePlugin"],
        "child_classes": {
            "SectionPlugin": ["CKEditorPlugin", "GlimpsePlugin", "PersonPlugin"]
        },
        "limits": {"CKEditorPlugin": 1},
    },
    "courses/cms/person_detail.html organizations": {
        "name": _("Organizations"),
        "plugins": ["OrganizationPlugin"],
    },
    # Blog page detail
    "courses/cms/blogpost_detail.html author": {
        "name": _("Author"),
        "plugins": ["PersonPlugin"],
        "limits": {"PersonPlugin": 1},
    },
    "courses/cms/blogpost_detail.html categories": {
        "name": _("Categories"),
        "plugins": ["CategoryPlugin"],
    },
    "courses/cms/blogpost_detail.html cover": {
        "name": _("Cover"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/blogpost_detail.html excerpt": {
        "name": _("Excerpt"),
        "plugins": ["PlainTextPlugin"],
        "limits": {"PlainTextPlugin": 1},
    },
    "courses/cms/blogpost_detail.html body": {
        "name": _("Body"),
        "excluded_plugins": ["CKEditorPlugin", "GoogleMapPlugin"],
    },
    "courses/cms/blogpost_detail.html headline": {
        "name": _("Headline"),
        "plugins": ["SectionPlugin", "CKEditorPlugin"],
        "child_classes": {"SectionPlugin": ["CKEditorPlugin"]},
    },
    # Program page detail
    "courses/cms/program_detail.html program_categories": {
        "name": _("Categories"),
        "plugins": ["CategoryPlugin"],
    },
    "courses/cms/program_detail.html program_cover": {
        "name": _("Cover"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/program_detail.html program_teaser": {
        "name": _("Teaser"),
        "plugins": ["VideoPlayerPlugin"],
        "limits": {"VideoPlayerPlugin": 1},
    },
    "courses/cms/program_detail.html program_excerpt": {
        "name": _("Excerpt"),
        "plugins": ["PlainTextPlugin"],
        "limits": {"PlainTextPlugin": 1},
    },
    "courses/cms/program_detail.html program_organizations": {
        "name": _("Organizations"),
        "plugins": ["OrganizationPlugin"],
    },
    "courses/cms/program_detail.html program_body": {
        "name": _("Body"),
        "plugins": ["CKEditorPlugin"],
        "limits": {"CKEditorPlugin": 1},
    },
    "courses/cms/program_detail.html program_objectives": {
        "name": _("What you will learn"),
        "plugins": ["CKEditorPlugin"],
    },
    "courses/cms/program_detail.html program_courses": {
        "name": _("Courses"),
        "plugins": ["CoursePlugin"],
    },
    "courses/cms/program_detail.html program_team": {
        "name": _("Instructors"),
        "plugins": ["PersonPlugin"],
    },
    "courses/cms/program_detail.html program_information": {
        "name": _("Complementary information"),
        "plugins": ["SectionPlugin"],
        "parent_classes": {
            "CKEditorPlugin": ["SectionPlugin"],
            "SimplePicturePlugin": ["SectionPlugin"],
            "GlimpsePlugin": ["SectionPlugin"],
        },
        "child_classes": {
            "SectionPlugin": ["CKEditorPlugin", "SimplePicturePlugin", "GlimpsePlugin"]
        },
    },
    "courses/cms/program_list.html maincontent": {
        "name": _("Main content"),
        "plugins": ["SectionPlugin"],
        "child_classes": {
            "SectionPlugin": [
                "BlogPostPlugin",
                "CategoryPlugin",
                "CoursePlugin",
                "GlimpsePlugin",
                "LinkPlugin",
                "OrganizationPlugin",
                "OrganizationsByCategoryPlugin",
                "PersonPlugin",
                "CKEditorPlugin",
                "SectionPlugin",
                "NestedItemPlugin",
            ],
            "NestedItemPlugin": ["CategoryPlugin"],
        },
    },
}

# Main CKEditor configuration
CKEDITOR_SETTINGS = {
    "language": "{{ language }}",
    "skin": "moono-lisa",
    "toolbarCanCollapse": False,
    "contentsCss": "/static/richie/css/ckeditor.css",
    # Enabled showblocks as default behavior
    "startupOutlineBlocks": True,
    # Enable some plugins
    # 'extraPlugins': 'codemirror',
    # Disable element filter to enable full HTML5, also this will let
    # append any code, even bad syntax and malicious code, so be careful
    "removePlugins": "stylesheetparser",
    "allowedContent": True,
    # Image plugin options
    "image_prefillDimensions": False,
    # Justify text using shortand class names
    "justifyClasses": ["text-left", "text-center", "text-right"],
    # Default toolbar configurations for djangocms_text_ckeditor
    "toolbar": "CMS",
    "toolbar_CMS": [
        ["Undo", "Redo"],
        ["cmsplugins", "-", "ShowBlocks"],
        ["Format", "Styles"],
        ["RemoveFormat"],
        ["Maximize"],
        "/",
        ["Bold", "Italic", "Underline", "-", "Subscript", "Superscript"],
        ["JustifyLeft", "JustifyCenter", "JustifyRight"],
        ["Link", "Unlink"],
        ["NumberedList", "BulletedList", "-", "HorizontalRule"],
        ["Source"],
    ],
}
# Share the same configuration for djangocms_text_ckeditor field and derived
# CKEditor widgets/fields
CKEDITOR_SETTINGS["toolbar_HTMLField"] = CKEDITOR_SETTINGS["toolbar_CMS"]

# CKEditor configuration for basic formatting
CKEDITOR_BASIC_CONFIGURATION = {
    "language": "{{ language }}",
    "skin": "moono-lisa",
    "toolbarCanCollapse": False,
    "contentsCss": "/static/css/ckeditor.css",
    # Only enable following tag definitions
    "allowedContent": ["p", "b", "i", "a[href,target]"],
    # Enabled showblocks as default behavior
    "startupOutlineBlocks": True,
    # Default toolbar configurations for djangocms_text_ckeditor
    "toolbar": "HTMLField",
    "toolbar_HTMLField": [["Undo", "Redo"], ["Bold", "Italic"], ["Link", "Unlink"]],
}

# CKEditor configuration for formatting limited to:
# paragraph, bold, italic and numbered or bulleted lists.
CKEDITOR_LIMITED_CONFIGURATION = {
    "language": "{{ language }}",
    "skin": "moono-lisa",
    "toolbarCanCollapse": False,
    "contentsCss": "/static/css/ckeditor.css",
    # Only enable following tag definitions
    "allowedContent": ["p", "b", "i", "ol", "ul", "li"],
    # Enabled showblocks as default behavior
    "startupOutlineBlocks": True,
    # Default toolbar configurations for djangocms_text_ckeditor
    "toolbar": "HTMLField",
    "toolbar_HTMLField": [
        ["Undo", "Redo"],
        ["Bold", "Italic"],
        ["Link", "Unlink"],
        ["NumberedList", "BulletedList", "-"],
    ],
}

# CKEditor configuration for formatting section title:
# only bold entity
CKEDITOR_INLINE_BOLD_CONFIGURATION = {
    "language": "{{ language }}",
    "skin": "moono-lisa",
    "toolbarCanCollapse": False,
    "contentsCss": "/static/css/ckeditor.css",
    # Only enable following tag definitions
    "allowedContent": ["strong"],
    # Block commands which adds break lines (Enter & Shift + Enter)
    # Enter Key Code = 13
    # CKEDITOR.SHIFT + Enter = 2228224 + 13 = 2228237
    "blockedKeystrokes": [13, 2228237],
    "keystrokes": [[13, None], [2228237, None]],
    # Enabled showblocks as default behavior
    "startupOutlineBlocks": True,
    # Default toolbar configurations for djangocms_text_ckeditor
    "toolbar_HTMLField": [["Undo", "Redo"], ["Bold"]],
    "enterMode": 2,
    "autoParagraph": False,
    "resize_enabled": False,
    "height": 68,
}

# Additional LinkPlugin templates. Note how choice value is just a keyword
# instead of full template path. Value is used inside a path formatting
# such as "templates/djangocms_link/VALUE/link.html"
DJANGOCMS_LINK_TEMPLATES = [("button-caesura", _("Button caesura"))]

DJANGOCMS_VIDEO_TEMPLATES = [("full-width", _("Full width"))]

# Richie plugins

RICHIE_PLAINTEXT_MAXLENGTH = {"course_introduction": 200, "bio": 150, "excerpt": 240}

RICHIE_SIMPLETEXT_CONFIGURATION = [
    {
        "placeholders": ["course_skills", "course_plan"],
        "ckeditor": "CKEDITOR_LIMITED_CONFIGURATION",
    },
    {
        "placeholders": ["course_description"],
        "ckeditor": "CKEDITOR_LIMITED_CONFIGURATION",
        "max_length": 1200,
    },
    {
        "placeholders": ["maincontent"],
        "ckeditor": "CKEDITOR_SETTINGS",
        "max_length": 5000,
    },
    {
        "placeholders": [
            "course_assessment",
            "course_format",
            "course_prerequisites",
            "course_accessibility",
            "course_required_equipment",
        ],
        "ckeditor": "CKEDITOR_BASIC_CONFIGURATION",
    },
]

RICHIE_SIMPLEPICTURE_PRESETS = {
    # Formatting images for the courses search index
    "cover": {
        "src": {"size": (300, 170), "crop": "smart"},
        "srcset": [
            {
                "options": {"size": (300, 170), "crop": "smart", "upscale": True},
                "descriptor": "300w",
            },
            {
                "options": {"size": (600, 340), "crop": "smart", "upscale": True},
                "descriptor": "600w",
            },
            {
                "options": {"size": (900, 560), "crop": "smart", "upscale": True},
                "descriptor": "900w",
            },
        ],
        "sizes": "300px",
    },
    "icon": {
        "src": {"size": (60, 60), "crop": "smart"},
        "srcset": [
            {
                "options": {"size": (60, 60), "crop": "smart", "upscale": True},
                "descriptor": "60w",
            },
            {
                "options": {"size": (120, 120), "crop": "smart", "upscale": True},
                "descriptor": "120w",
            },
            {
                "options": {"size": (180, 180), "crop": "smart", "upscale": True},
                "descriptor": "180w",
            },
        ],
        "sizes": "60px",
    },
}

# If true the toolbar item will already be showed. If false only a page which already
# have the extension will have the toolbar item and users won't be able to add
# MainMenuEntry extension on existing page, only create new page with index extension
# through the wizard.
RICHIE_MAINMENUENTRY_ALLOW_CREATION = False

# Define which node level can be processed to search for MainMenuEntry extension. You
# can set it to 'None' for never processing any node.
# This is a limit against performance issues to avoid making querysets for nothing.
RICHIE_MAINMENUENTRY_MENU_ALLOWED_LEVEL = 0

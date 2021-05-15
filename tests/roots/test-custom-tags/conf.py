extensions = ["sphinxext.opengraph2"]

master_doc = "index"
exclude_patterns = ["_build"]

html_theme = "basic"

ogp_site_url = "http://example.org/"

ogp_custom_meta_tags = [
    '<meta property="og:ignore_canonical" content="true" />',
]

import io

from test_doubles.demo_fake import HtmlPageConverter


def test_convert_second_page():
    fake_file = io.StringIO("""\
page one
PAGE_BREAK
page two
PAGE_BREAK
page three
""")
    converter = HtmlPageConverter(fake_file)
    converted_text = converter.get_html_page(1)
    assert converted_text == "page two<br />"

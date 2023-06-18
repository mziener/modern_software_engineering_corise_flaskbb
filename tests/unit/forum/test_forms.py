import pytest
from flaskbb.forum.forms import SpecialTopicForm
from werkzeug.datastructures import MultiDict
pytestmark = pytest.mark.usefixtures("post_request_context", "default_settings")

###################################################################
# CoRise TODO: add unit tests below that test the functionality of
# the `SpecialTopicForm`

class TestSpecialTopicForm(object):
    
    def test_special_topic_title_starts_with_prefix(self):
        data = MultiDict({'title': 'My title', 'content': 'My Content', 'track_content': False})
        special_topic = SpecialTopicForm(data)
        assert special_topic.data['title'] == ("Special Topic: My title")

    def test_special_topic_content_starts_with_prefix(self):
        data = MultiDict({'title': 'My title', 'content': 'My content', 'track_content': False})
        special_topic = SpecialTopicForm(data)
        assert special_topic.data['content'] == ("Special Topic: My content")
    pass

###################################################################
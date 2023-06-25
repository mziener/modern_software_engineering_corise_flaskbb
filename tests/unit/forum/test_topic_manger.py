# CoRise TODO: add unit tests for topic manager

import pytest
from flaskbb.forum.topic_manager import TopicManager
from flaskbb.forum.models import Topic

class TestTopicManager(object):

    def test_delete(self, topic):
        tm = TopicManager([topic])

        modified_topics = tm.delete()
        assert modified_topics == 1

        assert Topic.query.filter_by(id=topic.id).first() == None

    def test_hide_unhide(self, topic, super_moderator_user):
        tm = TopicManager([topic])

        modified_topics = tm.hide(super_moderator_user)
        assert modified_topics == 1
        assert topic.hidden == True

        modified_topics = tm.unhide()

        assert modified_topics == 1
        assert topic.hidden == False

    def test_set_state_important(self, topic):
        tm = TopicManager([topic])
        modified_topics = tm.set_attribute("important", True)

        assert modified_topics == 1
        assert topic.important == True

    def test_set_state_locked(self, topic):
        tm = TopicManager([topic])
        modified_topics = tm.set_attribute("locked", True)

        assert modified_topics == 1
        assert topic.locked == True


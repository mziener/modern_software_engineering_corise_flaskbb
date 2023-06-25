# CoRise TODO: implement a class for managing topics with in a forum
class TopicManager(object):
    def __init__(self, topics) -> None:
        self.topics = topics
        
    def set_attribute(self, attr, v):
        modified_topics = 0
        for topic in self.topics:
            if getattr(topic, attr):
                continue
            setattr(topic, attr, v)
            modified_topics += 1
            topic.save()
        return modified_topics

    def hide(self, user):
        modified_topics = 0
        for topic in self.topics:
            if topic.hidden:
                continue
            topic.hide(user)
            topic.save()
            modified_topics += 1
        return modified_topics
    
    def unhide(self):
        modified_topics = 0
        for topic in self.topics:
            if not topic.hidden:
                continue
            modified_topics += 1
            topic.unhide()
        return modified_topics

    def delete(self): 
        modified_topics = 0
        for topic in self.topics:
            modified_topics += 1
            topic.delete()
        return modified_topics

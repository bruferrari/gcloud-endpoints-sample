from google.appengine.ext import ndb
from google.appengine.ext import endpoints
from endpoints_proto_datastore.ndb import EndpointsModel, EndpointsAliasProperty


class Entity(EndpointsModel):

    _message_fields_schema = ('name', 'register_dt', 'rating_avg', 'registered_by')

    name = ndb.StringProperty(required=True)
    register_dt = ndb.DateProperty(auto_now_add=True)
    rating_avg = ndb.FloatProperty(default=0.0)
    registered_by = ndb.UserProperty(required=True)

    def entity_set(self, value):
        # TODO: do some validation
        self._entity = value

    @EndpointsAliasProperty(setter=entity_set)
    def entity(self):
        if self.key is not None:
            return self._entity


def rating_validator(prop, value):
    if value > float(5.0):
        raise endpoints.BadRequestException(
            '{} must not be greater than 5.0'.format(prop._name))
    if value < float(0.0):
        raise endpoints.BadRequestException(
            '{} must not be negative'.format(prop._name))


class Evaluation(EndpointsModel):

    _message_fields_schema = ('user', 'entity', 'rating', 'date')

    user = ndb.UserProperty(required=True)
    entity = ndb.KeyProperty(kind=Entity, required=True)
    rating = ndb.FloatProperty(required=True, default=0.0, validator=rating_validator)
    date = ndb.DateTimeProperty(auto_now_add=True)

    def calculate_entity_rating_avg(self):
        pass

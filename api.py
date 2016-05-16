from google.appengine.ext import endpoints
from protorpc import remote
from models import Evaluation, Entity


@endpoints.api(
    name='evaluation',
    version='v1',
    description='API for evaluation of entities')
class EvaluationApi(remote.Service):
    @Evaluation.method(user_required=True,
                       request_fields=('entity', 'rating',),
                       name='evaluation.insert',
                       path='evaluation')
    def insert_evaluation(self, evaluation):
        evaluation.user = endpoints.get_current_user()
        evaluation.put()
        return evaluation

    @Evaluation.query_method(user_required=True,
                             query_fields=('limit', 'pageToken'),
                             name='evaluation.list',
                             path='evaluations')
    def list_evaluation(self, query):
        return query.filter(Evaluation.user == endpoints.get_current_user())

    @Evaluation.query_method(query_fields=('rating',),
                             user_required=True,
                             path='evaluation',
                             name='evaluation.get_by_rating')
    def evaluation_get(self, query):
        return query.filter(Evaluation.user == endpoints.get_current_user())


@endpoints.api(name='entity',
               version='v1',
               description='API for entities management')
class EntityApi(remote.Service):
    @Entity.method(user_required=True,
                   request_fields=('name',),
                   name='entity.insert',
                   path='entity')
    def insert_entity(self, entity):
        entity.registered_by = endpoints.get_current_user()
        if entity.from_datastore:
            raise endpoints.BadRequestException('Entity {} already exists.'.format(entity.name))
        entity.put()
        return entity

    @Entity.query_method(user_required=True,
                         query_fields=('limit', 'pageToken'),
                         name='entity.list_all',
                         path='all_entities')
    def list_all_entities(self, query):
        return query


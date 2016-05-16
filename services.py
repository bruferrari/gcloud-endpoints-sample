from google.appengine.ext import endpoints
from api import EvaluationApi, EntityApi


application = endpoints.api_server([EvaluationApi, EntityApi],
                                   restricted=False)

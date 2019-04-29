from aiohttpdemo_polls import settings
from aiohttpdemo_polls import views

STATIC_PATH = settings.PROJECT_ROOT / 'static'

def setup_routes(app):
    app.router.add_get('/', views.index)

    app.router.add_get(
        '/poll/{question_id}', views.poll, name='poll')
    app.router.add_get(
        '/poll/{question_id}/results', views.results, name='results')
    app.router.add_post(
        '/poll/{question_id}/vote',
        views.vote,
        name='vote')

    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static/', path=STATIC_PATH, name='static')

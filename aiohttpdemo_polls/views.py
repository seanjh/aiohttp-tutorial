import logging

import aiohttp_jinja2
from aiohttp import web

from aiohttpdemo_polls import db

log = logging.getLogger(__name__)


@aiohttp_jinja2.template('index.html')
async def index(request):
    async with request.app['db'].acquire() as conn:
        questions = await db.get_questions(conn)
    log.debug(f'Questions: {questions}')
    return {'questions': questions}


@aiohttp_jinja2.template('detail.html')
async def poll(request):
    async with request.app['db'].acquire() as conn:
        question_id = request.match_info['question_id']
        try:
            question, choices = await db.get_question(conn, question_id)
        except db.RecordNotFound as err:
            raise web.HTTPNotFound(text=str(e))
        return {
            'question': question,
            'choices': choices,
        }


async def results(request):
    pass


async def vote(request):
    pass

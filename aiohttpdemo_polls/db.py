import aiopg.sa

from aiohttpdemo_polls.models import question, choice


class RecordNotFound(Exception):
    """Requested record in database was not found"""


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )
    app['db'] = engine


async def close_pg(app):
    db = app['db']
    db.close()
    await db.wait_closed()


async def get_questions(conn, limit=None):
    stmt = question.select()
    if limit is not None:
        stmt = stmt.limit(limit)
    result = await conn.execute(stmt)
    return await result.fetchall()


async def get_question(conn, question_id):
    result = await conn.execute(
        question.select()
        .where(question.c.id == question_id))
    question_record = await result.first()
    if not question_record:
        msg = f'Question with id: {question_id} does not exist'
        raise RecordNotFound(msg)
    result = await conn.execute(
        choice.select()
        .where(choice.c.question_id == question_id)
        .order_by(choice.c.id))
    choice_records = await result.fetchall()
    return question_record, choice_records

from db.run_sql import run_sql
from models.biting import Biting
from repositories import human_repository, zombie_repository

def save(biting):
    zombie_id = biting.zombie.id
    human_id = biting.human.id
    sql = "INSERT INTO bitings (zombie_id, human_id) VALUES (%s, %s) RETURNING *"
    values = [zombie_id, human_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    biting.id = id
    return biting

def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)

def select_all():
    bitings = []
    sql = "SELECT * FROM bitings"
    results = run_sql(sql)
    for result in results:
        human = human_repository.select(result['human_id'])
        zombie = zombie_repository.select(result['zombie_id'])
        biting = Biting(human, zombie, result['id'])
        bitings.append(biting)
    return bitings

from db.run_sql import run_sql
from models.biting import Biting

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


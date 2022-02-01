#=================================
# database for emr
# author: Lily
# created: 2022.2.1
#=================================

from pathlib import Path
import json

from emr import INITIAL_DATA

dbfile = Path(__file__).parent.parent.joinpath('db.json')

def update_db(data):
    data_str = json.dumps(data, indent=4)
    dbfile.write_text(data_str)

def del_db():
    dbfile.unlink(missing_ok=True)

def init_db():
    update_db(INITIAL_DATA)

def load_db():
    if not dbfile.exists():
        init_db()
    data_str = dbfile.read_text()
    return json.loads(data_str)

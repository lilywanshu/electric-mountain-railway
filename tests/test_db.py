from emr.db import dbfile, load_db, update_db, del_db
from emr import INITIAL_DATA, TRAIN_SEAT

def test_del_db():
    del_db()
    assert not dbfile.exists()

def test_loaddb():
    data = load_db()
    print(data)
    assert data[0]['ticket'] == TRAIN_SEAT




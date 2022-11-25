from playhouse.db_url import connect
from peewee import Model
from peewee import IntegerField
from peewee import CharField
from peewee import DateTimeField


db = connect("sqlite:///peewee_db.sqlite")

if not db.connect():
    print("接続NG")
    exit()
print("接続OK")


class detected_count(Model):
    id = IntegerField()  # ID
    image_name = CharField()  # 画像の名前
    count = IntegerField()  # 検出結果の個数
    created_date = DateTimeField()  # 作成日時

    class Meta:
        database = db
        table_name = "detected_count"


db.create_tables([detected_count])

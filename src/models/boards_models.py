from tortoise import fields, models


class BoardModel(models.Model):
    id = fields.IntField(pk=True)
    board_name = fields.CharField(max_length=100)
    time_create = fields.DatetimeField(auto_now_add=True)
    time_change = fields.DatetimeField(auto_now=True)

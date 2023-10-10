from tortoise import fields, models

from models.boards_models import BoardModel

class NoteModel(models.Model):
    id = fields.IntField(pk=True)
    text_note = fields.TextField(null=False)
    time_create = fields.DatetimeField(auto_now_add=True)
    time_change = fields.DatetimeField(auto_now=True)
    board_id = fields.ForeignKeyField('models.BoardModel', on_delete=fields.CASCADE)

    def __str__(self):
        return self.text_note

    def get_change_time(self):
        return self.time_change

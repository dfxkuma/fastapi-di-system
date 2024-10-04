from tortoise import Model, fields


class Message(Model):
    id = fields.IntField(pk=True, generated=True)
    username = fields.CharField(max_length=100)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    __repr__ = (
        lambda self: f"<Message ID: {self.id}, Username: {self.username}, Content: {self.content}>"
    )

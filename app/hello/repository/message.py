from app.hello.entities.message import Message


class MessageRepository:

    @classmethod
    async def get(cls, *args, **kwargs) -> Message | None:
        return await Message.get(*args, **kwargs)

    @classmethod
    async def create(cls, *args, **kwargs) -> Message:
        return await Message.create(*args, **kwargs)

    @classmethod
    async def exists(cls, *args, **kwargs) -> bool:
        return await Message.exists(*args, **kwargs)

    @classmethod
    async def update(cls, entity_id: str, **kwargs) -> Message | None:
        await Message.filter(id=entity_id).update(**kwargs)
        return await Message.get(id=entity_id)

    async def write(self, username: str, message: str) -> Message:
        return await self.create(username=username, content=message)

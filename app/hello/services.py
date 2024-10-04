import tortoise

from app.hello.repository.message import MessageRepository


class HelloService:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    @staticmethod
    async def hello(name: str) -> str:
        return f"Hello, {name}!"

    async def write_message(self, username: str, message: str) -> str:
        created_entity = await self.repository.write(username, message)
        return f"Message ID {created_entity.id} has been created!"

    async def get_message(self, entity_id: str) -> str:
        if not entity_id:
            return "Message ID is required"
        if not await MessageRepository.exists(id=entity_id):
            return "Message Not Found"
        entity = await self.repository.get(id=entity_id)
        if not entity:
            return "Message Not Found"
        return f"Message Content: {entity.content}"

    async def get_all_messages(self) -> str:
        try:
            entities = await self.repository.get()
        except tortoise.exceptions.DoesNotExist:
            return "No messages found"
        return "\n".join([repr(entity) for entity in entities])

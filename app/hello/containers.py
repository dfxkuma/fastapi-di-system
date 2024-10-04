from dependency_injector import containers, providers

from app.hello.services import HelloService
from app.hello.repository.message import MessageRepository


class HelloContainer(containers.DeclarativeContainer):
    repository: MessageRepository = providers.Singleton(MessageRepository)
    service: HelloService = providers.Factory(HelloService, repository=repository)

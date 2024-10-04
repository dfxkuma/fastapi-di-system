from dependency_injector import containers, providers

from app.hello.containers import HelloContainer


class AppContainers(containers.DeclarativeContainer):
    hello: HelloContainer = providers.Container(HelloContainer)

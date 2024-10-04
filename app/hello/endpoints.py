from dependency_injector.wiring import inject, Provide

from fastapi import APIRouter, Depends
from fastapi_restful.api_model import APIMessage
from fastapi_restful.cbv import cbv

from app.hello.dto import hello_dto
from app.hello.services import HelloService
from app.containers import AppContainers

router = APIRouter(
    prefix="/hello",
    tags=["hello"],
    responses={404: {"description": "Not found"}},
)


@cbv(router)
class HelloEndpoint:

    @router.post("/say", response_model=APIMessage, description="Say a message")
    @inject
    async def say_hello(
        self,
        data: hello_dto.EnterNameDto,
        service: "HelloService" = Depends(Provide[AppContainers.hello.service]),
    ):
        return APIMessage(detail=str(await service.hello(data.name)))

    @router.post("/write", response_model=APIMessage, description="Write a message")
    @inject
    async def write_hello(
        self,
        data: hello_dto.WriteMessageDto,
        service: "HelloService" = Depends(Provide[AppContainers.hello.service]),
    ):
        return APIMessage(
            detail=str(await service.write_message(data.username, data.message))
        )

    @router.get("/get/{entity_id}", response_model=APIMessage, description="Get a message")
    @inject
    async def get_hello(
        self,
        entity_id: str,
        service: "HelloService" = Depends(Provide[AppContainers.hello.service]),
    ):
        return APIMessage(detail=str(await service.get_message(entity_id)))

    @router.get("/get", response_model=APIMessage, description="Get all messages")
    @inject
    async def get_all_hello(
        self,
        service: "HelloService" = Depends(Provide[AppContainers.hello.service]),
    ):
        return APIMessage(detail=str(await service.get_all_messages()))

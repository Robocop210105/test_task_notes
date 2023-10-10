import logging
from typing import List
from fastapi.responses import Response
from fastapi.routing import APIRouter
from tortoise.exceptions import DoesNotExist

from schemas import BoardSchemaRead, NoteSchemaRead
from models import BoardModel

logger = logging.getLogger("logging")
router = APIRouter()


@router.get(
    "/read_board",
    description="Reading board",
    response_model=BoardSchemaRead,
    responses={
        200: {
            "description": "Done",
        },
        204: {
            "description": "Object does not exist",
        },
        422: {
            "description": "Validation Error",
        },
        500: {
            "description": "Internal Server Error",
        },
    },
)
async def read_board(id_board: int):
    try:
        if isinstance(id_board, int):
            obj = await BoardModel.get(id=id_board)
            return BoardSchemaRead(
                name=obj.board_name,
                time_create=obj.time_create,
                time_change=obj.time_change,
                notes=[
                    NoteSchemaRead(
                        text=i.text_note,
                        time_create=i.time_create,
                        time_change=i.time_change,
                                    )
                    for i in await obj.notemodels.all()
                ]
            )
        else:
            raise ValueError
    except DoesNotExist:
        return Response(status_code=204)
    except ValueError:
        return Response(status_code=422)
    except BaseException as e:
        logger.error(f'Read board error --->{e}')
        return Response(status_code=500)


@router.get(
    "/read_all_boards",
    description="Reading all boards",
    response_model=List[BoardSchemaRead],
    responses={
        200: {
            "description": "Done",
        },
        204: {
            "description": "Object does not exist",
        },
        422: {
            "description": "Validation Error",
        },
        500: {
            "description": "Internal Server Error",
        },
    },
)
async def read_all_boards():
    try:
            return [BoardSchemaRead(
                name=obj.board_name,
                time_create=obj.time_create,
                time_change=obj.time_change,
                notes=[
                    NoteSchemaRead(
                        text=i.text_note,
                        time_create=i.time_create,
                        time_change=i.time_change,
                                    )
                    for i in await obj.notemodels.all()
                ]
            ) for obj in await BoardModel.all()]
    except DoesNotExist:
        return Response(status_code=204)
    except ValueError:
        return Response(status_code=422)
    except BaseException as e:
        logger.error(f'Read boards error --->{e}')
        return Response(status_code=500)

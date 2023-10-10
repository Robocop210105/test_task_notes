import logging
from typing import List
from fastapi.responses import Response
from fastapi.routing import APIRouter
from tortoise.exceptions import DoesNotExist

from schemas import NoteSchemaRead
from models import NoteModel

logger = logging.getLogger("logging")
router = APIRouter()


@router.get(
    "/read_notes",
    description="Reading note",
    response_model=NoteSchemaRead,
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
async def read_note(id_note: int):
    try:
        if isinstance(id_note, int):
            obj = await NoteModel.get(id=id_note)
            return NoteSchemaRead(
                text=obj.text_note,
                time_create=obj.time_create,
                time_change=obj.time_change,
            )
        else:
            raise ValueError
    except DoesNotExist:
        return Response(status_code=204)
    except ValueError:
        return Response(status_code=422)
    except BaseException as e:
        logger.error(f'Read note error ---> {e}')
        return Response(status_code=500)


@router.get(
    "/read_all_notes",
    description="Reading all notes",
    response_model=List[NoteSchemaRead],
    responses={
        200: {
            "description": "Done",
        },
        204: {
            "description": "Objects does not exist",
        },
        500: {
            "description": "Internal Server Error",
        },
    },
)
async def read_all_notes():
    try:
        return [NoteSchemaRead(
            text=i.text_note,
            time_create=i.time_create,
            time_change=i.time_change,
        ) for i in await NoteModel.all()]
    except DoesNotExist:
        return Response(status_code=204)
    except BaseException as e:
        logger.error(f'Read notes error ---> {e}')
        return Response(status_code=500)

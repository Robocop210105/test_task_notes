import logging
from fastapi.responses import Response
from fastapi.routing import APIRouter
from tortoise.exceptions import DoesNotExist

from schemas import NoteSchemaWrite
from models import NoteModel, BoardModel

logger = logging.getLogger("logging")
router = APIRouter()

@router.post(
    "/create_note",
    description="Creating note",
    responses={
        200: {
            "description": "Done",
        },
        204: {
            "description": "Object 'Board' does not exist",
        },
        500: {
            "description": "Internal Server Error",
        },

    },
)
async def create_note(note: NoteSchemaWrite):
    try:
        new_note = NoteModel(text_note=note.text,
                             board_id=await BoardModel.get(id=note.board_id)
                             )
        await new_note.save()
        return new_note.id
    except DoesNotExist:
        return Response(status_code=204)
    except BaseException as e:
        logger.error(f'Create note error ---> {e}')
        return Response(status_code=500)

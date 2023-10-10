import logging
from fastapi.responses import Response
from fastapi.routing import APIRouter
from tortoise.exceptions import DoesNotExist

from schemas import NoteSchemaWrite
from models import NoteModel

logger = logging.getLogger("logging")
router = APIRouter()


@router.patch(
    "/update_notes",
    description="Changing note",
    response_model=NoteSchemaWrite,
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
async def update_note(id_note: int, text_note: NoteSchemaWrite):
    try:
        if isinstance(id_note, int):
            note = await NoteModel.get(id=id_note)
            await note.update_from_dict({"text_note": text_note.text})
            await note.save()
            return Response(status_code=200)
        else:
            raise ValueError
    except DoesNotExist:
        return Response(status_code=204)
    except ValueError:
        return Response(status_code=422)
    except BaseException as e:
        logger.error(f'Update note error ---> {e}')
        return Response(status_code=500)

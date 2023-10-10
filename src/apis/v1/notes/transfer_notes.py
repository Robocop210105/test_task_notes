import logging
from fastapi.responses import Response
from fastapi.routing import APIRouter
from tortoise.exceptions import DoesNotExist

from models import NoteModel, BoardModel

logger = logging.getLogger("logging")
router = APIRouter()


@router.patch(
    "/transfer_notes",
    description="Moving a note to another board",
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
async def transfer_note(id_note: int, id_board: int):
    try:
        if isinstance(id_note, int):
            note = await NoteModel.get(id=id_note)
            await note.update_from_dict({"board_id": await BoardModel.get(id=id_board)})
            await note.save()
            return Response(status_code=200)
        else:
            raise ValueError
    except DoesNotExist:
        return Response(status_code=204)
    except ValueError:
        return Response(status_code=422)
    except BaseException as e:
        logger.error(f'Transfer note error ---> {e}')
        return Response(status_code=500)

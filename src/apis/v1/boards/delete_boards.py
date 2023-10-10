import logging
from fastapi.responses import Response
from fastapi.routing import APIRouter
from tortoise.exceptions import DoesNotExist

from models import BoardModel

logger = logging.getLogger("logging")
router = APIRouter()


@router.delete(
    "/delete_board",
    description="Deleting note",
    responses={
        200: {
            "description": "Done",
        },
        204: {
            "description": "object not created or deleted",
        },
        422: {
            "description": "Validation Error",
        },
        500: {
            "description": "Internal Server Error",
        },
    },
)
async def delete_board(id_board: int):
    try:
        if isinstance(id_board, int):
            await BoardModel.get(id=id_board).delete()
            return Response(status_code=200)
        else:
            raise ValueError
    except DoesNotExist:
        return Response(status_code=204)
    except ValueError:
        return Response(status_code=400)
    except BaseException as e:
        logger.error(f'Delete board error ---> {e}')
        return Response(status_code=500)

import logging
from fastapi.responses import Response
from fastapi.routing import APIRouter
from tortoise.exceptions import DoesNotExist

from schemas import BoardSchemaWrite
from models import BoardModel

logger = logging.getLogger("logging")
router = APIRouter()

@router.patch(
    "/update_board",
    description="Changing board",
    responses={
        200: {
            "description": "Done",
        },
        204: {
            "description": "Object 'Board' does not exist",
        },
        422: {
            "description": "Validation Error",
        },
        500: {
            "description": "Internal Server Error",
        },
    },
)
async def update_board(id_board: int, name_board: BoardSchemaWrite):
    try:
        if isinstance(id_board, int):
            board = await BoardModel.get(id=id_board)
            await board.update_from_dict({"board_name": name_board.name})
            await board.save()
            return Response(status_code=200)
        else:
            raise ValueError
    except DoesNotExist:
        return Response(status_code=204)
    except ValueError:
        return Response(status_code=422)
    except BaseException as e:
        logger.error(f'Update board error ---> {e}')
        return Response(status_code=500)

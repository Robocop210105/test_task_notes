import logging
from fastapi.responses import Response
from fastapi.routing import APIRouter

from schemas import BoardSchemaWrite
from models import BoardModel

logger = logging.getLogger("logging")
router = APIRouter()


@router.post(
    "/create_board",
    description="Creating board",
    responses={
        200: {
            "description": "Done",
        },
        500: {
            "description": "Internal Server Error",
        },

    },
)
async def create_board(board: BoardSchemaWrite):
    try:
        new_board = BoardModel(board_name=board.name)
        await new_board.save()
        return new_board.id
    except BaseException as e:
        logger.error(f'Create board error ---> {e}')
        return Response(status_code=500)

from apis.v1 import notes, boards

from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(boards.create_boards.router, prefix="/boards", tags=["boards"])
api_router.include_router(boards.delete_boards.router, prefix="/boards", tags=["boards"])
api_router.include_router(boards.read_boards.router, prefix="/boards", tags=["boards"])
api_router.include_router(boards.update_boards.router, prefix="/boards", tags=["boards"])

api_router.include_router(notes.create_notes.router, prefix="/notes", tags=["notes"])
api_router.include_router(notes.update_notes.router, prefix="/notes", tags=["notes"])
api_router.include_router(notes.read_notes.router, prefix="/notes", tags=["notes"])
api_router.include_router(notes.delete_notes.router, prefix="/notes", tags=["notes"])
api_router.include_router(notes.transfer_notes.router, prefix="/notes", tags=["notes"])

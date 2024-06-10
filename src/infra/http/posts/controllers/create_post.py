from fastapi import APIRouter

from src.domain.usecases.create_post import CreatePostUseCase
from src.infra.ai.crew import crew
from src.infra.http.posts.dtos.create_post import CreatePostRequest

router = APIRouter(prefix='/posts', tags=['Posts'])


@router.post(path='/')
def handler(body: CreatePostRequest):
    print(body.topic)
    usecase = CreatePostUseCase(crew)
    return 'teste'

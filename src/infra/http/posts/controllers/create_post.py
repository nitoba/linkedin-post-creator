from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.domain.usecases.create_post import CreatePostUseCase
from src.infra.ai.crew import crew
from src.infra.http.posts.dtos.create_post import CreatePostRequest

router = APIRouter(prefix='/posts', tags=['Posts'])


@router.post(path='/')
def handler(body: CreatePostRequest):
    usecase = CreatePostUseCase(crew)
    response = usecase.execute(body.topic)
    print(response)
    return JSONResponse({'data': response})

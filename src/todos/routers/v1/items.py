import fastapi

router = fastapi.APIRouter()


@router.get('/')
def search():
    return {'data': []}

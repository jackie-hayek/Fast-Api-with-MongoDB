from fastapi import APIRouter, status, HTTPException

from containers import Container
from exceptions.exceptions import Exceptions
from models.student_model import Student as StudentsModel, UpdateStudentModel
import logging

router = APIRouter()

logging.basicConfig(level=logging.DEBUG)

student_service = Container.student_service()


@router.post("/student()", response_model=StudentsModel, status_code=status.HTTP_201_CREATED)
async def add_student(student: StudentsModel):
    return await student_service.add_student(student)


@router.get("/student()", response_model=list[StudentsModel], status_code=200)
async def get_students():
    return await student_service.get_students()


@router.get("/student/{student_id}", status_code=status.HTTP_200_OK)
async def get_student_by_id(student_id: str):
    try:
        return await student_service.get_student_by_id(student_id)
    except Exceptions as e:
        raise HTTPException(status_code=404, detail=e.__str__())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.delete("/student/{student_id}", status_code=status.HTTP_200_OK)
async def delete_student_by_id(student_id: str):
    try:
        return await student_service.delete_student_by_id(student_id)
    except Exceptions as e:
        raise HTTPException(status_code=404, detail=e.__str__())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.put("/student/{student_id}", response_model=UpdateStudentModel, status_code=status.HTTP_200_OK)
async def update_student(student_id: str, studentx: UpdateStudentModel):
    try:
        return await student_service.update_student(student_id, studentx.dict())
    except Exceptions as e:
        raise HTTPException(status_code=404, detail=e.__str__())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=e.__str__())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())
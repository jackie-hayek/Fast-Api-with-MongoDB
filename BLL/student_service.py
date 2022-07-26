import logging

from BLL.abstract_student_service import AbstractStudentService
from DAL.abstract_student_repository import AbstractStudentRepository
from models.student_model import Student as StudentsModel


class StudentService(AbstractStudentService):

    def __init__(self, student_repository: AbstractStudentRepository):
        self.student_repository = student_repository

    def add_student(self, student: StudentsModel):
        new_student = self.student_repository.add_new_student(student)
        logging.info('Student added to the list')
        return new_student

    def get_students(self):
        try:
            return self.student_repository.get_students()
            logging.info('Students list returned')

        except Exception as e:
            logging.info('No Students List available')
            raise e

    def get_student_by_id(self, student_id: str):
        try:
            return self.student_repository.get_student_by_id(student_id)
            logging.info('Student with the specified id is returned')
        except Exception as e:
            logging.error('Student with the specified id is not found')
            raise e

    def delete_student_by_id(self, id: str):
        try:
            deleted_student = self.student_repository.delete_student_by_id(id)
            return deleted_student
            logging.info('Student deleted')

        except Exceptions as e:
            logging.error('Student not found')
            raise e

        except Exception as e:
            raise e

    def update_student(self, id: str, student: StudentsModel):
        try:
            updated_student = self.student_repository.update_student_data(id, student)
            logging.info('Student data updated')
            return updated_student

        except ValueError as e:
            raise e

        except Exception as e:
            logging.error('Student not found')
            raise e

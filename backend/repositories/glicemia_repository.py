from config import db
from models.glicemia import Glicemia
from datetime import datetime

class GlycemiaRepository:
    @staticmethod
    def create_record(user_id, value, notes=None):
        new_record = Glicemia(user_id=user_id, value=value, notes=notes)
        db.session.add(new_record)
        db.session.commit()
        return new_record

    @staticmethod
    def get_record_by_id(record_id, user_id):
        return db.session.execute(
            db.select(Glicemia).filter_by(id=record_id, user_id=user_id)
        ).scalar_one_or_none()

    @staticmethod
    def get_all_records_by_user(user_id):
        return db.session.execute(
            db.select(Glicemia).filter_by(user_id=user_id).order_by(Glicemia.timestamp.desc())
        ).scalars().all()

    @staticmethod
    def update_record(record_id, user_id, value=None, notes=None):
        record = GlycemiaRepository.get_record_by_id(record_id, user_id)
        if record:
            if value is not None:
                record.value = value
            if notes is not None:
                record.notes = notes
            db.session.commit()
            return record
        return None

    @staticmethod
    def delete_record(record_id, user_id):
        record = GlycemiaRepository.get_record_by_id(record_id, user_id)
        if record:
            db.session.delete(record)
            db.session.commit()
            return True
        return False

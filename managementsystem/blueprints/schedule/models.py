from sqlalchemy import func

from managementsystem.app import db



class Date(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    date = db.Column(
        db.String(10), # Should be different - Date/Time
        default = func.current_date()
    )

    is_holiday = db.Column(
        db.Boolean,
        default = False
    )


class ShiftLog(db.Model):
    
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # ShiftHours ID
    shift_id = db.Column(
        db.Integer,
        nullable = False
    )

    # Person ID
    person_id = db.Column(
        db.Integer,
        nullable = False
    )

    # Date ID
    date_id = db.Column(
        db.Integer,
        nullable = False
    )

    hours_worked = db.Column(
        db.Numeric
    )


class ShiftHours(db.Model):

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    # Shift start time
    start_time = db.Column(
        db.String(10) # Temporary, change!
    )

    # Shift end time
    end_time = db.Column(
        db.String(10) # Temporary, change!
    )

    duration = db.Column(
        db.Numeric
    )

    pass
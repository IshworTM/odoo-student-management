from odoo import fields, models


class StudentReport(models.Model):
    _name = "student.report"
    _description = "A student academic report module"

    student_name = fields.Char(
        string="Student's Name",
        required=True
    )

    maths = fields.Float(
        string="Maths"
    )
    science = fields.Float(
        string="Science"
    )
    english = fields.Float(
        string="English"
    )
    nepali = fields.Float(
        string = "Nepali"
    )
    computer = fields.Float(
        string="Computer"
    )
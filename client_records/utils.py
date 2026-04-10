import os
from openpyxl import Workbook
from django.conf import settings
from .models import HCTRecord, LSERecord


def export_hct_records_to_excel():
    file_path = os.path.join(settings.BASE_DIR, 'hct_records_auto.xlsx')

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "HCT Records"

    headers = ["Name", "Surname", "Date of Birth", "Sex", "Result", "TB Tested", "Counselor", "Date Created"]
    worksheet.append(headers)

    records = HCTRecord.objects.all()

    for record in records:
        worksheet.append([
            record.name,
            record.surname,
            str(record.date_of_birth),
            record.sex,
            record.result,
            record.tb_tested,
            record.counselor.username,
            record.date_created.strftime("%Y-%m-%d %H:%M:%S"),
        ])

    workbook.save(file_path)

    print("HCT Excel file created at:", file_path)


def export_lse_records_to_excel():
    file_path = os.path.join(settings.BASE_DIR, 'lse_records_auto.xlsx')

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "LSE Records"

    headers = ["Name", "Surname", "Date of Birth", "Grade", "Sex", "Club Type", "Counselor", "Date Created"]
    worksheet.append(headers)

    records = LSERecord.objects.all()

    for record in records:
        worksheet.append([
            record.name,
            record.surname,
            str(record.date_of_birth),
            record.grade,
            record.sex,
            record.club_type,
            record.counselor.username,
            record.date_created.strftime("%Y-%m-%d %H:%M:%S"),
        ])

    workbook.save(file_path)

    print("LSE Excel file created at:", file_path)
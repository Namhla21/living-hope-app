from django.contrib import admin
from django.http import HttpResponse
from openpyxl import Workbook
from .models import LSERecord, HCTRecord


def export_lse_to_excel(modeladmin, request, queryset):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "LSE Records"

    headers = ["Name", "Surname", "Date of Birth", "Grade", "Sex", "Club Type", "Counselor", "Date Created"]
    worksheet.append(headers)

    for record in queryset:
        worksheet.append([
            record.name,
            record.surname,
            record.date_of_birth.strftime("%Y-%m-%d"),
            record.grade,
            record.sex,
            record.club_type,
            record.counselor.username,
            record.date_created.strftime("%Y-%m-%d %H:%M:%S"),
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="lse_records.xlsx"'
    workbook.save(response)
    return response

export_lse_to_excel.short_description = "Export selected LSE records to Excel"


def export_hct_to_excel(modeladmin, request, queryset):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "HCT Records"

    headers = ["Name", "Surname", "Date of Birth", "Sex", "Result", "TB Tested", "Counselor", "Date Created"]
    worksheet.append(headers)

    for record in queryset:
        worksheet.append([
            record.name,
            record.surname,
            record.date_of_birth.strftime("%Y-%m-%d"),
            record.sex,
            record.result,
            record.tb_tested,
            record.counselor.username,
            record.date_created.strftime("%Y-%m-%d %H:%M:%S"),
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="hct_records.xlsx"'
    workbook.save(response)
    return response

export_hct_to_excel.short_description = "Export selected HCT records to Excel"


@admin.register(LSERecord)
class LSERecordAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "grade", "sex", "club_type", "counselor", "date_created")
    actions = [export_lse_to_excel]


@admin.register(HCTRecord)
class HCTRecordAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "sex", "result", "tb_tested", "counselor", "date_created")
    actions = [export_hct_to_excel]
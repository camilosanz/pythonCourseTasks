from src.helpers.csv_processor import get_filename_and_path, read_csv_file


def test_get_file_name_and_path():
    result = get_filename_and_path()
    first = [
        'meetingAttendanceReport.csv',
        'C:\\Users\\USUARIO\\Desktop\\DevOpsBootcamp\\Python_introduction\\' +
        'pythonCourseTasks\\week3\\Day1\\teams_attendance_app\\' +
        'attendance_reports\\04252022'
    ]

    assert result[0] == first


def test_read_csv_file():
    result = read_csv_file()
    control_params = [
        'meeting title',
        'total number of participants',
        'meeting start time',
        'meeting end time',
        'meeting id'
    ]

    for param in control_params:
        assert param in result[0]

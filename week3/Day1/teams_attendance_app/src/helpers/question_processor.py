
from utils import date_format_out, date_format_in


def user_question_selection():
    user_input = {
        'question':'',
        'question_type': '',
        'meeting_title': '**{meeting_name}**',
        'start_date': '**{start_date}**',
        'end_date': '**{end_date}**'
    }

    questions = {
        'participants':(f'- What is the number of Partipants attending {user_input["meeting_title"]} Meeting per date, date filter between {user_input["start_date"]} and {user_input["end_date"]}'),
        'duration':(f'- What is duration of {user_input["meeting_title"]} Meeting per date, date filter between {user_input["start_date"]} and {user_input["end_date"]}')
    }


    for q in questions:
        print(questions[q])
    
    
    user_input['question_type'] = input('\nSelect your question (enter "participants" or "duration"): ')
    user_input['meeting_title'] = input('\nEnter meeting name: ')
    user_input['start_date'] = date_format_in(input('\nEnter start date (mm/dd/yyyy): '))
    user_input['end_date'] = date_format_in(input('\nEnter end date (mm/dd/yyyy): '))
    user_input['question'] = questions[user_input['question_type']]

    return user_input

def answer_processor(answer, params):
    questions = {
        'participants':(f'- What is the number of Partipants attending {params["meeting_title"]} Meeting per date, date filter between {date_format_out(params["start_date"])} and {date_format_out(params["end_date"])}'),
        'duration':(f'- What is duration of {params["meeting_title"]} Meeting per date, date filter between {date_format_out(params["start_date"])} and {date_format_out(params["end_date"])}')
    }
    print(f"\n{questions[params['question_type']]}\n\n```json\n{answer}")

## app entry point
import csv

from helpers.question_processor import  user_question_selection, answer_processor
from helpers.json_processor import  generate_answer_json


def main():
    params = user_question_selection()
    answer = generate_answer_json(params['question_type'], params['meeting_title'], params['start_date'], params['end_date'])
    answer_processor(answer, params)

main()
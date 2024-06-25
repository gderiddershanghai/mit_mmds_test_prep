import numpy as np
from src.mpc_questions_graphs import COURSE_MPC_QUESTIONS
from src.transcript_questions import TRANSCRIPT_MPC_QUESTIONS
from src.knowledge_check_questions import KC_MPC_QUESTIONS
from src.additional_reading_questions import READING_MPC_QUESTIONS
from src.open_questions_graphs import OPEN_QUESTIONS
from src.chart_math_questions import IMAGE_QUESTIONS

#====================TOKEN===================
class Token():
    def __init__(self, STATE="final"):
        self.STATE = STATE
        self.mpc_questions = []
        self.picture_questions = None
        self.islr_questions = None
        # self.image = None

    def initialize_mpc_questions(self):
        self.STATE = 'mpc'
        review_questions = COURSE_MPC_QUESTIONS 
        list_length = len(review_questions)
        mpc_idxs = np.random.choice(range(list_length), size=4, replace=False)
        print('______________________________________________')
        print('mpc_idxs: ',mpc_idxs, type(mpc_idxs))
        print('______________________________________________')
        for idx in mpc_idxs:
            self.mpc_questions.append(review_questions[idx])

    # def initialize_transcript_questions(self):
    #     self.STATE = 'transcript'
    #     review_questions = TRANSCRIPT_MPC_QUESTIONS
    #     list_length = len(review_questions)
    #     mpc_idxs = np.random.choice(range(list_length), size=4, replace=False)
    #     print('______________________________________________')
    #     print('mpc_idxs: ',mpc_idxs, type(mpc_idxs))
    #     print('______________________________________________')
    #     for idx in mpc_idxs:
    #         self.mpc_questions.append(review_questions[idx])

    # def initialize_reading_questions(self):
    #     self.STATE = 'reading'
    #     review_questions = READING_MPC_QUESTIONS
    #     list_length = len(review_questions)
    #     mpc_idxs = np.random.choice(range(list_length), size=4, replace=False)
    #     print('______________________________________________')
    #     print('mpc_idxs: ',mpc_idxs, type(mpc_idxs))
    #     print('______________________________________________')
    #     for idx in mpc_idxs:
    #         self.mpc_questions.append(review_questions[idx])

    def initialize_open_questions(self):
        self.STATE = 'open'
        review_questions = OPEN_QUESTIONS
        list_length = len(review_questions)
        open_idxs = np.random.choice(range(list_length), size=3, replace=False)
        # print('______________________________________________')
        # print('mpc_idxs: ',mpc_idxs, type(mpc_idxs))
        # print('______________________________________________')
        for idx in open_idxs:
            self.mpc_questions.append(review_questions[idx])

    # def initialize_image_questions(self):
    #     self.STATE = 'chart'
    #     review_questions = IMAGE_QUESTIONS
    #     list_length = len(review_questions)
    #     open_idxs = np.random.choice(range(list_length), size=2, replace=False)
    #     # print('______________________________________________')
    #     # print('mpc_idxs: ',mpc_idxs, type(mpc_idxs))
    #     # print('______________________________________________')
    #     for idx in open_idxs:
    #         # print(review_questions[idx])
    #         self.mpc_questions.append(review_questions[idx])

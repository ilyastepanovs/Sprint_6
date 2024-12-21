import allure
import pytest
from sprint_6_tests.data import Questions


class TestMainPage:

    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном».')
    @pytest.mark.parametrize(
        "num, expected_result",
        [
            (0, Questions.QUESTION_1),
            (1, Questions.QUESTION_2),
            (2, Questions.QUESTION_3),
            (3, Questions.QUESTION_4),
            (4, Questions.QUESTION_5),
            (5, Questions.QUESTION_6),
            (6, Questions.QUESTION_7),
            (7, Questions.QUESTION_8)
        ]
    )
    def test_questions(self, main_page, num, expected_result):
        assert expected_result == main_page.click_question_and_get_answer_text(num)

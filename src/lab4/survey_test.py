import unittest
from survey import Respondent, group_respondents


class TestQuest(unittest.TestCase):

    def test_group_respondents(self):
        respondents = [
            Respondent("John Doe", 25),
            Respondent("Jane Smith", 35),
            Respondent("Mike Johnson", 45),
            Respondent("Emily Brown", 55),
            Respondent("David Wilson", 65)
        ]
        age_groups = [(18, 30), (31, 50), (51, 70)]
        expected_result = [
            "51-70: David Wilson (65), Emily Brown (55)",
            "31-50: Mike Johnson (45), Jane Smith (35)",
            "18-30: John Doe (25)"
        ]
        self.assertEqual(group_respondents(
            respondents, age_groups), expected_result)


if __name__ == 'main':
    unittest.main()
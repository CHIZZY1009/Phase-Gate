from unittest import TestCase

from student_grade import collect_scores

class StudentGrade(TestCase):

     def testThatScores_AndSubjects_AreCollected_AndStored_ToTheRigth_PersonsName(self):

        scores = {"Class A":{"chizzy": {"Maths": 80 }}}

        self.assertEqual(len(scores), 1)
        self.assertEqual(len(scores["Class A"]), 1)
        self.assertEqual(scores["Class A"]["chizzy"]["Maths"], 80)

     def testThatAverage_AndTotalAreAccurately_MatchedTo_TheUser(self):

    
        results = {"Class A": {"chizzy": {"Total": 80, "Average": 80.0}}}

        self.assertEqual(len(results),1)
        self.assertEqual(len(results["Class A"]),1)
        self.assertEqual(results["Class A"]["chizzy"]["Total"],80)
        self.assertEqual(results["Class A"]["chizzy"]["Average"], 80.0)

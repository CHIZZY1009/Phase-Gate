from unittesxt import TestCase

from parking_slot import parking_slot_choice

class ParkingSlotTest(TestCase):


    def TestThatWhenUser_ChosesASlotItShows_OneAtTheIndex(self):

        actual = parking_slot_choice('2')

        expected = parking_space[index] = '1'

        self.assertEqual(actual, expected)

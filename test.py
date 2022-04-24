import unittest
from students_np import Solution


def has_duplicates(thelist):
  seen = set()
  for x in thelist:
    if x in seen:
      return x
    seen.add(x)
  return False

class TestGenerateSolution(unittest.TestCase):

    def test_correct_length_of_solution(self):
        for seed in range(100):
          s = Solution(seed)
          res = s.generate_soltn()

          self.assertEqual(len(res), s.avail_spots, "Failed with seed: {}".format(seed))

    def test_same_student_not_paired_with_itself(self):
      for seed in range(100):
        s = Solution(seed)
        res = s.generate_soltn()

        for pair in res:
          self.assertNotEqual(pair[0], pair[1], "A student was paired with themself. Random seed: {}".format(seed))

    def test_no_duplicate_students(self):
      for seed in range(100):
        s = Solution(seed)
        res = s.generate_soltn()

        flattened_res = [item for sublist in res for item in sublist]

        dups = has_duplicates(flattened_res)
        self.assertFalse(dups, "Result list has a duplicate. Random seed: {}".format(seed))

    def test_no_excluded_tuples_in_solution(self):
      for seed in range(100):
        s = Solution(seed)
        res = s.generate_soltn()

        exclusions = s.get_exclusions()

        for pair in res:
          self.assertNotIn(pair, exclusions, "An excluded pair was included in the solution. Random seed: {}".format(seed))



if __name__ == '__main__':
  unittest.main()
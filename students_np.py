import random
import itertools
import sys

"""
students = Range[400]

spots = 100

inc = 20;
inclist = RandomInteger[{1, 400}, {inc, 2}]

solutionlist = {};

For[i = 1, i < inc, i++,

For[j = 1, j < Length[students], j++,

    If[inclist[[i]][[2]] != students[[j]],

      AppendTo[solutionlist, {inclist[[i]][[1]], students[[j]]}];
      students = Delete[students, j];
      j = Length[students];

      ];

    ];

  ];

For[i = Length[solutionlist], i < spots/2, i = i + 2,
  AppendTo[solutionlist, {students[[i]], students[[i + 1]]}]]; 
"""

class Solution():
    NUM_STUDENTS = 400
    AVAIL_SPOTS = 100

    def __init__(self, random_seed):
        self.random_seed = random_seed
        self.students = list(range(self.NUM_STUDENTS))
        self.exclusions = random.sample(
            list(itertools.product(range(self.NUM_STUDENTS), repeat=2)), 20)

    @property
    def avail_spots(self):
      return self.AVAIL_SPOTS

    def generate_soltn(self):
        random.seed(self.random_seed)

        solution = []

        for i in range(0, len(self.exclusions)):
            templength=len(self.students)
            for j in range(0, templength):
                if (self.exclusions[i][1] != self.students[j]):
                    solution.append((self.exclusions[i][0], self.students[j]))
                    try:
                      self.students.remove(self.students[j])
                      self.students.remove(self.exclusions[i][0])
                    except:
                      pass
                    break

        idx = len(solution)
        while (len(solution) < self.AVAIL_SPOTS):
          solution.append((self.students[idx], self.students[idx + 1]))
          idx += 2

        return solution

if __name__ == '__main__':

  if len(sys.argv) < 2:
    print("Usage: python students_np.py [RANDOM_SEED]")
    sys.exit(1)

  s = Solution(sys.argv[1])
  res = s.generate_soltn()

  print(res)


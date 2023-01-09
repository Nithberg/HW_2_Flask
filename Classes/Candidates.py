import json


class Candidates:
    def __init__(self, path):
        with open(path, "r", encoding="utf-8") as file:
            self.path = json.load(file)

    def get_all_candidates(self):
        return self.path

    def get_candidate(self, uid):
        for candidate in self.path:
            if uid == candidate["id"]:
                return {
                    'name': candidate['name'],
                    'position': candidate['position'],
                    'skills': candidate['skills']
                }
        return {'not_found': 'Профиль не найден!'}

    def get_search(self, candidate_name):
        return [candidate for candidate in self.path if candidate_name.lower() in candidate['name'].lower()]

    def get_skills(self, skill):
        return [candidate for candidate in self.path if skill.lower() in candidate['skills'].lower().split(', ')]

# DATA = "../candidates.json"
#
# candidates = Candidates(DATA)
#
# print(candidates.get_skills('go'))

from flask import Flask, render_template
from Classes.Candidates import Candidates

app = Flask(__name__)
DATA = "candidates.json"
candidates = Candidates(DATA)


@app.route('/')
def candidate_lists():  # put application's code here
    candidate_names = candidates.get_all_candidates()
    return render_template('lists.html', candidate_names=candidate_names)


@app.route('/candidate/<int:uid>')
def profile(uid):
    candidate = candidates.get_candidate(uid)
    return render_template('profile.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search(candidate_name):
    candidate_searched = candidates.get_search(candidate_name)
    return render_template('search.html', candidate_searched=candidate_searched,
                           candidate_searched_len=len(candidate_searched))


@app.route('/skill/<skill>')
def skills(skill):
    candidates_skills = candidates.get_skills(skill)
    return render_template('skill.html', candidates_skills=candidates_skills,
                           candidates_skills_len=len(candidates_skills))


if __name__ == '__main__':
    app.run()

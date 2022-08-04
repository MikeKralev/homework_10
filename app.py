from flask import Flask

from utils import get_all, get_by_pk, get_by_skill


app = Flask(__name__)


@app.route('/')
def page_main():
    """Main page"""
    return f"<pre>{get_all()}</pre>"


@app.route('/candidates/<int:pk>')
def page_candidates(pk):
    """Candidate by pk page"""
    candidate_by_pk = get_by_pk(pk)
    return f"{candidate_by_pk['photo']}<pre>{candidate_by_pk['info']}</pre>"


@app.route('/skills/<skill>')
def page_skills(skill):
    """Candidates by skill page"""
    return f"<pre>{get_by_skill(skill)}</pre>"


if __name__ == "__main__":
    app.run()

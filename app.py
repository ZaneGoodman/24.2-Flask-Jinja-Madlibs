from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)


PROMPTS = [
    'place', 'noun', 'verb', 'adjective', 'plural_noun'
]

@app.route('/')
def home_form():
    prompts = PROMPTS
    return render_template('madlib_form.html', prompts=prompts)

@app.route('/story')
def make_story():
    words = request.args.getlist('prompt')
    markup = Story(words, """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
    story = markup.generate({PROMPTS[i]:words[i] for i in range(len(words))})
    
    return render_template('make_story.html', words=words, story=story)
from flask import Flask
import random
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/hello')

def hello():
   
   page = """
      <h1>Here's a random number: {0}</h1>
      <form>
         <button>New Number 1-25</button>
      </form>
      <a href="/live">Live</a>
   """
   num = random.randint(1, 25)
   return page.format(num)

@app.route('/live')
def live():
   some = """
   <a href="/hello">Hello</a>
   """
   return some
if __name__ == '__main__':
   app.run()
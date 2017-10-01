import spotipy
import spotipy.util as sp_util
import json

import .ml_engine

from flask import Flask, request, g, config
app = Flask(__name__)


with app.app_context():
  @app.route('/')
  def hello():
      return "Hello World!"

  @app.route('/login')
  def login():
      user_id = "primsu" # request.args.get('user_id')

      scope = 'user-library-read'
      app.config['token'] = sp_util.prompt_for_user_token(user_id, scope)
      if not app.config['token']:
          raise ValueError('Could not authenticate user')
      app.config['sp'] = spotipy.Spotify(auth=app.config['token'])
      return "user successfully authenticated"

  @app.route('/artists')
  def search_artists():
      query = request.args.get('query')
      return json.dumps(app.config.get_namespace('sp')[''].search(q='artist:' + query, type='artist'))

  @app.route('/albums')
  def search_albums():
      query = request.args.get('query')
      return json.dumps(app.config.get_namespace('sp')[''].search(q='album:' + query, type='album'))

  @app.route('/artist_ranking')
  def get_artist_ranking():
      query = request.args.get('query')
      return json.dumps(app.config.get_namespace('sp')[''].search(q='artist:' + query, type='artist'))



if __name__ == '__main__':
    app.run()

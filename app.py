from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample playlists data (you would typically use a database)
playlists = [
    {"id": 1, "name": "My Favorites", "tracks": ["Song A", "Song B"]},
    {"id": 2, "name": "Workout Mix", "tracks": ["Song C", "Song D"]},
]

# Function to create a new playlist
@app.route('/create_playlist', methods=['POST'])

def create_playlist(playlist_name):
    global playlists
    new_playlist = {"id": len(playlists) + 1, "name": playlist_name, "tracks": []}
    playlists.append(new_playlist)

# Function to add a song to a playlist
def add_song_to_playlist(playlist_id, song_name):
    global playlists
    playlist = next((p for p in playlists if p["id"] == playlist_id), None)
    if playlist:
        playlist["tracks"].append(song_name)

# Function to edit a playlist (name and tracks)
def edit_playlist(playlist_id, new_name):
    global playlists
    playlist = next((p for p in playlists if p["id"] == playlist_id), None)
    if playlist:
        playlist["name"] = new_name

# Function to delete a playlist
def delete_playlist(playlist_id):
    global playlists
    playlists = [p for p in playlists if p["id"] != playlist_id]

# Render the playlist management page
@app.route('/')
def index():
    return render_template('playlists.html', playlists=playlists)

# Handle form submission for creating a new playlist
@app.route('/create_playlist', methods=['POST'])
def create_playlist_route():
    playlist_name = request.form['playlistName']
    create_playlist(playlist_name)
    return redirect(url_for('index'))

# Handle form submission for adding a song to a playlist
@app.route('/add_song_to_playlist', methods=['POST'])
def add_song_to_playlist_route():
    playlist_id = int(request.form['playlistId'])
    song_name = request.form['songName']
    add_song_to_playlist(playlist_id, song_name)
    return redirect(url_for('index'))

# Handle form submission for editing a playlist
@app.route('/edit_playlist', methods=['POST'])
def edit_playlist_route():
    playlist_id = int(request.form['playlistId'])
    new_name = request.form['newName']
    edit_playlist(playlist_id, new_name)
    return redirect(url_for('index'))

# Handle form submission for deleting a playlist
@app.route('/delete_playlist', methods=['POST'])
def delete_playlist_route():
    playlist_id = int(request.form['playlistId'])
    delete_playlist(playlist_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

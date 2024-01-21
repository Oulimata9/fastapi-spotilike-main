from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from typing import List

from fastapi_spotilike_main import crud, database
from fastapi_spotilike_main import models

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# OAuth2PasswordBearer is a class that will help FastAPI recognize the login route.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Modèles
class Album(BaseModel):
    titre: str
    pochette: str
    date_de_sortie: str
    morceaux: List[int]
    artiste: int

class Morceau(BaseModel):
    titre: str
    duree: str
    artiste: int
    genre: List[str]
    album: int

class Artiste(BaseModel):
    nom_artiste: str
    avatar: str
    biographie: str

class Genre(BaseModel):
    titre: str
    description: str

class Utilisateur(BaseModel):
    nom_utilisateur: str
    mot_de_passe: str
    email: str

# Endpoints

# 1. GET - /api/albums : Récupère la liste de tous les albums
@app.get("/api/albums", response_model=List[models.Album])
async def get_all_albums(db: Session = Depends(get_db)):
    return crud.get_albums(db)

# 2. GET - /api/albums/{id} : Récupère les détails de l’album précisé par {id}
@app.get("/api/albums/{album_id}", response_model=models.Album)
async def get_album(album_id: int, db: Session = Depends(get_db)):
    return crud.get_album(db, album_id)

# 3. GET - /api/albums/{id}/songs : Récupère les morceaux de l’album précisé par {id}
@app.get("/api/albums/{album_id}/songs", response_model=List[models.Morceau])
async def get_album_songs(album_id: int, db: Session = Depends(get_db)):
    return crud.get_album_songs(db, album_id)

# 4. GET - /api/genres : Récupère la liste de tous les genres
@app.get("/api/genres", response_model=List[models.Genre])
async def get_all_genres(db: Session = Depends(get_db)):
    return crud.get_genres(db)

# 5. GET - /api/artists/{id}/songs : Récupère la liste de tous les morceaux de l’artiste précisé par {id}
@app.get("/api/artists/{artist_id}/songs", response_model=List[models.Morceau])
async def get_artist_songs(artist_id: int, db: Session = Depends(get_db)):
    return crud.get_artist_songs(db, artist_id)

# 6. POST - /api/users/signin : Ajout d’un utilisateur
@app.post("/api/users/signin", response_model=models.Utilisateur)
async def create_user(user: models.Utilisateur, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

# 7. POST - /api/users/login : Connexion d’un utilisateur (JWT)
@app.post("/api/users/login", response_model=dict)
async def user_login(form_data: OAuth2PasswordBearer = Depends(oauth2_scheme)):
    return {"access_token": form_data, "token_type": "bearer"}

# 8. POST - /api/albums : Ajout d’un album
@app.post("/api/albums", response_model=models.Album)
async def create_album(album: models.Album, db: Session = Depends(get_db)):
    return crud.create_album(db, album)

# 9. POST - /api/albums/{id}/songs : Ajout d’un morceau dans l’album précisé par {id}
@app.post("/api/albums/{album_id}/songs", response_model=models.Morceau)
async def add_song_to_album(album_id: int, morceau: models.Morceau, db: Session = Depends(get_db)):
    return crud.add_song_to_album(db, album_id, morceau)

# 10. PUT - /api/artists/{id} : Modification de l’artiste précisé par {id}
@app.put("/api/artists/{artist_id}", response_model=models.Artiste)
async def update_artist(artist_id: int, artiste: models.Artiste, db: Session = Depends(get_db)):
    return crud.update_artist(db, artist_id, artiste)

# 11. PUT - /api/albums/{id} : Modification de l’album précisé par {id}
@app.put("/api/albums/{album_id}", response_model=models.Album)
async def update_album(album_id: int, album: models.Album, db: Session = Depends(get_db)):
    return crud.update_album(db, album_id, album)

# 12. PUT - /api/genres/{id} : Modification du genre précisé par {id}
@app.put("/api/genres/{genre_id}")
async def update_genre(genre_id: int, genre: models.Genre, db: Session = Depends(get_db)):
    return crud.update_genre(db, genre_id, genre)

from fastapi import HTTPException

# 13. DELETE - /api/users/{id} : Suppression de l'utilisateur précisé par {id}
@app.delete("/api/users/{user_id}", response_model=models.Utilisateur)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_utilisateur(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user

# 14. DELETE - /api/albums/{id} : Suppression de l'album précisé par {id}
@app.delete("/api/albums/{album_id}", response_model=models.Album)
async def delete_album(album_id: int, db: Session = Depends(get_db)):
    album = crud.delete_album(db, album_id)
    if album is None:
        raise HTTPException(status_code=404, detail="Album non trouvé")
    return album

# 15. DELETE - /api/artists/{id} : Suppression de l'artiste précisé par {id}
@app.delete("/api/artists/{artist_id}", response_model=models.Artiste)
async def delete_artist(artist_id: int, db: Session = Depends(get_db)):
    artist = crud.delete_artiste(db, artist_id)
    if artist is None:
        raise HTTPException(status_code=404, detail="Artiste non trouvé")
    return artist

# ...
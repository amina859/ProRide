from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    adresse = db.Column(db.String(200))
    telephone = db.Column(db.String(50))
    role = db.Column(db.String(50))
    numero_permis = db.Column(db.String(100), nullable=True)
    marque_voiture = db.Column(db.String(100), nullable=True)
    modele_voiture = db.Column(db.String(100), nullable=True)

    trajets = db.relationship('Trajet', backref='conducteur', lazy=True)
    reservations = db.relationship('Reservation', backref='passager', lazy=True)

class Trajet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    depart = db.Column(db.String(100))
    destination = db.Column(db.String(100))
    heure_depart = db.Column(db.String(20))
    places = db.Column(db.Integer)
    itineraire = db.Column(db.String(50))
    cout = db.Column(db.String(20))
    conducteur_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    reservations = db.relationship('Reservation', backref='trajet', lazy=True)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    passager_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    trajet_id = db.Column(db.Integer, db.ForeignKey('trajet.id'), nullable=False)

from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app import db
from app.models import User, Trajet, Reservation


main = Blueprint('main', __name__)


@main.route('/')
def accueil():
    session.clear() 
    return render_template('accueil.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        password = request.form['password']
        telephone = request.form['telephone']
        adresse = request.form['adresse']
        role = request.form['role']

        nouvel_utilisateur = User(
            nom=nom,
            email=email,
            password=password,
            telephone=telephone,
            adresse=adresse,
            role=role
        )
        db.session.add(nouvel_utilisateur)
        db.session.commit()

        return redirect(url_for('main.login'))

    return render_template('register.html')



@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email, password=password).first()

        if user:
            session['email'] = user.email
            session['role'] = user.role
            session['nom'] = user.nom
            if user.role == 'conducteur':
                return redirect(url_for('main.dashboard_conducteur'))
            else:
                return redirect(url_for('main.recherche'))
        else:
            flash("Email ou mot de passe incorrect", "danger")

    return render_template('login.html')

@main.route('/logout')
def logout():
    session.clear()
    flash('Déconnexion réussie.', 'info')
    return redirect(url_for('main.accueil'))

@main.route('/conducteur/dashboard')
def dashboard_conducteur():
    if session.get('role') != 'conducteur':
        return redirect(url_for('main.login'))

    # Trouver le conducteur connecté
    conducteur = User.query.filter_by(email=session.get('email')).first()

    if not conducteur:
        flash("Conducteur introuvable.", "danger")
        return redirect(url_for('main.login'))

    # Trouver tous ses trajets
    trajets = Trajet.query.filter_by(conducteur_id=conducteur.id).all()

    # Toutes les réservations associées à ses trajets
    reservations = []
    for trajet in trajets:
        for res in trajet.reservations:
            reservations.append({
                'nom_passager': res.passager.nom,
                'email_passager': res.passager.email,
                'telephone_passager': res.passager.telephone,
                'adresse_passager': res.passager.adresse,
                'depart': trajet.depart,
                'destination': trajet.destination,
                'heure_depart': trajet.heure_depart
            })

    return render_template('conducteur.html', trajets=trajets, reservations=reservations)


@main.route('/conducteur/ajouter_trajet', methods=['GET', 'POST'])
def ajouter_trajet():
    if session.get('role') != 'conducteur':
        flash("Accès refusé.", 'danger')
        return redirect(url_for('main.login'))

    if request.method == 'POST':
        depart = request.form['depart']
        destination = request.form['destination']
        heure_depart = request.form['heure_depart']
        places = int(request.form['places'])
        itineraire = request.form['itineraire']
        cout = request.form['cout']

        # Cherche le conducteur dans la base de données
        conducteur = User.query.filter_by(email=session['email']).first()

        trajet = Trajet(
            depart=depart,
            destination=destination,
            heure_depart=heure_depart,
            places=places,
            itineraire=itineraire,
            cout=cout,
            conducteur_id=conducteur.id
        )
        db.session.add(trajet)
        db.session.commit()

        flash("Trajet ajouté avec succès.", 'success')
        return redirect(url_for('main.dashboard_conducteur'))

    return render_template('ajouter_trajet.html')


@main.route('/recherche', methods=['GET', 'POST'])
def recherche():
    if request.method == 'POST':
        depart = request.form['depart']
        destination = request.form['destination']

        trajets = Trajet.query.filter(
            Trajet.depart.ilike(f'%{depart}%'),
            Trajet.destination.ilike(f'%{destination}%')
        ).all()
    else:
        trajets = Trajet.query.all()
        
    return render_template('recherche.html', trajets=trajets)

@main.route('/reserver/<int:trajet_id>', methods=['POST'])
def reserver(trajet_id):
    if session.get('role') != 'passager':
        flash("Seuls les passagers peuvent réserver.", "danger")
        return redirect(url_for('main.login'))

    trajet = Trajet.query.get_or_404(trajet_id)
    
    if trajet.places <= 0:
        flash("Aucune place disponible pour ce trajet.", "danger")
        return redirect(url_for('main.recherche'))

    passager = User.query.filter_by(email=session['email']).first()
    if not passager:
        flash("Passager introuvable.", "danger")
        return redirect(url_for('main.recherche'))

    # Création de la réservation
    reservation = Reservation(
        passager_id=passager.id,
        trajet_id=trajet.id
    )
    db.session.add(reservation)
    
    # Réduction du nombre de places disponibles
    trajet.places -= 1
    db.session.commit()

    # On prépare les infos à afficher dans confirmation.html
    infos_reservation = {
        'nom_passager': passager.nom,
        'email_passager': passager.email,
        'telephone_passager': passager.telephone,
        'adresse_passager': passager.adresse,
        'depart': trajet.depart,
        'destination': trajet.destination,
        'heure_depart': trajet.heure_depart
    }

    return render_template('confirmation.html', reservation=infos_reservation)



@main.route('/passager/dashboard')
def dashboard_passager():
    if session.get('role') != 'passager':
        return redirect(url_for('main.login'))

    passager = User.query.filter_by(email=session['email']).first()
    mes_reservations = Reservation.query.filter_by(passager_id=passager.id).all()
    return render_template('dashboard_passager.html', reservations=mes_reservations)

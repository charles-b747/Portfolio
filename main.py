# Import
from flask import Flask , render_template,request, redirect
#Import
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
# Podłączanie SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creating a DB
db = SQLAlchemy(app )



# Uruchamianie strony z treścią
@app.route('/')
def index():
    # Wyświetlanie obiektów Bazy
    # Assignment #2. Display the objects from the DB in index.html
    cards = Card.query.order_by(Card.id).all()
    
    return render_template('index.html',
                           #karty = cards
                            cards=cards
                           )


# Uruchomienie strony z kartą
@app.route('/card/<int:id>')
def card(id):
    #Zadanie #2. Wyświetl właściwą kartę według jej identyfikatora
    card = Card.query.get(id)

    return render_template('card.html', card=card)


# Umiejętności dynamiczne
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python , button_discord=button_discord , button_html=button_html , button_db=button_db)


class Card(db.Model):
   # Tworzenie kolumn
    # Adres mailowy
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, primary_key=True)

    def __repr__(self):
        return f'<Card {self.id}>'


# Formularz zgłoszeniowy
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        id =  request.form['id']
        text =  request.form['text']

        # Tworzenie obiektu, który zostanie wysłany do bazy danych
        card = Card(id=id, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')



if __name__ == "__main__":
    app.run(debug=True)

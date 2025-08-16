
from flask import (Blueprint,render_template,request,flash,redirect,url_for)
from myapp.db import get_db

bp=Blueprint("contact",__name__)

@bp.route("/")
def index():
    db = get_db()
    data = db.execute("SELECT * FROM contacts ORDER BY name ASC").fetchall()
    return render_template("contact.html", contacts=data)


from sqlite3 import IntegrityError

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        phone_no = request.form['phone_no']
        email = request.form['email']
        error = None

        # 🔍 Validation
        if not name:
            error = 'First Name is required.'
        elif not phone_no:
            error = 'Mobile No is required.'
        elif not email:
            error = 'Email Id is required.'

        if error:
            flash(error)
        else:
            try:
                db = get_db()
                db.execute(
                    'INSERT INTO contacts (name, phone_no, email) VALUES (?, ?, ?)',
                    (name, phone_no, email)
                )
                db.commit()
                flash('Contact added successfully!')
            except IntegrityError:
                flash('The name already exists!!! Try another.')

        return redirect(url_for('contact.index'))

    return render_template('create_contact.html')


@bp.route('/update/<id>',methods=('GET','POST'))
def update(id):
    db=get_db()
    data=db.execute("SELECT * FROM contacts where id=?",(id)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        phone_no = request.form['phone_no']
        email = request.form['email']
        error = None
        
        if not name:
            error = 'First Name is required.'
        if not phone_no:
            error = 'Mobile No is required.'
        if not email:
            error = 'Email Id is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE  contacts SET name=?, phone_no=?, email=? where id=?',
                ( name, phone_no, email, id)
            )
            db.commit()
        return redirect(url_for('contact.index'))

    return render_template('edit_contact.html',contact=data)


@bp.route('/delete/<id>')
def delete(id):
    db=get_db()
    db.execute("DELETE FROM contacts where id=?",(id)).fetchone()
    db.commit()
    flash("Deleted!!")
    return redirect(url_for('contact.index'))


@bp.route('/search', methods=['POST'])
def search():
    
    if request.method == 'POST':
        text = request.form['text']
        print("text:",text)
        
        error = None
        
        if error is not None:
            flash(error)
            return
        
        else:
            db=get_db()
            data = db.execute("SELECT * FROM contacts WHERE name LIKE ? or phone_no LIKE ? or email LIKE ?", [f"%{text}%", f"%{text}%",f"%{text}%"]).fetchall()

            return render_template("contact.html",contacts=data)
        
    
    return render_template('edit_contact.html',contact=data)


    



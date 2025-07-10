from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy 
from config import Config
from datetime import datetime

app = Flask(__name__)


app.config.from_object(Config)


db = SQLAlchemy(app)
class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(255), nullable=False)
    reviewer_name = db.Column(db.String(255), nullable=True) 
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Review {self.id}: {self.school_name} - {self.rating}/5>"


@app.route('/')
def index():
    return render_template('index.html', form_data={})

@app.route('/submit_review', methods=['POST'])
def submit_review():
    school_name = request.form.get('school_name', '').strip()
    reviewer_name = request.form.get('reviewer_name', '').strip()
    rating_str = request.form.get('rating', '').strip()
    comment = request.form.get('comment', '').strip()

    if not school_name or not rating_str or not comment:
        flash('All fields marked with (*) are required!', 'danger')
        return render_template('index.html', form_data=request.form)

   
    rating = int(rating_str)
    if not (1 <= rating <= 5):
        flash('Rating must be a number between 1 and 5.', 'danger')
        return render_template('index.html', form_data=request.form)

    
    new_review = Review(
        school_name=school_name,
        reviewer_name=reviewer_name,
        rating=rating,
        comment=comment
    )
    db.session.add(new_review)
    db.session.commit()
    flash('Review submitted successfully!', 'success')
    return redirect(url_for('reviews'))

@app.route('/reviews')
def reviews():
    all_reviews = Review.query.order_by(Review.submission_date.desc()).all()
    return render_template('review.html', reviews=all_reviews)


if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(debug=True)

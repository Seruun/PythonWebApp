from datetime import datetime

from flask import render_template, flash
from flask_login import login_required

from . import home
from .forms import NewCustomerForm
from .. import db
from ..globals import REV_NUM
from ..models import Customer, Employee

# if 0 -> no maintenance else maintenance
maintenance = 0


@home.context_processor
def inject_now():
    """
    Footer Copyright Year Getter
    """
    return {'now': datetime.utcnow()}


@home.context_processor
def revision():
    return {'rev_version': REV_NUM}


@home.route('/')
@home.route('/index')
def index():
    """
    Render the landingpage template on the / route
    """
    return render_template('index.html', title=str(title.name + ' - ' + page.name), template='index.html',
                           maintenance=maintenance)


@home.route('/home')
def homepage():
    """
    Render the homepage template on the /home route
    """
    return render_template('home.html', title=str(title.name + ' - ' + page.name))


@home.route('/contact')
def contact():
    """
    Render the contact template on the /contact route
    """
    return render_template('contact.html', title=str(title.name + ' - ' + page.name))


@home.route('/info')
def info():
    """
    Render the about us template on the /info route
    """
    return render_template('info.html', title=str(title.name + ' - ' + page.name))


@home.route('/gallery')
def gallery():
    """
    Render the contact template on the /dashboard route
    """
    return render_template('gallery.html', title=str(title.name + ' - ' + page.name))


@home.route('/felicia')
def felicia():
    """
    Render the contact template on the /felicia route
    """
    return render_template('staff/felicia.html', title=str(title.name + ' - ' + page.name))


@home.route('/frank')
def frank():
    """
    Render the contact template on the /felicia route
    """
    return render_template('staff/frank.html', title=str(title.name + ' - ' + page.name))


@home.route('/cover_up')
def cover_up():
    """
    Render the contact template on the /felicia route
    """
    return render_template('style/cover_up.html', title=str(title.name + ' - ' + page.name))


@home.route('/bio_realistic')
def bio_realistic():
    """
    Render the contact template on the /felicia route
    """
    return render_template('style/bio_realistic.html', title=str(title.name + ' - ' + page.name))


@home.route('/Steampunk')
def steampunk():
    """
    Render the contact template on the /felicia route
    """
    return render_template('style/steampunk.html', title=str(title.name + ' - ' + page.name))


@home.route('/care_instructions')
def care_instructions():
    """
    Render the contact template on the /felicia route
    """
    return render_template('style/care_instructions.html', title=str(title.name + ' - ' + page.name))


@home.route('/finance')
@login_required
def finance():
    """
    Render the contact template on the /felicia route
    """
    return render_template('secured/finance.html', title=str(title.name + ' - ' + page.name))


@home.route('/capacity')
@login_required
def capacity():
    """
    Render the contact template on the /felicia route
    """
    return render_template('secured/capacity.html', title=str(title.name + ' - ' + page.name))


@home.route('/settings')
@login_required
def settings():
    """
    Render the contact template on the /felicia route
    """
    return render_template('secured/settings.html', title=str(title.name + ' - ' + page.name))


@home.route('/producer')
def producer():
    """
    Render the contact template on the /felicia route
    """
    return render_template('producer.html', title=str(title.name + ' - ' + page.name))


@home.route('/version')
@login_required
def version():
    """
    Render the contact template on the /felicia route
    """
    return render_template('version.html', title=str(title.name + ' - ' + page.name))


# dynamic News display
@home.route('/news_index/')
@home.route('/news_index/<news_id>/')
@login_required
def news_index(news_id):
    """
    Render the contact template on the /felicia route
    """
    return render_template('news/news_index_{}'.format(news_id) + '.html', title=str(title.name + ' - ' + page.name))

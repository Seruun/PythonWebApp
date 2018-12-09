from flask import render_template, flash
from flask_login import login_required

from . import home
from ..globals import title_name, maintenance


@home.route('/')
@home.route('/index')
def index():
    """
    Render the landingpage template on the / route
    """
    Titel = "Landingpage"

    return render_template('index.html', title=str(title_name + ' - ' + Titel), template='index.html',
                           maintenance=maintenance)


@home.route('/home')
def homepage():
    """
    Render the homepage template on the /home route
    """

    Title = "Home"

    return render_template('home.html', title=str(title_name + ' - ' + Title))


@home.route('/contact')
def contact():
    """
    Render the contact template on the /contact route
    """

    Title = "Kontakt"

    return render_template('contact.html', title=str(title_name + ' - ' + Title))


@home.route('/info')
def info():
    """
    Render the about us template on the /info route
    """

    Title = "Über uns"

    return render_template('info.html', title=str(title_name + ' - ' + Title))


@home.route('/gallery')
def gallery():
    """
    Render the contact template on the /dashboard route
    """

    Title = "Gallerie"

    return render_template('gallery.html', title=str(title_name + ' - ' + Title))


@home.route('/felicia')
def felicia():
    """
    Render the contact template on the /felicia route
    """

    Title = "Tätowiererin Nicole Kemnitz"

    return render_template('staff/felicia.html', title=str(title_name + ' - ' + Title))


@home.route('/frank')
def frank():
    """
    Render the contact template on the /felicia route
    """

    Title = "Tätowierer Frank Kemnitz"

    return render_template('staff/frank.html', title=str(title_name + ' - ' + Title))


@home.route('/cover_up')
def cover_up():
    """
    Render the contact template on the /felicia route
    """

    Title = "Cover Up's"

    return render_template('style/cover_up.html', title=str(title_name + ' - ' + Title))


@home.route('/bio_realistic')
def bio_realistic():
    """
    Render the contact template on the /felicia route
    """

    Title = "Bio Realismus"

    return render_template('style/bio_realistic.html', title=str(title_name + ' - ' + Title))


@home.route('/Steampunk')
def steampunk():
    """
    Render the contact template on the /felicia route
    """

    Title = "Steampunk"

    return render_template('style/steampunk.html', title=str(title_name + ' - ' + Title))


@home.route('/care_instructions')
def care_instructions():
    """
    Render the contact template on the /felicia route
    """

    Title = "Tattoopflegehinweise"

    return render_template('style/care_instructions.html', title=str(title_name + ' - ' + Title))


@home.route('/finance')
@login_required
def finance():
    """
    Render the contact template on the /felicia route
    """

    Title = "Buchhaltung"

    return render_template('secured/finance.html', title=str(title_name + ' - ' + Title))


@home.route('/capacity')
@login_required
def capacity():
    """
    Render the contact template on the /felicia route
    """

    Title = "Lager und Bestellungen"

    return render_template('secured/capacity.html', title=str(title_name + ' - ' + Title))


@home.route('/settings')
@login_required
def settings():
    """
    Render the contact template on the /felicia route
    """

    Title = "Einstellungen"

    return render_template('secured/settings.html', title=str(title_name + ' - ' + Title))


@home.route('/producer')
def producer():
    """
    Render the contact template on the /felicia route
    """

    Title = "Powered By"

    return render_template('producer.html', title=str(title_name + ' - ' + Title))


@home.route('/version')
@login_required
def version():
    """
    Render the contact template on the /felicia route
    """

    Title = "Versionshistorie"

    return render_template('version.html', title=str(title_name + ' - ' + Title))


# dynamic News display
@home.route('/news_index/')
@home.route('/news_index/<news_id>/')
@login_required
def news_index(news_id):
    """
    Render the contact template on the /felicia route
    """

    Title = "Newsletter"

    return render_template('news/news_index_{}'.format(news_id) + '.html', title=str(title_name + ' - ' + Title))

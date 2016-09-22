import sae
sae.add_vendor_dir('flaskmail')
from run import app
  
application = sae.create_wsgi_app(app)
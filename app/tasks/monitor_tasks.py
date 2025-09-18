from celery_worker import celery
from app import create_app
from app.extensions import db
from app.models.site import Site, StatusLog
from app.utils.http_checker import check_site
from datetime import datetime

flask_app = create_app()
flask_app.app_context().push()

@celery.task
def verificar_sites():
    sites = Site.query.all()

    for site in sites:
        status = check_site(site.url)

        log = StatusLog(
            site_id=site.id,
            status_code=status,
            checked_at=datetime.utcnow()
        )
        db.session.add(log)

    db.session.commit()

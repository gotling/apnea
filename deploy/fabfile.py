from fabric.decorators import task
from fabric.tasks import execute
import refabric

refabric.bootstrap()

@task
def setup():
    """
    Full application setup from scratch
    """
    from blues import app, postgresql, memcached, uwsgi, nginx

    postgresql.setup()
    memcached.setup()
    app.setup()
    uwsgi.setup()
    nginx.setup()


@task
def deploy():
    """
    Full application deploy
    """
    from blues import app, django, memcached, uwsgi

    # Update source code and install requirements
    code_changed = app.deploy(auto_reload=False)

    if code_changed:
        # Migrage database and collect static files
        django.deploy()

        # Reload
        app.reload()

        uwsgi.reload()

        memcached.flush()


@task
def deploy_code():
    """
    Deploy code and collect static files, skip migrations and requirements
    """
    from blues import app
    from blues import django

    # Update source code
    pre_commit, post_commit = app.update_source()

    if pre_commit != post_commit:
        # Collect static files
        django.collectstatic()
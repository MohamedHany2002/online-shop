from celery import task
@task
def printhello():
    print("hello")
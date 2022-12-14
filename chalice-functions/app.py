import os
import random
import uuid
import boto3

import requests
from boto3.dynamodb.conditions import Attr
from bs4 import BeautifulSoup
from chalice import Chalice

app = Chalice(app_name='etl-functions')

AWS_ACCESS_KEY_ID = os.environ.get("PROVIDER_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("PROVIDER_AWS_SECRET_ACCESS_KEY")


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/lemonde/international')
def latest_lemonde_news():
    url = 'https://www.lemonde.fr/international/'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    latest_news = [l.get_text() for l in soup.find_all("h3", {"class": "teaser__title"})]

    dynamodb = boto3.resource('dynamodb')
    scrapped_data_table = dynamodb.Table('scrapped-data')

    res = scrapped_data_table.scan(
        FilterExpression=Attr('scrapped_data').is_in(latest_news),
    )
    existing = [r['scrapped_data'] for r in res['Items']]
    news = set(latest_news) - set(existing)

    print(f"Inserted news {len(news)}")

    with scrapped_data_table.batch_writer() as batch:
        for n in news:
            batch.put_item(
                Item={
                    'id': str(uuid.uuid4()),
                    'label': 'LEMONDE_NEWS_TITLE',
                    'scrapped_data': n
                },
            )

    return [{'title': n} for n in news]


@app.schedule('rate(1 minute)')
def every_minute(event):
    number = random.randint(0, 4)
    if number > 2:
        print("fake exception !")
        raise ValueError("Fake exception")
    print("I ran !")


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#

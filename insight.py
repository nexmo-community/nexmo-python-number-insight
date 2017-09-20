import json
import click
import nexmo


@click.command()
@click.argument('type', type=click.Choice(['basic', 'standard', 'advanced']))
@click.option('--number', prompt=True)
def cli(type, number):
    nexmo_client = nexmo.Client(key='KEY', secret='SECRET')
    response = {
        'basic': nexmo_client.get_basic_number_insight,
        'standard': nexmo_client.get_number_insight,
        'advanced': nexmo_client.get_advanced_number_insight
    }.get(type)(number=number)

    print(json.dumps(response))

import click
from date_calculator.models import Date


@click.command()
@click.argument("event1")
@click.argument("event2")
def main(event1, event2):
    date1 = Date.from_string(event1)
    date2 = Date.from_string(event2)
    print(date1.days_fully_elapsed_to(date2))


if __name__ == "__main__":
    main()

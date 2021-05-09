import click
from date_calculator.models import Date


class DateParamType(click.ParamType):
    name = "date_param_type"

    def convert(self, value, param, ctx):
        try:
            return Date.from_string(value)
        except (IndexError, ValueError, TypeError):
            self.fail(f"{value!r} is not a valid DD/MM/YYYY string", param, ctx)


DATE_PARAM_TYPE = DateParamType()


@click.command()
@click.argument("event_1", type=DATE_PARAM_TYPE)
@click.argument("event_2", type=DATE_PARAM_TYPE)
def main(event_1, event_2):
    """A command-line based program that accepts date input from the console
    and calculates the number of full days elapsed in between two events.
    Dates are to be formatted DD/MM/YYYY.
    
    Usage example:
    
    date-calculator-cli 03/01/1989 03/08/1983
    
    1979
    """
    click.echo("{}".format(event_1.days_fully_elapsed_to(event_2)))


if __name__ == "__main__":
    main()

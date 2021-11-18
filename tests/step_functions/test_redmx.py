"""Rate, Errors and Duration (RED) Metrics feature tests."""
import time
from redmx import RateErrorDuration

from pytest_bdd import (
    given,
    parsers,
    scenario,
    then,
    when,
)


@scenario('../features/redmx.feature', 'Test Metrics')
def test_test_metrics():
    """Test Metrics."""


@given('a metrics object', target_fixture='redmx_fixture')
def a_metrics_object():
    """a metrics object."""
    redmx = RateErrorDuration()

    return {
        'redmx': redmx
    }


@when(parsers.parse('{actual_duration:d} duration in seconds is applied'))
def actual_duration_duration_in_seconds_is_applied(actual_duration):
    """<actual_duration> duration in seconds is applied."""
    time.sleep(actual_duration)


@when(parsers.parse('{actual_errors} errors are applied'))
def actual_errors_errors_are_applied(redmx_fixture, actual_errors):
    """<actual_errors> errors are applied."""
    redmx = redmx_fixture['redmx']
    actual_errors = actual_errors.split(',')

    for s in actual_errors:
        i = int(s)
        redmx.increment_errors(i)

    redmx_fixture['redmx'] = redmx


@when(parsers.parse('{actual_transactions} transactions are applied'))
def actual_transactions_transactions_are_applied(redmx_fixture, actual_transactions):
    """<actual_transactions> transactions are applied."""
    actual_transactions = actual_transactions.split(',')
    redmx = redmx_fixture['redmx']

    for count in actual_transactions:
        count = int(count)
        redmx.increment_count(count)

    redmx_fixture['redmx'] = redmx


@then(parsers.parse('ensure duration is greater than or equal to {expected_duration:d}'))
def ensure_duration_is_greater_than_or_equal_to_expected_duration(redmx_fixture, expected_duration):
    """ensure duration is greater than or equal to <expected_duration>."""
    redmx = redmx_fixture['redmx']
    duration = redmx.duration()
    message = f'Expected duration (ms) to be >= {expected_duration}, but it was {duration}.'
    assert duration >= expected_duration, message


@then(parsers.parse('ensure errors matches {expected_errors:d}'))
def ensure_errors_matches_expected_errors(redmx_fixture, expected_errors):
    """ensure errors matches <expected_errors>."""
    redmx = redmx_fixture['redmx']
    assert expected_errors == redmx.errors()


@then(parsers.parse('ensure rate matches {expected_rate:d}'))
def ensure_rate_matches_expected_rate(redmx_fixture, expected_rate):
    """ensure rate matches <expected_rate>."""
    redmx = redmx_fixture['redmx']
    redmx.rate() == expected_rate

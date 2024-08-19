import unittest
from unittest.mock import patch
alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    if celcius>200:
        return 500
    return 200

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0


alert_in_celcius(400.5)
alert_in_celcius(303.6)
assert(network_alert_stub(204.2)==500)
print('All is well (maybe!)')
print(f'{alert_failure_count} alerts failed.')
@patch('network_alert_stub')
def test_alert_failure_count_increment(mock_network_alert):
    mock_network_alert.return_value = 500
    alert_in_celcius(100)
    assert(alert_failure_count==1)


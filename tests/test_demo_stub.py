# http://xunitpatterns.com/Test%20Double.html

from unittest.mock import Mock

from test_doubles.demo_stub import Alarm, Sensor


def test_alarm_is_off_by_default() -> None:
    alarm = Alarm()
    assert not alarm.is_alarm_on

# Either create a custom stub like this and use it in test_alarm_is_on_at_lower_threshold


class StubSensor:
    def sample_pressure(self):
        return 17.0


def test_alarm_is_on_at_lower_threshold() -> None:
    # passing StubSensor
    alarm = Alarm(StubSensor())
    alarm.check()
    assert alarm.is_alarm_on

# or instead use Mock and use it like below, both are same


def test_alarm_is_on_at_higher_threshold() -> None:
    # these 2 stub lines of code do the same thing as StubSensor Class
    stub = Mock(Sensor)
    stub.sample_pressure.return_value = 21.0
    # passing Mock
    alarm = Alarm(stub)
    alarm.check()
    assert alarm.is_alarm_on

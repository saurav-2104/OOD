"""
Define a one-to-many dependency between objects so that when one object
changes state, all its dependents are notified and updated automatically.
"""
import abc

"""
Use case:
The WeatherObject provides information about weather for a given city. It can be assumed that it collects the
information from the interface of sensors. There are several display which depend on this object to get the latest
data. Moreover, several third party would also want to plug in their display in future.
"""


# All the interfaces
class Observable(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def register_observer(self, observer):
        raise NotImplementedError("Abstract method")

    @abc.abstractmethod
    def remove_observer(self, observer):
        raise NotImplementedError("Abstract method")

    @abc.abstractmethod
    def notify_observers(self):
        raise NotImplementedError("Abstract method")


class Observer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self, temp, pressure, humidity):
        raise NotImplementedError("Abstract method")


class Display(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def display(self):
        raise NotImplementedError("Abstract method")


# Concrete classes
class Weather(Observable):

    def __init__(self, observers=None):
        self.pressure = None
        self.temp = None
        self.humidity = None
        self.observers = observers

    def register_observer(self, observer):
        if self.observers:
            self.observers.append(observer)
        else:
            self.observers = [observer]

    def remove_observer(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print("The given observer: {} is not registered.".format(observer))

    def notify_observers(self):
        for o in self.observers:
            o.update(self.temp, self.pressure, self.humidity)

    def update_weather(self, pressure, temp, humidity):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()


class MobileDisplay(Observer, Display):

    def __init__(self, weather_object=None):
        # Only updates pressure. Pull pattern will work better here.
        self.pressure = None
        self.weather_object = weather_object
        self.weather_object.register_observer(self)

    def update(self, temp, pressure, humidity):
        self.pressure = pressure
        self.display()

    def display(self):
        print("Mobile display: The pressure is {}".format(self.pressure))


class WatchDisplay(Observer, Display):

    def __init__(self, weather_object=None):
        # Only updates pressure. Pull pattern will work better here.
        self.temp = None
        self.weather_object = weather_object
        self.weather_object.register_observer(self)

    def update(self, temp, pressure, humidity):
        self.temp = temp
        self.display()

    def display(self):
        print("Watch display: The temperature is {}".format(self.temp))


if __name__ == '__main__':
    weather = Weather()
    mobile = MobileDisplay(weather)
    watch = WatchDisplay(weather)
    weather.update_weather(1012, 28, 60)

from django.dispatch import Signal
action_signal = Signal(providing_args=["instance","request"])
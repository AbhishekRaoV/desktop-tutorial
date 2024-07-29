'''This code will calculate the energy metrics using codecarbon'''
'''Provide your package/filename in order to continue with calculation of energy metrics (ex: model_emissions)'''

from codecarbon import EmissionsTracker
import model_emissions
import importlib
try:
    # print("Enter you package name")
    # pkg = input()
    # model_emission = importlib.import_module(pkg)

    tracker = EmissionsTracker()

    tracker.start()
    model_emissions.main()
    emissions = tracker.stop()
    print(emissions)
except Exception as e:
    print(e)

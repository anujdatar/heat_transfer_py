''' import material and process properties from the settings files '''

import json

def import_material(material):
    ''' import material properties from the settings files '''

    jsfile = open('./settings/materials.json')
    data = json.load(jsfile)
    jsfile.close()

    # material
    rho = data[material]['Density']
    Cp = data[material]['SpecificHeat']
    k = data[material]['Conductivity']
    T_melt = data[material]['MeltingTemperature']
    emissiv = data[material]['Emissivity']

    return rho, Cp, k, T_melt, emissiv

def import_process():
    ''' import process settings'''

    jsfile = open('./settings/process_settings.json')
    data = json.load(jsfile)
    jsfile.close()

    # process
    L_pow = data['process']['LaserPower']
    L_spot = data['process']['LaserSpotSize']
    L_vel = data['process']['LaserScanningVelocity']
    T_inf = data['process']['AmbientTemperature']
    hc_air = data['process']['ConvectiveCoefficient']

    return L_pow, L_spot, L_vel, T_inf, hc_air

def import_solver_settings(solver):
    ''' import solver settings '''

    jsfile = open('./settings/solver_settings.json')
    data = json.load(jsfile)
    jsfile.close()

    epsit = data[solver]['epsit']
    max_iter = data[solver]['max_iter']
    omega = data[solver]['omega']

    return epsit, max_iter, omega
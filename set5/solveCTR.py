from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy import Symbol
import sympy as sy
from math import floor
import numpy as np

A = {'bid': .10, 'ctr1': .015, 'ctr2': .010, 'ctr3': .005, 'budget': 1}
B = {'bid': .09, 'ctr1': .016, 'ctr2': .012, 'ctr3': .006, 'budget': 2}
C = {'bid': .08, 'ctr1': .017, 'ctr2': .014, 'ctr3': .007, 'budget': 3}
D = {'bid': .07, 'ctr1': .018, 'ctr2': .015, 'ctr3': .008, 'budget': 4}
E = {'bid': .06, 'ctr1': .019, 'ctr2': .016, 'ctr3': .010, 'budget': 5}


total_clicks = 0
Adv = {1: A, 2: B, 3: C, 4: D, 5: E}
print Adv
expected_frs = {x: round(Adv[x]['bid']*Adv[x]['ctr1'], 5) for x in Adv.keys() if Adv[x]['budget'] > Adv[x]['bid']}
expected_sec = {x: round(Adv[x]['bid']*Adv[x]['ctr2'], 5) for x in Adv.keys() if Adv[x]['budget'] > Adv[x]['bid']}
expected_thr = {x: round(Adv[x]['bid']*Adv[x]['ctr3'], 5) for x in Adv.keys() if Adv[x]['budget'] > Adv[x]['bid']}

expected_ads = [expected_frs, expected_sec, expected_thr]
ads_shown = {}
for i, expected_ad in enumerate(expected_ads):
    ad_id = [k for k, v in expected_ad.iteritems() if v == max(expected_ad.values()) and k not in [x['id'] for x in ads_shown.values()]][0]
    print ad_id
    ads_shown[i+1] = {'id': ad_id, 'bid': Adv[ad_id]['bid'], 'ctr': Adv[ad_id]['ctr'+str(i+1)], 'budget': Adv[ad_id]['budget']}

min_clicks = np.inf
exhaust = None
for k, ad_details in ads_shown.iteritems():
    clicks = ad_details['budget']*ad_details['ctr']/ad_details['bid']
    if clicks < min_clicks:
        min_clicks = clicks
        exhaust = k
    

click_until_now = ads_shown[exhaust]['budget']/ads_shown[exhaust]['bid']

for k, ad_details in ads_shown.iteritems():
    clicks = floor((click_until_now*ad_details['ctr'])/ads_shown[exhaust]['ctr'])
    Adv[ad_details['id']]['budget'] -= clicks*Adv[ad_details['id']]['bid']
    print ad_details['id'], 'has', clicks, 'clicks'
    total_clicks += clicks

print Adv
print '---------------------'
print 'total clicks', total_clicks


expected_frs = {x: round(Adv[x]['bid']*Adv[x]['ctr1'], 5) for x in Adv.keys() if Adv[x]['budget'] > Adv[x]['bid']}
expected_sec = {x: round(Adv[x]['bid']*Adv[x]['ctr2'], 5) for x in Adv.keys() if Adv[x]['budget'] > Adv[x]['bid']}
expected_thr = {x: round(Adv[x]['bid']*Adv[x]['ctr3'], 5) for x in Adv.keys() if Adv[x]['budget'] > Adv[x]['bid']}

expected_ads = [expected_frs, expected_sec, expected_thr]
ads_shown = {}
for i, expected_ad in enumerate(expected_ads):
    ad_id = [k for k, v in expected_ad.iteritems() if v == max(expected_ad.values()) and k not in [x['id'] for x in ads_shown.values()]][0]
    print ad_id
    ads_shown[i+1] = {'id': ad_id, 'bid': Adv[ad_id]['bid'], 'ctr': Adv[ad_id]['ctr'+str(i+1)], 'budget': Adv[ad_id]['budget']}

print ads_shown
min_clicks = np.inf
exhaust = None
for k, ad_details in ads_shown.iteritems():
    clicks = ad_details['budget']*ad_details['ctr']/ad_details['bid']
    if clicks < min_clicks:
        min_clicks = clicks
        exhaust = k
    

click_until_now = ads_shown[exhaust]['budget']/ads_shown[exhaust]['bid']

for k, ad_details in ads_shown.iteritems():
    clicks = floor((click_until_now*ad_details['ctr'])/ads_shown[exhaust]['ctr'])
    Adv[ad_details['id']]['budget'] -= clicks*Adv[ad_details['id']]['bid']
    print ad_details['id'], 'has', clicks, 'clicks'
    total_clicks += clicks

print Adv
print '---------------------'
print 'total clicks', total_clicks

expected_frs = {x: round(Adv[x]['bid']*Adv[x]['ctr1'], 5) for x in Adv.keys() if Adv[x]['budget'] > Adv[x]['bid']}
expected_sec = {x: round(Adv[x]['bid']*Adv[x]['ctr2'], 5) for x in Adv.keys() if Adv[x]['budget'] > Adv[x]['bid']}
expected_thr = {x: round(Adv[x]['bid']*Adv[x]['ctr3'], 5) for x in Adv.keys() if Adv[x]['budget'] > Adv[x]['bid']}

expected_ads = [expected_frs, expected_sec, expected_thr]
ads_shown = {}
for i, expected_ad in enumerate(expected_ads):
    ad_id = [k for k, v in expected_ad.iteritems() if v == max(expected_ad.values()) and k not in [x['id'] for x in ads_shown.values()]][0]
    print ad_id
    ads_shown[i+1] = {'id': ad_id, 'bid': Adv[ad_id]['bid'], 'ctr': Adv[ad_id]['ctr'+str(i+1)], 'budget': Adv[ad_id]['budget']}

print ads_shown
min_clicks = np.inf
exhaust = None
for k, ad_details in ads_shown.iteritems():
    clicks = ad_details['budget']*ad_details['ctr']/ad_details['bid']
    if clicks < min_clicks:
        min_clicks = clicks
        exhaust = k
    

click_until_now = ads_shown[exhaust]['budget']/ads_shown[exhaust]['bid']

for k, ad_details in ads_shown.iteritems():
    clicks = floor((click_until_now*ad_details['ctr'])/ads_shown[exhaust]['ctr'])
    Adv[ad_details['id']]['budget'] -= clicks*Adv[ad_details['id']]['bid']
    print ad_details['id'], 'has', clicks, 'clicks'
    total_clicks += clicks

print Adv
print '---------------------'
print 'total clicks', total_clicks






































# x = Symbol('x', real=True)

# sol_frs = sy.solve(x*Adv[max_frs.keys()[0]]['bid'] >= Adv[max_frs.keys()[0]]['budget'], x)
# sol_sec = sy.solve(x*Adv[max_sec.keys()[0]]['bid'] >= Adv[max_sec.keys()[0]]['budget'], x)
# sol_thr = sy.solve(x*Adv[max_thr.keys()[0]]['bid'] >= Adv[max_thr.keys()[0]]['budget'], x)




# print floor(sol_frs.rhs)
# print floor(sol_sec.rhs)
# print floor(sol_thr.rhs)

# print floor(sol_frs.rhs)*round(Adv[max_frs.keys()[0]]['ctr1'], 5)
# print floor(sol_sec.rhs)*round(Adv[max_sec.keys()[0]]['ctr2'], 5)
# print floor(sol_thr.rhs)*round(Adv[max_thr.keys()[0]]['ctr3'], 5)

# ineq = [[x*Adv[max_frs.keys()[0]]['bid']*Adv[max_frs.keys()[0]]['ctr1'] >= 
#         Adv[max_frs.keys()[0]]['budget']],
#         [x*Adv[max_sec.keys()[0]]['bid']*Adv[max_sec.keys()[0]]['ctr2'] >= 
#         Adv[max_sec.keys()[0]]['budget']],
#         [x*Adv[max_thr.keys()[0]]['bid']*Adv[max_thr.keys()[0]]['ctr3'] >= 
#         Adv[max_thr.keys()[0]]['budget']]
#         ]
# sol = reduce_rational_inequalities(ineq, x)
# print floor(sol.rhs)
# print floor(sol.rhs)*Adv[max_frs.keys()[0]]['ctr1']
# print floor(sol.rhs)*Adv[max_sec.keys()[0]]['ctr2']
# print floor(sol.rhs)*Adv[max_thr.keys()[0]]['ctr3']

# print floor(sol.rhs)*Adv[max_sec.keys()[0]]['bid']*Adv[max_sec.keys()[0]]['ctr1']
# print floor(sol.rhs)*Adv[max_thr.keys()[0]]['bid']*Adv[max_thr.keys()[0]]['ctr1']
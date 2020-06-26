import DML_Construction as dml
import csv
import pickle
import Aid_Function_Blocks as aid
import Production_Simulation as pdc
import Massive_Simulation as ms

# rmt_module_number_list = [3, 2, 2]
# time_span_day = 50.3
# order_size = 500
# order_low_mean = 20
# order_lar_mean = 200

# save = open("test.csv", "wb")
# pickle.dump(x, save)
# save.close()

# process_time_array = [5, 13.7, 6, 25.5]
# process_shrinking_ratio_lower_bond = 0.1
# process_shrinking_ratio_upper_bond = 0.5
#
# x = dml.layout_reconfiguration_time(process_time_array,
#                                     process_shrinking_ratio_lower_bond, process_shrinking_ratio_upper_bond)
# print(x)
#

# # RMS Summary
#
# print(order_size)
# aid.mean_print(mean)
# aid.boundary_print(order_lower_bond, order_upper_bond)

# # Manufacturing Process List
# manufacturing_process_kind = ['Cut', 'Mill', 'Bore', 'Drill', 'Turn']
# manufacturing_process_weight = [100, 50, 35, 15, 100]
#
# # order_sequence = [i for i in range(1, order_size + 1)]
# # print(order_sequence)
# # product_variant = [random.randint(1, product_variant_num) for i in range(0, order_size)]
# # print(product_variant)
# #
# # combined_order = order_sequence
# # for i in range(order_size):
# #     combined_order[i] = {'Sequence': order_sequence[i], 'Variant': product_variant[i]}
# # print(combined_order)
#
# # for i in range(10):
# #     test = RandomComponentGenerator.gen_uniform(lower_bond, upper_bond)
# #     print(test)
# #     i += 1
# #
# #
# # product_plan = random.choices(RandomComponentGenerator.manufacturing_process_kind,
# #                               RandomComponentGenerator.manufacturing_process_weight, k=10)
# # print(product_plan)

profit_time_grade = (2.25, 3.38, 5.06, 7.59)

# test_order = [[5598, 8, 2345], [30005, 5, 1305], [38168, 1, 2306], [54722, 4, 2209], [77190, 1, 2347], [112188, 8, 2429], [134101, 5, 1390], [162641, 6, 289], [200535, 5, 1332], [210874, 3, 2209], [259936, 4, 2153], [262348, 7, 1747], [293476, 2, 2246], [298594, 2, 2267], [308850, 8, 2353], [319287, 6, 300], [349515, 1, 2384], [390776, 4, 2157], [413562, 7, 1697], [426388, 3, 2295], [461153, 1, 2379], [478300, 6, 311], [486715, 0, 2404], [501772, 8, 2371], [520204, 7, 1695], [549905, 0, 2429], [565110, 7, 1716], [605718, 5, 1305], [689862, 4, 2304], [696255, 5, 1304], [759511, 6, 296], [768664, 1, 2388], [807489, 6, 292], [836166, 0, 2354], [853727, 6, 289], [917190, 1, 2365], [921045, 4, 2196], [971928, 4, 2208], [986993, 0, 2379], [992849, 4, 2114], [1039646, 8, 2481], [1074059, 3, 2160], [1079426, 6, 285], [1088653, 0, 2385], [1095530, 8, 2438], [1258780, 6, 293], [1285276, 3, 2230], [1292096, 5, 1304], [1313275, 8, 2465], [1339096, 6, 283], [1399480, 4, 2126], [1565822, 4, 2183], [1578321, 3, 2181], [1617228, 8, 2358], [1705344, 8, 2494], [1731887, 2, 2315], [1787668, 5, 1291], [1806088, 5, 1271], [1848417, 8, 2398], [1978075, 6, 326], [1982629, 7, 1688], [1992975, 6, 313], [2005583, 4, 2201], [2009739, 5, 1309], [2092320, 2, 2258], [2119808, 2, 2337], [2203259, 5, 1355], [2383687, 7, 1742], [2413682, 8, 2373], [2414817, 6, 283], [2422405, 4, 2116], [2440828, 3, 2173], [2451965, 0, 2474], [2465340, 5, 1327], [2477919, 2, 2283], [2509750, 4, 2207], [2511702, 5, 1301], [2540891, 1, 2281], [2561026, 8, 2340], [2631335, 6, 295], [2663738, 2, 2433], [2697927, 6, 289], [2761147, 7, 1692], [2765464, 8, 2317], [2770741, 5, 1317], [2775026, 4, 2135], [2800915, 8, 2370], [2857346, 2, 2365], [2868193, 6, 276], [2909792, 7, 1688], [2934883, 2, 2352], [2951345, 4, 2184], [2958426, 4, 2231], [2983195, 3, 2166], [2989830, 3, 2235], [3096352, 3, 2188], [3100943, 7, 1690], [3130004, 3, 2213], [3134851, 5, 1320], [3145686, 1, 2281], [3177539, 1, 2300], [3221279, 7, 1706], [3223873, 0, 2523], [3255877, 2, 2296], [3261767, 4, 2201], [3271074, 0, 2385], [3346830, 7, 1706], [3389134, 4, 2241], [3462519, 8, 2403], [3478521, 3, 2153], [3484124, 0, 2379], [3587915, 3, 2232], [3608921, 7, 1718], [3760757, 2, 2259], [3795315, 1, 2351], [3795858, 5, 1226], [3807507, 6, 296], [3811985, 3, 2139], [3835852, 4, 2175], [3848322, 0, 2415], [3870464, 8, 2402], [3883954, 8, 2375], [3888064, 2, 2322], [3893233, 4, 2207], [3913070, 4, 2189], [3914691, 2, 2271], [3961128, 1, 2367], [3965371, 0, 2458], [4029116, 0, 2451], [4064223, 1, 2422], [4092878, 7, 1715], [4097989, 5, 1305], [4129674, 5, 1357], [4135877, 4, 2175], [4145093, 2, 2229], [4204406, 1, 2356], [4217220, 2, 2302], [4218852, 6, 310], [4220202, 3, 2239], [4280440, 4, 2208], [4281152, 3, 2187], [4296962, 8, 2333], [4335235, 3, 2207], [4363702, 2, 2338], [4372947, 4, 2284], [4377073, 8, 2383], [4427457, 1, 2379], [4430385, 3, 2239], [4456466, 2, 2275], [4472341, 5, 1416], [4510768, 4, 2236], [4520372, 7, 1754], [4520725, 1, 2355], [4552308, 4, 2206], [4591203, 5, 1339], [4627184, 7, 1698], [4642330, 3, 2325], [4655130, 4, 2151], [4726327, 6, 299], [4726672, 6, 313], [4760735, 0, 2467], [4841278, 4, 2122], [4879669, 4, 2170], [4882642, 0, 2417], [4910012, 4, 2242], [4930845, 7, 1768], [4978726, 1, 2274], [5018356, 7, 1703], [5049967, 6, 321], [5069955, 5, 1271], [5080392, 5, 1309], [5085853, 6, 288], [5095134, 4, 2221], [5122185, 1, 2256], [5128621, 2, 2303], [5131579, 7, 1670], [5136039, 2, 2297], [5138891, 7, 1713], [5147064, 8, 2319], [5156928, 7, 1613]]
#
# test_production_time = [17.02, 11.86, 17.65, 12.939999999999998, 19.3, 21.73, 24.01, 18.099999999999998, 16.57]
# test_dml_process_time_array = [6.3587230608188845, 2.1673057696229754, 7.153371087920857,
#                                5.719706074158943, 4.25907154086885, 8.94257108017298,
#                                4.54875797954298, 4.308234776750582, 3.3411593249358025]
#
# test_reconfiguring_time = [81, 156, 179, 249, 261, 164, 98, 64, 238]
# test_dml_reconfiguring_time = [47802, 681346, 159458, 221358, 914462, 103509, 259859, 264835, 124789]
# test_expand_ratio = 5

test_order = [[447,    0, 2210], [2134,   3, 2390], [5690,   1, 3000], [7598,   0, 2210], [12413,  0, 2320],
              [15224,  1, 2860], [30804,  3, 2540], [43747,  2, 2090], [50034,  2, 1670], [55950,  0, 2180],
              [58849,  3, 2450], [59792,  0, 1680], [77684,  0, 2020], [89686,  3, 2280], [94536,  2, 1720],
              [107695, 3, 2350], [112531, 1, 2810], [119548, 0, 2050], [120227, 2, 2310], [123640, 1, 2770],
              [125949, 0, 1900], [126690, 3, 2230], [132125, 3, 2550], [141378, 1, 3140], [145169, 3, 2210],
              [147391, 0, 2090], [148028, 1, 2950], [156016, 2, 2000], [164845, 1, 3170], [167780, 0, 2330]]

# test_order = [[3300, 2, 430],
#               [9600, 3, 4880],
#               [10200, 1, 540],
#               [10800, 0, 800],
#               [17400, 0, 940],
#               [17400, 1, 1180],
#               [19400, 3, 1230],
#               [27700, 2, 460],
#               [28100, 2, 200],
#               [34500, 0, 1570],
#               [35000, 3, 50],
#               [38800, 0, 3330],
#               [39600, 0, 1030],
#               [46400, 3, 3440],
#               [50500, 2, 2220],
#               [55600, 3, 1260],
#               [57600, 1, 1250],
#               [59800, 0, 4340]]

test_dml_process_time_array = [30, 25, 40, 55]
test_dml_reconfiguring_time = [3600, 2500, 4700, 5200]

test_min_batch = [1000, 800, 500, 1500]
test_stock_ratio = 2
test_stock_standard, test_request_stock = dml.pull_dml_stock_initialise(test_min_batch, test_stock_ratio)
# print(test_stock_standard, test_request_stock)
# test_request_stock = [[100, 1200], [199, 1000], [500, 1000], [100, 1400]]
# queue = [[6, 2, 200, 3900, 4700], [9, 2, 300, 2500, 3600], [18, 3, 120, 4500, 4700]]
# [25, 1, 500], [42, 0, 300], [58, 0, 500], [75, 3, 1600]]

# current_queue, queue = pdc.go_production(1, queue)
# print(current_queue)
# print(queue)

# while dealing_variant := pdc.order_queue_prior_variant(queue, test_stock_standard, test_request_stock, test_min_batch):
#
#     print(dealing_variant)
#     test_request_stock[dealing_variant] = [0, test_stock_standard[dealing_variant]]
#     print(test_request_stock)
# queue = []
# for order in range(len(test_order)):
#     if order // 2 == 0:
#         del queue[0]
#     queue.append([order, test_order[order][1], test_order[order][2]])
#     print(queue)

test_dml = pdc.dml_pull_production(test_order, test_dml_process_time_array, test_dml_reconfiguring_time,
                                   profit_time_grade, 10, 2)
print(test_dml)

# go_production_order, queue = dml.go_production(2, queue)
#
# queue = aid.add_empty_column(queue)
# print(queue)


# test_batch_expand_ratio = 5

# variant_waiting = [[3, 1641863419], [4, 425863419], [1, 1641863419], [0, 1641863419], [2, 1641863419]]
# low_location = aid.min_location(variant_waiting)
# variant_waiting = dml.update_variant_waiting_priority(variant_waiting)
# print(variant_waiting)
# del(variant_waiting[1])

# min_b = dml.min_batch(test_dml_process_time_array, test_dml_reconfiguring_time, test_batch_expand_ratio)
# stock_s , rqNstk = dml.pull_dml_stock_initialise(min_b,2)
#
# print(stock_s)
# print(rqNstk)


#
# print(test_dml)

# aid.csv_export("ref.cvs", test_order)

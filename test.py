import DML_Construction as dml
import csv
import pickle
import Aid_Function_Blocks as aid
import Production_Simulation as pdc
import Massive_Simulation as ms

print("Here we are")

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

# test_order = [[52993, 5, 123], [103087, 2, 351], [109080, 3, 48], [161163, 3, 43], [161900, 6, 202], [184491, 5, 126], [197074, 1, 137], [218001, 6, 238], [252283, 2, 349], [268207, 5, 113], [273326, 2, 363], [283750, 5, 127], [322205, 5, 112], [328141, 3, 52], [503789, 1, 122], [560804, 2, 318], [564626, 3, 55], [613048, 4, 113], [798144, 0, 516], [808730, 0, 518], [914191, 3, 47], [926156, 3, 57], [1036230, 3, 58], [1058421, 6, 251], [1095587, 2, 377], [1131722, 6, 216], [1138393, 4, 91], [1272175, 5, 117], [1336161, 3, 58], [1363653, 0, 498], [1450963, 4, 105], [1451108, 2, 387], [1464768, 1, 122], [1527499, 1, 126], [1643177, 0, 472], [1662176, 6, 220], [1670499, 0, 519], [1821188, 2, 345], [1839470, 5, 108], [1893359, 1, 130], [1916454, 1, 127], [1932235, 4, 126], [1958080, 2, 388], [1981461, 5, 117], [2135607, 1, 128], [2264337, 6, 234], [2422495, 5, 129], [2455756, 0, 510], [2552118, 0, 498], [2585557, 4, 109], [2662718, 2, 370], [2728540, 1, 138], [2741868, 6, 257], [2938979, 1, 112], [2974571, 1, 126], [3038737, 4, 98], [3040431, 6, 249], [3098643, 1, 120], [3101255, 3, 54], [3115154, 5, 109], [3142693, 0, 498], [3205502, 2, 368], [3263781, 3, 42], [3271321, 5, 120], [3304971, 3, 57], [3311882, 4, 118], [3324735, 5, 136], [3330282, 2, 390], [3418961, 0, 499], [3427882, 0, 506], [3434923, 0, 491], [3465402, 1, 99], [3498063, 1, 137], [3521957, 3, 38], [3532724, 5, 127], [3547293, 6, 219], [3589737, 4, 111], [3613080, 1, 123], [3660727, 4, 100], [3665539, 6, 220], [3793756, 0, 515], [3813056, 5, 120], [3814291, 2, 386], [3838773, 2, 346], [3855571, 4, 110], [3875051, 6, 227], [3964593, 6, 286], [3978216, 4, 126], [3989350, 3, 49], [4022892, 5, 136], [4040396, 5, 108], [4065358, 1, 136], [4192963, 5, 116], [4323929, 5, 110], [4347682, 3, 58], [4351156, 4, 120], [4374959, 4, 117], [4446024, 5, 117], [4571741, 4, 103], [4654551, 1, 129], [4689194, 3, 48], [4692530, 3, 43], [4725904, 6, 208], [4744090, 2, 401], [4816372, 0, 474], [4847686, 0, 478], [4854436, 5, 115], [4873109, 2, 347], [4895287, 4, 105], [4913497, 3, 46], [4917699, 5, 144], [4932438, 2, 371], [4949034, 2, 370], [4971495, 3, 62], [4992309, 4, 120], [5026015, 4, 106], [5039970, 4, 116], [5040273, 6, 242], [5093690, 6, 236], [5105758, 6, 222], [5128923, 3, 56], [5203524, 4, 102], [5230261, 5, 117], [5326127, 3, 56], [5350815, 4, 124], [5355608, 0, 494], [5387183, 1, 118], [5415394, 2, 348], [5505748, 2, 396], [5522535, 6, 234], [5652143, 3, 60], [5820456, 5, 109], [5864485, 6, 213], [5888184, 2, 366], [5942726, 6, 237], [6027009, 1, 133], [6064190, 0, 519], [6081326, 4, 121], [6160445, 2, 378], [6187908, 2, 360], [6294486, 0, 480], [6304984, 1, 120], [6327308, 6, 247], [6362153, 0, 486], [6462014, 5, 118], [6549795, 6, 239], [6604829, 4, 121], [6614569, 5, 106], [6650846, 4, 118], [6698165, 1, 116], [6714326, 6, 245], [6798257, 3, 54], [6816319, 5, 119], [6826981, 3, 59], [6873541, 0, 514], [6911577, 5, 109], [6937643, 1, 121], [6941017, 3, 40], [6964045, 6, 226], [7021514, 5, 89], [7113348, 1, 123], [7138227, 3, 42], [7242301, 3, 60], [7296411, 4, 104], [7307496, 4, 100], [7360461, 2, 355], [7375043, 5, 122], [7377785, 1, 130], [7394332, 4, 107], [7446614, 0, 494], [7485971, 2, 370], [7528407, 5, 105], [7534575, 0, 494], [7613211, 5, 117], [7641274, 5, 125], [7650860, 6, 232], [7665138, 6, 272], [7671533, 4, 118], [7715661, 0, 522], [7716170, 4, 101], [7734194, 4, 105], [7785676, 3, 38], [7791892, 0, 473], [7812741, 1, 122], [7837674, 0, 490], [7884307, 2, 394], [7888130, 4, 85], [7899622, 3, 49], [7921822, 4, 119], [8005752, 5, 120], [8054808, 3, 46], [8073163, 1, 140], [8095711, 1, 119], [8105852, 0, 490], [8175511, 2, 357], [8182034, 4, 95], [8190469, 4, 114], [8280776, 6, 231], [8315582, 4, 98], [8331978, 1, 135], [8351273, 5, 117], [8371454, 6, 205], [8396697, 4, 126], [8422650, 0, 471], [8500175, 6, 246], [8510649, 2, 386], [8644680, 0, 542], [8654576, 1, 119], [8693110, 3, 61], [8875552, 6, 227], [8910740, 6, 228], [8969919, 1, 111], [9036633, 5, 113], [9040124, 4, 103], [9091032, 3, 53], [9295762, 3, 53], [9340496, 0, 530], [9366778, 2, 403], [9392758, 1, 124], [9404537, 4, 95], [9523267, 5, 113], [9541596, 0, 506], [9543670, 0, 470], [9547370, 0, 494], [9549546, 3, 53], [9582446, 4, 111], [9584592, 1, 107], [9643497, 2, 365], [9657296, 2, 392], [9664493, 0, 436], [9675653, 1, 105], [9709797, 5, 101], [9720880, 4, 125], [9737969, 3, 40], [9759463, 3, 49], [9763743, 3, 61], [9838793, 3, 54], [9873996, 6, 247], [10004032, 2, 361], [10055136, 6, 251], [10073489, 3, 58], [10103398, 5, 122], [10140437, 5, 115], [10150904, 6, 244], [10195094, 1, 134], [10297274, 3, 57], [10331480, 5, 121], [10374492, 4, 90], [10487416, 4, 99], [10517394, 6, 230], [10589174, 2, 366], [10661422, 3, 54], [10690941, 3, 55], [10713627, 2, 372], [10738608, 6, 210], [10777868, 0, 461], [10779248, 1, 115], [10784836, 1, 134], [10834908, 2, 374], [10875418, 4, 128], [10913500, 2, 325], [10923037, 0, 533], [11003391, 1, 142], [11016214, 3, 45], [11031619, 1, 121], [11066767, 0, 503], [11172830, 5, 144], [11207162, 0, 477], [11256706, 3, 53], [11273074, 5, 141], [11383198, 3, 49], [11453816, 3, 60], [11500309, 3, 53], [11514018, 4, 99], [11547288, 2, 394], [11615189, 4, 123], [11630616, 3, 63], [11634744, 2, 363], [11692979, 2, 385], [11721236, 2, 374], [11737730, 1, 98], [11775806, 6, 224], [11780352, 0, 485], [11789715, 2, 372], [11801944, 5, 104], [11802969, 2, 365], [11806937, 2, 376], [11857967, 5, 115], [11874695, 3, 58], [11937557, 5, 137], [11940711, 0, 533], [12131378, 3, 52], [12143205, 6, 239], [12152256, 3, 57], [12184387, 6, 250], [12243648, 5, 137], [12452213, 6, 234], [12508025, 1, 102], [12578241, 4, 114], [12579541, 4, 122], [12602146, 2, 347], [12625403, 3, 47], [12633647, 0, 559], [12684104, 1, 136], [12767583, 5, 101], [12789255, 3, 51], [12810316, 2, 372], [12812485, 3, 48], [12825224, 0, 498], [12835304, 5, 141], [12866349, 6, 248], [12884318, 1, 138], [12913521, 6, 218], [12977002, 3, 57], [13108629, 4, 102], [13129161, 0, 523], [13158674, 1, 111], [13195980, 4, 106], [13286773, 0, 472], [13372803, 0, 514], [13428580, 5, 132], [13443097, 4, 89], [13472435, 6, 221], [13493237, 1, 101], [13529619, 6, 240], [13558217, 1, 135], [13584604, 4, 110], [13683390, 1, 126], [13693187, 6, 245], [13736397, 1, 125], [13751806, 0, 525], [13771150, 1, 115], [13792397, 5, 154], [13832410, 6, 235], [13844270, 2, 361], [13867441, 6, 230], [13928819, 2, 391], [13962178, 0, 478], [13990306, 3, 56], [14013577, 2, 355], [14016202, 3, 57], [14025659, 2, 405], [14035667, 0, 465], [14046744, 6, 251], [14082544, 4, 117], [14098188, 5, 125], [14100404, 3, 57], [14101912, 0, 525], [14124639, 0, 486], [14146185, 5, 135], [14167852, 3, 46], [14192536, 0, 517], [14212146, 6, 204], [14364973, 2, 363], [14435575, 3, 58], [14500497, 0, 491], [14714614, 6, 207], [14726885, 2, 359], [14741460, 5, 106], [14803804, 6, 233], [14862971, 3, 48], [14895882, 5, 124], [14994614, 5, 113], [15002896, 1, 134], [15018484, 5, 121], [15066002, 6, 202], [15070303, 6, 239], [15085937, 4, 111], [15137595, 6, 218], [15139719, 0, 470], [15247731, 3, 48], [15290355, 2, 365], [15378862, 3, 50], [15428448, 5, 123], [15466559, 1, 113], [15483382, 1, 126], [15514941, 3, 52], [15542052, 0, 512], [15553219, 6, 241], [15581805, 6, 249], [15680371, 2, 370], [15771834, 5, 137], [15795547, 0, 502], [15804907, 4, 98], [15817109, 6, 205], [15893682, 5, 129], [16165088, 0, 491], [16239221, 5, 112], [16262304, 0, 469], [16330692, 4, 119], [16350408, 0, 512], [16358595, 0, 467], [16388596, 3, 61], [16412995, 4, 104], [16497809, 5, 108], [16512651, 6, 260], [16596125, 0, 496], [16598969, 0, 516], [16642892, 3, 54], [16671435, 0, 487], [16717945, 0, 501], [16730275, 0, 518], [16746195, 2, 363], [16782086, 6, 255], [16797232, 1, 132], [16817034, 2, 390], [16817926, 1, 115], [16916997, 3, 51], [16917201, 4, 93], [16938792, 0, 514], [16968340, 4, 102], [16985264, 2, 378], [17045277, 0, 487], [17053153, 5, 108], [17074541, 2, 343], [17097788, 6, 210], [17137676, 3, 55], [17155133, 0, 489], [17177504, 5, 104], [17222669, 5, 121], [17307998, 6, 244], [17330506, 1, 145], [17369642, 1, 121], [17394963, 6, 223], [17399283, 1, 116], [17399719, 3, 56], [17470236, 0, 507], [17493387, 4, 108], [17495174, 4, 108], [17510899, 1, 115], [17514971, 2, 361], [17602665, 6, 218], [17679574, 6, 267], [17708650, 3, 47], [17711957, 4, 94], [17765211, 3, 49], [17808487, 6, 227], [17928049, 6, 260], [17951865, 3, 53], [17967865, 4, 102], [17984795, 1, 135], [18248296, 5, 101], [18279379, 6, 234], [18311643, 0, 474], [18328123, 5, 106], [18376456, 2, 354], [18461130, 1, 108], [18513259, 6, 214], [18541905, 2, 420], [18552582, 2, 378], [18755304, 1, 120], [18796849, 2, 379], [18797126, 1, 113], [18817990, 1, 119], [18882982, 5, 122], [18939335, 6, 225], [18968633, 4, 116], [19035341, 6, 227], [19080119, 0, 525], [19101272, 5, 122], [19356320, 2, 353], [19393626, 2, 362], [19446920, 6, 235], [19471915, 6, 207], [19489931, 3, 45], [19502588, 4, 115], [19550653, 5, 116], [19574680, 1, 133], [19601791, 2, 376], [19606836, 1, 114], [19607850, 6, 241], [19662223, 0, 506], [19722330, 4, 104], [19732970, 6, 256], [19751800, 5, 123], [19794279, 0, 533], [19831728, 3, 36], [19839084, 3, 50], [19847370, 1, 109], [19850430, 1, 132], [19902843, 0, 475], [19915337, 2, 366], [19989333, 4, 112], [20030637, 6, 263], [20035594, 3, 47], [20045605, 6, 252], [20090869, 2, 377], [20109009, 2, 359], [20117925, 2, 363], [20169275, 0, 520], [20212651, 6, 247], [20234444, 0, 508], [20247651, 1, 131], [20259135, 4, 94], [20312017, 6, 227], [20330219, 3, 44], [20441062, 4, 119], [20479629, 2, 373], [20511183, 2, 377], [20562046, 1, 122], [20566570, 5, 95], [20573542, 5, 130], [20591737, 5, 109], [20690643, 6, 224], [20703316, 0, 492], [20709837, 4, 99], [20735796, 4, 98], [20778732, 5, 111], [20815480, 6, 241], [20847306, 6, 245], [20894111, 2, 380], [21051085, 4, 109], [21088971, 0, 492], [21178934, 0, 502], [21195847, 1, 118], [21213235, 5, 139], [21225977, 6, 247], [21227535, 4, 110], [21272693, 4, 107], [21330519, 0, 469], [21364202, 3, 49], [21462329, 0, 485], [21490286, 0, 472], [21556851, 2, 372], [21568277, 3, 52], [21570664, 4, 100], [21593895, 1, 133], [21597937, 6, 226], [21636938, 5, 118], [21639082, 2, 387], [21711061, 5, 123], [21762018, 0, 466], [21813090, 1, 117], [21858558, 4, 113], [21893535, 0, 550], [21987234, 0, 511], [21991379, 0, 522], [22005169, 5, 121], [22071474, 6, 253], [22107756, 2, 357], [22138845, 6, 241], [22229874, 5, 111], [22272368, 4, 88], [22289255, 3, 43], [22308560, 0, 524], [22316698, 4, 104], [22366888, 4, 126], [22399322, 0, 497], [22425879, 3, 60], [22447126, 2, 362], [22465438, 0, 494], [22484408, 6, 249], [22554212, 0, 458], [22554275, 2, 316], [22615668, 3, 33], [22738617, 6, 243], [22784951, 0, 530], [22806194, 1, 120], [22816068, 0, 503], [22830977, 2, 353], [22848289, 4, 128], [22862128, 5, 130], [22896021, 6, 220], [22972658, 3, 41], [22979275, 1, 126], [23001697, 6, 225], [23007853, 1, 140], [23058913, 4, 112], [23064668, 6, 258], [23094191, 2, 374], [23098763, 0, 491], [23111885, 3, 50], [23148211, 5, 106], [23156756, 3, 61], [23158660, 0, 509], [23332825, 3, 56], [23364427, 5, 106], [23459662, 5, 116], [23655179, 0, 475], [23670885, 3, 38], [23673868, 1, 125], [23756239, 1, 147], [23757796, 5, 130], [23785296, 6, 257], [23804861, 0, 482], [23805305, 0, 477], [23841916, 4, 105], [23847597, 6, 241], [23883541, 5, 140], [23908145, 0, 499], [23947262, 2, 375], [24079507, 6, 242], [24091905, 5, 129], [24209852, 1, 126], [24210141, 2, 375], [24255453, 3, 40], [24367838, 5, 115], [24387699, 2, 397], [24469728, 0, 510], [24473954, 1, 129], [24564655, 0, 513], [24586337, 5, 105], [24731986, 1, 150], [24805321, 1, 109], [24822585, 3, 43], [24822667, 6, 258], [24846690, 3, 53], [24897068, 6, 217], [24912686, 6, 211], [24913200, 4, 106], [24916501, 4, 117], [24954492, 4, 118], [25026186, 6, 218], [25037580, 6, 241], [25046836, 6, 218], [25050875, 1, 107], [25073784, 3, 47], [25086176, 0, 479], [25098350, 6, 236], [25169094, 3, 57], [25201103, 3, 52], [25207840, 1, 131], [25230323, 6, 259], [25294619, 1, 129], [25304880, 0, 468], [25356621, 6, 209], [25467369, 0, 499], [25542874, 0, 470], [25558258, 0, 521], [25591528, 2, 352], [25616659, 4, 107], [25650515, 0, 481], [25656108, 5, 121], [25665964, 0, 542], [25674999, 1, 127], [25678686, 6, 225], [25718020, 2, 367], [25733325, 0, 493], [25738916, 0, 476], [25769734, 1, 111], [25796450, 4, 98], [25828865, 2, 366], [25834560, 0, 490], [25870327, 5, 107], [25918379, 2, 345], [25927355, 5, 103], [26088439, 5, 124], [26091715, 4, 124], [26126575, 2, 358], [26144424, 5, 103], [26174025, 4, 101], [26175740, 3, 45], [26200101, 0, 476], [26226886, 1, 111], [26248961, 5, 128], [26322675, 2, 396], [26324446, 0, 512], [26374887, 3, 43], [26428198, 6, 223], [26472001, 3, 46], [26489962, 3, 43], [26516190, 5, 137], [26520851, 0, 516], [26614511, 0, 479], [26639278, 4, 99], [26664784, 0, 495], [26682438, 5, 106], [26728482, 0, 486], [26827445, 6, 230], [26837855, 2, 345], [26873906, 4, 122], [26885898, 1, 131], [26893564, 4, 101], [26936478, 2, 365], [27001494, 1, 111], [27056435, 3, 57], [27073929, 2, 358], [27103166, 4, 107], [27104117, 5, 107], [27118772, 0, 521], [27184772, 5, 112], [27217337, 0, 490], [27234524, 2, 366], [27276405, 4, 92], [27277349, 1, 124], [27353313, 6, 250], [27409522, 2, 393], [27438642, 0, 510], [27458758, 0, 498], [27473912, 3, 51], [27484888, 3, 63], [27503655, 2, 371], [27541705, 6, 222], [27590038, 2, 416], [27596197, 5, 127], [27603120, 5, 104], [27655354, 5, 115], [27694293, 6, 244], [27705151, 6, 224], [27737958, 4, 99], [27750061, 0, 473], [27774449, 2, 363], [27819290, 5, 127], [27835925, 5, 121], [27861774, 6, 218], [27876189, 5, 129], [27944808, 2, 379], [28003049, 3, 53], [28011082, 3, 50], [28033544, 2, 357], [28092990, 0, 506], [28122341, 5, 130], [28122870, 4, 106], [28151610, 6, 231], [28160041, 6, 257], [28197155, 6, 255], [28218924, 2, 361], [28274127, 6, 199], [28280883, 3, 39], [28325118, 3, 47], [28379200, 0, 485], [28519022, 1, 140], [28519039, 3, 60], [28526300, 6, 247], [28575765, 0, 525], [28587549, 6, 230], [28595279, 5, 122], [28613437, 6, 225], [28623367, 3, 51], [28642209, 6, 248], [28652342, 3, 45], [28688027, 4, 114], [28733326, 5, 128], [28742531, 6, 233], [28766646, 0, 556], [28770380, 2, 321], [28787128, 2, 331], [28802537, 6, 249], [28825034, 6, 233], [28833031, 1, 124], [28836873, 2, 394], [28861102, 6, 235], [28916971, 5, 137], [28924790, 0, 475], [28946463, 5, 123], [28972115, 4, 107], [29010081, 2, 389], [29050230, 6, 225], [29079644, 2, 382], [29094356, 6, 230], [29101523, 6, 211], [29259991, 3, 48], [29275172, 3, 41], [29293282, 0, 504], [29294256, 1, 116], [29316438, 4, 112], [29385183, 0, 472], [29392642, 4, 114], [29406002, 2, 335], [29551226, 3, 49], [29718023, 6, 222], [29728580, 6, 225], [29816530, 1, 120], [29911288, 4, 112], [29937127, 6, 237], [30027662, 6, 235], [30046016, 6, 239], [30081507, 0, 498], [30083316, 0, 501], [30256041, 5, 113], [30265153, 3, 42], [30278450, 6, 238], [30279131, 1, 107], [30324125, 2, 403], [30325517, 4, 109], [30447736, 4, 102], [30489726, 5, 127], [30506586, 1, 111], [30528176, 2, 402], [30593218, 0, 496], [30640182, 4, 91], [30691276, 2, 344], [30700467, 3, 52], [30743305, 0, 526], [30768164, 4, 103], [30816775, 6, 210], [30830079, 2, 368], [30917551, 2, 391], [30921131, 4, 113], [30995600, 1, 111], [31000243, 5, 117], [31015311, 4, 86], [31054620, 3, 73], [31146801, 6, 246], [31269382, 1, 101], [31343009, 6, 224], [31349598, 2, 386], [31394771, 4, 104], [31418373, 5, 119], [31518797, 5, 110]]
# [[447,    0, 2210], [2134,   3, 2390], [5690,   1, 3000], [7598,   0, 2210], [12413,  0, 2320],
#           [15224,  1, 2860], [30804,  3, 2540], [43747,  2, 2090], [50034,  2, 1670], [55950,  0, 2180],
#           [58849,  3, 2450], [59792,  0, 1680], [77684,  0, 2020], [89686,  3, 2280], [94536,  2, 1720],
#           [107695, 3, 2350], [112531, 1, 2810], [119548, 0, 2050], [120227, 2, 2310], [123640, 1, 2770],
#           [125949, 0, 1900], [126690, 3, 2230], [132125, 3, 2550], [141378, 1, 3140], [145169, 3, 2210],
#           [147391, 0, 2090], [148028, 1, 2950], [156016, 2, 2000], [164845, 1, 3170], [167780, 0, 2330]]

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

# test_dml_process_time_array = [22.89, 15.98, 23.68, 18.490000000000002, 24.54, 17.63, 22.03]
# test_dml_reconfiguring_time = [230, 186, 152, 110, 59, 286, 144]
#
# test_min_batch = [1000, 800, 500, 1500]
# test_stock_ratio = 2
# test_stock_standard, test_request_stock = dml.pull_dml_stock_initialise(test_min_batch, test_stock_ratio)
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

# test_dml = pdc.dml_pull_production(test_order, test_dml_process_time_array, test_dml_reconfiguring_time,
#                                    profit_time_grade, 10, 2)
# aid.csv_export("order.csv", test_dml)

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

import pytest
import get_coordinates


def test_get_coordinates():
    formula = "3x^2 + 4x + 2"

    assert get_coordinates.get_coordinates(-5, 5, -5, 5, formula) == (
        [
            -1.8600000000000638,
            -1.8500000000000638,
            -1.8400000000000638,
            -1.8300000000000638,
            -1.8200000000000638,
            -1.8100000000000638,
            -1.8000000000000638,
            -1.7900000000000638,
            -1.7800000000000638,
            -1.7700000000000637,
            -1.7600000000000637,
            -1.7500000000000637,
            -1.7400000000000637,
            -1.7300000000000637,
            -1.7200000000000637,
            -1.7100000000000637,
            -1.7000000000000637,
            -1.6900000000000637,
            -1.6800000000000637,
            -1.6700000000000637,
            -1.6600000000000636,
            -1.6500000000000636,
            -1.6400000000000636,
            -1.6300000000000636,
            -1.6200000000000636,
            -1.6100000000000636,
            -1.6000000000000636,
            -1.5900000000000636,
            -1.5800000000000636,
            -1.5700000000000636,
            -1.5600000000000636,
            -1.5500000000000635,
            -1.5400000000000635,
            -1.5300000000000635,
            -1.5200000000000635,
            -1.5100000000000635,
            -1.5000000000000635,
            -1.4900000000000635,
            -1.4800000000000635,
            -1.4700000000000635,
            -1.4600000000000635,
            -1.4500000000000635,
            -1.4400000000000635,
            -1.4300000000000634,
            -1.4200000000000634,
            -1.4100000000000634,
            -1.4000000000000634,
            -1.3900000000000634,
            -1.3800000000000634,
            -1.3700000000000634,
            -1.3600000000000634,
            -1.3500000000000634,
            -1.3400000000000634,
            -1.3300000000000634,
            -1.3200000000000633,
            -1.3100000000000633,
            -1.3000000000000633,
            -1.2900000000000633,
            -1.2800000000000633,
            -1.2700000000000633,
            -1.2600000000000633,
            -1.2500000000000633,
            -1.2400000000000633,
            -1.2300000000000633,
            -1.2200000000000633,
            -1.2100000000000632,
            -1.2000000000000632,
            -1.1900000000000632,
            -1.1800000000000632,
            -1.1700000000000632,
            -1.1600000000000632,
            -1.1500000000000632,
            -1.1400000000000632,
            -1.1300000000000632,
            -1.1200000000000632,
            -1.1100000000000632,
            -1.1000000000000631,
            -1.0900000000000631,
            -1.0800000000000631,
            -1.0700000000000631,
            -1.0600000000000631,
            -1.050000000000063,
            -1.040000000000063,
            -1.030000000000063,
            -1.020000000000063,
            -1.010000000000063,
            -1.000000000000063,
            -0.990000000000063,
            -0.980000000000063,
            -0.970000000000063,
            -0.960000000000063,
            -0.950000000000063,
            -0.940000000000063,
            -0.930000000000063,
            -0.920000000000063,
            -0.910000000000063,
            -0.900000000000063,
            -0.890000000000063,
            -0.880000000000063,
            -0.870000000000063,
            -0.8600000000000629,
            -0.8500000000000629,
            -0.8400000000000629,
            -0.8300000000000629,
            -0.8200000000000629,
            -0.8100000000000629,
            -0.8000000000000629,
            -0.7900000000000629,
            -0.7800000000000629,
            -0.7700000000000629,
            -0.7600000000000628,
            -0.7500000000000628,
            -0.7400000000000628,
            -0.7300000000000628,
            -0.7200000000000628,
            -0.7100000000000628,
            -0.7000000000000628,
            -0.6900000000000628,
            -0.6800000000000628,
            -0.6700000000000628,
            -0.6600000000000628,
            -0.6500000000000627,
            -0.6400000000000627,
            -0.6300000000000627,
            -0.6200000000000627,
            -0.6100000000000627,
            -0.6000000000000627,
            -0.5900000000000627,
            -0.5800000000000627,
            -0.5700000000000627,
            -0.5600000000000627,
            -0.5500000000000627,
            -0.5400000000000627,
            -0.5300000000000626,
            -0.5200000000000626,
            -0.5100000000000626,
            -0.5000000000000626,
            -0.4900000000000626,
            -0.4800000000000626,
            -0.4700000000000626,
            -0.4600000000000626,
            -0.45000000000006257,
            -0.44000000000006256,
            -0.43000000000006255,
            -0.42000000000006255,
            -0.41000000000006254,
            -0.40000000000006253,
            -0.3900000000000625,
            -0.3800000000000625,
            -0.3700000000000625,
            -0.3600000000000625,
            -0.3500000000000625,
            -0.3400000000000625,
            -0.33000000000006247,
            -0.32000000000006246,
            -0.31000000000006245,
            -0.30000000000006244,
            -0.29000000000006243,
            -0.2800000000000624,
            -0.2700000000000624,
            -0.2600000000000624,
            -0.2500000000000624,
            -0.24000000000006239,
            -0.23000000000006238,
            -0.22000000000006237,
            -0.21000000000006236,
            -0.20000000000006235,
            -0.19000000000006234,
            -0.18000000000006233,
            -0.17000000000006232,
            -0.16000000000006231,
            -0.1500000000000623,
            -0.1400000000000623,
            -0.1300000000000623,
            -0.12000000000006229,
            -0.1100000000000623,
            -0.1000000000000623,
            -0.09000000000006231,
            -0.08000000000006231,
            -0.07000000000006232,
            -0.060000000000062316,
            -0.050000000000062314,
            -0.04000000000006231,
            -0.03000000000006231,
            -0.020000000000062308,
            -0.010000000000062308,
            -6.230779781013496e-14,
            0.009999999999937692,
            0.019999999999937693,
            0.029999999999937695,
            0.039999999999937697,
            0.0499999999999377,
            0.0599999999999377,
            0.0699999999999377,
            0.07999999999993769,
            0.08999999999993769,
            0.09999999999993768,
            0.10999999999993768,
            0.11999999999993767,
            0.12999999999993767,
            0.13999999999993767,
            0.14999999999993768,
            0.1599999999999377,
            0.1699999999999377,
            0.1799999999999377,
            0.18999999999993772,
            0.19999999999993773,
            0.20999999999993774,
            0.21999999999993775,
            0.22999999999993775,
            0.23999999999993776,
            0.24999999999993777,
            0.2599999999999378,
            0.2699999999999378,
            0.2799999999999378,
            0.2899999999999378,
            0.2999999999999378,
            0.3099999999999378,
            0.31999999999993783,
            0.32999999999993784,
            0.33999999999993785,
            0.34999999999993786,
            0.35999999999993787,
            0.3699999999999379,
            0.3799999999999379,
            0.3899999999999379,
            0.3999999999999379,
            0.4099999999999379,
            0.4199999999999379,
            0.42999999999993793,
            0.43999999999993794,
            0.44999999999993795,
            0.45999999999993796,
            0.46999999999993797,
            0.479999999999938,
            0.489999999999938,
            0.499999999999938,
            0.509999999999938,
            0.519999999999938,
            0.529999999999938,
        ],
        [
            4.938800000000457,
            4.867500000000454,
            4.796800000000449,
            4.726700000000446,
            4.657200000000442,
            4.588300000000438,
            4.520000000000433,
            4.45230000000043,
            4.385200000000426,
            4.318700000000422,
            4.252800000000418,
            4.187500000000413,
            4.12280000000041,
            4.058700000000406,
            3.995200000000402,
            3.9323000000003985,
            3.8700000000003936,
            3.808300000000391,
            3.7472000000003867,
            3.686700000000383,
            3.6268000000003795,
            3.5675000000003765,
            3.508800000000372,
            3.450700000000367,
            3.3932000000003644,
            3.336300000000361,
            3.2800000000003564,
            3.224300000000352,
            3.169200000000348,
            3.1147000000003446,
            3.0608000000003406,
            3.007500000000337,
            2.9548000000003327,
            2.902700000000329,
            2.8512000000003255,
            2.8003000000003215,
            2.750000000000318,
            2.700300000000314,
            2.6512000000003093,
            2.602700000000307,
            2.554800000000302,
            2.507500000000298,
            2.4608000000002948,
            2.4147000000002903,
            2.369200000000287,
            2.3243000000002834,
            2.280000000000279,
            2.2363000000002753,
            2.193200000000272,
            2.150700000000268,
            2.1088000000002634,
            2.06750000000026,
            2.0268000000002555,
            1.9867000000002522,
            1.9472000000002483,
            1.9083000000002448,
            1.8700000000002408,
            1.8323000000002372,
            1.795200000000233,
            1.7587000000002293,
            1.722800000000225,
            1.6875000000002212,
            1.6528000000002177,
            1.6187000000002136,
            1.58520000000021,
            1.5523000000002067,
            1.520000000000202,
            1.4883000000001987,
            1.4572000000001948,
            1.4267000000001913,
            1.3968000000001872,
            1.3675000000001836,
            1.3388000000001794,
            1.3107000000001756,
            1.2832000000001713,
            1.2563000000001683,
            1.2300000000001643,
            1.2043000000001602,
            1.179200000000157,
            1.1547000000001528,
            1.130800000000149,
            1.1075000000001456,
            1.0848000000001417,
            1.0627000000001372,
            1.041200000000134,
            1.0203000000001303,
            1.0000000000001261,
            0.9803000000001223,
            0.9612000000001188,
            0.9427000000001149,
            0.9248000000001109,
            0.9075000000001072,
            0.8908000000001031,
            0.8747000000000993,
            0.8592000000000959,
            0.844300000000092,
            0.830000000000088,
            0.8163000000000844,
            0.8032000000000803,
            0.7907000000000766,
            0.7788000000000732,
            0.7675000000000693,
            0.7568000000000654,
            0.7467000000000619,
            0.7372000000000578,
            0.7283000000000541,
            0.7200000000000504,
            0.7123000000000466,
            0.7052000000000427,
            0.698700000000039,
            0.6928000000000352,
            0.6875000000000315,
            0.6828000000000278,
            0.6787000000000241,
            0.6752000000000202,
            0.6723000000000163,
            0.6700000000000126,
            0.6683000000000088,
            0.6672000000000049,
            0.6667000000000014,
            0.6667999999999976,
            0.6674999999999938,
            0.6687999999999898,
            0.6706999999999861,
            0.6731999999999825,
            0.6762999999999788,
            0.6799999999999748,
            0.684299999999971,
            0.6891999999999674,
            0.6946999999999637,
            0.7007999999999599,
            0.707499999999956,
            0.7147999999999524,
            0.7226999999999486,
            0.7311999999999448,
            0.7402999999999411,
            0.7499999999999374,
            0.7602999999999336,
            0.7711999999999297,
            0.782699999999926,
            0.7947999999999225,
            0.8074999999999186,
            0.8207999999999149,
            0.8346999999999112,
            0.8491999999999074,
            0.8642999999999037,
            0.8799999999999,
            0.8962999999998962,
            0.9131999999998925,
            0.9306999999998888,
            0.9487999999998848,
            0.9674999999998812,
            0.9867999999998776,
            1.0066999999998738,
            1.02719999999987,
            1.0482999999998663,
            1.0699999999998626,
            1.092299999999859,
            1.1151999999998552,
            1.1386999999998515,
            1.1627999999998477,
            1.1874999999998441,
            1.2127999999998402,
            1.2386999999998367,
            1.265199999999833,
            1.292299999999829,
            1.3199999999998253,
            1.3482999999998218,
            1.3771999999998181,
            1.4066999999998142,
            1.4367999999998107,
            1.4674999999998068,
            1.4987999999998032,
            1.5306999999997994,
            1.5631999999997956,
            1.596299999999792,
            1.629999999999788,
            1.6642999999997845,
            1.6991999999997807,
            1.734699999999777,
            1.7707999999997732,
            1.8074999999997694,
            1.8447999999997657,
            1.882699999999762,
            1.9211999999997582,
            1.9602999999997546,
            1.9999999999997509,
            2.040299999999747,
            2.0811999999997433,
            2.1226999999997394,
            2.164799999999736,
            2.2074999999997322,
            2.250799999999728,
            2.2946999999997244,
            2.339199999999721,
            2.384299999999717,
            2.4299999999997133,
            2.4762999999997097,
            2.5231999999997057,
            2.570699999999702,
            2.6187999999996983,
            2.667499999999695,
            2.716799999999691,
            2.7666999999996875,
            2.8171999999996835,
            2.86829999999968,
            2.919999999999676,
            2.9722999999996724,
            3.0251999999996686,
            3.078699999999665,
            3.132799999999661,
            3.187499999999658,
            3.242799999999654,
            3.2986999999996502,
            3.3551999999996465,
            3.412299999999643,
            3.469999999999639,
            3.5282999999996356,
            3.587199999999632,
            3.6466999999996283,
            3.7067999999996246,
            3.767499999999621,
            3.8287999999996174,
            3.8906999999996135,
            3.95319999999961,
            4.016299999999607,
            4.079999999999602,
            4.144299999999599,
            4.209199999999595,
            4.274699999999592,
            4.340799999999588,
            4.407499999999584,
            4.474799999999581,
            4.542699999999577,
            4.611199999999574,
            4.680299999999569,
            4.749999999999566,
            4.820299999999562,
            4.891199999999558,
            4.962699999999555,
        ],
    )

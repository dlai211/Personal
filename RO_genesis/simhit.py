from pynput.mouse import Controller, Button, Listener
import time

mouse = Controller()
pos_time = [
        [(848, 585), 22.37],
        [(1040, 433), 23.22],
        [(1043, 734), 24.17],
        [(655, 440), 25.10],
        [(651, 724), 25.94],
        [(848, 413), 26.77],
        [(1092, 590), 27.76],
        [(1043, 493), 28.2],
        [(662, 523), 29.1],
        [(662, 591), 29.49],
        [(950, 711), 30.31],
        [(817, 716), 31.24],
        [(870, 715), 32.17],
        [(953, 714), 33.10],
        [(955, 424), 34.04],
        [(710, 521), 34.91],
        [(690, 647), 35.25],
        [(857, 572), 36.15],
        [(647, 723), 37.07],
        [(699, 666), 37.99],
        [(758, 605), 38.78],
        [(827, 548), 39.8],
        [(1069, 718), 40.69],
        [(1012, 664), 41.56],
        [(951, 604), 42.5],
        [(877, 527), 42.93],
        [(710, 421), 43.26],
        [(782, 422), 44.30],
        [(856, 424), 45.14],
        [(928, 425), 46.0],
        [(855, 719), 47.06],
        [(855, 570), 47.81],
        [(662, 425), 48.79],
        [(759, 496), 49.16],
        [(1049, 423), 49.81],
        [(1049, 497), 50.6],
        [(1048, 424), 51.45],
        [(951, 426), 52.40],
        [(1051, 713), 53.26],
        [(1047, 616), 54.12],
        [(661, 421), 54.47],
        [(760, 521), 55.06],
        [(661, 710), 56.02],
        [(759, 617), 56.91],
        [(709, 713), 57.36],
        [(783, 713), 57.90],
        [(858, 715), 58.73],
        [(931, 713), 59.63],
        [(861, 591), 60.34],
        [(1066, 421), 61.18],
        [(1008, 480), 61.22],
        [(952, 541), 62.22],
        [(885, 598), 63.07],
        [(807, 483), 64.04],
        [(643, 429), 64.4],
        [(701, 675), 64.89],
        [(761, 619), 65.89],
        [(838, 544), 66.11],
        [(914, 620), 66.73],
        [(643, 660), 67.61],
        [(731, 635), 67.96],
        [(817, 537), 68.5],
        [(1067, 660), 69.4],
        [(983, 639), 69.68],
        [(895, 544), 70.31],
        [(860, 584), 71.2],
        [(648, 429), 71.57],
        [(705, 678), 72.12],
        [(761, 615), 73.05],
        [(837, 550), 73.32],
        [(913, 467), 73.96],
        [(913, 695), 74.83],
        [(954, 580), 75.1],
        [(761, 581), 75.55],
        [(914, 467), 75.6],
        [(917, 706), 76.57],
        [(951, 578), 76.9],
        [(859, 580), 77.56],
        [(1048, 435), 78.45],
        [(1050, 725), 79.3],
        [(665, 436), 80.23],
        [(664, 721), 81.16],
        [(857, 406), 81.5],
        [(1096, 584), 82.10],
        [(1049, 495), 82.26],
        [(667, 553), 82.60],
        [(667, 609), 83.1],
        [(953, 737), 83.71],
        [(822, 734), 84.35],
        [(880, 732), 84.5],
        [(953, 735), 85.55],
        [(957, 446), 86.12],
        [(715, 545), 86.78],
        [(696, 667), 86.92],
        [(859, 592), 87.72],
        [(652, 744), 87.82],
        [(766, 630), 88.1],
        [(706, 685), 88.2],
        [(1069, 746), 88.57],
        [(831, 571), 88.59],
        [(1013, 685), 89.28],
        [(954, 629), 89.54],
        [(877, 553), 90.4],
        [(714, 445), 90.5],
        [(786, 446), 91.12],
        [(859, 447), 91.37],
        [(930, 447), 92.0],
        [(859, 736), 92.25],
        [(857, 592), 93.16],
        [(669, 445), 93.25],
        [(762, 519), 93.75],
        [(1052, 446), 94.10],
        [(1048, 516), 94.79],
        [(1051, 447), 95.1],
        [(954, 448), 95.45],
        [(1050, 734), 96.1],
        [(1048, 640), 96.5],
        [(669, 452), 96.79],
        [(762, 540), 97.4],
        [(667, 735), 97.73],
        [(762, 638), 98.3],
        [(718, 737), 98.59],
        [(787, 734), 99.28],
        [(860, 736), 99.56],
        [(929, 734), 100.14],
        [(860, 595), 100.70],
        [(1072, 440), 100.87],
        [(1012, 495), 101.18],
        [(957, 551), 101.75],
        [(808, 495), 102.45],
        [(888, 612), 102.55],
        [(649, 439), 103.33],
        [(707, 686), 103.61],
        [(764, 632), 103.86],
        [(840, 552), 104.47],
        [(915, 627), 105.11],
        [(649, 668), 105.40],
        [(733, 648), 106.15],
        [(822, 551), 106.47],
        [(1070, 667), 107.12],
        [(984, 649), 107.55],
        [(898, 554), 107.85],
        [(862, 591), 108.5],
        [(649, 436), 109.],
        [(762, 631), 109.27],
        [(704, 690), 109.35],
        [(839, 552), 110.2],
        [(918, 473), 110.3],
        [(917, 705), 110.8],
        [(860, 446), 111.15],
        [(857, 736), 111.7],
        [(1011, 479), 112.12],
        [(1013, 706), 112.6],
        [(955, 593), 113.1],
        [(861, 592), 113.53],
        [(1052, 447), 114.13],
        [(1050, 737), 114,2],
        [(666, 446), 114.85],
        [(667, 738), 115.6],
        [(860, 420), 115.7],
        [(1098, 594), 116.52],
        [(667, 552), 116.89],
        [(1049, 498), 117.25],
        [(665, 609), 117.8],
        [(955, 734), 117.9],
        [(889, 730), 118.25],
        [(838, 727), 118.6],
        [(955, 738), 118.75],
        [(953, 451), 119.7],
        [(717, 544), 120.15],
        [(861, 593), 120.52],
        [(695, 666), 120.62],
        [(648, 745), 121.0],
        [(706, 684), 121.35],
        [(765, 627), 121.89],
        [(828, 572), 122.32],
        [(1070, 746), 123.],
        [(1010, 688), 123.24],
        [(957, 629), 123.5],
        [(876, 556), 124.],
        [(714, 448), 124.16],
        [(784, 448), 125.],
        [(931, 443), 125.38],
        [(859, 448), 125.57],
        [(858, 736), 125.82],
        [(859, 589), 126.3],
        [(670, 452), 126.37],
        [(1050, 446), 127.1],
        [(763, 519), 127.2],
        [(1055, 519), 127.3],
        [(1051, 444), 127.6],
        [(1052, 735), 128.62],
        [(1052, 641), 128.73],
        [(954, 444), 128.9],
        [(666, 450), 129.23],
        [(764, 546), 129.55],
        [(663, 733), 129.96],
        [(763, 636), 130.45],
        [(707, 731), 130.73],
        [(784, 732), 130.91],
        [(858, 732), 131.36],
        [(930, 733), 131.7],
        [(861, 588), 132.2],
        [(781, 515), 133.],
        [(982, 648), 133.4],
        [(1070, 668), 133.73],
        [(935, 516), 134.],
        [(860, 585), 134.5],
        [(651, 747), 134.97],
        [(723, 665), 135.6],
        [(784, 592), 135.89],
        [(859, 513), 136.05],
        [(933, 438), 136.45],
        [(857, 595), 136.73],
        [(649, 743), 137.37],
        [(716, 724), 137.69],
        [(763, 627), 138.05],
        [(830, 572), 138.65],
        [(1011, 688), 138.9],
        [(880, 552), 139.1],
        [(1068, 748), 139.2],
        [(953, 630), 139.53],
        [(858, 591), 143.8],
        [(764, 592), 144.52],
        [(955, 593), 145.1],
        [(878, 594), 150]


]
sta = time.time()
lag, lag2 = 0, 0
for i in range(len(pos_time)):

    mouse.position = pos_time[i][0]
    mouse.click(Button.left, 1)
    end = time.time()
    lag = end - sta
    #print(f'lag time {lag}')
    sleep_time = pos_time[i+1][1] - pos_time[i][1] - lag - lag2
    if sleep_time > 0:
        time.sleep(sleep_time)
    lag2 = time.time() - end - sleep_time
    #print(f'2nd lag {time.time() - end - sleep_time}')
    sta = time.time()

def return_joint_state(arm_num, joint_num):

    if arm_num == 'right_arm':
        right_joint_total=['joint_1_up','joint_1_down','joint_2_up','joint_2_down','joint_3_up','joint_3_down','joint_4_up','joint_4_down','joint_5_up','joint_5_down','joint_hand_out_low','joint_hand_inside_release']
        joint_num_state=right_joint_total[joint_num]
        if joint_num_state=='joint_1_up':
            return [1.5024168491363525, -1.5583857297897339, -1.5646002292633057, -0.030075587332248688, 0.47444334626197815, 0.28390926122665405, -1.4440211057662964]
        if joint_num_state=='joint_1_down':
            return [1.6778455972671509, -1.6296939849853516, -1.5798126459121704, -0.41235220432281494, 0.2887904644012451, 0.4886409640312195, -1.3165780305862427]
        if joint_num_state=='joint_2_up':
            return [1.092969536781311, -1.5380184650421143, -1.4573118686676025, 0.2626366913318634, 0.17969664931297302, 0.3638852536678314, -1.073843002319336]
        if joint_num_state=='joint_2_down':
            return [1.3363401889801025, -1.0898970365524292, -1.4443535804748535, 0.44336768984794617, 3.420609474182129, 0.9420353174209595, 3.018526554107666]
        if joint_num_state=='joint_3_up':
            return [1.5009297132492065, -1.011546015739441, -1.440324068069458, 0.5672059655189514, 3.490061044692993, 1.2173329591751099, 3.0692217350006104]
        if joint_num_state=='joint_3_down':
            return [1.5736968517303467, -1.0619909763336182, -1.5524935722351074, 0.45445170998573303, 3.3969733715057373, 1.1540648937225342, 3.0895192623138428]
        if joint_num_state=='joint_4_up':
            return [1.547721982,-0.975123584,-1.425058126,0.427137256,3.43200016,1.116520643,3.086297512]
        if joint_num_state=='joint_4_down':
            return [1.6134154797,-1.032587409,-1.5367376804,0.3015876412,3.3316938877,1.0310608149,3.1173522472]
        if joint_num_state=='joint_5_up':
            return [1.6798139811,-0.9578893185,-1.4970027208,0.4048714936,3.4262340069,1.2005531788,3.1135492325]
        if joint_num_state=='joint_5_down':
            return [1.7620639801,-1.0336602926,-1.6182199717,0.2667441964,3.315778017,1.1212291718,3.1433637142]
        if joint_num_state=='joint_hand_out_low':
            return [1.596020221710205, -0.7798439860343933, -1.2379815578460693, -0.14349110424518585, 3.9499971866607666, 0.8009695410728455, 2.5808541774749756]
        if joint_num_state=='joint_hand_inside_release':
            return[0.42854681611061096, -1.3110144138336182, -1.4462252855300903, 0.8245474696159363, 2.740112543106079, 0.45960697531700134, 3.49589467048645]

    if arm_num == 'left_arm':
        left_joint_total=['joint_1_up','joint_1_down','joint_2_up','joint_2_down','joint_3_up','joint_3_down','joint_4_up','joint_4_down','joint_5_up','joint_5_down','joint_hand_out_low','joint_hand_inside_release']
        joint_num_state=left_joint_total[joint_num]
        if joint_num_state=='joint_1_up':
            return [-1.2175465822219849, -1.9326857328414917, 1.277530312538147, 0.19142229855060577, 0.5448440909385681, 0.13077190518379211, 0.5889006853103638]
        if joint_num_state=='joint_1_down':
            return [-1.405513882637024, -1.9171849489212036, 1.284825086593628, -0.20881244540214539, 0.037473250180482864, 0.3338181972503662, 1.1445248126983643]
        if joint_num_state=='joint_2_up':
            return [-0.896358847618103, -1.9419759511947632, 1.2656543254852295, 0.4356665313243866, 0.7266150712966919, 0.2309715449810028, 0.2851850390434265]
        if joint_num_state=='joint_2_down':
            return [-1.3363401889801025, -1.0898970365524292, 1.4443535804748535, 0.44336768984794617, -3.420609474182129, 0.9420353174209595, -3.018526554107666]
        if joint_num_state=='joint_3_up':
            return [-1.5009297132492065, -1.011546015739441, 1.440324068069458, 0.5672059655189514, -3.490061044692993, 1.2173329591751099, -3.0692217350006104]
        if joint_num_state=='joint_3_down':
            return [-1.5736968517303467, -1.0619909763336182, 1.5524935722351074, 0.45445170998573303, -3.3969733715057373, 1.1540648937225342, -3.0895192623138428]
        if joint_num_state=='joint_4_up':
            return [-1.547721982,-0.975123584,1.425058126,0.427137256,-3.43200016,1.116520643,-3.086297512]
        if joint_num_state=='joint_4_down':
            return [-1.6134154797,-1.032587409,1.5367376804,0.3015876412,-3.3316938877,1.0310608149,-3.1173522472]
        if joint_num_state=='joint_5_up':
            return [-1.6798139811,-0.9578893185,1.4970027208,0.4048714936,-3.4262340069,1.2005531788,-3.1135492325]
        if joint_num_state=='joint_5_down':
            return [-1.7620639801,-1.0336602926,1.6182199717,0.2667441964,-3.315778017,1.1212291718,-3.1433637142]
        if joint_num_state=='joint_hand_out_low':
            return [-1.596020221710205, -0.7798439860343933, 1.2379815578460693, -0.14349110424518585, -3.9499971866607666, 0.8009695410728455, -2.5808541774749756]
        if joint_num_state=='joint_hand_inside_release':
            return [-0.42854681611061096, -1.3110144138336182, 1.4462252855300903, 0.8245474696159363, -2.740112543106079, 0.45960697531700134, -3.49589467048645]
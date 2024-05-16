from python.TLE_ import TLE

def TLE_data_to_dict(name, line1, line2):
    TLE_data = dict()
    
    line1 = line1.split()
    line2 = line2.split()

    TLE_data['name'] = name
    TLE_data['NORAD ID'] = line1[1]
    TLE_data['International designation ID'] = line1[2]
    TLE_data['Epoch'] = line1[3]
    TLE_data['First time derivative of the mean motion'] = line1[4]
    TLE_data['Second time derivative of mean motion'] = line1[5]
    TLE_data['BSTAR drag term'] = line1[6]
    TLE_data['Ephemeris type'] = line1[7]
    TLE_data['Element set number'] = line1[8]

    TLE_data['Inclination'] = line2[2]
    TLE_data['Right ascension of the ascending node'] = line2[3]
    TLE_data['Eccentricity'] = line2[4]
    TLE_data['Argument of perigee'] = line2[5]
    TLE_data['Mean anomaly'] = line2[6]
    TLE_data['Mean motion'] = line2[7]

    TLE_data['line1'] = '\t'.join(line1)
    TLE_data['line2'] = '\t'.join(line2)

    try:
        TLE_data['Revolution count at epoch'] = line2[8]
    except:
        TLE_data['Revolution count at epoch'] = None

    return TLE_data

def TLE_obj_from_file(file_name):
    
    TLE_objs = []

    with open(file_name, 'r') as file:
        line = file.readlines()

        i = 0
        while 1:

            if line[i][0] != '1' and line[i][0] != '2' and line[i][0] != '\n':

                TLE_objs.append(TLE(TLE_data_to_dict(line[i],line[i+1],line[i+2])))
                i += 1

            else: i+=1

            if i >= len(line):
                break


    return TLE_objs

if __name__ == '__main__':
    TLE_objs = TLE_obj_from_file('TLE_ISS_Live.txt')
    for obj in TLE_objs:
        print(obj)
        # print(obj.epoch_to_utc(dict=True))
        print('\n')
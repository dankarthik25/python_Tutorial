# Given :
# There are Three Pole : P_source, P_temporary, P_destination.
# In pole P_source : There are N disk disk from large diamer(N) to small(1) from bottom to top respectively

# Aim:              : To Move all disk from P_source to P_destination
# CONDTION:         : Larger Disk can't disk on the smallar disk
# movedisk(ps, pd)  : only if  d_source < d_destionation
# movetower(ps,pd)  : if No of disk in ps is odd: then top disk should be moved to pd
#                   : by tower wise moments
# moveddisk(1,ps,pd),movedisk(2,ps,pt)> movetower(1,pd,pt)(ch 2),
# movedisk(3,ps,pd) > moveTower(2,pt,pd)(ch 3),movedisk(4,ps,pt)> movetower(3,pd,pt)(ch 4)
# movedisk(5,ps,pd) > moveTower(4,pt,pd)(ch 5),movedisk(6,ps,pt)> moveTower(7,pd,pt)..........

# For  above we can say :
#                     N   tower a pd
#                     N-1 tower a pt
#                     N-2 tower a ps
#                     N-3 tower a pd
# Work :
#       show Towers
#       movedisk(ps,pd) in graphical view (using for loop)
#       study move disk: try to find condtion
#           : odd disk move top top to des or vice versa only if des has disk larger
#           : revised : if size(top disk) in des pole is in between size[topDisk, bottomDisk] of source then
#           : then


class Pole:
    def __init__(self, name, list):
        self.name = name
        self.disk = list

    def showTowers(p_s, p_t, p_d, n):
        p_empty = ['|']
        l1 = [ps, pt, pd]
        for idx in l1:
            if idx.name == 'ps':
                sp_s = (n - len(idx.disk)) * p_empty + idx.disk
                # print(sp_s)
        for idx in l1:
            if idx.name == 'pd':
                sp_d = (n - len(idx.disk)) * p_empty + idx.disk
                # print(sp_d)
        for idx in l1:
            if idx.name == 'pt':
                sp_t = (n - len(idx.disk)) * p_empty + idx.disk
                # print(sp_t)

        # ls = len(p_s.disk)
        # lt = len(p_t.disk)
        # ld = len(p_d.disk)
        #
        # sp_t = (n - lt) * p_empty + p_t.disk
        # sp_d = (n - ld) * p_empty + p_d.disk
        for i in range(0, n):
            print ("\t " + str(sp_s[i]) + '\t' + str(sp_t[i]) + "\t" + str(sp_d[i]))
        print(" " * 9 + "-" * 16)

    def move(p1, p2):
        # pstr = ''
        p2.disk.insert(0, p1.disk[0])
        del p1.disk[0]
        pstr = "Disk " + str(p2.disk[0]) + ': is moved from ' + p1.name + ' to ' + p2.name
        return p1, p2, pstr

    def diskSize_conditon2move(p1, p2):
        pstr = "Disk Size CONDTION : "
        if len(p2.disk) == 0:
            c = True
            pstr += "Pole " + p2.name + "is empty so Disk " + str(p1.disk[0]) + ' from ' + p1.name + ' can put on the top of ' + p2.name
        else:
            if(p2.disk[0] > p1.disk[0]):
                c = True
                pstr += " Can Move Disk" + str(p1.disk[0]) + ' from ' + p1.name + ' to ' + p2.name
            else:
                c = False
                pstr += " Can't Move Disk" + str(p1.disk[0]) + ' from ' + p1.name + ' to ' + p2.name
        return c, pstr


# odd disk move top top to des or vice versa only if des has disk larger
# revised : if size(top disk) in des pole is in between size[topDisk, bottomDisk] of source then
# then

    def towemove_condition2move(p_s, p_t, p_d):
        dd_idx = -1
        if len(p_d.disk) == 0:                  # directly move tower ps to pd
            c = True
            pstr += "Pole " + p_d.name + "is empty so Tower from " + p_s.name + ' can put on the top of ' + p_d.name
            # makeAtower(p_s, , pd)  can be done a normal
        else:
            # top disk of P_d is larger than bottom of disk of P_s
            if (p_d.disk[0] > p_s.disk[-1]):    # directly move tower ps to pd
                c = True
                pstr += " Pole " + p_d.name + "has disk larger than " + p_s.name + 'disk, We can put on the top of ' + p_d.name
            else:
                # P_d has unwnated tower which is size  (less the tower size of P_s) at d_idx which is has to calculated
                # We have to move unwanted TOWER
                # moveTower(source = P_d[0:d_idx],temp = P_s, destination = P_other)
                c = False
                idx = 0
                d_idx = 0
                for disk in p_d.disk:
                    if disk < p_s.disk[-1]:
                        d_idx = idx
                        print(d_idx, idx)
                    else:
                        break
                    idx += 1
                pstr += " Pole " + p_d.name + "has unwanted tower of size" + p_d.disk[d_idx] + 'disk, We can\'t put on the top of ' + p_d.name
            return c, pstr, d_idx

    def makeAtower(p_s, p_t, p_d, n, sd_idx):
        print("-- Make A Tower : p_s = " + p_s.name + ", p_t= " + p_t.name + ", p_d = " + p_d.name)
        while input("Type: STOP") != "STOP":
            print('|-- makeAtower LOOP:')
            if sd_idx >= 0:
                if (sd_idx % 2 == 1):  # condtion: move disk from source_pole to destiantion/temorayr_pole
                    # odd No of disk move to P_destination
                    c, str, t_idx = Pole.towemove_condition2move(p_s, p_t, p_d)
                    print("|--" + str)
                    if c:       # condtion move disk from source / move Tower to other pole
                        p_s, p_d, pstr = Pole.move(p_s, p_d)
                        sd_idx -= 1
                        print(pstr)
                        Pole.showTowers(p_s, p_t, p_d, n)
                    else:
                        p_d, p_s, p_s

                        p_d, p_s, p_t = Pole.makeAtower(p_d, p_s, p_t, n, t_idx)
                        Pole.showTowers(p_s, p_t, p_d, n)
                        c, str, t_idx2 = Pole.towemove_condition2move(p_s, p_t, p_d)
                        sd_idx = t_idx2

                else:

                    # Even No Disk move to P_temporary
                    c, str = Pole.diskSize_conditon2move(p_s, p_t)
                    print("|--" + str)
                    if c:
                        p_s, pt, pstr = Pole.move(p_s, p_t)
                        print(pstr)
                        Pole.showTowers(p_s, p_t, p_d, n)
                    else:
                        p_t, p_s, p_d = Pole.makeAtower(p_t, p_s, p_d)
                        Pole.showTowers(p_s, p_t, p_d, n)
                    return ps, pt, pd
            else:
                print("-- COMPLETED: Tower is moved")
                break

        Pole.showTowers(p_s, p_t, p_d, n)
        return p_s, p_t, p_d


def Element_ps2pd(p_s, p_t, p_d, n):
    print("|- Element_ps2pd")
    print("|- P_source:" + p_s.name + ", P_temporary: " + p_t.name + ", P_destination:" + p_d.name)
    if (len(p_s.disk) % 2 == 1)and(len(p_s.disk) > 0):
        # odd No of disk move to P_destination
        if Pole.diskSize_conditon2move(p_s, p_d):
            # if P_destination is able to disk
            p_s, p_d = Pole.move(p_s, p_d)
        else:

            # P_destination as small disk so entire disk's should to moved to P_temporary then p_source are assigned to P_destination
            # Logic:
                # source is change to the P_destination
                # destination is chante to P_temporary
                # CONSTRUCT : A TOWER at P_temporary
                            # source for construction tower are from: P_destination
                            # destation for construction tower is : P_temporary
            p_d, p_s, p_s = makeAtower(p_d, p_s, p_t)
            print('-- out of loop')
    else:
        # Even No Disk move to P_temporary
        if Pole.diskSize_conditon2move(p_s, p_t):
            Pole.move(p_s, p_t)
        else:
            # Simillar to the above total_ps2pd case :
            # P_temporary as small disk so entire disk's should to moved to P_destination then p_source are assigned to P_temporary
            # Logic:
                # source is change to the P_temporary
                # destination is chante to source
                # CONSTRUCT : A TOWER at P_temporary
                            # source for construction tower are from: P_temporary
                            # destation for construction tower is : P_destination
            p_t, p_s, p_d = makeAtower(p_t, p_s, p_d)
            return ps, pt, pd


def total_ps2pd(ps, pt, pd, n):
    while input("Type: STOP") != "STOP":
        print('TOTAL_ps2pd LOOP BECAUSE P_D IS FULL NEED TO EMPTY')
        if len(ps.disk) > 0:
            print('- The lenght of P_source : ' + str(len(ps.disk)))
            ps, pt, pd = Element_ps2pd(ps, pt, pd, n)
        elif len(pt.disk) > 0:
            pt, ps, pd = Element_ps2pd(pt, ps, pd, n)
        else:
            print("- COMPLETED: Break total_ps2pd")
            break
        Pole.showTowers(ps, pt, pd, n)


n = 4
ps = Pole('ps', list(range(1, n+1)))
pt = Pole('pt', [])
pd = Pole('pd', [])
print('Before')
Pole.showTowers(ps, pt, pd, n)
# total_ps2pd(ps, pt, pd, n)

# ps = Pole('ps', [4])
# pt = Pole('pt', [1, 3])
# pd = Pole('pd', [2])
# print('Befor:')
# Pole.showTowers(ps, pt, pd, n)
pt, ps, pd = Pole.makeAtower(pt, ps, pd, n, len(pt.disk))
# if len(ps.disk) > 0:
#     ps2pd(ps, pt, pd, n)
# elif len(pt.disk) > 0:
#     ps2pd(pt, ps, pd, n)
# else:
#     print("COMPLETED")
#     break
# Pole.showTowers(ps, pt, pd, n)

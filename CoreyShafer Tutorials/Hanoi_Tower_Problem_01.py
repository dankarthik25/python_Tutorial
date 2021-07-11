class Pole:
    def __init__(self, name, Nodisk, list):
        self.name = name
        self.Nodisk = Nodisk
        self.disk = list

    def showTowers(p_s, p_t, p_d):
        p_empty = ['|']
        l1 = [p_s, p_t, p_d]
        for idx in l1:
            if idx.name == 'ps':
                sp_s = (idx.Nodisk - len(idx.disk)) * p_empty + idx.disk
        for idx in l1:
            if idx.name == 'pd':
                sp_d = (idx.Nodisk - len(idx.disk)) * p_empty + idx.disk
        for idx in l1:
            if idx.name == 'pt':
                sp_t = (idx.Nodisk - len(idx.disk)) * p_empty + idx.disk
        for i in range(0, idx.Nodisk):
            print ("\t " + str(sp_s[i]) + '\t' + str(sp_t[i]) + "\t" + str(sp_d[i]))
        print(" " * 9 + "-" * 16)

    def move(p_s, p_d):
        if (len(p_s.disk) > 0):
            # pstr = ''
            p_d.disk.insert(0, p_s.disk[0])
            del p_s.disk[0]
            pstr = "Disk " + str(p_d.disk[0]) + ': is moved from  Pole ' + p_s.name + ' to Ploe ' + p_d.name
        return p_s, p_d, pstr


def towers(p_s, p_t, p_d, n):
    if n == 1:
        print('Move disk.No {} from pole {} to pole {}'.format(n, p_s.name, p_d.name))
        p_s, p_d, pstr = Pole.move(p_s, p_d)
        print(pstr)
        Pole.showTowers(p_s, p_t, p_d)
    else:
        # Move (N-1) disk's or tower (N-1) from P_s to P_t
        towers(p_s, p_d, p_t, n - 1)
        # Move Nth Disk from Ps to Pd
        print('Move disk.No {} from pole {} to pole {}'.format(n, p_s.name, p_d.name))
        p_s, p_d, pstr = Pole.move(p_s, p_d)
        print(pstr)
        Pole.showTowers(p_s, p_t, p_d)
        # # Ps is empty Nth disk is moved to P_d and remaining are in tower on P_t
        # We have to move tower at P_t TO P_d simillar to P_s
        towers(p_t, p_s, p_d, n - 1)


n = 4
ps = Pole('ps', n, list(range(1, n + 1)))
pt = Pole('pt', n, [])
pd = Pole('pd', n, [])
Pole.showTowers(ps, pt, pd)
towers(ps, pt, pd, n)
# print(ps)
# print('Name', ps.name)
# print('No.of Disk', ps.Nodisk)
# print('Disk list', ps.disk)

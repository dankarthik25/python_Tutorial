# # import pickle
# #
# # imelda = ('More Mayhem', 'Imelda MAy', '2011', ((1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')))
# #
# # with open("imelda.pickle","wb") as pickle_file:
# #     pickle.dump(imelda,pickle_file)
# #
# #
# # # To retrive the file from imelda.pickle
# #
# # with open("imelda.pickle","rb") as imelda_pickled:
# #     imelda2 = pickle.load(imelda_pickled)
# #
# # print(imelda2)
#
#
# import  pickle
# imelda = ('More Mayhem', 'Imelda MAy', '2011', ((1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')))
# even = list(range(0,10,2))
# odd = list(range(1,10,2))
#
#
# with open("imelda.pickle","wb") as pickle_file:
#     pickle.dump(imelda,pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
#     pickle.dump(even, pickle_file, protocol=0)
#     pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
#     pickle.dump(2998302, pickle_file, protocol=0)
#
#
# # To retrive the file from imelda.pickle
#
# with open("imelda.pickle","rb") as imelda_pickled:
#     imelda2 = pickle.load(imelda_pickled)
#     even_list = pickle.load(imelda_pickled)
#     old_list = pickle.load(imelda_pickled)
#     x = pickle.load(imelda_pickled)
# #  pickle will store the type of protocol it used to load
# # 0 is most human read able
# # In before version py2  the perfomed safty check unpickling, py would refuse to call functions and class constructors which are marke not marked for pickling which are removed in py2
# # we can say is not secure in pickle but the job is good
#
# print(imelda2)
# print(even_list)
# print (old_list)
# print(x)
#
#
#
#
#
#
pickle.load(b"cos\nsystem\n(S' rm imelda.pickle'\ntR")

# https://docs.python.org/3/library/pickle.html
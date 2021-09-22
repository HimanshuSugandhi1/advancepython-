import argparse
parser=argparse.ArgumentParser()

parser.add_argument('-s',action='store',dest='simple_value',help='store simple value')
parser.add_argument('-c',action='store_const',dest='const_value',const="100",help='store simple value')
parser.add_argument('-t',action='store_true',dest='boolean_Switch',default=False, help='set a switch to true')
parser.add_argument('-f',action='store_false',dest='boolean_Switch',default =False,help='set a switch to false')
parser.add_argument('-a',action='append',dest='collection',default=[],help='add repeated value to list')
parser.add_argument('-A',action='append_const',dest='const_collection',const='value-1 to append',help="Add different values to list")

parser.add_argument('--version',action='version',version='1.0')

result=parser.parse_args()
print('simple_value =', result.simple_value)
print('const value =',result.const_value)
print('boolean_switch =', result.boolean_Switch)
print('collection =',result.collection)
print('const_collection =',result.const_collection)


